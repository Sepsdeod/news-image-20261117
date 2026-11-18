#!/usr/bin/env python3
"""Draw the front-page poster for Tuesday 17 November 2026.

Build tooling for the make.fun news-image-20261117 entry. All graphics are
drawn by this script with PIL: typography, rules and simple shapes only.
Output: entry.png (1024x1024, PNG).
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)   # off-white newsprint
INK = (18, 18, 18)        # near-black
RED = (176, 30, 30)       # accent red
GREY = (90, 86, 78)

SERIF = "/usr/share/fonts/truetype/liberation/LiberationSerif-Bold.ttf"
SERIF_REG = "/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf"
SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_width):
    """Greedy word wrap returning a list of lines that fit max_width."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += leading
    return y

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)
MX = 36                      # side margin
CW = W - 2 * MX              # content width

# ---------- masthead ----------
y = 22
d.rectangle([MX, y, W - MX, y + 4], fill=INK)
y += 14
mast = font(SERIF, 84)
d.text((W / 2, y), "THE WORLD", font=mast, fill=INK, anchor="ma")
y += 92
d.rectangle([MX, y, W - MX, y + 2], fill=INK)
y += 8
date_f = font(SANS_BOLD, 28)
d.text((W / 2, y), "TUESDAY 17 NOVEMBER 2026", font=date_f, fill=RED, anchor="ma")
y += 38
sub_f = font(SANS, 19)
d.text((W / 2, y), "THE DAY IN SEVEN STORIES  —  FROM KYIV TO MANILA",
       font=sub_f, fill=GREY, anchor="ma")
y += 26
d.rectangle([MX, y, W - MX, y + 4], fill=INK)
y += 14

# ---------- lead story ----------
kick_f = font(SANS_BOLD, 20)
d.text((MX, y), "UKRAINE WAR  •  LEAD STORY", font=kick_f, fill=RED)
y += 28
head_f = font(SERIF, 48)
head_lines = wrap(d, "Kerch Bridge collapses as Ukraine strikes the Crimea link",
                  head_f, CW)
y = draw_lines(d, head_lines, MX, y, head_f, INK, 54)
y += 6
body_f = font(SANS, 21)
body = ("A section of the road bridge linking Russia to occupied Crimea fell "
        "after a Ukrainian strike — the second attack in two days. Russia hit "
        "Kyiv's bridges over the Dnipro, disrupting power, water and heating.")
body_lines = wrap(d, body, body_f, CW)
y = draw_lines(d, body_lines, MX, y, body_f, INK, 27)
y += 10

# Drawn bridge: two towers, a deck with a broken middle span (red sag + crack).
bx0, bx1 = MX, W - MX
by = y + 26
mid = (bx0 + bx1) // 2
tower_l, tower_r = bx0 + 150, bx1 - 150
# suspension cables from tower tops to deck
for tx in (tower_l, tower_r):
    d.line([tx, by - 56, tx - 130, by], fill=INK, width=2)
    d.line([tx, by - 56, tx + 130, by], fill=INK, width=2)
# towers: upright + crossbar
for tx in (tower_l, tower_r):
    d.rectangle([tx - 8, by - 56, tx + 8, by], fill=INK)
    d.rectangle([tx - 28, by - 56, tx + 28, by - 48], fill=INK)
# deck, with a gap in the middle
d.line([bx0, by, mid - 60, by], fill=INK, width=5)
d.line([mid + 60, by, bx1, by], fill=INK, width=5)
# broken span sags down in red, with a jagged crack above it
d.line([mid - 60, by, mid, by + 18, mid + 60, by], fill=RED, width=3)
crack = [(mid - 18, by - 2), (mid - 8, by - 12), (mid + 2, by - 2),
         (mid + 12, by - 12), (mid + 22, by - 2)]
d.line(crack, fill=RED, width=3)
y = by + 26
d.rectangle([MX, y, W - MX, y + 2], fill=INK)
y += 12

# ---------- story grid: 2 rows x 3 columns ----------
stories = [
    ("MIDDLE EAST",
     "Tankers hit by mines near Hormuz",
     "Iran says two oil tankers struck mines by the Strait of Hormuz as a "
     "third US carrier arrived in the region. Iran also fired drones at a US "
     "radar base in Bahrain; no casualties were reported."),
    ("ASIA",
     "Trump lands in Manila; Xi, Trump and Putin to meet",
     "President Trump arrived in the Philippines for the ASEAN summit. China "
     "confirmed a first three-way meeting of Xi, Trump and Putin in Shenzhen "
     "on Thursday."),
    ("MARKETS",
     "Stocks slide; Nvidia beats after the bell",
     "The S&P 500 fell 1.0% to its lowest close since July. After hours, "
     "Nvidia beat forecasts with $115.8bn revenue in its first report since "
     "Jensen Huang resigned."),
    ("BANKING",
     "JPMorgan blames software bug for bank outage",
     "A software bug slowed online banking, branches and Zelle payments at "
     "major US banks on Monday. JPMorgan said there was no sign of a "
     "cyberattack."),
    ("WEST BANK",
     "UK sanctions settlement builders",
     "Britain sanctioned eight Israeli firms building West Bank settlements. "
     "Palestinian officials said settlers killed a 72-year-old woman near "
     "Jericho overnight."),
    ("DEFENCE",
     "Pentagon fails audit for ninth year",
     "Auditors again could not verify Pentagon accounts covering more than "
     "$4.8 trillion in assets, issuing a disclaimer of opinion for fiscal "
     "2026."),
]

gap = 18
col_w = (CW - 2 * gap) // 3
row_h = 218
card_kick = font(SANS_BOLD, 17)
card_head = font(SERIF, 25)
card_body = font(SANS, 18)

for i, (kicker, headline, text) in enumerate(stories):
    r, c = divmod(i, 3)
    x0 = MX + c * (col_w + gap)
    y0 = y + r * (row_h + 14)
    d.rectangle([x0, y0, x0 + col_w, y0 + 3], fill=RED)
    cy = y0 + 12
    d.text((x0, cy), kicker, font=card_kick, fill=RED)
    cy += 26
    hl = wrap(d, headline, card_head, col_w)
    cy = draw_lines(d, hl, x0, cy, card_head, INK, 29)
    cy += 4
    bl = wrap(d, text, card_body, col_w)
    draw_lines(d, bl, x0, cy, card_body, INK, 23)

y = y + 2 * (row_h + 14) - 14 + 8

# ---------- footer ----------
d.rectangle([MX, y, W - MX, y + 2], fill=INK)
y += 10
foot_f = font(SANS, 16)
d.text((W / 2, y),
       "THE WORLD  •  Tuesday 17 November 2026  •  All events of 17 November 2026",
       font=foot_f, fill=GREY, anchor="ma")

img.save("entry.png", format="PNG", optimize=True)
print("saved entry.png")
