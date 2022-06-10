# tepraPy
Windows 環境で TEPRA ソフトウェア（SPC10）の API を使用して印刷する

## バージョン履歴
### v0.1 (2022-06-10)

## なぜ作ったのか
Microsoft Store から簡単に Python が利用できるようになり、既に PC から TEPRA の印刷をしている環境で、そのまま Python からも印刷ができるようになると便利だと思ったため。

## 使用方法
1. [TEPRA の公式サイト](https://www.kingjim.co.jp/download/tepra/)からラベル印刷ソフトウェア（SPC10）をインストールし、ソフトウェアから正常にラベル印刷ができる状態にしてください。
2. env-sample.txt を複製し、ファイル名を .env に変更してください。
3. .env の各設定値を必要に応じて変更してください。（下記の環境設定値参照）

#### 設定値
- TPRPY_SPCPATH ... SPC10.exe のパス（必須）
- TPRPY_LBLPATH ... ラベルファイルのパス（省略可能）
- TPRPY_CSVPATH ... 生成、インポートする CSV ファイルのパス（省略可能）

### サンプルコード
```

```