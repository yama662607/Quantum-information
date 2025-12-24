# Quantum Information Study Notes

このリポジトリは、John Watrous 教授の著作 "The Theory of Quantum Information" をベースにした学習ノートとリソースを管理しています。

## 🚀 クイックスタート (Quick Start)

リポジトリをクローンして、以下の手順で環境を構築・プレビューを開始できます。

```bash
# 1. リポジトリのクローン
git clone https://github.com/yama662607/Quantum-information.git
cd Quantum-information

# 2. 依存関係のインストールとセットアップ
just setup

# 3. プレビューサーバーの起動
just docs
```

ブラウザで `http://localhost:4312` にアクセスすると、編集内容がリアルタイムに反映されるプレビューを確認できます。

## 🤝 共同開発ガイド (Collaboration)

このプロジェクトは、人間とAIエージェントが協力して執筆することを前提に設計されています。

- **クロスプラットフォーム対応**: macOS, Linux, Windows どの環境でも `just` コマンドだけで同じワークフローが再現可能です。
- **環境チェック**: 何か問題が起きたら `just check-env` を実行してください。
- **品質管理**: 変更をプッシュする前に `just check` を実行し、リンターやバリデーションをパスすることを確認してください。
- **AIエージェントとの協調**: パートナーのAIエージェントにはまず [AGENTS.md](./AGENTS.md) を読むように指示してください。プロジェクト固有のルールや最新のワークフローが記載されています。

## 🛠️ 技術スタック

- **[Quarto](https://quarto.org/)**: 技術文書の出版・ドキュメンテーションシステム。
- **Python (uv)**: 依存関係管理とスクリプティング。
- **Just**: コマンド操作を標準化するためのタスクランナー。

## 🔧 セットアップガイド

このリポジトリを動かすには、[uv](https://github.com/astral-sh/uv) と [Just](https://github.com/casey/just) のインストールが必要です。

### 1. uv のインストール

Pythonの超高速パッケージ・プロジェクト管理ツールである **uv** のインストール方法です。

#### 推奨：スタンドアロン・インストーラー
OSを問わず、最も速く最新版を導入できる推奨される方法です。

- **macOS / Linux:**
  ```bash
  curl -LsSf https://astral.sh/uv/install.sh | sh
  ```
- **Windows:**
  ```powershell
  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
  ```

#### パッケージマネージャー経由
- **macOS (Homebrew):** `brew install uv`
- **Windows (winget):** `winget install astral-sh.uv`
- **Windows (Scoop):** `scoop install uv`
- **Linux:** `apk add uv` (Alpine), `pacman -S uv` (Arch)

#### 確認とアップデート
```bash
uv --version      # バージョン確認
uv self update    # uv自体の更新
```

### 2. Just のインストール

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
