
from pathlib import Path
import math, textwrap, html
import yaml

ROOT = Path(__file__).resolve().parents[1]

def load_yaml(rel):
    with open(ROOT / rel, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

GAME = load_yaml("data/game.yaml")
BOARD = load_yaml("data/board.yaml")
CARDS = load_yaml("data/cards.yaml")
REF = load_yaml("data/reference-card.yaml")
STYLE = load_yaml("data/visual-style.yaml")

P = STYLE["palette"]
TILES = STYLE["tiles"]

def esc(s):
    return html.escape(str(s), quote=False)

def mm(n):
    return f"{n:.2f}"

def svg_header(width_mm, height_mm):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{mm(width_mm)}mm" height="{mm(height_mm)}mm" viewBox="0 0 {mm(width_mm)} {mm(height_mm)}">'

def wrap_text(text, max_chars):
    text = str(text).strip()
    if not text:
        return []
    return textwrap.wrap(text, width=max_chars, break_long_words=False, break_on_hyphens=False)

def svg_text_lines(x, y, lines, font_size=3, line_gap=1.1, fill=None, weight=None, anchor="start", family="Arial"):
    if fill is None:
        fill = P["ink"]
    parts = []
    yy = y
    for line in lines:
        attrs = [
            f'x="{mm(x)}"',
            f'y="{mm(yy)}"',
            f'font-family="{family}"',
            f'font-size="{font_size}"',
            f'fill="{fill}"',
            f'text-anchor="{anchor}"'
        ]
        if weight:
            attrs.append(f'font-weight="{weight}"')
        parts.append(f'<text {" ".join(attrs)}>{esc(line)}</text>')
        yy += font_size * line_gap
    return "\n".join(parts), yy

def svg_bullet_text(x, y, bullet, max_chars, font_size=3, line_gap=1.1, fill=None, anchor="start", family="Arial"):
    if fill is None:
        fill = P["ink"]
    lines = wrap_text(bullet, max_chars)
    parts = []
    yy = y

    if ":" in bullet and lines:
        prefix, _ = bullet.split(":", 1)
        prefix = prefix + ":"
        first_line = lines[0]
        if first_line.startswith(prefix):
            remainder = first_line[len(prefix):].lstrip()
            attrs = [
                f'x="{mm(x)}"',
                f'y="{mm(yy)}"',
                f'font-family="{family}"',
                f'font-size="{font_size}"',
                f'fill="{fill}"',
                f'text-anchor="{anchor}"'
            ]
            if remainder:
                parts.append(
                    f'<text {" ".join(attrs)}><tspan font-weight="bold">{esc(prefix)}</tspan><tspan> {esc(remainder)}</tspan></text>'
                )
            else:
                parts.append(
                    f'<text {" ".join(attrs)}><tspan font-weight="bold">{esc(prefix)}</tspan></text>'
                )
            yy += font_size * line_gap
            for line in lines[1:]:
                attrs = [
                    f'x="{mm(x)}"',
                    f'y="{mm(yy)}"',
                    f'font-family="{family}"',
                    f'font-size="{font_size}"',
                    f'fill="{fill}"',
                    f'text-anchor="{anchor}"'
                ]
                parts.append(f'<text {" ".join(attrs)}>{esc(line)}</text>')
                yy += font_size * line_gap
            return "\n".join(parts), yy

    return svg_text_lines(x, y, lines, font_size=font_size, line_gap=line_gap, fill=fill, anchor=anchor, family=family)

def panel(x, y, w, h, title, title_fill, body_fill=None, title_text_fill="#fffaf0"):
    if body_fill is None:
        body_fill = P["panel_bg"]
    return f'''
    <rect x="{mm(x)}" y="{mm(y)}" width="{mm(w)}" height="{mm(h)}" rx="2.8" fill="{body_fill}" stroke="{P["frame"]}" stroke-width="0.45"/>
    <rect x="{mm(x)}" y="{mm(y)}" width="{mm(w)}" height="6.8" rx="2.8" fill="{title_fill}"/>
    <rect x="{mm(x)}" y="{mm(y+5.2)}" width="{mm(w)}" height="1.6" fill="{title_fill}"/>
    <text x="{mm(x+3)}" y="{mm(y+4.45)}" font-family="Arial" font-size="3.3" font-weight="bold" fill="{title_text_fill}">{esc(title)}</text>
    '''

def icon_group(tile_type, cx, cy, size):
    s = size
    half = s / 2
    col = TILES[tile_type]["stroke"]
    fill = P["panel_bg"]
    def tx(px): return cx - half + px * s
    def ty(py): return cy - half + py * s

    if tile_type == "Skog":
        return f'''
        <rect x="{mm(cx-half)}" y="{mm(cy-half)}" width="{mm(s)}" height="{mm(s)}" rx="{mm(s*0.18)}" fill="{fill}" stroke="{col}" stroke-width="0.45"/>
        <polygon points="{mm(tx(0.50))},{mm(ty(0.12))} {mm(tx(0.22))},{mm(ty(0.48))} {mm(tx(0.78))},{mm(ty(0.48))}" fill="{col}"/>
        <polygon points="{mm(tx(0.50))},{mm(ty(0.30))} {mm(tx(0.18))},{mm(ty(0.72))} {mm(tx(0.82))},{mm(ty(0.72))}" fill="{col}"/>
        <rect x="{mm(tx(0.45))}" y="{mm(ty(0.72))}" width="{mm(s*0.10)}" height="{mm(s*0.14)}" fill="{P["frame_dark"]}"/>
        '''
    if tile_type == "Berg":
        return f'''
        <rect x="{mm(cx-half)}" y="{mm(cy-half)}" width="{mm(s)}" height="{mm(s)}" rx="{mm(s*0.18)}" fill="{fill}" stroke="{col}" stroke-width="0.45"/>
        <polygon points="{mm(tx(0.12))},{mm(ty(0.76))} {mm(tx(0.42))},{mm(ty(0.30))} {mm(tx(0.64))},{mm(ty(0.76))}" fill="{col}"/>
        <polygon points="{mm(tx(0.35))},{mm(ty(0.76))} {mm(tx(0.70))},{mm(ty(0.18))} {mm(tx(0.90))},{mm(ty(0.76))}" fill="{col}" opacity="0.9"/>
        '''
    if tile_type == "Äng":
        return f'''
        <rect x="{mm(cx-half)}" y="{mm(cy-half)}" width="{mm(s)}" height="{mm(s)}" rx="{mm(s*0.18)}" fill="{fill}" stroke="{col}" stroke-width="0.45"/>
        <circle cx="{mm(tx(0.50))}" cy="{mm(ty(0.49))}" r="{mm(s*0.08)}" fill="{col}"/>
        <circle cx="{mm(tx(0.50))}" cy="{mm(ty(0.31))}" r="{mm(s*0.10)}" fill="{col}" opacity="0.95"/>
        <circle cx="{mm(tx(0.65))}" cy="{mm(ty(0.40))}" r="{mm(s*0.10)}" fill="{col}" opacity="0.95"/>
        <circle cx="{mm(tx(0.62))}" cy="{mm(ty(0.58))}" r="{mm(s*0.10)}" fill="{col}" opacity="0.95"/>
        <circle cx="{mm(tx(0.38))}" cy="{mm(ty(0.58))}" r="{mm(s*0.10)}" fill="{col}" opacity="0.95"/>
        <circle cx="{mm(tx(0.35))}" cy="{mm(ty(0.40))}" r="{mm(s*0.10)}" fill="{col}" opacity="0.95"/>
        '''
    if tile_type == "Grotta":
        return f'''
        <rect x="{mm(cx-half)}" y="{mm(cy-half)}" width="{mm(s)}" height="{mm(s)}" rx="{mm(s*0.18)}" fill="{fill}" stroke="{col}" stroke-width="0.45"/>
        <path d="M {mm(tx(0.18))} {mm(ty(0.72))} Q {mm(tx(0.22))} {mm(ty(0.32))} {mm(tx(0.50))} {mm(ty(0.20))} Q {mm(tx(0.78))} {mm(ty(0.32))} {mm(tx(0.82))} {mm(ty(0.72))} Z" fill="{col}"/>
        <path d="M {mm(tx(0.36))} {mm(ty(0.72))} Q {mm(tx(0.38))} {mm(ty(0.46))} {mm(tx(0.50))} {mm(ty(0.42))} Q {mm(tx(0.62))} {mm(ty(0.46))} {mm(tx(0.64))} {mm(ty(0.72))} Z" fill="{fill}"/>
        '''
    if tile_type == "Ruin":
        return f'''
        <rect x="{mm(cx-half)}" y="{mm(cy-half)}" width="{mm(s)}" height="{mm(s)}" rx="{mm(s*0.18)}" fill="{fill}" stroke="{col}" stroke-width="0.45"/>
        <rect x="{mm(tx(0.20))}" y="{mm(ty(0.28))}" width="{mm(s*0.18)}" height="{mm(s*0.42)}" fill="{col}"/>
        <rect x="{mm(tx(0.46))}" y="{mm(ty(0.22))}" width="{mm(s*0.18)}" height="{mm(s*0.48)}" fill="{col}"/>
        <rect x="{mm(tx(0.72))}" y="{mm(ty(0.34))}" width="{mm(s*0.10)}" height="{mm(s*0.36)}" fill="{col}"/>
        <rect x="{mm(tx(0.18))}" y="{mm(ty(0.20))}" width="{mm(s*0.22)}" height="{mm(s*0.06)}" fill="{col}"/>
        <rect x="{mm(tx(0.44))}" y="{mm(ty(0.14))}" width="{mm(s*0.22)}" height="{mm(s*0.06)}" fill="{col}"/>
        '''
    if tile_type == "Stig":
        return f'''
        <rect x="{mm(cx-half)}" y="{mm(cy-half)}" width="{mm(s)}" height="{mm(s)}" rx="{mm(s*0.18)}" fill="{fill}" stroke="{col}" stroke-width="0.45"/>
        <path d="M {mm(tx(0.18))} {mm(ty(0.66))} C {mm(tx(0.28))} {mm(ty(0.52))}, {mm(tx(0.38))} {mm(ty(0.58))}, {mm(tx(0.46))} {mm(ty(0.42))} C {mm(tx(0.56))} {mm(ty(0.20))}, {mm(tx(0.68))} {mm(ty(0.26))}, {mm(tx(0.78))} {mm(ty(0.18))}" fill="none" stroke="{col}" stroke-width="{mm(s*0.10)}" stroke-linecap="round"/>
        <circle cx="{mm(tx(0.20))}" cy="{mm(ty(0.66))}" r="{mm(s*0.06)}" fill="{col}"/>
        <circle cx="{mm(tx(0.45))}" cy="{mm(ty(0.44))}" r="{mm(s*0.05)}" fill="{col}"/>
        <circle cx="{mm(tx(0.76))}" cy="{mm(ty(0.20))}" r="{mm(s*0.06)}" fill="{col}"/>
        '''
    if tile_type == "Bas":
        return f'''
        <rect x="{mm(cx-half)}" y="{mm(cy-half)}" width="{mm(s)}" height="{mm(s)}" rx="{mm(s*0.18)}" fill="{fill}" stroke="{col}" stroke-width="0.45"/>
        <polygon points="{mm(tx(0.16))},{mm(ty(0.46))} {mm(tx(0.50))},{mm(ty(0.18))} {mm(tx(0.84))},{mm(ty(0.46))}" fill="{col}"/>
        <rect x="{mm(tx(0.24))}" y="{mm(ty(0.46))}" width="{mm(s*0.52)}" height="{mm(s*0.30)}" fill="{col}"/>
        <rect x="{mm(tx(0.44))}" y="{mm(ty(0.56))}" width="{mm(s*0.12)}" height="{mm(s*0.20)}" fill="{fill}"/>
        '''
    if tile_type == "Fyrplats":
        return f'''
        <rect x="{mm(cx-half)}" y="{mm(cy-half)}" width="{mm(s)}" height="{mm(s)}" rx="{mm(s*0.18)}" fill="{fill}" stroke="{col}" stroke-width="0.45"/>
        <polygon points="{mm(tx(0.36))},{mm(ty(0.76))} {mm(tx(0.64))},{mm(ty(0.76))} {mm(tx(0.58))},{mm(ty(0.30))} {mm(tx(0.42))},{mm(ty(0.30))}" fill="{col}"/>
        <rect x="{mm(tx(0.40))}" y="{mm(ty(0.22))}" width="{mm(s*0.20)}" height="{mm(s*0.10)}" fill="{col}"/>
        <path d="M {mm(tx(0.28))} {mm(ty(0.22))} Q {mm(tx(0.18))} {mm(ty(0.18))} {mm(tx(0.16))} {mm(ty(0.10))}" fill="none" stroke="{col}" stroke-width="{mm(s*0.05)}" stroke-linecap="round"/>
        <path d="M {mm(tx(0.72))} {mm(ty(0.22))} Q {mm(tx(0.82))} {mm(ty(0.18))} {mm(tx(0.84))} {mm(ty(0.10))}" fill="none" stroke="{col}" stroke-width="{mm(s*0.05)}" stroke-linecap="round"/>
        '''
    return f'<circle cx="{mm(cx)}" cy="{mm(cy)}" r="{mm(size*0.25)}" fill="{col}"/>'

def write_tile_icon_assets():
    out_dir = ROOT / "assets/style/tile-icons"
    out_dir.mkdir(parents=True, exist_ok=True)
    for tile_type in TILES.keys():
        icon = [svg_header(24,24), icon_group(tile_type, 12, 12, 14), '</svg>']
        name = tile_type.lower().replace("ä","a").replace("å","a").replace("ö","o")
        (out_dir / f'{name}.svg').write_text("\n".join(icon), encoding="utf-8")

def build_reference_svg():
    width, height = 105, 148
    margin = 6
    gutter = 4
    col_w = (width - margin*2 - gutter) / 2

    left_titles = ["Start", "Tur & handlingar", "Mat", "Basen"]
    right_titles = ["Nattfas", "Platser", "Fyren"]
    sec_map = {s["title"]: s["bullets"] for s in REF["sections"]}

    def section_height(title, bullets):
        base = 9.2
        body = 0
        for b in bullets:
            max_chars = 28 if title != "Platser" else 26
            lines = wrap_text(b, max_chars)
            body += max(1, len(lines)) * 3.0 + 0.9
        return max(18, base + body + 3)

    left_sections = [(t, sec_map.get(t, []), section_height(t, sec_map.get(t, []))) for t in left_titles]
    right_sections = [(t, sec_map.get(t, []), section_height(t, sec_map.get(t, []))) for t in right_titles]
    usable_h = height - 24 - margin

    def scale_sections(sections):
        total = sum(h for _,_,h in sections) + (len(sections)-1)*3
        if total > usable_h:
            scale = (usable_h - (len(sections)-1)*3) / sum(h for _,_,h in sections)
        else:
            scale = 1.0
        return [(t,b,h*scale) for t,b,h in sections]

    left_sections = scale_sections(left_sections)
    right_sections = scale_sections(right_sections)

    title_colors = {
        "Start": P["accent"],
        "Tur & handlingar": TILES["Bas"]["stroke"],
        "Mat": TILES["Äng"]["stroke"],
        "Basen": TILES["Bas"]["stroke"],
        "Nattfas": P["dark_track"],
        "Platser": TILES["Skog"]["stroke"],
        "Fyren": TILES["Fyrplats"]["stroke"],
    }

    parts = [svg_header(width, height)]
    parts.append(f'<rect x="0" y="0" width="{mm(width)}" height="{mm(height)}" fill="{P["page_bg"]}"/>')
    parts.append(f'<rect x="{mm(margin-1)}" y="{mm(margin-1)}" width="{mm(width-2*(margin-1))}" height="{mm(height-2*(margin-1))}" rx="4" fill="{P["panel_alt"]}" stroke="{P["frame"]}" stroke-width="0.65"/>')
    parts.append(f'<rect x="{mm(margin)}" y="{mm(margin)}" width="{mm(width-2*margin)}" height="14" rx="3.5" fill="{P["frame_dark"]}"/>')
    parts.append(f'<text x="{mm(width/2)}" y="{mm(margin+5.6)}" text-anchor="middle" font-family="Arial" font-size="5" font-weight="bold" fill="#fff7e9">{esc(GAME["title"])}</text>')
    parts.append(f'<text x="{mm(width/2)}" y="{mm(margin+10.5)}" text-anchor="middle" font-family="Arial" font-size="2.8" fill="#f0e4c9">Referenskort</text>')
    parts.append(f'<text x="{mm(width-margin-1.5)}" y="{mm(height-margin+0.2)}" text-anchor="end" font-family="Arial" font-size="1.9" fill="{P["muted"]}">styled v0.7.5</text>')

    def draw_section(x, y, w, h, title, bullets):
        parts.append(panel(x, y, w, h, title, title_colors.get(title, P["accent"])))
        ty = y + 10.8
        max_chars = 29 if w >= 44 else 27
        for idx, b in enumerate(bullets):
            parts.append(f'<circle cx="{mm(x+2.1)}" cy="{mm(ty-0.9)}" r="0.55" fill="{P["frame"]}"/>')
            fyr_indent = title == "Fyren" and 1 <= idx <= 3
            text_x = x + (6.0 if fyr_indent else 3.6)
            txt, ty2 = svg_bullet_text(
                text_x,
                ty,
                b,
                max_chars - (2 if fyr_indent else 0),
                font_size=2.55,
                line_gap=1.14
            )
            parts.append(txt)
            ty = ty2 + 0.75

    y_left = margin + 17
    for title, bullets, h in left_sections:
        draw_section(margin, y_left, col_w, h, title, bullets)
        y_left += h + 3

    y_right = margin + 17
    for title, bullets, h in right_sections:
        draw_section(margin + col_w + gutter, y_right, col_w, h, title, bullets)
        y_right += h + 3

    parts.append('</svg>')
    return "\n".join(parts)

def build_reference_a4_4up(a6_svg):
    width, height = 210, 297
    margin = 10
    gap_x = 6
    gap_y = 6
    card_w = 105
    card_h = 148
    inner = a6_svg.split(">", 1)[1].rsplit("</svg>", 1)[0]
    positions = [(margin, margin), (margin+card_w+gap_x, margin), (margin, margin+card_h+gap_y), (margin+card_w+gap_x, margin+card_h+gap_y)]
    parts = [svg_header(width, height), f'<rect x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>']
    for x, y in positions:
        parts.append(f'<g transform="translate({mm(x)},{mm(y)})">{inner}</g>')
    parts.append('</svg>')
    return "\n".join(parts)

def build_board_svg():
    width, height = 210, 297
    margin = 10
    gap = 4
    sidebar_w = 34
    grid_w = width - 2*margin - sidebar_w - gap
    grid_h = 180
    cols = BOARD["grid"]["columns"]
    rows = BOARD["grid"]["rows"]
    cell_gap = 3
    cell_w = (grid_w - cell_gap*(cols-1)) / cols
    cell_h = (grid_h - cell_gap*(rows-1)) / rows
    grid_x = margin
    grid_y = 28
    layout = BOARD["grid"]["layout"]

    parts = [svg_header(width, height)]
    parts.append(f'<rect x="0" y="0" width="{width}" height="{height}" fill="{P["page_bg"]}"/>')
    parts.append(f'<rect x="{mm(margin-2)}" y="{mm(margin-2)}" width="{mm(width-2*(margin-2))}" height="{mm(height-2*(margin-2))}" rx="5" fill="{P["panel_alt"]}" stroke="{P["frame"]}" stroke-width="0.8"/>')
    parts.append(f'<rect x="{mm(margin)}" y="{mm(margin)}" width="{mm(width-2*margin)}" height="14" rx="3.5" fill="{P["frame_dark"]}"/>')
    parts.append(f'<text x="{mm(width/2)}" y="{mm(margin+5.7)}" text-anchor="middle" font-family="Arial" font-size="6" font-weight="bold" fill="#fff8eb">{esc(GAME["title"])}</text>')
    parts.append(f'<text x="{mm(width/2)}" y="{mm(margin+10.8)}" text-anchor="middle" font-family="Arial" font-size="2.8" fill="#e6d6b7">Spelplan</text>')
    parts.append(f'<rect x="{mm(grid_x-2)}" y="{mm(grid_y-2)}" width="{mm(grid_w+4)}" height="{mm(grid_h+4)}" rx="4" fill="{P["panel_bg"]}" stroke="{P["frame"]}" stroke-width="0.5"/>')

    for r in range(rows):
        for c in range(cols):
            tile = layout[r][c]
            x = grid_x + c*(cell_w + cell_gap)
            y = grid_y + r*(cell_h + cell_gap)
            fill = TILES[tile]["fill"]
            stroke = TILES[tile]["stroke"]
            parts.append(f'<rect x="{mm(x)}" y="{mm(y)}" width="{mm(cell_w)}" height="{mm(cell_h)}" rx="3" fill="{fill}" stroke="{stroke}" stroke-width="0.8"/>')
            parts.append(f'<rect x="{mm(x)}" y="{mm(y)}" width="{mm(cell_w)}" height="7.2" rx="3" fill="{stroke}" opacity="0.15"/>')
            parts.append(icon_group(tile, x + cell_w/2, y + cell_h/2 - 2.8, min(cell_w, cell_h)*0.30))
            parts.append(f'<text x="{mm(x+cell_w/2)}" y="{mm(y+cell_h-6.2)}" text-anchor="middle" font-family="Arial" font-size="3.2" font-weight="bold" fill="{P["ink"]}">{esc(tile)}</text>')

    track_x = grid_x + grid_w + gap
    track_y = grid_y
    track_w = sidebar_w
    track_h = grid_h
    values = BOARD["darkness_track"]["values"]
    n = len(values)
    step_h = (track_h - 13) / n
    parts.append(f'<rect x="{mm(track_x)}" y="{mm(track_y)}" width="{mm(track_w)}" height="{mm(track_h)}" rx="4" fill="{P["panel_bg"]}" stroke="{P["frame"]}" stroke-width="0.6"/>')
    parts.append(f'<rect x="{mm(track_x)}" y="{mm(track_y)}" width="{mm(track_w)}" height="11" rx="4" fill="{P["dark_track"]}"/>')
    parts.append(f'<text x="{mm(track_x+track_w/2)}" y="{mm(track_y+4.7)}" text-anchor="middle" font-family="Arial" font-size="3.5" font-weight="bold" fill="#f8f2ff">MÖRKER</text>')
    parts.append(f'<text x="{mm(track_x+track_w/2)}" y="{mm(track_y+8.8)}" text-anchor="middle" font-family="Arial" font-size="2.1" fill="#e2d9f0">räknar ned mot 0</text>')
    for i, v in enumerate(values):
        yy = track_y + 13 + i*step_h
        fill = "#f5e6e1" if v <= 2 else "#f6f1ea" if v <= 5 else "#eee7f7"
        if v == 10:
            fill = "#e4f1e6"
        parts.append(f'<rect x="{mm(track_x+4)}" y="{mm(yy)}" width="{mm(track_w-8)}" height="{mm(step_h-1.2)}" rx="2" fill="{fill}" stroke="{P["line"]}" stroke-width="0.35"/>')
        parts.append(f'<text x="{mm(track_x+track_w/2)}" y="{mm(yy+(step_h/2)+1.2)}" text-anchor="middle" font-family="Arial" font-size="4.1" font-weight="bold" fill="{P["ink"]}">{v}</text>')

    parts.append(f'<text x="{mm(width-margin)}" y="{mm(height-margin+0.2)}" text-anchor="end" font-family="Arial" font-size="2.0" fill="{P["muted"]}">styled v0.7.2</text>')
    parts.append('</svg>')
    return "\n".join(parts)

def card_backdrop(x, y, w, h, header_fill, stroke):
    return f'''
    <rect x="{mm(x)}" y="{mm(y)}" width="{mm(w)}" height="{mm(h)}" rx="2.5" fill="#ffffff" stroke="{stroke}" stroke-width="0.65"/>
    <rect x="{mm(x)}" y="{mm(y)}" width="{mm(w)}" height="11.6" rx="2.5" fill="{header_fill}" opacity="0.96"/>
    <rect x="{mm(x+2.2)}" y="{mm(y+13.2)}" width="{mm(w-4.4)}" height="{mm(h-17.2)}" rx="1.8" fill="#fffdf9" stroke="#d8ccb8" stroke-width="0.25"/>
    '''

def build_card_sheet(deck_name):
    layouts = load_yaml("data/print-layouts.yaml")["print_layouts"]
    layout_id = f"cards_{deck_name}_a4_4x4"
    cfg = [x for x in layouts if x["id"] == layout_id][0]
    paper = cfg["paper"]
    grid = cfg["grid"]
    card = cfg["card"]
    width, height = paper["width_mm"], paper["height_mm"]
    margin = paper["margin_mm"]
    cols, rows = grid["cols"], grid["rows"]
    gap = grid["gap_mm"]
    cw, ch = card["width_mm"], card["height_mm"]

    cards = [c for c in CARDS["cards"] if c["deck"] == deck_name]
    while len(cards) < cols*rows:
        cards.append(None)

    header_fill = P["fynd"] if deck_name == "fynd" else P["hot"]
    stroke = P["fynd_dark"] if deck_name == "fynd" else P["hot_dark"]
    icon_tile = "Ruin" if deck_name == "fynd" else "Grotta"

    parts = [svg_header(width, height)]
    parts.append(f'<rect x="0" y="0" width="{mm(width)}" height="{mm(height)}" fill="#ffffff"/>')
    parts.append(f'<text x="{mm(width/2)}" y="6.5" text-anchor="middle" font-family="Arial" font-size="4.2" font-weight="bold" fill="{stroke}">{esc("Fyndkort" if deck_name=="fynd" else "Hotkort")} – 4×4</text>')
    idx = 0
    for r in range(rows):
        for c in range(cols):
            x = margin + c*(cw + gap)
            y = margin + 4 + r*(ch + gap)
            cdata = cards[idx]
            if cdata is None:
                parts.append(f'<rect x="{mm(x)}" y="{mm(y)}" width="{mm(cw)}" height="{mm(ch)}" rx="2.5" fill="#faf8f2" stroke="#c8c1b2" stroke-dasharray="2 1" stroke-width="0.5"/>')
                parts.append(f'<text x="{mm(x+cw/2)}" y="{mm(y+ch/2)}" text-anchor="middle" font-family="Arial" font-size="3.2" fill="{P["muted"]}">Reservkort</text>')
                idx += 1
                continue
            parts.append(card_backdrop(x,y,cw,ch,header_fill,stroke))
            parts.append(f'<text x="{mm(x+3)}" y="{mm(y+4.3)}" font-family="Arial" font-size="2.2" fill="#fff7ea">{esc(cdata["id"])}</text>')
            parts.append(f'<text x="{mm(x+cw/2)}" y="{mm(y+8.4)}" text-anchor="middle" font-family="Arial" font-size="3.3" font-weight="bold" fill="#fff7ea">{esc(cdata["name"])}</text>')
            parts.append(icon_group(icon_tile, x+cw-5.0, y+5.9, 5.0))
            effect_lines = wrap_text(cdata["effect"], 23)
            txt, _ = svg_text_lines(x+4, y+19.7, effect_lines, font_size=3.1, line_gap=1.18)
            parts.append(txt)
            parts.append(f'<text x="{mm(x+cw-2.5)}" y="{mm(y+ch-2.5)}" text-anchor="end" font-family="Arial" font-size="2.2" fill="{P["muted"]}">{esc(cdata["type"].capitalize())}</text>')
            idx += 1
    parts.append('</svg>')
    return "\n".join(parts)

def write_outputs():
    write_tile_icon_assets()
    ref_svg = build_reference_svg()
    out_ref = ROOT / "output/print/reference/reference-card-a6-REGLERV4-STARTBALANS-v0.7.1-styled.svg"
    out_ref.parent.mkdir(parents=True, exist_ok=True)
    out_ref.write_text(ref_svg, encoding="utf-8")

    out_ref4 = ROOT / "output/print/reference/reference-card-a4-4up-REGLERV4-STARTBALANS-v0.7.1-styled.svg"
    out_ref4.write_text(build_reference_a4_4up(ref_svg), encoding="utf-8")

    board_svg = build_board_svg()
    out_board = ROOT / "output/print/board/board-a4-REGLERV4-STARTBALANS-v0.7.1-styled.svg"
    out_board.parent.mkdir(parents=True, exist_ok=True)
    out_board.write_text(board_svg, encoding="utf-8")
    out_preview = ROOT / "output/preview/board-a4-REGLERV4-STARTBALANS-v0.7.1-styled.svg"
    out_preview.parent.mkdir(parents=True, exist_ok=True)
    out_preview.write_text(board_svg, encoding="utf-8")

    for deck in ["fynd","hot"]:
        out_card = ROOT / f'output/print/cards/{"fyndkort" if deck=="fynd" else "hotkort"}-a4-4x4-v0.8.0-styled-inkfriendly.svg'
        out_card.parent.mkdir(parents=True, exist_ok=True)
        out_card.write_text(build_card_sheet(deck), encoding="utf-8")

if __name__ == "__main__":
    write_outputs()
    print("Styled printables generated.")
