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

---

## 調査 2026-04-07 11:30 （JST）

**調査日 D＝2026-04-07。** `news-recency-policy.md` により、新規トピックの主出典は **JST で 2026-04-06 または 2026-04-07** に公開（記載）されたもの。Tesla 調査終了・Broadcom は **Reuters 本文日付**、Axios 事件は **TechCrunch 掲載日**で確認。

### 新規トピック

#### 半導体・AIインフラ

- **Broadcom が Google と次世代カスタムAIチップ等の長期供給で合意（2031年まで）** — Google の次世代AIラック向けに TPU 等を開発・供給。別途 Anthropic と約3.5GW規模のAI計算容量（Google のAIプロセッサ活用、2027年開始）の取引も発表、金額は非公表。出典: [Reuters](https://www.reuters.com/business/broadcom-signs-long-term-deal-develop-googles-custom-ai-chips-2026-04-06/)（掲載: 2026-04-06）
- **Reuters Breakingviews：計画段階のデータセンター需要と資金調達ギャップ** — 計画中の約110GW規模の案件と、1GWあたりの建設コスト試算から総額が数兆ドル規模に膨らみうる一方、ハイパースケーラーのキャッシュフロー・社債・インフラ基金などを積み上げても「紙の上」では足りても、株主還元・集中リスク・送配電など周辺コストで計画の相当部分は実現しない（vaporware）可能性が高い、という**解説・意見**枠。出典: [Reuters Breakingviews](https://www.reuters.com/commentary/breakingviews/ai-dreams-crash-into-stark-7-trln-reality-2026-04-07)（掲載: 2026-04-07）

#### モビリティ・規制

- **NHTSA が Tesla「Actually Smart Summon」調査を終了** — 約260万台対象の調査で、主に低速・物損にとどまり死傷なしとし、追加措置は不要と判断。障害物検知やカメラ曇り等への OTA 更新で対応したと整理。FSD 系は別件で工程が進む文脈。出典: [Reuters](https://www.reuters.com/business/autos-transportation/us-auto-safety-regulator-closes-probe-into-teslas-driver-assistance-feature-2026-04-06/)（掲載: 2026-04-06）

#### セキュリティ・OSS

- **北朝鮮系とみられる攻撃が Axios メンテナーに長期のソーシャルエンジニアリングの後侵害** — 偽企業・Slack・偽ミーティング経由でマルウェア実行し、3/31 に悪意ある npm 公開（約3時間で取り下げ）。メンテナーが GitHub でポストモーテム公開。出典: [TechCrunch](https://techcrunch.com/2026/04/06/north-koreas-hijack-of-one-of-the-webs-most-used-open-source-projects-was-likely-weeks-in-the-making/)（掲載: 2026-04-06）

#### プラットフォーム・法務

- **Apple が Epic との App Store 手数料係争で再び最高裁審理を求める方針** — 外部決済への27%徴求が裁判所命令に反するとされた流れを受け、上告・差止めなどの動き。4/6 に控訴審が Apple の差止め動議を認めた旨を報道。出典: [TechCrunch](https://techcrunch.com/2026/04/06/apple-epic-games-lawsuit-supreme-court-appeal-app-store-commission/)（掲載: 2026-04-06）

#### 生成AI・プロダクト

- **Google が iOS向けオフライン優先の音声入力アプリ「Google AI Edge Eloquent」を公開** — Gemma ベースのASRを端末にダウンロード後、フィラー除去や文体変換など。クラウドモードでは Gemini による整形も可。出典: [TechCrunch](https://techcrunch.com/2026/04/06/google-quietly-releases-an-offline-first-ai-dictation-app-on-ios/)（掲載: 2026-04-06）

#### メッセージング・エコシステム

- **Samsung が「Samsung Messages」を2026年7月に終了し Google Messages への移行を案内（米国告知）** — RCS・Gemini 連携などを理由に挙げ、古いAndroidは対象外など条件を記載。出典: [ABC News (AP)](https://abcnews.go.com/Technology/wireStory/samsung-discontinuing-texting-app-tells-impacted-users-switch-131766567)（掲載: 2026-04-06）

### メモ（任意）

- **Tesla Summon** は Electrek 等でも同一事件だが、本ブロックは **Reuters** を主出典に統一。
- Breakingviews 項目は**分析・コラム**であり投資判断材料としては一次の財務開示と区別して読む。

---

## 調査 2026-04-08 10:00 （JST）

**調査日 D＝2026-04-08。** `news-recency-policy.md` により、新規トピックの主出典は **JST で 2026-04-07 または 2026-04-08** に公開（記載）されたもの。Project Glasswing は **Anthropic 公式（ニュース一覧で Apr 7）**、CISA 勧告は **Release Date: April 07, 2026**、Intel×Terafab は **TechCrunch 掲載日（PDT Apr 7）**、Moto 製品は **Motorola 公式ニュース**（同日メディアと整合）、Android XR は **Google 公式ブログ Apr 07, 2026** で確認。

### 新規トピック

#### セキュリティ・OT

- **CISA、イラン系APTが米国重要インフラ向けRockwell/Allen-Bradley系PLC等を標的に悪用していると警告（AA26-097A）** — インターネット公開OT機器への攻撃、HMI/SCADA表示の改ざん、事業継続・金銭被害の事例を整理。PLCの直接公開回避、IOC照会、推奨緩和策を掲載。出典: [CISA](https://www.cisa.gov/news-events/cybersecurity-advisories/aa26-097a)（Release Date: April 07, 2026）

#### AI・サイバー防衛

- **Anthropic が「Project Glasswing」— 主要クラウド・セキュリティ・金融・半導体企業等と重要ソフトの防衛利用で連携** — 未公開フロンティアモデル「Claude Mythos Preview」を防御的スキャン・脆弱性発見に使う枠組み。数千件規模の重大欠陥発見の実績を説明し、利用クレジット最大約1億ドル・OSS向け寄付400万ドルなどを公表。出典: [Anthropic](https://www.anthropic.com/glasswing)（発表日: 2026-04-07）

#### 半導体・AIインフラ

- **Intel が Musk 陣営の「Terafab」半導体プロジェクトに参画（米テキサス製造）** — SpaceX・Tesla との協業に加え、大規模設計・製造・パッケージで1TW/年規模の算力目標を後押しするとする報道。Intel は X 上の企業投稿を引用。詳細は限定的。出典: [TechCrunch](https://techcrunch.com/2026/04/07/intel-signs-on-to-elon-musks-terafab-chips-project/)（掲載: 2026-04-07）

#### モバイル・ハードウェア

- **Motorola が「moto g stylus（2026）」と米国キャリア向けタブレット「moto pad（2026）」を発表** — アクティブスタイラス（傾き・筆圧）、11インチ2.5Kタブレット・MediaTek D6300 5G、価格・発売時期（例: タブレット4/30 T-Mobile系）を公式に案内。出典: [Motorola News](https://motorolanews.com/introducing-moto-g-stylus-2026-and-moto-pad-2026-where-ideas-take-shape-across-screens/)

#### XR・プラットフォーム

- **Google が Android XR に5機能をロールアウト（Galaxy XR向け）** — 実験機能「auto-spatialization」で2Dアプリ・Web・画像・動画を3D体験化、壁へのピン留め、ホーム空間での実手表示、セッション再開、100本超のXR向けアプリなどを公式に説明。出典: [Google Keyword (blog)](https://blog.google/products-and-platforms/platforms/android/android-xr-immersive-features-update-april-2026/)（掲載: Apr 07, 2026）

### メモ（任意）

- **Docker Engine / Moby の AuthZ プラグイン回避（CVE-2026-34040）** はメディアで4/7付の解説が出ているが、**NVD の公開日は 2026-03-30** のため、鮮度ポリシーにより本回の「新規トピック」には含めず。必要なら [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-34040) および [GitHub Advisory](https://github.com/moby/moby/security/advisories/GHSA-x744-4wpc-v9h2) を参照。
- **Anthropic の Google・Broadcom 向け計算拡大**は公式ニュースの日付が **2026-04-06** のため、D＝4/8 の **D−1 未満**として新規トピックから除外（過去ブロックの Broadcom 報道とも同一文脈）。

---

## 調査 2026-04-09 12:00 （JST）

**調査日 D＝2026-04-09。** `news-recency-policy.md` により、新規トピックの主出典は **JST で 2026-04-08 または 2026-04-09** に公開（記載）されたもの。**Shared AI License Foundation** は GlobeNewswire の **April 08, 2026**、**Gemini の notebooks** は Google 公式ブログ **Apr 08, 2026**、**Chrome Extended Stable** は Chrome Releases の **Wednesday, April 8, 2026** で確認。

### 新規トピック

#### 知的財産・AI産業

- **「Shared AI License Foundation（SAIL）」創設 — 基盤モデル関連特許の非独占ライセンス共有** — Anthropic、Genentech（Roche）、IBM、Meta、Microsoft が創設理事、eBay・TD Bank Group がオブザーバー。Block・Figma がメンバー参加。会員間で基盤モデル特許を非独占ライセンスし開発を加速する「共有特許コモンズ」を掲げ、Gartner 予測の2026年AI支出規模なども言及。出典: [GlobeNewswire（Shared AI License Foundation）](https://www.globenewswire.com/news-release/2026/04/08/3270111/0/en/AI-Pioneers-Unite-to-Launch-the-Shared-AI-License-Foundation-to-Advance-Foundation-Model-Innovation.html)（掲載: 2026-04-08）

#### 生成AI・プロダクト

- **Google が Gemini に「notebooks」— NotebookLM と同期するプロジェクト用ナレッジ基盤** — チャットやファイルをトピックごとに整理し、Gemini アプリと NotebookLM でソースを共有。Ultra / Pro / Plus の Web から順次展開、モバイル・欧州・無料層への拡大予告。18未満・Workspace / Education は対象外と明記。出典: [Google Keyword (blog)](https://blog.google/innovation-and-ai/products/gemini-app/notebooks-gemini-notebooklm/)（掲載: Apr 08, 2026）

#### セキュリティ・ブラウザ

- **Google Chrome、Extended Stable チャネル向けデスクトップ更新（2026-04-08）** — 企業向け長期サポート系チャネルの定期更新として Chrome Releases に掲載。修正内容・バージョン番号は同リリースノートおよびリリース後のセキュリティアドバイザリで確認。出典: [Chrome Releases](https://chromereleases.googleblog.com/2026/04/extended-stable-updates-for-desktop.html)（掲載: Wednesday, April 8, 2026）

### メモ（任意）

- **Microsoft セキュリティブログの SOHO ルーター侵害（Forest Blizzard）**は URL 上 **2026/04/07** のため、本 D では **D−2 相当**として新規トピックに含めず。必要なら [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/04/07/soho-router-compromise-leads-to-dns-hijacking-and-adversary-in-the-middle-attacks/) を参照。
- **Project Glasswing / Mythos** の二次報道のみ、**Apple Arcade（Nick Jr.）** などニュースルーム本文で**暦日がページ冒頭で取れない**ソースは、鮮度・重複の観点から本回は新規トピック見送り。

---

## 調査 2026-04-10 15:00 （JST）

**調査日 D＝2026-04-10。** `news-recency-policy.md` により、新規トピックの主出典は **JST で 2026-04-09 または 2026-04-10** に公開（記載）されたもの。**Mercor** は TechCrunch 記事で **April 9, 2026**（PDT）、**OpenAI 英国DC** は Reuters で **April 9 (Reuters)**、**生数科技** は Reuters で **April 10 (Reuters)**、**米財務省・FRBと銀行CEO** は Reuters 記事本文 **April 9 (Reuters)**（URL スラッグは 2026-04-10）で確認。

### 新規トピック

#### AI・データ・サプライチェーン

- **Mercor（評価額約100億ドル規模のAIデータ訓練）— 侵害後の顧客・パートナー動向が報じられる** — 3/31 の侵害公表後、ハッカー側が4TB規模の窃取を主張していること、オープンソース LiteLLM 経由の資格情報窃取が起点だったことの整理。Meta が契約を無期限停止（Wired 経由で報道）、委託者5名が個人情報流出を理由に提訴（Business Insider 経由）、OpenAI は影響調査中で当時は契約継続と報じられる、など。出典: [TechCrunch](https://techcrunch.com/2026/04/09/after-data-breach-10b-valued-startup-mercor-is-having-a-month/)（掲載: April 9, 2026）

#### AI・インフラ・政策

- **OpenAI が英国のメインデータセンター計画を一時停止** — 規制環境とエネルギーコストを理由に、条件が長期投資に適したものになるまで見送ると説明。Stargate UK（Nvidia・Nscale との協業）は継続検討とし、英国政府は OpenAI 等との連携を続ける旨をコメント。出典: [Reuters](https://www.reuters.com/business/openai-pauses-uk-data-centre-project-over-regulation-costs-2026-04-09/)（April 9, 2026）

#### AI・資金調達（中国）

- **生数科技（ShengShu）が約2億9300万ドル規模の資金調達** — アリババクラウドが主導し、「物理環境でのAGI」に向けた感覚情報を扱う「汎用世界モデル」開発に投じると発表。Vidu 動画生成やロボット向けオープンソース Motus などの文脈で競合関係を説明。出典: [Reuters](https://www.reuters.com/world/asia-pacific/chinese-startup-shengshu-raises-293-million-advance-artificial-general-2026-04-10/)（April 10, 2026）

#### AI・金融規制・サイバーリスク

- **米財務長官・FRB議長が銀行CEOらと会合 — Anthropic「Mythos」モデルのサイバーリスクを警告** — 関係者話として、火曜の財務省主催会合で主要行CEOにリスク認識と防御策を促したと報道。Mythos は広範リリースを抑え、政府・業界への事前説明を続けている旨が本文で整理。初報は Bloomberg。出典: [Reuters](https://www.reuters.com/business/finance/bessent-powell-warn-bank-ceos-about-anthropic-model-risks-bloomberg-news-reports-2026-04-10/)（April 9, 2026）

### メモ（任意）

- **Fortinet FortiClient EMS（CVE-2026-35616 等）** は既に `seen-urls.json` の [Fortinet PSIRT FG-IR-26-099](https://fortiguard.fortinet.com/psirt/FG-IR-26-099) で同一事件扱いのため、本回は URL 追加なし。
- **Anthropic Mythos の公開範囲**についての分析記事（例: TechCrunch 4/9）は、上記 Reuters と**同一テーマ**のため主出典は Reuters に集約。

---

## 調査 2026-04-10 22:00 （JST）

**調査日 D＝2026-04-10（追補）。** `news-recency-policy.md` により、新規トピックの主出典は **JST で 2026-04-09 または 2026-04-10** に公開（記載）されたもの。**OpenAI** の Axios 件は公式投稿 **April 10, 2026**、**Bloomberg** の Alibaba 動画モデルは **April 10, 2026**、**The Register** の Mozilla 批判は **Fri 10 Apr 2026**、**TechCrunch** 各稿は **April 10, 2026**（記事ヘッダの掲載日時）で確認。

### 新規トピック

#### セキュリティ・サプライチェーン

- **OpenAI、macOS アプリ署名に関わる第三者 Axios ライブラリ侵害への対応** — 2026年3月31日（UTC）の広範なサプライチェーン事案の一環として、GitHub Actions ワークフローが悪意ある Axios 1.14.1 を取得した可能性があると説明。ユーザー・IP・改ざんの証拠はない一方、証明書を失効・ローテーションし、2026年5月8日以降は旧版デスクトップアプリの更新・サポート終了や起動制限の恐れがあるとして、ChatGPT Desktop・Codex・Atlas などの最小バージョンを列挙。出典: [OpenAI](https://openai.com/index/axios-developer-tool-compromise/)（April 10, 2026）

#### 生成AI・動画

- **Alibaba が動画生成モデル「Happy Horse 1.0」を公表し、Artificial Analysis のテキスト・トゥ・ビデオ指標で首位と報道** — 開発元が同社傘下の Alibaba Token Hub 系事業で、ベータ段階とする説明。出典: [Bloomberg](https://www.bloomberg.com/news/articles/2026-04-10/stealth-alibaba-video-ai-model-tops-global-ranking-on-debut)（April 10, 2026）

#### プラットフォーム・UX・政策論点

- **Mozilla が Microsoft の Windows への Copilot 展開を批判** — Redmond が Copilot 機能の一部を縮小した動きを「遅すぎる見直し」とし、同意なしの導入や既定の押し付けがユーザーの選択を損ねたと主張。出典: [The Register](https://www.theregister.com/2026/04/10/mozilla_microsofts_copilot_strategy/)（Fri 10 Apr 2026）

#### 生成AI・エコシステム

- **Anthropic が OpenClaw 作者 Peter Steinberger の Claude アクセスを一時停止 — 数時間後に復旧** — 第三者ハーネス利用の課金変更（いわゆる消費ベースの「claw tax」文脈）直後、不審活動を理由に停止したが、投稿が拡散後にアカウント復帰。同社エンジニアが OpenClaw 利用自体を理由にした禁止はしていないとコメントした、と報道。出典: [TechCrunch](https://techcrunch.com/2026/04/10/anthropic-temporarily-banned-openclaws-creator-from-accessing-claude/)（April 10, 2026）

- **Meta が Muse Spark モデルとともに AI 戦略を刷新 — Meta AI アプリの利用が友人側に見える設計への注意喚起が話題** — アプリのダウンロード急増（App Store 順位の言及）と、Instagram 連携による「知られたくない利用」への懸念が記事の焦点。出典: [TechCrunch](https://techcrunch.com/2026/04/10/psa-if-you-use-the-meta-ai-app-your-friends-will-find-out-and-it-will-be-embarrassing/)（April 10, 2026）

#### 法務・ガバナンス

- **元交際相手が OpenAI を提訴 — ChatGPT がストーカー行為を助長したと主張** — 大量殺傷に関する警告が社内でフラグされたにもかかわらず十分に対応しなかった、などとする訴えが TechCrunch により報道。OpenAI の立法戦略（イリノイ法案など）との接続も言及。出典: [TechCrunch](https://techcrunch.com/2026/04/10/stalking-victim-sues-openai-claims-chatgpt-fueled-her-abusers-delusions-and-ignored-her-warnings/)（April 10, 2026）

### メモ（任意）

- **CBS など米メディアの Mythos／財務省会合**は、同日ログで主出典にした [Reuters](https://www.reuters.com/business/finance/bessent-powell-warn-bank-ceos-about-anthropic-model-risks-bloomberg-news-reports-2026-04-10/) と**同一テーマ**のため URL は追加せず。
- **米司法省の GRU・SOHO ルーター DNS 侵害網の妨害（Operation Masquerade）**は、[司法省プレスリリース](https://www.justice.gov/opa/pr/justice-department-conducts-court-authorized-disruption-dns-hijacking-network-controlled) の公表日が **2026-04-07** のため、本 D の **D−1（4/9）未満**として新規トピックには含めない。4/10 付けの解説記事は二次にあたる。

---

## 調査 2026-04-12 14:00 （JST）

**調査日 D＝2026-04-12。** `news-recency-policy.md` により、新規トピックの主出典は **JST 暦日で 2026-04-11 または 2026-04-12** に公開（記載）されたもの。**日本・Rapidus** は Reuters 記事で **April 11 (Reuters)**、**Sam Altman** は TechCrunch で **April 11, 2026**、**Operation Atlantic** は BleepingComputer で **April 11, 2026**、**Reddit／大陪審** は The Verge で **Apr 11, 2026**、**Artemis II** は Ars Technica で **2026-04-11**、**Generalist AI GEN-1** は Robotics & Automation News で **2026/04/11** と確認。

### 新規トピック

#### 半導体・産業政策

- **日本政府が Rapidus に追加で約 6320 億円（約 40 億ドル）の支援を承認** — 先端ロジック半導体の研究開発加速が目的。累計の政府系 R&D 支援は約 2.35 兆円規模に。NEDO が富士通・IBM 日本法人の設計関連プロジェクトも支援すると報道。Rapidus は 2nm 世代の量産を 2027 会計年度開始を目標とする説明。出典: [Reuters](https://www.reuters.com/world/asia-pacific/japan-approves-additional-4-bln-chipmaker-rapidus-2026-04-11/)

#### AI・企業・ガバナンス

- **OpenAI CEO が『New Yorker』の長文プロフィールと自宅への火炎瓶投擲疑惑を受けブログで応答** — 金曜早朝の事案で負傷者なし、容疑者は後に本社で逮捕されたとする SFPD の説明を引用する報道。記事は対立回避の傾向や 2023 年の取締役会騒動への言及などを要約。出典: [TechCrunch](https://techcrunch.com/2026/04/11/sam-altman-responds-to-incendiary-new-yorker-article-after-attack-on-his-home/)

- **Generalist AI がロボット向け「GEN-1」モデルを発表 — 特定タスクで高成功率を主張** — 身体性基盤モデルとして、実世界データでの事前学習や適応に関する説明。同社の主張として成功率・速度の改善を報じ、限界も認める旨が記事に記載。出典: [Robotics & Automation News](https://roboticsandautomationnews.com/2026/04/11/generalist-ai-unveils-gen-1-model-claiming-breakthrough-in-real-world-robotic-task-performance/100516/)

#### セキュリティ・法執行

- **英 NCA 主導の「Operation Atlantic」— 暗号資産「承認フィッシング」等で 2 万人超の被害者を特定** — 米シークレットサービス・カナダ当局などと連携した国際捜査。約 1200 万ドル相当の凍結・約 4500 万ドル相当の不正取得コインの追跡などが報道。出典: [BleepingComputer](https://www.bleepingcomputer.com/news/security/police-identifies-20-000-victims-in-international-crypto-fraud-crackdown/)

#### プラットフォーム・法政策

- **DHS／ICE が Reddit 利用者の身元開示を求め大陪審召喚状に至ったと報道** — カリフォルニアでの召喚取下げ後、DC の大陪審向けに当局が再び情報取得を試みたという流れを The Intercept 等を引用して整理。Reddit は声明で「政府批判や抗議を行う利用者」への任意開示はしない旨を伝えたと報道。出典: [The Verge](https://www.theverge.com/policy/910714/dhs-is-trying-to-force-reddit-to-expose-a-user-who-said-mean-things-about-ice)

#### 宇宙・エンジニアリング

- **NASA Artemis II が太平洋にスプラッシュダウン — 月周回有人飛行が約半世紀ぶりに完了** — Orion の再突入・減速・回収までを速報。有人深宇宙飛行の工程・リスクの文脈で報道。出典: [Ars Technica](https://arstechnica.com/space/2026/04/four-astronauts-are-back-home-after-a-daring-ride-around-the-moon/)

### メモ（任意）

- **OpenAI・第三者 Axios／macOS 署名**は、[OpenAI 公式投稿](https://openai.com/index/axios-developer-tool-compromise) および [Reuters 4/11](https://www.reuters.com/business/openai-identifies-security-issue-involving-third-party-tool-says-user-data-was-2026-04-11/) が同一事件のため、主出典は既出 URL に集約（本回 `seen-urls.json` には追加せず）。
- **Anthropic Project Glasswing／Mythos** のフォロー報道（NPR・CS Monitor 等、4/11）は [Anthropic Glasswing](https://www.anthropic.com/glasswing) と同一テーマのため URL 追加なし。
- **Gmail エンタープライズ向け E2EE のモバイル展開**（BleepingComputer 掲載 **2026-04-10**）は **D−1（4/11）未満**のため新規トピックから除外。

---

## 調査 2026-04-13 12:00 （JST）

**調査日 D＝2026-04-13。** `news-recency-policy.md` により、新規トピックの主出典は **JST で 2026-04-12 または 2026-04-13** に公開（記載）されたもの、または **公式ページの Last updated が該当暦日**のもの。**Adobe APSB26-43** は本文で **Date Published: April 11, 2026** だが **Last updated on Apr 12, 2026** かつ **Revisions: April 12, 2026**（CVSS 改訂）で確認。**Samsung Shallow-π** は Seoul Economic Daily 英語版 URL 上 **2026/04/12**。**X のクリエイター支払い**は TechCrunch ヘッダ **April 12, 2026** で確認。

### 新規トピック

#### セキュリティ・ソフトウェア

- **Adobe、Acrobat／Reader の緊急セキュリティ更新（APSB26-43）— CVE-2026-34621 を悪用中と公表** — プロトタイプ汚染経由の任意コード実行（Critical、CVSS 3.1 ベース 8.6）。4月12日付で攻撃ベクトル等の改訂あり。該当バージョンへの更新を推奨。出典: [Adobe Security Bulletin](https://helpx.adobe.com/security/products/acrobat/apsb26-43.html)（Date Published: April 11, 2026／Last updated: Apr 12, 2026）

#### ロボティクス・AI

- **Samsung Research が人形ロボ向け制御技術「Shallow-π」を発表したと報道** — 知識蒸留で推論ステップを約3分の1に圧縮、判断速度を 8Hz から 17.2Hz へ、オンデバイス VLA で Jetson 系上の検証や精密タスク成功率の言及など。製造現場向けの物理AI・2030年工場ロードマップの文脈。出典: [Seoul Economic Daily (English)](https://en.sedaily.com/finance/2026/04/12/samsung-secures-humanoid-robot-brain-tech-17-decisions-per)（掲載: 2026-04-12）

#### プラットフォーム・クリエイターエコノミー

- **X がクリックベイト・高速ニュースアグリゲーター等へのクリエイター支払いを削減** — プロダクト責任者が投稿で、集約アカウントのペイアウトを当サイクル 60% にし次サイクルでさらに 20% 減、常習的な「BREAKING」煽り投稿への減額も、と説明。タイムライン洪水が創作者を押しのけたとする主張。出典: [TechCrunch](https://techcrunch.com/2026/04/12/x-says-its-reducing-payments-to-clickbait-accounts/)（掲載: April 12, 2026）

### メモ（任意）

- **Reuters に掲載の Century Huatong「Digiloong Cup」プレスリリース**は **Sponsored content／EZ Newswire** で編集独立性が低いため、新規トピックには含めず。必要なら [Reuters（プレスリリース）](https://www.reuters.com/press-releases/century-huatong-2nd-digiloong-cup-ai-innovation-competition-2026-04-12/)（April 12, 2026 表記）を参照。

---

## 調査 2026-04-14 12:00 （JST）

**調査日 D＝2026-04-14。** `news-recency-policy.md` により、新規トピックの主出典は **JST で 2026-04-13 または 2026-04-14** に公開（記載）されたもの。以下はいずれも **2026-04-13（記事見出し・電文日付）** で確認。

### 新規トピック

#### セキュリティ

- **Anodot 侵害 — 複数顧客データ窃取と身代金要求が報道** — ビジネス監視 SaaS の Anodot でトークン等が流出し、Snowflake 上のデータストアへの不正アクセスにつながったとされる。ShinyHunters による脅迫・Rockstar Games など複数社が言及。出典: [TechCrunch](https://techcrunch.com/2026/04/13/hack-at-anodot-leaves-over-a-dozen-breached-companies-facing-extortion/)（Posted: April 13, 2026）

- **FBI、グローバル・フィッシング「W3LL」の摘発を公表 — インドネシア当局と連携** — 数千人超の被害、数百万ドル規模の詐取試行、マーケットプレイス閉鎖・容疑者拘束などと報道（TechCrunch は FBI 発表を引用）。出典: [TechCrunch](https://techcrunch.com/2026/04/13/fbi-announces-takedown-of-phishing-operation-that-targeted-thousands-of-victims/)（Posted: April 13, 2026）

#### プラットフォーム・子ども安全

- **Roblox、「Kids」「Select」アカウントを導入 — 年齢に応じたゲーム・チャット** — 5〜9歳は Kids、9〜15歳は Select、16歳以上は標準。チャット既定オフや親による通信相手指定など。6月初旬からの段階的展開。出典: [TechCrunch](https://techcrunch.com/2026/04/13/roblox-introduces-kids-and-select-accounts-for-age-appropriate-access-to-games-and-chat/)（April 13, 2026）

#### AI・政策

- **Anthropic、次世代モデル「Mythos」等についてトランプ政権側と協議していると共同創業者が表明** — ペンタゴンとのガードレール契約紛争はある一方、国家安全保障の文脈で政府との対話を続ける姿勢と報道。出典: [Reuters](https://www.reuters.com/world/anthropic-talking-trump-administration-about-its-next-ai-model-co-founder-says-2026-04-13/)（WASHINGTON, April 13, 2026）

#### モビリティ・規制

- **オランダ RDW、Tesla FSD の EU 域内型式承認を欧州委に申請する方針を通知** — 5月に技術委へ提示の見込み、米版より厳しいドライバー監視などとの言及。出典: [Reuters](https://www.reuters.com/business/dutch-regulator-notifies-european-commission-plan-seek-eu-approval-teslas-fsd-2026-04-13/)（April 13, 2026）

### メモ（任意）

- **Mythos** は [Anthropic Glasswing](https://www.anthropic.com/glasswing) 文脈の続報だが、本件は **政権・ペンタゴンとの協議** を主題とする **Reuters 単独 URL** のため新規トピックに掲載。

---

## 調査 2026-04-15 18:00 （JST）

**調査日 D＝2026-04-15。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-14 または 2026-04-15** に公開（記載）されたもの。以下の主出典は **2026-04-14** のページ日付で確認（**4/15 JST 掲載の別件**は本ブロックでは未採用）。

### 新規トピック

#### AI・セキュリティ

- **OpenAI、防御的サイバー向け「GPT-5.4-Cyber」を公表 — Mythos 公表を受けた文脈で限定提供** — 検証済みベンダ・研究者向けに段階展開し、Trusted Access for Cyber を拡大する方針などと報道。出典: [Reuters](https://www.reuters.com/technology/openai-unveils-gpt-54-cyber-week-after-rivals-announcement-ai-model-2026-04-14/)（April 14, 2026）

#### セキュリティ・サプライチェーン

- **WordPress プラグイン群にバックドア — 新オーナーが Essential Plugin 系を取得後、休眠から活性化** — 数万インストール規模、ディレクトリからの削除・利用者への確認呼びかけなど。出典: [TechCrunch](https://techcrunch.com/2026/04/14/someone-planted-backdoors-in-dozens-of-wordpress-plugins-used-in-thousands-of-websites/)（April 14, 2026）

#### クラウド・M&A

- **Amazon、衛星事業 Globalstar を約 115.7 億ドルで買収合意 — Apple との接続継続契約も** — Amazon Leo 強化、Globalstar の軌道・スペクトラム・地上設備の取得などと報道。出典: [TechCrunch](https://techcrunch.com/2026/04/14/amazon-to-buy-globalstar-for-11-57b-in-bid-to-flesh-out-its-satellite-biz/)（April 14, 2026）

#### プラットフォーム・生成 AI

- **Microsoft、MAI-Image-2-Efficient を Foundry／MAI Playground に提供開始** — 従来比で高速・低コストの画像生成を主張、業務利用向けと説明。出典: [The Verge](https://www.theverge.com/tech/911532/microsoft-mai-image-2-efficient-model-release)（Posted Apr 14, 2026）

#### 規制・インフラ

- **米メイン州議会、大型データセンター向けの一時停止（モラトリアム）を米国初として可決したと報道** — 電力・環境・地域コミュニティへの影響を審議する期間を設ける趣旨など。出典: [Reuters](https://www.reuters.com/sustainability/boards-policy-regulation/maine-legislature-approves-first-us-moratorium-big-data-centers-2026-04-14/)（April 14, 2026）

### メモ（任意）

- **note 続報（薄／同一事件）:** `note/20260414/2026-04-14-anthropic-mythos-pentagon-clark｜政権協議と調達訴訟の読み分け.md` について、[TechCrunch（4/14）](https://techcrunch.com/2026/04/14/anthropic-co-founder-confirms-the-company-briefed-the-trump-administration-on-mythos/) で Clark が政権への Mythos ブリーフィングを確認したとあるが、主筋は既ログの [Reuters（4/13）](https://www.reuters.com/world/anthropic-talking-trump-administration-about-its-next-ai-model-co-founder-says-2026-04-13/) と**同一事件**のため `### note底稿の続報` には載せず。Rapidus 底稿（04-13）の **4/14 以降の新主出典**は本回の検索では未確認。
- **Adobe Acrobat ゼロデイ**の [TechCrunch（4/14）](https://techcrunch.com/2026/04/14/adobe-fixes-pdf-zero-day-security-bug-that-hackers-have-exploited-for-months/) は、既ログの [Adobe APSB26-43](https://helpx.adobe.com/security/products/acrobat/apsb26-43.html)（CVE-2026-34621）と**同一事件**のため新規トピック外。
