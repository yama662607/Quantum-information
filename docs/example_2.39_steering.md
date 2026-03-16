# Example 2.39：もつれを用いた遠隔状態準備 (Steering) の計算

この例題は、最大もつれ状態の一方の系に対して測定を行うと、**「驚くべきことに、その測定演算子の形がそのまま他方の系の状態として転写される」**という性質を数学的に示しています。

## 1. 設定（Setup）

2つの系 $Y, Z$（どちらもアルファベット $\Sigma$ に対応する空間 $\mathbb{C}^\Sigma$）が、以下の**最大もつれ状態** $\sigma \in \mathrm{D}(Y \otimes Z)$ にあるとします。

$$ \sigma = \frac{1}{|\Sigma|} \sum_{b,c \in \Sigma} E_{b,c} \otimes E_{b,c} $$

ここで $E_{b,c} = |b\rangle\langle c|$ です。
系 $Y$ に対して、任意の測定（POVM） $\mu: \Sigma \to \mathrm{Pos}(Y)$ を行います。

---

## 2. 測定結果 $a$ が得られる確率 $p(a)$

部分測定のルールによれば、確率は次のように計算されます。

$$ p(a) = \langle \mu(a), \rho_Y \rangle = \operatorname{Tr}(\mu(a) \rho_Y) $$

まず、系 $Y$ の還元済み密度演算子 $\rho_Y$ を求めます。$\rho_Y = \operatorname{Tr}_Z(\sigma)$ です。

$$ 
\begin{aligned}
\rho_Y &= \frac{1}{|\Sigma|} \sum_{b,c} \operatorname{Tr}_Z(E_{b,c} \otimes E_{b,c}) \\
&= \frac{1}{|\Sigma|} \sum_{b,c} E_{b,c} \operatorname{Tr}(E_{b,c}) \\
&= \frac{1}{|\Sigma|} \sum_{b,c} E_{b,c} \delta_{b,c} \\
&= \frac{1}{|\Sigma|} \sum_{b} E_{b,b} = \frac{\mathbb{I}_Y}{|\Sigma|}
\end{aligned}
$$

したがって、確率は以下のようになります（教科書の式 2.230）。

$$ p(a) = \operatorname{Tr}\left(\mu(a) \frac{\mathbb{I}_Y}{|\Sigma|}\right) = \frac{\operatorname{Tr}(\mu(a))}{|\Sigma|} $$

---

## 3. 測定後の系 $Z$ の状態 $\rho_{Z|a}$

測定結果 $a$ が得られたときの系 $Z$ の正規化された状態を計算します。
アンサンブル（非正規化状態） $\eta(a)$ は以下の通りです。

$$ \eta(a) = \operatorname{Tr}_Y \Big( (\mu(a) \otimes \mathbb{I}_Z) \sigma \Big) $$

具体的に $\sigma$ を代入して計算します。

$$ 
\begin{aligned}
\eta(a) &= \frac{1}{|\Sigma|} \sum_{b,c} \operatorname{Tr}_Y \Big( (\mu(a) E_{b,c}) \otimes E_{b,c} \Big) \\
&= \frac{1}{|\Sigma|} \sum_{b,c} \operatorname{Tr}(\mu(a) E_{b,c}) E_{b,c}
\end{aligned}
$$

ここでトレースの中身を評価します。$E_{b,c} = |b\rangle\langle c|$ なので、
$\operatorname{Tr}(\mu(a) |b\rangle\langle c|) = \langle c | \mu(a) | b \rangle$ です。
これは行列 $\mu(a)$ の $(c,b)$ 成分、すなわち **転置行列 $\mu(a)^T$** の $(b,c)$ 成分に他なりません。

$$ 
\begin{aligned}
\eta(a) &= \frac{1}{|\Sigma|} \sum_{b,c} \langle c | \mu(a) | b \rangle E_{b,c} \\
&= \frac{1}{|\Sigma|} \mu(a)^T
\end{aligned}
$$

最後にこれを確率 $p(a)$ で割って正規化します（教科書の式 2.231）。

$$ 
\rho_{Z|a} = \frac{\eta(a)}{p(a)} = \frac{\frac{1}{|\Sigma|} \mu(a)^T}{\frac{\operatorname{Tr}(\mu(a))}{|\Sigma|}} = \frac{\mu(a)^T}{\operatorname{Tr}(\mu(a))}
$$

---

## 4. 物理的メッセージ：なぜ重要か？

この結果は非常に深い意味を持っています。

1.  **Remote State Preparation (遠隔状態準備)**:
    アリスが系 $Y$ を、ボブが系 $Z$ を持っているとします。アリスが自分の系で**どのような測定を選ぶか**によって、ボブの系の状態を「望みの形（$\mu(a)^T$）」に直接誘導（Steer）できることを意味します。
2.  **転置の意味**:
    $\mu(a)^T$ という転置が現れるのは、最大もつれ状態の形に関係しています。ブラケット記法で書くと $\sum |b\rangle|b\rangle$ という対称な形をしているため、一方への作用が他方へ「鏡合わせ（転置）」のように伝わるのです。
3.  **非局所性のデモンストレーション**:
    これは後の章で学ぶ「EPR相関」や「Bellの不等式」、そして「量子テレポーテーション」の理論的な核となる計算です。

::: {.callout-note}
この Example 2.39 は、単なる計算練習ではなく、**「一方の系で行った測定が、他方の系の量子状態を瞬時に決定する」**という量子力学の非局所的な性質を、最も簡潔な数式で示したものです。
:::
