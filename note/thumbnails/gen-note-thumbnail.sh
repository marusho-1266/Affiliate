#!/usr/bin/env bash
# note 用 dark-network サムネイルをタイトルのみで生成する（日付なし・中央寄せ）。
# 使い方: gen-note-thumbnail.sh "タイトル全文" [出力PNG相対パス]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
TITLE="${1:?タイトルを第1引数で指定してください}"
OUT_REL="${2:-note/thumbnails/note-thumbnail-latest.png}"
exec python note/thumbnails/apply_thumbnail_date.py --no-date -t "$TITLE" -o "$OUT_REL"
