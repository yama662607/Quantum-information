# =============================================================================
# Configuration & Variables
# =============================================================================

set dotenv-load := true

# Package manager and runtime
# Package manager and runtime
pm := "uv"
python := "uv run python"

# Windows-specific configuration (PowerShell)
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

# =============================================================================
# Standard Interface (AI Agent Protocol)
# =============================================================================

# デフォルト: 全体の品質チェックを実行
default: check

# 環境の整合性チェック: 必要なツール (uv, just, quarto, npm) がインストールされているか確認
check-env:
    @{{python}} tools/check_env.py

# 環境構築: 依存関係のインストールとツールチェーンのセットアップ
setup: check-env
    @echo " Setting up environment..."
    {{pm}} sync --all-extras
    npm install
    @echo " Environment setup complete!"

# 全体品質検証: コードを変更せずに品質を検証 (CIゲート)
check: fmt-check lint typecheck validate-docs test
    @echo " All quality checks passed!"

# フル品質検証: 通常チェックに加えてQuarto HTML実レンダリングを確認
check-full: check render-site
    @echo " Full quality checks passed!"

# 自動修正: フォーマット、Lint、およびドキュメントの構造エラーを自動修正
fix: fmt lint-fix validate-docs-fix
    @echo " Auto-fixes applied!"

# =============================================================================
# Testing & Verification
# =============================================================================

# ユニットテストの実行: pytest を使用
test *args="":
    @echo " Running unit tests..."
    {{pm}} run pytest {{args}}

# =============================================================================
# Granular Tasks (Components of 'check' & 'fix')
# =============================================================================

# コードの自動整形チェック (Ruff)
fmt-check:
    @echo " Checking formatting..."
    {{pm}} run ruff format --check

# コードの自動整形 (Ruff)
fmt:
    @echo " Formatting code..."
    {{pm}} run ruff format

# 静的解析 (Ruff)
lint:
    @echo " Linting..."
    {{pm}} run ruff check

# 静的解析による自動修正 (Ruff)
lint-fix:
    @echo " Fixing lint errors..."
    {{pm}} run ruff check --fix

# 型検査 (mypy 等)
typecheck:
    @echo " Checking types..."
    {{pm}} run mypy tools

# =============================================================================
# Operations & Utilities
# =============================================================================

# ビルド成果物やキャッシュの削除 (Cross-platform)
clean:
    {{python}} tools/clean.py

# =============================================================================
# Project-Specific Tasks
# =============================================================================

# Quarto文書のリアルタイム・プレビュー起動 (自動更新機能付き)
docs:
    @{{python}} tools/dev_server.py || (echo "\n Preview failed. If the port is already in use, try running: \033[1mjust fix-docs\033[0m" && exit 1)

# Quarto HTML book の実レンダリング
render-site:
    quarto render quarto --to html

# Quarto PDF book の実レンダリング
render-book-pdf:
    quarto render quarto --to pdf

# docs が失敗した（ポート使用中など）場合の復旧コマンド
fix-docs:
    @echo " Cleaning up lingering Quarto processes and freeing port 4312..."
    -lsof -ti:4312 | xargs kill -9 2>/dev/null
    -pkill -f "quarto preview" 2>/dev/null
    @echo " Cleanup complete. You can now try 'just docs' again."

# Streamlitアプリの起動
app path:
    @echo " Starting Streamlit app: {{path}}"
    {{python}} -m streamlit run {{path}}

# Quarto/Mermaid/LaTeX のドキュメント整合性検証
validate-docs:
    @echo " Running integrated document validation..."
    {{python}} tools/validate_docs.py quarto/

# キャッシュを使わずにドキュメント検証
validate-docs-no-cache:
    @echo " Running integrated document validation without cache..."
    {{python}} tools/validate_docs.py quarto/ --no-cache

# ドキュメント整合性エラーの自動修正
validate-docs-fix:
    @echo " Automatically fixing document style issues..."
    {{python}} tools/validate_docs.py quarto/ --fix

# バリデーション結果のキャッシュクリア
clear-validation-cache:
    @echo " Clearing document validation cache..."
    {{python}} tools/validate_docs.py --clear-cache

# 教科書PDFの画像化 (PNG出力)
# 使い方: just render-pdf <pdf_path> <start_page> <end_page>
render-pdf pdf_path start end *args="":
    @echo " Rendering PDF pages {{start}}-{{end}}..."
    {{python}} tools/render_pdf.py {{pdf_path}} --start {{start}} --end {{end}} {{args}}

# PDFページからのテキスト・数式(LaTeX)抽出
# 使い方: just extract-content <pdf_path> <start_page> <end_page>
# ※事前に just render-pdf を実行しておく必要があります。
extract-content pdf_path start end *args="":
    @echo " Extracting content from PDF pages {{start}}-{{end}}..."
    @export PYTHONPATH=${PYTHONPATH:-}:. && {{python}} tools/extract_pdf_content.py {{pdf_path}} --start {{start}} --end {{end}} {{args}}
