# 海外ITニュース・短文サマリ（実行時点）

実行時点の海外ITニュースを**5件以内**に絞り、**各1〜2文＋出典URL**で日本語報告する。結果は **Markdown に追記**し、**過去実行とURL単位で重複しない**ようにする（本調査コマンドと**同一の `seen-urls.json`**を使う）。

## 出力ファイル

| ファイル | 用途 |
|----------|------|
| `reports/overseas-it-news/news-brief-log.md` | brief 用の**累積ログ**（追記） |
| `reports/overseas-it-news/seen-urls.json` | **既出URL**（`overseas-it-news` と共有） |

## 重複排除（必ず実行前に）

1. **`seen-urls.json` を読む**。
2. **`overseas-it-news.md` と同じURL正規化**（https化、末尾`/`除去、ホスト小文字、不要クエリ除去）で `urls` と照合する。
3. **既に `urls` にある主出典URLのトピックは採用しない**。同一事件の別URLも、内容が既ログと同じならスキップする。
4. **新規のみ**を最大5件 `news-brief-log.md` に追記し、採用URLを `seen-urls.json` にマージして保存する。

**新規0件**のときは `news-brief-log.md` に日時見出しだけ追記し「新規なし」と書く。

## 手順

1. Web検索で `tech news` と `security news` を**当日〜72時間**の文脈で実行する。
2. 候補を重複排除後、**最大5件**に絞る。
3. **エイプリルフール**の日付付近は、ジョーク記事を採用しないか、公式確認済みと明記する。

## ログ追記フォーマット（`news-brief-log.md` 末尾）

```markdown
## YYYY-MM-DD HH:MM （TZ）

1. 要約 — [媒体](URL)
2. …
```

## チャットでの返答

- 新規分の **Top 5 以内**（ログと整合）
- 保存したファイルパス
