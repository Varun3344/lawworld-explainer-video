"""Logo-only thumbnail cards (no presenter photo): copper mark + serif LawWorld with the tagline as the hero.

Usage (from product-explainer/): python3 thumbnail/build_card.py brand <out_dir> [template ...]
Writes <out_dir>/<NN>_<name>.jpg for each template (default: all) and 00_all_cards.jpg.
The only copy is the brand tagline "The all-in-one AI platform for advocates".
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PIL import Image, ImageDraw  # noqa: E402

from build_thumb import (  # noqa: E402
    ACCENT, ACCENT_LIGHT, CREAM, H, INK, PAPER, PEACH, W, Kit, blank, contact_sheet, linear, paste_x, radial, shadow,
)

COPPER_INK = ((112, 56, 42), (212, 126, 84))  # logo gradient, darkened enough to read on cream
COPPER_GLOW = ((250, 204, 170), (222, 140, 96))  # the same gradient lifted for dark grounds
MARKER = (243, 208, 184)


# ---------- pieces ----------

def ground(halo_y, dark=False, copper=False):
    if copper:
        c = linear((W, H), (64, 35, 29), (184, 110, 74), 62)
        c.alpha_composite(radial((W, H), (540, halo_y), 640, (36, 20, 16), 0.45))
    elif dark:
        c = linear((W, H), (20, 15, 13), (40, 28, 22), 90)
        c.alpha_composite(radial((W, H), (540, halo_y), 760, (110, 66, 46), 0.60))
    else:
        c = Image.new("RGBA", (W, H), CREAM + (255,))
        c.alpha_composite(radial((W, H), (900, 260), 900, PEACH, 0.9))
        c.alpha_composite(radial((W, H), (540, halo_y), 560, (250, 246, 239), 0.75))
    return c


def head(kit, c, top, mark=300, word=700, light=False):
    """Mark with its soft shadow and the wordmark under it; returns the bottom y."""
    m = kit.mark(mark)
    mx = (W - m.width) // 2
    sh = blank()
    sh.paste(m, (mx, top + 16))
    c.alpha_composite(shadow(sh.getchannel("A"), 26, 0.55 if light else 0.30, (0, 0, 0) if light else (70, 45, 35)))
    c.alpha_composite(m, (mx, top))
    wm = kit.wordmark(word, CREAM if light else INK)
    wy = top + m.height + round(mark * 0.22)
    paste_x(c, wm, wy)
    c.mark_cy = top + mark // 2
    return wy + wm.height


def text(parts, tracking=0, max_w=960):
    im = Kit.line(parts, tracking)
    im = im.crop(im.getbbox())
    if im.width > max_w:
        im = im.resize((max_w, round(im.height * max_w / im.width)), Image.LANCZOS)
    return im


def gradient_text(s, font, colors, max_w=960):
    a = text([(s, font, (255, 255, 255))], max_w=max_w)
    g = linear(a.size, colors[0], colors[1], 0)
    g.putalpha(a.getchannel("A"))
    return g


def star(size, color, k=2.4):
    """The logo's four-point star (concave sides), anti-aliased."""
    n = size * 4
    pts = []
    for i in range(720):
        t = math.radians(i / 2)
        x = math.copysign(abs(math.cos(t)) ** k, math.cos(t))
        y = math.copysign(abs(math.sin(t)) ** k, math.sin(t))
        pts.append((n / 2 + x * n / 2, n / 2 + y * n / 2))
    a = Image.new("L", (n, n), 0)
    ImageDraw.Draw(a).polygon(pts, fill=255)
    out = Image.new("RGBA", (size, size), color + (0,))
    out.putalpha(a.resize((size, size), Image.LANCZOS))
    return out


def starred(label, star_color, gap=26):
    s = star(round(label.height * 1.25), star_color)
    out = Image.new("RGBA", (label.width + 2 * (s.width + gap), max(label.height, s.height)), (0, 0, 0, 0))
    out.alpha_composite(s, (0, (out.height - s.height) // 2))
    out.alpha_composite(label, (s.width + gap, (out.height - label.height) // 2))
    out.alpha_composite(s, (out.width - s.width, (out.height - s.height) // 2))
    return out


def marker_behind(word_img, color, alpha=235):
    """Highlighter stroke across the lower half of a word, slightly tilted, word on top."""
    w, h = word_img.width + 60, round(word_img.height * 0.42)
    band = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(band).rounded_rectangle((0, 0, w - 1, h - 1), radius=h // 2, fill=color + (alpha,))
    band = band.rotate(1.6, resample=Image.BICUBIC, expand=True)
    out = Image.new("RGBA", (max(band.width, word_img.width), word_img.height + 10), (0, 0, 0, 0))
    out.alpha_composite(band, ((out.width - band.width) // 2, round(word_img.height * 0.50)))
    out.alpha_composite(word_img, ((out.width - word_img.width) // 2, 0))
    return out


def stack(c, items, y, gaps):
    for im, gap in zip(items, gaps):
        y += gap
        paste_x(c, im, y)
        y += im.height
    return y


# ---------- cards ----------

def c_stack(kit, c):
    y = head(kit, c, 300)
    lead = starred(text([("THE ALL-IN-ONE", kit.sans(44, 800), INK)], tracking=12), ACCENT)
    hero = marker_behind(gradient_text("AI platform", kit.serif(230, True), COPPER_INK), MARKER)
    tail = text([("for advocates", kit.serif(132), INK)])
    stack(c, [lead, hero, tail], y, [120, 40, 26])
    return c


def c_pill(kit, c):
    y = head(kit, c, 300)
    lead = text([("The all-in-one", kit.serif(128), INK)])
    word = text([("AI platform", kit.serif(150, True), PAPER)])
    pill = Image.new("RGBA", (word.width + 120, word.height + 84), (0, 0, 0, 0))
    ImageDraw.Draw(pill).rounded_rectangle((0, 0, pill.width - 1, pill.height - 1), radius=pill.height // 2, fill=ACCENT + (255,))
    pill.alpha_composite(word, (60, 36))
    tail = text([("for advocates", kit.serif(128), INK)])
    top = y + 110
    lead_y = top
    pill_y = lead_y + lead.height + 40
    sh = blank()
    sh.paste(pill, ((W - pill.width) // 2, pill_y + 14))
    c.alpha_composite(shadow(sh.getchannel("A"), 24, 0.35, (120, 60, 40)))
    stack(c, [lead, pill, tail], top, [0, 40, 40])
    return c


def c_ribbon(kit, c):
    y = head(kit, c, 290)
    l1 = text([("The all-in-one", kit.serif(96), PAPER)])
    hero = text([("AI platform", kit.serif(170, True), (255, 222, 198))])
    l2 = text([("for advocates", kit.serif(96), PAPER)])
    pad, gap = 78, 30
    band_top = y + 110
    band_h = pad * 2 + l1.height + hero.height + l2.height + 2 * gap
    band = linear((W, band_h), (186, 100, 72), (216, 136, 98), 0)
    d = ImageDraw.Draw(band)
    for inset in (18, 26):  # fine double rule, like a printed ribbon
        d.line((0, inset, W, inset), fill=(246, 214, 192, 150), width=2)
        d.line((0, band_h - inset, W, band_h - inset), fill=(246, 214, 192, 150), width=2)
    sh = blank()
    sh.paste(band, (0, band_top + 12))
    c.alpha_composite(shadow(sh.getchannel("A"), 26, 0.30, (110, 55, 38)))
    c.alpha_composite(band, (0, band_top))
    stack(c, [l1, hero, l2], band_top + pad, [0, gap, gap])
    s = star(58, PAPER)
    hero_cy = band_top + pad + l1.height + gap + hero.height // 2
    for x in ((W - hero.width) // 2 - 70 - s.width, (W + hero.width) // 2 + 70):
        c.alpha_composite(s, (x, hero_cy - s.height // 2))
    return c


def c_noir(kit, c):
    y = head(kit, c, 300, light=True)
    lead = starred(text([("THE ALL-IN-ONE", kit.sans(44, 800), CREAM)], tracking=12), ACCENT_LIGHT)
    hero = gradient_text("AI platform", kit.serif(230, True), COPPER_GLOW)
    tail = text([("for advocates", kit.serif(132), CREAM)])
    stack(c, [lead, hero, tail], y, [120, 44, 34])
    return c


def c_copper(kit, c):
    y = head(kit, c, 290, light=True)
    lead = text([("The all-in-one", kit.serif(124), CREAM)])
    hero = text([("AI platform", kit.serif(210, True), (255, 230, 210))])
    rule = Image.new("RGBA", (round(hero.width * 0.62), 8), (0, 0, 0, 0))
    ImageDraw.Draw(rule).rounded_rectangle((0, 0, rule.width - 1, 7), radius=4, fill=(255, 230, 210, 230))
    tail = text([("for advocates", kit.serif(124), CREAM)])
    stack(c, [lead, hero, rule, tail], y, [110, 36, 34, 40])
    return c


def c_classic(kit, c):
    """Closest to the video's opening card: same centred lockup, tagline twice the size on two lines."""
    y = head(kit, c, 420, mark=300, word=690)
    size = 104
    l1 = Kit.line([("The all-in-one ", kit.serif(size), INK)])
    hero = gradient_text("AI platform", kit.serif(size, True), COPPER_INK)
    l1 = l1.crop(l1.getbbox())
    row = Image.new("RGBA", (l1.width + 24 + hero.width, max(l1.height, hero.height) + 6), (0, 0, 0, 0))
    row.alpha_composite(l1, (0, 0))
    row.alpha_composite(hero, (l1.width + 24, 0))
    l2 = text([("for advocates", kit.serif(size), INK)])
    s = star(40, ACCENT)
    end = stack(c, [row, l2], y, [96, 28])
    paste_x(c, s, end + 70)
    return c


CARDS = {  # name: (draw, ground)
    "stack": (c_stack, "cream"),
    "pill": (c_pill, "cream"),
    "ribbon": (c_ribbon, "cream"),
    "noir": (c_noir, "dark"),
    "copper": (c_copper, "copper"),
    "classic": (c_classic, "cream"),
}
OPTICAL_CENTRE = 0.47  # a touch above the middle, like the opening card


def render(kit, name):
    draw, kind = CARDS[name]
    layer = blank()
    layer.mark_cy = 0
    draw(kit, layer)
    solid = layer.getchannel("A").point(lambda v: 255 if v > 60 else 0)
    top, bottom = solid.getbbox()[1], solid.getbbox()[3]
    dy = round(H * OPTICAL_CENTRE - (top + bottom) / 2)
    c = ground(layer.mark_cy + dy, dark=kind == "dark", copper=kind == "copper")
    shifted = blank()
    shifted.paste(layer, (0, dy))
    c.alpha_composite(shifted)
    return c


def main():
    brand, out_dir = sys.argv[1:3]
    names = sys.argv[3:] or list(CARDS)
    os.makedirs(out_dir, exist_ok=True)
    kit = Kit(brand)
    order = list(CARDS)
    paths = []
    for name in names:
        path = f"{out_dir}/{order.index(name) + 1:02d}_{name}.jpg"
        render(kit, name).convert("RGB").save(path, quality=92, optimize=True, progressive=True)
        paths.append(path)
        print(path)
    if len(paths) > 1:
        contact_sheet(paths, f"{out_dir}/00_all_cards.jpg", cols=len(paths) if len(paths) <= 6 else 5)


if __name__ == "__main__":
    main()
