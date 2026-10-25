# IBM Quantum Composer を活用した量子回路・手計算・設計理由 2時間ゼミ授業計画

**確認日**: 2026年10月19日  
**調査対象URL**:
- IBM Quantum Composer アプリケーション: [https://quantum.cloud.ibm.com/composer](https://quantum.cloud.ibm.com/composer)
- 公式ドキュメント: [https://quantum.cloud.ibm.com/docs/en/guides/composer](https://quantum.cloud.ibm.com/docs/en/guides/composer)
- ビット順序（Little-endian）公式解説: [https://quantum.cloud.ibm.com/docs/en/guides/bit-ordering](https://quantum.cloud.ibm.com/docs/en/guides/bit-ordering)

---

## 1. 授業の前提と位置づけ

### 対象学習者
- 量子力学および量子情報の数理基礎（Preskill Lecture Notes Chapter 2 / Chapter 3、ベクトル空間、密度行列、射影測定など）を履修済み。
- 理論的な行列計算やブラケット記法は追えるが、「なぜ量子回路ではこのゲート配置になるのか」「目的の状態や計算からどう逆算して回路を組むのか」に実践的な疑問を持っている同期学生（大学院・学部上級生）。
- 既存教材 [quarto/qiskit/algorithms.qmd](/quarto/qiskit/algorithms.qmd) の論理展開（0:状態記録 → 1:1量子ビット → 2:振幅追跡 → 3:2量子ビット → 4:回路設計 → 5:関数計算 → 6:Deutsch）に完全準拠し、それをブラウザ上の視覚的UIで追体験する。

### 授業の主眼
1. **「手計算」と「UIの可視化」の完全一致**:
   学生にまず紙で途中状態の振幅（位相・確率）を計算させ、予想を立てた上で Composer の「Inspect」ステップ実行機能で1層ずつ進め、一致を確認する。
2. **「状態ベクトルの確率」と「測定の確率的収束」の厳密な区別**:
   Composer の Probabilities パネルや Statevector パネルが表示しているのは「状態ベクトルから計算される理論確率（振幅の絶対値2乗）」であり、「有限回測定のヒストグラム（ショット）」ではないことを最初に明確化する。
3. **回路の上下とビット順序の逆転（Little-endian陷阱）の完全克服**:
   上段のワイヤ $q_0$ は状態表記 $\lvert q_1 q_0 \rangle$ では「右側の文字」になるという記法トラップを、手計算とUIの表示で対比して納得する。

---

## 2. IBM Quantum Composer 実機UI検証結果（機能・制約・仕様）

Playwright を用いて 2026年10月19日に最新の IBM Quantum Platform Composer (OpenQASM 3.0 対応版) をブラウザ操作し、各機能の挙動・制限・動作仕様を実証しました。

### (1) 実操作で確認できた機能
1. **ログイン不要の即時シミュレーション**:
   - アカウント作成やログイン（Sign in）を行わなくても、ブラウザ上で全回路編集、理論状態ベクトル計算、Probabilities パネル、Statevector パネル、Q-sphere パネルが完全にリアルタイム動作する。
   - ログインが要求されるのは「Set up and run」（実機バックエンドへのジョブ投入やクラウド保存）のみ。ゼミ授業は完全無料・ログイン不要で成立する。
2. **コードエディタと回路図の双方向同期**:
   - 右側パネルで **OpenQASM 3.0** と **Qiskit (Python)** の表示・切替が可能。
   - OpenQASM 3.0 コードをエディタに直接ペーストすると、即座に中央のグラフィカル回路図と下部の状態シミュレーションに反映される。
3. **強力なステップ実行機能（Inspect モード）**:
   - ツールバーの「Inspect」トグルスイッチを ON にすると、回路の「最初の初期状態 $|0\dots 0\rangle$」から各層（タイムスライス）ごとに前進（Next layer / Run）・後退（Previous layer / Go to begin）できる。
   - 各ステップでの状態ベクトル（Statevector: 複素振幅値、位相棒グラフ）、基底ごとの確率（Probabilities: 青棒グラフ）、Q-sphere が同期して更新される。
4. **状態ベクトルの位相可視化（Statevector パネル）**:
   - 「View > Panels > Statevector」で表示可能。
   - 各基底状態のバーが「振幅の絶対値」の高さになり、色が「位相角（$-\pi$ から $+\pi$）」で色分けされる（0は水色、$\pi$ または $-1$ は赤色）。
   - 配下のテキストに `[ 0.707, -0.707 ]` のように数値が直接表示される。
5. **画像エクスポート機能**:
   - 「File > Export circuit image」により、テーマ（Light / Dark）、形式（SVG / PNG）、行折り返しを選択して回路図を直接ダウンロード可能。
6. **ビット順序（Little-endian）**:
   - $q_0$ に $X$ ゲートを置くと、Probabilities パネルでは基底 $|01\rangle$ に $100\%$ が立ち、Statevector は `[ 0, 1, 0, 0 ]` となる。
   - $q_1$ に $X$ ゲートを置くと、基底 $|10\rangle$ に $100\%$ が立ち、Statevector は `[ 0, 0, 1, 0 ]` となる。
   - すなわち、**回路図の一番上のワイヤ $q_0$ は、ケット表示 $\lvert q_{n-1}\dots q_1 q_0 \rangle$ の一番「右（最下位ビット）」** であることが実機で確定。

### (2) UIの制約・注意点
1. **可視化の量子ビット数上限**:
   - Probabilities パネル: 最大 **8量子ビット** まで。
   - Statevector パネル: 最大 **6量子ビット** まで。
   - Q-sphere: 最大 **5量子ビット** まで。
   - ゼミの教材（1〜3量子ビット）では全く問題なくすべて動作する。
2. **測定（Measure）ゲートの扱い**:
   - 回路の最後に `c = measure q` を置くと、Composer の理論シミュレータは射影後の1つの結果にコラプスした状態（または初期化状態）を表示することがある。
   - 授業での「振幅の干渉や重ね合わせの追跡」を行う実験では、測定ゲートを置く前の状態を Statevector / Probabilities で観察し、最後に測定を置いたときの意味を対比させるのがベストプラクティス。
3. **ブラウザドラッグ＆ドロップの環境差**:
   - マウスやトラックパッドのドラッグ＆ドロップでも配置可能だが、操作に不慣れな学生がいる場合、右側エディタに OpenQASM 3.0 の1〜2行を直接書く（または貼る）方が圧倒的に速く、構文エラーも即座にハイライトされる。

---

## 3. 2時間のゼミ授業計画（120分構成）

### タイムテーブル概要
- **第0部（10分）**: 導入 — 状態の記録・ビット順序・確率の正体
- **第1部（25分）**: 1量子ビットの振幅追跡 — なぜ結末が変わるのか ($H-H$ vs $H-Z-H$)
- **第2部（30分）**: 2本の線とエンタングルメント — Bell状態と局所観測の限界
- **第3部（30分）**: 目的からの回路設計 — 位相キックバックの幾何と代数
- **第4部（20分）**: 関数を計算する回路 — Deutschアルゴリズムの設計意図
- **まとめ・質疑（5分）**: 理論（Preskill Ch 2/3）と回路の接点

---

### 第0部（10分）：導入とツールの準備
#### 目的
回路の読み方のルール（特にビット順序と確率の定義）を揃え、全員の Composer 画面を開く。
#### 事前説明
1. **状態ベクトルの記録**:
   $$\lvert 0 \rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad \lvert 1 \rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \quad \lvert \psi \rangle = \alpha \lvert 0 \rangle + \beta \lvert 1 \rangle$$
2. **画面の見方**:
   - 上部: 回路図（ワイヤ）とゲートパレット。
   - 下部: Probabilities（$|\alpha|^2, |\beta|^2$）と Statevector（振幅と位相）。
   - 右部: コード（OpenQASM / Qiskit）。
3. **Little-endian の警告**:
   - 回路の上段ワイヤ $q_0$ は、ケットの右端（$\lvert q_1 q_0 \rangle$）。
   - 「上が左」と思い込むと、すべての手計算と画面の表示が左右逆に見えて大混乱するため、ここで釘を刺す。

---

### 第1部（25分）：1量子ビットの振幅追跡 — なぜ結末が変わるのか
**既存教材対応**: [algorithms/_01-single-qubit-gates.qmd](/quarto/qiskit/algorithms/_01-single-qubit-gates.qmd), [algorithms/_02-follow-the-amplitudes.qmd](/quarto/qiskit/algorithms/_02-follow-the-amplitudes.qmd)

#### 実験 1-A: $H$ ゲート1回と2回 ($H^2 = I$)
1. **学習者の予想**:
   - 「$|0\rangle$ に $H$ をかけるとどうなるか？」
   - 「さらにもう一度 $H$ をかけると、なぜランダムではなく $100\% |0\rangle$ に戻るのか？」
2. **手計算**:
   $$\lvert 0 \rangle \xrightarrow{H} \frac{\lvert 0 \rangle + \lvert 1 \rangle}{\sqrt{2}} \xrightarrow{H} \frac{1}{2}(\lvert 0 \rangle + \lvert 1 \rangle) + \frac{1}{2}(\lvert 0 \rangle - \lvert 1 \rangle) = \left(\frac{1}{2}+\frac{1}{2}\right)\lvert 0 \rangle + \left(\frac{1}{2}-\frac{1}{2}\right)\lvert 1 \rangle = \lvert 0 \rangle$$
   - ポイント: $|1\rangle$ の振幅が $\frac{1}{2} - \frac{1}{2} = 0$ で**打ち消し合う（干渉）**。
3. **Composer での操作**:
   - パレットから $H$ を $q_0$ に2つ並べる。
   - 「Inspect」スイッチを ON にし、1ステップ進める $\to$ Probabilities で $0, 1$ が $50\%$ ずつ、Statevector で振幅が両方正（水色）であることを確認。
   - もう1ステップ進める $\to$ 再び $0$ に $100\%$ 戻ることを確認。

#### 実験 1-B: $H-Z-H$ vs $H-H$（途中の確率は同じなのに結末が逆転する）
1. **学習者の予想**:
   - 「1個目の $H$ の後で $Z$ を挟む。$Z$ は位相を反転するだけ（確率分布は $50:50$ のまま不変）。では最後の $H$ を通した結果はどうなるか？」
2. **手計算**:
   $$\lvert 0 \rangle \xrightarrow{H} \frac{\lvert 0 \rangle + \lvert 1 \rangle}{\sqrt{2}} \xrightarrow{Z} \frac{\lvert 0 \rangle - \lvert 1 \rangle}{\sqrt{2}} \xrightarrow{H} \frac{1}{2}(\lvert 0 \rangle + \lvert 1 \rangle) - \frac{1}{2}(\lvert 0 \rangle - \lvert 1 \rangle) = \lvert 1 \rangle$$
3. **Composer での操作**:
   - $H, Z, H$ を $q_0$ に並べる。
   - Inspect で1層ずつ追う:
     - 1層目 ($H$ 直後): 振幅 $[+0.707, +0.707]$、両方水色。
     - 2層目 ($Z$ 直後): 振幅 $[+0.707, -0.707]$、**$|1\rangle$ のバーが赤色（位相 $\pi$）に変化**！
     - 3層目 ($H$ 直後): 振幅 $[0, 1]$、結果が $100\% |1\rangle$ に確定！
4. **深い問いと納得**:
   - 「古典確率（コイン投げ）では、表裏が半々の状態で裏だけに目印をつけても、もう一回シャッフルすれば半々のまま。なぜ量子では $100\% 1$ になるのか？」
   - **結論**: 確率は足し算できない。振幅の正負（位相）が干渉して、望まない答え（$|0\rangle$）を完全に打ち消し、欲しい答え（$|1\rangle$）を強め合っている。

---

### 第2部（30分）：2本の線とエンタングルメント — Bell状態
**既存教材対応**: [algorithms/_03-two-qubits.qmd](/quarto/qiskit/algorithms/_03-two-qubits.qmd)

#### 実験 2-A: CNOT ゲートと基底の変換
1. **手計算規則**:
   $$\text{CNOT} \lvert a, b \rangle = \lvert a, a \oplus b \rangle$$
   - 上段 $a$（control）が 0 なら下段 $b$ はそのまま。上段が 1 なら下段を反転。
2. **Little-endian の実体験**:
   - $q_0$ に $X$ を置く $\to$ 表示は $|01\rangle$。
   - $q_1$ に $X$ を置く $\to$ 表示は $|10\rangle$。
   - 画面の「01」と「10」を指差し確認させる。

#### 実験 2-B: Bell状態 $|Phi^+angle = rac{|00angle + |11angle}{sqrt{2}}$ の生成
1. **手計算**:
   $$\lvert 00 \rangle \xrightarrow{H \otimes I} \frac{\lvert 0 \rangle + \lvert 1 \rangle}{\sqrt{2}} \lvert 0 \rangle = \frac{\lvert 00 \rangle + \lvert 10 \rangle}{\sqrt{2}} \xrightarrow{\text{CNOT}_{0 \to 1}} \frac{\lvert 00 \rangle + \lvert 11 \rangle}{\sqrt{2}}$$
   ※ $q_0$ が 1 の項 $|10\rangle$ だけ、下段 $q_1$ が反転して $|11\rangle$ になる。
2. **Composer での操作**:
   - $q_0$ に $H$ を置き、$q_0$ を制御、$q_1$ を標的とする CNOT（パレットの $\oplus$ または cx）を配置。
   - Probabilities パネルを確認:
     - $|00\rangle$ が $50\%$、$|11\rangle$ が $50\%$。$|01\rangle$ と $|10\rangle$ は厳密に $0\%$。
   - Statevector パネルを確認:
     - `[ 0.707, 0, 0, 0.707 ]`、両方水色（同相）。
3. **典型的な誤読と問い**:
   - 「$q_0$ だけを見ると $50\%$ で 0、$50\%$ で 1。$q_1$ だけを見ても $50\%$ で 0、$50\%$ で 1。じゃあ2枚の独立なコイン投げと同じ？」
   - **手計算での反論**: 独立なら $|01\rangle$ や $|10\rangle$ も $25\%$ ずつ出るはず。出ない理由は状態が積状態 $|\psi_A\rangle \otimes |\psi_B\rangle$ に分解できないから（Preskill 第3章のエンタングルメントの定義）。

---

### 第3部（30分）：目的からの回路設計 — 位相キックバック
**既存教材対応**: [algorithms/_04-design-small-circuits.qmd](/quarto/qiskit/algorithms/_04-design-small-circuits.qmd), [algorithms/_08-why-the-circuit-works.qmd](/quarto/qiskit/algorithms/_08-why-the-circuit-works.qmd)

#### 最重要の問い
「CNOT は上（制御ビット）を見て下（標的ビット）を変える部品だった。では、**上のビットの位相を変えるために CNOT を使う**ことはできるか？」

#### 実験 3: 標的を $X$ の固有状態 $|-angle$ にしたときの CNOT
1. **学習者の予想**:
   - 「下段に何を入れようと、制御ビット自身は変化しないのでは？」
2. **手計算（式展開）**:
   - 標的ビット $q_1$ を $\lvert - \rangle = \frac{\lvert 0 \rangle - \lvert 1 \rangle}{\sqrt{2}}$ に準備する。
   - 制御ビット $q_0$ が $\lvert 0 \rangle$ のとき:
     $$\lvert 0 \rangle \lvert - \rangle \xrightarrow{\text{CNOT}} \lvert 0 \rangle \lvert - \rangle = +1 \cdot \lvert 0 \rangle \lvert - \rangle$$
   - 制御ビット $q_0$ が $\lvert 1 \rangle$ のとき:
     $$\lvert 1 \rangle \lvert - \rangle \xrightarrow{\text{CNOT}} \lvert 1 \rangle X\lvert - \rangle = \lvert 1 \rangle (-\lvert - \rangle) = -1 \cdot \lvert 1 \rangle \lvert - \rangle$$
   - 制御ビットが $\lvert + \rangle = \frac{\lvert 0 \rangle + \lvert 1 \rangle}{\sqrt{2}}$ のとき:
     $$\frac{\lvert 0 \rangle + \lvert 1 \rangle}{\sqrt{2}} \lvert - \rangle \xrightarrow{\text{CNOT}} \frac{\lvert 0 \rangle - \lvert 1 \rangle}{\sqrt{2}} \lvert - \rangle = \lvert - \rangle \lvert - \rangle$$
   - **驚きの事実**: **標的ビット $|-\rangle$ は全く変化せず、制御ビットの符号だけが反転した（位相キックバック）！**
3. **Composer での操作**:
   - $q_1$ に $X$, $H$（$|-\rangle$ を作る）。
   - $q_0$ に $H$（$|+\rangle$ を作る）。
   - CNOT（制御: $q_0$, 標的: $q_1$）。
   - $q_0$ にもう一度 $H$（$q_0$ の位相変化を測定値に変換）。
   - Inspect モードで CNOT の前後を観察:
     - CNOT の直後、Statevector で $q_0$ に相当する成分の符号が反転していることを確認。
     - 最後の $H$ の後、Probabilities は $100\%$ で $q_0=1$ を指す（表示は $|01\rangle$ または $|11\rangle$）。
4. **設計理由の言語化**:
   - 「下のビットは変わらないのに、なぜわざわざ用意したのか？」
   - $\to$ これが量子アルゴリズム（Deutsch-Jozsa, Grover, Shor）でオラクルから情報を引き出す万能のメカニズムである。

---

### 第4部（20分）：関数を計算する回路 — Deutsch アルゴリズム
**既存教材対応**: [algorithms/_05-computing-a-function.qmd](/quarto/qiskit/algorithms/_05-computing-a-function.qmd), [algorithms/_06-design-deutsch.qmd](/quarto/qiskit/algorithms/_06-design-deutsch.qmd)

#### 課題設定
入力 $x \in \{0, 1\}$ に対し、関数 $f(x) \in \{0, 1\}$ がある。
$f$ が定数関数（$f(0)=f(1)$）か、バランス関数（$f(0) \neq f(1)$）かを、**関数をたった1回呼ぶだけで100%確実に判定せよ**。

1. **オラクル回路の構造**:
   $$\lvert x \rangle \lvert y \rangle \xrightarrow{U_f} \lvert x \rangle \lvert y \oplus f(x) \rangle$$
   $y = \lvert - \rangle$ に置くと、キックバックにより
   $$\lvert x \rangle \lvert - \rangle \xrightarrow{U_f} (-1)^{f(x)} \lvert x \rangle \lvert - \rangle$$
2. **手計算**:
   - 入力 $x$ を $H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}$ で入れる。
   - $U_f$ を通すと:
     $$\frac{(-1)^{f(0)}\lvert 0 \rangle + (-1)^{f(1)}\lvert 1 \rangle}{\sqrt{2}} \lvert - \rangle = (-1)^{f(0)} \frac{\lvert 0 \rangle + (-1)^{f(0)\oplus f(1)}\lvert 1 \rangle}{\sqrt{2}} \lvert - \rangle$$
   - 最後の $H$ を $x$ にかけると:
     - 定数関数（$f(0) \oplus f(1) = 0$）$\to$ 相対位相 $+1$ なので必ず **$0$** が出る。
     - バランス関数（$f(0) \oplus f(1) = 1$）$\to$ 相対位相 $-1$ なので必ず **$1$** が出る。
3. **Composer での実験**:
   - バランス関数 $f(x) = x$（オラクルは CNOT そのもの）を組む。
   - 測定ゲートを $q_0$ につなぎ、Probabilities を確認 $\to$ 測定結果 $c_0 = 1$ が $100\%$。
   - 定数関数 $f(x) = 0$（オラクルは素通り / ゲートなし）に変えてみる $\to$ 測定結果 $c_0 = 0$ が $100\%$。
4. **設計の納得**:
   - 「なぜ $H$ で挟むのか？」 $\to$ 相対位相の差を、計算基底の 0 と 1 の差に変換するため。
   - 「なぜ補助ビットが必要か？」 $\to$ 可逆計算を満たし、かつ位相キックバックを起こすため。

---

### 第5部（5分）：まとめと理論（Preskill Ch 2/3）への接続
- 行列の掛け算として学んだユニタリ変換が、回路では「振幅の分配と干渉の制御」として具体化された。
- なぜ純粋状態と位相が壊れては困るのか？ $\to$ 混合状態（密度行列の非対角成分の消失＝デコヒーレンス）が起きると、第1部で見た $-1/2$ と $+1/2$ の打ち消し合いが起こらなくなるから。

---

## 4. 60分短縮版プラン（演習・ハッカソン向け）

もしゼミの時間が1時間しかない場合は、以下のように絞り込みます。

| 時間 | 内容 | 取り扱う実験 | 省略する内容 |
| :--- | :--- | :--- | :--- |
| **0-15分** | 振幅の追跡と干渉 | 実験 1-B ($H-Z-H$) | 実験 1-A ($H-H$) の詳細展開を口頭のみに |
| **15-35分** | 位相キックバック | 実験 3 (制御 $X$, 標的 $|-\rangle$) | 実験 2 (Bell状態) はスキップし直接キックバックへ |
| **35-55分** | Deutsch の回路 | 実験 4 (バランス vs 定数) | 4つのオラクル全パターンの比較を2パターンに限定 |
| **55-60分** | 質疑・まとめ | なぜ量子で高速化できるか | 密度行列との形式的接続 |

---

## 5. 発表者用の操作手順とトラブルシューティング

### 授業前の準備
1. **ブラウザ確認**:
   - Chrome, Edge, Safari, Firefox のいずれかで [https://quantum.cloud.ibm.com/composer](https://quantum.cloud.ibm.com/composer) にアクセス。
   - ログインは不要。Cookie の同意ダイアログが出たら「Accept All」をクリック。
2. **画面パネル設定**:
   - 上部メニュー「View > Panels」を開き、**Statevector** にチェックを入れる（Probabilities, Statevector, Q-sphere の3枚構成にしておくと解説が非常にスムーズ）。
3. **OpenQASM 3.0 コード集の手元準備**:
   - スライドや配布資料に、各実験の QASM コードをコピペ用として用意しておく（マウス操作が遅れた学生がすぐ追いつけるため）。

### ネットワーク不通・Composer 不可時の代替策
- **代替策1 (ローカル Qiskit Notebook)**:
   - 既存の [quarto/qiskit/algorithms.qmd](/quarto/qiskit/algorithms.qmd) は、全く同一の回路・手計算・状態ベクトル出力を Python コードブロックで備えています。
   - `quarto preview quarto/qiskit/algorithms.qmd` をローカルで立ち上げるか、JupyterLab で AerSimulator を動かせば、オフラインでも完全に同一内容の講義が可能です。
- **代替策2 (Quarto Live / Pyodide)**:
   - プロジェクト内の対話シミュレーション（docs/quarto-live.md 準拠）を利用。

---

## 6. 未確認事項・今後の調査課題

1. **実機へのジョブ投入とノイズ（今回は対象外）**:
   - 今回はログイン不要の理論シミュレータに限定して検証しました。実機（IBM Quantum 物理バックエンド）への投入時は、ログインとキュー待ち時間、および測定エラー緩和が必要になります。
2. **OpenQASM 3.0 の高度な古典制御構文**:
   - Composer UI 上に `if`, `for`, `while`, `box` のパレットボタンが存在しますが、グラフィカルエディタでの配置サポート度合いとシミュレータ側の動的回路（Dynamic Circuits）対応範囲については、次回の課題とします。

