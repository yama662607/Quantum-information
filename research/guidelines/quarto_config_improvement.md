# _quarto.yml 改善提案

## 現状分析（2025-04-07）

### 現在の設定（すでに優良）

✅ **既に適切に設定済み**：
- `number-sections: true` — 見出し番号が有効
- `crossref: chapters: true` — 図表が章ごとに番号付け（Figure 1.1, 1.2, など）
- `lang: ja` — 日本語設定

⚙️ **改善の余地あり**：
- `number-depth: 3` （現在）→ `number-depth: 2` （推奨）
- `crossref` に日本語プレフィックスが未設定
- PDF 出力で `top-level-division: chapter` が明示化されていない

---

## 🎯 推奨改善案

### 改善1: number-depth を 3 → 2 に変更

**理由**：
- 3階層の全番号付けは、教科書では視覚的に見づらくなりやすい
- H3（### 見出し）が「1.2.3」のように深くなると、本文の可読性が低下
- H3 は補助的な説明（定義の補足、例の詳細）であることが多く、番号不要な場合が多い

**変更前**：
```yaml
number-depth: 3
```

**変更後**：
```yaml
number-depth: 2
```

**効果**：
- `## 見出し` まで採番 → 1.1, 1.2, など
- `### 見出し` は番号なし → より読みやすい

---

### 改善2: crossref に日本語プレフィックスを追加

**理由**：
参照が「Section 1.1」ではなく「節 1.1」のような日本語寄りになり、読み文脈がより自然になる。

**追加設定**：
```yaml
crossref:
  chapters: true
  sec-prefix: "節"
  fig-prefix: "図"
  tbl-prefix: "表"
  eq-prefix: "式"
```

**出力例**：
- `@sec-background` → "節 1.1"（現状: "Section 1.1"）
- `@fig-example` → "図 1.1"（現状: "Figure 1.1"）

**注意**：
- この設定の効果はパンドック / ブラウザバージョンに左右される可能性あり
- 改善後は HTML / PDF 両方で視覚的に確認が必要

---

### 改善3: PDF 出力で top-level-division を明示化

**理由**：
PDF では H1 を「章」として明確に扱うことで、レイアウトや改ページが教科書らしくなる。

**変更前**：
```yaml
format:
  pdf:
    include-in-header: preamble.tex
    pdf-engine: xelatex
```

**変更後**：
```yaml
format:
  pdf:
    include-in-header: preamble.tex
    pdf-engine: xelatex
    top-level-division: chapter
    number-sections: true
    number-depth: 2
```

**効果**：
- PDF 出力で H1 が「Chapter 1」のように章題扱いされる
- 改ページが自動的に挿入されるなど、教科書らしい構成になる

---

## 📋 推奨修正案（_quarto.yml の該当部分）

```yaml
# ✅ 既存（保持）
number-sections: true

# 🔧 改善（変更）
number-depth: 2

# ✅ 既存（拡張）
crossref:
  chapters: true
  sec-prefix: "節"
  fig-prefix: "図"
  tbl-prefix: "表"
  eq-prefix: "式"

# ... その他既存設定 ...

format:
  html:
    # ... 既存設定 ...
  pdf:
    include-in-header: preamble.tex
    pdf-engine: xelatex
    top-level-division: chapter         # 新規追加
    number-sections: true                # 明示化（冗長だが安全）
    number-depth: 2                      # 明示化（冗長だが安全）
```

---

## ✅ 実施手順

1. **テスト環境で確認**（推奨）
   ```bash
   just docs  # HTML プレビューで日本語参照の見た目を確認
   # PDF 出力も確認（Quarto で PDF render）
   ```

2. **問題がなければ反映**
   - `_quarto.yml` を上記の改善案で更新

3. **全文書の検証**
   ```bash
   just check
   ```

4. **レンダリング確認**
   ```bash
   just docs
   ```

---

## ⚠️ リスク評価

| 項目 | リスク | 対策 |
|------|--------|------|
| number-depth 変更 | 既存文書の見出し階層が変わって見える | テストで事前確認 |
| crossref 日本語化 | 出力フォーマットによっては反映されない | HTML/PDF 両フォーマット確認 |
| top-level-division | PDF レイアウトが変わる | Preamble との相互作用を確認 |

**総合判定**：低リスク。テストで視覚確認すれば安全に反映可能。

