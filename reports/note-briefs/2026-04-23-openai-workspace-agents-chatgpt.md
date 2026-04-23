# 報告資料: OpenAI「workspace agents」（ChatGPT）

- **調査日**: 2026-04-23
- **主出典**: [OpenAI（製品発表）](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)
- **要約（1文）**: OpenAI が 2026年4月22日、ChatGPT の Business／Enterprise／Edu／Teachers 向けに、**Codex 基盤のクラウド共有エージェント「workspace agents」**をリサーチプレビューとして公開し、**2026年5月6日まで無料**の後にクレジット課金へ移行すると明記した。

---

## 1. 背景 — なぜ今この情報が出ているか

- **事実（時系列）**:
  - **2026-04-16**: OpenAI が Codex の大型アップデート（「職場」向け機能の拡張など）を公表（同一週のプロダクト文脈）。出典: [OpenAI — Codex for (almost) everything](https://openai.com/index/codex-for-almost-everything/)（April 16, 2026）
  - **2026-04-22**: 「workspace agents」を公表。GPTs の**進化形**と位置づけ、**Codex** で駆動すると明記。対象プランは **ChatGPT Business, Enterprise, Edu, Teachers**。**リサーチプレビュー**。出典: [OpenAI — Introducing workspace agents](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)（April 22, 2026）
  - **価格**: 公式本文で **Workspace agents will be free until May 6, 2026, with credit-based pricing starting on that date.** と記載（同日投稿）。
  - **ヘルプセンター**: Enterprise では**ローンチ時は既定でオフ**、管理者が有効化。**EKM（Enterprise の顧客管理鍵）利用ワークスペースには未提供**と記載。出典: [OpenAI Help Center](https://help.openai.com/en/articles/20001143)（ページ上「Updated: …」は相対表記のため、執筆時に再確認推奨）

- **公開情報から読み取れる動機**:
  - 個人向けチャット利用から、**組織内の共有コンテキスト・引き継ぎ・複数ツール横断**の業務へ価値を伸ばす意図が、公式の問題設定（「many of the most important workflows … depend on shared context, handoffs, and decisions across teams」）として明示されている。
  - **エンタープライズ統制**（管理者によるツール／アクション権限、Compliance API、エージェント停止など）を同時に打ち出しており、法人導入の前提条件を揃える発表になっている。

- **補足・推測（根拠付き）**:
  - **競合環境**: 他社も「職場でのエージェント」（例: 別ベンダの Cowork 系、ブラウザ／Workspace 連携のエージェント機能）が同時期に報じられている**市場文脈**はあるが、**OpenAI が特定競合に言及しているわけではない**（因果の断定は避ける）。
  - **GPTs からの移行**: 公式は GPTs は当面維持し、**近く GPTs から workspace agents への変換を容易にする**と述べている。カスタム GPT 利用組織への移行導線を用意する段階と読めるが、詳細仕様は「Soon」に委ねられている。

---

## 2. 目的 — 誰に、何をしてほしいか

| 想定読者 | 発信側が望む行動（推定） | note 読者への実務的示唆 |
|----------|---------------------------|-------------------------|
| **法人 IT／セキュリティ・コンプライアンス** | エージェント機能の**段階的有効化**、ロールベース制御・Compliance API による可視化、リスクの高い公開（個人アカウント紐づけエージェント等）の抑制 | ヘルプ記載のとおり **Enterprise 初期はオフ**・**EKM 顧客は対象外**を前提に、**試験利用の範囲とデータ境界**を先に決めてから有効化する |
| **業務部門・PM（非エンジニア含む）** | サイドバー「Agents」から**テンプレまたは対話的ビルダー**でワークフローをエージェント化し、**Slack／スケジュール実行**まで含めて試す | 「モデル力」より **接続アプリ・承認フロー・監査ログ**を設計の中心に置く（公式も統制・承認を強調） |
| **開発者・業務システム担当** | **カスタム MCP** やコネクタ、**エージェント所有アカウント vs エンドユーザーアカウント**の認証設計を検討 | ヘルプの警告どおり、**共有接続＋Slack**では権限範囲と「他者がトリガーした際の影響」をレビューする |
| **経営・調達** | Business／Enterprise 等への継続利用と、**2026-05-06 以降のクレジット課金**に向けた予算・契約確認 | **5/6 前後の利用量とクレジット単価**を公式アナウンス・契約書で確認（本ブリーフ時点では単価の一次記載なし） |

---

## 3. 効果 — 短期・中期・長期の予想

**時間軸の定義（本資料）**

- **短期**: 直近 **0〜3か月**
- **中期**: **3か月〜1年**
- **長期**: **1年以上**

- **短期（0〜3か月）**:
  - **予想される効果**: 対象プラン組織での**パイロット利用**増、営業・CS・運用チームの定型レポート／ルーティング業務の一部自動化、Slack 上での問い合わせ一次対応の試行。
  - **不確実性**: **リサーチプレビュー**のため仕様変更・制限追加がありうる。**5/6 以降の課金**が利用パターンを変える。ヘルプに記載の **EKM 非対応**など、自社が該当すると展開が限られる。
  - **効果が出ない条件**: 管理者が有効化しない、コネクタ認証が整備されない、**プロンプトインジェクション**や誤った書き込み承認設定で運用が止まる。

- **中期（3か月〜1年）**:
  - **予想される効果**: 部門横断の「**再利用可能なエージェント**」の蓄積、GPTs からの移行・テンプレ標準化、Compliance API を前提にした**監査対応**の型。
  - **不確実性**: 競合製品との機能・価格比較で**乗り換え・併用**が進む可能性。クレジット課金後の**TCO**がボトルネックになるかは公式情報が限定的。
  - **効果が出ない条件**: 組織内でエージェントが乱立しガバナンスが追いつかない、または逆に統制過多で現場が使わない。

- **長期（1年以上）**:
  - **予想される効果**: 公式が示唆する「**Codex アプリでの workspace agents 対応**」など、開発ツールと業務チャットの**一本化されたエージェント体験**への拡張（[Introducing workspace agents](https://openai.com/index/introducing-workspace-agents-in-chatgpt/) の What’s next）。
  - **不確実性**: 規制・契約・業界別コンプライアンス（金融・医療等）がプロダクト境界を変えうる。**長期の産業構造予測は本件の一次ソースからは導けない**。
  - **効果が出ない条件**: 企業が「チャット UI 上の自律実行」を許容しない方針に転じる、または別アーキテクチャ（オンプレ・専用モデル）に回帰する。

**数値について**: OpenAI 公式ブログに **Rippling** の顧客コメントとして、週 **5〜6 時間**かかっていた作業がバックグラウンドで回る例が引用されている。これは**事例紹介**であり、一般化された効果測定ではない。

---

## 4. note 執筆メモ（任意）

- **フック案（1〜2文）**: 「カスタム GPT」の次は**チームで育てるクラウドエージェント**——OpenAI が **Codex** を背中に据え、**5月6日まで無料**のリサーチプレビューを切った。法人向けには**オフから始まる**スイッチと、**Compliance API** という監査の手がかりもセットになっている。
- **検証が必要な一点（事実・数値・日付）**:
  - **2026-05-06 以降のクレジット単価・枠**（本投稿時点では「credit-based」のみ）。
  - **GPTs → workspace agents 変換**の具体的 UI・互換範囲（「Soon」）。
  - **Codex アプリ**側の workspace agents 対応の時期・範囲（ロードマップ記述レベル）。
- **免責・注意**: 本資料は公開情報の整理であり、**投資・契約・法務判断**の代わりにはならない。EKM・データ residency 等は契約とヘルプの最新版で確認すること。

---

## 5. 参照一覧

- [OpenAI — Introducing workspace agents in ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)（一次・2026-04-22）
- [OpenAI Help Center — ChatGPT Workspace Agents for Enterprise and Business](https://help.openai.com/en/articles/20001143)（準一次・運用・管理画面の事実）
- [OpenAI — Codex for (almost) everything](https://openai.com/index/codex-for-almost-everything/)（一次・直前の Codex 大型更新、文脈用 2026-04-16）
- [OpenAI — Prompt injections（安全説明）](https://openai.com/safety/prompt-injections/)（workspace agents 投稿内からリンク）

---

**深掘りモード**: **ライト**（主に OpenAI 公式投稿＋ヘルプセンターで事実充足。規制当局・訴訟・CVE が主役ではないためサブエージェント並列調査は未実施。）
