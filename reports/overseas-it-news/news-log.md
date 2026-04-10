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
