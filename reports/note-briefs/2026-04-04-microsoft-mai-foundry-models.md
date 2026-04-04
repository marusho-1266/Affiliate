# 報告資料: Microsoft MAI（Transcribe-1 / Voice-1 / Image-2）の Foundry 提供

- **調査日**: 2026-04-04
- **主出典**: [Microsoft AI News — Today we're announcing 3 new world class MAI models, available in Foundry](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/)（**2026-04-02**、署名: Mustafa Suleyman）
- **要約（1文）**: Microsoft は自社ブランド **MAI** の音声認識・音声合成・画像生成の 3 モデルを **Microsoft Foundry** と **MAI Playground** で利用可能にし、公式に価格帯・ベンチマーク主張・モデルカード PDF・責任ある AI・ガバナンスの文脈を同時に示した。

---

## 1. 背景 — なぜ今この情報が出ているか

- **事実（時系列）**:
  - **2026-04-02**: Microsoft AI がブログで **MAI-Transcribe-1**、**MAI-Voice-1**、**MAI-Image-2** を **Microsoft Foundry** および **MAI Playground** で提供開始と発表（上記 URL）。
  - **MAI-Transcribe-1（公式の主張要約）**: 業界標準の **FLEURS** を引用し、**Microsoft 製品利用の多い上位 25 言語**を対象に品質を説明。バッチ文字起こし速度が **既存の Azure Fast 比 2.5 倍**と記載。**脚注**で「25 言語のうち 11 言語で FLEURS 1 位」等、**Whisper-large-v3** や **Gemini 3.1 Flash** との比較文が本文・脚注にある。
  - **MAI-Voice-1**: 自然な音声生成、**数秒の音声からカスタム音声を安全に作成**可能とし、**1 秒で 60 秒分の音声**を生成可能と記載。**Copilot Audio Expressions** や **Copilot Podcasts** への体験導線を提示。
  - **MAI-Image-2**: **Arena.ai リーダーボード**でモデルファミリーとして **トップ 3** に入った実績を引用。Foundry / Copilot で **少なくとも 2 倍速**の生成（品質は同程度）と **実運用トラフィックデータ**に基づく旨を記載。**Bing** と **PowerPoint** への段階的展開を言及。**WPP** のクリエイティブ責任者コメントを掲載。
  - **価格（公式本文に明記）**:
    - MAI-Transcribe-1: **時間あたり $0.36 から**
    - MAI-Voice-1: **100 万文字あたり $22 から**
    - MAI-Image-2: **テキスト入力 100 万トークンあたり $5**、**画像出力 100 万トークンあたり $33** から
  - **モデルカード**: 各モデル **PDF** へのリンクが記事内にあり（[Transcribe-1](https://microsoft.ai/pdf/MAI-Transcribe-1-Model-Card.pdf)、[Voice-1](https://microsoft.ai/pdf/MAI-Voice-1-Model-Card.pdf)、[Image-2](https://microsoft.ai/pdf/MAI-Image-2-Model-Card.pdf)）。
  - **アクセス**: Foundry 未利用者向けに **問い合わせフォーム**。**MAI Playground** は **（US のみ）** と明記。
  - **安全・統治**: 開発・テスト・レッドチーミングを実施した旨、Foundry の **ガードレール・ガバナンス・エンタープライズ向けコントロール**に言及。
- **公開情報から読み取れる動機**:
  - **自社スタックの外販**: Copilot / Bing / PowerPoint 等で使っているモデルを **開発者向けに Foundry 経由で提供**し、価格・速度・品質を前面に出す。
  - **「Humanist AI」** というブランド叙述（人間中心、実用向けコミュニケーション）を短く提示。
- **補足・推測（根拠付き）**:
  - **競合比「最も競争力のある価格」「大手クラウドで最高の価格性能」**等の表現は **ベンダ自身のマーケティング主張**であり、**第三者の独立検証をこのブログだけで断定できない**。
  - **Arena.ai ランキング**は時点・評価方法で変動しうるため、記事執筆時は **ランキングのスナップショット日**を確認するとよい。

---

## 2. 目的 — 誰に、何をしてほしいか

| 想定読者 | 発信側が望む行動（推定） | note 読者への実務的示唆 |
|----------|---------------------------|-------------------------|
| エンタープライズ開発者・ISV | **Microsoft Foundry** で MAI を組み込み、音声エージェント・メディア・クリエイティブ案件に利用 | **モデルカード PDF** と **Learn の API ドキュメント**（例: [MAI-Transcribe-1（Speech）](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe)）を読んでから PoC 設計 |
| 既存 Azure / Microsoft 365 顧客 | Copilot 系で体験した品質を **自社アプリ**に拡張 | **利用地域・データ境界・コンプライアンス**は契約・ドキュメントで確認（本ブリーフは断定しない） |
| クリエイティブ・マーケ業界 | 画像生成の速度・品質で制作フローを再設計 | **WPP の事例**は広告グループの **推奨引用**であり、一般化の根拠としては限定的 |
| 一般消費者 | **Copilot Audio Expressions** 等で体験 | MAI Playground は **米国のみ**とあるため、日本からの利用可否は公式の地域表記で要確認 |

---

## 3. 効果 — 短期・中期・長期の予想

**時間軸の定義**: **短期＝0〜3か月**、**中期＝3か月〜1年**、**長期＝1年以上**（一般的目安）。

- **短期（0〜3か月）**:
  - **予想される効果**: Foundry 利用者の **PoC・プロトタイプ**で MAI が試され、音声・画像の **レイテンシ／コスト試算**が更新されうる。
  - **不確実性**: **「最安・最高の価格性能」**は競合の価格改定で相対評価が変わる。**GPU 効率**の主張はワークロード依存。
  - **効果が出ない条件**: 組織が **OpenAI 等の既存契約**にロックインしており、Foundry 側の評価が進まない場合。

- **中期（3か月〜1年）**:
  - **予想される効果**: **エージェント音声**・**社内動画**・**広告クリエイティブ**で、マルチモーダル API の **標準オプション**として MAI が並ぶ可能性（エコシステム依存）。
  - **不確実性**: **規制・著作権・声のなりすまし**に関する企業ポリシーが利用を制限しうる。
  - **効果が出ない条件**: 品質が特定業種要件を満たさない、または **カスタム音声**のコンプラ審査がボトルネックになる場合。

- **長期（1年以上）**:
  - **予想される効果**: クラウド上の **「自社基盤モデル」ブランド**（Google / OpenAI / Anthropic 等と並ぶ選択肢）としての認知が定着するかは **継続投資と実利用**に依存（推測）。
  - **不確実性**: モデル世代の入れ替え、**価格戦争**、**オープンモデル**の進展。
  - **効果が出ない条件**: 研究開発や競合の優位が拡大し、**差別化が価格のみ**に収まる場合。

---

## 4. note 執筆メモ（任意）

- **フック案（1〜2文）**: 「自社モデルを“中の人”にした Microsoft」が、**文字起こしの時給単価・画像のトークン単価まで**ブログで晒した日——**見せたいのは技術か、採算か**。
- **検証が必要な一点（事実・数値・日付）**:
  - **FLEURS / Arena.ai** の順位は **公開時点のスナップショット**として扱い、**競合モデルの版**（Whisper 等）を脚注どおりに確認する。
  - **価格**は **「starts at」** とあるため、リージョン・通貨・課金単位の **正式な価格表（Azure）** と突合したい。
  - **MAI Playground「US only」** の範囲（居住者か IP か）は公式 FAQ で確認。
- **免責・注意**: 価格・性能は変わりうる。**投資・調達判断**は専門家へ。ベンダの **競合比較は一次情報でも宣伝**の側面がある。

---

## 5. 参照一覧

### 一次・準一次（優先）

- [Microsoft AI News: 3 new world class MAI models in Foundry](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/)（2026-04-02）
- モデルカード PDF: [MAI-Transcribe-1](https://microsoft.ai/pdf/MAI-Transcribe-1-Model-Card.pdf) / [MAI-Voice-1](https://microsoft.ai/pdf/MAI-Voice-1-Model-Card.pdf) / [MAI-Image-2](https://microsoft.ai/pdf/MAI-Image-2-Model-Card.pdf)
- [Microsoft Learn: MAI-Transcribe-1 in LLM Speech API](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe)（ドキュメント）
- [Microsoft Learn: Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)（概要）

### 二次（コミュニティ・紹介記事）

- [Tech Community: Introducing MAI-Transcribe-1, MAI-Voice-1, and MAI-Image-2 in Microsoft Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-mai-transcribe-1-mai-voice-1-and-mai-image-2-in-microsoft-foundry/4507787)（Azure AI Foundry ブログ）

---

## 調査モード

- **ライト調査**（親エージェントが **microsoft.ai 公式投稿**を取得し、**Microsoft Learn** でドキュメントを補強）。**Task サブエージェントおよびレーン A〜E は未使用**。
