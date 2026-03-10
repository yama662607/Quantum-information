# 量子測定：学部の量子力学からPOVMへの接続

このドキュメントでは、標準的な量子力学（学部レベル）で学ぶ「測定」の概念と、量子情報理論（本章 2.3節）で定義される「POVM（ Positive Operator-Valued Measure）」や「量子から古典へのチャネル」としての測定の定義が、どのようにつながっているのかを解説します。

## 1. 学部レベルの測定（可観測量を用いた定式化）

通常の量子力学では、測定は以下のように定式化されます。

*   **状態**: 状態ベクトル $|\psi\rangle$
*   **測定（オブザーバブル / 可観測量）**: エルミート演算子 $H$ ($H^\dagger = H$)
*   **測定結果**: $H$ の固有値 $\lambda_a$
*   **ボルン則（確率）**: $H$ のスペクトル分解を $H = \sum_a \lambda_a |a\rangle\langle a|$ としたとき、測定値 $\lambda_a$ が得られる確率は
    $$ \Pr(a) = |\langle a | \psi \rangle|^2 = \langle \psi | \left( |a\rangle\langle a| \right) | \psi \rangle $$
*   **事後状態**: 波束の収縮（状態の崩壊）により、系は測定結果に対応する固有状態 $|a\rangle$ になります。

このとき、射影演算子 $P_a = |a\rangle\langle a|$ を使うと、確率は $\Pr(a) = \langle \psi | P_a | \psi \rangle$ と書けます。
また、基底が完全系をなすため、確率の総和が1になる要請から **$\sum_a P_a = \mathbb{I}$（完全性の関係）** が成り立ちます。

教科書の セクション `2.3.3 Projective measurements`（射影測定）は、まさにこの学部レベルの理想的な測定プロセスの数学的表現です。

## 2. 量子情報への飛躍：POVM（正作用素値測度）の導入

量子情報の文脈に入ると、発想が少し変わります。

**「測定値（固有値 $\lambda_a$）の具体的な数値（例えばエネルギーのJ、スピンの角運動量など）はそれほど重要ではなく、結果ごとの『確率分布』が得られれば良い」** と考えます。
例えば、「スピン上向き」ならば $+1$、「下向き」なら $-1$ という値自体に物理的意味を持たせるより、単なる情報理論的な「結果0」と「結果1」の2つのアウトカム（古典情報）として扱います。

そのため、オブザーバブル $H$ そのものではなく、それぞれの結果を生み出す「**演算子のセット $\{P_a\}$**」に注目します。
射影演算子 $P_a$ は以下の2つの性質を持っています。

1.  **正値性**: 全ての状態に対して確率が $0$ 以上になるため、$P_a \ge 0$ （半正定値）
2.  **完全性（確率の合計が1）**: $\sum_a P_a = \mathbb{I}$

ここで量子情報理論では、次のように一般化します。
「必ずしも『射影演算子 ($P_a^2 = P_a$)』でなくても、上の **1. 半正定値性** と **2. 足して恒等演算子（完全性）** の条件さえ満たす演算子のセット $\{\mu(a)\}$ を定義すれば、それを全て『測定』とみなそう」

これが教科書の **Definition 2.34**（POVM）の定義です。

$$ \text{測定の条件（POVM）: } \quad \mu(a) \ge 0, \quad \sum_a \mu(a) = \mathbb{I} $$

射影測定よりも条件が緩いため、より一般的な（ノイズを含んだり、不完全な）測定プロセスを数学的にきれいに記述できます。

## 3. 表記の変換（ブラケットから密度行列・トレースへ）

教科書では、ブラケット記法 $\langle \psi | \dots | \psi \rangle$ の代わりに、密度行列（密度演算子） $\rho$ と**トレース** $\operatorname{Tr}$ や **内積表記** $\langle A, B \rangle$ を多用しています。ここを繋ぐのが理解の鍵になります。

純粋状態 $\rho = |\psi\rangle\langle\psi|$ を考えると、ある結果 $a$ が出る確率に関する学部の表記は、トレースの巡回性（$\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$）を使って次のように変形できます。

$$ \langle \psi | \mu(a) | \psi \rangle = \operatorname{Tr} \left( \mu(a) |\psi\rangle\langle\psi| \right) = \operatorname{Tr} \left( \mu(a) \rho \right) $$

この量子情報の教科書では、さらにエルミート行列の空間におけるヒルベルト＝シュミット内積 $\operatorname{Tr} (A^\dagger B)$ を行列の内積 $\langle A, B \rangle$ として書くルールを採用しているため（効果演算子 $\mu(a)$ はエルミートなので $\mu(a)^\dagger = \mu(a)$）、

$$ \Pr(a) = \langle \mu(a), \rho \rangle $$

と表現されています。
記号の見た目は違いますが、中身は完全に「学部で習ったボルン則」の一般化です。

## 4. Naimarkの定理：2つのパラダイムの架け橋

なぜ「理想的な射影測定」からわざわざ条件を緩めた「POVM」を導入するのでしょうか？

*   **学部の量子力学**: 「孤立系」における「理想的で鋭い測定（射影測定）」を中心に学びます。測定によって状態が確定（崩壊）します。
*   **量子情報理論**: ノイズや環境との相互作用も込みで「量子系からいかに古典的なビット（確率情報）を取り出すか」を扱います。POVMは、対象とする系だけでなく、その周りの環境も含めた巨大なシステムを対象系だけに制限（部分トレース）した結果として自然に現れます。

実は、教科書の **Naimarkの定理 (Theorem 2.42)** は、この2つを繋ぐ非常に強力な定理です。

> 「どんなに複雑で一般化された POVM 測定 $\mu$ であっても、対象の系の外側に環境（補助ビット：ancilla）を付け足して広い視点で見れば、全体の系に対するただの『普通の射影測定』として完全に記述できる」

つまり、「学部レベルの理想的な射影測定（大きな系）」を、対象の系（小さな系）に限定して観測した「影」のようなものが、POVM の正体なのです。
これにより、量子情報理論における広範な数学的定義が、物理的な実装（補助量子ビット＋ユニタリ時間発展＋通常の射影測定）によって必ず実現可能であることが保証されます。

## 5. $\langle \mu(a), \rho \rangle = \operatorname{Tr}(\mu(a) \rho)$ が成り立つ理由

ゼミの板書でも触れられていた**「行列の内積」**について補足します。
量子情報理論では、2つの演算子（行列）$A, B$ の間の「ヒルベルト＝シュミット内積 (Hilbert-Schmidt inner product)」を次のように定義します。

$$ \langle A, B \rangle \equiv \operatorname{Tr}(A^\dagger B) $$

ここで測定に関する確率 $p(a)$ を計算する式 $\langle \mu(a), \rho \rangle$ にこの定義を当てはめると、

$$ \langle \mu(a), \rho \rangle = \operatorname{Tr}(\mu(a)^\dagger \rho) $$

となります。
POVMの要素である効果演算子 $\mu(a)$ は**エルミート演算子**（より強く言えば半正定値演算子）であるため、自己随伴性 $\mu(a)^\dagger = \mu(a)$ を持ちます（板書にある $\mu(a)^* = \mu(a)$ の部分です）。
したがって、そのまま以下が成り立ちます。

$$ \langle \mu(a), \rho \rangle = \operatorname{Tr}(\mu(a) \rho) $$

### 確率が非負 $p(a) \ge 0$ になる理由の証明

板書の後半にあった証明の流れも非常に重要です。なぜ $\operatorname{Tr}(\mu(a)\rho) \ge 0$ になるのかを厳密に示しています。

密度行列 $\rho$ は半正定値なので、平方根 $\rho^{1/2}$ が存在し、$\rho = \rho^{1/2} \rho^{1/2}$ と書けます。
トレースの巡回性 $\operatorname{Tr}(ABC) = \operatorname{Tr}(CAB)$ を用いると：

$$ \operatorname{Tr}(\mu(a)\rho) = \operatorname{Tr}(\mu(a) \rho^{1/2} \rho^{1/2}) = \operatorname{Tr}(\rho^{1/2} \mu(a) \rho^{1/2}) $$

ここで得られた行列 $M = \rho^{1/2} \mu(a) \rho^{1/2}$ が半正定値（$M \ge 0$）であることを示せば、そのトレース（固有値の和）も $0$ 以上になるため、確率が非負であることが証明できます。
任意のベクトル $|x\rangle$ に対して、二次形式を計算します（板書の青字 $x^\dagger A x = \langle x, A x \rangle$ の部分です）：

$$ \langle x | \rho^{1/2} \mu(a) \rho^{1/2} | x \rangle $$

$|y\rangle = \rho^{1/2} |x\rangle$ と置くと、$\rho^{1/2}$ はエルミートなので $\langle y| = \langle x| \rho^{1/2}$ となります。代入すると：

$$ \langle y | \mu(a) | y \rangle $$

$\mu(a)$ は POVM の定義により半正定値 ($\mu(a) \ge 0$) であるため、どんなベクトル $|y\rangle$ に対してもこの値は $0$ 以上になります。
よって、$\operatorname{Tr}(\mu(a)\rho) \ge 0$ が示され、確率の公理 (1) $p(a) \ge 0$ が数学的に保証されます。

## 6. 数学的な一般化：「射影測定（PVM）」から「正作用素値測度（POVM）」へ

ご質問の通り、これは**「数学でよくある、性質（公理）を一般化して新しい定義にする」**という極めて典型的で美しいアプローチです。

### 学部レベルにおける「POVMに対応するもの」

学部レベル（標準的な量子力学）で測定を表す演算子 $P_a = |a\rangle\langle a|$（射影演算子）は、POVM の特別なケースにほかなりません。
射影演算子を使った測定は **PVM (Projection-Valued Measure：射影値測度)** とも呼ばれますが、これはそのまま POVM に対応しています。

つまり、「学部レベルの可観測量（$H = \sum_a \lambda_a P_a$）に基づく測定」は、効果演算子 $\{\mu(a)\}$ を以下の特別な条件で選んだ POVM と完全に一致します：

1.  $\mu(a) = P_a \ge 0$ （半正定値）
2.  $\sum_a \mu(a) = \sum_a P_a = \mathbb{I}$ （完全性）
3.  **$\mu(a)^2 = \mu(a)$（射影演算子である）**
4.  **$\mu(a)\mu(b) = 0 \quad (a \neq b)$（互いに直交している）**

このように、学部レベルの測定（PVM）は、すでに確率 $p(a) \ge 0$ と $\sum p(a) = 1$ を満たす立派な「測度（Measure）」として機能しています。

### なぜ一般化が必要になったのか？

関数解析や確率論の文脈で「確率を吐き出す装置」としての最低限の要件を考えたとき、実は **条件3（射影であること）や条件4（直交していること）は、確率論の公理（0以上で足して1になる）を満たす上で【厳しすぎる制約（過剰な条件）】** であることに数学者や物理学者が気づきました。

$$ p(a) = \langle \psi | \mu(a) | \psi \rangle $$
という式が「確率」として正しく振る舞うためには、

1.  $p(a) \ge 0 \implies \mu(a)$ が半正定値（Positive Operator）であれば十分。
2.  $\sum_a p(a) = 1 \implies \sum_a \mu(a) = \mathbb{I}$（Identity）であれば十分。

「$\mu(a)^2 = \mu(a)$（射影）」や「直交性」は、数学的に **確率を定義するためには全く不要な条件** だったのです。

### 「性質」を抜き出して「定義」にする（POVMの誕生）

そこで数学者は、「射影であるという制約を外し、確率として振る舞うための最低限のバリアント（性質）だけを残したものを、最も一般的な測定の定義にしよう」と考えました。
これが **POVM (Positive Operator-Valued Measure：正作用素値測度)** という名前の由来です。

*   Valued Measure（値測度）: 各結果 $a$ に対して、確率（測度）を与える
*   Positive Operator（正作用素）: そのために割り当てるのは「半正定値演算子」でよい（射影演算子 Projection である必要はない）

この一般化によって以下のような現実の物理現象も、1つの数学的な枠組み（POVM）で美しく記述できるようになりました。

1.  **ノイズのある測定**：検出器のロスのせいで、直交するはずの基底が混ざって区別できなくなるような測定。
2.  **情報完全測定**：2次元空間（1量子ビット）の情報を得るために、直交しない4方向以上の測定（例えば正四面体の頂点方向など、基底の数よりも多い結果を持つ測定）を設計すること。

要約すると、学部で習う測定（PVM）は「確率を保証する条件」＋「理想的な孤立系という過剰な条件」を持っていました。そこから**「確率を保証する本質的な性質（正値性・完全性）」だけを抽出して一般化し、新しい測定の定義にした**のが POVM （量子情報における測定の定義）です。

## 7. $p(a) = \langle \psi | \mu(a) | \psi \rangle$ と $\Pr(a) = \langle \mu(a), \rho \rangle$ は同じことか？

結論から言うと、**これらは全く同じこと（ボルン則による確率計算）を表しています。**
この2つの表記の違いは、「純粋状態専用の記法（ブラケット）」を使うか、「混合状態も含めた一般化された記法（密度行列と内積）」を使うかの違いに過ぎません。

数式を使って、この2つがどのように結びついているか確認してみましょう。

### 「純粋状態」の場合

系が純粋状態 $|\psi\rangle$ にあるとき、その密度行列 $\rho$ は、状態ベクトル自身への射影演算子として次のように書けます：
$$ \rho = |\psi\rangle\langle\psi| $$

量子情報理論での確率の定義 $\Pr(a) = \langle \mu(a), \rho \rangle$ に出発し、これをヒルベルト＝シュミット内積の定義（$\operatorname{Tr}(A^\dagger B)$）に当てはめます（$\mu(a)$ はエルミートなので $\mu(a)^\dagger = \mu(a)$）。

$$ \Pr(a) = \operatorname{Tr}(\mu(a) \rho) $$

ここに純粋状態の密度行列 $\rho = |\psi\rangle\langle\psi|$ を代入します。

$$ \Pr(a) = \operatorname{Tr}\Big( \mu(a) |\psi\rangle\langle\psi| \Big) $$

ここで、「**トレースの巡回性**（$\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$）」という非常に便利な性質を使います。行列の掛け算の順番をぐるっと回しても、トレースの値は変わりません。
この式で、$\big(\mu(a) |\psi\rangle\big)$ を $A$、$\langle\psi|$ を $B$ だと思うと、次のように並べ替えられます。

$$ \Pr(a) = \operatorname{Tr}\Big( \langle\psi| \, \mu(a) \, |\psi\rangle \Big) $$

さて、括弧の中身 $\langle\psi| \mu(a) |\psi\rangle$ に注目してください。これはベクトルに挟まれているので、もはや行列ではなく**ただのスカラー（1×1の単なる数字、確率の値）**です。
スカラーのトレースは、その数字そのものです（$\operatorname{Tr}(c) = c$）。したがって、トレース記号が外れて、学部レベルで見慣れた式になります！

$$ \Pr(a) = \langle \psi | \mu(a) | \psi \rangle $$

### なぜわざわざ $\langle \mu(a), \rho \rangle$ と書くのか？

ブラケット記法の方が分かりやすいのに、なぜ量子情報理論では $\Pr(a) = \langle \mu(a), \rho \rangle$ を使うのでしょうか？
最大理由は、**「混合状態（Mixed States）」を扱えるようにするため**です。

ブラケット記法 $|\psi\rangle$ は、「系が100%確実にこの状態にある（純粋状態）」場合にしか使えません。
しかし現実の量子コンピュータや通信では、「50%の確率で $|\psi_1\rangle$、50%の確率で $|\psi_2\rangle$ が来る（古典的な確率的無知が含まれる）」ような状況を扱う必要があります。これが混合状態で、密度行列 $\rho = 0.5 |\psi_1\rangle\langle\psi_1| + 0.5 |\psi_2\rangle\langle\psi_2|$ として記述されます。

このような混合状態に対しては、もはや1つのベクトル $|\psi\rangle$ で状態を書き表すことができません。
しかし、**密度行列 $\rho$ と内積 $\langle \mu(a), \rho \rangle$（または トレース $\operatorname{Tr}(\mu(a)\rho)$）を使えば、純粋状態だろうが混合状態だろうが、全く同じたった1つの式で確率を計算できる**のです。

そのため、量子情報理論のような汎用性を求める枠組みでは、$p(a) = \langle \psi | \mu(a) | \psi \rangle$ よりも、より強力で一般化された記法 $\Pr(a) = \langle \mu(a), \rho \rangle$ （または $\operatorname{Tr}(\mu(a)\rho)$）が好んで使われます。

### 「混合状態」の場合の詳しい計算過程（なぜ $\Pr(a) = \langle \mu(a), \rho \rangle$ になるのか）

混合状態とは、「確率 $q_1$ で状態 $|\psi_1\rangle$、確率 $q_2$ で状態 $|\psi_2\rangle$、…（一般に確率 $q_i$ で状態 $|\psi_i\rangle$）」という**古典的な確率分布**を持つアンサンブル（集団）のことです。
※ここで、確率の和は $\sum_i q_i = 1$ ($q_i \ge 0$) を満たします。

この系全体に対する密度行列 $\rho$ は、それぞれの純粋状態の密度行列を確率で重み付けした和として定義されます。
$$ \rho = \sum_i q_i |\psi_i\rangle\langle\psi_i| $$

さて、この「混合状態」が測定装置に入ってきたとき、測定結果としてアトカム $a$ が得られる確率 $\Pr(a)$ はどのように計算すべきでしょうか。
古典的な確率論の「全確率の定理」に従い、次のように計算するのが自然です。

$$ \Pr(a) = \sum_i \Big( (\text{状態 } |\psi_i\rangle \text{ である確率}) \times (\text{状態 } |\psi_i\rangle \text{ のときに結果 } a \text{ が出る確率}) \Big) $$

これを数式に落とし込みます。
1つ目の項は古典的な確率 $q_i$ であり、2つ目の項は純粋状態に対する量子力学のボルン則 $p(a|\psi_i) = \langle \psi_i | \mu(a) | \psi_i \rangle$ です。

$$ \Pr(a) = \sum_i q_i \langle \psi_i | \mu(a) | \psi_i \rangle $$

ここから、先ほどの「純粋状態」の証明と同じように、スカラー値 $\langle \psi_i | \mu(a) | \psi_i \rangle$ に対してあえてトレースをつける逆算のトリック（$\operatorname{Tr}(c)=c$）を使います。

$$ \Pr(a) = \sum_i q_i \operatorname{Tr}\Big( \langle \psi_i | \mu(a) | \psi_i \rangle \Big) $$

トレースの巡回性（$\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$）を使って、ベクトル $\langle\psi_i|$ を後ろに回します。

$$ \Pr(a) = \sum_i q_i \operatorname{Tr}\Big( \mu(a) |\psi_i\rangle\langle\psi_i| \Big) $$

**トレース $\operatorname{Tr}$ は線形性を持つ（足し算や定数倍を外に出したり中に入れたりできる）**ため、総和記号 $\sum$ と定数 $q_i$ をトレースの中に入れることができます。

$$ \Pr(a) = \operatorname{Tr}\Big( \sum_i q_i \mu(a) |\psi_i\rangle\langle\psi_i| \Big) $$

さらにもう一度、行列の掛け算に関する線形性（分配法則）を使い、共通の演算子である $\mu(a)$ を総和記号の外（左側）にくくり出します。

$$ \Pr(a) = \operatorname{Tr}\left( \mu(a) \left[ \sum_i q_i |\psi_i\rangle\langle\psi_i| \right] \right) $$

大括弧 $[ \dots ]$ の中身をよく見てください。
これは、まさに一番最初で定義した**全体としての密度行列 $\rho$ そのもの**です。

$$ \rho = \sum_i q_i |\psi_i\rangle\langle\psi_i| $$

したがって、大括弧の部分を $\rho$ に置き換えることができます。

$$ \Pr(a) = \operatorname{Tr}(\mu(a) \rho) $$

最後に、ヒルベルト＝シュミット内積の定義 $\langle A, B \rangle \equiv \operatorname{Tr}(A^\dagger B)$ と、$\mu(a)$ のエルミート性 ($\mu(a)^\dagger = \mu(a)$) を適用すれば、

$$ \Pr(a) = \langle \mu(a), \rho \rangle $$

が得られます。

このように、途中で「古典的な確率の和 $\sum q_i$」と「純粋な量子力学の式 $\langle \psi_i | \mu(a) | \psi_i \rangle$」を混ぜて計算をスタートしたのにも関わらず、**計算の最後には $\sum q_i$ などの古典的分布の情報が、すべて密度行列 $\rho$ の中にきれいに吸収されて消えてしまいます**。

これが、量子情報理論において確率分布を計算するときに、わざわざ状態ベクトルではなく $\Pr(a) = \langle \mu(a), \rho \rangle$ （または $\operatorname{Tr}(\mu(a)\rho)$）という密度行列を使った強力な記法を用いる最大の理由です。

## 8. 部分測定 (Partial Measurements) への拡張

これまでの議論（POVMや確率の定式化）を踏まえた上で、**「部分測定（Partial Measurements）」**について考えます。
部分測定とは、**「複数の量子系（例えば量子ビットAと量子ビットB）があるとき、そのうちの一部（Aだけ）を測定し、残りの部分（B）には何もしない」**という操作のことです。

量子通信（エンタングルメントの共有や量子テレポーテーションなど）では、アリスの手元にある系Aだけを測定し、ボブの手元にある系Bはそのままにしておく、という状況が頻繁に登場するため、この定式化は非常に重要です。

### テンソル積を用いた「部分測定」の表現

系全体が状態空間 $\mathcal{X} \otimes \mathcal{Y}$ （系 $\mathcal{X}$ と系 $\mathcal{Y}$ の合成系）にあるとします。
ここで、「系 $\mathcal{X}$ のみに対して POVM $\mu = \{\mu_\mathcal{X}(a)\}$ で測定を行い、系 $\mathcal{Y}$ には何もしない」という部分測定を、これまでの数学的枠組みにどう組み込むかを考えます。

量子力学のルール「何もしない＝恒等演算子 $\mathbb{I}$ を作用させる」に従うと、系全体 $\mathcal{X} \otimes \mathcal{Y}$ に対する効果演算子は、テンソル積を用いて次のように構成されます。

$$ M(a) = \mu_\mathcal{X}(a) \otimes \mathbb{I}_\mathcal{Y} $$

これが、系全体に作用する「新しいPOVMの要素」になります。
実際にPOVMの条件を満たしているか確認してみましょう。

1.  **正値性**: $\mu_\mathcal{X}(a) \ge 0$ かつ $\mathbb{I}_\mathcal{Y} \ge 0$ なので、テンソル積 $M(a) = \mu_\mathcal{X}(a) \otimes \mathbb{I}_\mathcal{Y} \ge 0$ （半正定値）を満たします。
2.  **完全性**: $\sum_a M(a) = \sum_a \left( \mu_\mathcal{X}(a) \otimes \mathbb{I}_\mathcal{Y} \right) = \left( \sum_a \mu_\mathcal{X}(a) \right) \otimes \mathbb{I}_\mathcal{Y} = \mathbb{I}_\mathcal{X} \otimes \mathbb{I}_\mathcal{Y} = \mathbb{I}_{\mathcal{X} \otimes \mathcal{Y}}$ となり、全体空間の恒等演算子になります。

つまり、**部分測定は、「測定する側（$\mathcal{X}$）のPOVMと、何もしない側（$\mathcal{Y}$）の恒等演算子のテンソル積」を作るだけで、自動的に系全体に対する正当な巨大なPOVMになる**という、非常に美しい性質を持っています。

### 確率の計算と「部分トレース（Partial Trace）」の出現

系全体が（エンタングルしているかもしれない）密度行列 $\rho_{\mathcal{XY}}$ の状態にあるとき、部分測定の結果 $a$ が得られる確率 $\Pr(a)$ を計算してみましょう。
前節までの結論 $\Pr(a) = \operatorname{Tr}(M(a) \rho_{\mathcal{XY}})$ に、そのまま $M(a) = \mu_\mathcal{X}(a) \otimes \mathbb{I}_\mathcal{Y}$ を代入します。

$$ \Pr(a) = \operatorname{Tr}_{\mathcal{XY}} \Big( (\mu_\mathcal{X}(a) \otimes \mathbb{I}_\mathcal{Y}) \rho_{\mathcal{XY}} \Big) $$

ここで、「系全体のトレース（$\operatorname{Tr}_{\mathcal{XY}}$）」は、「系 $\mathcal{X}$ についてのトレース（$\operatorname{Tr}_\mathcal{X}$）」と「系 $\mathcal{Y}$ についてのトレース（部分トレース $\operatorname{Tr}_\mathcal{Y}$）」を順番に行うことと同等です。
系 $\mathcal{Y}$ 側には恒等演算子 $\mathbb{I}_\mathcal{Y}$ しか作用していないため、先に $\mathcal{Y}$ について部分トレース $\operatorname{Tr}_{\mathcal{Y}}$ をとると、

$$ \Pr(a) = \operatorname{Tr}_{\mathcal{X}} \Big( \mu_\mathcal{X}(a) \cdot \operatorname{Tr}_{\mathcal{Y}}(\rho_{\mathcal{XY}}) \Big) $$

と変形できます。
ここで面白いことが起きます。$\operatorname{Tr}_{\mathcal{Y}}(\rho_{\mathcal{XY}})$ という量は、系 $\mathcal{Y}$ の情報を無視（周辺化）して得られる、系 $\mathcal{X}$ 単独の**「縮約密度行列（Reduced Density Matrix）」 $\rho_{\mathcal{X}}$** そのもの定義です！

$$ \rho_{\mathcal{X}} \equiv \operatorname{Tr}_{\mathcal{Y}}(\rho_{\mathcal{XY}}) $$

これを代入すると、確率の式は次のように劇的にシンプルになります。

$$ \Pr(a) = \operatorname{Tr}_{\mathcal{X}} \Big( \mu_\mathcal{X}(a) \, \rho_{\mathcal{X}} \Big) = \langle \mu_\mathcal{X}(a), \rho_{\mathcal{X}} \rangle $$

### なぜこの式展開が重要なのか？

この展開は、量子情報理論における極めて深遠で実用的な事実（**ノーシグナリング定理**）を示しています。

> **局所的な性質とノーシグナリング定理**
> 「アリス（系 $\mathcal{X}$）が自分だけの系で測定を行うとき、得られる結果の確率分布 $\Pr(a)$ は、ボブ（系 $\mathcal{Y}$）が遠くで何をしていようと、アリス自身の手元にある縮約密度行列 $\rho_{\mathcal{X}}$ **だけ**で完全に計算できる」

もしアリスの手元の確率分布がボブの操作によって変化してしまうと、アリスは確率の偏りを見るだけでボブのメッセージを受け取ることができ、光速を超えた通信（超光速通信）が可能になってしまいます。

しかし、上の数式展開が示す通り、巨大な $\rho_{\mathcal{XY}}$ にテンソル積で作った巨大なPOVM $\mu_\mathcal{X}(a) \otimes \mathbb{I}_\mathcal{Y}$ を適用する計算は、数学的に完全に「アリス手元の $\rho_\mathcal{X}$ と $\mu_\mathcal{X}$ だけの内積」に帰着します。

つまり、これまでのPOVMと $\operatorname{Tr}(\dots)$ の枠組みは、部分測定をテンソル積（$\otimes \mathbb{I}$）で自然に拡張するだけで、**「部分トレース」という計算上の便利な道具を導き出し、さらに相対論的因果律（情報伝達速度の限界＝ノーシグナリング）までもが数式の中に自動的に組み込まれる**という、驚くほど一貫した体系になっているのです。

### 教科書でのより厳密な定式化（Quantum-to-classical channel と Ensemble）

ここまでの説明は直感的な理解を優先しましたが、教科書の `2.3.2 Basic notions concerning measurements`（PDF p.105-106）では、これをさらに厳密な数学的枠組みで定式化しています。

教科書では、「測定とは『量子から古典へのチャネル (Quantum-to-classical channel)』である」という強い立場に立っています。したがって、系 $Y_k$ の部分測定 $\mu: \Sigma \to \mathrm{Pos}(Y_k)$ を単なるテンソル積 $\mu \otimes \mathbb{I}$ として扱うのではなく、**「測定結果 $a$ を記録するための、新しい古典レジスタ $Z$ （状態空間 $\mathbb{C}^\Sigma$）を追加し、情報をそこに書き込むプロセス」**として厳密に記述します。

このプロセスの全貌を、途中式を省略せずに追ってみましょう。

#### ステップ1：量子から古典へのチャネル $\Phi$ の定義
系 $Y_k$ の測定は、入力 $X \in \mathrm{L}(Y_k)$ を受け取り、古典レジスタ $Z$ の純粋な古典状態（対角行列）を出力するチャネル $\Phi \in \mathrm{C}(Y_k, Z)$ として定義されます（定理 2.37）。

$$ \Phi(X) = \sum_{a \in \Sigma} \langle \mu(a), X \rangle E_{a,a} = \sum_{a \in \Sigma} \operatorname{Tr}(\mu(a) X) E_{a,a} $$

#### ステップ2：全体系へのチャネルの作用
全体系のレジスタを $X = (Y_1, \dots, Y_n)$ とし、その状態を $\rho$ とします。
ここでは記法を簡単にするため、測定しない残りのすべてのレジスタ $(Y_1, \dots, Y_{k-1}, Y_{k+1}, \dots, Y_n)$ をまとめて巨大な「系 $W$」と呼びましょう。全体系は $W \otimes Y_k$ となり、状態は $\rho_{WY_k}$ と書けます。

系 $W$ には何もしない（$\mathbb{I}_W$）で、系 $Y_k$ にだけ測定チャネル $\Phi$ を作用させます。これをテンソル積 $(\mathbb{I}_W \otimes \Phi)$ で表します。
計算を実行するため、全体の状態 $\rho_{WY_k}$ をテンソル積の和の形 $\sum_i w_i \otimes y_i$ に分解して考えます（$w_i \in \mathrm{L}(W), y_i \in \mathrm{L}(Y_k)$）。

$$ (\mathbb{I}_W \otimes \Phi)(\rho_{WY_k}) = (\mathbb{I}_W \otimes \Phi) \Big( \sum_i w_i \otimes y_i \Big) $$

チャネルの線形性より、テンソル積ごとに作用させます。

$$ = \sum_i \Big( w_i \otimes \Phi(y_i) \Big) $$

ここでステップ1の $\Phi$ の定義を代入します。

$$ = \sum_i \left( w_i \otimes \left[ \sum_{a \in \Sigma} \operatorname{Tr}(\mu(a) y_i) E_{a,a} \right] \right) $$

和の順序を入れ替えて、アトカム $a$ と古典状態 $E_{a,a}$ に着目して整理します（実数であるトレース値は前に出せます）。さらに、教科書（PDF p.106）の記法に合わせるため、テンソル積の順番を入れ替えて古典レジスタ $Z$ （すなわち $E_{a,a}$）を先頭に持っていきます。

$$ = \sum_{a \in \Sigma} E_{a,a} \otimes \Big( \sum_i \operatorname{Tr}\big( \mu(a) y_i \big) w_i \Big) \quad \dots \text{ (式A)} $$

#### ステップ3：「アンサンブル $\eta(a)$」の発見
ここで、式Aの右側にある大括弧 $\Big( \sum_i \operatorname{Tr}\big( \mu(a) y_i \big) w_i \Big)$ の部分に注目します。
これは、実は**「部分トレース（Partial Trace）」**を使った計算結果と全く同じ形をしています。

系 $Y_k$ についての部分トレース $\operatorname{Tr}_{Y_k}$ の定義を思い出してください。テンソル積 $w_i \otimes y_i$ に対して $\operatorname{Tr}_{Y_k}(w_i \otimes y_i) = w_i \operatorname{Tr}(y_i)$ となります。
これを使うと、次のような計算が成り立ちます。

$$ \operatorname{Tr}_{Y_k} \Big( (\mathbb{I}_W \otimes \mu(a)) (w_i \otimes y_i) \Big) = \operatorname{Tr}_{Y_k} \big( w_i \otimes \mu(a)y_i \big) = w_i \operatorname{Tr}\big(\mu(a)y_i\big) = \operatorname{Tr}\big(\mu(a)y_i\big) w_i $$

これを全体の状態 $\rho_{WY_k} = \sum_i w_i \otimes y_i$ に対して線形に足し合わせると、

$$ \operatorname{Tr}_{Y_k} \Big( (\mathbb{I}_W \otimes \mu(a)) \rho_{WY_k} \Big) = \sum_i \operatorname{Tr}\big( \mu(a) y_i \big) w_i $$

となります。これはまさに（式A）の大括弧の中身そのものです！
教科書では、この量を**アンサンブル（Ensemble） $\eta(a)$**として定義しています。

$$ \eta(a) \equiv \operatorname{Tr}_{Y_k} \Big( (\mathbb{I}_W \otimes \mu(a)) \rho_{WY_k} \Big) $$
※もとの $Y_1, \dots, Y_n$ の記法に戻せば、教科書の式 $(2.226)$ と完全に一致します。

#### ステップ4：事後状態の完成と確率の対応
したがって、測定とレジスタの入れ替えが終わった後の全体系（古典レジスタ $Z$ ＋ 残りの量子系 $W$）の状態は、驚くほど美しい次の形に帰着します。

$$ \text{測定後の状態} = \sum_{a \in \Sigma} E_{a,a} \otimes \eta(a) $$

この状態は **Classical-quantum state（古典-量子状態）** と呼ばれます。「古典レジスタに結果 $a$ が書き込まれており（$E_{a,a}$）、そのとき残りの量子系は $\eta(a)$ に比例する状態になっている」という事実を、たった1つのテンソル行列として表しています。

ここで、アンサンブル $\eta(a)$ に対して全体のトレース（系 $W$ でのトレース）を取ってみましょう。

$$ \operatorname{Tr}_{W} \big( \eta(a) \big) = \operatorname{Tr}_{W} \Big[ \operatorname{Tr}_{Y_k} \Big( (\mathbb{I}_W \otimes \mu(a)) \rho_{WY_k} \Big) \Big] = \operatorname{Tr}_{WY_k} \Big( (\mathbb{I}_W \otimes \mu(a)) \rho_{WY_k} \Big) = \langle \mu(a), \rho_{Y_k} \rangle $$

なんと、$\eta(a)$ のトレース値は、まさに私たちが前の節で計算した「結果 $a$ が得られる確率 $\Pr(a)$」そのものになります。
$$ \Pr(a) = \operatorname{Tr}(\eta(a)) $$

そして、結果 $a$ が得られたという条件付きでの、測定後の正規化された残りの量子状態は
$$ \frac{\eta(a)}{\operatorname{Tr}(\eta(a))} = \frac{\eta(a)}{\Pr(a)} $$
となります。これは教科書の式 $(2.228)$ に対応します。

#### まとめ
教科書の厳密な定式化の素晴らしい点は、部分測定を単に「確率を求めるためだけの計算」で終わらせず、**「古典レジスタを付加して全体系のチャネルを通す」という物理的に実装可能な（現実の）プロセスとして数式化し、最終的に「計算された確率」と「測定後の残りの量子状態」を、1つのアンサンブル $\eta(a)$ または1つの古典-量子状態としてパッケージ化した**点にあります。
これにより、測定結果 $a$ の値を古典通信でアリスからボブへ送り、ボブがその結果（情報 $Z$）を見て自分の残りの量子系を操作する（例：量子通信プロトコル）といった複雑な流れを、一切の曖昧さなく数学的に記述できるようになっています。







