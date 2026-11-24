#!/usr/bin/env python3
"""THE EARTH LEDGER — NI23 G3 entry composer for final5 (@kangair110).

A classic one-page newspaper front for Monday 23 November 2026, drawn
from scratch with PIL: giant Playfair masthead, a numbers strip,
13 large illustrated story cards (lead + grid), a dotted_map of the
world with numbered pins, a UTC timeline, an ALSO ON column of briefs
(stories 14-39), a red DATE CHECK box and a verification footer.
Every fact comes only from the locked NI23 pool. Original drawings.

Usage: python3 compose.py [A|B|C] [output.png]   (duel variants)
"""

import math
import sys

from PIL import Image, ImageDraw, ImageFont

FD = "/home/hatch/workspace/tools/bedah-19nov/news-image/fonts/"
W = H = 1024
M = 24

PALETTES = {
    "A": dict(bg=(242, 231, 206), card=(251, 245, 228), ink=(58, 42, 24),
              accent=(102, 112, 42), faint=(122, 102, 70), rule=(58, 42, 24)),
    "B": dict(bg=(43, 29, 16), card=(58, 42, 24), ink=(242, 231, 206),
              accent=(168, 180, 90), faint=(190, 170, 130), rule=(242, 231, 206)),
    "C": dict(bg=(252, 250, 244), card=(255, 255, 255), ink=(51, 36, 26),
              accent=(154, 74, 31), faint=(130, 110, 88), rule=(51, 36, 26)),
}

REGION_COLORS = {
    "AFRIKA": (138, 109, 31),
    "TIMUR TENGAH": (179, 84, 30),
    "AMERIKA UTARA": (70, 90, 140),
    "EROPA": (90, 70, 140),
    "ASIA SELATAN": (160, 60, 90),
    "ASIA TENGGARA": (30, 120, 110),
    "ASIA-PASIFIK": (60, 130, 60),
    "GLOBAL": (102, 112, 42),
}

# grid cards: (num, region, topic, src, head, deck, kind)
grid = [
    (2, "TIMUR TENGAH", "gulf war", "AP LIVE", "Tankers Burn in the Gulf",
     "Ablaze in Hormuz; Iran-US war widens.", "flame"),
    (3, "AMERIKA UTARA", "us house", "BBC 23 NOV", "House Falls 258-173",
     "Democrats' biggest House win since 1992.", "ballot"),
    (4, "EROPA", "kyiv rescue", "BBC 23 NOV", "Kyiv Boy Out Alive",
     "Boy, 7, freed in Kyiv; 6 killed.", "cross"),
    (5, "ASIA SELATAN", "test cricket", "OBSERVER VOICE", "India Pile Up 720/9d",
     "Highest Test total ever in Wellington.", "bat"),
    (6, "GLOBAL", "gold price", "OBSERVER VOICE", "Gold Slides to $3,538",
     "Down $2,000 from the $5,595 record.", "coin"),
    (7, "EROPA", "climate talks", "BBC / AP", "COP31 Ends, No Deal",
     "COP31 draft from Turkiye omits fuels.", "leaf"),
    (8, "ASIA TENGGARA", "icj ruling", "ICJ RULING", "ICJ: Myanmar Genocide",
     "Guilty over 2017 Rohingya campaign.", "scales"),
    (9, "ASIA SELATAN", "steel deal", "OBSERVER VOICE", "Tata Steel Pipe Sale",
     "Pipe unit sold to APL Apollo.", "factory"),
    (10, "ASIA TENGGARA", "factory fire", "JAGRAN JOSH", "Indonesia Fire Toll",
     "7 found, 50 missing - 23 Nov update.", "flame"),
    (11, "AMERIKA UTARA", "wedding", "BBC 23 NOV", "Miley Cyrus Weds",
     "Marries Maxx Morando in California.", "ring"),
    (12, "EROPA", "tennis", "BBC 23 NOV", "Alcaraz's First ATP",
     "Beats Zverev for first ATP Finals.", "trophy"),
    (13, "GLOBAL", "ai weapons", "SALONVISION", "UN Talks: Killer AI",
     "States agree: UN talks on AI continue.", "robot"),
]

NUMS = [
    ("258-173", "US HOUSE"),
    ("720/9d", "INDIA WELLINGTON"),
    ("$3,538", "GOLD PER OUNCE"),
    ("7 + 50", "FOUND MISSING JAVA"),
    ("Rs28,000 cr", "TATA STEEL DEAL"),
    ("14", "MISSING IN KYIV"),
    ("65.9%", "INDIGO SHARE"),
]

TL = [
    ("00:02Z", "UN killer-AI talks resume"),
    ("02:00Z", "Albanese on COP31"),
    ("MORNING", "Benghazi blast reported"),
    ("MIDDAY", "Kyiv missing count: 14"),
    ("EVENING", "House called 258-173"),
]

BRIEFS = [
    "IRGC claims Patriot hits",
    "Coalition intercepts Houthi missile",
    "Swimmer crosses Hormuz",
    "US releases UFO footage",
    "Albanese: COP31 failure",
    "Russian ship burns, Finland",
    "Ship towed, Gulf of Finland",
    "Kyiv: 14 missing - Zelenskiy",
    "Burnham hails UK-EU reset",
    "Thousands march in Lisbon on prices",
    "Myanmar junta slams ASEAN",
    "Ex-rebels trapped in Cameroon",
    "Lion loose in Turkiye",
    "Nepal's Shah meets Modi",
    "India-Bulgaria IMEC talks",
    "Guru Nanak Jayanti marked",
    "UP drill in 75 districts",
    "India chase win, NZ 119/2",
    "India take ODI series 3-2",
    "Snooker crown kept by Anupama",
    "World Chess draws crowds",
    "MP Wadkute dies in Delhi",
    "Kota bus tragedy: 9 dead",
    "SpiceJet call; IndiGo 65.9%",
    "Google $5M for IIT AI",
    "FBI probes Justice database",
]

dc = ("Xi-Trump-Putin summit - 19 Nov 2026 · SpiceJet Rs5,500 cr raise - "
      "18 Nov 2026 · Paolo Bulgari death - reported 22 Nov 2026 · "
      "24 killed, South Sudan - Juba, 22 Nov 2026 · Bolsonaro stable in "
      "ICU - Brasilia, 22 Nov 2026 · Indonesia candy-factory fire itself "
      "- 22 Nov 2026")

dotted_map = [
    "                                                              ",
    "      #### ###            ##### ########## ####               ",
    "    ###########         ########################## ##         ",
    "     #########           ########################  ####       ",
    "      ######  ##          ##################      ######      ",
    "       ####  ####          ###############         ####       ",
    "        ##  ######          ############           ##         ",
    "           ########          ##########                       ",
    "            ######   ##       ########     ###                ",
    "             ####   ####       ######    #######              ",
    "             ###     ##         ####      #####               ",
    "             ##                  ##        ###    ##          ",
    "             #                             ##   ####    #     ",
    "                                                ##            ",
]

# pins on the dotted map: (card number, column, row)
PINS = [(1, 27, 6), (2, 36, 7), (3, 7, 3), (4, 31, 2), (5, 57, 13),
        (6, 17, 8), (7, 33, 4), (8, 45, 8), (9, 42, 7), (10, 49, 10),
        (11, 3, 4), (12, 29, 3), (13, 28, 2)]


def fb(n, name="Archivo-Bold.ttf"):
    return ImageFont.truetype(FD + name, n)


def fr(n):
    return ImageFont.truetype(FD + "Archivo.ttf", n)


def fsr(n):
    return ImageFont.truetype(FD + "Archivo.ttf", n)


_GF = {}


def gf(name, size):
    """Cached auxiliary fonts (chip/tag/source sizes) for lead/mini."""
    key = (name, size)
    if key not in _GF:
        _GF[key] = ImageFont.truetype(FD + name, size)
    return _GF[key]


def fit(d, text, fontfn, size, max_w, min_size=10):
    s = size
    while s > min_size:
        f = fontfn(s)
        if d.textlength(text, font=f) <= max_w:
            return f, text
        s -= 1
    f = fontfn(min_size)
    while text and d.textlength(text + "..", font=f) > max_w:
        text = text[:-1]
    return f, text + ".."


def draw_icon(d, kind, x, y, s, col):
    if kind == "flame":
        d.polygon([(x + s * .5, y), (x + s * .85, y + s * .55),
                   (x + s * .7, y + s), (x + s * .3, y + s),
                   (x + s * .15, y + s * .55)], outline=col, width=2)
        d.ellipse([x + s * .38, y + s * .55, x + s * .62, y + s * .9],
                  outline=col, width=2)
    elif kind == "ballot":
        d.rectangle([x + 2, y + s * .35, x + s - 2, y + s], outline=col, width=2)
        d.line([x + s * .2, y + s * .35, x + s * .5, y + 2], fill=col, width=3)
        d.line([x + s * .3, y + s * .6, x + s * .45, y + s * .75], fill=col, width=2)
        d.line([x + s * .45, y + s * .75, x + s * .72, y + s * .5], fill=col, width=2)
    elif kind == "cross":
        d.rectangle([x + s * .38, y + 2, x + s * .62, y + s - 2], outline=col, width=2)
        d.rectangle([x + 2, y + s * .3, x + s - 2, y + s * .58], outline=col, width=2)
    elif kind == "bat":
        d.line([x + s * .25, y + s - 2, x + s * .7, y + 2], fill=col, width=4)
        d.ellipse([x + s * .62, y + s * .62, x + s - 2, y + s - 2], outline=col, width=2)
    elif kind == "coin":
        d.ellipse([x + 2, y + 2, x + s - 2, y + s - 2], outline=col, width=2)
        d.text((x + s * .34, y + s * .22), "$", font=fb(int(s * .55)), fill=col)
    elif kind == "leaf":
        d.ellipse([x + 2, y + 2, x + s - 2, y + s - 2], outline=col, width=2)
        d.line([x + s * .3, y + s * .75, x + s * .72, y + s * .28], fill=col, width=2)
    elif kind == "scales":
        d.line([x + s * .5, y + 2, x + s * .5, y + s - 4], fill=col, width=2)
        d.line([x + 4, y + s * .2, x + s - 4, y + s * .2], fill=col, width=2)
        d.arc([x + 1, y + s * .2, x + s * .35, y + s * .62], 0, 180, fill=col, width=2)
        d.arc([x + s * .65, y + s * .2, x + s - 1, y + s * .62], 0, 180, fill=col, width=2)
        d.line([x + s * .3, y + s - 2, x + s * .7, y + s - 2], fill=col, width=3)
    elif kind == "factory":
        d.rectangle([x + 2, y + s * .45, x + s - 2, y + s - 2], outline=col, width=2)
        d.rectangle([x + s * .12, y + s * .12, x + s * .3, y + s * .45], outline=col, width=2)
        d.line([x + s * .55, y + s * .68, x + s * .8, y + s * .68], fill=col, width=2)
    elif kind == "ring":
        d.ellipse([x + s * .22, y + s * .38, x + s * .78, y + s * .95], outline=col, width=3)
        d.polygon([(x + s * .5, y + 1), (x + s * .68, y + s * .22),
                   (x + s * .5, y + s * .4), (x + s * .32, y + s * .22)],
                  outline=col, width=2)
    elif kind == "trophy":
        d.arc([x + s * .25, y + 2, x + s * .75, y + s * .6], 0, 180, fill=col, width=2)
        d.line([x + s * .25, y + s * .3, x + 2, y + s * .18], fill=col, width=2)
        d.line([x + s * .75, y + s * .3, x + s - 2, y + s * .18], fill=col, width=2)
        d.line([x + s * .5, y + s * .55, x + s * .5, y + s * .8], fill=col, width=3)
        d.line([x + s * .28, y + s - 3, x + s * .72, y + s - 3], fill=col, width=3)
    elif kind == "robot":
        d.rectangle([x + s * .18, y + s * .3, x + s * .82, y + s * .85], outline=col, width=2)
        d.line([x + s * .5, y + s * .3, x + s * .5, y + 2], fill=col, width=2)
        d.ellipse([x + s * .3, y + s * .48, x + s * .44, y + s * .62], fill=col)
        d.ellipse([x + s * .56, y + s * .48, x + s * .7, y + s * .62], fill=col)
    else:
        d.polygon([(x + 2, y + s * .6), (x + s - 2, y + s * .6),
                   (x + s * .8, y + s * .85), (x + s * .2, y + s * .85)],
                  outline=col, width=2)
        d.line([x + s * .5, y + s * .6, x + s * .5, y + 2], fill=col, width=2)


def draw_ship_scene(d, x, y, w, h, ink, accent):
    hull_y = y + h * 0.62
    d.polygon([(x + 8, hull_y), (x + w - 30, hull_y), (x + w - 70, hull_y + 34),
               (x + 40, hull_y + 34)], outline=ink, width=3)
    for i in range(3):
        cx = x + 46 + i * 52
        d.rectangle([cx, hull_y - 30, cx + 44, hull_y - 4], outline=ink, width=2)
        d.rectangle([cx, hull_y - 56, cx + 44, hull_y - 32], outline=accent, width=2)
    d.line([x + w - 120, hull_y, x + w - 120, hull_y - 74], fill=ink, width=3)
    d.line([x + w - 120, hull_y - 74, x + w - 66, hull_y - 40], fill=ink, width=2)
    cx, cy, r = x + w - 26, y + 34, 24
    pts = []
    for i in range(16):
        rr = r if i % 2 == 0 else r * 0.45
        a = math.pi * i / 8
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    d.polygon(pts, outline=accent, width=3)
    d.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=accent)
    for wx in range(int(x) + 4, int(x + w - 10), 34):
        d.arc([wx, hull_y + 42, wx + 26, hull_y + 58], 180, 360, fill=accent, width=2)


def lead(d, x, y, w, h, num, region, src, head, deck, kind, P):
    """The big No 1 card. Args 7-10 (src/head/deck/kind) are the record."""
    ink, accent, faint, card = P["ink"], P["accent"], P["faint"], P["card"]
    d.rectangle([x, y, x + w, y + h], fill=card, outline=ink, width=2)
    draw_ship_scene(d, x + 14, y + 56, 236, 106, ink, accent)
    chip = "No %s - %s" % (num, region)
    fc = gf("Archivo-Bold.ttf", 13)
    d.rectangle([x + 14, y + 12, x + 14 + d.textlength(chip, font=fc) + 16, y + 34],
                fill=REGION_COLORS[region])
    d.text((x + 22, y + 16), chip, font=fc, fill=(255, 255, 255))
    d.text((x + 14, y + 40), "LEAD STORY - LIBYA",
           font=gf("Archivo.ttf", 11), fill=faint)
    tx = x + 264
    parts = head.rsplit(" in ", 1)
    fh = fb(35, "PlayfairDisplay-Bold.ttf")
    d.text((tx, y + 14), parts[0], font=fh, fill=ink)
    if len(parts) > 1:
        d.text((tx, y + 56), "in " + parts[1], font=fh, fill=ink)
    fd = fr(16)
    lines = ["An explosion rocks a Russian vessel in Benghazi",
             "port, Libya - a suspected drone strike, 23 Nov."]
    for j, ln in enumerate(lines):
        if d.textlength(ln, font=fd) <= x + w - tx - 10:
            d.text((tx, y + 100 + j * 24), ln, font=fd, fill=ink)
        else:
            fl2, ln2 = fit(d, ln, fr, 16, x + w - tx - 10)
            d.text((tx, y + 100 + j * 24), ln2, font=fl2, fill=ink)
    d.text((tx, y + h - 22), "SOURCE: " + src,
           font=gf("Archivo-Bold.ttf", 11), fill=accent)


def mini(d, x, y, w, h, num, region, src, head, deck, kind, P):
    """One grid card. Args 7-10 (src/head/deck/kind) are the record."""
    ink, accent, faint, card = P["ink"], P["accent"], P["faint"], P["card"]
    d.rectangle([x, y, x + w, y + h], fill=card, outline=faint, width=1)
    d.ellipse([x + 8, y + 8, x + 30, y + 30], fill=accent)
    fn2 = gf("Archivo-Bold.ttf", 13)
    ns = str(num)
    d.text((x + 19 - d.textlength(ns, font=fn2) / 2, y + 12), ns, font=fn2,
           fill=(255, 255, 255))
    rc = REGION_COLORS[region]
    fchip = gf("Archivo-Bold.ttf", 10)
    d.rectangle([x + 36, y + 9, x + 36 + d.textlength(region, font=fchip) + 10, y + 28],
                fill=rc)
    d.text((x + 41, y + 13), region, font=fchip, fill=(255, 255, 255))
    fsrc = gf("Archivo.ttf", 10)
    d.text((x + w - 8 - d.textlength(src, font=fsrc), y + 12), src, font=fsrc, fill=faint)
    draw_icon(d, kind, x + w - 34, y + 34, 26, accent)
    fh = fb(24)
    head2 = head
    if d.textlength(head2, font=fh) > w - 52:
        fh, head2 = fit(d, head, fb, 24, w - 52)
    d.text((x + 10, y + 34), head2, font=fh, fill=ink)
    fd = fr(14)
    deck2 = deck
    if d.textlength(deck2, font=fd) > w - 18:
        fd, deck2 = fit(d, deck, fr, 14, w - 18)
    d.text((x + 10, y + 59), deck2, font=fd, fill=faint)


def main():
    variant = sys.argv[1] if len(sys.argv) > 1 else "A"
    out = sys.argv[2] if len(sys.argv) > 2 else "/tmp/ni23g3-final5/entry.png"
    P = PALETTES[variant]
    bg, ink, accent, faint, rule = P["bg"], P["ink"], P["accent"], P["faint"], P["rule"]
    img = Image.new("RGB", (W, H), bg)
    d = ImageDraw.Draw(img)

    # kicker
    kick = "39 STORIES - 8 REGIONS - EVERY ONE FROM 23 NOVEMBER 2026"
    f, kick = fit(d, kick, fb, 15, W - 2 * M)
    d.text(((W - d.textlength(kick, font=f)) / 2, 16), kick, font=f, fill=accent)
    d.line([M, 42, W - M, 42], fill=rule, width=3)
    d.line([M, 47, W - M, 47], fill=rule, width=1)

    # masthead (PlayfairDisplay-Black)
    f, mast = fit(d, "THE EARTH LEDGER",
                  lambda s: ImageFont.truetype(FD + "PlayfairDisplay-Black.ttf", s),
                  86, W - 2 * M, 64)
    d.text(((W - d.textlength(mast, font=f)) / 2, 52), mast, font=f, fill=ink)
    date = "Monday 23 November 2026"
    fdate = fb(31, "PlayfairDisplay-Bold.ttf")
    tw = d.textlength(date, font=fdate)
    d.text(((W - tw) / 2, 146), date, font=fdate, fill=accent)
    d.line([M, 160, (W - tw) / 2 - 16, 160], fill=rule, width=2)
    d.line([(W + tw) / 2 + 16, 160, W - M, 160], fill=rule, width=2)
    d.line([M, 186, W - M, 186], fill=rule, width=1)

    # numbers strip
    sy, sh = 194, 46
    cell = (W - 2 * M) / 7.0
    for i, (num, lab) in enumerate(NUMS):
        cx = M + i * cell
        if i:
            d.line([cx, sy + 4, cx, sy + sh - 4], fill=faint, width=1)
        fn, num2 = fit(d, num, fb, 23, cell - 8)
        d.text((cx + (cell - d.textlength(num2, font=fn)) / 2, sy), num2, font=fn, fill=ink)
        fl, lab2 = fit(d, lab, fr, 10, cell - 6)
        d.text((cx + (cell - d.textlength(lab2, font=fl)) / 2, sy + 28), lab2,
               font=fl, fill=faint)
    d.line([M, sy + sh + 4, W - M, sy + sh + 4], fill=rule, width=2)

    # lead card + map
    ly, lh = 252, 176
    lead(d, M, ly, 640, lh, "1", "AFRIKA", "BBC - 23 NOV 2026",
         "Blast Hits Russian Ship in Benghazi Port",
         "An explosion rocks a Russian vessel in Benghazi port, Libya - "
         "a suspected drone strike, reported 23 November.", "ship", P)
    mx = 676
    d.rectangle([mx, ly, W - M, ly + lh], fill=P["card"], outline=ink, width=2)
    d.text((mx + 12, ly + 10), "WHERE IT HAPPENED", font=fb(14), fill=ink)
    ox, oy, step = mx + 16, ly + 32, 4.4
    for r, row in enumerate(dotted_map):
        for c, ch in enumerate(row):
            if ch == "#":
                px, py = ox + c * step, oy + r * step
                d.ellipse([px, py, px + 2.4, py + 2.4], fill=faint)
    fp = fb(10)
    for num, c, r in PINS:
        px, py = ox + c * step, oy + r * step
        d.ellipse([px - 8, py - 8, px + 9, py + 9], fill=accent, outline=ink)
        s = str(num)
        d.text((px - d.textlength(s, font=fp) / 2 + 0.5, py - 6), s, font=fp,
               fill=(255, 255, 255))
    d.text((mx + 12, ly + 97), "Dotted map - numbered pins mark story places",
           font=fr(10), fill=faint)
    leg = [("TIMUR TENGAH", "Middle East"), ("EROPA", "Europe"),
           ("ASIA SELATAN", "South Asia"), ("ASIA TENGGARA", "SE Asia"),
           ("AMERIKA UTARA", "N America"), ("AFRIKA", "Africa"),
           ("GLOBAL", "Global"), ("ASIA-PASIFIK", "Asia-Pacific")]
    for i, (key, name) in enumerate(leg):
        lx = mx + 12 + (i % 2) * 158
        lyy = ly + 112 + (i // 2) * 15
        d.rectangle([lx, lyy + 2, lx + 10, lyy + 12], fill=REGION_COLORS[key])
        d.text((lx + 15, lyy), name, font=fr(11), fill=ink)

    # grid cards
    gy = ly + lh + 10
    cw, chh, gx, gyap = 310, 78, 7, 5
    for i, (num, region, topic, src, head, deck, kind) in enumerate(grid):
        cx = M + (i % 3) * (cw + gx)
        cy = gy + (i // 3) * (chh + gyap)
        mini(d, cx, cy, cw, chh, num, region, src, head, deck, kind, P)

    # timeline
    ty = gy + 4 * chh + 3 * gyap + 6
    d.line([M, ty, W - M, ty], fill=rule, width=2)
    tw5 = (W - 2 * M) / 5.0
    for i, (slot, txt) in enumerate(TL):
        cx = M + i * tw5
        d.ellipse([cx + 2, ty + 7, cx + 10, ty + 15], fill=accent)
        d.text((cx + 16, ty + 4), slot, font=fb(13), fill=ink)
        ftl, txt2 = fit(d, txt, fr, 12, tw5 - 14)
        d.text((cx + 2, ty + 24), txt2, font=ftl, fill=faint)

    # bottom: ALSO ON + DATE CHECK
    by = ty + 44
    d.rectangle([M, by, 640, 972], fill=P["card"], outline=faint, width=1)
    d.text((M + 12, by + 8), "ALSO ON THE EARTH LEDGER - STORIES 14-39",
           font=fb(14), fill=ink)
    colw = (640 - M - 16) / 3.0
    for i, item in enumerate(BRIEFS):
        cx = M + 10 + (i // 9) * colw
        cy = by + 32 + (i % 9) * 14
        label = "%d. %s" % (14 + i, item)
        fa = fsr(13)
        label2 = label
        if d.textlength(label2, font=fa) > colw - 6:
            fa, label2 = fit(d, label, fsr, 13, colw - 6)
        d.text((cx, cy), label2, font=fa, fill=ink)
    dx = 652
    d.rectangle([dx, by, W - M, 972],
                fill=(250, 235, 225) if variant != "B" else (70, 34, 22),
                outline=(178, 44, 32), width=2)
    d.text((dx + 12, by + 8), "DATE CHECK - NOT 23 NOVEMBER",
           font=fb(14), fill=(178, 44, 32))
    for i, item in enumerate(dc.split("·")):
        fdc, item2 = fit(d, item.strip(), fr, 13, W - M - dx - 22)
        d.text((dx + 12, by + 36 + i * 20), item2, font=fdc,
               fill=(150, 30, 22) if variant != "B" else (255, 190, 170))

    # footer
    f1 = ("Every story happened, or was first reported, on Monday 23 November "
          "2026. Contested claims are attributed.")
    ff1, f1b = fit(d, f1, fr, 12, W - 2 * M)
    d.text(((W - d.textlength(f1b, font=ff1)) / 2, 980), f1b, font=ff1, fill=ink)
    f2 = "Original drawings. - THE EARTH LEDGER - one day, one page."
    d.text(((W - d.textlength(f2, font=fr(11))) / 2, 998), f2, font=fr(11), fill=faint)

    img.save(out)
    print("wrote", out, variant)


if __name__ == "__main__":
    main()
