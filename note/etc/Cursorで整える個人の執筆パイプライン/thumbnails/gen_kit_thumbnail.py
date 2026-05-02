#!/usr/bin/env python3
"""Generate HUD-style thumbnails for cursor-writing-pipeline-kit bonus article.

Matches palette/layout family of ep05-thumb-note (1280×670) and ep05-thumb (1536×1024).
Outputs: cursor-writing-pipeline-kit-thumb-note.png, cursor-writing-pipeline-kit-thumb.png
"""
from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
OUT_NOTE = HERE / "cursor-writing-pipeline-kit-thumb-note.png"
OUT_FULL = HERE / "cursor-writing-pipeline-kit-thumb.png"

ACCENT = (120, 220, 235)
ACCENT_BRIGHT = (130, 240, 250)
WHITE = (250, 252, 252)
BG_DARK = (18, 24, 30)
BG_LIGHT = (28, 36, 44)


def _font_jp(size: int, bold: bool) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("/c/Windows/Fonts/NotoSansJP-VF.ttf"),
        Path("C:/Windows/Fonts/NotoSansJP-VF.ttf"),
        Path("/mnt/c/Windows/Fonts/NotoSansJP-VF.ttf"),
        Path("/c/Windows/Fonts/meiryob.ttc"),
        Path("C:/Windows/Fonts/meiryob.ttc"),
    ]
    for p in candidates:
        if p.exists():
            return ImageFont.truetype(str(p), size=size)
    return ImageFont.load_default()


def _font_headline(size: int) -> ImageFont.FreeTypeFont:
    """Heavy JP sans for hero title (Yu Gothic Bold → Noto fallback)."""
    paths = [
        Path("/c/Windows/Fonts/YuGothB.ttc"),
        Path("C:/Windows/Fonts/YuGothB.ttc"),
    ]
    for p in paths:
        if p.exists():
            try:
                return ImageFont.truetype(str(p), size=size, index=0)
            except OSError:
                pass
    return _font_jp(size + 8, True)


def _radial_bg(w: int, h: int) -> Image.Image:
    """Dark vignette + subtle radial lift in center."""
    img = Image.new("RGB", (w, h), BG_DARK)
    px = img.load()
    cx, cy = w * 0.5, h * 0.42
    max_r = math.hypot(w, h) * 0.55
    for y in range(h):
        for x in range(w):
            d = math.hypot(x - cx, y - cy) / max_r
            t = min(1.0, d**1.2)
            br, bg, bb = BG_LIGHT
            dr, dg, db = BG_DARK
            r = int(dr + (br - dr) * (1 - t) * 0.35)
            g = int(dg + (bg - dg) * (1 - t) * 0.35)
            b = int(db + (bb - db) * (1 - t) * 0.35)
            px[x, y] = (r, g, b)
    return img


def _dot_corners(draw: ImageDraw.ImageDraw, w: int, h: int, s: float) -> None:
    spacing = max(5, int(6 * s))
    rdot = max(1, int(2 * s))
    grids = [(30, 30, 9, 9), (w - 30 - spacing * 8, 30, 9, 9), (30, h - 30 - spacing * 8, 9, 9), (w - 30 - spacing * 8, h - 30 - spacing * 8, 9, 9)]
    base = ACCENT_BRIGHT
    soft = tuple(int(c * 0.42 + BG_DARK[i] * 0.58) for i, c in enumerate(base))
    for gx, gy, gw, gh in grids:
        for iy in range(gh):
            for ix in range(gw):
                x = gx + ix * spacing
                y = gy + iy * spacing
                draw.ellipse([x, y, x + rdot, y + rdot], fill=soft)


def _bracket_curve(draw: ImageDraw.ImageDraw, w: int, h: int, s: float) -> None:
    cy = int(h * 0.43)
    r = int(min(w, h) * 0.28)
    lw = max(2, int(2 * s))
    for side in (-1, 1):
        cx = w // 2 + side * int(w * 0.22)
        bbox = [cx - r, cy - r, cx + r, cy + r]
        if side < 0:
            draw.arc(bbox, 100, 260, fill=ACCENT_BRIGHT, width=lw)
        else:
            draw.arc(bbox, -80, 80, fill=ACCENT_BRIGHT, width=lw)


def _hex_footer_points(cx: float, cy: float, ww: float, hh: float) -> list[tuple[float, float]]:
    """Flat hex bracket (episode box style)."""
    q = ww * 0.25
    return [
        (cx - ww - q * 0.3, cy - hh),
        (cx + ww + q * 0.3, cy - hh),
        (cx + ww + q, cy),
        (cx + ww + q * 0.3, cy + hh),
        (cx - ww - q * 0.3, cy + hh),
        (cx - ww - q, cy),
    ]


def _draw_h_line_nodes(draw: ImageDraw.ImageDraw, y: int, cx: int, half: int, accent: tuple[int, ...]) -> None:
    lw = 2
    draw.line([(cx - half, y), (cx + half, y)], fill=accent, width=lw)
    for x in (cx - half, cx + half):
        draw.ellipse([x - 4, y - 4, x + 4, y + 4], outline=accent, width=2)


def _pill_roundrect(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], r: int) -> None:
    draw.rounded_rectangle(box, radius=r, outline=ACCENT_BRIGHT, width=2)


def _draw_text_segments(
    img: Image.Image,
    draw: ImageDraw.ImageDraw,
    x_center: float,
    y: float,
    segments: list[tuple[str, tuple[int, int, int]]],
    font: ImageFont.FreeTypeFont,
) -> None:
    total_w = 0
    bboxes = []
    for txt, col in segments:
        bb = draw.textbbox((0, 0), txt, font=font)
        w = bb[2] - bb[0]
        bboxes.append((w, bb))
        total_w += w
    xs = x_center - total_w / 2
    cur_x = xs
    for i, ((txt, col), (bw, bb)) in enumerate(zip(segments, bboxes)):
        draw.text((cur_x, y), txt, font=font, fill=col)
        cur_x += bw


def render_kit_thumbnail(w: int, h: int) -> Image.Image:
    scale = math.sqrt((w * h) / (1280 * 670))
    img = _radial_bg(w, h)
    draw = ImageDraw.Draw(img)
    cx = w / 2

    _dot_corners(draw, w, h, scale)
    _bracket_curve(draw, w, h, scale)

    # Extend lines (top decoration)
    _draw_h_line_nodes(draw, int(h * 0.06), int(cx), int(w * 0.42), ACCENT_BRIGHT)

    # Top pill box
    pill_h = max(42, int(52 * scale))
    pill_w_ratio = min(0.92, (920 if w <= 1360 else 1100) / w)
    pill_w = int(w * pill_w_ratio)
    py = max(34, int(48 * scale))
    px_left = int(cx - pill_w / 2)
    pr = pill_h // 2
    _pill_roundrect(draw, (px_left, py, px_left + pill_w, py + pill_h), pr)

    font_pill = _font_jp(max(17, int(21 * scale)), True)
    series_line = [
        ("Cursor", ACCENT_BRIGHT),
        ("で作る", WHITE),
        ("「書き続ける仕組み」", WHITE),
        ("入門", WHITE),
    ]
    series_full = "".join(p[0] for p in series_line)
    bbox_p = draw.textbbox((0, 0), series_full, font=font_pill)
    th = bbox_p[3] - bbox_p[1]
    pil_y = py + (pill_h - th) // 2 - bbox_p[1]
    _draw_text_segments(img, draw, cx, pil_y, series_line, font_pill)

    # Badge circle (gift symbol)
    badge_r = max(28, int(38 * scale))
    by = int(py + pill_h + 28 * scale + 28)
    bx = int(cx)
    draw.ellipse([bx - badge_r - 2, by - badge_r - 2, bx + badge_r + 2, by + badge_r + 2], outline=ACCENT_BRIGHT, width=3)
    font_star = _font_headline(max(42, int(54 * scale)))
    draw.text((bx, by), "★", fill=WHITE, font=font_star, anchor="mm")

    yt = int(by + badge_r + 22 * scale)
    font_main = _font_headline(max(48, int(60 * scale)))
    main_segments = [("購入者特典キット", WHITE)]
    _draw_text_segments(img, draw, cx, yt, main_segments, font_main)

    bb_main = draw.textbbox((0, 0), main_segments[0][0], font=font_main)
    main_height = bb_main[3] - bb_main[1]

    font_sub = _font_jp(max(20, int(26 * scale)), True)
    sub_line = [
        ("Commands", ACCENT_BRIGHT),
        ("・", WHITE),
        ("Skills", ACCENT_BRIGHT),
        ("・ワークシート", WHITE),
    ]
    y_sub = yt + main_height + max(14, int(14 * scale))
    _draw_text_segments(img, draw, cx, y_sub, sub_line, font_sub)

    bb_s1 = draw.textbbox((0, 0), "".join(s[0] for s in sub_line), font=font_sub)
    h_s1 = bb_s1[3] - bb_s1[1]
    sub_line2 = [("受け取り方と使い方", WHITE)]
    y_sub2 = y_sub + h_s1 + max(8, int(8 * scale))
    _draw_text_segments(img, draw, cx, y_sub2, sub_line2, font_sub)

    y_rule = min(h - int(95 * scale), y_sub2 + int(32 * scale))
    rule_half = min(int(w * 0.38), int(240 * scale))
    _draw_h_line_nodes(draw, y_rule, int(cx), rule_half, ACCENT_BRIGHT)

    # Footer hexagon
    fw = max(90, int(138 * scale))
    fh = max(18, int(26 * scale))
    fcy = h - max(62, int(74 * scale))
    pts_f = _hex_footer_points(cx, fcy, fw, fh)
    draw.line(pts_f + [pts_f[0]], fill=ACCENT_BRIGHT, width=2)

    footer_label = [("特典キット", ACCENT_BRIGHT)]
    font_footer = _font_jp(max(24, int(34 * scale)), True)
    segs_tw = "".join([s[0] for s in footer_label])
    bb_f = draw.textbbox((0, 0), segs_tw, font=font_footer)
    fy = fcy - (bb_f[3] - bb_f[1]) / 2 - bb_f[1]
    _draw_text_segments(img, draw, cx, fy + 4, footer_label, font_footer)

    # Dash vents beside footer box
    vent_y = [fcy + fh + 14, fcy + fh + 26]
    for vy in vent_y:
        vx0 = cx - fw - min(int(110 * scale), int(w * 0.09))
        vx1 = cx + fw + min(int(50 * scale), int(w * 0.045))
        for vx in (vx0, vx1):
            for i in range(4):
                draw.line(
                    [(int(vx + i * 10 * scale), vy), (int(vx + 6 * scale + i * 10 * scale), vy + max(10, int(11 * scale)))],
                    fill=ACCENT_BRIGHT,
                    width=max(2, int(2 * scale)),
                )

    _draw_h_line_nodes(draw, h - max(38, int(52 * scale)), int(cx), int(w * 0.48), ACCENT_BRIGHT)

    return img


def main() -> None:
    out_note = render_kit_thumbnail(1280, 670)
    out_note.save(OUT_NOTE, optimize=True)

    out_full = render_kit_thumbnail(1536, 1024)
    out_full.save(OUT_FULL, optimize=True)

    print("Wrote:", OUT_NOTE, OUT_FULL)


if __name__ == "__main__":
    main()
