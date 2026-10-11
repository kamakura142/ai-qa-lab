# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## このリポジトリについて

QAエンジニアの個人学習用リポジトリ。Python・pytest・Playwright を初級から学ぶ。
利用者は学習中の初心者なので、「動くコード」だけでなく「理解できるコード・説明」を優先する。

## 応答・説明のルール

- **説明は日本語で行う。**
- **結論を先に書く。** 理由や詳しい説明はその後に続ける。
- **専門用語には一言の説明をつける。**
  例：「fixture（フィクスチャ：テストの前準備・後片付けをまとめて書く仕組み）」
- 一度に多くの新しい概念を詰め込まず、必要なものから段階的に説明する。

## コードを書くときのルール

- **初心者向けに、コメントを多めにつける。**
  - 各関数・テストの冒頭に「何を確認するのか」を書く。
  - 新しい文法・ライブラリの機能が初めて出てくる行には、その役割をコメントで説明する。
  - コメントも日本語で書く。
- 短く巧妙な書き方より、読みやすく素直な書き方を選ぶ。

## よく使うコマンド

```bash
pytest                                   # すべてのテストを実行
pytest tests/test_sample.py              # 1ファイルだけ実行
pytest tests/test_sample.py::test_name   # 1つのテスト関数だけ実行
pytest -v                                # テスト名を1件ずつ詳しく表示
playwright install                       # Playwright が使うブラウザをダウンロード（初回のみ）
pytest --headed                          # （pytest-playwright 使用時）ブラウザ画面を表示して実行
```

## 現状

作成時点ではリポジトリは空で、ディレクトリ構成・依存関係ファイル（requirements.txt 等）はまだない。
構成が決まったらこのファイルを更新すること。
