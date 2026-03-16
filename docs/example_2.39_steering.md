# Example 2.39：もつれを用いた遠隔状態準備 (Steering) と確率計算の基礎

このドキュメントでは、量子情報におけるもっとも強力な確率計算の公式 $p(a) = \operatorname{Tr}(\mu(a)\rho)$ の導出から、その具体的な応用例である Example 2.39（最大もつれ状態を用いた遠隔状態の操作）までを詳しく解説します。

---

## 1. 基礎：なぜ確率が $\operatorname{Tr}(\mu(a)\rho)$ になるのか？

学部レベルのブラケット記法（ベクトル）から、量子情報の密度行列（行列）への橋渡しを整理します。

### 1.1 純粋状態でのボルン則
状態ベクトル $|\psi\rangle$ に対し、測定演算子 $\mu(a)$ による結果 $a$ の出現確率は以下の通りです。
$$ p(a) = \langle \psi | \mu(a) | \psi \rangle $$

### 1.2 トレースによる書き換え
トレースには「巡回性」という強力な性質があります：$\operatorname{Tr}(AB) = \operatorname{Tr}(BA)$。
スカラー値（数字） $c$ は $\operatorname{Tr}(c) = c$ なので、以下のように変形できます。

1.  $$ \langle \psi | \mu(a) | \psi \rangle = \operatorname{Tr}\left( \underline{\langle \psi |} \cdot \underline{\mu(a) | \psi \rangle} \right) $$
2.  下線部 $A = \langle \psi |$ と $B = \mu(a) | \psi \rangle$ の順序を入れ替えます。
3.  $$ = \operatorname{Tr}\left( \mu(a) \cdot \underline{|\psi\rangle \langle \psi |} \right) $$

ここで現れた **$|\psi\rangle\langle \psi |$ こそが密度演算子 $\rho$** です。したがって、
$$ p(a) = \operatorname{Tr}(\mu(a) \rho) = \langle \mu(a), \rho \rangle $$
が得られます（$\langle \cdot, \cdot \rangle$ はヒルベルト・シュミット内積）。

### 1.3 密度行列のメリット
もし状態が「確率 $q_1$ で $|\psi_1\rangle$、確率 $q_2$ で $|\psi_2\rangle$」という混合状態なら、
$$ p(a) = q_1 \operatorname{Tr}(\mu(a)\rho_1) + q_2 \operatorname{Tr}(\mu(a)\rho_2) = \operatorname{Tr}(\mu(a) [q_1\rho_1 + q_2\rho_2]) $$
となります。このように、**$\rho$ という一つの行列を定義するだけで、純粋状態も混合状態も全く同じ式で計算できる**のがこの定式化の最大の利点です。

---

## 2. Example 2.39：最大もつれ状態を用いた具体計算

この基礎を踏まえ、教科書の例題を解いてみましょう。

### 2.1 設定
2つの系 $Y, Z$ が以下の最大もつれ状態 $\sigma$ にあるとします。
$$ \sigma = \frac{1}{|\Sigma|} \sum_{b,c \in \Sigma} E_{b,c} \otimes E_{b,c} $$
系 $Y$ に対して測定 $\mu$ を行い、結果 $a$ を得ます。

### 2.2 ステップ1：系 $Y$ の周辺状態 $\rho_Y$
アリス（系 $Y$）側の確率を出すため、系 $Z$ を部分トレースで消去します。
$$ \rho_Y = \operatorname{Tr}_Z(\sigma) = \frac{1}{|\Sigma|} \sum_{b,c} E_{b,c} \operatorname{Tr}(E_{b,c}) = \frac{1}{|\Sigma|} \sum_{b,c} E_{b,c} \delta_{b,c} = \frac{\mathbb{I}_Y}{|\Sigma|} $$
アリス側から見ると、完全にバラバラな状態（完全混合状態）に見えます。

### 2.3 ステップ2：出現確率 $p(a)$ の計算
セクション1で導出した公式を使います。
$$ p(a) = \operatorname{Tr}(\mu(a) \rho_Y) = \operatorname{Tr}\left( \mu(a) \frac{\mathbb{I}_Y}{|\Sigma|} \right) = \frac{\operatorname{Tr}(\mu(a))}{|\Sigma|} $$
これが教科書の $(2.230)$ 式です。

### 2.4 ステップ3：測定後の系 $Z$ の状態 $\eta(a)$
アリスが結果 $a$ を得たときの、$Z$ 系に残された非正規化状態 $\eta(a)$ を計算します。
$$ \eta(a) = \operatorname{Tr}_Y \left( (\mu(a) \otimes \mathbb{I}_Z) \sigma \right) = \frac{1}{|\Sigma|} \sum_{b,c} \operatorname{Tr}(\mu(a) E_{b,c}) E_{b,c} $$
トレース部分 $\operatorname{Tr}(\mu(a) |b\rangle\langle c|) = \langle c | \mu(a) | b \rangle$ は、行列 $\mu(a)$ の $(c,b)$ 要素、つまり**転置行列 $\mu(a)^T$** の $(b,c)$ 要素です。
$$ \eta(a) = \frac{1}{|\Sigma|} \mu(a)^T $$

### 2.5 ステップ4：正規化された事後状態
$$ \rho_{Z|a} = \frac{\eta(a)}{p(a)} = \frac{\mu(a)^T}{\operatorname{Tr}(\mu(a))} $$
これが教科書の $(2.231)$ 式です。

---

## 3. 結論：何を意味しているのか？

この数式展開からわかる物理的なメッセージは以下の通りです：

1.  **情報の「転写」**: アリスが系 $Y$ で行った測定演算子 $\mu(a)$ の形（の転置）が、そのまま離れた場所にあるボブの系 $Z$ の「状態」として現れます。
2.  **量子ステアリング**: アリスは自分がどの測定（POVM）を選ぶかによって、ボブの系の状態を特定のアンサンブルに誘導（Steer）できます。
3.  **テレポーテーションへの道**: この「測定がつくる状態」という考え方が、後の量子通信プロトコルのすべての基礎になります。
