#!/usr/bin/env bash
# note-thumbnail-dark-network.png を「タイトル」と日付で生成する
# 使い方: build-thumbnail.sh "中央に出すタイトル" [YYYY.MM.DD]
# 日付省略時は今日（ローカルタイムゾーン）
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"
TITLE="${1:-}"
DATE="${2:-$(date +%Y.%m.%d)}"
if [[ -z "$TITLE" ]]; then
  echo "Usage: $0 \"タイトル文字列\" [YYYY.MM.DD]" >&2
  echo "例: $0 \"x402 が Linux Foundation に入った意味\" 2026.04.03" >&2
  exit 1
fi
exec python note/thumbnails/apply_thumbnail_date.py "$DATE" -t "$TITLE"
