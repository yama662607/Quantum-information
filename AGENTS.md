# AIエージェント向けドキュメント

このドキュメントでは、本プロジェクトのアーキテクチャ上の決定事項、制約、およびワークフローを概説します。**すべてのAIエージェントは、ドキュメントの整合性を保つために以下のルールに従わなければなりません。**

## 🏗️ アーキテクチャと規約

### 1. 信頼できる唯一の情報源 (`textbook.qmd`)
- **ルール**: すべての教科書解説は、単一のファイル `quarto/textbook.qmd` に統合されています。
- **制約**: 新しい親ファイル（例: `chapterX.qmd`）を作成**しないでください**。すべての章は `textbook.qmd` 内のレベル1見出し（`#`）として定義されます。
- **インクルード**: コンテンツを取り込む際は、Quartoの `{{< include textbook/path/to/_file.qmd >}}` を使用してください。

### 2. パーシャル（断片）ファイル (`_*.qmd`)
- **場所**: `quarto/textbook/chapterX/`
- **命名**: 必ずアンダースコアで始めてください（例: `_1.1-linear-algebra.qmd`）。
- **内容**: 純粋な Markdown/Quarto コンテンツのみ。**YAMLヘッダーを含めてはいけません**（親ドキュメントのビルドが壊れるため）。
- **見出しレベル**: 節（Section）はレベル2（`##`）、項（Sub-section）はレベル3（`###`）から始めてください。

### 3. PDFリンク戦略
- **ファイル**: `quarto/assets/Quantum_Information.pdf`。
- **ロジック**: PDFへのリンクは「物理ページ番号」を使用します。
- **計算式**: `物理ページ` = `本の表記ページ` + `8`。
- **リンク形式**: `[📄 p.9](assets/Quantum_Information.pdf#page=17)` （例: 本のページが9の場合、物理ページ17へリンク）。
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
    - 形式: `## 見出し [📄 p.XX](Quantum_Information.pdf#page=YY) {#anchor}`
    - ページ番号 `XX` と `YY` の対応は `index.qmd` を確認してください。

5.  **Fenced Div の書式 (Style)**:
    - `:::` による囲み（Definition, Theorem 等）を使用する場合、**閉じ括弧の直前には必ず空行を挿入**してください。
    - これを怠ると Quarto/Pandoc のパースに失敗する場合があります。`just fix` で自動修正可能です。


## コンテンツ作成ワークフロー (Content Creation Workflow)

**重要: ノートを作成する前に、必ず元のPDFを読み込んでください。**

AIエージェントとして新しいノートを作成または編集する場合は、以下の手順を厳守してください。

1.  **原文の読解 (Read the Source)**:
    `extract_pdf.py` ツールを使用して、対応するPDFのテキストを抽出・読解します。
    推測で書くのではなく、必ず教科書の記述に基づいてください。

    ```bash
    # ページ範囲を指定して抽出 (例: 5ページから10ページ)
    uv run python extract_pdf.py docs/divided/Chapter3_Distance.pdf --start 5 --end 10
## Content Creation Workflow

1.  **PDF Extraction**:
    - Use both `tools/extract_pdf.py` (for searchable text) and the `view_file` tool (for high-fidelity visual check of formulas, diagrams, and layout).
    - Meticulously cross-reference both outputs to ensure technical terms and mathematical symbols are transcribed exactly.
2.  **Modular QMD Creation**: Create or update partial files (`_*.qmd`) in `quarto/textbook/chapter[N]/`.
3.  **Cross-linking**: Maintain absolute links to the source PDF and relative links between textbook/notes.
4.  **Verification**: Always run `just check` to ensure formatting, math, and Mermaid validity.

## 教科書解説の追加 (Adding New Textbook Content)
1.  **テンプレートの準備**: `quarto/templates/quantum_textbook_template.qmd` の内容をコピーし、新しい断片ファイル `quarto/textbook/chapterX/_new-section.qmd` を作成します。
2.  **YAMLの削除**: **重要: 断片ファイルからは必ず YAML ヘッダーを削除してください。**
3.  **インクルード**: `quarto/textbook.qmd` の適切な場所に `{{< include textbook/chapterX/_new-section.qmd >}}` を追加します。
3.  **ロードマップの更新**: `quarto/index.qmd` の表に行を追加します。
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
