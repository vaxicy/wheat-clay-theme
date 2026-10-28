"""Wheat Clay Theme - icon candidates.

Code-drawn marks, a light/dark contact sheet and an inline strip.

Run from the project root:  py -3 scripts/generate-icon-candidates.py
"""

import io
import math
import os

from PIL import Image, ImageDraw, ImageFont

S = 3
W = 1024

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "logo-candidates")

KHAKI = (138, 127, 106, 255)      # #8A7F6A
BROWN = (107, 95, 74, 255)        # #6B5F4A
SAND = (183, 176, 158, 255)       # #B7B09E
PALE = (222, 214, 193, 255)       # #DED6C1
CREAM = (235, 226, 204, 255)      # #EBE2CC

LIGHT_BG = (250, 247, 240, 255)
DARK_BG = (54, 50, 42, 255)
LIGHT_INK = (58, 51, 40, 255)
DARK_INK = (238, 231, 216, 255)

FONT_DIR = r"C:\Windows\Fonts"


def font(name, size):
    try:
        return ImageFont.truetype(os.path.join(FONT_DIR, name), size)
    except Exception:
        return ImageFont.load_default()


def scr(p):
    return (p[0] * S, p[1] * S)


def wd(v):
    return max(1, int(round(v * S)))


def canvas():
    return Image.new("RGBA", (W * S, W * S), (0, 0, 0, 0))


def finish(img):
    return img.resize((W, W), Image.LANCZOS)


def poly(draw, pts, fill):
    draw.polygon([scr(p) for p in pts], fill=fill)


def disc(draw, center, r, fill):
    draw.ellipse([center[0] * S - r * S, center[1] * S - r * S,
                  center[0] * S + r * S, center[1] * S + r * S], fill=fill)


def ring(draw, center, r, width, fill):
    draw.ellipse([center[0] * S - r * S, center[1] * S - r * S,
                  center[0] * S + r * S, center[1] * S + r * S],
                 outline=fill, width=wd(width))


def oval(draw, center, rx, ry, angle, fill):
    cx, cy = center
    pts = []
    ca, sa = math.cos(angle), math.sin(angle)
    for i in range(64):
        t = 2 * math.pi * i / 64
        x, y = rx * math.cos(t), ry * math.sin(t)
        pts.append((cx + x * ca - y * sa, cy + x * sa + y * ca))
    poly(draw, pts, fill)


# ---------------------------------------------------------------- candidates

def cand_bowl():
    img = canvas()
    d = ImageDraw.Draw(img)

    # side view of a hand-thrown bowl
    d.pieslice([scr((250, 402)), scr((774, 900))], 0, 180, fill=KHAKI)
    d.line([scr((250, 402)), scr((774, 402))], fill=BROWN, width=wd(32))
    d.arc([scr((330, 480)), scr((694, 812))], 20, 160, fill=PALE, width=wd(28))
    d.arc([scr((392, 560)), scr((632, 830))], 24, 156, fill=SAND, width=wd(20))
    # foot
    d.rectangle([scr((436, 884)), scr((588, 916))], fill=BROWN)

    return finish(img)


def cand_seeds():
    img = canvas()
    d = ImageDraw.Draw(img)

    oval(d, (410, 420), 196, 126, math.radians(-24), BROWN)
    oval(d, (654, 566), 172, 110, math.radians(18), KHAKI)
    oval(d, (452, 706), 152, 96, math.radians(-8), SAND)

    return finish(img)


def cand_wheel():
    img = canvas()
    d = ImageDraw.Draw(img)

    disc(d, (512, 512), 340, KHAKI)
    disc(d, (512, 512), 258, PALE)
    disc(d, (512, 512), 74, CREAM)
    ring(d, (512, 512), 74, 20, BROWN)

    for i in range(8):
        ang = 2 * math.pi * i / 8
        p0 = (512 + math.cos(ang) * 286, 512 + math.sin(ang) * 286)
        p1 = (512 + math.cos(ang) * 340, 512 + math.sin(ang) * 340)
        d.line([scr(p0), scr(p1)], fill=CREAM, width=wd(22))

    return finish(img)


def cand_field():
    img = canvas()
    d = ImageDraw.Draw(img)

    for x, top, colour in ((330, 300, BROWN), (512, 220, KHAKI), (694, 320, BROWN)):
        d.line([scr((x, 780)), scr((x, top))], fill=colour, width=wd(22))
        for i in range(5):
            y = top + 40 + i * 62
            for sign in (1, -1):
                oval(d, (x + sign * 44, y), 34, 20, math.radians(-32 * sign), SAND)

    d.line([scr((196, 796)), scr((828, 796))], fill=KHAKI, width=wd(28))

    return finish(img)


def cand_rings():
    img = canvas()
    d = ImageDraw.Draw(img)

    ring(d, (512, 512), 330, 48, KHAKI)
    ring(d, (512, 512), 236, 36, SAND)
    ring(d, (512, 512), 154, 28, BROWN)
    disc(d, (512, 512), 62, PALE)

    return finish(img)


def cand_sheaf():
    img = canvas()
    d = ImageDraw.Draw(img)

    for x_top, x_bottom, colour in ((440, 486, BROWN), (512, 512, KHAKI), (584, 538, BROWN)):
        d.line([scr((x_top, 300)), scr((x_bottom, 800))], fill=colour, width=wd(24))
        for i in range(4):
            y = 330 + i * 54
            t = (y - 300) / 500
            x = x_top + (x_bottom - x_top) * t
            for sign in (1, -1):
                oval(d, (x + sign * 38, y), 30, 17, math.radians(-40 * sign), SAND)

    d.line([scr((398, 590)), scr((622, 590))], fill=PALE, width=wd(30))

    return finish(img)


CANDIDATES = [
    ("01", "clay-bowl", cand_bowl),
    ("02", "grain-seeds", cand_seeds),
    ("03", "potter-wheel", cand_wheel),
    ("04", "wheat-field", cand_field),
    ("05", "clay-rings", cand_rings),
    ("06", "sheaf", cand_sheaf),
]


# ---------------------------------------------------------------- sheet bits

def centered_text(d, center, text, fnt, fill):
    b = d.textbbox((0, 0), text, font=fnt)
    x = center[0] - (b[2] - b[0]) / 2 - b[0]
    y = center[1] - (b[3] - b[1]) / 2 - b[1]
    d.text((x, y), text, font=fnt, fill=fill)


def contact_sheet(icons, bg, ink, path):
    cell_w, cell_h = 420, 540
    margin, gap = 40, 26
    head = 118
    sheet_w = margin * 2 + cell_w * 3 + gap * 2
    sheet_h = margin + head + cell_h * 2 + gap + margin

    sheet = Image.new("RGBA", (sheet_w, sheet_h), bg)
    d = ImageDraw.Draw(sheet)

    f_title = font("segoeuib.ttf", 40)
    f_num = font("segoeuib.ttf", 30)
    f_name = font("segoeui.ttf", 26)
    f_small = font("segoeui.ttf", 20)

    centered_text(d, (sheet_w / 2, margin + 34), "WHEAT CLAY THEME", f_title, ink)
    centered_text(d, (sheet_w / 2, margin + 82), "icon candidates", f_small, ink)

    for idx, (num, name, icon) in enumerate(icons):
        row, col = divmod(idx, 3)
        gx = margin + col * (cell_w + gap)
        gy = margin + head + row * (cell_h + gap)

        sheet.alpha_composite(icon.resize((260, 260), Image.LANCZOS),
                              (gx + (cell_w - 260) // 2, gy + 30))

        centered_text(d, (gx + cell_w / 2, gy + 330), num, f_num, ink)
        centered_text(d, (gx + cell_w / 2, gy + 372), name, f_name, ink)
        centered_text(d, (gx + cell_w / 2, gy + 404), "1024 x 1024  PNG", f_small, ink)

        thumb = icon.resize((32, 32), Image.LANCZOS)
        tx, ty = gx + cell_w - 32 - 22, gy + cell_h - 32 - 22
        d.rectangle([tx - 10, ty - 10, tx + 42, ty + 42],
                    outline=(ink[0], ink[1], ink[2], 70), width=1)
        sheet.alpha_composite(thumb, (tx, ty))

    save_png(sheet.convert("RGB"), path)


def inline_strip(icons, path):
    size, gap, margin = 150, 18, 30
    strip_w = margin * 2 + size * len(icons) + gap * (len(icons) - 1)
    strip_h = margin * 2 + size + 34
    strip = Image.new("RGBA", (strip_w, strip_h), LIGHT_BG)
    d = ImageDraw.Draw(strip)
    f_num = font("segoeuib.ttf", 20)

    for idx, (num, _name, icon) in enumerate(icons):
        x = margin + idx * (size + gap)
        strip.alpha_composite(icon.resize((size, size), Image.LANCZOS), (x, margin))
        centered_text(d, (x + size / 2, margin + size + 16), num, f_num, LIGHT_INK)

    save_png(strip.convert("RGB"), path)


def save_png(img, path):
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(buf.getvalue())


def main():
    os.makedirs(OUT, exist_ok=True)

    icons = []
    for num, name, fn in CANDIDATES:
        icon = fn()
        box = icon.getbbox()
        if box is None:
            raise AssertionError("%s rendered empty" % name)
        left, top, right, bottom = box
        lo, hi = 70, 954
        if left < lo or top < lo or right > hi or bottom > hi:
            raise AssertionError("%s out of safe area: %s" % (name, box))
        path = os.path.join(OUT, "%s-%s.png" % (num, name))
        save_png(icon, path)
        print("wrote", os.path.relpath(path, ROOT), box)
        icons.append((num, name, icon))

    contact_sheet(icons, LIGHT_BG, LIGHT_INK, os.path.join(OUT, "contact-light.png"))
    contact_sheet(icons, DARK_BG, DARK_INK, os.path.join(OUT, "contact-dark.png"))
    inline_strip(icons, os.path.join(OUT, "inline-strip.png"))
    print("wrote contact-light.png / contact-dark.png / inline-strip.png")


if __name__ == "__main__":
    main()
