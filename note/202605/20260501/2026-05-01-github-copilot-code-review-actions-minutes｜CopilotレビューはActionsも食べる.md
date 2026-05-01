# GitHub Copilot code review｜AIのレビューは、Actionsの請求にもつながる

## はじめに

GitHub は 2026年4月27日、**GitHub Copilot code review** の課金に関する変更を公式 Changelog で案内しました。

ポイントは、2026年6月1日から、プライベートリポジトリで Copilot code review を実行すると、Copilot 側の AI Credits に加えて、**GitHub Actions の所要分も消費する**ようになることです。

公開リポジトリについては、GitHub Actions 分はこれまでどおり無料と説明されています。つまり今回の話は、主に「プライベートリポジトリで Copilot にコードレビューを任せている人・組織」が見るべき変更です。

※本記事は GitHub の公開情報をもとにした一般的な整理です。請求・契約・税務の判断は、GitHub の最新ドキュメント、自社の契約、購買・法務・経理の判断を必ず確認してください。

---

## この記事での用語

| 用語 | 本記事での意味 |
|------|----------------|
| Copilot code review | Pull Request などに対して、GitHub Copilot がレビューコメントを出す機能 |
| GitHub Actions | GitHub 上で CI や自動処理を動かす仕組み |
| runner | GitHub Actions の処理を実際に動かす実行環境 |
| GitHub-hosted runner | GitHub 側が用意する runner |
| self-hosted runner | 利用者側が用意・管理する runner |
| AI Credits | 2026年6月1日からの Copilot 利用量課金で使われる単位 |
| PRU | 変更前の Copilot premium request unit。2026年6月1日まではこの枠で扱われると説明されている |

---

## 1. 何が変わるのか

先に結論です。

- 2026年6月1日から、Copilot code review は **AI Credits** の対象になる
- 同じく 2026年6月1日から、プライベートリポジトリでのレビュー実行は **GitHub Actions 分も消費**する
- 公開リポジトリでは、Actions 分はこれまでどおり無料
- 2026年6月1日までは、従来どおり PRU の枠で扱われ、Actions 分は消費しない
- self-hosted runner を使う場合、GitHub Docs では **GitHub Actions 分を消費しない**と説明されている

一言でいうと、  
**Copilot のコードレビューは「AIの利用料」だけでなく、「実行するためのインフラ利用」も意識する段階に入る**、という話です。

---

## 2. 公式情報ベースの要点

### 2-1. 2種類の課金が同時に出てくる

GitHub の Changelog では、2026年6月1日から Copilot code review が次の2つの形で扱われると説明されています。

1つ目は、Copilot の利用そのものが **AI Credits** として計上されることです。GitHub Docs では、Copilot のやり取りは入力・出力・再利用される文脈などの token に応じて AI Credits に換算されると説明されています。

2つ目は、プライベートリポジトリでコードレビューを実行する場合、**GitHub Actions の分数が既存プランの枠から消費される**ことです。枠を超えた分は、通常の GitHub Actions 料金として扱われます。

ここで混同しやすいのは、AI Credits と GitHub Actions 分が同じものではない点です。Copilot のモデル利用と、レビューエージェントを動かす実行基盤は、別の観点で見たほうが安全です。

### 2-2. プライベートリポジトリが主な対象

今回の Actions 分の話で重要なのは、対象が **プライベートリポジトリで実行されるレビュー**だという点です。

GitHub は Changelog で、公開リポジトリについては GitHub Actions 分が無料のままであると説明しています。

そのため、OSS など公開リポジトリ中心の利用者と、社内システム・受託開発・プロダクトコードをプライベートリポジトリで管理する組織では、受ける影響がかなり違います。

社内のプライベートリポジトリで「PR が出たら Copilot にレビューさせる」運用を広げている場合、6月以降は GitHub Actions の利用量にも目を向ける必要があります。

### 2-3. runner の選び方がコストと運用に効く

GitHub Docs では、Copilot code review は既定では GitHub-hosted runner を使うと説明されています。

一方で、self-hosted runner を使う場合は GitHub Actions 分を消費しないとも書かれています。ただし、self-hosted runner を使えば単純に楽になる、という話ではありません。

同じ GitHub Docs では、Copilot code review の self-hosting について、ARC（Actions Runner Controller）が公式にサポートされる手段であり、セキュリティ上の理由から非 ARC の self-hosted runner は使わないよう警告されています。また、Ubuntu x64 Linux runner との互換性や、ネットワーク制御の設定も前提になります。

つまり、self-hosted runner はコスト回避の選択肢になりえますが、同時に運用・セキュリティ・保守の責任を自分たちで引き受ける選択でもあります。

---

## 3. データ利用の話とは分けて読む

GitHub Copilot については、2026年4月24日からの規約・プライバシー更新も話題になりました。Copilot Free / Pro / Pro+ の対話データが、オプトアウトしない限りモデル改善に利用されうる、という論点です。

ただし、今回の code review の話は、それとは別です。

| 論点 | 見るべきポイント |
|------|------------------|
| データ利用 | Copilot に入力した内容が、AI モデルの改善に使われるか |
| 請求 | Copilot の利用が AI Credits や GitHub Actions 分としてどう計上されるか |
| runner | レビュー処理を GitHub-hosted で動かすか、自社側で動かすか |

同じ Copilot の話なので混ざりやすいですが、実務では分けて確認したほうがよいです。

「データ利用はオプトアウト済みだから大丈夫」と思っていても、請求設定や Actions の利用量は別に確認が必要です。逆に「料金が変わるからデータ利用も変わる」と読むのも短絡です。

---

## 4. まず確認したいチェックリスト

6月1日までに、最低限ここは見ておきたいです。

1. 自分または組織の Copilot プランを確認する
2. プライベートリポジトリで Copilot code review を使っているか確認する
3. GitHub Actions の現在の利用量と残り枠を確認する
4. Copilot code review の実行頻度を確認する
5. 請求の budget や spending limit が現実的か確認する
6. `copilot-pull-request-reviewer` 関連の workflow を GitHub Actions metrics や Billing usage report で追えるようにする
7. self-hosted runner を検討する場合は、コストだけでなくネットワーク制御・保守・セキュリティ責任も見積もる

特に組織利用では、開発チームだけで完結しにくい話です。請求管理者、エンジニアリング責任者、セキュリティ担当が同じ前提を持てるようにしておくのが大事です。

---

## 5. 短期・中期・長期で見る影響

ここでは時間軸を次のように置きます。

- **短期**: 2026年6月1日から約3か月
- **中期**: 3か月〜1年
- **長期**: 1年以上

### 5-1. 短期：予想外の Actions 消費に気づく時期

短期では、プライベートリポジトリで Copilot code review を多く使っている組織ほど、GitHub Actions の消費量に変化が出る可能性があります。

ただし、GitHub が「1回のレビューで何分」といった単純な目安を出しているわけではありません。実際の影響は、Pull Request の数、レビュー実行の頻度、既存の Actions 利用量、runner の種類に左右されます。

公開リポジトリ中心の人や、Copilot code review をほとんど使っていない人は、Actions 側の影響は限定的です。

### 5-2. 中期：レビュー運用と予算管理がセットになる

中期では、「どのリポジトリで自動レビューを使うか」「どこまでを Copilot に任せるか」「予算アラートをどの単位で見るか」といった運用設計が必要になります。

特に Copilot Business / Enterprise では、GitHub Docs 上で AI Credits が組織や Enterprise の請求単位でプールされる説明があります。さらに既存顧客向けには、2026年6月1日から9月1日までの初期期間に含まれる AI Credits が多めに設定される記載もあります。

一方で、Actions 分は別の観点で見なければなりません。AI Credits の枠に余裕があっても、Actions の枠や予算が別に効いてくる可能性があります。

### 5-3. 長期：AIエージェントはCIの一部として扱われる

長期では、AI によるコードレビューは「チャット機能」ではなく、CI や自動化基盤の一部として扱われていく可能性があります。

これは悪い話だけではありません。レビューの品質向上、見落としの減少、チーム横断の基準づくりには役立つ可能性があります。

ただし、AI エージェントがリポジトリ全体の文脈を見に行き、実行環境を使い、複数の処理を行うなら、その分のコストと権限設計も必要になります。

「便利だからオンにする」から、「どの範囲で、どの予算で、どの責任分界で使うか」へ。今回の変更は、その移行を分かりやすく見せた例だと思います。

---

## 6. 向いている対応 / 様子見でよいケース

### 向いている対応

- プライベートリポジトリで Copilot code review を使っているチームは、6月1日前に利用量と budget を見る
- 組織利用では、請求管理者と開発責任者に今回の変更を共有する
- 自動レビューを広げる前に、対象リポジトリと runner 方針を決める
- self-hosted runner を検討する場合は、ARC・ネットワーク制御・保守体制まで含めて判断する

### 様子見でよいケース

- 公開リポジトリ中心で、プライベートリポジトリの Copilot code review を使っていない
- Copilot code review を手動でたまに使う程度で、Actions の利用枠に十分余裕がある
- まずは6月以降の実績データを見てから運用を決めたい

様子見でよい場合でも、設定画面と請求画面の場所だけは先に確認しておくと安心です。

---

## 7. まとめ

今回の変更で大事なのは、Copilot code review を「AIの機能」としてだけ見ないことです。

**2026年6月1日以降、プライベートリポジトリでの Copilot code review は、AI Credits と GitHub Actions 分の両方で見ていく必要があります。**

データ利用の設定、Copilot の利用量、GitHub Actions の消費量、runner の選び方。これらは似ているようで別の論点です。

まずは自分や自社の GitHub で、次の3つだけ確認しておくのが現実的です。

1. Copilot code review をどのリポジトリで使っているか
2. GitHub Actions の現在の利用量と budget はどうなっているか
3. 6月以降も GitHub-hosted runner のままでよいか

便利なレビュー機能を止める話ではなく、**便利さを予算と運用の中に入れる話**として読むのがよさそうです。

---

## 参考情報（一次情報）

- [GitHub Changelog: GitHub Copilot code review will start consuming GitHub Actions minutes on June 1, 2026](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/)
- [GitHub Docs: Models and pricing for GitHub Copilot](https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing#github-actions-minutes-for-code-review)
- [GitHub Docs: Usage-based billing for individuals](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals)
- [GitHub Docs: Usage-based billing for organizations and enterprises](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises)
- [GitHub Docs: Configuring runners for GitHub Copilot code review](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-runners)

---

## 免責

本記事は公開情報をもとにした一般的な整理であり、GitHub の契約、請求、税務、法務上の助言ではありません。実際の料金・適用条件・契約上の扱いは、GitHub の最新ドキュメント、自社の契約内容、社内規程に従って確認してください。
