"""Add article title to note thumbnail (one-off script)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "note-20260401-anthropic-claude-code-thumbnail.png"
OUT = ROOT / "note-20260401-anthropic-claude-code-thumbnail.png"

TITLE_LINES = (
    "Anthropic「Claude Code」",
    "ソースマップ露出報道をどう読むか",
)

FONT_CANDIDATES: list[tuple[str, int | None]] = [
    (r"C:\Windows\Fonts\YuGothM.ttc", 0),
    (r"C:\Windows\Fonts\meiryo.ttc", 0),
    (r"C:\Windows\Fonts\NotoSansJP-VF.ttf", None),
]


def load_font(size: int) -> ImageFont.FreeTypeFont:
    for path, index in FONT_CANDIDATES:
        p = Path(path)
        if not p.exists():
            continue
        try:
            if index is not None and path.lower().endswith(".ttc"):
                return ImageFont.truetype(str(p), size, index=index)
            return ImageFont.truetype(str(p), size)
        except OSError:
            continue
    return ImageFont.load_default()


def main() -> None:
    img = Image.open(SRC).convert("RGBA")
    w, h = img.size

    band_h = int(h * 0.28)
    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    for y in range(band_h):
        alpha = int(200 * (y / band_h) ** 0.9)
        draw_overlay.line(
            [(0, h - band_h + y), (w, h - band_h + y)],
            fill=(12, 14, 18, alpha),
        )
    img = Image.alpha_composite(img, overlay)
    draw = ImageDraw.Draw(img)

    font_size = 46
    font = load_font(font_size)
    line_gap = 14
    text_color = (248, 250, 252, 255)
    shadow = (0, 0, 0, 120)

    line_heights: list[int] = []
    for line in TITLE_LINES:
        bbox = draw.textbbox((0, 0), line, font=font)
        line_heights.append(bbox[3] - bbox[1])

    total_h = sum(line_heights) + line_gap * (len(TITLE_LINES) - 1)
    y0 = h - band_h + (band_h - total_h) // 2 - 8

    cx = w // 2
    y = y0
    for i, line in enumerate(TITLE_LINES):
        bbox = draw.textbbox((0, 0), line, font=font)
        tw = bbox[2] - bbox[0]
        x = cx - tw // 2
        for dx, dy in ((2, 2), (1, 1)):
            draw.text((x + dx, y + dy), line, font=font, fill=shadow)
        draw.text((x, y), line, font=font, fill=text_color)
        y += line_heights[i] + line_gap

    img.convert("RGB").save(OUT, "PNG", optimize=True)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
