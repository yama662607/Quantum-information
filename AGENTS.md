# AIエージェント向けドキュメント

このドキュメントでは、本プロジェクトのアーキテクチャ上の決定事項、制約、およびワークフローを概説します。**すべてのAIエージェントは、ドキュメントの整合性を保つために以下のルールに従わなければなりません。**

## 🏗️ アーキテクチャと規約

### 1. 信頼できる唯一の情報源
- **メイン教科書 (Preskill版)**: `quarto/textbook-preskill/textbook.qmd`
- **アーカイブ (Watrous版)**: `quarto/textbook-watrous/textbook.qmd`
- **ルール**: すべての解説は、各教科書の `textbook.qmd` に `include` 形式で統合されます。
- **制約**: 新しいメイン qmd ファイルを直下に作成せず、セクションごとの断片ファイル（`_*.qmd`）を `chapterX/` フォルダ内に作成してください。

### 2. パーシャル（断片）ファイル (`_*.qmd`)
- **場所**: `quarto/textbook-[preskill|watrous]/chapterX/`
- **命名**: 必ずアンダースコアで始めてください（例: `_1-introduction.qmd`）。
- **内容**: 純粋な Markdown/Quarto コンテンツのみ。**YAMLヘッダーを含めてはいけません**。

### 3. PDFリンク戦略
- **Watrous版**: `quarto/assets/pdf/watrous/Quantum_Information.pdf` を使用。
  - **計算式**: `物理ページ` = `本の表記ページ` + `8`。
- **Preskill版**: `quarto/assets/pdf/preskill/` 配下の各チャプター PDF を使用。
  - **計算式**: ページ番号のズレについては、各チャプターの PDF 構造を観測して決定してください。
  - **形式**: `[📄 chap1.pdf](assets/pdf/preskill/chap1.pdf#page=Y)`
### 4. テンプレート・システム (Templates)
執筆の効率と品質を維持するために、2種類の標準テンプレートを用意しています。
- **場所**: `quarto/templates/`
- **実戦用**: `quantum_textbook_template.qmd` (章や節の新規作成時にコピーして使用)
- **部品集**: `quarto_feature_showcase.qmd` (複雑なレイアウトやパーツの書き方を確認・コピーする際に使用)
- **ルール**: 新しくノートを作成する際は、必ず `quantum_textbook_template.qmd` の構成（PDFリンク、対応表、ポイント等）をベースにしてください。

## 💎 ノート品質ガイドライン (Quality Standards)

重要な定義や定理に関しては、以下の基準を厳守してください。

1.  **完全な数式記述**:
    - 文章だけで説明せず、必ず**厳密な数式定義**を併記してください。
    - 曖昧さを排除するため、集合の定義域や写像の型（例: $\Phi: \mathcal{L}(\mathcal{X}) \to \mathcal{L}(\mathcal{Y})$）も明記します。

2.  **物理学的直感との接続**:
    - 数学的な定義（線形代数）だけでなく、物理学で一般的な表記（ブラケット記法など）や概念との対応関係があれば補足してください。

3.  **視覚的な補助 (Visual Aids)**:
    - 複雑な概念、プロトコル、写像の関係性については、**可換図式**や**フローチャート**（Mermaid記法）を積極的に導入し、直感的な理解を助けてください。

4.  **PDFリンクの配置**:
    - すべてのセクション（`##`）およびサブセクション（`###`）の見出しには、必ず対応するPDFページへのリンクを付与してください。
    - 形式 (Watrous版): `## 見出し [📄 p.XX](assets/pdf/watrous/Quantum_Information.pdf#page=YY) {#anchor}`
    - 形式 (Preskill版): `## 見出し [📄 chap1.pdf](assets/pdf/preskill/chap1.pdf#page=YY) {#anchor}`
    - ページ番号 `XX` と `YY` の対応は `index.qmd` を確認してください。

5.  **Fenced Div の書式 (Style)**:
    - `:::` による囲み（Definition, Theorem 等）を使用する場合、**閉じ括弧の直前には必ず空行を挿入**してください。
    - これを怠ると Quarto/Pandoc のパースに失敗する場合があります。`just fix` で自動修正可能です。


## コンテンツ作成ワークフロー (Content Creation Workflow)

**重要: ノートを作成する前に、必ず元のPDFを読み込んでください。**

AIエージェントとして新しいノートを作成または編集する場合は、以下の手順を厳守してください。

1.  **原文の読解（テキスト抽出と画像スキャンの併用）**:
    テキストの抽出には `tools/extract_pdf.py` を使用します。
    ```bash
    # ページ範囲を指定してテキストを抽出（例：Watrous版）
    uv run python tools/extract_pdf.py quarto/assets/pdf/watrous/Quantum_Information.pdf --start 5 --end 10
    ```
    複雑な数式や可換図式など、テキスト抽出で記号が欠落・崩壊しやすい部分を読み取る場合は、`tools/extract_pdf_image.py` を使用してページを画像として出力し、AIエージェントが持つ **`view_file` ツールを用いて直接視覚情報として読み込んで**ください。
    ```bash
    # 特定の物理ページ（例: 114）を高解像度画像として抽出
    uv run --with pymupdf python tools/extract_pdf_image.py quarto/assets/pdf/watrous/Quantum_Information.pdf 114 /tmp/page_114.png
    ```
    （※画像抽出後、エージェントは `/tmp/page_114.png` に対し `view_file` ツールを実行し、マルチモーダル入力としてスキャンします。抽出した画像は不要になれば破棄して構いません）

2.  **断片ファイル (Partial QMD) の作成**: `quarto/textbook/chapter[N]/` 直下に部分ファイル (`_*.qmd`) を作成・更新します。
3.  **リンク付け (Cross-linking)**: 元のPDFへの絶対リンクと、教科書内の相対リンクを維持します。
4.  **形式と数式の検証 (Verification)**: 変更後は必ず `just check` を実行し、フォーマット、数式環境、Mermaidの構文エラーがないか確認してください。

## 教科書解説の追加 (Adding New Content)
1. **テンプレートの準備**: `quarto/templates/quantum_textbook_template.qmd` をコピーし、断片ファイル `quarto/textbook-[preskill|watrous]/chapterX/_name.qmd` を作成します。
2. **YAMLの削除**: 断片ファイルからは必ず YAML ヘッダーを削除してください。
3. **インクルード**: 該当する `textbook.qmd` に `{{< include chapterX/_name.qmd >}}` を追加します。
4. **ロードマップの更新**: `quarto/index.qmd` の対応する表に行を追加します。
    - カラム構成: `| 項目名 | 原文 PDF | 教科書解説 |`
    - 教科書解説へのリンクは `[📖 Textbook](textbook.qmd#new-anchor)` とします。

### トップページ (`index.qmd`) の修正
- デザインはシンプルに保つ: カラムは3つだけです。
- 明示的な指示がない限り、「ステータス」や「日付」カラムを追加しないでください。
- 「項目名」カラムの階層インデントには、全角スペース（`　`）を使用してください（レンダリング安定のため）。

## 🛑 よくある間違い（禁止事項）
- ❌ `quarto/textbook/chapter1.qmd` を作成しないでください。
- ❌ `_*.qmd` ファイルに `title: ...` 等の YAML を追加しないでください。
- ❌ `pip install` を提案しないでください。`uv sync` または `uv add` を使用してください。
- ❌ `:::` の閉じ括弧の前に空行を忘れないでください。

## 🤖 Justfile ガイド (AIエージェント用)

本プロジェクトではタスクランナー `Just` を採用しています。AIエージェントは、シェルコマンドを直接実行するのではなく、可能な限り `just` コマンドを使用してください。

| コマンド | 用途 | エージェントへの指示 |
| :--- | :--- | :--- |
| `just check-env` | **環境確認** | 初回参加時や、エラー時に依存関係を確認するために使用してください。 |
| `just setup` | **環境構築** | 依存関係 (`uv`, `npm`) を最新の状態に同期します。 |
| `just check` | **全体検証** | コードを変更した後は必ず実行してください。Lint, Format, Quarto構造, Mermaid, LaTeXが検証されます。 |
| `just fix` | **自動修正** | Lint, Formatに加え、**ドキュメントの空行不足等の構造エラーも自動修正**します。まずこれを試してください。 |
| `just docs` | **プレビュー** | ドキュメントのレンダリングを確認する際に使用します（サーバーが起動します）。 |
| `just validate-docs` | **ドキュメント検証** | Quarto/Mermaid/LaTeX の統合検証を手動で実行します。 |

## 🚀 AIエージェント向け初期導入ガイド (Onboarding)

新しいAIエージェントがこのプロジェクトに参加した際は、以下のステップで現状を把握してください。

1. **環境確認**: `just check-env` を実行し、必要なツール（Quarto, uv, just）が利用可能か確認してください。
2. **依存関係の同期**: `just setup` を実行し、仮想環境とライブラリを最新にしてください。
3. **ドキュメントの整合性チェック**: `just validate-docs` を実行し、既存のコンテンツに構造上の問題がないか確認してください。
4. **プレビューの確認**: `just docs` を実行し、ブラウザでレンダリング結果を確認できる状態にしてください。
