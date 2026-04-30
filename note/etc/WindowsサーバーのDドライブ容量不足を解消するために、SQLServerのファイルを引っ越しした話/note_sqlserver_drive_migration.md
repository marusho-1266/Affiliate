# WindowsサーバーのDドライブ容量不足を解消するために、SQLServerのファイルを引っ越しした話

## はじめに

私の担当環境の Windows サーバーでは、ディスク使用状況が次のとおりでした。

- C ドライブ：空き容量が 500 GB 以上ある
- D ドライブ：空きが約 20 GB まで減少している

C ドライブ側の空きを D に回す方法としてパーティションの再構成を考える場合、**物理ディスク上の並びや Windows の標準ツールの制約により、希望どおりに拡張できない**ことがあります。本記事では、そのような制約下でパーティション操作に頼らず、**SQL Server のデータファイル等を C ドライブへ移し、D ドライブの占有量を減らして空きを確保する**手順を整理します。

---

## なぜパーティション操作では解決しにくいのか

まず最初に検討しがちなのが、Windowsの「ディスクの管理」（diskmgmt.msc）を使ったパーティションの縮小・拡張です。

しかし、CドライブとDドライブが同じ物理ディスク上にある場合でも、**Cドライブを縮小してできる未割り当て領域はDドライブの「左側」に配置されます。**

```
【Cを縮小した後の状態】
[C: 縮小後] [未割り当て] [D: 20GB空き]
                ↑
         Dの左側に来てしまう
```

Windowsの標準ツールは「右隣に未割り当て領域がある場合のみ」しか拡張できない仕様のため、この構成ではDドライブを拡張できません。

サードパーティツール（MiniTool Partition Wizardなど）を使えばパーティションの移動・結合は可能ですが、本番サーバーへの適用はリスクを伴います。

---

## 現実的な解決策：SQLServerのファイルをCドライブに移動する

パーティション構成を変えずに済む、より安全なアプローチです。SQLServerのデータファイルを特定し、Cドライブに引っ越しすることでDドライブの空き容量を回復させます。

### 作業の基本的な流れ

1. 各DBの容量を確認して移動対象を絞る
2. 対象DBをオフラインにする
3. ファイルをCドライブにコピーする
4. SQL Server上のファイルパスを更新する
5. DBをオンラインに戻して動作確認する
6. 確認が取れたら旧ファイルを削除する

**1DBずつ順番に作業することを強く推奨します。** 問題が起きたときの切り分けがしやすく、他のDBへの影響を最小限に抑えられます。

---

## STEP 1：各DBの容量を確認する

まずSSMS（SQL Server Management Studio）で以下のクエリを実行し、どのDBがどれだけ容量を使っているか把握します。

### DB別・ファイル別の詳細確認

```sql
SELECT
    DB_NAME(database_id) AS DBName,
    type_desc AS ファイル種別,
    physical_name AS ファイルパス,
    ROUND(size * 8.0 / 1024, 1) AS サイズMB,
    ROUND(size * 8.0 / 1024 / 1024, 2) AS サイズGB
FROM sys.master_files
ORDER BY size DESC;
```

### DB単位の合計容量確認

```sql
SELECT
    DB_NAME(database_id) AS DBName,
    ROUND(SUM(size * 8.0 / 1024 / 1024), 2) AS 合計GB
FROM sys.master_files
GROUP BY database_id
ORDER BY 合計GB DESC;
```

結果の見方：
- **ROWS**：データファイル（.mdf / .ndf）
- **LOG**：ログファイル（.ldf）

容量の大きいDBが移行の優先候補です。まずは小さいDBで手順を確認してから、大きいDBに適用するのがおすすめです。

---

## STEP 2：対象DBのファイルパス・論理名を確認する

移動作業に必要な情報を取得します。

```sql
SELECT name AS 論理名, physical_name AS 物理パス, type_desc
FROM sys.master_files
WHERE database_id = DB_ID('対象DB名');
```

「論理名」はSTEP 4のALTER DATABASE文で使用します。必ず控えておきましょう。

---

## STEP 3：DBをオフラインにしてファイルをコピーする

```sql
-- DBをオフラインに
ALTER DATABASE [対象DB名] SET OFFLINE WITH ROLLBACK IMMEDIATE;
```

次に、コマンドプロンプトでファイルをCドライブにコピーします。

```cmd
robocopy "D:\SQLData" "C:\SQLData" 対象DB.mdf 対象DB.ldf /COPYALL
```

> **ポイント**：`/COPYALL` オプションで所有者・タイムスタンプ・ACLを含めてコピーできます。

---

## STEP 4：SQL Server上のファイルパスを更新する

ファイルを物理的にコピーしただけでは、SQL Serverはまだ旧パスを参照しています。必ずALTER DATABASE文で新しいパスを登録してください。

```sql
-- データファイルのパスを更新
ALTER DATABASE [対象DB名]
MODIFY FILE (NAME = '論理名_data', FILENAME = 'C:\SQLData\対象DB.mdf');

-- ログファイルのパスを更新
ALTER DATABASE [対象DB名]
MODIFY FILE (NAME = '論理名_log', FILENAME = 'C:\SQLData\対象DB.ldf');
```

---

## STEP 5：DBをオンラインに戻して動作確認する

```sql
-- DBをオンラインに
ALTER DATABASE [対象DB名] SET ONLINE;

-- パスが更新されているか確認
SELECT name, physical_name FROM sys.master_files
WHERE database_id = DB_ID('対象DB名');

-- DBが正常に使えるか確認
USE [対象DB名];
SELECT TOP 10 * FROM 任意のテーブル;
```

新しいパス（C:\SQLData\...）が表示され、データを正常に参照できることを確認してください。

---

## STEP 6：動作確認後に旧ファイルを削除する

動作確認が取れてから、Dドライブの旧ファイルを削除します。**確認前に削除しないことが鉄則です。**

```cmd
del "D:\SQLData\対象DB.mdf"
del "D:\SQLData\対象DB.ldf"
```

これでDドライブの空き容量が回復します。

---

## システムDBについて

master、model、msdb、tempdbといったシステムDBの移動は、SQL Serverサービスの停止が必要で手順も異なります。ユーザーDBの移動だけで十分な空き容量を確保できる場合は、**システムDBは触らない**ことを推奨します。

---

## 注意事項まとめ

- **作業前に必ずバックアップを取得すること**
- ALTER DATABASE文でのパス更新を忘れずに（物理コピーだけでは不十分）
- 旧ファイルの削除は動作確認が完全に取れてから
- 本番サーバーでの作業はメンテナンスウィンドウを設けて実施する
- 1DBずつ順番に作業することで、リスクを最小化できる

---

## おわりに

パーティション操作という「大手術」をせずとも、SQLServerのファイル移行という「引っ越し」で容量問題を解決できます。手順自体はシンプルで、1DBずつ丁寧に進めれば安全に実施できます。

同じような状況で困っている方の参考になれば幸いです。
