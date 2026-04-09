# 報告資料: Claude Managed Agents（ホスト型エージェント API）

- **調査日**: 2026-04-09
- **主出典**: [Claude — Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents)
- **要約（1文）**: Anthropic が **Claude Platform** 上で、オーケストレーション・サンドボックス・セッション管理を抱えた **ホスト型エージェント実行環境（Managed Agents）** を **パブリックベータ**として提供し始め、トークン課金に加え **セッションの `running` 時間に対するランタイム課金**を導入した。

---

## 1. 背景 — なぜ今この情報が出ているか

- **事実（時系列）**:
  - **2026-04-08（ブログ掲載日）**: [製品ブログ](https://claude.com/blog/claude-managed-agents) で **Claude Managed Agents** を発表。**composable APIs** でクラウドホストのエージェントを構築・スケール展開できる、と説明。**Claude Platform 上の public beta** で利用可能、と記載。
  - ブログ上の訴求は、本番エージェントに必要な **サンドボックス実行、チェックポイント、クレデンシャル、スコープされた権限、エンドツーエンドのトレース**などを自前で積むと月単位のインフラ作業になりがちで、Managed Agents は **タスク・ツール・ガードレールを定義すれば Anthropic 側インフラで実行**する、という整理。
  - 公式ドキュメント [Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview) では、**Messages API（直接プロンプト）**と対比し、Managed Agents は **プリビルドの設定可能な agent harness がマネージドインフラ上で動く**もの、**長時間・非同期向け**と位置づけ。
  - **ベータ要件**: 全 Managed Agents エンドポイントに **`managed-agents-2026-04-01` ベータヘッダ**が必要。SDK が自動設定、**リリース間で挙動が調整されうる**と明記。
  - **リサーチプレビュー（別途申請）**: [outcomes](https://platform.claude.com/docs/en/managed-agents/define-outcomes)、[multiagent](https://platform.claude.com/docs/en/managed-agents/multi-agent)、[memory](https://platform.claude.com/docs/en/managed-agents/memory) — ブログでも multi-agent 協調や「成果物・成功基準の自己評価・反復」に [フォーム](https://claude.com/form/claude-managed-agents) を案内。
  - **料金（一次）**: [Pricing — Claude Managed Agents pricing](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing) に、(1) **セッションが消費するトークンは通常のモデル単価**、プロンプトキャッシュ同様、(2) セッション内 **Web 検索は 1000 回あたり $10（標準）**、(3) **セッションランタイムは `running` 状態の時間に対し $0.08 / session-hour**（ミリ秒単位計測。`idle` / `rescheduling` / `terminated` は課金対象外）、(4) **Code Execution のコンテナ時間課金は Managed Agents 利用時は session runtime に置き換わり二重課金しない**、と記載。**Bedrock / Vertex 等のサードパーティ API 料金は適用されず、Claude API 直利用のみ**と表形式で明記。
  - **レート制限（ドキュメント）**: 作成系 60 req/分、読取系 600 req/分（組織あたり）。他に tier ベースの spend / rate limit が適用。
  - **ブログ記載の自己評価**: 構造化ファイル生成タスクの内部テストで、標準プロンプトループ比 **最大約10ポイント**の成功率改善など（**比較条件はブログ本文依存**）。
  - **顧客引用**: Notion、Rakuten、Asana、Vibecode、Sentry、Atlassian、他スタートアップ等（いずれもブログ内の引用・ケースリンク）。

- **公開情報から読み取れる動機**:
  - エージェント需要の拡大に対し、**各社が同じ「ランタイム・サンドボックス・セッション状態」を再実装するコスト**を下げ、**Claude へのロックインと開発速度**を両取りするプロダクト線。
  - **Messages API だけでは長時間・ステートフル・ツール連鎖の運用負荷**が残るため、**製品としてハーネスを提供**する段階に移った、という読み。

- **補足・推測（根拠付き）**:
  - **競合**: AWS・GCP・Azure 上の「エージェント用マネージド実行」や、他 LLM ベンダの類似機能との **機能・価格競争**は続く（推測。本ブリーフでは個社比較は割愛）。
  - **「10x faster」**はマーケティング表現であり、**再現性や外部ベンチマークはブログからは検証不可**。

---

## 2. 目的 — 誰に、何をしてほしいか

| 想定読者 | 発信側（Anthropic）が望む行動（推定） | note 読者への実務的示唆 |
|----------|----------------------------------------|-------------------------|
| **B2B アプリ開発者・スタートアップ** | Claude API と Managed Agents で **本番エージェントを早く載せる**。[Console / CLI / Claude Code の Skill](https://claude.com/blog/claude-managed-agents) から試す。 | **自前ループ vs マネージド**の責任分界（ログ・データ出口・中断・コスト）を要件定義に書く。 |
| **中堅〜エンタープライズ IT / セキュリティ** | ガバナンス（スコープ権限・トレース）を前面に出し、**承認を取りやすくする**。 | **DPA・データ所在地・ベータ条項**を法務と確認。`running` 時間課金で **長時間放置セッションのコスト**を監視設計する。 |
| **既存 Claude / Messages API 利用者** | 長時間・多ツール・ステートフル用途を **Managed Agents に寄せる**。 | ドキュメントどおり **Batch 割引・Fast mode premium・Long context premium 等が Managed Agents では非適用** — 見積もりロジックを分ける。 |
| **パートナー・ISV** | 自社ブランドを維持しつつ **「Powered by Claude」等の表記ルール**に従う（[overview の Branding guidelines](https://platform.claude.com/docs/en/managed-agents/overview)）。 | 「Claude Code / Cowork と誤認されない UI・表記」をチェックリスト化。 |

---

## 3. 効果 — 短期・中期・長期の予想

**時間軸の定義（本資料内）**

- **短期**: 直近 **0〜3か月**
- **中期**: **3か月〜1年**
- **長期**: **1年以上**

- **短期（0〜3か月）**:
  - **予想される効果**: パイロット案件の増加、**プロトタイプ〜限定本番**での開発期間短縮の体験談、ブログ掲載の **顧客ロゴ・引用**に基づく認知拡大。
  - **不確実性**: ベータのため **API 変更・挙動調整**、ドキュメントと実装の差、**research preview 機能は一般未開放**。
  - **効果が出ない条件**: 組織が **Bedrock / Vertex 経由しか使えない**契約の場合（ドキュメント上 Managed Agents は **Claude API 直**）。セキュリティ審査で **ベータ利用が止まる**場合。

- **中期（3か月〜1年）**:
  - **予想される効果**: GA 近傍での **SLA・サポート・課金の安定化**、エコシステム（MCP・Skills 連携）の事例増。**session-hour とトークンの合算**が FinOps の標準話題になる可能性（推測）。
  - **不確実性**: モデル世代交代で **ハーネス最適化の再調整**、価格改定。
  - **効果が出ない条件**: **自社オーケストレーション**の方が細かい制御やコストで勝つワークロードでは乗り換えが進まない。

- **長期（1年以上）**:
  - **予想される効果**: 「LLM API」から **「ホスト型エージェント実行」**が既定オプションの一つになる、という産業パターンの一部として定着しうる（一般的推論）。
  - **不確実性**: **規制・監査**（自動実行の責任、越境）、**ベンダロックイン**への反動でオープンソース／マルチクラウド抽象化が進む可能性。
  - **効果が出ない条件**: 重大な **セキュリティインシデント**や **信頼失墜**でマネージド実行への慎重姿勢が強まる場合（シナリオ）。

---

## 4. note 執筆メモ（任意）

- **フック案（1〜2文）**: 「エージェントを“APIで叩くだけ”から、“Anthropic の部屋で働かせる”に変えた。課金もトークンだけじなく、**動いている秒がそのままドルになる**。」
- **検証が必要な一点（事実・数値・日付）**:
  - **10x / 10ポイント改善**は **社内テスト・マーケ文言**として扱い、**再現手順が公開されていない**点を明記。
  - **料金・非適用モディファイア**は [pricing の表](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing) を引用し、**改定時は要再確認**。
  - **「API アカウントではデフォルトで有効」**等の文言はドキュメント版に合わせる（ブログと docs の細部差が出たら docs 優先）。
- **免責・注意**: 投資・契約・法務判断の助言ではない。**ベータ**であり、本番前は社内承認・セキュリティレビューを前提とする。

---

## 5. 参照一覧

- [Claude Blog — Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents)（一次：製品発表・顧客引用・概要）
- [Anthropic Docs — Claude Managed Agents overview](https://platform.claude.com/docs/en/managed-agents/overview)（一次：Messages API との対比、概念、ベータヘッダ、レート制限、ブランディング）
- [Anthropic Docs — Pricing / Claude Managed Agents pricing](https://platform.claude.com/docs/en/about-claude/pricing#claude-managed-agents-pricing)（一次：トークン・session-hour・Web search・非適用モディファイア・例）
- [Research preview 申請フォーム](https://claude.com/form/claude-managed-agents)（一次：multi-agent / outcomes / memory 等）
- （任意深掘り） [Tools](https://platform.claude.com/docs/en/managed-agents/tools)、[Console quickstart リンク](https://platform.claude.com/workspaces/default/agent-quickstart) — 記事で手を動かす回向け

---

**調査モード**: ライト（公式ブログ・開発者ドキュメント・Pricing の取得のみ。**Task レーン A〜E は未使用**。）
