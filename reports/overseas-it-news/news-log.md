# 海外ITニュース調査ログ（累積）

このファイルは `**/overseas-it-news**` の実行ごとに**追記**する。  
**重複排除**は `seen-urls.json` に記録した出典URLで行う（同じURLの記事は再掲しない）。

---

## 調査 2026-04-02 （JST）

公開情報の掲載時期はおおむね **2026年3月下旬〜4月初旬**。チャット実行時点の速報ベース。

### 新規トピック

#### AI・企業動向

- **OpenAI が大規模資金調達を発表** — 次フェーズのAIインフラ加速を目的としたラウンドで、評価額・投資家構成などを公式に説明。出典: [OpenAI](https://openai.com/index/accelerating-the-next-phase-ai/)
- **GPT-5.4 の公開** — 推論・コーディング・エージェント向け機能の強化として位置づけ。出典: [OpenAI](https://openai.com/index/introducing-gpt-5-4/)
- **Microsoft「Copilot Cowork」** — Frontier Program 向けに、複数モデルを組み合わせたエンタープライズ調査・作業支援の提供が進む、という公式系報道。出典: [Microsoft Source EMEA](https://news.microsoft.com/source/emea/2026/03/copilot-cowork-now-available-in-the-frontier-program/)

#### インフラ

- **テキサス拠点のAIデータセンター拡張で Microsoft が主導的役割** — OpenAI 側が同拡張を進めない見通しとなり、Microsoft がプロジェクトを引き取る、とする通信社報道。出典: [AP News](https://apnews.com/article/ai-stargate-microsoft-openai-crusoe-oracle-f4f74c3a4617d8cfab5b933fc31ccc6e)

#### セキュリティ

- **Citrix NetScaler（ADC/Gateway）のメモリ関連欠陥が実害型で悪用** — SAML IdP 構成などが条件。管理セッション窃取に結びつく恐れとして専門メディアが継続追跡。出典: [BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-citrix-netscaler-memory-flaw-actively-exploited-in-attacks/)
- **F5 BIG-IP APM の RCE（CVE-2025-53521）が悪用されているとの警告** — CISA KEV 掲載・連邦調達向け対応の文脈で報じられている。出典: [Help Net Security](https://www.helpnetsecurity.com/2026/03/28/big-ip-apm-vulnerability-cve-2025-53521-exploited/)
- **CISA が KEV に脆弱性を追加（アラート 2026-03-26）** — サプライチェーン／スキャナ関連の注意喚起の一環として参照すべき一次情報。出典: [CISA](https://www.cisa.gov/news-events/alerts/2026/03/26/cisa-adds-one-known-exploited-vulnerability-catalog)

### メモ（任意）

- 4月1日前後に報じられた **Arm の自社シリコン**等はエイプリルフールと混同しうるため、本ログでは**公式一次情報の確認が取れるまで採用見送り**。
- メディア各社の **Oracle 大規模リストラ**報道は数値表記のブレが見られたため、本回は**単一出典に絞らず確証が付くまで保留**。

---

## 調査 2026-04-03 12:00 （JST）

公開情報の掲載時期はおおむね **2026年3月31日〜4月2日**。チャット実行時点の速報ベース。Chrome ゼロデイは **Google 公式リリースノート**で脆弱性・修正版が明記されていることを確認済み。

### 新規トピック

#### AI・オープンモデル

- **Google 公式が Gemma 4 を公開** — 推論・エージェントワークフロー向けに設計したオープンモデル群。E2B／E4B／26B MoE／31B など複数サイズ、Apache 2.0、長コンテキスト・多言語・マルチモーダルなどを公式に説明。出典: [Google Keyword (blog)](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/)

#### AI・企業動向

- **Microsoft が自社基盤モデル MAI を公開（音声・画像など）** — MAI-Transcribe-1、MAI-Voice-1、MAI-Image-2 を Microsoft Foundry 等で提供開始とする公式発表。出典: [Microsoft AI (news)](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/)
- **Microsoft が Copilot 系で GPT と Claude を組み合わせた「Critique」方式を報道** — 研究品質向上のため複数モデル連携を進める、とする報道。出典: [Axios](https://www.axios.com/2026/03/31/microsoft-critique-anthropic-openai)

#### セキュリティ

- **Chrome 安定版にゼロデイ修正（CVE-2026-5281、悪用確認）** — 2026年3月31日のデスクトップ向け Stable 更新として公開。出典: [Chrome Releases](https://chromereleases.googleblog.com/2026/03/stable-channel-update-for-desktop_31.html)

#### Web3・決済インフラ

- **Coinbase のエージェント向け決済プロトコル x402 が Linux Foundation 傘下へ** — オープンソース化・業界支援の動きとして CoinDesk が報道。出典: [CoinDesk](https://www.coindesk.com/tech/2026/04/02/coinbase-s-ai-payments-system-joins-linux-foundation-gathers-support-from-google-stripe-aws-and-others)

### メモ（任意）

- **F5 BIG-IP APM（CVE-2025-53521）**の「未修正インスタンス数」フォロー記事などは、前回ログの **同一事件**のため本回はURL追加せず省略。
- CISA は **2026-04-01** に同一 CVE を KEV に追加した旨の別アラートあり（本ログでは Chrome 公式リリースを主出典に集約）。

