# -*- coding: utf-8 -*-
"""サムネイル PNG に記事タイトルを重ねる（Pillow）"""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
SRC_CURRENT = ROOT / "apple_ai_article_thumbnail.png"
BACKUP = ROOT / "apple_ai_article_thumbnail_notitle.png"

# 記事見出しに合わせた行分割
LINES = [
    "AppleがAI戦略を",
    "ハードウェア中心に転換",
    "——",
    "「AIを作らず、AIを配る側」",
    "になる戦略の全貌",
]


def pick_font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        Path(r"C:\Windows\Fonts\meiryob.ttc"),
        Path(r"C:\Windows\Fonts\meiryo.ttc"),
        Path(r"C:\Windows\Fonts\YuGothB.ttc"),
        Path(r"C:\Windows\Fonts\msgothic.ttc"),
    ]
    for p in candidates:
        if p.is_file():
            try:
                return ImageFont.truetype(str(p), size=size, index=0)
            except OSError:
                continue
    return ImageFont.load_default()


def draw_stroke_text(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int, int],
    stroke_w: int,
    stroke_fill: tuple[int, int, int, int],
) -> None:
    draw.text(xy, text, font=font, fill=fill, stroke_width=stroke_w, stroke_fill=stroke_fill)


def main() -> None:
    import shutil

    # 再実行時は常に「無地」のバックアップから読む
    if BACKUP.is_file():
        src = BACKUP
    elif SRC_CURRENT.is_file():
        shutil.copy2(SRC_CURRENT, BACKUP)
        src = BACKUP
    else:
        raise SystemExit(f"not found: {BACKUP} or {SRC_CURRENT}")

    img = Image.open(src).convert("RGBA")
    w, h = img.size
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # 右側に読みやすいよう薄いグラデーション帯（テキストエリア）
    band_w = int(w * 0.52)
    x0 = w - band_w
    for x in range(band_w):
        a = int(140 * (x / band_w) ** 0.9)
        draw.line([(x0 + x, 0), (x0 + x, h)], fill=(10, 12, 18, a))

    img = Image.alpha_composite(img, overlay)

    draw = ImageDraw.Draw(img)

    font_title = pick_font(38)
    font_small = pick_font(30)

    stroke = 3
    stroke_fill = (15, 15, 20, 255)
    fill_main = (250, 248, 242, 255)
    fill_em = (255, 235, 210, 255)

    margin_top = 130
    line_gap = 12
    x_text = x0 + 28

    y = margin_top

    for i, line in enumerate(LINES):
        if line == "——":
            f = font_small
            fill = (180, 175, 168, 255)
            sw = 2
        elif i >= 3:
            f = font_title if len(line) < 20 else pick_font(34)
            fill = fill_em if "「" in line else fill_main
            sw = stroke
        else:
            f = font_title
            fill = fill_main
            sw = stroke
        draw_stroke_text(draw, (x_text, y), line, f, fill, sw, stroke_fill)
        bbox = draw.textbbox((0, 0), line, font=f)
        y += (bbox[3] - bbox[1]) + line_gap + (4 if line == "——" else 0)

    img.save(SRC_CURRENT, "PNG", optimize=True)
    print("saved:", SRC_CURRENT)
    print("source (no title, 再生成用):", BACKUP)


if __name__ == "__main__":
    main()
