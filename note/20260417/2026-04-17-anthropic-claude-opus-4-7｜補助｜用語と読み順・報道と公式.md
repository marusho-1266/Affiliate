# 「ITニュース・補助」｜Opus 4.7／Glasswing — 用語と読み順・報道と公式

## 本稿の位置づけ

**本編**は、Anthropic 公式が **2026-04-16** に公表した **Claude Opus 4.7** の内容と、直前の **Project Glasswing／Mythos Preview** との**接続**を整理します。

- [「ITニュース」｜Claude Opus 4.7 — Glasswingの「次の一段」が一般提供に載った日](./2026-04-17-anthropic-claude-opus-4-7｜Opus-4.7とサイバー安全策の一段目.md)（本編・無料）

**補助（本稿）**は、用語の足場・読み順・「誰の文脈か」の整理に紙幅を使います。

---

## おすすめの読み順

| 読者 | 推奨 |
|------|------|
| **初めての方** | **この補助** → **本編** |
| **Glasswing から追う方** | [Project Glasswing 本編](../20260408/2026-04-08-project-glasswing-note.md) → **本編**（補助は用語表だけでも可） |
| **筆者メモ（有料想定）だけ** | 本編の **§6 まとめ**まで読んでから **§7** へ |

---

## 1. 用語ミニ辞典

| 用語 | ざっくりした意味（本リポジトリ内の用法） |
|------|------------------------------------------|
| **GA（一般提供）** | Generally available。特定プレビューではなく、公式が定めるチャネルで利用できる状態、という趣旨（細部は各プラットフォームの表記に従う）。 |
| **Opus** | Anthropic の Claude ファミリのうち、高能力寄りの系譜。本件では **Opus 4.7** が新規。 |
| **Mythos Preview** | Glasswing の文脈で公表された**限定提供のフロンティアモデル**。公式は防衛的サイバー用途での利用を主眼に説明。 |
| **Project Glasswing** | 複数企業・団体と組み、クリティカルなソフトの防御に Mythos 等を当てる**イニシアチブ**の名称。 |
| **サイバー安全策（本件の言い方）** | Opus 4.7 投稿における **禁止・高リスク用途の自動検知とブロック**、および正当用途向けの **Cyber Verification Program** のセットを指す。 |
| **Cyber Verification Program** | 脆弱性研究・ペネトレーション・レッドチーム等の**正当なセキュリティ用途**で Opus 4.7 を使いたい利用者向けの**申請・検証**の仕組み（公式がフォームで案内）。 |
| **differentially reduce（投稿内表現）** | 学習の過程で**サイバー関連能力を相対的に抑える試み**をした、という公式の説明。外部からの技術監査ではない。 |
| **`claude-opus-4-7`** | Claude API 上のモデル識別子として公式投稿が言及。実装は [Models overview](https://platform.claude.com/docs/en/about-claude/models/overview) の最新表で確認。 |
| **Bedrock / Vertex AI / Foundry** | それぞれ AWS・Google Cloud・Microsoft 側のマーケットプレイス／開発者向け経路でモデルを提供する枠組み。契約・ログ・データ境界は**クラウド事業者＋自社契約**で別問題。 |

**API 上の ID・料金・コンテキスト等の対比**は、下記 **§5** に抜粋しています。

---

## 2. 年表（本件に直結する範囲）

| 時期 | 内容 | 出典 |
|------|------|------|
| 2026-04-07 前後 | **Project Glasswing** と **Mythos Preview** を公表 | [Anthropic — Glasswing](https://www.anthropic.com/glasswing) |
| 2026-04-16 | **Claude Opus 4.7** を GA。Glasswing で述べた段階的検証の**第一段**として位置づけ、サイバー安全策と Cyber Verification を説明 | [Anthropic — Opus 4.7](https://www.anthropic.com/news/claude-opus-4-7) |

---

## 3. 報道と公式のレイヤー

本トピックは **Anthropic 公式ブログが主役**です。通信社や大手テックメディアの見出しは、**追いかけ・引用**として読むのが素直です。

| レイヤ | 何が言えるか |
|--------|----------------|
| **Anthropic 公式（Opus 4.7）** | 機能・位置づけ・価格据え置き・提供チャネル・サイバー安全策・申請フォームへのリンク。 |
| **Anthropic 公式（Glasswing）** | Mythos の位置づけ、パートナー、クレジット・寄付のコミットなど**前段の物語**。 |
| **報道・二次** | 同日の競合動向との並べ方、投資・市場の文脈など。**数字や因果の追加**があるときは、元記事の一次に戻る。 |

---

## 4. 本編に入る前のチェックリスト（任意）

- [ ] **Opus 4.7 と Mythos Preview**を混同していない（公式は「Mythos よりサイバー能力は抑えた」と明記）。  
- [ ] **無許可の侵入テスト**を依頼していない（許可・法域は法務とセット）。  
- [ ] **API 名・リージョン・ログ**は、自社が実際に契約しているチャネルのドキュメントで再確認した。  

---

## 5. カタログ上の比較（API ドキュメント要約）

**出典:** Anthropic **[Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)**（ページ改定で数値が変わりうるため、**見積・契約前は必ず最新版**を開いて確認してください）。**完全な料金**（Batch・プロンプトキャッシュ・Vision・Extended thinking 課金等）は **[Pricing](https://platform.claude.com/docs/en/about-claude/pricing)** を参照。

下表は **Claude API 上の「現行フラッグシップ寄り」**の対比です。**性能ベンチではなく**、ドキュメントに載る **ID・料金レンジ・コンテキスト・出力上限・思考モードの有無**に限定しています。

| 項目 | Claude Opus 4.7 | Claude Opus 4.6（現行リスト掲載） | Claude Sonnet 4.6 | Claude Haiku 4.5 |
|------|-----------------|----------------------------------|-------------------|-------------------|
| **位置づけ（公式の一行）** | 複雑推論・エージェントコーディング向けに最も能力が高い **GA** モデル | 4.7 への移行元としてリストに残存 | 速度と知能のバランス | 最速寄り・ニアフロンティア |
| **Claude API ID（例）** | `claude-opus-4-7` | `claude-opus-4-6` | `claude-sonnet-4-6` | `claude-haiku-4-5-20251001`（エイリアス `claude-haiku-4-5`） |
| **標準料金（入力／出力・百万トークン）** | **$5**／**$25** | **$5**／**$25** | **$3**／**$15** | **$1**／**$5** |
| **Extended thinking** | いいえ | はい | はい | はい |
| **Adaptive thinking** | はい | —（ドキュメントの**旧世代一覧**に当項目の列がない） | はい | いいえ |
| **コンテキストウィンドウ** | **100万**トークン | **100万** | **100万** | **20万** |
| **Max output（同期 Messages API）** | **128k** トークン | **128k** | **64k** | **64k** |
| **Reliable knowledge cutoff**（公式表記） | Jan 2026 | May 2025 | Aug 2025 | Feb 2025 |
| **Training data cutoff** | Jan 2026 | Aug 2025 | Jan 2026 | Jul 2025 |

**補足（表の外に書かれている公式メモ）**

- **Mythos Preview** — [Project Glasswing](https://www.anthropic.com/glasswing) 経由の**研究プレビュー**・招待制。上表のような **公開の「$/MTok」一覧には載らない**運用です（本編の論点どおり **Opus 4.7 GA とは別物**）。  
- **AWS Bedrock** — 同一ドキュメントでは、**Opus 4.7 は Bedrock 上で research preview** の扱いに触れています（通常 GA の Bedrock ID 表とは読み分けが必要）。  
- **Opus 4.6** — ドキュメント上は **4.7 への移行**が推奨され、**Batch API で最大 30 万トークン出力**などの beta ヘッダの記載は **4.7／4.6／Sonnet 4.6** が対象、とあります（詳細は Models overview 本文）。

---
