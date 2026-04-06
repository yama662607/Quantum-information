# Quarto 見出し番号付けガイド（プロジェクト版）

このガイドは、John Preskill / Watrous 教科書プロジェクトで見出し番号を実装するための実務向けリファレンスです。

---

## 📋 このプロジェクトでの推奨設定

### 基本方針

本プロジェクトでは、教科書形式のため以下の設定を推奨します：

```yaml
# _quarto.yml（プロジェクト全体設定）
toc: true                    # 目次を出す
number-sections: true        # 見出し番号を有効化
number-depth: 2              # 2階層まで番号付け（章.節）
```

これにより：
- **H1（# 見出し）** → 1, 2, 3, ...（章番号）
- **H2（## 見出し）** → 1.1, 1.2, 2.1, ...（節番号）
- **H3（### 見出し）** → 番号なし（可読性重視）

---

## 🎯 実装パターン

### パターン1: 標準的な教科書構成（推奨）

#### _quarto.yml
```yaml
project:
  type: default

toc: true
toc-depth: 3
number-sections: true
number-depth: 2

format:
  html:
    theme: cosmo
    number-sections: true
    number-depth: 2
  pdf:
    number-sections: true
    number-depth: 2
    top-level-division: chapter    # PDF では H1 を「章」として扱う
```

#### 個別 .qmd ファイル（断片）
```markdown
## 2.1 量子状態 {#sec-quantum-states}

### 定義

密度行列 $\rho$ は以下を満たします：

- 正定値性：$\rho \succeq 0$
- トレース条件：$\mathrm{Tr}(\rho) = 1$

### 物理的解釈

$\rho$ の固有値を $\{p_i\}$、固有ベクトルを $\{|\psi_i\rangle\}$ とするとき...
```

#### マスターファイル（textbook.qmd）での参照
```markdown
---
title: "Quantum Information Study Notes"
number-sections: true
number-depth: 2
---

{{< include chapter1/_1.1-introduction.qmd >}}
{{< include chapter2/_2.1-quantum-states.qmd >}}
```

---

## 🚫 特定見出しを番号なしにする

### 例：序文、参考文献、付録

```markdown
# はじめに {.unnumbered}

このプロジェクトについて説明します。

---

# 参考文献 {.unnumbered}

- Preskill, J. (2024) Quantum Computation...
```

### さらに目次からも消したい場合

```markdown
# 執筆者向けメモ {.unnumbered .unlisted}

（AIエージェント向けの内部メモなど）
```

---

## 🔗 節参照の使用方法（重要）

見出し番号と連動した参照を使うには、**必ず `{#sec-...}` ラベルを付けてください**。

### 推奨: 明示的ラベル付け

```markdown
## 測定の公理系 {#sec-measurement-axioms}

詳細は @sec-measurement-axioms で説明します。
```

### 参照記法のバリエーション

| 記法 | 出力例 | 用途 |
|------|--------|------|
| `@sec-id` | "Section 1.2" | 標準的な参照 |
| `@sec-id.` | "Section 1.2." | 文末参照（ピリオド付き） |
| `[-@sec-id]` | "1.2" | 番号のみ（プレフィックスなし） |
| `[see @sec-id]` | "see Section 1.2" | カスタムプレフィックス |

---

## 📊 図表の章ごと番号付け

教科書では「Figure 2.1, 2.2, 3.1」のように章ごとに番号を分けたいことが多いです。

```yaml
# _quarto.yml
crossref:
  chapters: true
```

すると：

```markdown
## 量子回路

![ベル状態準備](bell-circuit.png){#fig-bell-circuit}

図 @fig-bell-circuit はベル状態を生成します。
```

出力：`Figure 1.1（第1章の1番目の図）`

---

## ⚙️ Preskill版とWatrous版の番号付けを分ける

（オプション）異なる章番号体系が必要な場合：

### Preskill版（`quarto/textbook-preskill/textbook.qmd`）
```yaml
---
title: "Preskill版"
number-sections: true
number-depth: 2
---
```

### Watrous版（`quarto/textbook-watrous/textbook.qmd`）
```yaml
---
title: "Watrous版"
number-sections: true
number-depth: 2
---
```

各 `textbook.qmd` で独立した番号体系が成立します。

---

## 🔧 テンプレート統合

### quantum_textbook_template.qmd での推奨記述

```markdown
## XXX {#sec-xxx}

### YYY {#sec-xxx-yyy}

...内容...

### ZZZ {#sec-xxx-zzz}

...内容...
```

**ルール**：
- セクション見出しには必ず `#sec-` ラベルを付ける
- ラベルに**アンダースコア `_` を使わない**（ハイフン `-` を使用）
- サブセクション以下は参照が不要なら省略可

---

## ⚠️ よくある落とし穴

### 1. number-sections がない

```yaml
# ❌ 番号が出ない
title: "My Doc"
```

```yaml
# ✅ これが必須
number-sections: true
```

### 2. ラベルが sec- で始まっていない

```markdown
# ❌ 参照が成立しない
## 背景 {#background}

@background は機能しません。
```

```markdown
# ✅ 正しい形式
## 背景 {#sec-background}

@sec-background は機能します。
```

### 3. ラベルにアンダースコアを使う

```markdown
# ⚠️ PDF/LaTeX で問題が起きる可能性
## データ処理 {#sec-data_processing}
```

```markdown
# ✅ ハイフンを使う
## データ処理 {#sec-data-processing}
```

### 4. 番号なし章（.unnumbered）で figure 参照を多用

```markdown
# 謝辞 {.unnumbered}

図 @fig-xxx を参照する...  ← クロスリファレンスに問題が出る可能性
```

**→ 解決策**: 番号なし見出しは序文・謝辞・参考文献に限定し、本文内容は番号付きにする。

### 5. number-offset が PDF で効かない

```yaml
# ⚠️ HTML/Docx では機能、PDF では期待通りにならない可能性
number-offset: 5
```

**→ 解決策**: PDF 中心の運用なら、見出し構成や章番号設定で吸収する。

---

## 📋 実装チェックリスト

新しい章を追加する際の確認項目：

- [ ] `_quarto.yml` で `number-sections: true` と `number-depth` が設定されている
- [ ] 各セクション見出しに `{#sec-xxx}` ラベルが付いている
- [ ] ラベルにはハイフン `-` のみ、アンダースコア `_` は使っていない
- [ ] 参照は `@sec-xxx` 形式で記述している
- [ ] 序文・参考文献など必要な見出しに `.unnumbered` が付いている
- [ ] HTML と PDF で見た目を確認済み（`just docs` と PDF出力）

---

## 🎨 日本語化の参考設定

```yaml
# _quarto.yml で日本語向けカスタマイズ
crossref:
  sec-prefix: "節"         # "Section 1.2" → "節1.2" 的な寄せ方
  fig-prefix: "図"
  tbl-prefix: "表"
  eq-prefix: "式"
```

ただし、この設定の効果はフォーマットや Pandoc バージョンに依存するため、**出力を確認して調整することを推奨します**。

---

## 📚 参考資料

- **Quarto 公式**: https://quarto.org/docs/authoring/cross-references.html
- **Quarto PDF ガイド**: https://quarto.org/docs/output-formats/pdf-basics.html
- **本プロジェクト設定ファイル**: `quarto/_quarto.yml`
- **テンプレート**: `quarto/templates/quantum_textbook_template.qmd`
