# Microsoft「MAI」3モデルがFoundryに揃った｜音声認識・音声合成・画像生成を開発者向けAPIに

## はじめに

**MAI** は Microsoft が掲げる自社モデル群のブランド名、**Microsoft AI** は今回の発表主体（組織名）です。混同しやすいので、先にそろえておきます。

本記事では、**2026年4月2日**に **Microsoft AI**（署名: Mustafa Suleyman）が公表した **MAI-Transcribe-1 / MAI-Voice-1 / MAI-Image-2**（それぞれ **音声認識・音声合成・画像生成**）の **Microsoft Foundry** 提供について、**[公式ブログ](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/)** および **Microsoft Learn** に書いてある範囲を中心に、実務で使う目線で要点を整理します。

※本記事は**公開情報・一次ソースの要点**をもとに、筆者の解釈・所感を加えています。**投資・法務・税務の助言ではありません。**

SNS やまとめで数字や見出しがバラついて見えたときは、**記事末尾の公式リンクだけ開いて、日付と主張を自分の目で一度確認**してもらえると安心です。

---

## 1. 何が起きたのか（結論）

先に結論です。

- **2026年4月2日**、Microsoft は自社ブランド **MAI** の **音声認識・音声合成・画像生成**の3モデルを **Microsoft Foundry**（および試用向け **MAI Playground**）で利用可能にしたと発表した。
- このニュースの「主役」は単体モデルではなく、**Copilot / Bing / PowerPoint など製品側で使ってきた技術を、開発者向け API として切り出した**ことと、本文に **価格の起点（starting at）** まで載せたことだと読み取れる。
- 誤解されやすいのは、**「最も競争力のある価格」**のような**他社比の言葉**を、そのまま「客観事実」と読み替えること。一次情報でも**マーケティング表現**は残る。

「忙しいのでまず要点だけ知りたい」という方向けに言うと、  
**Microsoft が「自社のマルチモーダル」を Foundry に並べ、速度・品質に加え採算のメッセージまで出した**、という整理です。

---

## 2. 公式情報ベースの要点（3つ）

今回の情報で押さえるべきポイントは次の3点です。（出典は末尾の一次情報に寄せる）

### 2-1. Foundry で「使える」ようになった範囲

- **事実:** 公式は **Microsoft Foundry** と **MAI Playground** への導線を示している。Foundry の位置づけは [Microsoft Learn（Foundry）](https://learn.microsoft.com/en-us/azure/ai-foundry/) で確認できる。
- **補足:** **MAI Playground** は記事上 **US のみ** と明記されている。日本からの利用条件は、**利用時点の公式表記と契約**で要確認。
- **影響** または **あなたの現場に効く話:** 「社内で Foundry を触っているチーム」なら、**音声・画像の PoC 候補が一気に増える**ので、**いつの誰の発表か**をメモしてから評価比較表に載せると後で揉めにくい。

### 2-2. 三モデルの役割と、公式に載った価格の「起点」

- **まず一言ずつ:** **MAI-Transcribe-1** は音声認識（音声→テキスト）、**MAI-Voice-1** は音声合成（テキスト→音声）、**MAI-Image-2** は画像生成。

- **事実（公式本文の詳細）:**  
  - **MAI-Transcribe-1**: **FLEURS** を引用し、**Microsoft 製品利用の多い上位25言語**を軸に説明。バッチ文字起こしは **既存 Azure Fast 比 2.5 倍**などと記載。  
  - **MAI-Voice-1**: **数秒の音声**からカスタム声、**1秒で約60秒分の音声**などと記載。**Copilot Audio Expressions** / **Copilot Podcasts** への導線あり。  
  - **MAI-Image-2**: **Arena.ai** でモデルファミリー **トップ3** などと引用。Foundry / Copilot では **少なくとも2倍速**などの主張。**Bing**・**PowerPoint** への展開にも言及。  
  - 価格の起点（公式本文の **starting at**、いずれも USD 表記の抜粋）: Transcribe **$0.36/時間**、Voice **$22/100万文字**、Image-2 はテキスト入力 **$5/100万トークン**・画像出力 **$33/100万トークン** から、とある。
- **補足:** 価格は **リージョン・通貨・課金単位**で変わりうる。脚注2では **Whisper-large-v3** および **Gemini 3.1 Flash**（いずれも**公式ブログ脚注の表記どおり**）との比較に触れている。**評価条件・対象言語・モデル版**まで含めて読まないとズレやすい。
- **影響** または **あなたの現場に効く話:** 見積りや PoC では、**ブログの数字だけでなく Azure の価格表・契約**と突き合わせる。**レート制限やデータ境界**はドキュメントとコンソールで確認。

### 2-3. モデルカード・安全・ガバナンス

- **事実:** 各モデルに **モデルカード PDF** のリンクがある（[Transcribe-1](https://microsoft.ai/pdf/MAI-Transcribe-1-Model-Card.pdf) / [Voice-1](https://microsoft.ai/pdf/MAI-Voice-1-Model-Card.pdf) / [Image-2](https://microsoft.ai/pdf/MAI-Image-2-Model-Card.pdf)）。記事では開発・テスト・レッドチーミングに触れ、Foundry に **ガードレール・ガバナンス・エンタープライズ向けコントロール**がある旨も述べている。API の入口例は [MAI-Transcribe-1（Speech）](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe)。
- **補足:** 広告グループ **WPP** のコメントは**企業側の推奨引用**であり、一般化の根拠には限界がある。
- **影響** または **あなたの現場に効く話:** 本番利用前に **モデルカード・利用規約・ログ保持**をセットで見る。**声のなりすまし・著作権**まわりは社内ポリシーと併せて整理。

---

## 3. 深堀り：関連する論点

### 3-1. 「一次情報」でも残るベンダ主張の読み方

公式ブログには **大手クラウド比較**や **価格性能**に踏み込んだ表現がある。一次ソースとはいえ、**宣伝色が乗らないニュースは少ない**ので、社内共有では **「公式の主張」ラベル**を付け、必要なら**自社データでのベンチマーク**を別枠にすると安全だ。

### 3-2. ランキングと「公開時点のスナップショット」

**Arena.ai** や **FLEURS** の順位は、**時点・評価方法・モデル版**で変わりうる。転載するときは **日付と出典**をセットにしたい。

---

## 4. これからどうなりうか（予想と不確実性）

時間軸はあくまで目安です。**競合の価格改定・公式ロードマップ**で変わり得ます。

**短期（数か月）**  
Foundry 利用者の **PoC** が増え、音声・画像まわりの **レイテンシ／コスト試算**が更新されうる。一方で **OpenAI 等の既存契約**が強い組織では、評価が進まないこともある。

**中期（〜1年）**  
エージェント音声・社内動画・クリエイティブ制作で、マルチモーダル API の**選択肢の一つ**として並びうる。**規制・声の悪用・著作権**の社内ルールがボトルネックになる可能性もある。

**長期（1年以上）**  
「自社基盤モデル」ブランドの定着は **継続投資と実利用**に依存。**オープンモデル**や**価格戦争**で相対評価は動きうる。

---

## 5. 実務でどう変わるか（筆者の見解）

地方SEとして日々の運用・開発に当てはめると、次の点が変わりそうです。**あなたの現場が近いところだけ拾って読んでも大丈夫**です。

- **契約・コスト:** ブログの **starts at** は「雰囲気」ではなく、**見積りのたたき台**にはなる。ただし **リージョンと課金単位**は Azure 側で確定させる。
- **設計・フォールバック:** 音声・画像を一本化するほど、**失敗時の代替モデル**や**オフラインフォールバック**の設計が効いてくる。
- **ガバナンス・ログ:** カスタム音声や画像生成は、**誰が承認し、どこまでログに残すか**が早めに詰まりやすい。

特に **API 課金とレート制限**では、  
**「公式が言う速さ」と「自社トラフィックでの速さ」は別物**、として切り分けるのが重要だと感じました。

---

## 6. まず何を試すか（行動ベース）

読むだけで終わらせないために、**負担の小さい順**の例です。無理のないところからで大丈夫です。

1. **一次情報の確認:** [公式ブログ](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/)で、**日付・価格の書き方・脚注**を原文で押さえる。
2. **技術の骨格の確認:** [Foundry ドキュメント](https://learn.microsoft.com/en-us/azure/ai-foundry/) と [MAI-Transcribe-1（Speech）](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe) で、用語とフローを自分の言葉で要約する。
3. **実装・契約の確認:** 権限があれば、Azure / Foundry の**価格ページ・利用規約・データ取り扱い**の最終更新日だけでも眺める。

---

## 7. 向いている人 / まだ様子見でよい人

### 向いている人

- **Microsoft Foundry や Azure AI を既に触っている**開発者・インフラ寄りの方
- **Copilot 周りの品質を、自社アプリに載せたい**プロダクト・社内SE
- **原文に当たってから記事を書きたい**読者

### 様子見でよい人

- **クラウドの生成 AI をまだ使っていない**段階で、まず基盤選定が固まっていない方
- **投資判断だけが目的**の場合（本記事は銘柄判断を扱いません）
- **米国以外の Playground 利用**をすぐに試したいが、契約・地域の整理がまだの方

---

## まとめ

今回のポイントを一言でまとめると、  
**Microsoft が MAI を Foundry に並べ、製品で培ったマルチモーダルを「開発者が組み込める形」で提示し、価格の起点まで出した** です。

今後 **API 価格・条項・仕様・提供地域**で状況が変わる可能性があるため、**気になったタイミングで末尾の一次情報と、自分の契約・設定画面だけでも覗く**きっかけにしてもらえるとうれしいです。

---

## 参考情報（原文）

- [Today we're announcing 3 new world class MAI models, available in Foundry](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/)（Microsoft AI 公式ブログ、2026-04-02）
- [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)（Microsoft Learn）
- [MAI-Transcribe-1 in LLM Speech API](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/mai-transcribe)（Microsoft Learn）
- モデルカード PDF: [MAI-Transcribe-1](https://microsoft.ai/pdf/MAI-Transcribe-1-Model-Card.pdf) / [MAI-Voice-1](https://microsoft.ai/pdf/MAI-Voice-1-Model-Card.pdf) / [MAI-Image-2](https://microsoft.ai/pdf/MAI-Image-2-Model-Card.pdf)
- [Tech Community: Introducing MAI-Transcribe-1, MAI-Voice-1, and MAI-Image-2 in Microsoft Foundry](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/introducing-mai-transcribe-1-mai-voice-1-and-mai-image-2-in-microsoft-foundry/4507787)（Azure AI Foundry ブログ、二次）

---

## 免責

本稿は公開情報の整理であり、**投資・契約・税務・法的判断の助言ではありません**。価格・機能・提供地域は変更されうる可能性があります。
