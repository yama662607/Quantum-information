# 量子アルゴリズム第1回改訂・第2回新設・音声解説動画制作 実施記録＆レビュー依頼書

- **作成日**: 2026年10月26日
- **対象コミット**: `9b68ff3` (`feat(qiskit): add Lesson 2 (BV, drug discovery phase estimation, Shor, 2026 frontier), revise Deutsch lesson, and add 4 voiced 1080p Manim lecture videos`)
- **目的**: 別エージェントが今回の制作物（Quarto教材・Qiskit/Pyodideシミュレーション・Manim音声付き1080p解説動画4本・科学イラスト2枚）を多角的にレビューできるよう、設計意図・全変更ファイル・教育的工夫・検証結果を網羅的に記録する。

---

## 1. 背景とユーザー要件（なぜこれを作ったか）

前回のゼミ（第1回：量子回路の読み方と基本アルゴリズム）を終えて、ユーザーから以下の課題と要望が提示された。

1. **前回の到達点と課題**:
   - 前回は [algorithms.qmd](/quarto/qiskit/algorithms.qmd) の補講（「同じ回路を第2・3章の言葉で読む」）の手前まで進んだ。
   - 量子回路の記号の読み方や手計算の方法は全員理解できたが、**「なぜ量子コンピュータに優位性があるのか」「なぜこんなに注目されているのか」が実感できず、単なるパズルを解いている感覚**にとどまっていた。
   - 特に **Deutsch のアルゴリズム**について、「なぜ標的ビットを $|-\rangle$ にするのか」「なぜその回路を思いつけるのか」が天下り的（AIが作ったこじつけのよう）に感じられ、自分では到底思いつけないという強い違和感があった。
2. **第2回ゼミに向けた要望**:
   - **「階段の上り幅（説明の飛躍）を極限まで小さくする」**: 本質にたどり着く前の計算やテクニック、天下り的な定義で頭がいっぱいにならないよう、伏線・素朴な失敗例・手計算・図解・インタラクティブシミュレーション・動画を総動員して、1段ずつ自然に登れる構成にする。
   - **Deutsch のアルゴリズムの再構築**: 前回のページ（`algorithms.qmd` 内の `_06-design-deutsch.qmd`）を、バックアップを残した上で「素朴な回路の失敗」から自然に導出するストーリーへ一から書き直す。
   - **前回の補講以降の切り出しと刷新**: 前回扱わなかった補講以降は第2回（`algorithms-part2.qmd`）へ移し、既存の下書きに縛られず一から作り直す。
   - **創薬（量子化学）への応用とオリジナル例題**: ユーザーが強く関心を持っている「創薬分野での応用」をメインテーマの一つに据え、複雑な分子計算の細部に溺れずに本質（ハミルトニアンの固有エネルギー＝位相の回転速度の推定）を肌感覚で理解できる**オリジナル例題**を設計する。
   - **いつ量子が古典に勝てるのかの直感**: どんな問題なら量子コンピュータで速くなるのか、2025〜2026年現在の世界の最前線はどうなっているのかを整理する。
   - **高品質な音声付き解説動画の制作**: ゼミ冒頭で流す復習動画を含め、ローカルTTS音声・科学イラスト・Manimアニメーションを組み合わせた1080p解説動画を複数本制作し、教材に埋め込む。

---

## 2. 成果物一覧とファイルマップ

### 2.1 Quarto 教科書教材（改訂・新設）

| 区分 | ファイルパス | 内容と教育的役割 |
| :--- | :--- | :--- |
| **第1回 親ファイル** | [quarto/qiskit/algorithms.qmd](/quarto/qiskit/algorithms.qmd) | 冒頭に Episode 1 音声解説動画を埋め込み。末尾の旧補講 (`_07`, `_08`) の include を外し、第2回へのブリッジを配置。 |
| **第1回 第6節（全面改訂）** | [quarto/qiskit/algorithms/_06-design-deutsch.qmd](/quarto/qiskit/algorithms/_06-design-deutsch.qmd) | **「失敗から発明する Deutsch のアルゴリズム」**。素朴な回路（標的 $|0\rangle$）がなぜ失敗するかを密度行列・部分トレースと手計算の両面で示し、「標的が変化すると制御の干渉が消える → 標的不変な固有状態 $|-\rangle$ を探す」という必然的な発見プロセスに全面改訂。 |
| **第1回 軽微修正** | [quarto/qiskit/algorithms/_01-single-qubit-gates.qmd](/quarto/qiskit/algorithms/_01-single-qubit-gates.qmd)<br/>[quarto/qiskit/algorithms/_05-computing-a-function.qmd](/quarto/qiskit/algorithms/_05-computing-a-function.qmd) | クロスリファレンスおよび表記の整合性調整。 |
| **旧ファイル退避** | [research/notes/backups/_06-design-deutsch.bak.qmd](/research/notes/backups/_06-design-deutsch.bak.qmd)<br/>`research/notes/backups/_07-*.bak.qmd`, `_08-*.bak.qmd` | 改訂前の `_06` の完全バックアップ。 |
| **第2回 親ファイル（新設）** | [quarto/qiskit/algorithms-part2.qmd](/quarto/qiskit/algorithms-part2.qmd) | 第2回ゼミ用メインページ。Pyodide (`numpy`, `matplotlib`) + ダミー `{ojs}` ローダー設定、4本の動画ナビゲーション、全6節の統合、確認クイズ・まとめを収録。 |
| **第2回 第1節（新設）** | [quarto/qiskit/algorithms-part2/_01-trap-of-superposition.qmd](/quarto/qiskit/algorithms-part2/_01-trap-of-superposition.qmd) | **「重ね合わせだけでは速くならない」**。全入力を重ね合わせて計算しても、そのまま測定すれば確率 $1/2^n$ のランダム抽出にしかならないこと、さらに標的ビットとのエンタングルメントが制御ビットのコヒーレンス（非対角成分）を破壊することを Preskill 第2・3章の密度行列 $\rho_A = \mathrm{Tr}_B(\rho_{AB})$ で回収。 |
| **第2回 第2節（新設）** | [quarto/qiskit/algorithms-part2/_02-secret-key-bv.qmd](/quarto/qiskit/algorithms-part2/_02-secret-key-bv.qmd) | **「1回の質問で秘密の鍵を抜く（Bernstein–Vazirani）」**。Deutsch の1ビット判定を $n$ ビットの秘密鍵 $s \in \{0,1\}^n$ 特定へ拡張。内積オラクル $f_s(x) = s \cdot x \bmod 2$ とテンソル積の分解 $(H^{\otimes n}|0\rangle^{\otimes n})$ により、古典で $n$ 回必要なクエリが量子なら **1回** で完了することを手計算・Qiskit・Pyodide で実証。Episode 2 動画を埋め込み。 |
| **第2回 第3節（新設）** | [quarto/qiskit/algorithms-part2/_03-why-quantum-chemistry.qmd](/quarto/qiskit/algorithms-part2/_03-why-quantum-chemistry.qmd) | **「なぜ創薬に量子コンピュータなのか？」**。薬の候補分子（リガンド）と標的タンパク質の結合親和性が基底状態エネルギー差 $\Delta E = E_{\text{complex}} - (E_{\text{protein}} + E_{\text{ligand}})$ で決まること、室温での化学精度（$\sim 1.6 \text{ mHa} \approx 1 \text{ kcal/mol}$）が結合定数を約5倍左右すること、電子相関により古典メモリが $O(2^N)$ で爆発する理由を解説。 |
| **第2回 第4節（新設）** | [quarto/qiskit/algorithms-part2/_04-measuring-phase-clock.qmd](/quarto/qiskit/algorithms-part2/_04-measuring-phase-clock.qmd) | **「見えないエネルギーを『時計の針』に変える（Hadamard Test / 位相推定）」**。シュレーディンガー方程式の時間発展 $U(t) = e^{-i\widehat{H}t/\hbar}$ が固有状態 $|\psi\rangle$ に位相 $e^{-iEt/\hbar}$ を刻むことに着目。全体位相はそのままでは測定できないが、補助ビット（アンシラ）を用いた **制御時間発展（Hadamard Test）** によって位相キックバックを起こせば、測定確率 $P(0) = \cos^2(\theta/2)$ としてエネルギーを読み出せることを導出。 |
| **第2回 第5節（新設）** | [quarto/qiskit/algorithms-part2/_05-drug-discovery-example.qmd](/quarto/qiskit/algorithms-part2/_05-drug-discovery-example.qmd) | **「オリジナル例題：1量子ビット創薬ポケットモデル $\widehat{H} = -gX$」**。リガンドの2つの配座 $|0\rangle, |1\rangle$ 間の量子トンネル結合を表す最小ハミルトニアン $\widehat{H} = -gX$ を題材に、候補薬 A・B・C の結合強度 $g$（および基底エネルギー $E_0 = -g$）を量子回路で決定するハンズオン例題。手計算・Qiskit 実装・ブラウザ上で時刻 $t$ やショット数を変えて推定できる **Pyodide インタラクティブ実験室**・Episode 3 動画を収録。 |
| **第2回 第6節（新設）** | [quarto/qiskit/algorithms-part2/_06-shor-and-frontier-2026.qmd](/quarto/qiskit/algorithms-part2/_06-shor-and-frontier-2026.qmd) | **「Shor の因数分解と 2025–2026 最前線マップ」**。$N=15, a=7$ の周期発見 $f(x) = 7^x \bmod 15$（周期 $r=4 \Rightarrow \gcd(7^2\pm 1, 15) = 3, 5$）を完全に手計算で追い、化学のエネルギー推定も暗号の因数分解も**同じ「位相・周期の干渉抽出」**であることを統合。最後に「どんな問題なら量子が速いか」の4分類マップと、2024〜2026年の最新動向（Google Willow、論理量子ビット実証、Quantinuum / QuEra / IBM Quantum-Centric Supercomputing）を整理。Episode 4 動画を収録。 |
| **ナビゲーション更新** | [quarto/_quarto.yml](/quarto/_quarto.yml)<br/>[quarto/index.qmd](/quarto/index.qmd)<br/>[quarto/qiskit/index.qmd](/quarto/qiskit/index.qmd) | サイドバーおよびトップページ目次に第2回教材（`algorithms-part2.qmd`）を追加。 |

---

### 2.2 音声付き 1080p Manim 解説動画（全4本・計約11分）と科学イラスト

ローカル TTS モデル（`Irodori-TTS-v4.1-Small-MF-fp16`, 48 kHz）による日本語ナレーション、WebVTT 字幕（`.vtt`）、ポスター画像（`.jpg`）、タイムスタンプメタデータ（`.lesson.json`）を備えた 1920×1080 @ 30fps の MP4 動画を4本制作した。

| エピソード | 動画ファイル / 尺 | スクリプト | 主な内容・視覚演出 |
| :--- | :--- | :--- | :--- |
| **Episode 1**<br/>ゼミ冒頭復習＆Deutsch導出 | [ep1-recap-and-deutsch.mp4](/quarto/assets/videos/ep1-recap-and-deutsch.mp4)<br/>**3分22秒** (202.8s)<br/>8チャプター | [ep1_recap_and_deutsch.py](/tools/quantum_videos/ep1_recap_and_deutsch.py) | 1. 前回の復習（量子回路の読み方、振幅と確率）<br/>2. なぜパズルに見えるのか？（素朴な並列計算の罠）<br/>3. 標的ビットを $|0\rangle$ にした素朴な回路の失敗（分岐による干渉の消失）<br/>4. 逆転の発想：$X$ ゲートで変わらない固有状態 $|-\rangle$ の発見<br/>5. 位相キックバックの視覚化と Deutsch 回路の完成 |
| **Episode 2**<br/>秘密の鍵とBVアルゴリズム | [ep2-secret-key-bv.mp4](/quarto/assets/videos/ep2-secret-key-bv.mp4)<br/>**2分38秒** (158.5s)<br/>6チャプター | [ep2_secret_key_bv.py](/tools/quantum_videos/ep2_secret_key_bv.py) | 1. 1ビットから $n$ ビットの秘密鍵 $s=101$ 探しへ<br/>2. 古典クエリ（1ビットずつ $n$ 回質問）の限界<br/>3. 内積オラクルと各ビット独立な位相キックバック $(-1)^{s_i x_i}$<br/>4. 一斉 Hadamard 変換による **1回クエリでの鍵完全復元** |
| **Episode 3**<br/>創薬と位相の時計（Hadamard Test） | [ep3-drug-discovery-phase.mp4](/quarto/assets/videos/ep3-drug-discovery-phase.mp4)<br/>**2分34秒** (154.9s)<br/>7チャプター | [ep3_drug_discovery_phase.py](/tools/quantum_videos/ep3_drug_discovery_phase.mp4)<br/>([.py](/tools/quantum_videos/ep3_drug_discovery_phase.py)) | 1. 創薬における結合エネルギー $\Delta E$ と古典メモリの指数爆発<br/>2. AI生成科学イラスト [img_drug_pocket.jpg](/quarto/assets/videos/img_drug_pocket.jpg) / [img_phase_clock_hero.jpg](/quarto/assets/videos/img_phase_clock_hero.jpg) を用いた導入<br/>3. 時間発展 $e^{-i\widehat{H}t/\hbar}$ と「見えない位相の時計」の回転アニメーション<br/>4. Hadamard Test による位相の可視化と $\widehat{H}=-gX$ 創薬ポケットモデルの比較実証 |
| **Episode 4**<br/>Shorの周期発見と2026最前線 | [ep4-shor-and-frontier.mp4](/quarto/assets/videos/ep4-shor-and-frontier.mp4)<br/>**2分28秒** (148.8s)<br/>6チャプター | [ep4_shor_and_frontier.py](/tools/quantum_videos/ep4_shor_and_frontier.py) | 1. RSA暗号と $N=15$ の因数分解<br/>2. べき乗剰余 $7^x \bmod 15$ の周期 $r=4$ のグラフ・時計アニメーション<br/>3. 量子フーリエ変換（QFT）による周期ピークの干渉抽出<br/>4. 量子優位性の4分類マップと 2025–2026 最前線（論理量子ビット・創薬ハイブリッド） |

#### 動画生成パイプライン（`tools/quantum_videos/`）
- [voiced_engine.py](/tools/quantum_videos/voiced_engine.py): Manim `Scene` を継承した `VoicedQuantumScene` 基底クラス。16:9 セーフエリアフレーム、上部プログレスヘッダ、下部ガラスモーフィズム字幕バー、チャプター間の安全なフェードトランジション、複数ボイスセグメントとアニメーション尺の完全同期（`play_synced`）を提供。
- [build_pipeline.py](/tools/quantum_videos/build_pipeline.py): `Irodori-TTS-v4.1-Small-MF-fp16` による 48 kHz 音声合成、Whisper ASR (`http://127.0.0.1:8001/v1/audio/transcriptions`) による読み誤り検査、Manim 1080p レンダリング、`ffmpeg` による音声マージ・ラウドネス正規化・ポスター抽出・WebVTT 字幕生成を自動化。
- [render_all.py](/tools/quantum_videos/render_all.py): 全4エピソードの一括ビルドスクリプト。

---

## 3. 教育設計上の工夫（階段の段差をどう解消したか）

1. **「なぜ失敗するか」を先に体験させる構成**:
   - Deutsch でも位相推定でも、いきなり正解の回路を出さず、「普通に考えたらこう作るはず（標的 $|0\rangle$ に重ね合わせを入れる／固有状態をそのまま測定する）」という素朴な回路を先に計算させ、**なぜそれでは情報が消えるのか**を納得させてから、それを解決する唯一の方法として $|-\rangle$ や制御時間発展を導入した。
2. **Preskill 第2・3章（密度行列・部分トレース・ユニタリ時間発展）との有機的接続**:
   - 「第3章までせっかく難しい数学を学んだのにアルゴリズムとの関係がわからない」という悩みを解消するため、部分トレース $\mathrm{Tr}_B(|\Psi\rangle\langle\Psi|)$ によって非対角項（干渉項）が $\langle f(0)|f(1)\rangle$ の内積倍だけ減衰する式を明示し、「抽象的な部分トレースの定義は、実は『標的ビットに情報が漏れると制御ビットの干渉が消える』ことを表していたのか！」と膝を打てる構成にした。
3. **創薬のリアルな文脈と手計算可能な最小モデルの両立**:
   - いきなり Jordan–Wigner 変換や数十量子ビットの VQE/QPE を出すと前処理だけで挫折するため、「なぜ創薬で基底エネルギー差 $\Delta E$ が必要なのか（化学精度 $1.6\text{ mHa}$ の意味）」を丁寧に語った上で、物理的意味を保った最小モデル $\widehat{H} = -gX$ に落とし込み、**手計算でも Qiskit でもブラウザ上のスライダー（Pyodide）でも100%追える**ようにした。
4. **TTS ナレーションの自然な韻律チューニング**:
   - ローカル TTS (`Irodori-TTS`) の特性を検証し、全文ひらがなではなく「通常の漢字かな交じり文＋英語・数式記号のみカタカナ表記（例：`エックスゲート`、`エイチゲート`、`シータ`、`コサイン二乗`）」とすることで、アクセント句の境界とイントネーションが最も自然になるよう全27チャプターの台本を調整し、Whisper ASR で読みを確認した。

---

## 4. 実施済みの検証・内部レビュー

1. **サブエージェント2名による独立レビューと修正反映**:
   - **教育構成・日本語表現レビュー** (`51d2bff4-caa6-48aa-8cd5-818c7eefc195`): 説明の飛躍、用語の初出定義、手計算の途中式の丁寧さ、読者目線でのつまずきポイントを監査し、補足説明やステップ展開を反映。
   - **Quarto機能・数式・視覚表現レビュー** (`a0b03705-9945-47f1-b93f-679516c2a92b`): Callout / panel-tabset / Mermaid 図式 / Pyodide セル / LaTeX 数式タグ・クロスリファレンスを監査し、すべて修正反映。
2. **動画全チャプターのフレーム画像抽出・目視検査**:
   - 全4本の動画（計27チャプター）について各チャプターの静止画フレームを `ffmpeg` で抽出し、テキストのはみ出し・重なり・コントラスト・数式表示を1枚ずつ目視確認。長い文字列の横幅スケーリング（`scale_to_fit_width`）等を調整して再レンダリング済み。
3. **ビルド・品質ゲート検証**:
   - `just fix` および `just check`（Ruff lint/format、Quarto 構造・Fenced Div・Mermaid・LaTeX 検証）：**0 errors で全件 PASS**。
   - `uv run quarto render quarto/qiskit/algorithms.qmd --to html` および `uv run quarto render quarto/qiskit/algorithms-part2.qmd --to html`：両ページともエラーなく HTML 出力および埋め込み Python コード実行が完了することを確認済み。

---

## 5. 別エージェントへのレビュー依頼観点（推奨チェックリスト）

このドキュメントおよび対象ファイルをレビューする別エージェントには、特に以下の観点から厳しくチェックしてもらうことを推奨します。

1. **階段の段差（教育的飛躍）の有無**:
   - [quarto/qiskit/algorithms/_06-design-deutsch.qmd](/quarto/qiskit/algorithms/_06-design-deutsch.qmd) および [quarto/qiskit/algorithms-part2.qmd](/quarto/qiskit/algorithms-part2.qmd)（`_01`〜`_06`）を前から順に読んだとき、「なぜこの式変形になるのか」「なぜこのゲートを置くのか」が一箇所でも天下りに見える部分はないか？
   - 特に第2回 `_04-measuring-phase-clock.qmd`（Hadamard Test による位相推定）と `_05-drug-discovery-example.qmd`（$\widehat{H}=-gX$ モデル）の接続で、初学者が混乱しそうな記号や暗黙の前提が残っていないか？
2. **数式・物理・量子情報理論の厳密性と正確性**:
   - 密度行列・部分トレースの式、時間発展演算子 $U(t) = \exp(-i\widehat{H}t/\hbar)$ の符号と位相キックバックの向き、Shor の $N=15, a=7$ の具体的な状態遷移と連分数展開の説明に数学的・物理的な不正確さはないか？
   - 2025〜2026年の量子コンピュータ最前線（`_06-shor-and-frontier-2026.qmd`）の記述に誇張や事実誤認はないか？
3. **Quarto / Pyodide / 動画連携の UX**:
   - 動画プレイヤー・Mermaid図・Callout・`panel-tabset`・Pyodide シミュレーションの配置バランスは適切か？情報過多で読みづらくなっている箇所や、逆に図解が足りない箇所はないか？
4. **動画スクリプト（`tools/quantum_videos/ep1`〜`ep4`）と教材本文の一貫性**:
   - 動画内のナレーション・記号表記と、教材本文の記号表記にズレがないか？
   - ゼミ発表（約2時間）で実際に流して使う際、さらに改善できる演出や補足はあるか？

---

## 6. クイック確認コマンド（レビュアー用）

```bash
# 1. 変更差分の一覧確認
git show --stat 9b68ff3

# 2. 品質ゲート・構造チェックの実行
just check

# 3. プレビューサーバーの起動（ブラウザで http://localhost:4321 等を確認）
just docs

# 4. 動画を再生成する場合（ローカル TTS サーバー起動時）
uv run python tools/quantum_videos/render_all.py
```
