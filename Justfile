# =============================================================================
# ⚙️ Configuration & Variables
# =============================================================================

set dotenv-load := true

# Package manager and runtime
pm := "uv"
python := "uv run python"

# =============================================================================
# 🤖 Standard Interface (AI Agent Protocol)
# =============================================================================

# デフォルト: 読み取り専用の全体チェックを実行
default: check

# 環境構築: 依存関係のインストール、ツールチェーンのセットアップ
setup:
    @echo "📦 Setting up environment..."
    {{pm}} sync --all-extras
    npm install
    @echo "✅ Environment setup complete!"

# 全体品質検証: コードを変更せずに品質を検証 (CIゲート)
check: fmt-check lint typecheck validate-docs test
    @echo "✅ All quality checks passed!"

# 自動修正: フォーマットとLint修正を適用 (Agentの第一手)
fix: fmt lint-fix validate-docs-fix
    @echo "✨ Auto-fixes applied!"

# =============================================================================
# 🧪 Testing & Verification
# =============================================================================

# ユニット/統合テスト: 引数パススルー対応
test *args="":
    @echo "🧪 Running unit tests..."
    {{pm}} run pytest {{args}}

# =============================================================================
# 🧩 Granular Tasks (Components of 'check' & 'fix')
# =============================================================================

# --- Format (整形) ---

fmt-check:
    @echo "📏 Checking formatting..."
    {{pm}} run ruff format --check

fmt:
    @echo "💅 Formatting code..."
    {{pm}} run ruff format

# --- Lint (静的解析) ---

lint:
    @echo "🔍 Linting..."
    {{pm}} run ruff check

lint-fix:
    @echo "🧹 Fixing lint errors..."
    {{pm}} run ruff check --fix

# --- Typecheck (型検査) ---

typecheck:
    @echo "📐 Checking types..."
    @echo "⚠️  Type checking not configured yet. Consider adding mypy to dev dependencies."
    @echo "   Skipping for now..."

# =============================================================================
# 🛠️ Operations & Utilities
# =============================================================================

# アーティファクト削除
clean:
    {{python}} tools/clean.py

# =============================================================================
# 📚 Project-Specific Tasks
# =============================================================================

# Quarto文書のプレビュー
docs:
    {{python}} tools/dev_server.py

# Streamlitアプリの起動
app path:
    @echo "🚀 Starting Streamlit app: {{path}}"
    {{python}} -m streamlit run {{path}}

# 統合ドキュメント検証 (Quarto, Mermaid, LaTeX)
validate-docs:
    @echo "🔍 Running integrated document validation..."
    {{python}} tools/validate_docs.py quarto/

# 統合ドキュメント自動修正
validate-docs-fix:
    @echo "🧹 Automatically fixing document style issues..."
    {{python}} tools/validate_docs.py quarto/ --fix

# 検証キャッシュのクリア
clear-validation-cache:
    @echo "🧹 Clearing document validation cache..."
    {{python}} tools/validate_docs.py --clear-cache

# PDFテキスト抽出
extract-pdf pdf_path *args="":
    @echo "📄 Extracting text from: {{pdf_path}}"
    {{python}} tools/extract_pdf.py {{pdf_path}} {{args}}
