# 実装ガイド索引

このプロジェクトの執筆・実装に必要なガイドの一覧と、それぞれの用途を解説します。

---

## 📚 ガイド全体の構成

```
research/guidelines/
├── IMPLEMENTATION_GUIDE_INDEX.md          ← このファイル（ナビゲーション）
├── writing_policy.md                      ← 執筆方針（Phase 1/2）
├── quarto_best_practices.md               ← Quarto 入門（既存）
├── quarto_heading_numbering.md            ← 【新】見出し番号付けガイド
├── quarto_config_improvement.md           ← 【新】_quarto.yml 改善案
├── preskill_pdf_mapping.md                ← 【新】Preskill版PDF対応戦略
├── preskill_chapter_mapping_template.md   ← 【新】チャプター別マッピングテンプレート
└── preskill_chap1_mapping.md              ← 【実装】Chapter 1 の実装情報
    (各チャプター毎に作成予定)
```

---

## 🎯 用途別ガイド選択フロー

### シナリオ1: 初めてこのプロジェクトに参加する

→ **読む順序**:
1. **最初**: `writing_policy.md` - 執筆の基本ルール（Phase 1/2）
2. **次に**: `quarto_best_practices.md` - Quarto 基本知識
3. **実装**: `preskill_pdf_mapping.md` - Preskill版の特殊な対応
4. **詳細**: `quarto_heading_numbering.md` - 見出し番号の細かい制御

---

### シナリオ2: Preskill版 Chapter X の翻訳を始める

→ **実施手順**:

1. **PDF 構造の観測** (翻訳前)
   ```bash
   just process-pdf quarto/assets/pdf/preskill/chapX.pdf 1 20
   ```

2. **マッピング表を作成**
   - `preskill_chapter_mapping_template.md` をコピー
   - `research/guidelines/preskill_chapX_mapping.md` として保存
   - 観測結果をもとに、セクション開始ページを記入

3. **翻訳開始**
   - `quarto/textbook-preskill/chapterX/` に `_X.Y-title.qmd` ファイルを作成
   - マッピング表を参考に、各見出しに PDFリンク を付ける
   - 見出し番号は `{#sec-anchor}` で明示

4. **プレビューで確認**
   ```bash
   just docs
   ```
   - ブラウザで PDFリンク をクリック
   - 正しいページが開くか確認

5. **品質チェック**
   ```bash
   just check
   ```

---

### シナリオ3: 見出し番号や参照の細かい設定を調整したい

→ **読むべきガイド**:
- `quarto_heading_numbering.md` - 見出し番号の全オプション解説
- `quarto_config_improvement.md` - _quarto.yml の改善案（実装済みの場合）

例: 「H3 まで番号を付けたい」「参照プレフィックスを変えたい」

---

### シナリオ4: _quarto.yml を修正したい

→ **読むべきガイド**:
- `quarto_config_improvement.md` - 現在の設定状況と改善案
- `quarto_heading_numbering.md` - 各オプションの詳細説明

改善案の主要ポイント:
- `number-depth: 3 → 2` （H3を番号なしに）
- `crossref.sec-prefix: "節"` （日本語化）
- `format.pdf.top-level-division: chapter` （PDF で章扱い）

---

## 📖 ガイド別内容概要

### 1. `writing_policy.md`
**用途**: 執筆の基本ルール・品質基準

| トピック | 詳細 |
|---------|------|
| Phase 1（忠実翻訳） | 定義・定理・証明の省略禁止 |
| Phase 2（解説拡充） | 直感・可換図式・Qiskit例 |
| 品質基準 | 完全な数式記述、物理的直感、視覚的補助 |

---

### 2. `quarto_best_practices.md` 
**用途**: Quarto 基本機能の入門

| トピック | 詳細 |
|---------|------|
| Markdown 拡張 | コールアウト、Fenced Div、Mermaid |
| 数式・図表 | LaTeX、図表参照 |
| レイアウト | カラム、グリッド |

---

### 3. `quarto_heading_numbering.md` ⭐ **新**
**用途**: 見出し番号付けの完全ガイド

| トピック | 詳細 |
|---------|------|
| 基本設定 | `number-sections: true` の役割 |
| 階層制御 | `number-depth` で採番深さ調整 |
| 特殊処理 | `.unnumbered`、`.unlisted` |
| 参照機構 | `{#sec-anchor}` + `@sec-anchor` |
| クロスリファレンス | 図表番号の章ごと採番（`chapters: true`） |

**このプロジェクトでの推奨**:
```yaml
number-sections: true
number-depth: 2
crossref:
  chapters: true
  sec-prefix: "節"
```

---

### 4. `quarto_config_improvement.md` ⭐ **新**
**用途**: _quarto.yml の診断と改善案

| 項目 | 現在 | 推奨 | 理由 |
|------|------|------|------|
| `number-depth` | 3 | **2** | H3 番号を削除し可読性向上 |
| `crossref.sec-prefix` | （未設定） | **"節"** | 日本語化 |
| `pdf.top-level-division` | （未設定） | **chapter** | PDF で章扱い |

**リスク**: 低（テストで確認後に反映推奨）

---

### 5. `preskill_pdf_mapping.md` ⭐ **新**
**用途**: Preskill版の独立PDF対応戦略

| 要点 | 詳細 |
|------|------|
| 問題設定 | 各チャプターが独立PDF、ページリセット |
| 対比 | Watrous版（統合PDF + 計算式）との違い |
| 解決策 | チャプター毎のマッピング表を作成・管理 |
| ワークフロー | PDF観測 → マッピング作成 → 翻訳 → 検証 |

**実装の流れ**:
```
1. just process-pdf chap1.pdf 1 20
2. research/guidelines/preskill_chap1_mapping.md 作成
3. セクション開始ページを記入
4. 翻訳ファイルに PDFリンク を付ける
5. just docs で確認
```

---

### 6. `preskill_chapter_mapping_template.md` ⭐ **新**
**用途**: 各チャプターのマッピング情報を管理するテンプレート

| 用途 | 方法 |
|------|------|
| **初期作成** | このテンプレートをコピー → `preskill_chapX_mapping.md` |
| **記入** | PDF を開きながら、セクション開始ページを記入 |
| **参照** | 翻訳時に PDFリンク のページ番号を決定 |
| **保守** | 追記のみ、修正は慎重に（リンク破壊の危険） |

**テンプレート内容**:
- 基本情報（ファイル名、総ページ数など）
- セクション構成表（セクション、見出し、開始ページ、終了ページ、ポイント）
- 記入のコツ、チェックリスト

---

## 🔗 相互参照マップ

```
writing_policy.md
  ↓ (Phase 1 で実装)
quarto_best_practices.md（Markdown 基本）
  ↓
quarto_heading_numbering.md（見出し番号の実装）
  ↓
_quarto.yml 修正（quarto_config_improvement.md 参照）
  ↓
preskill_pdf_mapping.md（Preskill版 PDF 対応）
  ↓
preskill_chapter_mapping_template.md（チャプター毎のマッピング）
```

---

## ✅ チェックリスト

### プロジェクト参加者向け

- [ ] `writing_policy.md` を読んだ
- [ ] `quarto_best_practices.md` で Quarto 基本を理解した
- [ ] `preskill_pdf_mapping.md` で独立PDF構造を理解した

### 新しいチャプター追加時

- [ ] `just process-pdf` で対象PDF を観測
- [ ] `preskill_chapter_mapping_template.md` をコピー
- [ ] マッピング表を完成
- [ ] 翻訳中に PDFリンク を付ける
- [ ] `just docs` でリンク確認
- [ ] `just check` で構文確認

### _quarto.yml 修正時

- [ ] `quarto_config_improvement.md` で改善案を確認
- [ ] テスト環境で視覚確認
- [ ] `number-depth`、`crossref` などを修正
- [ ] `just check` で Quarto 構文確認
- [ ] `just docs` で HTML プレビュー確認
- [ ] 必要に応じて PDF でも確認

---

## 📊 ガイド作成日時

| ガイド | 作成日 | 用途 |
|--------|--------|------|
| `writing_policy.md` | （既存） | 執筆方針 |
| `quarto_best_practices.md` | （既存） | Quarto基本 |
| `quarto_heading_numbering.md` | 2026-04-07 | 見出し番号 ⭐ |
| `quarto_config_improvement.md` | 2026-04-07 | _quarto.yml 改善 ⭐ |
| `preskill_pdf_mapping.md` | 2026-04-07 | PDF対応戦略 ⭐ |
| `preskill_chapter_mapping_template.md` | 2026-04-07 | マッピングテンプレート ⭐ |

---

## 🚀 今すぐ始める

### 最初のチャプター翻訳

```bash
# Step 1: PDF 観測
just process-pdf quarto/assets/pdf/preskill/chap1.pdf 1 20

# Step 2: マッピング作成
# research/guidelines/preskill_chapter_mapping_template.md をコピー
# → research/guidelines/preskill_chap1_mapping.md として保存
# → PDF を開きながら記入

# Step 3: 翻訳開始
# quarto/textbook-preskill/chapter1/_1.1-title.qmd を作成
# → マッピング表を参考に PDFリンク を付ける

# Step 4: 検証
just docs
just check
```

---

## 📞 質問・疑問がある場合

各ガイドの「よくある質問」セクションを確認してください。

- 見出し番号 → `quarto_heading_numbering.md` の「つまずきやすいポイント」
- PDF マッピング → `preskill_chapter_mapping_template.md` の「よくある質問」
- 執筆方針 → `writing_policy.md` の説明
