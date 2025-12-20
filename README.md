# Quantum Information Study Notes

このリポジトリは、John Watrous 教授の著作 "The Theory of Quantum Information" をベースにした学習ノートとリソースを管理しています。

## 🚀 クイックスタート

[uv](https://github.com/astral-sh/uv) と [Just](https://github.com/casey/just) がインストールされていることを確認してください。

```bash
# 1. 依存関係のインストール
uv sync

# 2. ドキュメントのプレビュー (プレビューサーバーが起動します)
just docs

# 3. コード品質のチェック (フォーマット, Lint, Mermaid検証)
just check
```

## 🛠️ 技術スタック

- **[Quarto](https://quarto.org/)**: 技術文書の出版・ドキュメンテーションシステム。
- **Python (uv)**: 依存関係管理とスクリプティング。
- **Just**: コマンド操作を標準化するためのタスクランナー。

## 📂 ディレクトリ構成

- `docs/`: Quarto ドキュメントのソースコード。
  - `notes.qmd`: **唯一のエントリーポイント**。すべての講義ノートはここに統合されています。
  - `index.qmd`: 学習ロードマップを表示するトップページ。
  - `notes/`: `notes.qmd` から include される分割ファイル（各章・節）。
- `apps/`: 可視化用の Streamlit アプリケーション。
- `notebooks/`: 実験用の Jupyter Notebook。
