# 報告資料: Copilot code review と GitHub Actions 分の課金（2026-06-01）

- **調査日**: 2026-05-01
- **主出典**: [GitHub Changelog — GitHub Copilot code review will start consuming GitHub Actions minutes on June 1, 2026](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/)
- **要約（1文）**: **2026年6月1日**から、プライベートリポジトリでの Copilot code review は **GitHub-hosted runner 上の実行として GitHub Actions の所要分がプラン枠から消費**され、Copilot 側は **AI Credits ベースの利用課金**とも併せて計上される一方、**公開リポでは Actions 分はこれまでどおり無償**という公式告知である。

---

## 1. 背景 — なぜ今この情報が出ているか

- **事実（時系列）**:
  - GitHub は Copilot code review が **エージェント型ツール呼び出し**により広いリポジトリ文脈を参照できる構成であり、その実行基盤が **GitHub Actions（GitHub-hosted runners）** 上にあることについて、先行して説明している（Changelog 本文）。
  - **2026年4月27日**付の Changelog で、**2026年6月1日**から課金メーターの取り扱いが変わる旨を公表した。
  - **2026年6月1日まで**は従来どおり Copilot の **premium request unit（PRU）枠**のみからコードレビュー利用がカウントされ、**GitHub Actions 分は消費しない**（公式）。
  - GitHub Docs の同一テーマでは、**セルフホステッド runner は Actions 所要分を消費しない**、**ラージ runner は標準 runner と異なる料金**などが補足されている。また **2026年6月1日以降**、請求レポート上の `workflow_path` の値が変わる旨が記載されている。

- **公開情報から読み取れる動機**:
  - Changelog に「請求に関わる変更は顧客にとって重要だから **早期に共有して計画・準備の時間を確保したい**」という旨が明示されている。

- **補足・推測（根拠付き）**:
  - Copilot 全体が **2026年6月1日**からリクエスト課金から **usage-based（AI Credits）** への移行が進む件と、このコードレビュー×Actions の変更が時期を共にしている（GitHub Docs の IMPORTANT 注記）。**コスト構造を Actions と AI Credits の両軸で揃える意図がある可能性**はあるが、GitHub が経営判断の詳細を述べているわけではないため断定しない。

---

## 2. 目的 — 誰に、何をしてほしいか

| 想定読者 | 発信側が望む行動（推定） | note 読者への実務的示唆 |
|----------|---------------------------|-------------------------|
| **個人開発者（Copilot Pro／Pro+）** | Actions の利用実態と上限を確認し、Copilot と Actions のモニタリング手段を把握する | **請求設定・Actions の所要分トレンド**を見て、レビュー自動実行の頻度や対象リポを見直す |
| **組織の請求／プラットフォーム管理者（Teams／Enterprise）** | **budget／支出上限**を見直し、Copilot と Actions のメトリクス・請求レポートで監視する | **6/1 前にエンジニアリング責任者へ周知**し、`copilot-pull-request-reviewer`（および移行後のパス）でフィルタした利用をベースライン化する |
| **レビュー運用を決める開発チーム** | プライベートリポでの code review が Actions と結びつくことを理解し、runner 構成（hosted／self-hosted／large）を確認する | **セルフホステッド runner で Actions 分を避けられる公式記述**があるため、コスト要件次第で構成検討の選択肢になる |
| **`note` 底稿読者（規約・データ利用とセットで読んでいる人）** | （プライバシー告知とは別ストリームだが）Copilot の「使い方ごとのコスト」が増えるので計画を更新する | **データ利用（opt-out）と請求（Actions／AI Credits）は別問題**としてレイヤーを分けて説明すると誤読が減る |

---

## 3. 効果 — 短期・中期・長期の予想

時間軸の定義:

- **短期**: **2026年6月1日から約3か月**（〜2026年8月末頃までを目安）
- **中期**: **約3か月〜1年**（〜2027年春頃までを目安）
- **長期**: **1年以上**

- **短期（0〜3か月）**:
  - **予想される効果**: プライベートリポで code review を多用する組織で **GitHub Actions の所要分枯渇や予期せぬ請求**が表面化する可能性。請求ダッシュボードで **workflow フィルタ**を使った可視化ニーズが一時的に増える可能性（公式が手順を提示）。
  - **不確実性**: 組織ごとのレビュー回数・PR ボリューム・既存 Actions 利用率は公開データがない。**1 回あたりの所要分**の感覚値は公式が簡潔な数値で公表しているわけではない（本ブリーフでは数値推定しない）。
  - **効果が出ない条件**: code review をほとんど使わない、または公開リポのみで運用している場合は **Actions 側のインパクトは限定的**（公式どおり）。

- **中期（3か月〜1年）**:
  - **予想される効果**: CI と Copilot の **予算統合・ガバナンス**（どのリポで自動レビューを既定 ON にするか、バジェットアラートの設計）が標準運用に組み込まれるチームが増える可能性。
  - **不確実性**: GitHub がメータリングや UI を追加変更する可能性。**請求レポートの `workflow_path` が変わる**旨は公式にあり、運用ドキュメントの追随コストが発生しうる。
  - **効果が出ない条件**: 早期にセルフホステッドへ寄せる、レビューを手動／別製品へ寄せるなどで **GitHub 上の課金イベント自体が減る**場合。

- **長期（1年以上）**:
  - **予想される効果**: 「エージェント型開発支援 = CI／クラウド実行資源とセットで計画する」という認識が定着する可能性（業界全体の説明フレームとしての一般化。**推測**）。
  - **不確実性**: 競合プラットフォームの価格・バンドル戦略、GitHub のプラン再編。
  - **効果が出ない条件**: 企業が Copilot code review を縮小・廃止し、別のレビュー自動化に移行した場合。

---

## 4. note 執筆メモ（任意）

- **フック案（1〜2文）**: 「Copilot のコードレビュー、**モデル token だけじなく GitHub Actions の分も食う**ようになる。プライベートリポ中心のチームほど **6月の請求に地味な抜け穴**が開きうる。」
- **検証が必要な一点（事実・数値・日付）**:
  - 自組織の **実効日は常に公式の現行ドキュメントで再確認**（特にタイムゾーンと「適用開始」の定義）。
  - **usage-based billing への移行**本文（個人／組織）と、コードレビュー条項の **前提条件が一致しているか**を、執筆時にリンク先で照合すること。
- **免責・注意**:
  - 請求・契約・税務の判断は **組織の購買・法務・税理**に任せる。本資料は公開情報の整理であり、GitHub の利用契約や個別見積の代替ではない。
- **`alerts-log.md:100` との関係**:
  - 底稿 `note/202603/20260327/【海外IT速報】GitHub規約更新（Copilotデータ利用方針）を実務目線で整理.md` は **データ学習／規約（2026-04-24 発効）** が主題。**本件は請求・インフラ消費**が主題。**同じ「Copilot を使う組織の checklist」に並べるのは有用だが、論点の混線に注意**。

---

## 5. 参照一覧

- [GitHub Changelog（2026-04-27）— Copilot code review / Actions minutes / 2026-06-01](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/)
- [GitHub Docs — Models and pricing for GitHub Copilot（GitHub Actions minutes for code review ほか）](https://docs.github.com/copilot/reference/copilot-billing/models-and-pricing#github-actions-minutes-for-code-review)
- [GitHub Docs — Usage-based billing for individuals](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals)（Docs 本文内リンク。執筆時に最新版を確認）
- [GitHub Docs — Usage-based billing for organizations and enterprises](https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises)
- [GitHub Docs — Configuring runners for GitHub Copilot code review](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/configure-runners)
- （関連・別件）Copilot のデータ利用・規約更新の一次: [GitHub Changelog（2026-03-25）— Privacy Statement / Terms / Copilot training](https://github.blog/changelog/2026-03-25-updates-to-our-privacy-statement-and-terms-of-service-how-we-use-your-data/)
