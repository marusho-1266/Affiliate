# Make で HNRSS → 要約 → Slack まで通す手順（レベル2・1フィード）

常時起動PCなしで動かす前提の、**最初の1本**として Hacker News（HNRSS）だけを Make に繋ぎ、**日本語要約を Slack に流す**までの手順です。  
判断・記事化・X投稿は人間が行う半自動のままにします。

---

## 1. この資料でできること・できないこと

| できること | まだやらないこと |
|------------|------------------|
| 新着RSS（HNRSS）を検知する | 複数フィードの統合・重複排除 |
| 記事タイトル・概要を AI で日本語要約する | WordPress 自動投稿 |
| 要約を Slack の指定チャンネルに投稿する | 完全自動での X 投稿 |

---

## 2. 事前に用意するもの

1. **Make（旧 Integromat）アカウント**  
   - [https://www.make.com](https://www.make.com) で登録。無料プランで試験可能（月間オペレーション上限あり）。

2. **Slack ワークスペース**  
   - 通知を流したいチャンネル（例：`#tech-news`）を作成できる権限。

3. **要約用の API キー（どちらか一方）**  
   - **OpenAI**：API キー（[https://platform.openai.com](https://platform.openai.com)）  
   - **Anthropic（Claude）**：API キー（[https://console.anthropic.com](https://console.anthropic.com)）  

4. **RSS の URL（今回は1本だけ）**  
   - Hacker News フロントページ用：  
     `https://hnrss.org/frontpage`

---

## 3. Slack 側の準備（Make から投稿できるようにする）

### 3.1 推奨：Make の「Slack」モジュールで接続する

1. Slack で通知用チャンネルを作成（例：`#tech-news`）。
2. Make のシナリオで Slack モジュールを初めて使うとき、**Connect** から OAuth でワークスペースと接続します。
3. 接続後、**Create a message**（メッセージ投稿）でチャンネルを指定できるようにします。

### 3.2 代替：Incoming Webhook を使う場合

ワークスペース方針でアプリ追加が難しい場合は、Slack の Incoming Webhook URL を取得し、Make の **HTTP > Make a request** で `POST` する方法もあります（この資料では主に 3.1 を想定）。

---

## 4. Make でシナリオを作成する

### 4.1 新規シナリオを作成

1. Make にログインし、**Scenarios** → **Create a new scenario**。
2. 名前を付ける（例：`HNRSS → 要約 → Slack`）。

### 4.2 モジュール1：RSS（トリガー）

1. 最初のモジュールに **RSS** を追加（検索語：`RSS`）。
2. **Watch RSS feed items**（または同等の「RSS フィードの新着を監視」系）を選択。
3. 設定例：
   - **Feed URL**：`https://hnrss.org/frontpage`
   - **Maximum number of returned articles**：試しに **5** など小さめ（初回やテスト時のオペレーション節約のため）。

4. **Schedule**（シナリオ全体の実行間隔）を設定。  
   - 例：**Every 15 minutes** または **Every 1 hour**（無料枠・API コストとの兼ね合いで調整）。

5. **Run once** で接続テストし、サンプルで `title` / `link` / `content`（または `description`）などが取れることを確認。

### 4.3 モジュール2：AI で要約（HTTP モジュール）

RSS モジュールの直後に **HTTP > Make a request** を追加します。

#### OpenAI（Chat Completions）の例

| 項目 | 設定の目安 |
|------|------------|
| URL | `https://api.openai.com/v1/chat/completions` |
| Method | `POST` |
| Headers | `Authorization`：`Bearer <あなたのAPIキー>`、`Content-Type`：`application/json` |
| Body type | Raw / JSON |

**Body（JSON）の例**（Make 上ではマッピングで RSS の値を差し込む）：

```json
{
  "model": "gpt-4o-mini",
  "messages": [
    {
      "role": "system",
      "content": "あなたはITニュースを日本語で簡潔に要約するアシスタントです。箇条書き3点以内、最後に原文URLを1行で示してください。"
    },
    {
      "role": "user",
      "content": "タイトル：{{1.title}}\nURL：{{1.link}}\n概要：{{1.content}}"
    }
  ],
  "max_tokens": 500
}
```

- `{{1.title}}` の **1** は、Make では「1番目のモジュール」を指すことが多いですが、実際のシナリオでは UI の **マッピングパネル** から該当フィールドをクリックして差し込むと安全です。
- レスポンスは `choices[0].message.content` に要約テキストが入ります（後続の Slack で参照）。

#### Anthropic（Messages API）の例

| 項目 | 設定の目安 |
|------|------------|
| URL | `https://api.anthropic.com/v1/messages` |
| Method | `POST` |
| Headers | `x-api-key`：APIキー、`anthropic-version`：`2023-06-01`、`Content-Type`：`application/json` |

Body は Anthropic のドキュメントに沿った JSON とし、ユーザメッセージに RSS の `title` / `link` / 概要をマッピングします。

**API キーの置き場所**：Make の **Connections** や各 HTTP モジュールのヘッダに直書きせず、可能なら **Make の変数 / データストア** やモジュール内の認証欄を使い、共有シナリオにキーを残さない運用を推奨します。

### 4.4 モジュール3：Slack に投稿

1. **Slack > Create a message** を追加。
2. 接続したワークスペース・チャンネルを選択。
3. **Text** に、HTTP モジュールの応答から要約文をマッピング：
   - OpenAI の場合：パース用に **JSON > Parse JSON** を挟むか、Make の組み込みパーサで `choices[0].message.content` を参照。
4. 必要なら **元記事 URL**（RSS の `link`）を同じメッセージに追記。

初回は **要約が空にならないか**、**文字数制限で切れていないか** を Slack で確認します。

---

## 5. 動作確認の順序

1. **RSS だけ**実行 → 新着が1件以上取れるか。
2. **RSS → HTTP** まで実行 → API のエラー（401/429 等）がないか、レスポンスに要約があるか。
3. **最後まで**実行 → Slack に意図した内容が届くか。

エラーが出た場合の典型：

| 症状 | 確認すること |
|------|----------------|
| 401 / Unauthorized | API キー、ヘッダ名（`Bearer` のスペース含む） |
| 429 / Rate limit | 実行間隔を長くする、モデルを軽めにする |
| Slack に投稿されない | チャンネル ID、アプリのチャンネル参加、OAuth スコープ |
| 要約が英語のまま | system / user プロンプトを日本語出力明示に修正 |

---

## 6. 無料枠・コストの目安

- **Make**：プランにより **月間オペレーション数** に上限。1記事あたり「RSS取得＋HTTP＋Slack」で複数オペレーション消費する想定で、**スケジュールを詰めすぎない**。
- **OpenAI / Anthropic**：トークン課金。`gpt-4o-mini` や短い max_tokens で試すと負担が小さい。

---

## 7. 次の拡張（この資料の次のステップ）

- 同じシナリオを複製し、**Feed URL だけ** Dev.to / TechCrunch 等に差し替える（オペレーションが増えるので間隔調整）。
- **Notion** モジュールを追加し、同じ要約をデータベースに1行蓄積する。
- 取得・重複排除を **GitHub Actions ＋スクリプト** に移し、Make は Webhook 受信だけにする（レベル2＋3のハイブリッド）。

---

## 8. 参考リンク

- HNRSS（非公式 RSS）：[https://hnrss.org/](https://hnrss.org/)  
- Make ヘルプ（シナリオ・RSS）：Make 公式ドキュメント内で「RSS」「Scenario」を検索。  
- OpenAI API：[https://platform.openai.com/docs](https://platform.openai.com/docs)  
- Anthropic API：[https://docs.anthropic.com](https://docs.anthropic.com)  

---

*作成日：2026-03-29。Make / Slack / 各 API の画面仕様は変更されるため、名称が一致しない場合は近いモジュール名で同等の操作をしてください。*
