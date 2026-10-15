"""Office-video thumbnail templates: the LawWorld logo card (copper mark, serif wordmark, tagline) with the presenter.

Steps (from product-explainer/):
  ffmpeg -ss 4.14 -i downloads/office/o03.mp4 -frames:v 1 -vf scale=1440:2560:flags=lanczos frame.png
  swift thumbnail/person_mask.swift frame.png mask.png
  python3 thumbnail/build_thumb.py frame.png mask.png brand <out_dir> [template ...]

Usage: python3 build_thumb.py <frame.png> <person_mask.png> <brand_dir> <out_dir> [template ...]
  frame.png        presenter frame upscaled to 1440x2560 (raw Flow clip is 720x1280)
  person_mask.png  Vision person mask at the same size (person_mask.swift)
  template         any of TEMPLATES (default: all); writes <out_dir>/<NN>_<name>.jpg + contact sheet

Copy is limited to the brand tagline, the site's feature names and lines from the video's own script.
"""
import math
import os
import sys
from functools import cached_property
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1080, 1920
CREAM = (245, 239, 230)
PAPER = (255, 252, 246)
PEACH = (243, 224, 210)
INK = (31, 30, 29)
ACCENT = (204, 120, 92)
ACCENT_LIGHT = (233, 163, 131)  # terracotta that still reads on dark grounds
ESPRESSO = (27, 20, 17)

# presenter crop in the 1440x2560 frame: head top (775) down to just above the desk plant's leaves (1690)
CROP_TOP, CROP_BOTTOM = 745, 1690
SCALE = 1.06
HEAD_OFFSET = 330  # head centre below the top of the scaled crop

SERIF = "Instrument_Serif_jizBRFtNs2ka5fXjeivQ4LroWlx-6zUTjnTLgNs.woff2"
SERIF_ITALIC = "Instrument_Serif_jizHRFtNs2ka5fXjeivQ4LroWlx-6zAjjH7Motmp5g.woff2"
SANS = "Manrope_xn7gYHE41ni1AdIRggexSvfedN4.woff2"  # latin subset, variable weight 200-800

# site feature names (owner's list) that the video also covers
FEATURES = [["LawChat", "Drafting", "Case laws"], ["Translation", "Your Cases", "Client Portal"]]


# ---------- primitives ----------

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


def linear(size, c0, c1, angle):
    """Opaque linear gradient, angle in degrees (0 = left to right, 90 = top to bottom)."""
    w, h = size
    yy, xx = np.mgrid[0:h, 0:w].astype(float)
    dx, dy = math.cos(math.radians(angle)), math.sin(math.radians(angle))
    t = xx * dx + yy * dy
    t = (t - t.min()) / (t.max() - t.min())
    out = np.zeros((h, w, 4), np.uint8)
    for i in range(3):
        out[..., i] = (c0[i] + (c1[i] - c0[i]) * t).astype(np.uint8)
    out[..., 3] = 255
    return Image.fromarray(out, "RGBA")


def shadow(alpha, blur, opacity, color=(70, 45, 35)):
    a = alpha.filter(ImageFilter.GaussianBlur(blur)).point(lambda v: int(v * opacity))
    s = Image.new("RGBA", alpha.size, color + (0,))
    s.putalpha(a)
    return s


def blank():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def paste_x(canvas, img, y, x=None):
    canvas.alpha_composite(img, ((W - img.width) // 2 if x is None else x, y))


class Kit:
    """Brand assets, and the presenter when a frame is given (logo-only cards pass none)."""

    def __init__(self, brand, frame=None, mask=None):
        self.brand = brand
        self.fonts = f"{brand}/fonts"
        self.mark_src = Image.open(f"{brand}/mark_copper_512.png").convert("RGBA")
        self.word_alpha = self._wordmark_alpha(f"{brand}/wordmark_ink.png")
        self.frame_path, self.mask_path = frame, mask

    @cached_property
    def frame(self):
        return Image.open(self.frame_path).convert("RGB")

    @cached_property
    def cutout(self):
        return self._presenter()

    # -- brand --
    @staticmethod
    def _wordmark_alpha(path):
        """The brochure wordmark carries a faint ink box (alpha 1-30); restretch what lies above that floor."""
        src = np.array(Image.open(path).convert("RGBA")).astype(float)
        a = Image.fromarray((np.clip((src[..., 3] - 34) / (255 - 34), 0, 1) * 255).astype(np.uint8), "L")
        return a.crop(a.getbbox())

    def wordmark(self, width, color=INK):
        a = self.word_alpha.resize((width, round(self.word_alpha.height * width / self.word_alpha.width)), Image.LANCZOS)
        im = Image.new("RGBA", a.size, color + (0,))
        im.putalpha(a)
        return im

    def mark(self, size):
        return self.mark_src.resize((size, size), Image.LANCZOS)

    def serif(self, size, italic=False):
        return ImageFont.truetype(f"{self.fonts}/{SERIF_ITALIC if italic else SERIF}", size)

    def sans(self, size, weight=700):
        f = ImageFont.truetype(f"{self.fonts}/{SANS}", size)
        f.set_variation_by_axes([weight])
        return f

    # -- text --
    def tagline(self, size, ink=INK, accent=ACCENT):
        reg, ita = self.serif(size), self.serif(size, True)
        parts = [("The all-in-one ", reg, ink), ("AI platform", ita, accent), (" for advocates", reg, ink)]
        widths = [f.getlength(t) for t, f, _ in parts]
        img = Image.new("RGBA", (int(sum(widths)) + 20, int(size * 1.5)), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        x = 10
        for (t, f, c), w in zip(parts, widths):
            d.text((x, size * 0.15), t, font=f, fill=c + (255,))
            x += w
        return img.crop(img.getbbox())

    @staticmethod
    def line(parts, tracking=0):
        """One line of mixed runs [(text, font, color)], baseline-aligned, cropped to the font's ascent/descent."""
        asc = max(f.getmetrics()[0] for _, f, _ in parts)
        desc = max(f.getmetrics()[1] for _, f, _ in parts)
        width = sum(f.getlength(t) + tracking * len(t) for t, f, _ in parts)
        img = Image.new("RGBA", (int(width) + 8, asc + desc), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        x = 4
        for t, f, c in parts:
            if tracking:
                for ch in t:
                    d.text((x, asc), ch, font=f, fill=c + (255,), anchor="ls")
                    x += f.getlength(ch) + tracking
            else:
                d.text((x, asc), t, font=f, fill=c + (255,), anchor="ls")
                x += f.getlength(t)
        return img

    def pill(self, text, size=34, fg=INK, bg=PAPER, dot=ACCENT, pad=(30, 18), outline=None):
        f = self.sans(size, 700)
        t = self.line([(text, f, fg)])
        dot_w = int(size * 0.62) if dot else 0
        w, h = t.width + pad[0] * 2 + dot_w, int(size * 1.0) + pad[1] * 2
        img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        d = ImageDraw.Draw(img)
        d.rounded_rectangle((0, 0, w - 1, h - 1), radius=h // 2, fill=bg + (255,), outline=outline, width=2 if outline else 0)
        if dot:
            r = size * 0.16
            cx, cy = pad[0] + r, h / 2
            d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=dot + (255,))
        img.alpha_composite(t, (pad[0] + dot_w, (h - t.height) // 2 + 1))
        return img

    # -- presenter --
    def _presenter(self):
        im, m = self.frame, Image.open(self.mask_path).convert("L")
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

    def presenter_layer(self, bottom=H):
        """Cut-out presenter on a full-canvas layer, bottom-anchored; returns (layer, head centre)."""
        p = self.cutout
        layer = blank()
        py = bottom - p.height
        layer.paste(p, ((W - p.width) // 2, py))
        return layer, (W // 2, py + HEAD_OFFSET)

    def office(self, scale, top):
        """The untouched office frame (desk, plant, hands) scaled to `scale` and placed with its top at `top`."""
        f = self.frame.resize((round(self.frame.width * scale), round(self.frame.height * scale)), Image.LANCZOS)
        f = f.filter(ImageFilter.UnsharpMask(radius=2, percent=45, threshold=2)).convert("RGBA")
        layer = blank()
        layer.paste(f, ((W - f.width) // 2, top))
        return layer


# ---------- shared blocks ----------

def cream_ground():
    bg = Image.new("RGBA", (W, H), CREAM + (255,))
    bg.alpha_composite(radial((W, H), (900, 260), 900, PEACH, 0.9))
    bg.alpha_composite(radial((W, H), (540, 520), 520, (250, 246, 239), 0.7))
    return bg


def logo_block(kit, canvas, top=170, mark=262, word=690, tag=62, dark=False):
    """Mark, wordmark and tagline stacked and centred, as on the video's opening card. Returns the bottom y."""
    m = kit.mark(mark)
    mx = (W - m.width) // 2
    sh = blank()
    sh.paste(m, (mx, top + 14))
    canvas.alpha_composite(shadow(sh.getchannel("A"), 22, 0.55 if dark else 0.30, (0, 0, 0) if dark else (70, 45, 35)))
    canvas.alpha_composite(m, (mx, top))
    wm = kit.wordmark(word, CREAM if dark else INK)
    wy = top + m.height + round(mark * 0.237)
    paste_x(canvas, wm, wy)
    t = kit.tagline(tag, CREAM if dark else INK, ACCENT_LIGHT if dark else ACCENT)
    ty = wy + wm.height + round(tag * 0.71)
    paste_x(canvas, t, ty)
    return ty + t.height


def lockup(kit, canvas, y, mark=88, word=300, color=INK):
    """Small horizontal mark + wordmark, centred."""
    m, wm = kit.mark(mark), kit.wordmark(word, color)
    gap = round(mark * 0.28)
    x = (W - (m.width + gap + wm.width)) // 2
    canvas.alpha_composite(m, (x, y))
    canvas.alpha_composite(wm, (x + m.width + gap, y + (m.height - wm.height) // 2 + 2))
    return y + m.height


def place_presenter(kit, canvas, glow=None, shadow_op=0.22, rim=None):
    layer, head = kit.presenter_layer()
    if glow:
        canvas.alpha_composite(radial((W, H), (head[0], head[1] + 220), 640, glow[0], glow[1]))
    if rim:  # warm light wrapping the silhouette, for dark grounds
        a = layer.getchannel("A").filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(28))
        r = Image.new("RGBA", (W, H), rim[0] + (0,))
        r.putalpha(a.point(lambda v: int(v * rim[1])))
        canvas.alpha_composite(r)
    canvas.alpha_composite(shadow(layer.getchannel("A"), 26, shadow_op))
    canvas.alpha_composite(layer)
    return head


def chip_rows(kit, canvas, rows, y, gap=18, row_gap=20, **pill_kw):
    for row in rows:
        pills = [kit.pill(t, **pill_kw) for t in row]
        total = sum(p.width for p in pills) + gap * (len(pills) - 1)
        x = (W - total) // 2
        for p in pills:
            sh = blank()
            sh.paste(p, (x, y + 8))
            canvas.alpha_composite(shadow(sh.getchannel("A"), 14, 0.35, (0, 0, 0)))
            canvas.alpha_composite(p, (x, y))
            x += p.width + gap
        y += pills[0].height + row_gap
    return y


# ---------- templates ----------

def t_glow(kit):
    c = cream_ground()
    logo_block(kit, c)
    place_presenter(kit, c, glow=((234, 200, 172), 0.75))
    return c


def t_disc(kit):
    c = cream_ground()
    logo_block(kit, c)
    _, (hx, hy) = kit.presenter_layer()
    r, cy = 470, hy + 120
    d = ImageDraw.Draw(c)
    d.ellipse((hx - r, cy - r, hx + r, cy + r), fill=(236, 205, 180, 255), outline=ACCENT + (255,), width=4)
    place_presenter(kit, c)
    return c


def t_noir(kit):
    c = linear((W, H), (20, 15, 13), (38, 26, 20), 90)
    c.alpha_composite(radial((W, H), (540, 420), 760, (92, 58, 42), 0.55))
    logo_block(kit, c, dark=True)
    _, (hx, hy) = kit.presenter_layer()
    c.alpha_composite(radial((W, H), (hx, hy + 260), 720, (205, 112, 76), 0.55))
    place_presenter(kit, c, shadow_op=0.0, rim=((240, 168, 128), 0.30))
    return c


def t_copper(kit):
    c = linear((W, H), (66, 36, 30), (186, 112, 76), 62)
    c.alpha_composite(radial((W, H), (540, 400), 700, (40, 22, 18), 0.45))
    logo_block(kit, c, dark=True)
    _, (hx, hy) = kit.presenter_layer()
    c.alpha_composite(radial((W, H), (hx, hy + 200), 640, (250, 232, 214), 0.70))
    place_presenter(kit, c, shadow_op=0.30)
    return c


def t_office(kit):
    c = Image.new("RGBA", (W, H), CREAM + (255,))
    top = 390
    c.alpha_composite(kit.office(0.75, top))
    # cream melts into the office wall above his head
    fade = np.zeros((H, W, 4), np.uint8)
    fade[..., :3] = CREAM
    solid = top + 250  # cover the ceiling strip under the logo, then reveal the wall down to his head
    t = np.clip((np.arange(H) - solid) / 360.0, 0, 1)
    ramp = 1 - t * t * (3 - 2 * t)  # smoothstep: no visible line where the fade begins
    fade[..., 3] = (ramp[:, None] * 255).astype(np.uint8)
    c.alpha_composite(Image.fromarray(fade, "RGBA"))
    logo_block(kit, c, top=110, mark=220, word=600, tag=56)
    return c


def t_arch(kit):
    c = cream_ground()
    logo_block(kit, c, top=110, mark=200, word=580, tag=54)
    x0, x1, top = 120, 960, 860
    r = (x1 - x0) // 2
    mask = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(mask)
    d.ellipse((x0, top, x1, top + 2 * r), fill=255)
    d.rectangle((x0, top + r, x1, H), fill=255)
    room = kit.office(0.8, 330)
    win = blank()
    win.paste(room, (0, 0), mask)
    c.alpha_composite(shadow(mask, 30, 0.28))
    c.alpha_composite(win)
    o = ImageDraw.Draw(c)
    g = 16  # thin copper line echoing the arch
    o.arc((x0 - g, top - g, x1 + g, top + 2 * r + g), 180, 360, fill=ACCENT + (255,), width=3)
    o.line((x0 - g, top + r, x0 - g, H), fill=ACCENT + (255,), width=3)
    o.line((x1 + g, top + r, x1 + g, H), fill=ACCENT + (255,), width=3)
    return c


def t_hook(kit):
    c = cream_ground()
    lockup(kit, c, 110)
    size = 116
    lines = [
        [("If you are an", kit.serif(size), INK)],
        [("advocate", kit.serif(size, True), ACCENT), (",", kit.serif(size), INK)],
        [("this video is for you.", kit.serif(size), INK)],
    ]
    y = 300
    for parts in lines:
        im = kit.line(parts)
        if im.width > 980:
            im = im.resize((980, round(im.height * 980 / im.width)), Image.LANCZOS)
        paste_x(c, im, y)
        y += round(size * 1.02)
    place_presenter(kit, c, glow=((234, 200, 172), 0.75))
    return c


def t_features(kit):
    c = cream_ground()
    logo_block(kit, c, top=130, mark=230, word=640, tag=58)
    place_presenter(kit, c, glow=((234, 200, 172), 0.75))
    label = kit.line([("15+ FEATURES IN ONE PLATFORM", kit.sans(36, 800), PAPER)], tracking=4)
    y = 1520
    badge = Image.new("RGBA", (label.width + 56, label.height + 26), (0, 0, 0, 0))
    ImageDraw.Draw(badge).rounded_rectangle((0, 0, badge.width - 1, badge.height - 1), radius=badge.height // 2, fill=ACCENT + (255,))
    badge.alpha_composite(label, (28, 13))
    paste_x(c, badge, y)
    chip_rows(kit, c, FEATURES, y + badge.height + 24, size=40, gap=16, row_gap=18)
    return c


def t_founder(kit):
    c = cream_ground()
    logo_block(kit, c, top=150, mark=240, word=660, tag=60)
    place_presenter(kit, c, glow=((234, 200, 172), 0.75))
    name = kit.line([("Ravishankar", kit.serif(84), INK)])
    role = kit.line([("FOUNDER, LAWWORLD", kit.sans(28, 800), ACCENT)], tracking=5)
    w = max(name.width, role.width) + 120
    h = name.height + role.height + 50
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle((0, 0, w - 1, h - 1), radius=22, fill=PAPER + (250,))
    d.rectangle((0, 22, 8, h - 23), fill=ACCENT + (255,))
    card.alpha_composite(name, ((w - name.width) // 2, 14))
    card.alpha_composite(role, ((w - role.width) // 2, 14 + name.height + 12))
    y = 1650
    sh = blank()
    sh.paste(card, ((W - w) // 2, y + 12))
    c.alpha_composite(shadow(sh.getchannel("A"), 22, 0.45, (0, 0, 0)))
    paste_x(c, card, y)
    return c


def t_twotone(kit):
    c = Image.new("RGBA", (W, H), CREAM + (255,))
    split = 1240
    top = linear((W, split), (24, 20, 18), (44, 32, 26), 90)
    top.alpha_composite(radial((W, split), (540, 330), 700, (96, 60, 44), 0.5))
    c.alpha_composite(top)
    logo_block(kit, c, top=120, mark=230, word=640, tag=58, dark=True)
    _, (hx, hy) = kit.presenter_layer()
    r, cy = 430, hy + 110
    d = ImageDraw.Draw(c)
    d.ellipse((hx - r, cy - r, hx + r, cy + r), fill=(238, 208, 184, 255))
    d.ellipse((hx - r - 18, cy - r - 18, hx + r + 18, cy + r + 18), outline=ACCENT_LIGHT + (255,), width=3)
    place_presenter(kit, c)
    return c


TEMPLATES = {
    "glow": t_glow,
    "disc": t_disc,
    "noir": t_noir,
    "copper": t_copper,
    "office": t_office,
    "arch": t_arch,
    "hook": t_hook,
    "features": t_features,
    "founder": t_founder,
    "twotone": t_twotone,
}


def contact_sheet(paths, out, cols=5, tile=(324, 576), gap=24):
    rows = (len(paths) + cols - 1) // cols
    label_h = 46
    sheet = Image.new("RGB", (cols * tile[0] + (cols + 1) * gap, rows * (tile[1] + label_h) + (rows + 1) * gap), (232, 226, 216))
    d = ImageDraw.Draw(sheet)
    try:
        f = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 26)
    except OSError:
        f = ImageFont.load_default()
    for i, p in enumerate(paths):
        x = gap + (i % cols) * (tile[0] + gap)
        y = gap + (i // cols) * (tile[1] + label_h + gap)
        sheet.paste(Image.open(p).convert("RGB").resize(tile, Image.LANCZOS), (x, y))
        d.text((x + 4, y + tile[1] + 10), os.path.splitext(os.path.basename(p))[0], font=f, fill=INK)
    sheet.save(out, quality=90)


def main():
    frame, mask, brand, out_dir = sys.argv[1:5]
    names = sys.argv[5:] or list(TEMPLATES)
    os.makedirs(out_dir, exist_ok=True)
    kit = Kit(brand, frame, mask)
    order = list(TEMPLATES)
    paths = []
    for name in names:
        img = TEMPLATES[name](kit).convert("RGB")
        path = f"{out_dir}/{order.index(name) + 1:02d}_{name}.jpg"
        img.save(path, quality=92, optimize=True, progressive=True)
        paths.append(path)
        print(path)
    if len(paths) > 1:
        contact_sheet(paths, f"{out_dir}/00_all_templates.jpg")


if __name__ == "__main__":
    main()
