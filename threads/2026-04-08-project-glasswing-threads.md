# Threads 投稿文案（昼）— Anthropic「Project Glasswing」／Claude Mythos Preview

関連ブリーフ: `reports/note-briefs/2026-04-08-project-glasswing.md`  
関連記事（note）: `note/20260408/2026-04-08-project-glasswing-note.md`

夜分（note 公開告知）: 必要なら `threads/2026-04-08-project-glasswing-threads-evening.md` を別途作成

---

## 投稿1（メイン）

昼のITメモ ☀️

2026/4/7、Anthropic が Project Glasswing を公表しました。未公開の汎用フロンティアモデル 「Claude Mythos Preview」 を、一般向けには出さず、AWS・Google・Microsoft・Cisco・CrowdStrike・Linux Foundation・JPMorgan Chase などが名を連ねる ローンチパートナーの 防御的セキュリティ業務に回す、という設計です。

公式ページでは、過去数週間で ゼロデイ相当が数千件規模、主要OS・ブラウザにも及ぶ、と書かれ、OpenBSD や FFmpeg、Linux カーネル連鎖など 修正済みの例は Red Team ブログ側に詳細がある、という流れ。「強い探索能力」と「限定公開」がセットで語られています。

コミットは Mythos 向け利用クレジット最大1億ドル（up to $100M） と、OSS セキュリティ組織への寄付400万ドル。二重利用と時間競争（防衛側が先に載せる）のフレーミングがはっきりしています。

続く↓

---

## 投稿2（補足・注意）

補足：

CyberGym などの数値比較（例: 公式表で Mythos と Opus 4.6 の差）は、Anthropic が示した評価条件での自己報告です。「数千件」の内訳も 第三者がそのまま検証しにくいので、SNSの要約数字は盲信せず一次で原文確認が安全そうです。

現場目線では、パートナー外でも 「AI が短時間に広くスキャンしうる」前提で、公開サービス・古い依存・境界の広い API の優先度を見直す、がメモになりそうです。ベンダの強さの主張と 自社のデータ境界・ログ・委託は別レイヤ、という切り分けも効きます。

一次ソース：

[https://www.anthropic.com/glasswing](https://www.anthropic.com/glasswing)

（技術例・修正済み事例の一部）

[https://red.anthropic.com/2026/mythos-preview](https://red.anthropic.com/2026/mythos-preview)

（整合性・リスク評価）

[https://www.anthropic.com/claude-mythos-preview-risk-report](https://www.anthropic.com/claude-mythos-preview-risk-report)

---

## 1本にまとめたい場合（参考）

投稿1の「続く↓」を削除し、投稿2から 「自己報告ベンチマークは原文で」「現場は脅威モデルとデータ境界」 を1〜2文に圧縮し、リンクは Glasswing 1本だけに絞っても可。
