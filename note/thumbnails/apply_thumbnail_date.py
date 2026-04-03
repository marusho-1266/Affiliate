# -*- coding: utf-8 -*-
"""note-thumbnail（dark-network）: マスターから右下日付・中央タイトルを描いた PNG を生成する。

--blank でタイトル・日付を消した無地マスター（タイトル可変用のベース）も出力できる。
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
BASE_WITH_01 = HERE / "note-thumbnail-dark-network_with-01.png"
OUT = HERE / "note-thumbnail-dark-network.png"
# タイトルなし（中央・右下をインペイント済み）。今後のサムネ共通ベース。
BLANK_MASTER = HERE / "note-thumbnail-dark-network-blank.png"

TITLE_PLACEHOLDER = "サムネイル用タイトル"


def pick_font(size: int, bold: bool = True) -> ImageFont.FreeTypeFont:
    candidates: list[Path] = []
    if bold:
        candidates += [
            Path(r"C:\Windows\Fonts\YuGothB.ttc"),
            Path(r"C:\Windows\Fonts\meiryob.ttc"),
            Path(r"C:\Windows\Fonts\arialbd.ttf"),
        ]
    candidates += [
        Path(r"C:\Windows\Fonts\YuGothM.ttc"),
        Path(r"C:\Windows\Fonts\meiryo.ttc"),
        Path(r"C:\Windows\Fonts\arial.ttf"),
    ]
    for p in candidates:
        if p.is_file():
            try:
                if p.suffix.lower() == ".ttc":
                    return ImageFont.truetype(str(p), size=size, index=0)
                return ImageFont.truetype(str(p), size=size)
            except OSError:
                continue
    return ImageFont.load_default()


def build_title_mask(img_rgb: np.ndarray) -> np.ndarray:
    """中央の白文字（プレースホルダー）領域マスク。"""
    h, w = img_rgb.shape[:2]
    rgb = img_rgb
    lum = rgb.mean(axis=2)
    mask = (lum > 195) & (rgb[:, :, 0] > 175) & (rgb[:, :, 1] > 175) & (rgb[:, :, 2] > 175)
    mask = mask.astype(np.uint8) * 255
    band = np.zeros((h, w), dtype=np.uint8)
    y0, y1 = int(h * 0.36), int(h * 0.60)
    band[y0:y1, int(w * 0.05) : int(w * 0.95)] = 255
    mask = cv2.bitwise_and(mask, band)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, np.ones((15, 25), np.uint8))
    mask = cv2.dilate(mask, np.ones((7, 7), np.uint8), 1)
    if cv2.countNonZero(mask) < 500:
        raise RuntimeError("中央のタイトル領域を検出できませんでした。")
    return mask


def build_digit_mask(img_rgb: np.ndarray) -> np.ndarray:
    h, w = img_rgb.shape[:2]
    x0, y0 = int(w * 0.72), int(h * 0.58)
    crop = img_rgb[y0:, x0:]
    g = crop.mean(axis=2)
    mask_crop = ((g > 22) & (g < 120)).astype(np.uint8) * 255
    mask_crop = cv2.morphologyEx(mask_crop, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask_crop = cv2.morphologyEx(mask_crop, cv2.MORPH_CLOSE, np.ones((9, 9), np.uint8))
    contours, _ = cv2.findContours(mask_crop, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes: list[tuple[int, int, int, int]] = []
    for c in contours:
        if cv2.contourArea(c) < 500:
            continue
        x, y, ww, hh = cv2.boundingRect(c)
        boxes.append((x, y, ww, hh))
    if not boxes:
        raise RuntimeError("右下の「01」領域を検出できませんでした。")
    xs = [b[0] for b in boxes] + [b[0] + b[2] for b in boxes]
    ys = [b[1] for b in boxes] + [b[1] + b[3] for b in boxes]
    pad = 20
    ux0, ux1 = min(xs) - pad, max(xs) + pad
    uy0, uy1 = min(ys) - pad, max(ys) + pad
    mask = np.zeros((h, w), dtype=np.uint8)
    gx0, gy0 = x0 + ux0, y0 + uy0
    gx1, gy1 = x0 + ux1, y0 + uy1
    mask[gy0:gy1, gx0:gx1] = 255
    mask = cv2.dilate(mask, np.ones((9, 9), np.uint8), 1)
    return mask


def wrap_lines(text: str, font: ImageFont.FreeTypeFont, draw: ImageDraw.ImageDraw, max_width: int) -> list[str]:
    text = text.replace("\r\n", "\n").strip()
    if not text:
        return [""]
    lines: list[str] = []
    for paragraph in text.split("\n"):
        if not paragraph:
            lines.append("")
            continue
        current = ""
        for ch in paragraph:
            test = current + ch
            bbox = draw.textbbox((0, 0), test, font=font)
            if bbox[2] - bbox[0] <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = ch
        if current:
            lines.append(current)
    return lines if lines else [""]


def draw_title_centered(
    draw: ImageDraw.ImageDraw,
    pil_w: int,
    pil_h: int,
    lines: list[str],
    max_width: int,
    no_wrap: bool = False,
    *,
    center_y_ratio: float = 0.42,
    max_block_height_ratio: float = 0.42,
) -> None:
    """中央付近に白太字で複数行描画。フォントサイズは収まるまで段階的に縮小。

    no_wrap が True のときは、splitlines() 済みの各行を自動折り返しせずそのまま描画する。
    center_y_ratio … ブロック全体の縦方向の基準位置（画像高さに対する比率、上端=0）。
    max_block_height_ratio … タイトルブロックの許容高さ（はみ出し防止）。
    """
    for size in range(88, 35, -4):
        font = pick_font(size, bold=True)
        wrapped: list[str] = []
        for line in lines:
            if not line:
                if not no_wrap:
                    wrapped.append("")
                continue
            if no_wrap:
                wrapped.append(line)
            else:
                wrapped.extend(wrap_lines(line, font, draw, max_width))
        if not wrapped:
            return
        line_heights: list[int] = []
        for ln in wrapped:
            bbox = draw.textbbox((0, 0), ln or " ", font=font)
            line_heights.append(bbox[3] - bbox[1])
        gap = max(4, size // 12)
        total_h = sum(line_heights) + gap * (len(wrapped) - 1)
        widths_ok = True
        if no_wrap:
            for ln in wrapped:
                bbox = draw.textbbox((0, 0), ln or " ", font=font)
                if bbox[2] - bbox[0] > max_width:
                    widths_ok = False
                    break
        if not widths_ok:
            continue
        if total_h < pil_h * max_block_height_ratio:
            cy = pil_h * center_y_ratio
            y = cy - total_h / 2
            stroke_w = max(1, size // 48)
            stroke_fill = (18, 18, 22, 255)
            for ln in wrapped:
                bbox = draw.textbbox((0, 0), ln or " ", font=font)
                tw = bbox[2] - bbox[0]
                th = bbox[3] - bbox[1]
                x = (pil_w - tw) / 2 - bbox[0]
                draw.text(
                    (x, y),
                    ln,
                    font=font,
                    fill=(255, 255, 255, 255),
                    stroke_width=stroke_w,
                    stroke_fill=stroke_fill,
                )
                y += th + gap
            return
    font = pick_font(34, bold=True)
    y = pil_h * max(0.35, center_y_ratio - 0.07)
    for ln in lines[:5]:
        draw.text((pil_w * 0.08, y), ln[:80], font=font, fill=(255, 255, 255, 255))
        y += 40


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser(
        description="サムネイル（dark-network）: 中央タイトルと右下日付（YYYY.MM.DD）を描画する。",
    )
    ap.add_argument(
        "date",
        nargs="?",
        default="",
        help="例: 2026.04.03（--no-date のときは省略可）",
    )
    ap.add_argument(
        "-t",
        "--title",
        default="",
        help=f'中央の「{TITLE_PLACEHOLDER}」を置き換えるテキスト（複数行可）。未指定ならプレースホルダーのまま。',
    )
    ap.add_argument(
        "-o",
        "--output",
        type=Path,
        default=None,
        help=f"出力PNG（未指定時: 通常は {OUT.name}、--blank 時は {BLANK_MASTER.name}）",
    )
    ap.add_argument(
        "-n",
        "--no-wrap",
        action="store_true",
        help="タイトルを自動折り返ししない（-t の改行をそのまま使う）。",
    )
    ap.add_argument(
        "--no-date",
        action="store_true",
        help="右下の日付を描かない（ベースの「01」はインペイントで消す）。",
    )
    ap.add_argument(
        "--blank",
        action="store_true",
        help="タイトルも日付も描かず、中央・右下を消したマスターのみ出力（タイトル可変用ベース）。",
    )
    args = ap.parse_args()

    if args.blank and args.title.strip():
        raise SystemExit("--blank では -t は使えません（無地マスター用です）。")
    if not args.blank and not args.no_date and not args.date.strip():
        raise SystemExit("日付を指定するか、--no-date を付けてください。")

    out_path = args.output
    if out_path is None:
        out_path = BLANK_MASTER if args.blank else OUT

    if not BASE_WITH_01.is_file():
        raise SystemExit(f"必要: {BASE_WITH_01}")

    img_bgr = cv2.imread(str(BASE_WITH_01))
    if img_bgr is None:
        raise SystemExit(f"読み込み失敗: {BASE_WITH_01}")

    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    mask = np.zeros(img_rgb.shape[:2], dtype=np.uint8)

    title = args.title.strip()
    if title or args.blank:
        mask = cv2.bitwise_or(mask, build_title_mask(img_rgb))
    mask = cv2.bitwise_or(mask, build_digit_mask(img_rgb))

    inp = cv2.inpaint(img_bgr, mask, 12, cv2.INPAINT_NS)

    pil = Image.fromarray(cv2.cvtColor(inp, cv2.COLOR_BGR2RGB)).convert("RGBA")
    draw = ImageDraw.Draw(pil)
    w, h = pil.size

    if title and not args.blank:
        max_w = int(w * 0.88)
        # 日付なしのときはタイトルをやや下げて画面中央付近に寄せる
        if args.no_date:
            center_y = 0.50
            max_h = 0.52
        else:
            center_y = 0.42
            max_h = 0.42
        draw_title_centered(
            draw,
            w,
            h,
            title.splitlines(),
            max_w,
            no_wrap=args.no_wrap,
            center_y_ratio=center_y,
            max_block_height_ratio=max_h,
        )

    if not args.blank and not args.no_date:
        font_date = pick_font(96, bold=True)
        date_str = args.date.strip()
        bbox = draw.textbbox((0, 0), date_str, font=font_date)
        tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
        margin = 36
        # 右下日付を下端から少し上へ（値を大きくするほど上）
        date_lift_px = 28
        tx = w - tw - margin
        ty = h - th - margin - 8 - date_lift_px
        for dx, dy, a in [(3, 3, 80), (0, 0, 115)]:
            draw.text((tx + dx, ty + dy), date_str, font=font_date, fill=(55, 58, 62, a))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    pil.convert("RGB").save(out_path, "PNG", optimize=True)
    print("saved:", out_path)
    if args.blank:
        print("mode: blank master (no title / no date)")
    elif title:
        print("title:", title.replace("\n", " / ")[:120])
    if not args.blank:
        if args.no_date:
            print("date: (なし)")
        else:
            print("date:", args.date.strip())


if __name__ == "__main__":
    main()
