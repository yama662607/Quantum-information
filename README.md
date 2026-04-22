# Quantum Information Study Notes

John Preskill 教授の講義ノート **"Quantum Computation"** を、自主ゼミ形式で1年かけて丁寧に読み解き、日本語の解説ノートとして再現するプロジェクトです。

> [!NOTE]
> John Watrous 教授の "The Theory of Quantum Information" の学習ノートはアーカイブとして引き続き参照できます。[ Watrous版 アーカイブへ](./quarto/textbook-watrous/textbook.qmd)

---

## プロジェクトの目的

このプロジェクトでは、単なる要約や解説にとどまらず、**原文を一言一句日本語に翻訳したうえで、数学的直感や Qiskit を用いた実装例を追加した、究極の日本語版講義ノート**を作ることを目指しています。

### 執筆方針

- **Phase 1（忠実翻訳）**: 定義・定理・証明・補足をすべて省かず日本語に翻訳します。「重要でない」と判断して省くことは禁止です。
- **Phase 2（解説拡充）**: Phase 1 の完全訳を土台に、直感的な解説・可換図式（Mermaid）・Qiskit 実装例などを追記します。

詳細は [`research/guidelines/writing_policy.md`](./research/guidelines/writing_policy.md) を参照してください。

### なぜ Preskill 版なのか

Preskill 教授の講義ノートは、量子情報理論を**物理学的な直感**から積み上げており、数学的な厳密さと物理的なイメージの両立が優れています。一方、Watrous 版は線形代数を基礎とした数学的な厳密さに特化しており、両者は相補的な関係にあります。

---

## ロードマップ（1年間の目安）

| 期間 | 章 | 内容 |
| :--- | :--- | :--- |
| 第1〜2ヶ月 | Chapter 1: Introduction | 情報と物理、古典情報理論の基礎 |
| 第3〜4ヶ月 | Chapter 2: Foundations I | 量子状態、密度行列、アンサンブル |
| 第5〜6ヶ月 | Chapter 3: Foundations II | 測定、POVM、量子チャネル |
| 第7〜8ヶ月 | Chapter 4: Quantum Entanglement | エンタングルメント、Bell 不等式 |
| 第9〜10ヶ月 | Chapter 5: Quantum Coding Theory | 量子誤り訂正の基礎 |
| 第11〜12ヶ月 | Chapter 6 以降 | 量子計算・アルゴリズムなど |

> [!TIP]
> 現在の進捗は [`quarto/index.qmd`](./quarto/index.qmd) のロードマップ表を確認してください。

---

## クイックスタート (Quick Start)

このプロジェクトを動かすには **[uv](https://github.com/astral-sh/uv)** と **[Just](https://github.com/casey/just)** が必要です。

1.  **ツールの準備**: 未インストールの方は [セットアップガイド](#-セットアップガイド) を参照してください。
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

## 共同開発ガイド (Collaboration)

このプロジェクトは、人間とAIエージェントが協力して執筆することを前提に設計されています。

- **品質管理**: パッチをプッシュする前に `just check` を実行してください。
- **PDF解析**: 新しいページを読むときは `just process-pdf <pdf> <start> <end>` を使ってテキスト・数式・画像を一括取得します。
- **AIエージェントとの協調**: パートナーのAIエージェントにはまず [AGENTS.md](./AGENTS.md) を読むように指示してください。

---

## 技術スタック (Tech Stack)

| ツール | 用途 |
| :--- | :--- |
| **[Quarto](https://quarto.org/)** | 技術文書の出版・ドキュメンテーションシステム |
| **[uv](https://github.com/astral-sh/uv)** | Python の超高速パッケージ管理・仮想環境制御 |
| **[Just](https://github.com/casey/just)** | コマンドライン操作を標準化するためのタスクランナー |
| **[Pix2Text](https://github.com/breezedeus/Pix2Text)** | PDF画像から数式（LaTeX）を抽出する数式OCRエンジン |

---

## ディレクトリ構成

```text
Quantum-information/
├── quarto/
│   ├── textbook-preskill/   # メイン: Preskill版 学習ノート
│   ├── textbook-watrous/    # アーカイブ: Watrous版 学習ノート
│   ├── assets/pdf/          # PDFアセット（著者ごとに整理）
│   │   ├── preskill/
│   │   └── watrous/
│   └── templates/           # 執筆テンプレート
├── research/
│   ├── guidelines/          # 執筆方針・ベストプラクティス
│   └── notes/               # リサーチメモ・翻訳作業ファイル
├── tools/                   # PDF解析・開発支援スクリプト
├── tests/                   # 品質検証スクリプト
├── AGENTS.md                # AIエージェント向けルール
└── Justfile                 # タスクランナー定義
```

---

## セットアップガイド (Setup Guide)

### 1. uv のインストール

- **macOS / Linux:**
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
- **macOS (Homebrew):** `brew install uv`

### 2. Just のインストール

- **macOS (Homebrew):** `brew install just`
- **Linux (Ubuntu/Debian):** `sudo apt install just`

> [!TIP]
> インストール後、ターミナルを再起動して `just --version` および `uv --version` が動作することを確認してください。

---

## デプロイ状況

GitHub Pages への自動デプロイが設定されています。`master` ブランチへのプッシュにより、以下の URL が更新されます：
`https://yama662607.github.io/Quantum-information/`

---

## ライセンス (License)

このプロジェクトは [MIT License](./LICENSE) のもとで公開されています。
© 2026 Daisuke Yamashiki
