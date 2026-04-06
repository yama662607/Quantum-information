# 執筆方針書（Preskill版自主ゼミ）

> [!IMPORTANT]
> このドキュメントは、John Preskill 教授の講義ノートの解説執筆において、AIエージェントとゼミメンバーの**全員が従うべき最優先ルール**を定めています。

---

## 🚨 ゴールデンルール（絶対に守ること）

**Phase 1（忠実翻訳）の段階では、原文の次の要素を一つも省略してはならない：**

- 定義 (Definition)
- 定理 (Theorem)
- 補題 (Lemma)
- 系 (Corollary)
- 証明 (Proof)
- 補足 (Remark / Note)
- 脚注 (Footnote)
- すべての式番号（例: (2.109)）
- 章・節・小節のタイトルおよびその番号

**「概念を理解しながら書く」ことと「全文を省略なく訳す」ことは別の作業です。Phase 1 では後者だけに集中してください。**

---

## 📋 二段階執筆サイクル

### Phase 1: 忠実翻訳（Faithful Translation）

**目的**: 原文の情報を100%日本語化する。

**手順**:
1. `just process-pdf <pdf> <start> <end>` で対象ページを解析する。
2. テキスト出力と画像を照合しながら、一文ずつ忠実に翻訳する。
3. 数式は Pix2Text の LaTeX 出力を参考にしつつ、画像と見比べて正確に入力する。
4. 定義・定理・証明は原文のラベルと番号をそのまま使う（例: `{#def-2.1}`, `{#thm-2.3}`）。
5. 完成したら `just check` を実行し、構文エラーがないことを確認する。

**禁止事項**:
- ❌ 「ここは自明なので省略」は不可。必ず書く。
- ❌ 証明の「概要」だけを書くことは不可。全ステップを記す。
- ❌ 原文の Remark や Footnote を「重要ではない」と判断して省くことは不可。
- ❌ AI自身の言葉での「まとめ」を Phase 1 の本文に混入することは不可。

---

### Phase 2: 解説と拡充（Guided Extension）

**目的**: Phase 1 の完全訳を土台に、理解を深めるコンテンツを追記する。

**推奨要素（すべて必須ではない）**:
- **直感的解説**: `::: {.callout-note}` ブロックで、数学的直感や物理的解釈を補足する。
- **概念の接続**: Mermaid 図式で、他の定義・定理との関係を可視化する。
- **実装例**: Python / Qiskit によるコード実装（`.callout-tip` 内に配置）。
- **ゼミ発表用チェック**: 当該セクションを人に説明できるかを確認するチェックリスト（`.callout-warning collapse="true"` として折りたたむ）。

---

## 📖 専門用語統一対応表

本プロジェクトでは以下の訳語に統一します。

| 英語 | 本プロジェクトの和訳 | 備考 |
| :--- | :--- | :--- |
| Density matrix / Density operator | 密度行列 / 密度演算子 | 文脈によって使い分け（行列表現の際は「密度行列」） |
| Ensemble | アンサンブル | 音訳で統一 |
| Hilbert space | ヒルベルト空間 | |
| Quantum channel | 量子チャネル | 「チャンネル」は使わない |
| Measurement | 測定 | |
| POVM | POVM | 翻訳しない |
| Qubit | 量子ビット | |
| Tensor product | テンソル積 | |
| Trace | トレース | 音訳で統一。「跡」は使わない |
| Pure state / Mixed state | 純粋状態 / 混合状態 | |
| Partial trace | 部分トレース | |
| Unitary | ユニタリ | 「ユニタリー」は使わない |
| Entanglement / Entangled | エンタングルメント / エンタングルした | 音訳で統一 |
| Observable | 観測量 | |
| Operator | 演算子 | |
| Superposition | 重ね合わせ | |
| Normalization | 規格化 | |
| Eigenvalue / Eigenvector | 固有値 / 固有ベクトル | |

---

## 🤖 AIへの指示テンプレート

以下の定型文を使うと、AIエージェントが正確に動作します。

### Phase 1 を依頼する場合:
```
quarto/assets/pdf/preskill/chap2_15.pdf の物理ページ XX〜YY を、
Phase 1（忠実翻訳）でお願いします。
対象セクションは「X.Y タイトル」です。
```

### Phase 2 を依頼する場合:
```
textbook-preskill/chapterX/_X.Y-section.qmd に対して、
Phase 2（解説拡充）を行ってください。
特に [追加したい要素] を重点的にお願いします。
```

---

## 🗓️ ゼミ進行スケジュール例（参考）

| 週 | 対象 | Phase |
| :--- | :--- | :--- |
| 第1週 | Chapter 1: Introduction（全体） | Phase 1 → Phase 2 |
| 第2-3週 | Chapter 2: Foundations I（前半） | Phase 1 → Phase 2 |
| ... | ... | ... |
