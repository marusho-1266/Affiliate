# Threads 投稿文案（夜）— Claude Managed Agents／ホスト型エージェントAPI note 公開告知

関連記事: `note/20260409/2026-04-09-claude-managed-agents｜ホスト型エージェントAPIと実務の読み方.md`（※公開後は「note 公開済み」と差し替え可）  
関連ブリーフ: `reports/note-briefs/2026-04-09-claude-managed-agents.md`  
昼分（調査メモ）: `threads/2026-04-09-claude-managed-agents-threads.md`

---

## 投稿1（メイン）

夜のITメモ

2026年4月8日付の Anthropic 公表をベースに、Claude Managed Agents を公式ブログ・Managed Agents の overview・Pricing まで踏まえて整理した note を公開しました。ホスト型の harness とインフラに責任が寄るぶん、見積もりはトークンだけ見ていても足りない、というのが個人的な読みどころです。

Messages API が直接プロンプト向けなのに対し、Managed Agents は長時間・多ツール・状態付きの非同期向け、という公式の対比、セッションが running のあいだだけ session-hour が乗る話、Web 検索の従量、Bedrock や Vertex 経由ではなく Claude API 直であること、ベータヘッダとレート制限、あとブログのテンエックス系の数字は比較条件が見えないので主軸にしない、まで一度にまとめています。

続く↓

---

## 投稿2（補足・フック）

補足です。

記事の後半では、自前の LangGraph などとどう棲み分けるか、FinOps で見積表に足す列の話、パートナー向けの表記ガイドライン（Claude Code などと誤認されない話）にも触れています。

質問というほどでもないのですが、エージェント導入の議論で「まずトークン単価」から入っていませんか。running 時間や検索回数まで同じ会議で扱っているチームがどれくらいあるのか、気になります。

一次ソースへのリンクは、プロフィールから辿れる note の末尾にまとめています。

---

## 投稿3（リンク方針の明示・任意）

note の URL はスレ内に貼らず、プロフィールの固定リンク（または外部リンク欄）からご覧ください（※公開中の記事 URL に差し替えてください）。

ブログ単体で押さえるなら  
https://claude.com/blog/claude-managed-agents  
料金の細部は Pricing の Managed Agents 節のアンカーが早いです。

---

## 1本にまとめる場合（参考）

夜のITメモ 🌙 本日、Claude Managed Agents を公式ドキュメントベースで整理した note を公開。Messages API との違い、トークン以外のメーター（running の session-hour・Web 検索）、Claude API 直であること、ベータと見積の落とし穴。テンエックスだけ拾うのは危ない、という注意も。一次ソースはプロフィールの note 末尾／note はプロフィールから。
