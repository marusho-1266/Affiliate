# 海外・日本 ITニュース調査ログ（累積）

このファイルは `**/overseas-it-news**` の実行ごとに**追記**する。**調査範囲**は **海外（主に英語圏）に加え日本国内**の IT・テック（公開ウェブで確認できる官公庁・報道・企業発表など）。  
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

---

## 調査 2026-04-16 12:00 （JST）

**調査日 D＝2026-04-16。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-15 または 2026-04-16** に公開（記載）されたもの。**Google DeepMind 公式ブログ**の Gemini Robotics-ER 1.6 は **April 14, 2026（UTC）** 表記で **D−2** にあたるため、新規トピックの主出典は **米メディアの 4/15（米東部）掲載**（JST では 4/16 未明〜）を採用。**NVD** の CVE-2026-22676 は **NVD Published Date: 04/15/2026** で確認。

### 新規トピック

#### AI・ロボティクス

- **Google DeepMind、ロボット向け推論モデル「Gemini Robotics-ER 1.6」を発表 — 空間推論・計器読み取り・Boston Dynamics Spot 連携など** — 公式 DeepMind 投稿は **4/14（UTC）** のため本枠の主出典から外し、**4/15 米東部掲載**の技術メディアを採用（JST **4/16 未明**相当）。Gemini API／AI Studio 提供や計器読み取りの強化など。出典: [SiliconANGLE](https://siliconangle.com/2026/04/15/deepmind-launches-gemini-robotics-er-1-6-meet-precise-physical-ai-demands/)（Published: 2026-04-15T12:15:01-04:00）

#### AI・企業動向

- **OpenAI、収益化のため企業向けへ軸足 — 次世代モデル「Spud」を Anthropic Claude Mythos への対抗として位置づけ** — CFO インタビューで週次ユーザー約9億人のうち約95%が非課金としつつ、法人売上比率の拡大や Sora アプリ終了など消費者施策の縮小、Dresser CRO の Anthropic 批判メモ（The Verge 経由）への言及など。出典: [AP News](https://apnews.com/article/openai-chatgpt-spud-sam-altman-anthropic-mythos-3c2674f5cdf67ac6d88eedb207de117c)（ページ上の掲載タイムスタンプは UTC で **2026-04-16** 帯）

#### セキュリティ

- **nginx-ui の MCP 統合欠陥（CVE-2026-33032、CVSS 9.8）— `/mcp_message` の認証不備で設定改ざん・nginx 乗っ取りが可能と報道** — 3月からの悪用、Pluto Security の詳細公開、修正版への更新や MCP 無効化・IP 制限の回避策など。出典: [CSO Online](https://www.csoonline.com/article/4159248/critical-nginx-ui-tool-vulnerability-opens-web-servers-to-full-compromise.html)（Apr 15, 2026）

- **Barracuda RMM、ローカル権限昇格（CVE-2026-22676）— `C:\Windows\Automation` の ACL 過剰許可が原因** — 2025.2.2 未満が対象。NVD が **2026-04-15** にエントリ公開。出典: [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-22676)（NVD Published Date: 04/15/2026）

- **Microsoft Copilot Studio と Salesforce Agentforce にフォーム経由のプロンプトインジェクション — 「ShareLeak」「PipeLeak」** — Capsule Security の開示を引用し、CVE-2026-21520（MSRC）や設定依存の指摘など。出典: [CSO Online](https://www.csoonline.com/article/4159079/copilot-and-agentforce-fall-to-form-based-prompt-injection-tricks.html)（Apr 15, 2026）

#### ガバナンス・運用

- **Microsoft Security、AI システム向けインシデント対応の考え方を整理** — 非決定性・速度・観測可能性のギャップ、段階的修復、監視期間、応答者のウェルビーイングなど。出典: [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/04/15/incident-response-for-ai-same-fire-different-fuel/)（April 15, 2026）

#### 半導体・自動車

- **Tesla、次世代 AI チップ「AI5」のテープアウトを Musk が表明 — スケジュール遅延や Cybercab は AI4 のまま等** — 量産は中盤2027頃までかかる見込みなどの整理。出典: [Electrek](https://electrek.co/2026/04/15/tesla-ai5-chip-taped-out-musk-ai6-dojo3/)（April 15, 2026）

### note底稿の続報

- **OpenAI「Spud」／法人寄り戦略の報道が補助底稿の整理対象を拡張** — AP が CFO／CRO 談話とメモ報道を束ね、次世代モデル「Spud」と Mythos 対比を明文化。**底稿:** `note/20260415/2026-04-15-openai-gpt-5-4-cyber｜補助｜用語と読み順・報道と公式.md`。**続報出典:** [AP News](https://apnews.com/article/openai-chatgpt-spud-sam-altman-anthropic-mythos-3c2674f5cdf67ac6d88eedb207de117c)（UTC 掲載 2026-04-16 付近）

### メモ（任意）

- **Gemini Robotics-ER 1.6 の公式主出典**は [Google DeepMind Blog](https://deepmind.google/blog/gemini-robotics-er-1-6/)（**April 14, 2026**）および [Google Keyword](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/gemini-robotics-er-1-6/) であり、**D−2** のため `### 新規トピック` には入れず。パートナー文脈は [Boston Dynamics（AIVI-Learning 更新説明）](https://bostondynamics.com/blog/aivi-learning-now-powered-google-gemini-robotics/) を参照（本文に **04/08/2026** の運用記載あり）。
- **CISA KEV の SharePoint（CVE-2026-32201）**は [CISA リリース](https://www.cisa.gov/news-events/alerts/2026/04/14/cisa-adds-two-known-exploited-vulnerabilities-catalog) が **April 14, 2026** のため **D−1（4/15）未満**として本ブロックでは未採用。
- **note 続報（薄／同一事件）:** Rapidus・Mythos・Generalist GEN-1・Meta Muse 各底稿は、**4/15 JST 以降の新規主出典 URL**が取れず、または既ログ・既 `seen-urls.json` の同一事件に収束する見込みのため `### note底稿の続報` は上記 **1 件のみ**。

---

## 調査 2026-04-17 12:00 （JST）

**調査日 D＝2026-04-17。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-16 または 2026-04-17** に公開（ページ記載）されたもの。**Anthropic** の Opus 4.7 は **Apr 16, 2026**、**OpenAI** の Codex 更新は **April 16, 2026**、**TechCrunch** の Bluesky 記事は **Posted: April 16, 2026（PDT）** で確認。

### 新規トピック

#### AI・モデル

- **Anthropic、Claude Opus 4.7 を一般提供 — 高度ソフトウェア工学・視覚推論の強化、Mythos より能力は抑えた上でサイバー用途の自動検知ブロック、正当なセキュリティ用途向け「Cyber Verification Program」** — Glasswing／Mythos Preview の文脈で段階的な安全策検証の位置づけを説明。API 名 `claude-opus-4-7`、料金は Opus 4.6 と同水準。出典: [Anthropic](https://www.anthropic.com/news/claude-opus-4-7)（Apr 16, 2026）

#### AI・開発者ツール

- **OpenAI、Codex の大規模アップデート — バックグラウンドの computer use（macOS 先行）、アプリ内ブラウザ、gpt-image-1.5 連携、プラグイン追加、PR レビューコメント対応・複数ターミナル・SSH devbox、自動化のスレッド再利用・スケジュール実行、メモリのプレビュー等** — 週300万人超の開発者向けにワークフロー全体をカバーする方向と説明。出典: [OpenAI](https://openai.com/index/codex-for-almost-everything/)（April 16, 2026）

#### プラットフォーム・インフラ

- **分散SNS Bluesky がサービス障害 — COO が DoS 攻撃と帰属、米東部 4/16 未明から status ページで継続調査** — 公式フィードのレート制限やエラー表示など。出典: [TechCrunch](https://techcrunch.com/2026/04/16/its-not-just-you-bluesky-is-sorta-down/)（Posted April 16, 2026 PDT）

### note底稿の続報

- **Glasswing／Mythos 以降の「サイバー安全策の段階的検証」として Opus 4.7 を位置づけ、Cyber Verification Program を新設** — 公式が前週の Glasswing 公表と接続して説明。**底稿:** `note/20260408/2026-04-08-project-glasswing-note.md`。**続報出典:** [Anthropic](https://www.anthropic.com/news/claude-opus-4-7)（Apr 16, 2026）

- **法人・職場向けのプロダクト投下として Codex を拡張（computer use・ブラウザ・画像・メモリ等）** — Spud／法人比率のナラティブと並行して「開発者の職場OS」側の更新。**底稿:** `note/20260416/2026-04-16-openai-spud-enterprise-pivot｜OpenAI「Spud」と法人寄りシフト.md`。**続報出典:** [OpenAI](https://openai.com/index/codex-for-almost-everything/)（April 16, 2026）

### メモ（任意）

- **note 続報（薄／未採用）:** `note/20260415/2026-04-15-openai-gpt-5-4-cyber｜…` など TAC／GPT-5.4-Cyber 底稿に対し、**4/16 JST 以降の OpenAI 公式の「同トピックの追記」**は本回検索では未確認（Codex は別レーン）。`note/20260414` Mythos・政権協議稿は Opus 4.7 が **製品**中心のため **同一事件の続報にはせず**、上記 Glasswing 底稿に集約。
- **nginx-ui（CVE-2026-33032）**の追跡記事や **Marimo／NKAbuse** 系は、主出典ページの**鮮度が D−1 未満**、または取得不能のため本ブロックの新規トピック外。

---

## 調査 2026-04-18 12:00 （JST）

**調査日 D＝2026-04-18。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-17 または 2026-04-18** に公開（ページ記載）されたもの。**Anthropic** の Claude Design は **Apr 17, 2026**、**Reuters** の Cerebras IPO 電は **April 17, 2026**、**TechCrunch** の Sequoia 記事は **Published: 2026-04-17T02:55:06+00:00（UTC）** で確認。**OpenAI×Cerebras の追加支出報道**（Reuters 電 **April 16**）は **D−2** のため本ブロックの新規トピックには含めず（必要なら別週で SEC 提出書類と併読）。

### 新規トピック

#### 生成AI・プロダクト

- **Anthropic Labs が「Claude Design」を研究プレビュー公開 — プロトタイプ・スライド・ワンページ等のビジュアル制作を自然言語で支援、Opus 4.7 を搭載** — Pro／Max／Team／Enterprise 向けに段階展開、デザインシステムの自動適用や Claude Code への引き渡しなどを説明。出典: [Anthropic](https://www.anthropic.com/news/claude-design-anthropic-labs)（Apr 17, 2026）

#### 半導体・資本市場

- **AI チップ企業 Cerebras が米国 IPO の届出を再提出 — 2025 年は黒字転換、Nvidia 競合としてウエハースケール推論など** — OpenAI との大規模取引の文脈や上場見通しが Reuters で整理。出典: [Reuters](https://www.reuters.com/technology/nvidia-rival-cerebras-reveals-us-ipo-filing-ai-boom-drives-listings-2026-04-17/)（April 17, 2026）

#### ベンチャー・AI投資

- **Sequoia Capital が拡張戦略向けに約 70 億ドルの新ファンドを調達したと報道 — AI 後期投資のスケール拡大** — Bloomberg を根拠に TechCrunch が紹介、新共同リーダー体制下で初の大型調達など。出典: [TechCrunch](https://techcrunch.com/2026/04/16/new-leaders-new-fund-sequoia-has-raised-7b-to-expand-its-ai-bets/)（Published: 2026-04-17T02:55:06+00:00）

### note底稿の続報

- **Opus 4.7 公開の翌日に Anthropic Labs で「Claude Design」を研究プレビュー — モデルをビジュアル製品に接続** — 底稿で扱った Opus 4.7 とサイバー安全策の段階的検証に続く、別レーンのプロダクト投下。**底稿:** `note/20260417/2026-04-17-anthropic-claude-opus-4-7｜Opus-4.7とサイバー安全策の一段目.md`。**続報出典:** [Anthropic](https://www.anthropic.com/news/claude-design-anthropic-labs)（Apr 17, 2026）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/20######/` 配下（`note/Druft/` 除外）を走査。ラジオ台本は本編がある場合は本編のみを優先。
- **note 続報（薄／未採用）:** Rapidus・Mythos／政権協議・Meta Muse・Generalist GEN-1 各底稿は、**4/17 JST 以降の新規主出典**が取れず、または本ブロックの鮮度条件外。**OpenAI×Cerebras の詳細報道**は主出典が **4/16 電**のため `### note底稿の続報` には入れず（`note/20260402/OpenAI約1220億ドル調達…` への「compute パートナー」続報は **薄**扱いで別資料推奨）。
- **同一 CVE:** nginx-ui（CVE-2026-33032）の **4/17 追跡記事**は既ログの CSO Online 報道と**同一事件**のため新規トピック外。

---

## 調査 2026-04-20 14:00 （JST）

**調査日 D＝2026-04-20。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-19 または 2026-04-20** に公開（ページ記載の日付／Last updated）されたもの。**Vercel** のセキュリティ速報は KB の **Last updated April 20, 2026**、**Axios** の NSA／Mythos 記事は **Apr 19, 2026**、**The Verge** の Keychron レビューは **Apr 19, 2026, 12:00 PM UTC** で確認。

### 新規トピック

#### セキュリティ・サプライチェーン

- **Vercel が社内システムへの不正アクセスを公表 — 第三者 AI ツール（Context.ai）経由で従業員の Google Workspace が乗っ取られ、非「sensitive」環境変数などに到達した可能性** — Mandiant 等と調査継続、限定的な顧客への連絡と資格情報ローテ推奨、OAuth アプリの IOC 公開。出典: [Vercel Knowledge Base](https://vercel.com/kb/bulletin/vercel-april-2026-security-incident)（Last updated April 20, 2026）

#### AI・政策

- **NSA が Anthropic の Mythos にアクセスしていると報道 — Pentagon がサプライチェーンリスクと位置づけた企業のモデルへのアクセスとのギャップが焦点** — 約 40 組織が Glasswing 文脈でアクセスとし、NSA は主に自ネットワークの脆弱性特定に利用との説明。出典: [Axios](https://www.axios.com/2026/04/19/nsa-anthropic-mythos-pentagon)（Apr 19, 2026）

#### ハードウェア・周辺機器

- **Keychron の Q1／V5 Ultra 8K レビュー — ZMK ファームウェアと 8kHz 無線ポーリング、長時間バッテリーが売り** — 既存 Q／V シリーズからの実用上の改善点を整理。出典: [The Verge](https://www.theverge.com/tech/914085/keychron-q1-v5-ultra-8k-zmk-mechanical-keyboards-review)（Apr 19, 2026, 12:00 PM UTC）

### note底稿の続報

- **Mythos の政府・防衛側アクセスが「NSA まで含む」形で報じられ、Glasswing／政権協議の線と接続して読める** — Axios が複数ソースを引用。**底稿:** `note/20260414/2026-04-14-anthropic-mythos-pentagon-clark｜政権協議と調達訴訟の読み分け.md` / `note/20260410/2026-04-10-Mythos｜米財務省・FRBと大行CEO会合報道の読み分け.md`。**続報出典:** [Axios](https://www.axios.com/2026/04/19/nsa-anthropic-mythos-pentagon)（Apr 19, 2026）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/20######/`（`note/Druft/` 除外）を走査。ラジオ台本は本編がある場合は本編のみを参照。
- **同一事件:** Vercel 侵害の **The Verge 報道**（[The Verge](https://www.theverge.com/tech/914723/vercel-hacked)、Apr 19, 2026 7:54 PM UTC）は上記 **Vercel 公式 KB と同一事件**のため、主出典は KB に集約（`seen-urls.json` に The Verge URLは未追加）。
- **note 続報（薄／未採用）:** Claude Design 底稿（`note/20260419/…`）は **4/18 以降の Anthropic 公式の新規プレス**は未確認。Cerebras IPO・Sequoia ファンド・Codex 等の底稿は **4/19 JST 以降の新規主出典**が本ブロックの鮮度条件で未採用。Rapidus・Generalist GEN-1・Meta Muse も同様。

---

## 調査 2026-04-21 12:00 （JST）

**調査日 D＝2026-04-21。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-20 または 2026-04-21** に公開（ページ記載）されたもの。**Apple** のプレスは **PRESS RELEASE April 20, 2026**、**Reuters** の Bezos／Prometheus 電は本文 **April 20 (Reuters)**（URL スラグは `2026-04-21`）、**Ars Technica** の Mythos 記事は **Published: 2026-04-20**、**9to5Mac** の Codex Chronicle は **2026/04/20**、**GlobeNewswire** の Aikido は **April 20, 2026 07:00 ET** で確認。

### 新規トピック

#### 企業・経営

- **Apple が CEO 交代を発表 — Tim Cook が 2026年9月1日付でエグゼクティブ・チェアマンへ、ハードウェアエンジニアリング SVP の John Ternus が CEO に** — 取締役会全会一致、夏まで Cook が CEO を継続して移行を支援、Arthur Levinson はリード・インディペンデント・ディレクターへ、Johnny Srouji がチーフ・ハードウェア・オフィサーに、など。出典: [Apple Newsroom](https://www.apple.com/newsroom/2026/04/tim-cook-to-become-apple-executive-chairman-john-ternus-to-become-apple-ceo/)（April 20, 2026）

#### AI・資金調達

- **Jeff Bezos 率いる AI ラボ「Project Prometheus」が約100億ドル調達で企業価値約380億ドルに近づく見込み、と FT 報道を Reuters が要約 — JPMorgan・BlackRock などが投資候補、製造・自動車・宇宙船向けのエンジニアリング用途** — クロージングは未確定。出典: [Reuters](https://www.reuters.com/technology/jeff-bezos-ai-lab-nears-38-billion-valuation-funding-deal-ft-reports-2026-04-21/)（April 20 (Reuters)、FT 報道ベース）

#### AI・セキュリティ・ガバナンス

- **Anthropic の Mythos をめぐり、政府・金融当局や企業がサイバー防御の追いつかなさを懸念する論調が英語圏で拡散 — 実害型悪用やエージェント時代の非対称性などを整理** — FT などの引用を含む総括記事。出典: [Ars Technica](https://arstechnica.com/ai/2026/04/anthropics-mythos-ai-model-sparks-fears-of-turbocharged-hacking/)（Published 2026-04-20）

#### AI・開発者ツール

- **OpenAI が Codex for Mac に「Chronicle」を追加 — 画面コンテキストでメモリを補強し、作業の言い直しを減らす研究プレビュー（Pro 向け、EU/UK/CH は対象外等）** — 公式開発者ドキュメントと同日のメディア解説。出典: [9to5Mac](https://9to5mac.com/2026/04/20/codex-for-mac-gains-chronicle-for-enhancing-context-using-recent-screen-content/)（2026-04-20）

#### セキュリティ・サプライチェーン

- **Aikido Security が開発者端末向け「Aikido Endpoint」を発表 — npm／PyPI／IDE 拡張など横断でインストール前ブロック、オープンソースの Safe Chain をエンタープライズ展開** — OSS サプライチェーン被害の増大を背景に位置づけ。出典: [GlobeNewswire（Aikido Security）](https://www.globenewswire.com/news-release/2026/04/20/3276846/0/en/Aikido-Security-Launches-Endpoint-Protection-for-Developer-Devices-as-Software-Supply-Chain-Attacks-Hit-Unprecedented-Scale.html)（April 20, 2026 07:00 ET）

### note底稿の続報

- **Mythos の能力と当局・産業の反応が英語メディアで一段と可視化（金融当局会合・各国の警戒発言などの文脈）** — 底稿で整理した Glasswing／政権・防衛側アクセスの線に、国際的な「脅威認知」の報道が重なる。**底稿:** `note/202604/20260414/2026-04-14-anthropic-mythos-pentagon-clark｜政権協議と調達訴訟の読み分け.md` / `note/202604/20260420/2026-04-20-nsa-anthropic-mythos-pentagon-axios｜NSAとMythos──「指定」と報道のズレをどう読むか.md`。**続報出典:** [Ars Technica](https://arstechnica.com/ai/2026/04/anthropics-mythos-ai-model-sparks-fears-of-turbocharged-hacking/)（Published 2026-04-20）

- **Codex 大型更新の翌週、Mac 向けに Chronicle（画面文脈×メモリ）が追加** — 4/16 公式の「職場化」ナラティブに続くプロダクト追投下。**底稿:** `note/202604/20260417/2026-04-17-openai-codex-major-update｜Codexが「開発の職場」まで広がる更新.md`。**続報出典:** [9to5Mac](https://9to5mac.com/2026/04/20/codex-for-mac-gains-chronicle-for-enhancing-context-using-recent-screen-content/)（2026-04-20）

- **Cook から Ternus への CEO 交代が公式に確定 — ハードウェア主導の次世代が表舞台に** — Apple Silicon や製品ポートフォリオの文脈で読める経営交代。**底稿:** `note/202603/20260331/Apple_AI戦略ハードウェア転換_深堀り分析.md`。**続報出典:** [Apple Newsroom](https://www.apple.com/newsroom/2026/04/tim-cook-to-become-apple-executive-chairman-john-ternus-to-become-apple-ceo/)（April 20, 2026）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**`（`note/Druft/` 除外）を走査。ラジオ台本は本編がある場合は本編を優先。
- **note 続報（薄／未採用）:** Rapidus・Generalist GEN-1・Meta Muse・Claude Design 専用底稿などは、**4/20 JST 以降の新規主出典**が本ブロック条件で未採用、または同一事件の再整理のみ。
- **開発者向け Chronicle の公式ドキュメント**（[OpenAI Developers](https://developers.openai.com/codex/memories/chronicle)）はページ上に**単独の公開日が明記されにくい**ため、本ブロックの新規トピックは **9to5Mac（2026-04-20）** を主出典に集約。

---

## 調査 2026-04-22 12:00 （JST）

**調査日 D＝2026-04-22。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-21 または 2026-04-22** に公開（ページ記載）されたもの。**TechCrunch** の SpaceX／Cursor 記事は **April 21, 2026 3:58 PM PDT**、**Google** の Deep Research ブログは **Apr 21, 2026**、**OpenAI** の Codex ブログは **April 21, 2026**、**OpenAI API Changelog** の **Apr 21** エントリ（GPT Image 2）を本文で確認。

### 新規トピック

#### 宇宙企業×開発者ツール・大型提携

- **SpaceX が Cursor と提携し、年内に Cursor を最大約600億ドルで買い取る「オプション」か、共同開発の対価として最大約100億ドルを払う選択肢を公表 — Colossus スパコンと「コーディング・ナレッジ労働向け次世代AI」を掲げる** — 報道は同時期の大規模資金調達目標や IPO 前の企業価値の扱いにも言及。出典: [TechCrunch](https://techcrunch.com/2026/04/21/spacex-is-working-with-cursor-and-has-an-option-to-buy-the-startup-for-60-billion/)（April 21, 2026）

#### 生成AI・API

- **Google が Gemini 3.1 Pro 基盤の「Deep Research」と「Deep Research Max」を双方向展開 — 速度重視版と、テスト時計算で網羅性を上げる Max、MCP 連携・可視化・Gemini API 有料層** — 12月プレビューからの段階的置き換えを説明。出典: [Google（The Keyword / blog.google）](https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/)（Apr 21, 2026）

- **OpenAI API に画像生成・編集モデル「GPT Image 2」をリリース — 柔らかな解像度指定、高忠実度の画像入力、トークン課金、Batch API 50% 割引など** — 開発者向け Changelog の **Apr 21** エントリに掲載。出典: [OpenAI（API / Changelog）](https://developers.openai.com/changelog)（Apr 21, 2026）

### note底稿の続報

- **法人向け「Codex Labs」開始と GSI パートナー列挙 — 週次WAU4百万超の文脈で底稿の「職場化」以降の一段目** — 直近 4/16 公式の大型 Codex 更新に続く、導入支援とスケールの公式的な枠づけ。**底稿:** `note/202604/20260417/2026-04-17-openai-codex-major-update｜Codexが「開発の職場」まで広がる更新.md`。**続報出典:** [OpenAI](https://openai.com/index/scaling-codex-to-enterprises-worldwide/)（April 21, 2026）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**` 底稿（`note/Druft/` 除外）を走査。`note/202604/20260422/` には**リポジトリ上では底稿ファイルなし**（ローカルに未コミットの `…spacex-cursor…` がある場合は、本ブロックの SpaceX／Cursor 主出典と**同一URL枠**で扱うのが自然）。
- **note 続報（薄／未採用）:** Cerebras IPO・Rapidus・Mythos 専用底稿・Spud 等は **4/21 JST 以降の新規主出典**が本回の鮮度で追加採用せず、または前回ログ（4/21 調査）の Apple／Mythos／Codex Chronicle と**同一事件の再整理**中心。
- **旧「The new ChatGPT Images」**（[OpenAI 同一URL](https://openai.com/index/new-chatgpt-images-is-here/)、ページ日付 **December 16, 2025**）は **4/22 の「最新」枠**とは掛け合わない（本ブロックの画像トピックは **API Changelog 上の GPT Image 2／Apr 21**に限定）。

---

## 調査 2026-04-23 12:00 （JST）

**調査日 D＝2026-04-23。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-22 または 2026-04-23** に公開（ページ記載または HTML メタ `publishedDate`）されたもの。**OpenAI** の workspace agents／WebSocket 記事は **April 22, 2026**、**TechCrunch** の Chrome 企業向け記事は **April 22, 2026 10:30 AM PDT**、**Microsoft Security Blog** はメタ **20260422**、**The Verge** の CISA 記事は **Apr 22, 2026, 4:57 PM UTC** を確認。

### 新規トピック

#### AI・業務自動化

- **OpenAI が ChatGPT に「workspace agents」を導入 — GPTs の進化形として、Codex 基盤でクラウド上の共有エージェントが複雑・長時間ワークフローを実行、Business／Enterprise／Edu／Teachers でリサーチプレビュー（2026年5月6日までは無料など価格方針も明記）** — 出典: [OpenAI](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)（April 22, 2026）

- **OpenAI が Responses API に WebSocket モードを投入 — エージェントループの往復を削減し、エンドツーエンドで最大約 40% の高速化などと説明、Codex 本番トラフィックの大半が WebSocket に移行した例を紹介** — 出典: [OpenAI](https://openai.com/index/speeding-up-agentic-workflows-with-websockets/)（April 22, 2026）

#### エンタープライズ・ブラウザ

- **Google が Chrome を職場向け「AI コワーカー」として強化 — Google Cloud Next の文脈で、企業ユーザー向けにタブ文脈を踏まえた「auto browse」エージェント機能やヒトインザループ、Workspace 米国向け展開、Chrome Enterprise Premium でのシャドウ AI／異常なエージェント活動の検知拡張などを報道** — 出典: [TechCrunch](https://techcrunch.com/2026/04/22/google-turns-chrome-into-an-ai-coworker-for-the-workplace/)（April 22, 2026）

#### AI・セキュリティ・政策

- **Microsoft が公式ブログで「AI が加速する脅威環境」への防御を論じ、Anthropic の Mythos Preview を Project Glasswing 経由で脆弱性発見・防御応答に活用する取り組みなどを説明** — 出典: [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/04/22/ai-powered-defense-for-an-ai-accelerated-threat-landscape/)（April 22, 2026／ページメタ `publishedDate: 20260422`）

- **Anthropic Mythos Preview を連邦政府が試用する一方、CISA はアクセスしていない可能性があると Axios 報道を引用して整理 — NSA・商務省などとの対比で政策論点を可視化** — 出典: [The Verge](https://www.theverge.com/policy/916758/anthropic-mythos-preview-cisa-left-out)（Apr 22, 2026, 4:57 PM UTC）

### note底稿の続報

- **Mythos の政府関係で「CISA は Preview に入れていない可能性」という新しい報道軸 — NSA 等の線と並べて読む材料** — **底稿:** `note/202604/20260414/2026-04-14-anthropic-mythos-pentagon-clark｜政権協議と調達訴訟の読み分け.md` / `note/202604/20260420/2026-04-20-nsa-anthropic-mythos-pentagon-axios｜NSAとMythos──「指定」と報道のズレをどう読むか.md`。**続報出典:** [The Verge](https://www.theverge.com/policy/916758/anthropic-mythos-preview-cisa-left-out)（Apr 22, 2026, 4:57 PM UTC）

- **4/16 前後の Codex「職場化」に続き、ChatGPT 側で Codex 駆動の workspace agents がリサーチプレビュー開始 — 底稿の「開発から組織運用へ」の流れの直後のプロダクト動き** — **底稿:** `note/202604/20260417/2026-04-17-openai-codex-major-update｜Codexが「開発の職場」まで広がる更新.md`。**続報出典:** [OpenAI](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)（April 22, 2026）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**` 底稿（`note/Druft/` 除外）。ラジオ台本は本編がある場合は本編を優先。
- **note 続報（薄）:** `note/202604/20260422/` の SpaceX×Cursor 底稿は、**4/21 掲載の TechCrunch 主出典と同一事件の別稿再掲**が中心のため、本ブロックの `### note底稿の続報` には載せず。
- **ASP.NET Core Data Protection（CVE-2026-40372）の OOB 修正**は公式系の公開日が **2026-04-21** 寄りに読めるため、**D＝4/23 の「新規トピック」枠（D−1 以降）には入れない**（必要なら別実行で 4/21 調査ブロックに集約済みか確認）。

---

## 調査 2026-04-24 12:00 （JST）

**調査日 D＝2026-04-24。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-23 または 2026-04-24** に公開（ページ記載）されたもの。**OpenAI** の GPT-5.5 紹介は **April 23, 2026**、**CNBC** の DeepSeek 記事は **2026/04/24** スラグ、**CNN Business** の Meta 人員再編は **PUBLISHED Apr 23, 2026, 3:58 PM ET** を本文で確認。**CVE-2026-40050**（CrowdStrike LogScale）は NVD の初回公開が **2026-04-21** のため、本ブロックの鮮度条件（D−1 以降）に合わず新規枠は見送り。

### 新規トピック

#### 生成AI・モデル

- **OpenAI が GPT-5.5 を公開 — ChatGPT／API／Codex 向けの「最も賢く直感的」モデル群として位置づけ、スーパーアプリ方向の一段とする説明。Plus／Pro／Enterprise 等へ展開** — 出典: [OpenAI](https://openai.com/index/introducing-gpt-5-5/)（April 23, 2026）

#### 中国系AI・オープンソース

- **DeepSeek が V4 系のプレビュー（V4-Pro／V4-Flash 等）を公表、オープンソースで米欧フロンティアと競合を宣言 — 1 年ぶりの大型アップデート文脈で CNBC が報道** — 出典: [CNBC](https://www.cnbc.com/2026/04/24/deepseek-v4-llm-preview-open-source-ai-competition-china.html)（2026/04/24）

#### 企業・人員

- **Meta が全社の約 10%（おおむそ 8,000 人）のレイオフ、約 6,000 の未充足ポジション取り下げ、AI 向け投資との両立を効率化の理由として従業員向けメモを確認したと報道 — 5 月 20 日付き等** — 出典: [CNN Business](https://www.cnn.com/2026/04/23/tech/meta-layoffs-10-percent-staff-ai)（Apr 23, 2026, 3:58 PM ET）

### note底稿の続報

- **ChatGPT 側の workspace agents や Responses API WebSocket 公開（4/22）の直後、GPT-5.5 が追加ローンチ — OpenAI スタックの公式的な重ね掛け** — **底稿:** `note/202604/20260423/2026-04-23-openai-workspace-agents-chatgpt｜カスタムGPTの次にくる「チームで育てる」共有エージェント.md` / `note/202604/20260424/2026-04-24-openai-responses-api-websockets｜Responses APIがつなぎっぱなしになった話.md` / `note/202604/20260417/2026-04-17-openai-codex-major-update｜Codexが「開発の職場」まで広がる更新.md` / `note/202604/20260415/2026-04-15-openai-gpt-5-4-cyber｜TACとGPT-5.4-Cyberのレイヤ読み分け.md`。**続報出典:** [OpenAI](https://openai.com/index/introducing-gpt-5-5/)（April 23, 2026）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**` 底稿（`note/Druft/` 除外）。ラジオ台本は本編がある場合は本編を優先。
- **鮮度で未採用:** **CrowdStrike LogScale / CVE-2026-40050** は NVD 初回 **2026-04-21** のため、**D＝4/24** の新規枠（D−1＝4/23 以降）に合わない。ベンダ勧告の本文に **4/23 以降の追記日**が明記されれば、別実行で再採用可能。
- **note 続報（薄）:** 他底稿（Mythos・Rapidus・Cerebras・SpaceX/Cursor 等）は **4/23 JST 以降の新規主出典**が本回条件と**別事件**で揃うまで保留、または前回までと同一の整理のみ。

---

## 調査 2026-04-25 12:00 （JST）

**調査日 D＝2026-04-25。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-24 または 2026-04-25** に公開（ページ記載）されたもの。**TechCrunch** の Google×Anthropic 記事は **April 24, 2026 11:00 AM PDT**（JST では 4/25 早朝）、**CNN Business** の Microsoft 記事は **PUBLISHED Apr 24, 2026, 1:20 PM ET**、**SiliconANGLE** の AWS×Meta 記事は **UPDATED 19:12 EDT / APRIL 24 2026** を確認。Bloomberg 経由の数値・条件は TechCrunch 本文内の要約に依存するため、主出典は同 TechCrunch とした。

### 新規トピック

#### 生成AI・資本・インフラ

- **Google（Alphabet）が Anthropic に最大約400億ドル規模の投資・コンピュート供与を計画 — 即時100億ドル・評価額3500億ドル、条件達成で追加300億ドル、Google Cloud から5年で5ギガワット級の容量拡張などと報道** — 出典: [TechCrunch](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)（April 24, 2026 11:00 AM PDT）

#### クラウド・半導体・AIインフラ

- **AWS と Meta が複数年・数十億ドル規模のインフラ契約 — Meta が数千万規模の Graviton コア利用権を取得し、エージェント型 AI の CPU 集約ワークロード向けと説明、追加オプションあり** — 出典: [SiliconANGLE](https://siliconangle.com/2026/04/24/aws-inks-multibillion-dollar-ai-infrastructure-deal-meta/)（UPDATED APRIL 24 2026 19:12 EDT）

#### 企業・人員

- **Microsoft が米国従業員向けに初の任意退職プログラム — 対象は米国のおおむね7%（年齢＋勤続年数が70以上など条件）、シニアディレクター以下、5月7日に詳細通知などと報道** — 出典: [CNN Business](https://www.cnn.com/2026/04/24/tech/microsoft-voluntary-buyouts-us-employees)（PUBLISHED Apr 24, 2026, 1:20 PM ET）

### note底稿の続報

- **NEC 協業公表（4/23–24）の直後に、Google 側の大型投資・クラウド容量の枠組みが報道され、Anthropic の資本・計算資源の地図が一段更新 — 「日本拠点初パートナー」読みとセットでインフラ多角化を追う材料** — **底稿:** `note/202604/20260424/2026-04-24-nec-anthropic-enterprise-ai｜NECがAnthropicの「日本拠点初のグローバルパートナー」になった話.md` / `note/202604/20260414/2026-04-14-anthropic-mythos-pentagon-clark｜政権協議と調達訴訟の読み分け.md` / `note/202604/20260420/2026-04-20-nsa-anthropic-mythos-pentagon-axios｜NSAとMythos──「指定」と報道のズレをどう読むか.md`。**続報出典:** [TechCrunch](https://techcrunch.com/2026/04/24/google-to-invest-up-to-40b-in-anthropic-in-cash-and-compute/)（April 24, 2026 11:00 AM PDT）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**` 底稿（`note/Druft/` 除外）。ラジオ台本は本編がある場合は本編を優先。
- **note 続報（薄）:** Workspace agents／WebSocket／GPT-5.5 底稿は **4/24 調査ブロックで同一主出典（OpenAI）済み**のため本回は追加せず。Cerebras・Rapidus・SpaceX/Cursor 等は **本回の新規主出典と別事件**で未採用または前回までの整理のみ。
- **鮮度で未採用:** **OpenAI Privacy Filter**（公式 **April 22, 2026**）は **D＝4/25** の D−1 基準（4/24 以降）に合わない。

---

## 調査 2026-04-26 12:00 （JST）

**調査日 D＝2026-04-26。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-25 または 2026-04-26** に公開（ページ記載）されたもの。**Reuters** の DeepRoute 記事は **BEIJING, April 25 (Reuters)**、OpenAI 謝罪は **April 25 (Reuters)**、**The Verge** の NSB 記事は **Apr 25, 2026, 7:20 PM UTC**（JST では 4/26 早朝）、**Economic Times** のインド財務相コメントは **Last Updated: Apr 26, 2026, 04:37:43 PM IST** を確認。

### 新規トピック

#### 自動運転・モビリティ

- **中国の DeepRoute.ai が北京モーターショー横の会見で、補助運転システム搭載車が30万台超、年内にさらに約100万台へ拡大する見通しなどと説明 — Reuters が通信社記事として報道** — 出典: [Reuters](https://www.reuters.com/world/asia-pacific/chinas-deeprouteai-says-over-300000-vehicles-use-its-advanced-driving-system-2026-04-25/)（April 25, 2026）

#### AI・ガバナンス・安全

- **OpenAI の Sam Altman が、BC 州 Tumbler Ridge の学校銃撃事件に関し、容疑者に紐づく ChatGPT アカウントを停止していたが当局に通報しなかったことについて道義的責任を認め、首脳会談姿勢や再発防止の協力に言及 — Reuters が通信社記事として報道** — 出典: [Reuters](https://www.reuters.com/sustainability/society-equity/openai-chief-apologizes-not-reporting-shooting-suspect-police-2026-04-25/)（April 25, 2026）

#### 科学政策・研究投資

- **トランプ政権が National Science Board（国家科学審議会）の委員の解任に踏み切ったと、複数報道を The Verge が整理 — NSF 資金・政策勧告枠の政治化懸念が焦点** — 出典: [The Verge](https://www.theverge.com/science/918769/trump-fires-the-entire-national-science-board)（Apr 25, 2026, 7:20 PM UTC）

### note底稿の続報

- **Mythos を「戦争に匹敵する」規模のサイバー脅威と位置づけ、インド政府が Anthropic・米当局とエンゲージを強化し、銀行・Nasscom 等の文脈で対応を説明 — 同国の上級閣僚発言を英語圏向け要約** — **底稿:** `note/202604/20260410/2026-04-10-Mythos｜米財務省・FRBと大行CEO会合報道の読み分け.md` / `note/202604/20260414/2026-04-14-anthropic-mythos-pentagon-clark｜政権協議と調達訴訟の読み分け.md` / `note/202604/20260420/2026-04-20-nsa-anthropic-mythos-pentagon-axios｜NSAとMythos──「指定」と報道のズレをどう読むか.md`。**続報出典:** [The Economic Times](https://economictimes.indiatimes.com/tech/artificial-intelligence/threat-from-anthropics-mythos-as-big-as-war-nirmala-sitharaman/articleshow/130530530.cms)（Last updated Apr 26, 2026, 4:37 PM IST）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**` 底稿（`note/Druft/` 除外）。ラジオ台本は本編がある場合は本編を優先。
- **同一事件:** Tumbler Ridge 関連は **The Verge（Apr 25 付の Altman 記事）** も存在するが、**Reuters 通信社**を主出典に集約（`seen-urls.json` には Verge の同事件 URL は未追加）。
- **note 続報（薄）:** `note/202604/20260426/2026-04-26-aws-meta-graviton-infrastructure-deal…md` など **Meta×AWS / Graviton** は、**4/25 調査ブロックの SiliconANGLE 主出典と同一事件**のため、本回の新規枠は追加せず。Workspace agents／Google×Anthropic 投資 等も前回までで同一主出典済み。

---

## 調査 2026-04-27 12:00 （JST）

**調査日 D＝2026-04-27。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-26 または 2026-04-27** に公開（ページ記載）されたもの。**TechCrunch** の Project Deal は **Published: 2026-04-25T21:43:37+00:00**（JST **4/26 早朝**）、Cohere×Aleph Alpha 解説は **Published: 2026-04-25T16:00:00+00:00**（JST **4/26 1:00**）を確認。**国内（日本）:** プレスリース・時事通信の **会社発表（シンカ「カイクラ AIナレッジ」）**は **掲載日 2026-04-22**、**提供開始予定は 2026-04-27** だが、鮮度ルールは**記事／PRの公開日**基準のため本ブロックの新規枠には入れず、メモに整理。

### 新規トピック

#### 生成AI・エンタープライズ

- **Anthropic が社内実験「Project Deal」を公表 — 従業員のエージェント同士が実物取引を交渉する分類広告型マーケットのパイロット、186 件・計 4,000 ドル超の取引、モデル格差と交渉結果の知覚ギャップなどを報告 — TechCrunch が詳報** — 出典: [TechCrunch](https://techcrunch.com/2026/04/25/anthropic-created-a-test-marketplace-for-agent-on-agent-commerce/)（Published 2026-04-25T21:43:37+00:00；JST では 4/26）

- **Cohere とドイツの Aleph Alpha が合併し「欧米横断」の企業・政府向けソブリン AI を掲げる構想 — 企業価値・Schwarz Group 系列の資本・当局・株主承認待ちなどを整理した解説記事** — 出典: [TechCrunch](https://techcrunch.com/2026/04/25/why-cohere-is-merging-with-aleph-alpha/)（Published 2026-04-25T16:00:00+00:00；JST では 4/26）

### メモ（任意）

- **国内IT（日本）調査:** **株式会社シンカ**の「カイクラ AIナレッジ」（社内ドキュメント限定 RAG 型チャット）— [PR TIMES](https://prtimes.jp/main/html/rd/p/000000277.000016795.html)・[時事ドットコム転載](https://www.jiji.com/jc/article?g=prt&k=000000277.000016795)の**ページ日付は 2026-04-22**、**サービス提供開始は 2026-04-27 予定**。本コマンドの **D−1＝4/26 以降の主出典**ルールに合わせ、**新規トピックには未採用**（**4/27 以降に日付の更新版公式ページや報道**が出た再実行で再検討可）。
- **官公庁・大手メディア（国内）:** **経済産業省**の [4/24 中小企業白書 閣議決定](https://www.meti.go.jp/press/2026/04/20260424005/20260424005.html) 等は **4/24 公開**のため、**D＝4/27** の新規枠（D−1＝4/26 以降）外。**デジタル庁**単独の **4/26–27 新規**の人工知能プレスは、本回の公開ウェブ検索では**主出典採用可能な1本に限定できず**。
- **note 続報:** 直近 8 週間の `note/**`（`note/Druft/` 除外）をざっと走査。Project Deal・Cohere 合併は **NEC×Anthropic 底稿**と接続可能だが、**新規主出典が `seen-urls.json` 済みの同一週の Anthropic 投資枠**と重なる論点もあり、**本ブロックでは `### note底稿の続報` を立てず**（**無**扱い）。

---

## 調査 2026-04-28 12:00 （JST）

**調査日 D＝2026-04-28。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-27 または 2026-04-28** に公開（ページ記載）されたもの。**Business Insider** の OpenAI 原則解説は **2026-04-27T04:13:16.706Z**、**Reuters** の北京モーターショー寄稿は **HONG KONG, April 27 (Reuters Breakingviews)**、**Denso／Rohm** は **TOKYO, April 27 (Reuters)**、**Techmeme** の Windows K2 リードは **April 27, 2026, 4:05 AM**（同サイトの米東部時刻表記）を確認。**OpenAI** 公式「Our principles」はページ上 **April 26, 2026**（タイムゾーン不明のため保守的扱い）で、本ブロックの新規枠では **4/27 付の解説記事**を主出典にした。**WIRED／Ars Technica** 経由の Palantir 内部議論記事は `article:published_time` **2026-04-25T10:49:52+00:00**（JST **4/25**）のため **D−1 基準外**。

### 新規トピック

#### AI・ガバナンス・競争

- **OpenAI がサム・アルトマン名義で運営原則を大幅更新 — 2018 年チャーターとの差分として、AGI への言及減少、他社に譲歩する競争観からの転換、自律的コミット表現の弱まりなどが論点化 — Business Insider が公式投稿（日曜）を踏まえ解説** — 出典: [Business Insider](https://www.businessinsider.com/openai-updated-principles-three-key-changes-competition-agi-anthropic-2026-4)（2026-04-27T04:13:16.706Z）

#### モビリティ・スマートカー

- **北京モーターショー前後で、華為の運転支援・車載 AI エージェント、CATL・地平線などサプライヤーが主役化 — 欧州メーカーの現地パートナーシップや投資規模の話題を Breakingviews が整理** — 出典: [Reuters](https://www.reuters.com/commentary/breakingviews/tech-steals-stage-beijing-auto-show-2026-04-27/)（April 27, 2026）

#### 半導体・産業

- **デンソーが Rohm への買収提案で合意に至らず撤退も検討と表明 — EV・データセンター向けパワー半導体を巡る統合構想の行方** — 出典: [Reuters](https://www.reuters.com/world/asia-pacific/denso-says-considers-ending-rohm-pursuit-acquisition-talks-stall-2026-04-27/)（April 27, 2026）

#### OS・プラットフォーム

- **Microsoft の「Windows K2」構想が報道 — Windows 11 の AI 過多・肥大化・性能・信頼性への不満への対応として 2026〜2027 年にかけ進める継続的イニシアティブと説明、単体 OS リリースではないとされる — Techmeme が Windows Central（Zac Bowden）を起点に要約** — 出典: [Techmeme](https://www.techmeme.com/260427/p8)（April 27, 2026, 4:05 AM ET 表記）

### note底稿の続報

- **OpenAI が運営原則を 2018 年以来の大きな改定に踏み込み、競争・繁栄・レジリエンス等の言い回しが「法人としての立ち位置」とセットで読み替え対象に — 調達・法人寄り製品の底稿と接続** — **底稿:** `note/202604/20260402/OpenAI約1220億ドル調達を公式ベースで整理｜computeとパートナーが主役.md` / `note/202604/20260416/2026-04-16-openai-spud-enterprise-pivot｜OpenAI「Spud」と法人寄りシフト.md`。**続報出典:** [Business Insider](https://www.businessinsider.com/openai-updated-principles-three-key-changes-competition-agi-anthropic-2026-4)（2026-04-27T04:13:16.706Z）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**` 底稿（`note/Druft/` 除外）。ラジオ台本は本編がある場合は本編を優先。
- **note 続報（薄／無）:** `note/202604/20260425/2026-04-25-google-anthropic-up-to-40b-investment…`（本編）、`note/202604/20260426/2026-04-26-aws-meta-graviton…`、Anthropic／Mythos 系は **いずれも 4/27 以降の新規主出典が同一事件・`seen-urls.json` 済みまたは鮮度外**で、本ブロックでは `### note底稿の続報` を OpenAI 原則以外には立てず。
- **参考（新規枠外）:** OpenAI 公式 [Our principles](https://openai.com/index/our-principles)（**April 26, 2026** 表記）。Palantir 内部議論（WIRED 原稿の Ars 再掲）は **4/25 UTC 公開**のため本調査の D−1 基準外。

---

## 調査 2026-04-28 18:00 （JST）

**調査日 D＝2026-04-28（継続）。** 同日 **12:00 JST** ブロックで採用済みの主出典と **URL 単位で重複しない**範囲で追加。**Reuters** の Cadence は **April 27 (Reuters)**、**NVD** の CVE-2026-41635 は **NVD Published Date: 04/27/2026**、**SecurityWeek** の OpenSSH は **Published: 2026-04-27T12:29:18+00:00**（JST では同日夜）、**SecurityAffairs** の Itron は **April 27, 2026** を確認。

### 新規トピック

#### EDA・半導体設計

- **Cadence Design Systems が通期売上見通しを引き上げ — AI 向けプロセッサ設計需要が EDA・検証需要をけん引する見通しとして、2026 会計年度売上を約 61.3〜62.3 億ドルレンジに上方修正（従来約 59〜60 億ドル）などと報道、Hexagon 系買収の影響で調整後 EPS 見通しはやや下方なども整理** — 出典: [Reuters](https://www.reuters.com/business/cadence-lifts-annual-revenue-forecast-sustained-ai-chip-design-boom-2026-04-27/)（April 27, 2026）

#### セキュリティ・インフラ

- **Apache MINA に IoBuffer.getObject() 経由の非信頼データ逆シリアル化（CWE-502）で任意コード実行の恐れ（CVE-2026-41635、CVSS 9.8）— 修正版は 2.0.28 / 2.1.11 / 2.2.6 など — NVD が同日登録** — 出典: [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-41635)（NVD Published Date: 04/27/2026）

- **OpenSSH が認証局の証明書プリンシパルにカンマが含まれる場合のパース不整合により root 相当認証に至りうる脆弱性（CVE-2026-35414、CVSS 8.1）— OpenSSH 10.3 で修正済みとの整理 — Cyera の調査が報道で紹介** — 出典: [SecurityWeek](https://www.securityweek.com/openssh-flaw-allowing-full-root-shell-access-lurked-for-15-years/)（Published: 2026-04-27T12:29:18+00:00）

- **米スマートメーター・ユーティリティ向け機器大手 Itron が、社内 IT の一部への不正アクセス検知（2026-04-13）と対応・当局通知を開示 — 顧客ホスト側への不正は確認されていない旨を SEC 8-K 経由で報道** — 出典: [Security Affairs](https://securityaffairs.com/191360/data-breach/u-s-utility-giant-itron-discloses-a-security-breach.html)（April 27, 2026）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**` 底稿（`note/Druft/` 除外）。ラジオ台本は本編がある場合は本編を優先。
- **note 続報:** Windows K2・Anthropic Project Deal 等は **同日 12:00 ブロックで既に主出典登録済みまたは論点が重複**のため、本追加ブロックでは **`### note底稿の続報` は立てず**。

---

## 調査 2026-04-28 21:30 （JST）

**調査日 D＝2026-04-28。** `news-recency-policy.md` により、新規トピックおよび `### note底稿の続報` の主出典は **JST で 2026-04-27 または 2026-04-28** に公開（ページ記載）されたもの。**OpenAI** の Microsoft 提携見直し投稿は **April 27, 2026**。**TechCrunch** の Ineffable／Meta は **April 27, 2026（PDT／UTC 表記）** を確認。**SecurityWeek** の CVE-2026-32202 解説は **Published: 2026-04-27T13:09:27+00:00**（JST では同日夜）。**DIGITIMES Asia** の Samsung／HBM4 は記事 ID が **20260428**（REALTIME NEWS）。

### 新規トピック

#### クラウド・提携・法務

- **OpenAI と Microsoft が提携契約を再修正（Microsoft の OpenAI IP／モデル・製品への権利が 2032 年までの非独占ライセンスに変更、OpenAI がどのクラウドでも製品を提供可能に、収益シェアの扱い見直しなどを公式説明 — AWS 絡みの独占抵触リスク回避が報道でも論点）** — 出典: [OpenAI](https://openai.com/index/next-phase-of-microsoft-partnership/)（April 27, 2026）

#### AI・資金調達

- **元 DeepMind の David Silver が主宰する英国の Ineffable Intelligence が約 11 億ドル調達・評価額約 51 億ドル — 強化学習で「人間データなし」の superlearner を目指す構想として報道** — 出典: [TechCrunch](https://techcrunch.com/2026/04/27/deepminds-david-silver-just-raised-1-1b-to-build-an-ai-that-learns-without-human-data/)（10:24 AM PDT · April 27, 2026）

#### データセンター・電力

- **Meta がスタートアップ Reflect Orbital と契約し、衛星経由で地上のソーラーに夜間も赤外線で電力を届ける構想でデータセンター電源を狙うと報道 — 詳細な商用タイムラインは開発途上との整理** — 出典: [TechCrunch](https://techcrunch.com/2026/04/27/meta-inks-deal-for-solar-power-at-night-beamed-from-space/)（Published 2026-04-27T10:00:00+00:00）

#### セキュリティ

- **CVE-2026-32202（Windows Shell／強制 SMB 認証・Net-NTLMv2 窃取が論点）について、不完全パッチ経緯や APT28 などの利用文脈を Akamai 調査ベースで整理 — Microsoft は Exploitation Detected とし 2026 年 4 月更新で修正などと説明** — 出典: [SecurityWeek](https://www.securityweek.com/incomplete-windows-patch-opens-door-to-zero-click-attacks/)（Published: 2026-04-27T13:09:27+00:00）

#### 半導体・メモリ供給

- **Samsung が平沢（Pyeongtaek）ラインの DRAM／HBM4 能力増強を急ぐとの報道 — AI サーバー需要を背景にしたメモリキャパシティ競争が論点（ページ本文は購読制）** — 出典: [DIGITIMES Asia](https://www.digitimes.com/news/a20260428VL209/samsung-hbm4-fab-capacity-dram.html)（REALTIME NEWS／記事 ID に 20260428）

### note底稿の続報

- **Microsoft×OpenAI の提携が「独占終了タイミング」「クラウド横断での製品提供」「収益シェア」まで踏み込んで改定され、調達・クラウド依存の読みに直接効く更新 — OpenAI 公式の同日投稿で一次確認可能** — **底稿:** `note/202604/20260402/OpenAI約1220億ドル調達を公式ベースで整理｜computeとパートナーが主役.md` / `note/202604/20260416/2026-04-16-openai-spud-enterprise-pivot｜OpenAI「Spud」と法人寄りシフト.md`。**続報出典:** [OpenAI](https://openai.com/index/next-phase-of-microsoft-partnership/)（April 27, 2026）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**` 底稿（`note/Druft/` 除外）。ラジオ台本は本編がある場合は本編を優先。
- **国内（日本）:** **IPA／経産省**のデジタルスキル標準 ver.2.0 は **公式公開が 2026-04-16** のため、本調査の **D−1（4/27）以降の主出典**としては採用していない。
- **note 続報（無／薄）:** `note/202604/20260427/2026-04-27-windows-k2-initiative｜Windows 11の品質回復をどう読むか.md` は **同日これまでのログで Techmeme 起点が登録済み**で、**4/27〜28 に別の「主出典 URL」として追加できる続報は見つけず**。

---

## 調査 2026-04-29 10:00 （JST）

**調査日 D＝2026-04-29。** `news-recency-policy.md` により、**新規トピック**および **`### note底稿の続報`** の主出典は **JST で 2026-04-28 または 2026-04-29** にページ記載の公開日・掲載日（または Last modified が同日更新と明確なソース）があるものに限定。**OpenAI×Microsoft 提携再修正（4/27 公式）**や **Ineffable 調達（4/27 TechCrunch）**など **4/27 以前の主出典のみ**のトピックは本ブロックでは再掲しない。**CVE-2026-3854** は NVD の初回 **Published** が **2026-03-10** のため、新規枠の主出典は **2026-04-28 掲載の解説記事**とした。

### 新規トピック

#### クラウド・AIインフラ

- **AWS と OpenAI が提携拡大を発表 — OpenAI の最新モデル・Codex・エージェント構築向き製品を Amazon Bedrock に展開、「Bedrock Managed Agents」で OpenAI 推論モデルと AWS 基盤を組み合わせる旨を Amazon 公式が説明（Microsoft 側の非独占化を踏まえた実装面の動きとして報道も追随）** — 出典: [About Amazon (AWS)](https://www.aboutamazon.com/news/aws/bedrock-openai-models)（Published: 2026-04-28T17:00:03+00:00）

#### セキュリティ・サプライチェーン

- **GitHub Enterprise Server 等を対象とした push 操作トークンのサニタイズ不備による RCE（CVE-2026-3854、CWE-77）が注目集める — Wiz 調査・バウンティ経由報告、複数 GHES パッチ版での修正が文脈で紹介（NVD 上の初回 Published は 2026-03-10 のため本枠では紙面掲載 4/28 の解説を主出典化）** — 出典: [Security Affairs](https://securityaffairs.com/191434/security/cve-2026-3854-github-flaw-enables-remote-code-execution.html)（April 28, 2026）

- **LiteLLM プロキシの認証前 SQL インジェクション（CVE-2026-42208）が実害型で悪用 — 1.83.7 への更新・露出キーローテーション等が推奨される整理** — 出典: [BleepingComputer](https://www.bleepingcomputer.com/news/security/hackers-are-exploiting-a-critical-litellm-pre-auth-sqli-flaw/)（April 28, 2026）

#### 国内・製造IT

- **イビデンが 4 月 13 日不具合のコーポレートサイトを完全復旧と発表 — 外部 Web サーバーへの不正アクセスで無関係ページ表示、サイト外への侵入やランサム痕跡なし・個人情報・社内停止なしと説明** — 出典: [Reuters Japan](https://jp.reuters.com/markets/global-markets/2OJSNGWJYRPD7OT4ZDOXF3JDKE-2026-04-28/)（［東京 28日 ロイター］表記）

#### 医療・セキュリティ（国内報道）

- **日本医科大学武蔵小杉病院のランサムウェア被害（2026年1月）と VPN 経路・ナースコール経由の個人情報取り扱い、公表の経緯・規模修正などを日経クロステックが整理（同連載内で医療機関の社内統制の論点にも触れる構成）** — 出典: [日経クロステック (xTECH)](https://xtech.nikkei.com/atcl/nxt/mag/nnw/18/041800012/041700322/)（Published: 2026-04-29T07:00:00+09:00）

### note底稿の続報

- **提携「非独占化」の直後に、AWS×OpenAI が Bedrock 上でのモデル・Codex・マネージドエージェント提供を公式化 — 4/27 公式改定の「どのクラウドでも提供」を実行面で裏付ける動き** — **底稿:** `note/202604/20260428/2026-04-28-microsoft-openai-partnership-amendment｜プライマリは残し独占は外した.md` / `note/202604/20260402/OpenAI約1220億ドル調達を公式ベースで整理｜computeとパートナーが主役.md`。**続報出典:** [About Amazon (AWS)](https://www.aboutamazon.com/news/aws/bedrock-openai-models)（Published: 2026-04-28T17:00:03+00:00）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**`（`note/Druft/` 除外）。ラジオ台本は本編がある場合は本編を優先。
- **鮮度外（参考）:** **アルプスアルパイン**の VPN 経由不正アクセス公表は **プレス日が 2026-04-27** のため、**D＝4/29** の **D−1（4/28）以降主出典**ルールでは新規枠から外した（**4/28 掲載の報道**のみでは一次の「公表日」と別暦になりうるため保守的に省略）。
- **省略（同一事件・既掲）:** **CVE-2026-32202** 不完整パッチ解説は **直近ログで SecurityWeek を既登録**済みのため本ブロックでは再掲なし。
- **note 続報（薄／無）:** Anthropic Project Deal・Mythos・Rapidus・Cursor/SpaceX ほか **4/28 以降の別主出典 URL**は、`seen-urls.json` 既出または **4/27 以前のみ**で追加せず。

---

## 調査 2026-04-30 12:00 （JST）

**調査日 D＝2026-04-30。** `news-recency-policy.md` により、**新規トピック**および **`### note底稿の続報`** の主出典は **JST で 2026-04-29 または 2026-04-30** にページ記載の公開日・掲載日（または通信社電文日付）があるものに限定。**TechCrunch** の Anthropic 観測記事は **5:07 PM PDT · April 29, 2026**（**JST では 4/30 午前**）。**Reuters** の DeepSeek／Huawei 特集は **April 29 (Reuters)** 電文。**Nikkei Asia** の東京エレクトロン稿は **April 29, 2026 02:40 JST**。**Reuters** の豪 APRA 関連は **SYDNEY, April 30 (Reuters)**。

### 新規トピック

#### 資金調達・AI企業

- **Anthropic が新たに約500億ドル規模の調達案を検討し、企業価値は約8500億〜9000億ドル帯との観測が複数筋から報じられる — 売上ラン・レートが急拡大していることや Claude Code／Cowork などが背景として説明、5月の取締役会で方針を確定する見込みなど** — 出典: [TechCrunch](https://techcrunch.com/2026/04/29/sources-anthropic-could-raise-a-new-50b-round-at-a-valuation-of-900b/)（5:07 PM PDT · April 29, 2026；JST 4/30 早朝）

#### AI・地政学・半導体

- **DeepSeek の V4 と Huawei Ascend 950 向け最適化を軸に、中国が Nvidia 依存を減らす「並行の AI エコシステム」を組む動きと、Meta×Manus 買収の中国側秩序解消が同じ長期インタビュー稿で接続される論旨 — Reuters が北京発の特集として整理** — 出典: [Reuters](https://www.reuters.com/technology/artificial-intelligence/deepseek-bets-huawei-china-pushes-end-reliance-nvidia-2026-04-29/)（April 29, 2026）

#### 半導体製造装置・供給網（国内報道）

- **台湾の裁判所判断などを手がかりに、東京エレクトロン子会社出身者による TSMC 機密流出疑惑が、主要顧客との関係や競争環境に与えうる影響として整理 — Nikkei Asia が英語で報道** — 出典: [Nikkei Asia](https://asia.nikkei.com/business/tech/semiconductors/tokyo-electron-s-close-ties-with-tsmc-at-risk-after-chip-tech-leak)（April 29, 2026 02:40 JST）

#### 規制・金融セキュリティ

- **豪州金融監督当局 APRA が銀行向け書簡で、ベンダ説明頼みの AI リスク管理や取締役会の技術リテラシー不足などを指摘 — 「フロンティア AI」として Mythos 等がサイバー攻撃の規模・速度を押し上げうるとの警告が通信社で紹介** — 出典: [Reuters](https://www.reuters.com/legal/government/australia-calls-stronger-ai-risk-controls-financial-firms-2026-04-30/)（SYDNEY, April 30, 2026）

### note底稿の続報

- **Google の大型投資・計算容量の枠組みに続き、追加ラウンド観測で評価帯がさらに上振れする公算が報じられ、Anthropic の資本・需要サイドの読みを更新する材料** — **底稿:** `note/202604/20260425/2026-04-25-google-anthropic-up-to-40b-investment｜ライバル同士をつなぐ資本とギガワット.md` / `note/202604/20260424/2026-04-24-nec-anthropic-enterprise-ai｜NECがAnthropicの「日本拠点初のグローバルパートナー」になった話.md`。**続報出典:** [TechCrunch](https://techcrunch.com/2026/04/29/sources-anthropic-could-raise-a-new-50b-round-at-a-valuation-of-900b/)（5:07 PM PDT · April 29, 2026）

- **Mythos を「フロンティア AI」のリスク例として金融監督の公式文脈に置いた APRA の警鐘 — 米国の調達・指定議論と並べて「規制当局がどの語彙で神経を尖らせているか」の続報** — **底稿:** `note/202604/20260410/2026-04-10-Mythos｜米財務省・FRBと大行CEO会合報道の読み分け.md` / `note/202604/20260414/2026-04-14-anthropic-mythos-pentagon-clark｜政権協議と調達訴訟の読み分け.md` / `note/202604/20260420/2026-04-20-nsa-anthropic-mythos-pentagon-axios｜NSAとMythos──「指定」と報道のズレをどう読むか.md`。**続報出典:** [Reuters](https://www.reuters.com/legal/government/australia-calls-stronger-ai-risk-controls-financial-firms-2026-04-30/)（SYDNEY, April 30, 2026）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**` 底稿（`note/Druft/` 除外）。ラジオ台本は本編がある場合は本編を優先。
- **鮮度外（参考）:** **Bloomberg** の Google×米国防総省（4/28 付）、**Reuters** の Meta×Manus 中国当局審査解説（**April 28, 2026** 電文）、**BleepingComputer** の Vimeo／Anodot 波及（**April 28, 2026** 掲載）はいずれも **D−1（4/29）未満の主出典日**のため新規枠に未採用。
- **note 続報（薄）:** AWS Bedrock×OpenAI 底稿は **4/29 調査ブロックの About Amazon 主出典が最新**のため追加せず。DeepSeek V4 単体底稿はリポジトリ内に本編が薄く、本回は **Reuters 深掘り稿**を新規トピックに集約。

---

## 調査 2026-05-01 19:00 （JST）

**調査日 D＝2026-05-01。** `news-recency-policy.md` により、**新規トピック**および **`### note底稿の続報`** の主出典は **JST で 2026-04-30 または 2026-05-01** にページ記載の公開日・掲載日（または電文日／KEV 追記日）があるものに限定。**OpenAI** の Advanced Account Security は公式 **April 30, 2026**。**The Verge** の Claude Security は **Posted Apr 30, 2026 at 5:00 PM UTC**（**JST では 5/1 午前**）。**BleepingComputer** の cPanel 記事は **April 30, 2026**。**DIGITIMES Asia** の OpenAI／Stargate は記事 ID **20260430**。**OpenAI** のインフラ総括ブログ [Building the compute infrastructure…](https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/) は **April 29, 2026** のため、本ブロックの「10GW 超え」の主出典は **4/30 の産業メディア**に寄せた。

### 新規トピック

#### アカウントセキュリティ・認証

- **OpenAI が ChatGPT アカウント向け「Advanced Account Security（AAS）」を任意適用で提供開始 — パスワードログインを止めパスキーまたはセキュリティキーを要求、メール／SMS リカバリ無効化・セッション短縮・ログイン通知などを束ね、Yubico と共同ブランドの YubiKey バンドルも説明 — Trusted Access for Cyber の個人メンバーは **2026年6月1日**から AAS 必須なども明記** — 出典: [OpenAI](https://openai.com/index/advanced-account-security/)（April 30, 2026）

#### AI・エンタープライズセキュリティ

- **Anthropic が法人向けコードベース走査ツール「Claude Security」を Opus 4.7 ベースでグローバルのエンタープライズ顧客へ展開すると報道 — Mythos とは別製品として整理** — 出典: [The Verge](https://www.theverge.com/ai-artificial-intelligence/921198/anthropic-rolls-out-its-codebase-scanning-security-tool-for-businesses)（Posted Apr 30, 2026 at 5:00 PM UTC；JST 5/1 早朝）

#### ホスティング・インフラセキュリティ

- **cPanel／WHM／WP Squared の認証バイパス（CVE-2026-41940）が実害型で悪用され、技術詳細・PoC 公開後の報道が注目を集める — CISA KEV には **2026-04-30** 追加・対応期限 **2026-05-03** の整理あり — 出典: [BleepingComputer](https://www.bleepingcomputer.com/news/security/critical-cpanel-and-whm-bug-exploited-as-a-zero-day-poc-now-available/)（April 30, 2026）（CVE の当局・NVD側では同日の KEV 追記・NVD 更新が確認可能: [NVD](https://nvd.nist.gov/vuln/detail/CVE-2026-41940)）

#### データセンター・電力（産業報道）

- **OpenAI が米国で Stargate の約10ギガワット目標を前倒しで達し、直近90日で3ギガワット超を追加したほか、地域コミュニティ投資の試みなどと並べて報じられる — 記事は購読制要素あり** — 出典: [DIGITIMES Asia](https://www.digitimes.com/news/a20260430VL210/openai-stargate-infrastructure-cost-demand.html)（REALTIME NEWS／記事 ID に 20260430）

### note底稿の続報

- **評価額観測とは別軸で、法人向けのコードベースセキュリティ製品が製品報道として具体化 — Opus 4.7／パートナー論と並べて「売上以外のエンタープライズ提供物」を追う材料** — **底稿:** `note/202604/20260417/2026-04-17-anthropic-claude-opus-4-7｜Opus-4.7とサイバー安全策の一段目.md` / `note/202604/20260424/2026-04-24-nec-anthropic-enterprise-ai｜NECがAnthropicの「日本拠点初のグローバルパートナー」になった話.md`。**続報出典:** [The Verge](https://www.theverge.com/ai-artificial-intelligence/921198/anthropic-rolls-out-its-codebase-scanning-security-tool-for-businesses)（Posted Apr 30, 2026 at 5:00 PM UTC）

- **チャット／開発アカウントのフィッシング耐性・モデル学習除外・サイバー防御プログラムとの接続が公式で一段ずれる — ワークスペース運用や法人ガバナンスの読みに効く** — **底稿:** `note/202604/20260423/2026-04-23-openai-workspace-agents-chatgpt｜カスタムGPTの次にくる「チームで育てる」共有エージェント.md` / `note/202604/20260415/2026-04-15-openai-gpt-5-4-cyber｜TACとGPT-5.4-Cyberのレイヤ読み分け.md`。**続報出典:** [OpenAI](https://openai.com/index/advanced-account-security/)（April 30, 2026）

- **米国内コンピュート確保の見え方が「目標前倒し達成」と産業報道でまとめられ、調達・インフラ底稿の時間軸を補強** — **底稿:** `note/202604/20260402/OpenAI約1220億ドル調達を公式ベースで整理｜computeとパートナーが主役.md` / `note/202604/20260429/2026-04-29-aws-bedrock-openai-codex-managed-agents｜独占を外した翌日にBedrockへ載った.md`。**続報出典:** [DIGITIMES Asia](https://www.digitimes.com/news/a20260430VL210/openai-stargate-infrastructure-cost-demand.html)（REALTIME NEWS／20260430）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**`（`note/Druft/` 除外）。ラジオ台本は本編がある場合は本編を優先。
- **国内（日本）:** **METI／IPA** の既知施策や **4/28 以前のロイター転載**中心で、**D−1（4/30）以降の独立トピックを大手報道・IR で1本に絞るのが難しく**、本ブロックは海外公式・産業報道を厚めに採用。
- **鮮度外（参考）:** OpenAI の **10GW** を説明する公式ブログ [Building the compute infrastructure…](https://openai.com/index/building-the-compute-infrastructure-for-the-intelligence-age/) は **April 29, 2026** のため **D＝5/1 の新規枠（4/30・5/1）からは外し**、関連は DIGITIMES（4/30）と AAS（4/30）に分散。
- **note 続報（薄／無）:** `note/202604/20260430/2026-04-30-anthropic-sources-50b-rumor…` は **調査時点で匿名ソース観測の更新主出典なし**（薄／無）。GitHub Copilot の Actions 課金告知は **`practical-it-alerts` と overseas の用途分立**のため本ログでは再掲せず。

---

