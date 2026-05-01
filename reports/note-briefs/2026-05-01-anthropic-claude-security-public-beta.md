# 報告資料: Anthropic「Claude Security」パブリックβと法人コードベース走査

- **調査日**: 2026-05-01
- **主出典（一次）**: [Claude — Claude Security is now in public beta](https://claude.com/blog/claude-security-public-beta)（**Date: April 30, 2026**）
- **主出典（報道・二次）**: [The Verge](https://www.theverge.com/ai-artificial-intelligence/921198/anthropic-rolls-out-its-codebase-scanning-security-tool-for-businesses)（Posted Apr 30, 2026 at 5:00 PM UTC）
- **補助（製品概要・FAQ）**: [Claude — Claude Security（ソリューション）](https://www.claude.com/solutions/claude-code-security)
- **要約（1文）**: Anthropic は **2026年4月30日**、**Claude Enterprise** 向けにコードベース脆弱性の走査と修正案提示を行う **「Claude Security」** を **パブリックβ**として全法人顧客に開放し、エンジンは **Claude Opus 4.7**、旧称は **Claude Code Security** と明記された。

---

## 1. 背景 — なぜ今この情報が出ているか

- **事実（時系列）**:
  - **2026-04-30（公式）**: 「Claude Security」が **パブリックβ**となり、**Claude Enterprise** 全顧客が利用可能になったと発表。**Claude Opus 4.7** でスキャン・修正案生成が行われる旨、**旧称 Claude Code Security** であり数百社規模の **限定リサーチプレビュー** 済みである旨が記載されている（[公式ブログ](https://claude.com/blog/claude-security-public-beta)）。
  - 同日付記事で、**Mythos Preview**（Glasswing 文脈）とは別線で、**一般提供モデル（Opus 4.7）** を幅広い組織の **防御側** に届ける狙いが説明されている（同上）。
  - **利用形態**: Claude.ai サイドバーまたは `claude.ai/security`、リポジトリ／ディレクトリ／ブランチのスコープ指定、スキャン後に説明・重要度・再現手順・パッチ案を提示し、**Claude Code on the Web** で修正を進められる流れとある（同上）。
  - **パートナー統合**: CrowdStrike、Microsoft Security、Palo Alto Networks、SentinelOne、TrendAI、Wiz などが **Opus 4.7** をセキュリティ製品に組み込む動きとして列挙されている（各リンクは公式ブログ内）。
  - **アクセス**: 現時点では **Enterprise のみ**。**Claude Team / Max** は **coming soon**（[公式ブログ](https://claude.com/blog/claude-security-public-beta)、[製品FAQ相当](https://www.claude.com/solutions/claude-code-security)）。
  - **管理**: 管理者が **admin console**（`claude.ai/admin-settings/claude-code`）で有効化（同上）。

- **公開情報から読み取れる動機**:
  - 「脆弱性発見と悪用の間のタイムラインが **AIによって圧縮**される」「組織は **防御側にフロンティア能力**を揃えるべき」という **市場・脅威環境**の話として位置づけられている（[公式ブログ](https://claude.com/blog/claude-security-public-beta)）。
  - **Mythos**（高能力検出・悪用寄りの議論）と混同されないよう、**一般利用可能モデルでの防御製品**として線を引いている（同上、The Verge も同趣旨）。

- **補足・推測（根拠付き）**:
  - **命名変更**（Claude Code Security → Claude Security）は、製品の認知・検索・チャネル整理の可能性があるが、公式は「先行プレビューからの進化」説明に留めており、**ブランド戦略の内部理由は未開示**。
  - **競合**（GitHub Advanced Security、SAST/SCA ベンダ、他LLMベンダの類似機能）との差分は、公式は「パターン照合ではなく文脈・データフロー理解」と **定性的**に説明。**シェア・価格の定量比較は本ブリーフでは扱わない**（出典なしのため）。

---

## 2. 目的 — 誰に、何をしてほしいか

| 想定読者 | 発信側が望む行動（推定） | note 読者への実務的示唆 |
|----------|---------------------------|-------------------------|
| **Enterprise の管理者・セキュリティ責任者** | admin console で **Claude Security を有効化**し、[Getting Started](https://claude.com/resources/tutorials/getting-started-with-claude-security) に沿ってリポジトリ接続・スキャンを開始する | 利用規約・**データ取扱い・コード持ち込み**（自社ポリシー・顧客契約）と突合してからパイロット範囲を決める |
| **AppSec／開発チーム** | **スキャン結果のパッチ案は人間がレビュー・承認**してから適用（誤検知・不安全な修正リスクへの注意がFAQでも明示） | 既存の **SAST/DAST・チケット運用（Jira 等）** と webhook／エクスポートを接続し、**トリアージ手順**（却下理由の記録含む）を決めてから定期スキャンにする |
| **経営・調達** | 「防御側への Opus 4.7」として **パートナー経由（EDR/CNAPP/SIEM 等）または直接**の導入経路を検討 | **単一ツール信仰を避け**、検出→優先度付け→パッチの **プロセス KPI**（公式ブログは「scan to fix」を重視）で効果を測る |
| **一般メディア読者** | Mythos と **別製品**であることを理解する | note では **「攻撃支援モデル規制」と「法人向け防御スキャン」**の軸を混ぜない |

---

## 3. 効果 — 短期・中期・長期の予想

**時間軸の定義（本資料）**

- **短期**: 0〜3か月  
- **中期**: 3か月〜1年  
- **長期**: 1年以上  

- **短期（0〜3か月）**:
  - **予想される効果**: Enterprise での **パイロット導入・PoC** が増え、一部チームで「高信頼度の検出→修正までのリードタイム短縮」が事例として共有されうる（公式はリサーチプレビュー期間のニーズに基づき **スケジュールスキャン・ディレクトリ指定・却下理由の記録** 等を強調）。
  - **不確実性**: **β** ゆえの機能変更、**誤検知・見逃し**の実測は組織ごとに異なる。**Opus 4.7 のサイバー系セーフガード**と業務利用の重なりは [Cyber Verification Program](https://support.claude.com/en/articles/14604842-real-time-cyber-safeguards-on-claude) の適用範囲確認が必要（公式注脚）。
  - **効果が出ない条件**: レビュー人員不足で **パッチが滞留**、リポジトリ接続範囲が狭すぎて **カバレッジが偏る**、既存ツールとの **二重運用のみ**でプロセスが整理されない場合。

- **中期（3か月〜1年）**:
  - **予想される効果**: **Team / Max** への拡大（公式予告）により利用層が広がる可能性。**Wiz・CrowdStrike 等**のプロダクト内統合と併せ、**「LLMによるセマンティック診断」** がエンタープライズAppSecの **標準説明**の一部になりうる。
  - **不確実性**: 競合の同等機能リリース、**規制当局**や顧客監査が「生成AIによるコード提案」の **証跡・責任分界**をどう求めるかは法域・業種依存。
  - **効果が出ない条件**: 組織が **ガバナンス（データ境界、サプライヤ条項）** を満たせず利用停止・縮小する場合。

- **長期（1年以上）**:
  - **予想される効果**: モデル世代交代に伴い、**見つかる欠陥クラスや自動修正案の品質**が変化し、SAST市場と **アシスト型レビュー**の境界が再編されうる（一般論；**数値予測は出典なしのため割愛**）。
  - **不確実性**: **悪用側モデル**の能力向上と規制・輸出管理の動き（Mythos / Glasswing 文脈と別レーンだが同一企業ストーリー内）。
  - **効果が出ない条件**: 組織が **人的レビューを外し**自動マージに依存してインシデントを起こし、ツール全体への信頼が損なわれる場合（FAQが警告するリスク）。

---

## 4. note 執筆メモ（任意）

- **フック案（1〜2文）**: 「評価額や Mythos 論争と**別レーン**で、Anthropic は **日常の法人コード**に Opus 4.7 を載せた **防御製品**をオープンβにした」ことが、底稿（Opus 4.7／NEC パートナー）の「**エンタープライズで何が売れるか**」の更新材料になる。
- **検証が必要な一点（事実・数値・日付）**: **「数百社のリサーチプレビュー」**や顧客引用は公式ブログ記載ベース。**Team/Max の具体的解禁日**は未記載のため「coming soon」のみとする。
- **読み違い防止**: **Claude Security（防御・スキャン）** と **Mythos Preview（Glasswing・高リスク能力の話）** を同一記事で **混同しない**（`reports/overseas-it-news/news-log.md` の当該ブロックの整理どおり）。
- **免責・注意**: 製品導入・契約・法務判断は **自社窓口・専門家**に依頼。本資料は公開情報の整理であり、投資助言ではない。

---

## 5. 参照一覧

- Anthropic / Claude — [Claude Security is now in public beta](https://claude.com/blog/claude-security-public-beta)（**April 30, 2026**；**一次**）
- Claude — [Claude Security（ソリューションページ）](https://www.claude.com/solutions/claude-code-security)（製品説明・FAQ・**一次**）
- Anthropic — [Introducing Claude Opus 4.7](https://www.anthropic.com/research/claude-opus-4-7)（モデル能力・セーフガードの文脈；**一次**）
- The Verge — [Anthropic rolls out its codebase-scanning security tool for businesses](https://www.theverge.com/ai-artificial-intelligence/921198/anthropic-rolls-out-its-codebase-scanning-security-tool-for-businesses)（**2026-04-30**；**二次**・要約報道）

---

## 関連 note 底稿（ログ 984 行付近より）

- `note/202604/20260417/2026-04-17-anthropic-claude-opus-4-7｜Opus-4.7とサイバー安全策の一段目.md`
- `note/202604/20260424/2026-04-24-nec-anthropic-enterprise-ai｜NECがAnthropicの「日本拠点初のグローバルパートナー」になった話.md`
