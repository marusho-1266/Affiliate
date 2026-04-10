# Threads 投稿文案（昼）— Claude Managed Agents（ホスト型エージェント）

関連ブリーフ: `reports/note-briefs/2026-04-09-claude-managed-agents.md`  
関連記事（note）: `note/20260409/2026-04-09-claude-managed-agents｜ホスト型エージェントAPIと実務の読み方.md`

夜分（note 公開告知）: `threads/2026-04-09-claude-managed-agents-threads-evening.md`

---

## 投稿1（メイン）

昼のITメモ

2026/4/8、Claude 公式ブログで Claude Managed Agents が発表されました。Claude Platform 上の パブリックベータで、エージェント用の オーケストレーション・サンドボックス・長時間セッションなどを Anthropic 側のマネージドインフラに寄せる、という位置づけです。

公式ドキュメントでは Messages API（直接プロンプト） と対比表があり、Managed Agents は プリビルドの harness がマネージド環境で動く想定で、数分〜数時間のツール連鎖・非同期向け、と整理されています。API 利用には `managed-agents-2026-04-01` のベータヘッダが必須で、挙動はリリース間で調整されうる、とも書かれています。

料金はドキュメント上、通常どおりトークンに加え、セッションが `running` の間だけ $0.08 / session-hour。`idle` などは対象外、と説明があります。セッション内の Web 検索は 1000 回あたり $10 の記載も。Bedrock / Vertex 経由ではなく Claude API 直、とも表で明記されています。

ブログには 楽天（Rakuten） の引用もあり、Slack / Teams 経由の社内エージェント展開の文脈で読めます。multi-agent や outcomes / memory は research preview（申請）扱い、とドキュメント側にも分かれがあります。

続く↓

---

## 投稿2（補足・注意）

補足：

ブログの 「10x faster」 や内部テストの 成功率 +10ポイント などは、マーケ・自己報告ベースなので、SNS要約だけで数字を信じすぎない方が安全そうです。導入検討では 見積もりがポイントで、Pricing には Batch 割引や Fast mode premium など Messages API のモディファイアが Managed Agents では非適用、という表もあります（見積ロジックを分けるメモ）。

現場目線では、長時間 `running` のセッションや Web 検索の多いエージェントは、トークン以外の行が効きやすいので、ダッシュボードとアラートを先に決めたいところです。あわせて ベータ条項・データ取り扱いは契約側で確認、が定番です。

一次ソース：

[https://claude.com/blog/claude-managed-agents](https://claude.com/blog/claude-managed-agents)

（概要・Messages API との対比・ベータ・レート制限）

[https://platform.claude.com/docs/en/managed-agents/overview](https://platform.claude.com/docs/en/managed-agents/overview)

（料金・非適用モディファイア・session-hour）

[https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing)

---

## 1本にまとめたい場合（参考）

投稿1の「続く↓」を削除し、投稿2から 「10x は原文で鵜呑みにしない」「running 時間と Web 検索がトークン以外のコスト」 を1〜2文に圧縮。リンクは ブログ 1本 または ブログ＋Pricing アンカー の2本までに絞っても可。