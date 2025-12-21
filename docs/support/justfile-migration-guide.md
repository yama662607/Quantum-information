# Justfile 活用・流用ガイド

このプロジェクトでは、タスクランナーとして **`just`** (Justfile) が非常に高度に活用されています。
複雑なコマンドを抽象化し、Pythonプロジェクトの品質維持を自動化するための構成を他プロジェクトへ持ち出すためのガイドです。

---

## 1. 導入のメリット

この `Justfile` を導入することで、開発者は以下の恩恵を受けられます。
1.  **コマンドの標準化**: `uv`, `ruff`, `pytest`, `quarto` などの異なるツールのコマンドを覚え直す必要がありません。
2.  **AIエージェントへの親和性**: `check` や `fix` といった標準的なインターフェースを提供することで、AIエージェントが自律的にコードを修正しやすくなります。
3.  **環境の再現性**: `setup` 一つで新しい開発者が作業を開始できます。

---

## 2. 主要コマンドリファレンス

このプロジェクトで定義されている、流用価値の高いコマンド群です。

### 🤖 標準インターフェース (エージェントプロトコル)
これらは、プロジェクトの健全性を保つための「入り口」となるコマンドです。
- `just setup`: 依存関係のインストールと環境構築 (`uv sync`)。
- `just check`: コードを変更せずに品質を検証（フォーマット、Lint、テストを一括実行）。CIでも使用可能。
- `just fix`: フォーマット修正やLintの自動修正を適用。開発の「最初の一手」として最適。

### 🧪 テスト・品質管理
- `just test`: 全テストの実行。`just test tests/specific_test.py` のように引数パススルーも可能。
- `just fmt`: `ruff` を使用したコード成形。
- `just lint`: 静的解析。

### 📚 プロジェクト固有タスク
- `just docs`: Quarto ドキュメントのローカルプレビュー。
- `just app [path]`: Streamlit アプリケーションの起動。
- `just validate-docs`: ドキュメント（Quarto, Mermaid, LaTeX）の統合検証。

---

## 3. 他プロジェクトへの流用ステップ

### ステップ 1: `just` のインストール
プロジェクト外の環境でも `just` コマンドを使えるようにします。
```bash
brew install just # macOS
```

### ステップ 2: `Justfile` の基本構造をコピー
プロジェクトのルートに `Justfile` を作成し、以下のコア部分をコピーします。

```makefile
set dotenv-load := true
set shell := ["bash", "-c"]

pm := "uv" # パッケージマネージャー (pip, poetry等に変更可)
python := "uv run python"

# デフォルトターゲット
default: check

# セットアップ
setup:
    @echo "📦 Setting up..."
    {{pm}} sync

# 品質チェック (CIでも使用)
check:
    @echo "🔍 Checking quality..."
    {{pm}} run ruff format --check
    {{pm}} run ruff check
    {{pm}} run pytest

# 自動修正
fix:
    @echo "✨ Fixing..."
    {{pm}} run ruff format
    {{pm}} run ruff check --fix
```

### ステップ 3: ツール設定との同期
`Justfile` が呼び出すツール（`ruff`, `pytest` 等）の設定が `pyproject.toml` に記述されていることを確認してください。

---

## 4. このプロジェクト独自の工夫点

### 🔧 引数パススルー (`*args`)
`test *args=""` のように定義することで、`just test -v -k "my_function"` のような複雑な引数を内部の `pytest` にそのまま渡せるようになっています。

### 🔍 ドキュメントバリデーターの統合
`validate-docs` コマンドのように、ドキュメントの品質（Quarto構造、Mermaid、LaTeXなど）までタスクランナーに組み込むことで、ドキュメントとコードの乖離を防ぎ、爆速な検証（ハッシュキャッシュ）を実現しています。

### 🧹 クリーンアップ
`just clean` によって、Python特有のキャッシュファイル（`__pycache__`, `.pytest_cache`）を一括削除できるため、環境が不安定になった際の復旧が容易です。

---

## まとめ：何を持ち出すべきか？

1.  **AIエージェント対応の `check`/`fix` インターフェース**: 開発効率が劇的に向上します。
2.  **`uv` をベースとした変数定義**: `pm` 変数一つでパッケージマネージャーを切り替えられる柔軟性。
3.  **引数パススルーの仕組み**: 柔軟なテスト実行を可能にします。

これらを流用することで、どのプロジェクトでも「コマンド一つで品質が保たれる」プロフェッショナルな開発環境を構築できます。
