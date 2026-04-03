# note サムネイル生成（dark-network）

ユーザーが **`/note-thumbnail` の直後に続けて書いた文字列をタイトル**として、リポジトリの `note/thumbnails/apply_thumbnail_date.py` で **PNG サムネイルを生成**する。

## チャットでの指定方法

- **形式:** `/note-thumbnail` のあとに**スペース区切りでタイトル全文**を書く（例は下記）。
- タイトルに **改行を入れたい**ときは、ユーザーが明示した行区切りに従い、`-n`（自動折り返し無し）を付けて `-t` に複数行を渡す。

### 例

```text
/note-thumbnail 「HTTP 402」にお金を載せる——x402 が Linux Foundation に入った意味
```

## エージェントが実行すること（必須）

1. 作業ディレクトリを **リポジトリルート**（`Affiliate` 相当）にする。
2. タイトル文字列を **`$TITLE`** として次のいずれかで実行する（**実際にコマンドを走らせ、成功を確認する**）。

**推奨（bash 利用可のとき）:**

```bash
bash note/thumbnails/gen-note-thumbnail.sh "$TITLE"
```

**同等の直接呼び出し:**

```bash
python note/thumbnails/apply_thumbnail_date.py --no-date -t "$TITLE" -o note/thumbnails/note-thumbnail-latest.png
```

- 既定の出力先は **`note/thumbnails/note-thumbnail-latest.png`**（都度上書き）。
- ユーザーが **出力パス**を指定した場合は、`gen-note-thumbnail.sh` の第2引数、または `-o` にそのパスを使う。

## 仕様（このコマンドのデフォルト）

| 項目 | 内容 |
|------|------|
| ベース | `note/thumbnails/note-thumbnail-dark-network_with-01.png`（スクリプト内定義） |
| 日付 | **描画しない**（`--no-date`）。右下の「01」はインペイントで消す |
| タイトル位置 | 画像縦方向の中央付近（スクリプト既定） |
| 長いタイトル | 第1引数のみ・1行のときは **自動折り返し**（`-n` なし） |

## 失敗時

- `python` / 依存（OpenCV・Pillow 等）のエラーを読み、パス・引用符・タイトル内の制御文字を確認して再試行する。
- 完了後、**保存した PNG のパス**と、**使ったタイトル**をユーザーに返す。

## 関連

- 無地マスターのみ出力: `python note/thumbnails/apply_thumbnail_date.py --blank`
- 日付付きで出力: `python note/thumbnails/apply_thumbnail_date.py YYYY.MM.DD -t "..."` または `note/thumbnails/build-thumbnail.sh`
