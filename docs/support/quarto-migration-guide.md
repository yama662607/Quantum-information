# Quarto 環境構築・流用ガイド

このプロジェクトの Quarto ドキュメント環境を他のプロジェクトに流用するための調査報告と構築ガイドです。
このシステムは、**V-S-V サイクル（Visual → Scratch → Verify）** をドキュメント、コード、テストの一貫した流れとして管理することに特化しています。

---

## 1. 主要な構成コンポーネント

このプロジェクトの Quarto 活用において、特に流用価値の高いコア要素は以下の通りです。

### 1.1 `docs/_quarto.yml` (統合設定)
Quarto の挙動を定義するプロジェクト全体の設計図です。
- **マルチフォーマット対応**: モダンな HTML テーマ (`cosmo`)、サイドバーナビゲーション、目次（TOC）の自動生成。
- **日本語対応**: `lang: ja` 設定による UI の日本語化。
- **高度な MD 機能**: コードの折りたたみ (`code-fold: true`)、コードツール、外部リンクの別窓表示、スムーズスクロール。

### 1.2 `docs/templates/theory_template.qmd` (理論用テンプレート)
学習・解説ドキュメントの質を担保する強力なボイラープレートです。
- **Mermaid 統合**: フローチャートやシーケンス図をテキストベースで記述可能。
- **Python コード実行**: ドキュメント内で Python を実行し、結果やグラフを直接埋め込み。
- **レイアウト機能**: `::: {.grid}` によるカラム分け、`::: {.panel-tabset}` によるタブ表示。
- **マージン注釈**: 本文横に補足を表示する `{.aside}` クラス。

### 1.3 `templates/apps/visualization/` (可視化ライブラリ)
ドキュメントとアプリの両方で使える再利用可能なプロット関数のライブラリです。
- **Plotly, PyVis, Manim**: 2D/3D グラフ、インタラクティブなネットワーク図、数学アニメーションのテンプレート。
- **責務の分離**: 「可視化ロジック（テンプレート）」と「表示（Streamlit/Quarto）」を分けることで、コードの重複を防止。

---

## 2. 他プロジェクトへの導入ステップ

### ステップ 1: Quarto のインストール
事前に [Quarto 公式サイト](https://quarto.org/docs/get-started/) から CLI をインストールしてください。

### ステップ 2: ディレクトリ構造のコピー
以下の構造をプロジェクト内に作成することをお勧めします。

```bash
.
├── docs/                # Quarto ドキュメントのメインディレクトリ
│   ├── _quarto.yml     # プロジェクト設定
│   ├── index.qmd       # トップページ
│   ├── templates/      # 今回の templates/theory_template.qmd をここに配置
│   └── [各カテゴリ]/    # コンテンツ（phase1, lesson01 など）
├── templates/          # 可視化やコードのテンプレート
│   └── apps/
│       └── visualization/ # 再利用可能な可視化関数群
└── Justfile            # (任意) docs: コマンドでプレビューを自動化
```

### ステップ 3: 設定ファイルの編集
`docs/_quarto.yml` をコピーし、プロジェクトに合わせて以下の項目を編集します。
- `project > output-dir`: ビルド結果の出力先。
- `website > navbar`: 上部ナビゲーション。
- `website > sidebar > contents`: サイドメニューの構成。
- `format > html > css`: カスタムスタイル（`docs/templates/styles.css` を参照）。

---

## 3. Quarto 活用のベストプラクティス

このプロジェクトで実践されている独自の工夫を以下にまとめます。

### 🐍 Python 連携 (Frozen Execution)
`execute: freeze: auto` 設定により、ドキュメント内の Python コードは実行結果がキャッシュ（フリーズ）されます。
これにより、環境が変わってもドキュメントの再レンダリングが高速化され、再現性が保たれます。

### 🎨 カスタム CSS による装飾
`docs/templates/styles.css` を通じて、標準の Quarto には無いスタイルを適用しています。
- **Callout ボックスの調整**: ヒントや警告の余白を最適化。
- **コード強調**: フォントや背景色の微調整。

### 🕵️ Mermaid バリデーター (`mermaid_validator.py`)
大規模なドキュメントプロジェクトでは、Mermaid の構文エラーがビルドを止めがちです。
このプロジェクトの `mermaid_validator.py` を流用することで、ビルド前に一括で構文チェックを行うことができます。

---

## 4. 依存パッケージ (pyproject.toml 抜粋)
Python コードを含むドキュメントを動かすには、以下のライブラリが重要です。

```toml
dependencies = [
    "quarto",       # CLI
    "jupyter",      # .qmd 内で Python を動かすために必要
    "plotly",       # インタラクティブな図解用
    "pyvis",        # ネットワーク図解用
    "icecream",     # デバッグ出力の整形用
    "matplotlib",   # 静的な図解用
]
```

## まとめ：何を持ち出すべきか？

1.  **`docs/_quarto.yml`**: プロジェクト全体の見た目と構造を一瞬で整えるため。
2.  **`docs/templates/theory_template.qmd`**: 質の高いドキュメントを量産する「型」として。
3.  **`docs/templates/styles.css`**: デザインの微調整を継承するため。
4.  **`templates/apps/visualization/`**: 可視化コードをドキュメントとアプリで共有するアーキテクチャ。

これらを流用することで、どのプロジェクトでも「見てわかる、動かしてわかる」高品質なドキュメント環境を数分で構築できます。
