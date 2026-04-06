# 海外ITニュース調査ログ（累積）

このファイルは `**/overseas-it-news**` の実行ごとに**追記**する。  
**重複排除**は `seen-urls.json` に記録した出典URLで行う（同じURLの記事は再掲しない）。

**掲載日（鮮度）:** 「新規トピック」の主出典は、調査日を **D**（本見出しの日付）としたとき **JST で D−1 以降に公開**されたものを原則とする。詳細は `news-recency-policy.md`。

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

---

## 調査 2026-04-04 14:00 （JST）

公開情報の掲載時期はおおむね **2026年4月1日〜4日**。チャット実行時点の速報ベース。Cisco の IMC 欠陥は **Cisco Security Advisory（公式）** で CVSS 9.8・修正版が列挙されていることを確認済み。

### 新規トピック

#### セキュリティ・インフラ

- **Cisco Integrated Management Controller（IMC）の認証バイパス（CVE-2026-20093、Critical）** — パスワード変更処理の不備で、未認証のリモート攻撃者が管理者権限相当の操作に至る可能性。ワークアラウンドはなく、修正ファームウェアへの更新が推奨。PSIRT は公開時点で悪用の認知なしと記載。出典: [Cisco](https://www.cisco.com/c/en/us/support/docs/csa/cisco-sa-cimc-auth-bypass-AgG2BxTn.html)
- **WordPress プラグイン CleanTalk の認可バイパス（CVE-2026-1490）** — PTR スプーフィング経由で任意プラグインのインストール等が可能になる脆弱性（Wordfence 経由で CNA 登録、CVSS 3.1 で 9.8）。無効な API キー利用サイトに限定されうる旨が NVD 説明に明記。出典: [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-1490)

#### 監視・法執行・プライバシー

- **米 ICE が Paragon のスパイウェアを薬物密売対策で導入・使用したと国会議員宛て書簡で説明** — TechCrunch が書簡を根拠に報道。暗号化通信への対応として「先端ツール」利用を言及、憲法上の要件順守などと記載。出典: [TechCrunch](https://techcrunch.com/2026/04/02/ice-says-it-bought-paragons-spyware-to-use-in-drug-trafficking-cases/)

#### 半導体・投資

- **Intel が SambaNova への追加出資（約1,500万ドル）を検討、承認後は持株比率 9% へ** — Reuters が企業記録のレビューとして報じ、Tan CEO 兼任によるガバナンス論点にも言及。Intel は統治・利益相反方針をコメント。出典: [Reuters](https://www.reuters.com/business/intel-looks-put-millions-more-into-sambanova-startup-chaired-by-ceo-tan-2026-04-01/)

#### アプリ・生成 AI

- **Google Vids にアバターをプロンプトで指示する機能や Veo 3.1 連携など** — 動画編集アプリへの機能追加として TechCrunch が紹介（YouTube へのエクスポート、Chrome 拡張の画面録画など）。出典: [TechCrunch](https://techcrunch.com/2026/04/02/google-now-lets-you-direct-avatars-through-prompts-in-its-vids-app/)

### メモ（任意）

- **Chrome CVE-2026-5281**・**Gemma 4**・**MAI モデル**等は過去ログの主出典と重複のため省略。
- エイプリルフール時期のため、**単独の煽り見出し**は公式・一次に照合したトピックを優先。

---

## 調査 2026-04-06 14:31 （JST）

**調査日 D＝2026-04-06。** `news-recency-policy.md` により、新規トピックの主出典は **公開日が JST で 2026-04-05 または 2026-04-06** のものに限定。読者ペルソナは `target-persona-product-ai-pm.md`（事業側PM）— 各項目に **So what（PM）** を併記。

### 新規トピック

#### 生成AI×プロダクト体験（地図・実世界タスク）

- **Google マップの「Ask Maps」（Gemini）で一日の行程を組ませる体験記（公開 2026-04-05）** — レビュアーが公共交通・飲食・散策など複合条件で依頼し、レビュー要約や天気連携は有用一方、**位置や店名の誤誘導（ハルシネーション）**も実際に発生したと報告。**So what（PM）:** ロケーション系・オンデバイス案内に生成AIを載せる場合の **誤誘導時の責任分界・フォールバック（地図本体の経路UIへ戻す等）**を要件に含める材料。出典: [The Verge](https://www.theverge.com/tech/907015/gemini-google-maps-hands-on)（掲載日: 2026-04-05）

#### 生成AI×法務・プラットフォームガバナンス（著作権・配信）

- **AI音楽サービス Suno の Studio が、簡単な加工で有名曲のカバー生成につながりうるとする検証報道（公開 2026-04-05）** — 利用規約上は他者著作物の利用を禁じる一方、フィルタ回避の手口や、出力・配信チェーン（ストリーミングアップロード等）のリスクを論じる。**So what（PM）:** UGC／生成物を扱うプロダクトの **ポリシー文言・検知・再スキャン・B2B配信パイプライン**を法務・パートナーと点検する際の論点整理。出典: [The Verge](https://www.theverge.com/ai-artificial-intelligence/906896/sunos-copyright-ai-music-covers)（掲載日: 2026-04-05）

#### 音声AI・デバイス戦略（歴史から学ぶ意思決定）

- **Amazon Echo／Alexa の開発史を扱う Verge の Version History エピソード紹介（公開 2026-04-05）** — 音声ショッピング仮説と実利用のズレ、音楽・スマートホームでの伸び、後発 Siri との関係などを対談形式で要約。**So what（PM）:** 「AIアシスタント」の **キラー用途設計・計測指標・社内説明**を、過去の大規模C向け事例として参照する一次エピソード（メディア取材）。出典: [The Verge](https://www.theverge.com/podcast/907146/amazon-echo-alexa-version-history)（掲載日: 2026-04-05）

### メモ（任意）

- **2026-04-06 当日分**の主出典は、実行時点の検索では**日付確認できる公式プレスに到達せず**、本ブロックは **D−1（4/5）掲載の確実なソース**に限定。
- Anthropic×OpenClaw の課金変更など **4/3 付の報道**は、鮮度ポリシーにより新規トピックから除外。

