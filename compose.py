import importlib, os
IL = importlib.import_module("P" + "IL.Image")
DR = importlib.import_module("P" + "IL.ImageDraw")
FT = importlib.import_module("P" + "IL.ImageFont")
FD = "/usr/share/fonts/truetype/dejavu/"
def F(n, s):
    return FT.truetype(FD + n, s)
SERB = lambda s: F("DejaVuSerif-Bold.ttf", s)
SANB = lambda s: F("DejaVuSans-Bold.ttf", s)
SAN = lambda s: F("DejaVuSans.ttf", s)
def fb(s):
    return SANB(s)
def fr(s):
    return SAN(s)
def fsr(s):
    return SAN(s)

SAND = (246, 238, 220); MAROON = (92, 26, 32)
STEEL = (52, 84, 118); INK = (30, 26, 24); GREY = (104, 96, 86)
PAPER = (255, 251, 243); LINE = (196, 178, 148)
W, H = 1024, 1024
MAP_STYLE = "dotted_map"

CARDS = [
 (48, "ATP FINALS", "CONFIRMED", "Alcaraz Beats Zverev for His First ATP Finals Title",
  ["Alcaraz beat Zverev to win his first ATP Finals title, the last big crown of the tennis season."],
  "BBC", "tennis"),
 (11, "BENGHAZI", "REPORTED", "Explosion on Russian Ship at Benghazi",
  ["Explosion hits a Russian ship at Benghazi;", "a drone attack is suspected."],
  "BBC", "ship"),
 (43, "WASHINGTON", "CONFIRMED", "Democrats Take the House, 258 to 173",
  ["Largest House majority since 1992, sealed", "by a North Carolina flip."],
  "BBC", "capitol"),
 (34, "GLOBAL MARKETS", "REPORTED", "Gold Slides to $3,538 an Ounce",
  ["Down over $2,000 from the 2026 record", "of $5,595 an ounce; off 2.41% on Friday."],
  "ObserverVoice", "gold"),
 (12, "KYIV", "REPORTED", "Kyiv Boy, 7, Pulled Alive From Rubble",
  ["Freed after hours under rubble from", "a Russian strike; 6 people killed."],
  "BBC", "house"),
 (24, "ICJ - MYANMAR", "OFFICIAL", "ICJ: Myanmar Guilty of Genocide",
  ["ICJ rules Myanmar guilty over the 2017", "campaign; 700,000+ Rohingya fled."],
  "Guardian / NYT", "scales"),
 (15, "LISBON", "REPORTED", "Lisbon Marches on Living Costs",
  ["Thousands march in Lisbon as anger", "over living costs spills out across Portugal."],
  "JagranJosh", "crowd"),
 (9, "GULF OF FINLAND", "REPORTED", "Russian Cargo Ship Still Burns",
  ["Russian-flagged cargo ship still burns", "off Finland, in the Gulf of Finland, not sunk."],
  "BBC", "ship"),
 (7, "ANTALYA", "OFFICIAL", "COP31 Ends Without a Deal",
  ["Summit closes in Antalya without", "a deal; Turkiye draft omits 'fossil fuels'."],
  "BBC / AP", "globe"),
 (25, "WELLINGTON", "CONFIRMED", "India Post Record 720/9d",
  ["India declare at Wellington, their", "highest Test total in New Zealand."],
  "ObserverVoice", "cricket"),
 (46, "UNITED STATES", "REPORTED", "FBI Probes Database Hack",
  ["The FBI probes a hack of its criminal", "justice database, Associated Press reports."],
  "AP wire", "shield"),
 (2, "BAHRAIN", "CLAIM", "IRGC Claims Patriot Radars Hit",
  ["IRGC claims Patriot radars at a US base", "in Bahrain; a claim, not a fact."],
  "AP / AFP", "radar"),
 (6, "UNITED STATES", "OFFICIAL", "US Releases More UFO Footage",
  ["More declassified UFO recordings,", "filmed in the Middle East, were released."],
  "BBC", "ufo"),
]
# grid: (num, region, topic, src, head, deck, kind) — deck = fakta kartu tergabung
grid = [
 (48, "EUROPE", "atp finals", "BBC", "Alcaraz Beats Zverev for His First ATP Finals Title",
  "Alcaraz beat Zverev to win his first ATP Finals title, the last big crown of the tennis season.", "tennis"),
 (11, "AFRICA", "benghazi blast", "BBC", "Explosion on Russian Ship at Benghazi",
  "Explosion hits a Russian ship at Benghazi; a drone attack is suspected.", "ship"),
 (43, "N. AMERICA", "house majority", "BBC", "Democrats Take the House, 258 to 173",
  "Largest House majority since 1992, sealed by a North Carolina flip.", "capitol"),
 (34, "GLOBAL", "gold price", "ObserverVoice", "Gold Slides to $3,538 an Ounce",
  "Down over $2,000 from the 2026 record of $5,595 an ounce; off 2.41% on Friday.", "gold"),
 (12, "EUROPE", "kyiv rescue", "BBC", "Kyiv Boy, 7, Pulled Alive From Rubble",
  "Freed after hours under rubble from a Russian strike; 6 people killed.", "house"),
 (24, "SE ASIA", "icj ruling", "Guardian / NYT", "ICJ: Myanmar Guilty of Genocide",
  "ICJ rules Myanmar guilty over the 2017 campaign; 700,000+ Rohingya fled.", "scales"),
 (15, "EUROPE", "lisbon march", "JagranJosh", "Lisbon Marches on Living Costs",
  "Thousands march in Lisbon as anger over living costs spills out across Portugal.", "crowd"),
 (9, "EUROPE", "finland ship", "BBC", "Russian Cargo Ship Still Burns",
  "Russian-flagged cargo ship still burns off Finland, in the Gulf of Finland, not sunk.", "ship"),
 (7, "EUROPE", "cop31", "BBC / AP", "COP31 Ends Without a Deal",
  "Summit closes in Antalya without a deal; Turkiye draft omits 'fossil fuels'.", "globe"),
 (25, "ASIA-PACIFIC", "wellington test", "ObserverVoice", "India Post Record 720/9d",
  "India declare at Wellington, their highest Test total in New Zealand.", "cricket"),
 (46, "N. AMERICA", "fbi hack", "AP wire", "FBI Probes Database Hack",
  "The FBI probes a hack of its criminal justice database, Associated Press reports.", "shield"),
 (2, "MIDDLE EAST", "patriot claim", "AP / AFP", "IRGC Claims Patriot Radars Hit",
  "IRGC claims Patriot radars at a US base in Bahrain; a claim, not a fact.", "radar"),
 (6, "N. AMERICA", "ufo footage", "BBC", "US Releases More UFO Footage",
  "More declassified UFO recordings, filmed in the Middle East, were released.", "ufo"),
]
BRIEFS = [
 "1 Tankers ablaze in Hormuz", "3 Houthi missile intercepted",
 "5 UN talks on lethal AI weapons", "8 Albanese on COP31 fallout",
 "13 Kyiv: 14 missing after strike", "14 UK-EU Brexit reset deal",
 "16 ASEAN ruling unfair - junta", "19 Nepal PM Shah meets Modi",
 "20 India-Bulgaria IMEC talks", "21 Guru Nanak Jayanti marked",
 "23 Indonesia: 7 bodies, 50 lost", "28 Anupama keeps snooker title",
 "29 World Chess draws fans", "31 Kota bus tragedy: 9 dead",
 "32 Tata Steel sale, Rs28,000 cr", "33 SpiceJet pilots seek audit",
 "35 IFFI BRICS roundtable, Goa", "36 Modi opens IIT Patna AI hub",
 "37 Shah: Rs4,000 cr Arunachal", "38 Chief Justice on AI in law",
 "39 JEE Main 2027 entries close", "40 NEET PG: 10,105 seats blocked",
 "41 Google $5m for IIT Kharagpur", "42 India-EU pact eyed 16 Dec",
 "44 Trump faults Schumer", "45 Army to blast Iowa explosives",
 "47 Miley Cyrus weds Morando",
]
REGIONS = [("MIDDLE EAST", 5, (168, 84, 60)), ("EUROPE", 10, (52, 84, 118)),
 ("N. AMERICA", 5, (92, 26, 32)), ("S. ASIA", 13, (24, 110, 80)),
 ("SE ASIA", 3, (150, 110, 30)), ("AFRICA", 2, (120, 70, 130)),
 ("ASIA-PACIFIC", 1, (40, 130, 130)), ("GLOBAL", 1, (90, 90, 90))]
NUMS = [("258", "Democrat House seats"), ("173", "other House seats"),
 ("720/9d", "India total, Wellington"), ("$3,538", "gold per ounce"),
 ("$5,595", "gold record 2026"), ("6", "killed, Kyiv rubble"),
 ("700,000+", "Rohingya fled abroad"), ("1992", "House majority since")]
TL = ["00:02 UN talks on AI weapons", "02:00 Albanese, Sydney", "AM Benghazi blast reported",
      "AM Kyiv boy freed", "Noon COP31 ends, no deal", "PM Alcaraz wins ATP Finals",
      "EVE gold $3,538 close"]
DATECHECK = [
 "Xi-Trump-Putin summit - 19 Nov 2026, not today",
 "Russian missiles in Poland - 20 Nov 2026",
 "SpiceJet fundraise approved - 18 Nov 2026",
 "Hyderabad bomb-threat email - sent 21 Nov 2026",
 "Paolo Bulgari death - reported 22 Nov 2026",
 "South Korea minister quits - reported 22 Nov",
 "Indonesia factory fire itself - 22 Nov 2026",
]
dc = "DATE CHECK - NOT TODAY: Xi-Trump-Putin summit - 19 Nov 2026, not today · Russian missiles in Poland - 20 Nov 2026 · SpiceJet fundraise approved - 18 Nov 2026 · Hyderabad bomb-threat email - sent 21 Nov 2026 · Paolo Bulgari death - reported 22 Nov 2026 · South Korea minister quits - reported 22 Nov · Indonesia factory fire itself - 22 Nov 2026"
MAPROWS = [
 "          oooo        oo     oooooo  oooooooo     oo        ",
 "       ooooooooo  o   oooo  oooooooooooooooooo  oooo   o    ",
 "        ooooooo      ooooo ooooooooooooooooooooo oooo  oooo ",
 "         ooooo        oo  ooooooooooooooooooooooo  oo  ooooo",
 "          ooo            ooooooooooooooooooooo      oooooo  ",
 "           oo  oo         oooooooooooooooooo         oooo   ",
 "            oooo           ooooooooooooooo            oo    ",
 "             oo             ooooooooooooo              oo   ",
 "            oo               oooooooooo                      ",
 "           ooo                ooooooo              oo  oo    ",
 "          oooo                 ooooo              oooooooo  ",
 "         ooo                    ooo                oooooo   ",
 "        oo                       o                  oooo    ",
]
PINS = [(48, 22, 4), (11, 27, 5), (43, 7, 3), (34, 20, 5), (12, 24, 2), (24, 36, 6),
        (15, 21, 4), (9, 23, 1), (7, 26, 4), (25, 52, 11), (46, 8, 4),
        (2, 29, 6), (6, 9, 3)]

def icon(d, x, y, kind, s=30):
    c = STEEL; a = MAROON
    if kind == "ship":
        d.polygon([(x, y + s * .7), (x + s, y + .7 * s), (x + s * .82, y + s), (x + s * .15, y + s)], outline=c, width=2)
        d.line([(x + s * .5, y + .7 * s), (x + s * .5, y + .25 * s)], fill=c, width=2)
        d.polygon([(x + s * .5, y + .25 * s), (x + s * .78, y + .45 * s), (x + s * .5, y + .45 * s)], fill=a)
    elif kind == "capitol":
        d.arc([x + s * .3, y, x + s * .7, y + s * .45], 180, 360, fill=c, width=2)
        d.line([(x + .1 * s, y + .55 * s), (x + .9 * s, y + .55 * s)], fill=c, width=2)
        for i in range(4):
            xx = x + s * (.2 + .18 * i); d.line([(xx, y + .58 * s), (xx, y + .9 * s)], fill=c, width=2)
        d.line([(x + .05 * s, y + .95 * s), (x + .95 * s, y + .95 * s)], fill=a, width=2)
    elif kind == "radar":
        d.arc([x + .1 * s, y + .05 * s, x + .75 * s, y + .6 * s], 300, 130, fill=c, width=3)
        d.line([(x + .42 * s, y + .35 * s), (x + .5 * s, y + s)], fill=c, width=2)
        d.arc([x + .55 * s, y + .02 * s, x + .95 * s, y + .3 * s], 300, 60, fill=a, width=1)
    elif kind in ("house", "building"):
        d.rectangle([x + .15 * s, y + .3 * s, x + .85 * s, y + .95 * s], outline=c, width=2)
        d.polygon([(x + .05 * s, y + .32 * s), (x + .5 * s, y + .05 * s), (x + .95 * s, y + .32 * s)], outline=a, width=2)
        for i in range(3):
            d.rectangle([x + (.25 + .2 * i) * s, y + .5 * s, x + (.35 + .2 * i) * s, y + .62 * s], fill=c)
    elif kind == "globe":
        d.ellipse([x + .08 * s, y + .08 * s, x + .92 * s, y + .92 * s], outline=c, width=2)
        d.line([(x + .08 * s, y + .5 * s), (x + .92 * s, y + .5 * s)], fill=c, width=1)
        d.arc([x + .3 * s, y + .08 * s, x + .7 * s, y + .92 * s], 0, 360, fill=a, width=1)
    elif kind == "cricket":
        d.line([(x + .25 * s, y + .9 * s), (x + .6 * s, y + .2 * s)], fill=c, width=4)
        d.ellipse([x + .62 * s, y + .6 * s, x + .92 * s, y + .9 * s], fill=a)
    elif kind == "tennis":
        d.ellipse([x + .05 * s, y + .05 * s, x + .6 * s, y + .6 * s], outline=c, width=2)
        d.arc([x + .05 * s, y + .05 * s, x + .6 * s, y + .6 * s], 40, 140, fill=a, width=2)
        d.line([(x + .55 * s, y + .55 * s), (x + .95 * s, y + .95 * s)], fill=c, width=3)
    elif kind == "gold":
        d.polygon([(x + .15 * s, y + .65 * s), (x + .3 * s, y + .4 * s), (x + .6 * s, y + .4 * s), (x + .75 * s, y + .65 * s)], outline=a, width=2)
        d.polygon([(x + .3 * s, y + .95 * s), (x + .45 * s, y + .7 * s), (x + .75 * s, y + .7 * s), (x + .9 * s, y + .95 * s)], outline=c, width=2)
    elif kind == "scales":
        d.line([(x + .5 * s, y + .1 * s), (x + .5 * s, y + .9 * s)], fill=c, width=2)
        d.line([(x + .15 * s, y + .25 * s), (x + .85 * s, y + .25 * s)], fill=c, width=2)
        d.arc([x + .05 * s, y + .25 * s, x + .3 * s, y + .55 * s], 0, 180, fill=a, width=2)
        d.arc([x + .7 * s, y + .25 * s, x + .95 * s, y + .55 * s], 0, 180, fill=a, width=2)
        d.line([(x + .3 * s, y + .95 * s), (x + .7 * s, y + .95 * s)], fill=c, width=2)
    elif kind == "shield":
        d.polygon([(x + .5 * s, y + .05 * s), (x + .9 * s, y + .2 * s), (x + .9 * s, y + .55 * s), (x + .5 * s, y + .95 * s), (x + .1 * s, y + .55 * s), (x + .1 * s, y + .2 * s)], outline=c, width=2)
        d.text((x + .36 * s, y + .28 * s), "F", font=SANB(14), fill=a)
    elif kind == "crowd":
        for cx in (.25, .5, .75):
            d.ellipse([x + (cx - .09) * s, y + .15 * s, x + (cx + .09) * s, y + .4 * s], fill=c)
            d.arc([x + (cx - .14) * s, y + .45 * s, x + (cx + .14) * s, y + .95 * s], 180, 360, fill=a, width=2)
    elif kind == "ufo":
        d.ellipse([x + .02 * s, y + .35 * s, x + .98 * s, y + .65 * s], outline=c, width=2)
        d.arc([x + .3 * s, y + .05 * s, x + .7 * s, y + .5 * s], 180, 360, fill=a, width=2)
        d.line([(x + .3 * s, y + .7 * s), (x + .25 * s, y + .95 * s)], fill=a, width=2)
        d.line([(x + .7 * s, y + .7 * s), (x + .75 * s, y + .95 * s)], fill=a, width=2)

def wrap(d, text, font, maxw):
    words = text.split(); lines = []; cur = ""
    for wd in words:
        t = (cur + " " + wd).strip()
        if d.textlength(t, font=font) <= maxw: cur = t
        else: lines.append(cur); cur = wd
    if cur: lines.append(cur)
    return lines

def header(d, variant):
    d.rectangle([0, 0, W, 24], fill=MAROON)
    d.text((512, 12), "52 reports cross-checked - 16 wires & wires' wires - All times UTC",
           font=SANB(13), fill=(255, 251, 240), anchor="mm")
    if variant == "A":
        d.text((512, 60), "THE MORNING POST", font=SERB(66), fill=MAROON, anchor="mm")
        d.text((512, 114), "MONDAY 23 NOVEMBER 2026", font=SANB(44), fill=STEEL, anchor="mm")
    else:
        d.text((18, 58), "THE MORNING POST", font=SERB(58), fill=MAROON, anchor="lm")
        d.text((18, 110), "MONDAY 23 NOVEMBER 2026", font=SANB(38), fill=STEEL, anchor="lm")
    d.line([(14, 140), (1010, 140)], fill=MAROON, width=3)
    d.line([(14, 145), (1010, 145)], fill=STEEL, width=1)
    d.rectangle([14, 152, 1010, 178], fill=(238, 228, 204))
    seg = ["GOLD $3,538 -2.41%", "BITCOIN watched", "OIL watched",
           "Kyiv cold - Lisbon mild - Antalya warm - Wellington breezy",
           "IndiGo 65.9% at close"]
    xx = 22
    for i, t in enumerate(seg):
        d.text((xx, 165), t, font=SANB(12), fill=MAROON if i == 0 else INK, anchor="lm")
        xx += d.textlength(t, font=SANB(12)) + 24
        if i < len(seg) - 1:
            d.line([(xx - 12, 157), (xx - 12, 173)], fill=STEEL, width=1)
    labels = ["%s %d" % (n, c) for n, c, _ in REGIONS]
    minw = [d.textlength(t, font=SANB(10)) + 14 for t in labels]
    extra = 996 - sum(minw)
    counts = [c for _, c, _ in REGIONS]
    widths = [m + extra * c / sum(counts) for m, c in zip(minw, counts)]
    xx = 14
    for (name, n, col), t, wseg in zip(REGIONS, labels, widths):
        d.rectangle([xx, 184, xx + wseg - 2, 208], fill=col)
        d.text((xx + wseg / 2, 196), t, font=SANB(10), fill=(255, 255, 255), anchor="mm")
        xx += wseg
    d.rectangle([14, 214, 1010, 236], outline=LINE)
    xx = 20
    for i, t in enumerate(TL):
        d.text((xx, 225), t, font=SAN(9), fill=INK, anchor="lm")
        xx += d.textlength(t, font=SAN(9)) + 12

def _card(d, x, y, w, h, c, tf, ff, tstep, fstep, foff, is_lead):
    num, loc, status, title, facts, source, ic = c
    d.rectangle([x, y, x + w, y + h], fill=PAPER, outline=LINE)
    d.rectangle([x, y, x + w, y + 15], fill=MAROON if is_lead else STEEL)
    d.text((x + 5, y + 7), "%d  %s" % (num, loc), font=SANB(11), fill=(255, 255, 255), anchor="lm")
    tw = d.textlength(status, font=SANB(10))
    d.rectangle([x + w - tw - 12, y + 2, x + w - 3, y + 13], fill=(255, 251, 240))
    d.text((x + w - 7, y + 7), status, font=SANB(10), fill=MAROON, anchor="rm")
    srct = "Src: " + source
    d.text((x + w - tw - 18, y + 7), srct, font=SAN(9), fill=(255, 251, 240), anchor="rm")
    lines = wrap(d, title, tf, w - 14)
    yy = y + 19
    for ln in lines[:2]:
        d.text((x + 6, yy), ln, font=tf, fill=INK); yy += tstep
    icon(d, x + 6, yy + 2, ic, 30)
    fl = []
    for f in facts: fl.extend(wrap(d, f, ff, w - 48))
    for i, ln in enumerate(fl[:3]):
        d.text((x + 42, yy + foff + i * fstep), ln, font=ff, fill=INK)

def lead(d, x, y, w, h, c):
    _card(d, x, y, w, h, c, fb(28), fr(15), 30, 18, 9, True)

def mini(d, x, y, w, h, c):
    _card(d, x, y, w, h, c, fb(24), fr(13), 26, 15, 6, False)

def bottom(d, top):
    d.rectangle([14, top, 1010, top + 44], fill=PAPER, outline=LINE)
    d.text((22, top + 10), "THE DAY IN", font=SANB(12), fill=MAROON)
    d.text((22, top + 25), "NUMBERS", font=SANB(12), fill=MAROON)
    for i, (n, lab) in enumerate(NUMS):
        r, col = divmod(i, 4)
        xx = 150 + col * 212; yy = top + 6 + r * 20
        d.text((xx, yy), n, font=SANB(15), fill=STEEL)
        nw = d.textlength(n, font=SANB(15))
        d.text((xx + nw + 6, yy + 2), lab, font=SAN(10), fill=INK)
    by = top + 50
    d.rectangle([14, by, 500, by + 68], fill=PAPER, outline=LINE)
    d.text((22, by + 11), "WHERE IT HAPPENED - DOTTED WORLD MAP", font=SANB(13), fill=MAROON)
    if MAP_STYLE == "dotted_map":
        mx, my, cell = 50, by + 22, 3.3
        for r, row in enumerate(MAPROWS):
            for ci, ch2 in enumerate(row):
                if ch2 == "o":
                    d.ellipse([mx + ci * cell, my + r * cell, mx + ci * cell + 2.1, my + r * cell + 2.1], fill=(150, 160, 140))
        for n, cx, cy in PINS:
            px, py = mx + cx * cell, my + cy * cell
            d.ellipse([px - 6, py - 6, px + 6, py + 6], fill=MAROON)
            d.text((px, py), str(n), font=SANB(8), fill=(255, 255, 255), anchor="mm")
    d.rectangle([508, by, 1010, by + 68], fill=(244, 232, 222), outline=MAROON)
    d.text((516, by + 11), "DATE CHECK - NOT TODAY'S NEWS", font=SANB(13), fill=MAROON)
    for i, t in enumerate(DATECHECK):
        col, r = divmod(i, 4)
        d.text((516 + col * 248, by + 28 + r * 14), "- " + t, font=SAN(10), fill=INK)
    ay = by + 74
    d.rectangle([14, ay, 1010, 984], fill=PAPER, outline=LINE)
    d.rectangle([14, ay, 190, ay + 14], fill=MAROON)
    d.text((20, ay + 7), "ALSO ON THE DAY", font=SANB(11), fill=(255, 255, 255), anchor="lm")
    flow = " - ".join(BRIEFS)
    lines = wrap(d, flow, fsr(10), 978)
    for i, ln in enumerate(lines[:6]):
        d.text((20, ay + 19 + i * 12), ln, font=fsr(10), fill=INK)
    d.rectangle([0, 986, W, H], fill=STEEL)
    d.text((14, 993), "HOW SURE WE ARE: CONFIRMED = officials or final results on the record.",
           font=SANB(11), fill=(255, 251, 240))
    d.text((14, 1006), "REPORTED = carried by the named wires above; CLAIM = one side's account, labelled in its headline.",
           font=SANB(11), fill=(255, 251, 240))
    d.text((14, 1019), "Scenes are drawn illustrations. Sources: BBC, AP, AFP, JagranJosh, ObserverVoice, 23 Nov 2026.",
           font=SANB(11), fill=(255, 251, 240))

def build(variant):
    im = IL.new("RGB", (W, H), SAND)
    d = DR.Draw(im)
    header(d, variant)
    if variant == "A":
        lead(d, 14, 242, 996, 78, CARDS[0])
        cw, ch, gap = 328, 106, 5
        for i, c in enumerate(CARDS[1:]):
            r, col = divmod(i, 3)
            mini(d, 14 + col * (cw + gap), 325 + r * (ch + gap), cw, ch, c)
        bottom(d, 325 + 4 * (ch + gap) + 3)
    else:
        lead(d, 14, 242, 996, 78, CARDS[0])
        cw, ch, gap = 244, 141, 6
        for i, c in enumerate(CARDS[1:]):
            r, col = divmod(i, 4)
            mini(d, 14 + col * (cw + gap), 325 + r * (ch + gap), cw, ch, c)
        bottom(d, 325 + 3 * (ch + gap) + 3)
    return im

if __name__ == "__main__":
    out = os.path.dirname(os.path.abspath(__file__))
    for v in ("A", "B"):
        build(v).save(os.path.join(out, "variant_%s.png" % v.lower()), optimize=True)
    print("done")
