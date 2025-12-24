# Quantum Information Study Notes

このリポジトリは、John Watrous 教授の著作 "The Theory of Quantum Information" をベースにした学習ノートとリソースを管理しています。

## 🚀 クイックスタート (Quick Start)

このプロジェクトを動かすには **[uv](https://github.com/astral-sh/uv)** と **[Just](https://github.com/casey/just)** が必要です。

1.  **ツールの準備**: 未インストールの方は [セットアップガイド](#-セットアップガイド) を参照してインストールしてください。
2.  **プロジェクトの開始**:
    ```bash
    # リポジトリのクローン
    git clone https://github.com/yama662607/Quantum-information.git
    cd Quantum-information

    # 依存関係のインストールと環境構築
    just setup

    # プレビューサーバーの起動
    just docs
    ```
3.  **プレビューの確認**: ブラウザで `http://localhost:4312` にアクセスしてください。

---

## 🤝 共同開発ガイド (Collaboration)

このプロジェクトは、人間とAIエージェントが協力して執筆することを前提に設計されています。

-   **クロスプラットフォーム対応**: macOS, Linux, Windows どの環境でも `just` コマンドだけで共通のワークフローが実行可能です。
-   **環境チェック**: 何か問題が起きたら `just check-env` を実行してください。必要なツールが揃っているか自動診断します。
-   **品質管理**: パッチをプッシュする前に `just check` を実行し、リンターやバリデーションを通過することを確認してください。
-   **AIエージェントとの協調**: パートナーのAIエージェントにはまず [AGENTS.md](./AGENTS.md) を読むように指示してください。

---

## 🛠️ 技術スタック (Tech Stack)

| ツール | 用途 |
| :--- | :--- |
| **[Quarto](https://quarto.org/)** | 技術文書の出版・ドキュメンテーションシステム。 |
| **[uv](https://github.com/astral-sh/uv)** | Python の超高速パッケージ管理・仮想環境制御。 |
| **[Just](https://github.com/casey/just)** | コマンドライン操作を標準化するためのタスクランナー。 |

---

## 🔧 セットアップガイド (Setup Guide)

### 1. uv のインストール

Python の環境構築を高速かつ確実に行うために使用します。

-   **macOS / Linux:**
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
-   **Windows:**
    ```powershell
    powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```
-   **その他パッケージマネージャー:**
    -   macOS (Homebrew): `brew install uv`
    -   Windows (winget): `winget install astral-sh.uv`

### 2. Just のインストール

プロジェクト内の様々なコマンド（ビルド、チェック、サーバー起動など）を実行するために必要です。

-   **macOS (Homebrew):** `brew install just`
*   **Windows (winget):** `winget install casey.just`
*   **Linux (Ubuntu/Debian):** `sudo apt install just`

> [!TIP]
> インストール後、ターミナルを再起動して `just --version` および `uv --version` が動作することを確認してください。

---

## 📂 ディレクトリ構成

-   `quarto/`: 学習ノートのソース（Quarto ファイル群）
-   `tools/`: 開発支援スクリプト（監視ツール、環境チェック等）
-   `tests/`: 品質の検証用スクリプト
-   `AGENTS.md`: AIエージェントとの対話・ワークフローに関する詳細
-   `Justfile`: 定義されている全コマンドの一覧

---

## 📈 デプロイ状況
GitHub Pages への自動デプロイが設定されています。`master` ブランチへのプッシュにより、以下の URL が更新されます：
`https://yama662607.github.io/Quantum-information/`
