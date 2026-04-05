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

## 調査 2026-04-05 16:00 （JST）

公開情報の掲載時期はおおむね **2026年3月下旬〜4月5日**。チャット実行時点の速報ベース。Progress ShareFile・FortiClient EMS は **NVD / Fortinet PSIRT** で説明・深刻度を確認済み。

### 新規トピック

#### セキュリティ

- **Progress ShareFile Storage Zones Controller に認証回避と RCE（CVE-2026-2699・CVE-2026-2701）** — 顧客管理型 SZC で、未認証の設定ページアクセスやファイルアップロード経由のコード実行につながる可能性。CNA は Progress、CVE-2026-2699 は CVSS 3.1 で 9.8（CRITICAL）。ベンダは Storage Zones Controller 5.x 向け修正・文書を参照。出典: [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-2699)（CVE-2026-2701 は同一製品ラインの連鎖として [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-2701) でも登録）
- **FortiClient EMS の認証・認可バイパス（CVE-2026-35616）が実害型で悪用** — Fortinet が「悪用を確認」とし、7.4.5 / 7.4.6 向けホットフィックスと 7.4.7 への修正予定を案内。7.2 系は非該当。出典: [Fortinet PSIRT](https://fortiguard.fortinet.com/psirt/FG-IR-26-099)

#### 金融IT・プライバシー

- **英ロイズ銀行グループのシステム不具合で最大約44.8万人分のデータが露出** — 夜間更新のソフト欠陥が原因で、他顧客の取引・口座・国民保険番号などが見える事象。補償・当局対応・委員会への報告が Reuters で整理。出典: [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/nearly-half-million-customers-hit-by-lloyds-it-glitch-that-exposed-transaction-2026-03-27/)

#### 半導体・製造

- **Intel がアイルランド Fab 34 合弁の Apollo 持分 49% を約142億ドルで買い戻し** — 2024年の共同投資からの再取得で、現金と約65億ドル規模の新規債で資金調達。Fab 34 は Intel 4 / Intel 3 製品の拠点として位置づけ。出典: [Intel Newsroom](https://newsroom.intel.com/corporate/intel-repurchase-49-equity-interest-ireland-fab-joint-venture)

#### AI・ガバナンス

- **Microsoft が自律エージェント向け「Agent Governance Toolkit」をオープンソース公開** — ポリシーエンジン・ID/信頼スコア・ランタイム分離・コンプライアンス対応など7パッケージ、OWASP Agentic AI リスクへの対応を公式に説明。MIT ライセンス。出典: [Microsoft Open Source Blog](https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/)

#### AI・メディア

- **OpenAI がテック業界トーク番組 TBPN を買収** — メディア会社としての初の買収と報じられ、番組はブランド維持・編集の独立性に言及。出典: [TechCrunch](https://techcrunch.com/2026/04/02/openai-acquires-tbpn-the-buzzy-founder-led-business-talk-show/)

### メモ（任意）

- **MAI モデル・Gemma 4・GPT-5.4** 等は過去ログの主出典と重複のため省略。
- FortiClient の **CVE-2026-21643**（別CVE）は過去検索結果で言及あり。本件 **CVE-2026-35616** は Fortinet が 2026-04-04 に初版公開した別脆弱性。

