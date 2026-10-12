# Mac Studio 移行 & エージェント作業引き継ぎドキュメント

本ドキュメントは、Quantum Information 教科書プロジェクトの作業環境を **Mac Studio（`studio`）** へ移行し、Phase 1（完全文字起こし・忠実和訳）および Phase 2（物理解説・シミュレーション）を継続するための引き継ぎ書です。

---

## 1. Mac Studio (`studio`) の環境構成

Mac Studio 側の環境構築および全自動テスト（`just check`）の動作確認が完了しています。

| 項目 | 設定値 / パス | 備考 |
| :--- | :--- | :--- |
| **Tailscale ホスト名 / IP** | `studio` (`100.94.63.34`) | `ssh studio` で相互ログイン可能 |
| **メインリポジトリ** | `/Users/daisukeyamashiki/Code/Learning/Quantum-information` | `master` ブランチ |
| **作業用 Worktree** | `/Users/daisukeyamashiki/Code/Learning/Quantum-information` | `feature/phase1-transcription-and-faithful-translation` |
| **Python / 仮想環境** | `uv 0.11.15` (CPython 3.12.13) | `.venv` 同期済み (`qiskit`, `torch`, `pymupdf` 完備) |
| **Node / JavaScript** | `bun 1.3.14` | `jsdom`, `mermaid`, `dompurify` 完備 |
| **タスクランナー** | `just 1.58.0` | `/opt/homebrew/bin/just` |
| **静的サイト生成** | `quarto 1.10.18` | `/Applications/quarto/bin/quarto` |
| **最新数式 OCR** | `mineru 4.0.12` | `uv tool install mineru` により導入済み (UniMERNet) |

---

## 2. 現在の進捗状況 (Preskill Chapter 2)

### ✅ 完了した作業 (PR #2 作成済み)
- **Section 2.5 (アンサンブル解釈の曖昧さ / Ambiguity of the ensemble interpretation)**:
  - 英語文字起こし: `research/transcripts/preskill/chapter2/_sec2.5_ambiguity.md` (式 2.97 〜 2.121 完全網羅)
  - Quarto 日本語和訳: `quarto/textbook-preskill/chapter2/_2.5-ambiguity.qmd`
  - 内容: 凸性、アンサンブル準備、超光速通信の不可能性、シュテルン＝ゲルラッハ量子消去、遅延選択 (Delayed choice: 式 2.110)、情報は物理的である (Information is physical)、HJW定理
- **Section 2.6 (状態間の距離 / How far apart are two quantum states?)**:
  - 英語文字起こし: `research/transcripts/preskill/chapter2/_sec2.6_distance.md` (式 2.122 〜 2.161 完全網羅)
  - Quarto 日本語和訳: `quarto/textbook-preskill/chapter2/_2.6-distance-between-quantum-states.qmd`
  - 内容: 忠実度 (Fidelity)、トレースノルム、ウールマンの定理 (Uhlmann's theorem)、距離尺度間の関係不等式
- **引き継ぎプロトコル策定**:
  - `research/guidelines/agent_handoff_protocol.md`

### 📋 次の着手タスク (Next Steps)
Preskill Chapter 2 の残りの節を、確定したワークフローで順次処理します。

1. **Section 2.1**: 状態の重ね合わせ (Superposition of states) [📄 p.1-8]
2. **Section 2.2**: シュミット分解 (Schmidt decomposition) [📄 p.9-14]
3. **Section 2.3**: エンタングルメントの幾何学 (Geometry of entanglement) [📄 p.15-20]
4. **Section 2.4**: デコヒーレンス (Decoherence) [📄 p.21-25]
5. **Section 2.7**: 演習問題 (Exercises) [📄 p.42-45]

---

## 3. 確定した標準ワークフロー（三重照合パイプライン）

Mac Studio 上で作業するエージェントは、以下の手順を厳守して作業してください。

### 実行コマンド例（Mac Studio 上）

```bash
# 作業ディレクトリへ移動
cd /Users/daisukeyamashiki/Code/Learning/Quantum-information

# 1. PDF ページの画像化 (例: Section 2.1 の p.1〜p.8)
just render-pdf quarto/assets/pdf/preskill/chap2.pdf 1 8

# 2. テキスト・数式の抽出
just extract-content quarto/assets/pdf/preskill/chap2.pdf 1 8

# 3. エージェントの視覚確認
# view_file ツールで /tmp/page_1.png 〜 /tmp/page_8.png を順次開き、
# 添字・太字・式番号を OCR テキストと 100% 照合・修正

# 4. 英語文字起こしファイルの作成
# research/transcripts/preskill/chapter2/_sec2.1_superposition.md

# 5. Quarto 忠実和訳の作成
# quarto/textbook-preskill/chapter2/_2.1-superposition-of-states.qmd

# 6. 品質ゲートの実行（Ruff, LaTeX, Mermaid, Quarto HTML Render）
just check
```

---

## 4. Phase 2（物理専門エージェント）への引き継ぎルール

Phase 1 エージェントが作成した `research/transcripts/` 配下の英語文字起こし Markdown は、Phase 2 エージェントのための信頼できる情報源です。

- **Phase 2 エージェントの役割**:
  - 原文 PDF の画像を開き直す必要はありません。
  - `research/transcripts/` の正確な英語原文・LaTeX 式番号を基に、直感的解説（Callout）、可換図式（Mermaid）、Qiskit 実装例、対話シミュレーション（Quarto Live）を追加します。
  - 既存の Phase 1 翻訳文を破壊・省略してはなりません。解説は `callout-note` や新規サブセクションとして追記します。
