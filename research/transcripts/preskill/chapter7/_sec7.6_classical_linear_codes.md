# Section 7.6: Classical Linear Codes [PDF Pages 24-26]

<!-- ============================================================ -->
<!-- Source: chap7.pdf, Physical Pages: 24-26                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 24 -->
## 7.6 Classical Linear Codes

Quantum error-correcting codes were first invented in the mid-1990s, but classical error-correcting codes have a much longer history. Beginning in the 1940s, a remarkably beautiful and powerful theory of classical coding has been erected. Much of this theory can be exploited in the construction of QECC's. Here we will quickly review just a few elements of the classical theory, confining our attention to binary linear codes.

In a binary code, $k$ bits are encoded in a binary string of length $n$. That is, from

<!-- Page 25 -->
among the $2^n$ strings of length $n$, we designate a subset containing $2^k$ strings – the codewords. A $k$-bit message is encoded by selecting one of these $2^k$ codewords.

In the special case of a binary linear code, the codewords form a $k$-dimensional closed linear subspace $C$ of the binary vector space $\mathbb{F}_2^n$. That is, the bitwise XOR of two codewords is another codeword. The space $C$ of the code is spanned by a basis of $k$ vectors $v_1, v_2, \ldots, v_k$; an arbitrary codeword may be expressed as a linear combination of these basis vectors:

$$
v(\alpha_1, \ldots, \alpha_k) = \sum_i \alpha_i v_i,
$$ {#eq-7.75}

where each $\alpha_i \in \{0, 1\}$, and addition is modulo 2. We may say that the length-$n$ vector $v(\alpha_1 \ldots \alpha_k)$ encodes the $k$-bit message $\alpha = (\alpha_1, \ldots, \alpha_k)$.

The $k$ basis vectors $v_1, \ldots, v_k$ may be assembled into a $k \times n$ matrix

$$
G = \begin{pmatrix} v_1 \\ \vdots \\ v_k \end{pmatrix},
$$ {#eq-7.76}

called the generator matrix of the code. Then in matrix notation, eq. (7.75) can be rewritten as

$$
v(\alpha) = \alpha G;
$$ {#eq-7.77}

the matrix $G$, acting to the left, encodes the message $\alpha$.

An alternative way to characterize the $k$-dimensional code subspace of $\mathbb{F}_2^n$ is to specify $n - k$ linear constraints. There is an $(n - k) \times n$ matrix $H$ such that

$$
Hv = 0
$$ {#eq-7.78}

for all those and only those vectors $v$ in the code $C$. This matrix $H$ is called the parity check matrix of the code $C$. The rows of $H$ are $n - k$ linearly independent vectors, and the code space is the space of vectors that are orthogonal to all of these vectors. Orthogonality is defined with respect to the mod 2 bitwise inner product; two length-$n$ binary strings are orthogonal if they “collide” (both take the value 1) at an even number of locations. Note that

$$
HG^T = 0;
$$ {#eq-7.79}

where $G^T$ is the transpose of $G$; the rows of $G$ are orthogonal to the rows of $H$.

For a classical bit, the only kind of error is a bit flip. An error occurring in an $n$-bit string can be characterized by an $n$-component vector $e$, where the 1’s in $e$ mark the locations where errors occur. When afflicted by the error $e$, the string $v$ becomes

$$
v \to v + e.
$$ {#eq-7.80}

Errors can be detected by applying the parity check matrix. If $v$ is a codeword, then

$$
H(v + e) = Hv + He = He.
$$ {#eq-7.81}

$He$ is called the syndrome of the error $e$. Denote by $\mathcal{E}$ the set of errors $\{e_i\}$ that we wish to be able to correct. Error recovery will be possible if and only if all errors $e_i$ have distinct syndromes. If this is the case, we can unambiguously diagnose the error given the syndrome $He$, and we may then recover by flipping the bits specified by $e$ as in

$$
v + e \to (v + e) + e = v.
$$ {#eq-7.82}

<!-- Page 26 -->
On the other hand, if $He_1 = He_2$ for $e_1 \ne e_2$ then we may misinterpret an $e_1$ error as an $e_2$ error; our attempt at recovery then has the effect

$$
v + e_1 \to v + (e_1 + e_2) \ne v.
$$ {#eq-7.83}

The recovered message $v + e_1 + e_2$ lies in the code, but it differs from the intended message $v$; the encoded information has been damaged.

The distance $d$ of a code $C$ is the minimum weight of any vector $v \in C$, where the weight is the number of 1’s in the string $v$. A linear code with distance $d = 2t + 1$ can correct $t$ errors; the code assigns a distinct syndrome to each $e \in \mathcal{E}$, where $\mathcal{E}$ contains all vectors of weight $t$ or less. This is so because, if $He_1 = He_2$, then

$$
0 = He_1 + He_2 = H(e_1 + e_2),
$$ {#eq-7.84}

and therefore $e_1 + e_2 \in C$. But if $e_1$ and $e_2$ are unequal and each has weight no larger than $t$, then the weight of $e_1 + e_2$ is greater than zero and no larger than $2t$. Since $d = 2t + 1$, there is no such vector in $C$. Hence $He_1$ and $He_2$ cannot be equal.

A useful concept in classical coding theory is that of the dual code. We have seen that the $k \times n$ generator matrix $G$ and the $(n - k) \times n$ parity check matrix $H$ of a code $C$ are related by $HG^T = 0$. Taking the transpose, it follows that $GH^T = 0$. Thus we may regard $H^T$ as the generator and $G$ as the parity check of an $(n - k)$-dimensional code, which is denoted $C^\perp$ and called the dual of $C$. In other words, $C^\perp$ is the orthogonal complement of $C$ in $\mathbb{F}_2^n$. A vector is self-orthogonal if it has even weight, so it is possible for $C$ and $C^\perp$ to intersect. A code contains its dual if all of its codewords have even weight and are mutually orthogonal. If $n = 2k$ it is possible that $C = C^\perp$, in which case $C$ is said to be self-dual.

An identity relating the code $C$ and its dual $C^\perp$ will prove useful in the following section:

$$
\sum_{v \in C} (-1)^{v \cdot u} = \begin{cases} 2^k & u \in C^\perp \\ 0 & u \notin C^\perp \end{cases}.
$$ {#eq-7.85}

The nontrivial content of the identity is the statement that the sum vanishes for $u \notin C^\perp$. This readily follows from the familiar identity

$$
\sum_{v \in \{0,1\}^k} (-1)^{v \cdot w} = 0, \quad w \ne 0,
$$ {#eq-7.86}

where $v$ and $w$ are strings of length $k$. We can express $v \in C$ as

$$
v = \alpha G,
$$ {#eq-7.87}

where $\alpha$ is a $k$-vector. Then

$$
\sum_{v \in C} (-1)^{v \cdot u} = \sum_{\alpha \in \{0,1\}^k} (-1)^{\alpha \cdot Gu} = 0,
$$ {#eq-7.88}

for $Gu \ne 0$. Since $G$, the generator matrix of $C$, is the parity check matrix for $C^\perp$, we conclude that the sum vanishes for $u \notin C^\perp$.
