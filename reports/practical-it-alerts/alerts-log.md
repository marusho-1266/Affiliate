# 実務ITアラート調査ログ（累積）

このファイルは **`practical-it-alerts`**（`/practical-it-alerts`）の実行ごとに**追記**する。

**対象:** 期限・失効・EOS、公式手順の更新、国内を含むベンダ／当局の実務向け告知など。採用基準は `alerts-policy.md`。

**重複排除:** 各トピックの**主出典 URL** を `seen-urls.json` に記録する（正規化ルールはコマンド `.cursor/commands/practical-it-alerts.md` に従う）。

---

## 調査 2026-04-23 12:00 （JST）

調査の前提: 直近8週間の `note/**`（`note/Druft/` 除外）を目安に、期限・EOS・国内公式周知の実務フックを優先して収集。

### トピック

#### OS・ファーム

- **セキュアブート用 Microsoft 証明書（2011 世代）の期限** — 2011 年版の KEK／UEFI CA などは **2026 年 6 月**、Windows Production PCA 2011 は **2026 年 10 月**に期限を迎え、未更新環境ではブート系のセキュリティ更新の継続に影響しうる、と公式が整理。**読者アクション:** Windows Update／OEM ファームの計画、PowerShell・レジストリで 2023 系への移行状況を**確認**。**期限・根拠日:** 6 月・10 月 2026（表記はブログ本文の失効表）。**出典:** [Windows IT Pro Blog (Tech Community)](https://techcommunity.microsoft.com/blog/windows-itpro-blog/act-now-securpire-in-june-2026/4426856)（**Editor’s note: 2026-01-14** に `MicrosoftUpdateManagedOptIn` 周りの明確化）

#### ライフサイクル

- **Windows 10 サポート終了の再確認** — 多くの Windows 10 エディションのサポートは **2025-10-14** に終了（移行先・**拡張セキュリティ更新 (ESU)** 等の選択は各組織のライセンス方針に従う）。**読者アクション:** 残存 10 端末の**棚卸し**と 11 移行・ESU の**計画**。**期限・根拠日:** 2025-10-14（EOS）。**出典:** [Microsoft Learn ライフサイクル](https://learn.microsoft.com/ja-jp/lifecycle/announcements/october-14-2025-products-end-of-support)

#### 国内・体制

- **長期休暇前の体制（2026 年度 GW）** — IPA が**ゴールデンウィーク**前の情報セキュリティ上の注意を案内（管理者不在時のインシデント対応遅延など）。**読者アクション:** 当番・監視・連絡体制を**休暇前に確認**。**期限・根拠日:** メールニュース **2026-04-20** 配信、GW 前に実務的な**カレンダー**が近い。**出典:** [IPA SECURITY ACTION](https://www.ipa.go.jp/security/security-action/mailnews/2026_4.html)

### note底稿のフォロー

- **【2026年問題】セキュアブート証明書** — 底稿は PowerShell／`UEFICA2023Status` 等の確認手順を整理済み。公式 **IT 向けガイダンス (KB 5062713)** が**変更履歴**で継続改訂されている。**底稿:** `note/202603/20260330/セキュアブート2026対応_説明資料.md`。**フォロー出典:** [Microsoft サポート](https://support.microsoft.com/ja-jp/topic/e2b43f9f-b424-42df-bc6a-8476db65ab2f)（**2026-02-13** 更新:「準備」に「サンプル信頼度データ」を追加、不要になった 1801/1808 用スクリプト記述を整理、**2026-02-03** に Hyper-V のイベント ID 1795 記載など）

### メモ（任意）

- **対象範囲:** 直近8週間の `note/20######/` 底稿。期限・手続きが明確なのは上記セキュアブートのみのため `### note底稿のフォロー` は1件。AI プロダクト解説系の多くの底稿は、本アラートの「期限」軸では今回採用見送り。

---

## 調査 2026-04-29 15:00 （JST）

調査の前提: 直近8週間の `note/**` を目安に、セキュアブート関連の公式 KB 変更履歴の確認と、ブラウザのリリース計画変更（カレンダー影響）を優先。

### トピック

#### OS・ブラウザ

- **Windows セキュリティでセキュアブート証明書の状態表示（KB 5087130）** — 2026 年 4 月以降、Windows セキュリティ「デバイスのセキュリティ」＞「セキュアブート」に更新状態の視覚的インジケーター（緑／黄／赤）が順次ロールアウト。5 月以降はファーム制限などで黄色警告の可能性、6 月頃からはブート関連の脆弱性状況により赤の可能性。**読者アクション:** 個人・小規模環境では **Windows 更新の適用後に同画面で状態を確認**し、Hyper-V／マネージド端末は IT 側ガイド（KB／ポリシー）に合わせる。**期限・根拠日:** UI 機能のロールアウトは **2026-04 以降**、黄色の追加は **2026-05 以降**、赤の可能性は早ければ **2026-06**（公式本文の記述）。**出典:** [Microsoft サポート（KB 5087130）](https://support.microsoft.com/ja-jp/topic/windows-%E3%82%BB%E3%82%AD%E3%83%A5%E3%83%AA%E3%83%86%E3%82%A3-%E3%82%A2%E3%83%97%E3%83%AA%E3%81%AE%E3%82%BB%E3%82%AD%E3%83%A5%E3%82%A2-%E3%83%96%E3%83%BC%E3%83%88%E8%A8%BC%E6%98%8E%E6%9B%B8%E3%81%AE%E6%9B%B4%E6%96%B0%E7%8A%B6%E6%85%8B-5ce39986-7dd2-4852-8c21-ef30dd04f046)（変更履歴 **2026-04-03** に表示文言の整理）

- **Chrome の安定版を2週間ごとに（2026年9月〜）** — Google は **Chrome 153 の安定版（2026-09-08 想定）** からデスクトップ・Android・iOS で **2 週間リリースサイクル**へ移行（Extended Stable は従来どおり 8 週間）。**読者アクション:** 社内ブラウザ更新・テスト・承認フローの **カレンダーと工数を再見積もり**。**期限・根拠日:** 移行開始 **2026-09**（公式ブログの表）。**出典:** [Chrome for Developers ブログ](https://developer.chrome.com/blog/chrome-two-week-release)

### note底稿のフォロー

- **セキュアブート IT 向けガイダンス（KB 5062713）** — 変更履歴に **2026-03-30**、「セキュアブート証明書の更新が Hyper-V の仮想マシンでイベント ID 1795 に失敗する」既知の問題が **解決** と記載（**2026-03-24** は同件の記述更新）。**底稿:** `note/202603/20260330/セキュアブート2026対応_説明資料.md`。**フォロー出典:** [Microsoft サポート（KB 5062713）](https://support.microsoft.com/ja-jp/topic/e2b43f9f-b424-42df-bc6a-8476db65ab2f)（変更履歴 2026-03-24・2026-03-30）

### メモ（任意）

- **対象範囲:** 直近8週間の `note/`。IPA の GW 注意単体ページは `-mailnews 2026_4` と同一キャンペーンのためトピックは重複見送り。セキュアブートの日本語解説記事（例: JP Windows Tech Support Blog 2026-04-10）は KB5087130 等と主題が重なるため今回は採用せず KB を主出典に統合。

---

## 調査 2026-04-30 14:45 （JST）

調査の前提: 直近8週間の `note/**`（`note/Druft/` 除外）を目安に、国内 IPA の CPU 周知・法人向け SaaS の課金切替日を優先。セキュアブート系 KB は変更履歴に新規追記がないため重複掲載は避ける。

### トピック

#### 国内・ミドルウェア

- **Oracle Java SE の 2026年4月 Critical Patch Update（IPA の整理）** — 2026年4月22日（日本時間）の Oracle 公表に伴い、Java SE 8 / 11 / 17 / 21 / 25 / 26 など複数ラインにセキュリティ更新があり、悪用時は異常終了や端末制御などのリスクとされる。**読者アクション:** 稼働中の JRE／JDK の**バージョン棚卸し**と、Oracle 公開の**修正レベルへの更新計画**を確認（商用はライセンスも合わせて確認）。**期限・根拠日:** 注意喚起ページ **公開 2026-04-22**（対処は「早急に適用」の公式表現ベース）。**出典:** [IPA — Oracle Java の脆弱性対策について(2026年4月)](https://www.ipa.go.jp/security/security-alert/2026/0422-jre.html)

#### SaaS・契約

- **ChatGPT のワークスペースエージェント（リサーチプレビュー）の無料期間終了予告** — Business／Enterprise／Edu／Teachers で提供中の workspace agents は**2026年5月6日まで無料**、同日から**クレジット制の課金**に移行すると OpenAI が明記。**読者アクション:** 利用中ワークスペースの**管理者がクレジット・上限・アラート設定を事前に確認**し、試用から本番運用への契約・予算を**計画**。**期限・根拠日:** **2026-05-06**（公式ブログ「Availability and pricing」）。**出典:** [OpenAI — Introducing workspace agents in ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)（**April 22, 2026**）

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**`。ワークスペースエージェントは底稿 `note/202604/20260423/` に同一公式の 5/6 記載があるが、**KB5062713・KB5087130 の変更履歴は 2026-04 以降の追記なし**（前回調査と同一）、セキュアブートは再掲しない。
- **IPA:** 「GW に関する注意喚起」単独ページは **メールニュース 2026_4** と同一キャンペーンのためトピック化せず。

---

## 調査 2026-05-01 16:30 （JST）

調査の前提: 直近8週間の `note/**`（`note/Druft/` 除外）を目安に、KB5062713・5087130 の変更履歴はライブ確認のみ（2026年4月末以降の追記なし）。GitHub Copilot の発効日・請求変更と IPA の Microsoft 月例（悪用確認済み CVE）を優先。

### トピック

#### SaaS・開発プラットフォーム

- **GitHub Copilot Free／Pro／Pro+ の対話データとモデル学習（規約・プライバシー更新の発効）** — **2026年4月24日**より、オプトアウトしない限り Copilot Free／Pro／Pro+ の対話データ（入力・出力・コード断片・コンテキスト等）がモデル改善に利用されうる方針が**発効**（Business／Enterprise は対象外）。**読者アクション:** `github.com/settings/copilot` の **Privacy で「AI モデルのトレーニングへのデータ利用」を希望どおりか確認**（既にオプトアウト済みなら偏好は維持と公式記載）。**期限・根拠日:** **発効 2026-04-24**（変更告知 **2026-03-25**）。**出典:** [GitHub Changelog](https://github.blog/changelog/2026-03-25-updates-to-our-privacy-statement-and-terms-of-service-how-we-use-your-data/)

- **GitHub Copilot code review と GitHub Actions 分の課金開始** — **2026年6月1日**から、プライベートリポジトリ上の Copilot code review は **GitHub Actions の所要分がプランに含まれる枠から消費**され、超過分は通常の Actions 料金（公開リポは無償のまま）。Copilot Pro／Pro+／Business／Enterprise が対象。**読者アクション:** **請求管理者が Actions／Copilot の利用見込み・予算・上限を 6/1 前に確認**し、レビュー運用チームへ共有。**期限・根拠日:** **2026-06-01**（告知 **2026-04-27**）。**出典:** [GitHub Changelog](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/)

#### 国内・ベンダ

- **Microsoft 製品の脆弱性対策（2026年4月月例・IPA）** — **2026年4月15日**公表の月例に含まれる **CVE-2026-32201（SharePoint Server なりすまし）について Microsoft が悪用を確認済み**とIPAが整理。**読者アクション:** Windows Update／更新管理プロセスで **当該月例の適用状況を棚卸し**し、未適用なら**優先展開**。**期限・根拠日:** 注意喚起 **公開 2026-04-15**（対処は「至急適用」の公式表現ベース）。**出典:** [IPA — Microsoft 製品の脆弱性対策について(2026年4月)](https://www.ipa.go.jp/security/security-alert/2026/0415-ms.html)

### note底稿のフォロー

- **GitHub 規約・Copilot データ利用** — 底稿は **2026/4/24** 発効の学習利用を整理済み。**フォロー出典:** [GitHub Changelog（Copilot code review の Actions 課金）](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/)（**2026-04-27** 公開、**2026-06-01** からプライベートリポで Actions 分を消費）。**底稿:** `note/202603/20260327/【海外IT速報】GitHub規約更新（Copilotデータ利用方針）を実務目線で整理.md`

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**`。セキュアブート KB は変更履歴に新規追記なし（既出 URL のためトピック再掲なし）。

---

## 調査 2026-05-02 11:15 （JST）

調査の前提: 直近8週間の `note/**`（`note/Druft/` 除外）を目安に、IPA の新規注意喚起を確認。`alerts-log.md` 未掲載の Adobe 整理ページをバックログとして補完。セキュアブート KB（5062713・5087130）は変更履歴に **2026-05-02 時点で 2026 年 4 月以降の新規追記なし**。

### トピック

#### 国内・オープンソース・デスクトップ

- **Linux カーネル権限昇格（CVE-2026-31431、Copy Fail）** — ローカル一般ユーザー前提の権限昇格で PoC が既に公開されており、他脆弱性との連鎖や共有カーネル環境（コンテナ等）での影響が懸念と IPA が整理。**読者アクション:** 稼働中ディストリビューションの**セキュリティアドバイザリを確認**し、提供された**カーネル／パッチを優先適用**（回避策はベンダ指示に従いテスト）。**期限・根拠日:** 注意喚起 **公開 2026-05-01**（対処は「迅速適用」の公式表現ベース）。**出典:** [IPA — Linuxの脆弱性対策について(CVE-2026-31431、Copy Fail)](https://www.ipa.go.jp/security/security-alert/2026/alert20260501.html)

- **Adobe Acrobat／Reader（2026年4月セキュリティ更新・IPA）** — **2026年4月11日（JST）** の Adobe 公表に伴い複数 CVE、うち **CVE-2026-34621 は Adobe が悪用確認済み**と IPA が整理。**読者アクション:** Continuous／Classic 2024 の**版数棚卸し**と**至急更新**（更新管理している組織は配布遅れがないか**確認**）。**期限・根拠日:** 注意喚起 **公開 2026-04-13**・Adobe 更新 **2026-04-11（JST）**。**出典:** [IPA — Adobe Acrobat および Reader の脆弱性対策について(2026年4月)](https://www.ipa.go.jp/security/security-alert/2026/0413-adobereader.html)

### メモ（任意）

- **対象範囲:** 直近 8 週間の `note/**`。`2026-05-01-github-copilot-code-review-actions-minutes`・Anthropic Claude Security 底稿は**期限・公式手順の新規明確化**が今回取れず、`### note底稿のフォロー` は省略。
- **ChatGPT ワークスペースエージェント無料終了（2026-05-06）** など **openai.com** 主出典は `seen-urls.json` 済みのため再掲しない（前回調査の `### トピック` 参照）。

---
