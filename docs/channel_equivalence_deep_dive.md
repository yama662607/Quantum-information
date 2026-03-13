# チャネル表現の同値性証明：数理と物理のディープダイブ（詳細版）

量子チャネルの特徴付け（Theorem 2.26: トレース保存性、Theorem 2.22: 完全正値性）の証明には、単なる式変形を超えた「物理的意味を持つ操作」や「強力な数学的トリック」が埋め込まれています。

ここでは、証明の鍵となるステップを数式を交えて詳細に解説します。

---

## 1. トレース保存 (TP) の証明における鍵：双対性

### 🔑 随伴写像の定義と物理的意味

数学的な定義は以下の内積保存です：
$$ \langle Y, \Phi(X) \rangle = \langle \Phi^*(Y), X \rangle $$
ここで、ヒルベルト・シュミット内積 $\langle A, B \rangle = \mathrm{Tr}(A^* B)$ を用います。

#### 証明のステップ: Trace Preserving $\iff$ Unital Adjoint

1.  **Schrödinger描像（左辺）**:
    「状態 $X$ をチャネル $\Phi$ に通した後、単位演算子 $\mathbb{I}$ （全確率）を測定する」
    $$
    \begin{aligned}
    \mathrm{Tr}(\Phi(X)) &= \mathrm{Tr}(\mathbb{I}^* \Phi(X)) \\
    &= \langle \mathbb{I}, \Phi(X) \rangle
    \end{aligned}
    $$

2.  **Heisenberg描像（右辺）**:
    「随伴チャネル $\Phi^*$ の定義を使って $\Phi$ を反対側に移動させる」
    $$
    \begin{aligned}
    \langle \mathbb{I}, \Phi(X) \rangle &= \langle \Phi^*(\mathbb{I}), X \rangle \\
    &= \mathrm{Tr}( (\Phi^*(\mathbb{I}))^* X )
    \end{aligned}
    $$

3.  **比較と結論**:
    トレース保存条件 $\mathrm{Tr}(\Phi(X)) = \mathrm{Tr}(X)$ は、すべての $X$ について以下が成り立つことと同値です。
    $$ \langle \Phi^*(\mathbb{I}), X \rangle = \langle \mathbb{I}, X \rangle $$
    任意のベクトルに対する内積が等しいなら、ベクトルそのものも等しいため：
    $$ \Phi^*(\mathbb{I}) = \mathbb{I} $$
    これが「随伴写像が単位的（Unital）」という条件の正体です。

---

## 2. 完全正値 (CP) の証明における鍵：Choi行列と分解

### 🔑 Choi-Jamiolkowski 同型による「診断」

Choi行列 $J(\Phi)$ は、正規化されていない最大エンタングル状態 $|\Gamma\rangle = \sum_{i=1}^d |i\rangle|i\rangle$ を入力して得られます。

$$
\begin{aligned}
J(\Phi) &= (\Phi \otimes \mathbb{I}) (|\Gamma\rangle\langle\Gamma|) \\
&= (\Phi \otimes \mathbb{I}) \left( \sum_{i,j} |i\rangle\langle j| \otimes |i\rangle\langle j| \right) \\
&= \sum_{i,j} \Phi(|i\rangle\langle j|) \otimes |i\rangle\langle j|
\end{aligned}
$$

*   **物理的意味**:
    入力の基底 $|i\rangle\langle j|$ が、出力側の第2系（参照系）に $|i\rangle\langle j|$ として「コピー」されています。
    つまり、$J(\Phi)$ は「入力 $i, j$ に対する出力 $\Phi(|i\rangle\langle j|)$ のリスト」そのものです。

### 🔑 Choi行列からKraus表現への変換（構成的証明）

「Choi行列が半正定値 ($J(\Phi) \ge 0$) ならば、Kraus表現が存在する」という証明は、実際にKraus演算子を作る手順になっています。

1.  **スペクトル分解**:
    $J(\Phi)$ はエルミートかつ半正定値なので、非負の固有値 $\lambda_k$ と正規直交固有ベクトル $u_k$ で分解できます。
    $$ J(\Phi) = \sum_k \lambda_k u_k u_k^* $$
    ここで、ベクトル $u_k$ を $\sqrt{\lambda_k}$ 倍して再定義し、$w_k = \sqrt{\lambda_k} u_k$ と置くと：
    $$ J(\Phi) = \sum_k w_k w_k^* $$

2.  **ベクトル化の逆変換 (Unvectorization)**:
    $w_k$ は空間 $\mathcal{Y} \otimes \mathcal{X}$ のベクトルですが、これは演算子 $\mathcal{X} \to \mathcal{Y}$ をベクトル化したものとみなせます。
    $$ \exists A_k \text{ s.t. } \mathrm{vec}(A_k) = w_k $$
    これを用いると、
    $$ J(\Phi) = \sum_k \mathrm{vec}(A_k) \mathrm{vec}(A_k)^* $$

3.  **表現の対応関係**:
    Proposition 2.20 で示された関係式 $\mathrm{vec}(A)\mathrm{vec}(B)^* \iff A(\cdot)B^*$ を使うと、上記のChoi行列に対応する写像は、
    $$ \Phi(X) = \sum_k A_k X A_k^* $$
    となります。
    これで、$A_k = B_k$ となる Kraus 表現（つまり CP 写像）が構成できました！

---

## 3. 数学的に便利なトリック：ベクトル化恒等式

証明中で頻出する $\mathrm{vec}(AXB^*) = (A \otimes \overline{B})\mathrm{vec}(X)$ の導出を少し詳しく見ます。

行列の成分を $(X)_{ij} = x_{ij}$ とし、$X = \sum_{ij} x_{ij} |i\rangle\langle j|$ と展開します。
ベクトル化は $\mathrm{vec}(|i\rangle\langle j|) = |i\rangle \otimes |j\rangle$ と定義されます（列ごとに並べる定義の場合）。

$$
\begin{aligned}
\mathrm{vec}(A X B^*) &= \mathrm{vec}\left( A \left( \sum_{ij} x_{ij} |i\rangle\langle j| \right) B^* \right) \\
&= \sum_{ij} x_{ij} \mathrm{vec}( (A|i\rangle) (\langle j|B^*) ) \\
&= \sum_{ij} x_{ij} \mathrm{vec}( (A|i\rangle) (B|j\rangle)^* ) \quad (\because \langle j|B^* = (B|j\rangle)^*)
\end{aligned}
$$
ここで、$(A|i\rangle)(B|j\rangle)^*$ は、ベクトル $u = A|i\rangle$ と $v = \overline{B|j\rangle}$ （成分の複素共役）の外積 $u v^T$ に対応します。これをベクトル化すると $u \otimes v$ になります（注：定義によりますが、ここでは標準的な $A \otimes \overline{B}$ になる定義を採用）。

$$
\begin{aligned}
&= \sum_{ij} x_{ij} (A|i\rangle) \otimes (\overline{B} |j\rangle) \\
&= (A \otimes \overline{B}) \sum_{ij} x_{ij} (|i\rangle \otimes |j\rangle) \\
&= (A \otimes \overline{B}) \mathrm{vec}(X)
\end{aligned}
$$

この恒等式があるおかげで、
「演算子のサンドイッチ積 $AXB^*$」 $\iff$ 「ベクトルの行列積 $(A \otimes \overline{B})v$」
という変換が自由自在に行えるのです。

---

## まとめ：証明の流れ図

1.  **物理的要請** ($\mathrm{Tr}=1$, $P \ge 0$)
    $\downarrow$
2.  **双対性・Choi同型**
    $\downarrow$
3.  **随伴条件 ($\Phi^*(\mathbb{I})=\mathbb{I}$) / Choi行列条件 ($J \ge 0$)**
    $\downarrow$ (スペクトル分解 & ベクトル化逆変換)
4.  **Kraus表現 / Stinespring表現**

この流れを行き来できることが、量子チャネル理論のマスタリーへの道です。
