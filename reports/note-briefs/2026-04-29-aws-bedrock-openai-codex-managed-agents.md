# 報告資料: AWS×OpenAI — Bedrock 上的モデル・Codex・マネージドエージェント（限定プレビュー）

- **調査日**: 2026-04-29
- **主出典**: [About Amazon (AWS)](https://www.aboutamazon.com/news/aws/bedrock-openai-models)（記事末尾の公開日時: 2026-04-28T17:00:03+00:00）、[OpenAI — OpenAI models, Codex, and Managed Agents come to AWS](https://openai.com/index/openai-on-aws)（2026-04-28）
- **要約（1文）**: Microsoft–OpenAI 提携改定（2026-04-27）で「任意クラウドへの提供」が契約上明文化された直後に、AWS と OpenAI が Amazon Bedrock 経由で最新モデル・Codex・OpenAI 基盤のマネージドエージェントを**いずれも限定プレビュー**で提供開始すると公表し、エンタープライズ向けの「既存 AWS 環境での調達・統制・運用」と OpenAI 製品の接続を前面に出した。

---

## 1. 背景 — なぜ今この情報が出ているか

- **事実（時系列）**:
  - **2026-04-27**: Microsoft と OpenAI が提携契約の改定を公表。Microsoft は引き続き OpenAI のプライマリクラウドパートナーで、製品は原則 Azure に先行提供するが、Microsoft が必要能力を支援できない／しない場合は他クラウドも可。**OpenAI は全製品を任意のクラウドプロバイダー経由で顧客に提供できる**旨が明記されている。Microsoft の OpenAI IP に対するライセンスは 2032 年まで継続するが**非独占**に。Microsoft の OpenAI へのレベニューシェア支払いは終了。OpenAI から Microsoft へのレベニューシェアは 2030 年まで継続（割合は同率、総額に上限）等。 — 出典: [The Official Microsoft Blog — The next phase of the Microsoft-OpenAI partnership](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)、[OpenAI — The next phase of the Microsoft OpenAI partnership](https://openai.com/index/next-phase-of-microsoft-partnership/)（いずれも 2026-04-27）
  - **2026-04-28**: AWS（About Amazon）と OpenAI がそれぞれ、**Amazon Bedrock 上での最新 OpenAI モデル**、**Amazon Bedrock 上の Codex**、**Amazon Bedrock Managed Agents, powered by OpenAI** の提供開始を**限定プレビュー**で発表。推論は Amazon Bedrock インフラ上で行い、IAM・PrivateLink・ガードレール・CloudTrail 等の既存のエンタープライズ統制を引き継ぐ叙述。Codex は Bedrock API 経由、Codex CLI・デスクトップアプリ・VS Code 拡張から開始との記載。 — 出典: [About Amazon — AWS and OpenAI announce expanded partnership…](https://www.aboutamazon.com/news/aws/bedrock-openai-models)、[OpenAI — OpenAI models, Codex, and Managed Agents come to AWS](https://openai.com/index/openai-on-aws)

- **公開情報から読み取れる動機**:
  - AWS／OpenAI の両稿は、**企業が最前線のモデル・エージェントを求めつつ、既に依存しているクラウド上のセキュリティ・統治・調達・運用成熟度も必要**と説明しており、Bedrock 一本化・AWS のコミットメントへの計上など**単一パスでの本番利用**を訴求している。
  - Microsoft–OpenAI 側の公表は、**柔軟性と予見可能性**、大規模 AI プラットフォーム運営と新機会の両立を謳っており、OpenAI のマルチクラウド展開を**契約面で後ろ盾する**タイミングと整合する。

- **補足・推測（根拠付き）**:
  - **news-log が指す「改定の実行面での裏付け」**は、4/27 公式文書上の「任意クラウドへの提供」と 4/28 の Bedrock 提供発表が**日付的に連続**していることから、読者・編集向けの**文脈整理として自然**だが、両社が「先に技術用意→改定」「改定合意後に即公開」と**因果の順序を公式に述べた掲載は確認していない**。
  - **競合クラウド（GCP 等）との差別化やシェア防衛**は業界常識レベルの解釈にとどまり、本件のプレスリリース単体では**主目的の断定は不可**。

---

## 2. 目的 — 誰に、何をしてほしいか

| 想定読者 | 発信側が望む行動（推定） | note 読者への実務的示唆 |
|----------|---------------------------|-------------------------|
| **AWS 上で本番ワークロードを持つエンタープライズ（開発・プラットフォーム・調達）** | Bedrock 経由で OpenAI モデル／Codex／Managed Agents の**限定プレビュー利用を検討**し、既存の IAM・ログ・コンプライアンス枠組みの下で評価する。関心登録フォームや問い合わせへ誘導（AWS 側ページ）。 | **限定プレビュー**のため、**自社の利用資格・リージョン・データ取扱い**を AWS／OpenAI の利用条件と照合する。**Azure 先行**等の提携条項が自社契約に与える影響は別途整理。 |
| **OpenAI API と AWS を併用している開発組織** | Codex を **Bedrock をプロバイダーとして構成**し、CLI・デスクトップ・VS Code から試す（OpenAI 投稿の手順叙述）。 | 請求・データ所在地・出口統制を**単一のクラウド請求**に寄せられるかを評価。プレビュー範囲外機能の有無をリリースノート相当で確認。 |
| **エージェント基盤を標準化したいアーキテクト** | Bedrock Managed Agents（OpenAI モデル・エージェント能力）と **Bedrock AgentCore** の役割分担を理解し、スケール時の認可・可観測性等のロードマップを追う（AWS 稿内の相互補完の説明）。 | 「インテリジェンス（OpenAI）」と「運用基盤（AWS）」の**境界と監査ログ**を設計レビューに入れる。 |

---

## 3. 効果 — 短期・中期・長期の予想

※ **短期** = おおよそ 0〜3 か月／**中期** = 3 か月〜1 年／**長期** = 1 年以上（本資料内の定義）。

- **短期（0〜3か月）**:
  - **予想される効果**: 既存 AWS 顧客の**評価・PoC 需要**が増える。メディア・投資家の関心が「OpenAI のマルチクラウド」文脈で一段まとまる。競合クラウドも同種の「統合マーケットプレイス」訴求を強める**プレッシャー**になる可能性。
  - **不確実性**: 限定プレビューの**申込条件・提供地域・SLA**は公表ページだけでは個社判断に不足しうる。価格・クォートは別途アナウンスに依存。
  - **効果が出ない条件**: 企業がプレビュー対象外、またはデータレジデンシー・規制で Bedrock 経由を選べない。

- **中期（3か月〜1年）**:
  - **予想される効果**: **一般提供（GA）**とモデル・エージェント機能の拡張により、Bedrock 内の**モデル複合（Anthropic / Meta 等と並列）**が進み、調達が「AWS 一本」に寄る案件が増える可能性。Codex 利用が AWS コミット消化に寄与する叙述は顧客 CFO 目線の訴求になりうる。
  - **不確実性**: Microsoft–OpenAI の「Azure 先行」条項が**特定製品のリリース順**にどう現れるかは、個別ローンチごとに要追跡。
  - **効果が出ない条件**: モデル性能・価格・レイテンシで OpenAI 直販や他チャネルが優位のまま。

- **長期（1年以上）**:
  - **予想される効果**: **クラウド中立に近い AI 調達**がエンタープライズ標準で、ベンダー境界が「推論 API」から「エージェント実行基盤＋統制」へ移る。OpenAI–AWS–Microsoft の**資本・契約・電力・シリコン**の組み合わせが産業地図として固定化されうる。
  - **不確実性**: 規制分岐、地政学、大口顧客のリパトリエーション、訴訟・独占政策。
  - **効果が出ない条件**: 技略的提携が縮小、またはオンプレ／別スタックへの回帰が主潮流になる。

---

## 4. note 執筆メモ（任意）

- **フック案（1〜2文）**: 「独占」を外した翌日、Bedrock に OpenAI が載った——日付を並べるだけでも読者の**制度変化とプロダクト**を同じ画面に置ける。
- **検証が必要な一点（事実・数値・日付）**: OpenAI 稿では **GPT-5.5 を Bedrock で利用可能と明記**（2026-04-28 時点）。About Amazon 側は「最新の OpenAI モデル」と表現。**同一モデル名を AWS 公式が別ページでどう一覧化しているか**は `aws.amazon.com/bedrock/openai/` 等で最終確認推奨。Codex の「週 4百万人ユーザー」は両公式稿に記載——**定義（MAU か週次か等）**はメソッド非公表のため注意書き必須。
- **免責・注意**: 本資料は公開プレス・ブログに基づく整理であり、**投資判断・契約・法務・税務**の助言ではない。限定プレビューの条件は変更されうる。

---

## 5. 参照一覧

- [About Amazon — AWS and OpenAI announce expanded partnership to bring frontier intelligence…](https://www.aboutamazon.com/news/aws/bedrock-openai-models)（一次：Amazon 公式ニュース）
- [OpenAI — OpenAI models, Codex, and Managed Agents come to AWS](https://openai.com/index/openai-on-aws)（一次：OpenAI）
- [Microsoft — The next phase of the Microsoft-OpenAI partnership](https://blogs.microsoft.com/blog/2026/04/27/the-next-phase-of-the-microsoft-openai-partnership/)（一次：Microsoft）
- [OpenAI — The next phase of the Microsoft OpenAI partnership](https://openai.com/index/next-phase-of-microsoft-partnership/)（一次：OpenAI）
- **リポジトリ内底稿（二次扱い・執筆文脈用）**: `note/202604/20260428/2026-04-28-microsoft-openai-partnership-amendment｜プライマリは残し独占は外した.md`、`note/202604/20260402/OpenAI約1220億ドル調達を公式ベースで整理｜computeとパートナーが主役.md`（news-log 記載どおり）

---

**調査モード**: ライト（Web 取得・検索による一次・公式の収集。規制・訴訟の深掘りは本件では Task レーン B〜E は未起動）
