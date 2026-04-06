# Preskill版 PDFマッピングガイド

## 🎯 問題設定

Preskill版の講義ノートは **チャプター毎に独立したPDFファイル** となっており、各PDFのページナンバリングが独立しています。つまり：

- `chap1.pdf` → p.1, p.2, ..., p.N
- `chap2_15.pdf` → p.1, p.2, ..., p.M（通常 p.1 からリセット）
- `chap3_15.pdf` → p.1, p.2, ..., p.L（同じく独立）

したがって、**Watrous版のように「全体通し番号 + オフセット」という単一の計算式では対応できない** ため、チャプター毎のマッピング管理が必須です。

---

## 📋 実装戦略

### ステップ1: 各チャプターPDFの構造を観測

新しいチャプターを始める際、**最初に必ず対象PDFを確認** してください。

```bash
# Preskill版 chap2 の先頭 5 ページの構造を確認
just process-pdf quarto/assets/pdf/preskill/chap2_15.pdf 1 5
```

出力から以下を記録：

1. **ページナンバリング**: 最初のページ番号は何か？（通常 p.1 だが、例外がある可能性）
2. **セクション配置**: どこから「2.1」や「2.2」が始まるか？
3. **グリフ・数式の位置**: 重要な数式や図はどのページにあるか？

### ステップ2: チャプター毎のPDFマッピング表を作成

`research/guidelines/` に、以下のテンプレートで各チャプターのマッピング情報を記録：

```markdown
# Preskill Chapter X PDF Mapping

| 項目 | 値 |
|------|-----|
| **PDFファイル** | `chap X.pdf` |
| **ページナンバリング** | p.1 から始まる（または例外） |
| **総ページ数** | XX |
| **セクション開始** | X.1 は p.Y、X.2 は p.Z、... |

## セクション毎のページマッピング

| セクション | 見出し | 開始ページ | 終了ページ | 備考 |
|-----------|--------|----------|----------|------|
| 1.1 | Introduction | 1 | 3 | 定義が含まれる |
| 1.2 | Quantum States | 4 | 8 | 図が多数 |
| 1.3 | ... | ... | ... | ... |
```

### ステップ3: Quarto内でのリンク記述

マッピング表を基にして、各セクションに対応するPDFリンクを記述：

```markdown
## 1.1 量子情報とは何か [📄 chap1.pdf](/assets/pdf/preskill/chap1.pdf#page=1) {#sec-what-is-qi}

（本文内容）
```

**ルール**：
- 各セクション（`##`）の見出しに **必ずPDFリンク** を付ける
- ページ番号は `#page=N` で指定（Nはそのセクションの開始ページ）
- リンク先は **チャプター固有のPDF**（全体統合PDFではない）

---

## 🔧 実装例

### 例1: Preskill Chapter 1

#### マッピング情報（事前調査）
```
chap1.pdf のページ構成:
- p.1-2: Introduction
- p.3-7: Foundations (1.1)
- p.8-15: Quantum States (1.2)
- p.16-20: References
```

#### Quarto での記述

```markdown
---
title: "Chapter 1: Introduction"
---

# Chapter 1: Introduction

## 1.1 基礎概念 [📄 chap1.pdf](/assets/pdf/preskill/chap1.pdf#page=3) {#sec-foundations}

ここでは量子情報の基礎を説明します。

## 1.2 量子状態 [📄 chap1.pdf](/assets/pdf/preskill/chap1.pdf#page=8) {#sec-quantum-states}

量子状態の定義と性質について述べます。
```

---

## 🛠️ ワークフロー実装手順

### フェーズ1: PDF構造の観測（翻訳前）

```bash
# 対象チャプターを まず読む
just process-pdf quarto/assets/pdf/preskill/chap2_15.pdf 1 10

# 出力から:
# - 実際のセクション番号（2.1, 2.2, ...）と対応ページを記録
# - テンプレートに基づいて research/guidelines/preskill_chap2_mapping.md を作成
```

### フェーズ2: マッピング表の記録

```markdown
# Preskill Chapter 2 PDF Mapping

| セクション | 見出し | 開始ページ |
|-----------|--------|----------|
| 2.1 | States and Ensembles | p.1 |
| 2.2 | Density Matrices | p.5 |
| 2.3 | Pure and Mixed | p.12 |
```

### フェーズ3: 翻訳と並行してリンク付け

```markdown
## 2.1 量子状態とアンサンブル [📄 chap2.pdf](/assets/pdf/preskill/chap2_15.pdf#page=1) {#sec-states-ensembles}

（翻訳内容）
```

### フェーズ4: プレビューで確認

```bash
just docs
# ブラウザで [📄 chap2.pdf] をクリック
# 正しいページが開くか確認（特にPDF#page番号が正確か）
```

---

## 📊 管理ファイルの位置づけ

```
research/
├── guidelines/
│   ├── preskill_pdf_mapping.md          ← このファイル（方法論）
│   ├── preskill_chap1_mapping.md        ← 実装情報（Chapter 1）
│   ├── preskill_chap2_mapping.md        ← 実装情報（Chapter 2）
│   └── preskill_chap3_mapping.md        ← 実装情報（Chapter 3）
│   └── ...
└── notes/
    ├── chap1_observations.md           ← 観測メモ（処理中）
    └── ...
```

### マッピングファイルのテンプレート

```markdown
---
name: Preskill Chapter X PDF Mapping
type: reference
---

# Preskill Chapter X: [タイトル]

| 項目 | 詳細 |
|------|------|
| **ファイル** | `chap X.pdf` |
| **ページ総数** | XX |
| **ナンバリング** | p.1 から（リセット） |

## セクション構成

| 見出し | ページ範囲 | 含まれる内容 |
|--------|-----------|------------|
| X.1 ... | p.1-Y | 定義、基本定理 |
| X.2 ... | p.Y-Z | 証明、例 |
| ... | ... | ... |

## 特記事項

- 図表の位置：p.XX
- 重要な式：p.YY
- 参考文献：p.ZZ

## 更新履歴

- 2026-04-07: 初版作成
```

---

## ⚠️ よくある落とし穴

### 1. ページ番号を統合PDFのものと混同

❌ **NG**: Watrous版の「物理ページ = 表記ページ + 8」のような計算をそのまま適用

✅ **OK**: 各チャプターのページナンバリングは独立。必ず対象PDFで確認

### 2. セクション番号とページ番号を対応付けないまま執筆

❌ **NG**: 「ページ5」と言ってるが、実際には別チャプターの内容だった

✅ **OK**: 執筆前に マッピング表を完成させてから翻訳開始

### 3. PDFリンクのページ番号が誤ったまま進行

❌ **NG**: `#page=10` で指定したが、実は `#page=8` が正しい（後から修正しづらい）

✅ **OK**: `just docs` で常に確認しながら作業

---

## 🔍 チェックリスト

新しいチャプターを開始する際：

- [ ] `just process-pdf` で対象PDF の最初の 10 ページを確認
- [ ] セクション開始ページを記録（マッピング表作成）
- [ ] `research/guidelines/preskill_chapX_mapping.md` を作成
- [ ] 翻訳ファイルの各セクション見出しに PDFリンク を付ける
- [ ] `just docs` で各リンクをテスト（正しいページが開くか確認）
- [ ] `just check` で Quarto 構文エラーがないか確認

---

## 📚 関連ドキュメント

- `AGENTS.md` → PDFリンク戦略（大方針）
- `quarto_heading_numbering.md` → 見出し番号と参照の実装
- `research/guidelines/preskill_chapX_mapping.md` → 各チャプター固有のマッピング情報

