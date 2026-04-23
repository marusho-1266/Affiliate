# 「ITニュース・補助」｜ChatGPT workspace agents — 用語と読み順・公式一次

## 本稿の位置づけ

本編は、**2026年4月22日**付の OpenAI 公式ブログ [Introducing workspace agents in ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt/) を主出典に、**何が公表されたか**と**何が「既定オフ」「未対応」「Soon」に留まるか**を切り分けたものです。

- [「ITニュース」｜ChatGPT に workspace agents — カスタム GPT の次にくる「チームで育てる」共有エージェント](./2026-04-23-openai-workspace-agents-chatgpt｜カスタムGPTの次にくる「チームで育てる」共有エージェント.md)

**補助（このファイル）**は足場です。**用語の初出定義**、**短い年表**、**情報の出どころ**をここに集約し、本編は論点の密度を保ちます。

---

## おすすめの読み順

| 読者 | おすすめ |
|------|-----------|
| **初めて** | この補助（用語・レイヤ）→ **本編** |
| **機能と条件だけ欲しい** | 本編「1. 何が公表されたか」→ 必要ならこの補助の用語表・年表 |
| **導入・ガバナンスの含意まで** | 本編 → 筆者メモ（本編末尾） |

---

## 1. 用語ミニ辞典

| 語 | ひとこと |
|----|-----------|
| **workspace agents（ワークスペース・エージェント）** | ChatGPT 上でチームが共有するクラウド側エージェント。**Codex で駆動**と公式が明記。**カスタム GPT の進化形**として位置づけ。 |
| **カスタム GPT／GPTs** | ChatGPT 上で個別にカスタマイズしたアシスタント。公式は当面維持し、**近く workspace agents への変換を容易にする**と述べる段階（詳細は「Soon」）。 |
| **リサーチプレビュー** | 仕様や提供範囲が変わりうる段階の公開。利用前にヘルプと契約で最新を確認する前提。 |
| **Codex** | OpenAI のコーディング／エージェント製品群。workspace agents の**駆動エンジン**として公式本文で言及。直前の [Codex for (almost) everything](https://openai.com/index/codex-for-almost-everything/)（Apr 16, 2026）の延長にある。 |
| **Compliance API** | OpenAI が Enterprise 向けに提供する監査・コンプライアンス用の API（公式投稿で言及）。**対象範囲と粒度**は管理者向け資料で要確認。 |
| **EKM（Enterprise Key Management）** | Enterprise 顧客が自前の鍵で暗号を管理する仕組み。**workspace agents はローンチ時点で EKM 利用ワークスペース未対応**とヘルプに記載。 |
| **MCP（Model Context Protocol）** | 外部ツール・コネクタを束ねるためのプロトコル。workspace agents の拡張でも前提になる用語。 |
| **コネクタ／接続アプリ** | Slack、Gmail、Notion など、エージェントが扱う外部アプリの接続。**エージェント所有アカウント**と**エンドユーザーアカウント**で認証設計が変わる。 |
| **テンプレ／対話的ビルダー** | workspace agents を作るときの二つの入り口。コーディング不要で、業務部門からも扱える想定。 |
| **サイドバー「Agents」** | ChatGPT の UI 上で workspace agents を呼び出すメニュー。 |
| **credit-based pricing** | 2026-05-06 から始まるクレジット制の課金。**単価の細目**は執筆時点では未公表。 |
| **共有コンテキスト／引き継ぎ（shared context, handoffs）** | 公式本文のキーワード。**チーム内で状態をつなぐ**ことが価値の中心、という位置づけを表す表現。 |

---

## 2. 年表（公式ページベース）

| 日付 | 内容 | レイヤ |
|------|------|--------|
| **2026-04-16** | OpenAI が **Codex** の大型アップデートを公表（[Codex for (almost) everything](https://openai.com/index/codex-for-almost-everything/)） | 一次・直前文脈 |
| **2026-04-22** | **workspace agents** をリサーチプレビューで公表（[Introducing workspace agents](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)） | **一次・本件** |
| **2026-04-22** | 同日、開発者向けに **Responses API の WebSocket モード**も別公表（本件とは**別レイヤの話**） | 参考（`note/202604/20260424/` の別稿） |
| **2026-05-06** | **workspace agents の無料期間終了**・**クレジット制課金開始**（公式本文明記） | 一次・予定 |
| **未確定（Soon）** | **GPTs → workspace agents の変換**導線（公式「Soon」） | 公式で明言あり、時期・互換範囲は未記載 |
| **未確定（What's next）** | **Codex アプリ側での workspace agents 対応**など（公式「What's next」の記述） | 公式で示唆、詳細は追加発信待ち |

---

## 3. 報道と公式のレイヤー

| 種類 | 例 | 読み方のメモ |
|------|-----|----------------|
| **OpenAI 公式ブログ（一次）** | [Introducing workspace agents in ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt/) | **機能名・提供形態・対象プラン・価格方針**はここを正とする。**事例**（Rippling 等）は「OpenAI が引用した顧客コメント」として扱う。 |
| **OpenAI ヘルプセンター（準一次）** | [ChatGPT Workspace Agents for Enterprise and Business](https://help.openai.com/en/articles/20001143) | **管理画面・既定オン/オフ・EKM 対象外・Slack 連携の注意**など、**運用の実装事実**が載る。ページの「Updated」表記は相対のため、利用時に再オープン推奨。 |
| **関連公式（横リンク）** | [Codex for (almost) everything](https://openai.com/index/codex-for-almost-everything/) / [Prompt injections](https://openai.com/safety/prompt-injections/) | **文脈**（Codex 側の機能線）と**安全**（プロンプトインジェクション）の補助資料として参照。 |
| **二次報道・解説記事** | 各メディアの要約・比較記事 | **追加の数値・競合比較**は帰属を確認。本件の核は公式＋ヘルプで足りる前提。 |

**よくある誤読:**

- **「Enterprise なら即オン」** → **既定オフ**（ヘルプ）。管理者が有効化する前提。
- **「EKM 顧客も使える」** → **ローンチ時は未提供**（ヘルプ）。対象外。
- **「Rippling のように週 5〜6 時間削れる」** → 事例紹介であり、**一般化された効果測定ではない**。
- **「カスタム GPT を今すぐ移すべき」** → 変換 UI は **Soon**。**急いで移さない**のが安全。

---

## 4. 本編に入る前のチェックリスト（任意）

**契約・対象**

- [ ] **対象プラン**（Business／Enterprise／Edu／Teachers）に該当するか
- [ ] **EKM 利用ワークスペース**でないか（該当だとローンチ時は未提供）
- [ ] **2026-05-06 以降のクレジット課金**を予算・契約の追跡対象に入れているか

**統制・運用**

- [ ] **Enterprise 管理者による有効化**のフローを誰が主に握るか決まっているか
- [ ] **Compliance API** の**対象範囲と粒度**が既存の監査要件と揃っているか
- [ ] **エージェント停止**の**発火手段**（誰が・どのログで判断するか）を紙で書いているか
- [ ] **共有コンテキスト**（誰が触れるか）が**人事・情報区分**の単位で描けているか

**資産・移行**

- [ ] **既存 GPTs** は**変換 UI（Soon）が出るまで並存**の前提で運用しているか
- [ ] **コネクタ／MCP** の許可リストとログの保持先が決まっているか
- [ ] **エージェント所有アカウント**と**エンドユーザーアカウント**の認証設計を分けているか

**安全**

- [ ] **プロンプトインジェクション**や**意図しない書き込み**のシナリオで**停止・復旧手順**をドライラン済みか
- [ ] **共有接続＋Slack** 等で、**他者がトリガーした際の影響**をレビュー済みか

---

※本補助は公開ページへのリンクにもとづきます。**投資助言や契約・法務の代行ではありません。** 機能・地域・契約条件は変更されうるため、導入判断は**最新の利用規約と管理者向け資料**で確認してください。
