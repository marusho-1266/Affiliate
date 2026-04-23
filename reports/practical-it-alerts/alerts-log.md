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
