"""Office-video thumbnail: the logo card (copper mark, serif LawWorld, tagline on cream) with the presenter cut out below it.

Steps (from product-explainer/):
  ffmpeg -ss 4.14 -i downloads/office/o03.mp4 -frames:v 1 -vf scale=1440:2560:flags=lanczos frame.png
  swift thumbnail/person_mask.swift frame.png mask.png
  python3 thumbnail/build_thumb.py frame.png mask.png brand <out_stem> glow|disc

Usage: python3 build_thumb.py <frame.png> <person_mask.png> <brand_dir> <out_stem> [variant]
  frame.png        presenter frame upscaled to 1440x2560 (raw Flow clip is 720x1280)
  person_mask.png  Vision person mask at the same size (person_mask.swift)
  variant          glow | disc   (backdrop behind the presenter)
"""
import sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1920
CREAM = (245, 239, 230)
PEACH = (243, 224, 210)
INK = (31, 30, 29)
ACCENT = (204, 120, 92)

# presenter crop in the 1440x2560 frame: head top (775) down to just above the desk plant's leaves (1690)
CROP_TOP, CROP_BOTTOM = 745, 1690
SCALE = 1.06


def radial(size, center, radius, color, strength):
    """Alpha-blended radial glow layer (RGBA)."""
    w, h = size
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt((xx - center[0]) ** 2 + (yy - center[1]) ** 2) / radius
    a = np.clip(1 - d, 0, 1) ** 1.6 * strength
    layer = np.zeros((h, w, 4), np.uint8)
    layer[..., :3] = color
    layer[..., 3] = (a * 255).astype(np.uint8)
    return Image.fromarray(layer, "RGBA")


def background():
    bg = Image.new("RGBA", (W, H), CREAM + (255,))
    bg.alpha_composite(radial((W, H), (900, 260), 900, PEACH, 0.9))
    bg.alpha_composite(radial((W, H), (540, 520), 520, (250, 246, 239), 0.7))
    return bg


def shadow(alpha, blur, opacity, color=(70, 45, 35)):
    a = alpha.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * opacity))
    s = Image.new("RGBA", alpha.size, color + (0,))
    s.putalpha(a)
    return s


def clean_wordmark(path):
    """The brochure wordmark carries a faint near-white box; rebuild alpha from ink darkness."""
    src = np.array(Image.open(path).convert("RGBA")).astype(float)
    # the box is ink at alpha 1-30; glyph edges are kept by restretching what lies above that floor
    a = np.clip((src[..., 3] - 34) / (255 - 34), 0, 1)
    out = np.zeros(a.shape + (4,), np.uint8)
    out[..., :3] = INK
    out[..., 3] = (a * 255).astype(np.uint8)
    im = Image.fromarray(out, "RGBA")
    return im.crop(im.getbbox())


def presenter(frame_path, mask_path):
    im = Image.open(frame_path).convert("RGB")
    m = Image.open(mask_path).convert("L")
    # tighten and feather the edge so no office wall shows as a halo
    # Vision leaves a wide soft band where the jacket meets the dark shelf; restretch it, then choke and feather
    m = m.point(lambda v: max(0, min(255, round((v - 125) * 255 / (225 - 125)))))
    m = m.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.4))
    box = (0, CROP_TOP, im.width, CROP_BOTTOM)
    im, m = im.crop(box), m.crop(box)
    size = (round(im.width * SCALE), round(im.height * SCALE))
    im = im.resize(size, Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2, percent=55, threshold=2))
    m = m.resize(size, Image.LANCZOS)
    p = im.convert("RGBA")
    p.putalpha(m)
    return p


def tagline(fonts_dir, size):
    reg = ImageFont.truetype(f"{fonts_dir}/Instrument_Serif_jizBRFtNs2ka5fXjeivQ4LroWlx-6zUTjnTLgNs.woff2", size)
    ita = ImageFont.truetype(f"{fonts_dir}/Instrument_Serif_jizHRFtNs2ka5fXjeivQ4LroWlx-6zAjjH7Motmp5g.woff2", size)
    parts = [("The all-in-one ", reg, INK), ("AI platform", ita, ACCENT), (" for advocates", reg, INK)]
    widths = [f.getlength(t) for t, f, _ in parts]
    img = Image.new("RGBA", (int(sum(widths)) + 20, int(size * 1.5)), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    x = 10
    for (t, f, c), w in zip(parts, widths):
        d.text((x, size * 0.15), t, font=f, fill=c + (255,))
        x += w
    return img.crop(img.getbbox())


def main():
    frame, mask, brand, stem = sys.argv[1:5]
    variant = sys.argv[5] if len(sys.argv) > 5 else "glow"
    canvas = background()

    # logo block
    mark = Image.open(f"{brand}/mark_copper_512.png").convert("RGBA").resize((262, 262), Image.LANCZOS)
    mx, my = (W - mark.width) // 2, 170
    sh = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sh.paste(mark, (mx, my + 14))
    canvas.alpha_composite(shadow(sh.getchannel("A"), 22, 0.30))
    canvas.alpha_composite(mark, (mx, my))

    word = clean_wordmark(f"{brand}/wordmark_ink.png")
    word = word.resize((690, round(word.height * 690 / word.width)), Image.LANCZOS)
    wy = my + mark.height + 62
    canvas.alpha_composite(word, ((W - word.width) // 2, wy))

    tag = tagline(f"{brand}/fonts", 62)
    ty = wy + word.height + 44
    canvas.alpha_composite(tag, ((W - tag.width) // 2, ty))

    # presenter, bottom-anchored
    p = presenter(frame, mask)
    px, py = (W - p.width) // 2, H - p.height
    head_cx, head_cy = W // 2, py + 330
    if variant == "disc":
        r = 470
        disc = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        dd = ImageDraw.Draw(disc)
        dd.ellipse((head_cx - r, head_cy - r + 120, head_cx + r, head_cy + r + 120), fill=(236, 205, 180, 255))
        dd.ellipse((head_cx - r, head_cy - r + 120, head_cx + r, head_cy + r + 120), outline=ACCENT + (255,), width=4)
        canvas.alpha_composite(disc)
    else:
        canvas.alpha_composite(radial((W, H), (head_cx, head_cy + 220), 640, (234, 200, 172), 0.75))
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    layer.paste(p, (px, py))
    canvas.alpha_composite(shadow(layer.getchannel("A"), 26, 0.22))
    canvas.alpha_composite(layer)

    out = canvas.convert("RGB")
    out.save(f"{stem}.png")
    out.save(f"{stem}.jpg", quality=92, optimize=True, progressive=True)
    print(stem, "tagline y", ty, "+", tag.height, "presenter top", py)


if __name__ == "__main__":
    main()
