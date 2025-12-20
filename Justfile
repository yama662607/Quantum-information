# =============================================================================
# ⚙️ Configuration & Variables
# =============================================================================

set dotenv-load := true
set shell := ["bash", "-c"]

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
    uv sync --all-extras
    @echo "✅ Environment setup complete!"

# 全体品質検証: コードを変更せずに品質を検証 (CIゲート)
check: fmt-check lint typecheck validate-mermaid test
    @echo "✅ All quality checks passed!"

# 自動修正: フォーマットとLint修正を適用 (Agentの第一手)
fix: fmt lint-fix
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
    @echo "🗑️ Cleaning artifacts..."
    rm -rf .pytest_cache .ruff_cache __pycache__ .mypy_cache
    find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
    find . -type f -name "*.pyc" -delete
    @echo "✅ Cleanup complete!"

# =============================================================================
# 📚 Project-Specific Tasks
# =============================================================================

# Quarto文書のプレビュー
docs:
    @echo "📖 Starting Quarto preview..."
    {{pm}} run quarto preview docs/

# Streamlitアプリの起動
app path:
    @echo "🚀 Starting Streamlit app: {{path}}"
    {{python}} -m streamlit run {{path}}

# Mermaid図の構文検証（時間がかかるため必要な時のみ実行）
validate-mermaid:
    @echo "🔍 Validating all Mermaid diagrams..."
    @if command -v mmdc >/dev/null 2>&1; then \
        {{python}} mermaid_validator.py docs/; \
    else \
        echo "❌ mmdc not found. Install with:"; \
        echo "   npm install -g @mermaid-js/mermaid-cli"; \
        exit 1; \
    fi

# 特定のQuartoファイルのみMermaid検証
validate-mermaid-file file:
    @echo "🔍 Validating Mermaid in: {{file}}"
    @if command -v mmdc >/dev/null 2>&1; then \
        {{python}} mermaid_validator.py {{file}}; \
    else \
        echo "❌ mmdc not found. Install with:"; \
        echo "   npm install -g @mermaid-js/mermaid-cli"; \
        exit 1; \
    fi
