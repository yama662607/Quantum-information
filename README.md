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

---

## 🔧 Just のインストール

コマンドライン・タスクランナーである「**just**」（Justfileを実行するためのツール）の各OSでのインストール方法をまとめました。

### 1. macOS

macOSでは **Homebrew** を使うのが最も一般的で簡単です。

- **Homebrew:** `brew install just`
- **MacPorts:** `sudo port install just`

### 2. Windows

Windowsでは、パッケージマネージャー（winget, Scoop, Chocolatey）のいずれかを使うのがスムーズです。

- **winget** (Windows標準): `winget install casey.just`
- **Scoop:** `scoop install just`
- **Chocolatey:** `choco install just`

### 3. Linux

主要なディストリビューションの公式リポジトリに含まれています。

- **Ubuntu / Debian / Mint:** `sudo apt install just`
- **Fedora:** `sudo dnf install just`
- **Arch Linux:** `sudo pacman -S just`
- **Alpine Linux:** `apk add just`

### 4. 言語系パッケージマネージャー

特定の言語環境を構築している場合は、以下の方法でもインストール可能です。

- **Rust (Cargo):** `cargo install just`
- **Python (pip):** `pip install rust-just`
- **Node.js (npm):** `npm install -g just-install`

### 5. インストールの確認

インストールが完了したら、以下のコマンドでバージョンが表示されるか確認してください。

```bash
just --version
```

### Tips: シェルの補完設定

`just` は入力補完（Tabキーでの補完）を生成する機能を持っています。例えば、zshをお使いの場合は以下のように設定に追加できます。

```bash
# zshの場合（~/.zshrc に追記）
source <(just --completions zsh)
```

## 📂 ディレクトリ構成

- `docs/`: Quarto ドキュメントのソースコード。
  - `notes.qmd`: **唯一のエントリーポイント**。すべての講義ノートはここに統合されています。
  - `index.qmd`: 学習ロードマップを表示するトップページ。
  - `notes/`: `notes.qmd` から include される分割ファイル（各章・節）。
- `apps/`: 可視化用の Streamlit アプリケーション。
- `notebooks/`: 実験用の Jupyter Notebook。
