# Section 7.15: Codes Over GF(4)

**Source:** Preskill Lecture Notes, Chapter 7, pp. 44–47 (Physical pages 50–53).

---

We constructed the $[[5, 1, 3]]$ code by guessing the stabilizer generators, and checking that $d = 3$. Is there a more systematic method?

In fact, there is. Our suspicion that the $[[5, 1, 3]]$ code might exist was aroused by the observation that its parameters saturate the quantum sphere-packing inequality for $t = 1$ codes:
$$
1 + 3n = 2^{n-k},
$$ {#eq-7.190}
($16 = 16$ for $n = 5$ and $k = 1$). To a coding theorist, this equation might look familiar.

Aside from the binary codes we have focused on up to now, classical codes can also be constructed from length-$n$ strings of symbols that take values, not in $\{0, 1\}$, but in the finite field with $q$ elements $\mathrm{GF}(q)$. Such finite fields exist for any $q = p^m$, where $p$ is prime. ($\mathrm{GF}$ is short for "Galois Field," in honor of their discoverer.)

For such nonbinary codes, we may model error as addition by an element of the field, a cyclic shift of the $q$ symbols. Then there are $q - 1$ nontrivial errors. The weight of a vector in $\mathrm{GF}(q)^n$ is the number of its nonzero elements, and the distance between two vectors is the weight of their difference (the number of elements that disagree). An $[n, k, d]_q$ classical code consists of $q^k$ codewords in $\mathrm{GF}(q)^n$, where the minimal distance between a pair is $d$. The sphere packing bound that must be satisfied for an $[n, k, d]_q$ code to exist becomes, for $d = 3$,
$$
1 + (q - 1)n \le q^{n-k}.
$$ {#eq-7.191}
In fact, the perfect binary Hamming codes that saturate this bound for $q = 2$ with parameters
$$
n = 2^m - 1, \quad k = n - m,
$$ {#eq-7.192}
admit a generalization to any $\mathrm{GF}(q)$; perfect Hamming codes over $\mathrm{GF}(q)$ can be constructed with
$$
n = \frac{q^m - 1}{q - 1}, \quad k = n - m.
$$ {#eq-7.193}
The $[[5, 1, 3]]$ quantum code is descended from the classical $[5, 3, 3]_4$ Hamming code (the case $q = 4$ and $m = 2$).

What do the classical $\mathrm{GF}(4)$ codes have to do with binary quantum stabilizer codes? The connection arises because the stabilizer can be associated with a set of vectors over $\mathrm{GF}(4)$ closed under addition.

The field $\mathrm{GF}(4)$ has four elements that may be denoted $0, 1, \omega, \bar{\omega}$, where
$$
\begin{aligned}
&1 + 1 = \omega + \omega = \bar{\omega} + \bar{\omega} = 0, \\
&1 + \omega = \bar{\omega},
\end{aligned}
$$ {#eq-7.194}
and $\omega^2 = \bar{\omega}$, $\omega\bar{\omega} = 1$. Thus, the additive structure of $\mathrm{GF}(4)$ echos the multiplicative structure of the Pauli operators $\boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z}$. Indeed, the length-$2n$ binary string $(\alpha|\beta)$ that we have used to denote an element of the Pauli group can equivalently be regarded as a length-$n$ vector in $\mathrm{GF}(4)^n$
$$
(\alpha|\beta) \leftrightarrow \alpha + \beta\omega.
$$ {#eq-7.195}
The stabilizer, with $2^{n-k}$ elements, can be regarded as a subcode of $\mathrm{GF}(4)$, closed under addition and containing $2^{n-k}$ codewords.

Note that the code need not be a vector space over $\mathrm{GF}(4)$, as it is not required to be closed under multiplication by a scalar $\in \mathrm{GF}(4)$. In the special case where the code is a vector space, it is called a *linear code*.

Much is known about codes over $\mathrm{GF}(4)$, so this connection opened the door for the (classical) coding theorists to construct many QECC's.[^fn-calderbank] However, not every subcode of $\mathrm{GF}(4)^n$ is associated with a quantum code; we have not yet imposed the requirement that the stabilizer is abelian — the $(\alpha|\beta)$'s that span the code must be mutually orthogonal in the symplectic inner product
$$
\alpha \cdot \beta' + \alpha' \cdot \beta.
$$ {#eq-7.196}
This orthogonality condition might look strange to a coding theorist, who is more accustomed to defining the inner product of two vectors in $\mathrm{GF}(4)^n$ as an element of $\mathrm{GF}(4)$ given by
$$
v * u = \bar{v}_1 u_1 + \dots + \bar{v}_n u_n,
$$ {#eq-7.197}
where conjugation, denoted by a bar, interchanges $\omega$ and $\bar{\omega}$. If this "hermitian" inner product $*$ of two vectors $v$ and $u$ is
$$
v * u = a + b\omega \in \mathrm{GF}(4),
$$ {#eq-7.198}
then our symplectic inner product is
$$
v \cdot u = b.
$$ {#eq-7.199}
Therefore, vanishing of the symplectic inner product is a weaker condition than vanishing of the hermitian inner product. In fact, though, in the special case of a linear code, self-orthogonality with respect to the hermitian inner product is actually equivalent to self-orthogonality with respect to the symplectic inner product. We observe that if $v * u = a + b\omega$, orthogonality in the symplectic inner product requires $b = 0$. But if $u$ is in a linear code, then so is $\bar{\omega}u$ where
$$
v * (\bar{\omega}u) = b + a\bar{\omega}
$$ {#eq-7.200}
so that
$$
v \cdot (\bar{\omega}u) = a.
$$ {#eq-7.201}
We see that if $v$ and $u$ belong to a linear $\mathrm{GF}(4)$ code and are orthogonal with respect to the symplectic inner product, then they are also orthogonal with respect to the hermitian inner product. We conclude then, that a linear $\mathrm{GF}(4)$ code defines a quantum stabilizer code if and only if the code is self-orthogonal in the hermitian inner product. Classical codes with these properties have been much studied.

In particular, consider again the $[5, 3, 3]_4$ Hamming code. Its parity check matrix (in an unconventional presentation) can be expressed as
$$
H = \begin{pmatrix}
1 & \omega & \omega & 1 & 0 \\
0 & 1 & \omega & \omega & 1
\end{pmatrix},
$$ {#eq-7.202}
which is also the generator matrix of its dual, a linear self-orthogonal $[5, 2, 4]_4$ code. In fact, this $[5, 2, 4]_4$ code, with $4^2 = 16$ codewords, is precisely the stabilizer of the $[[5, 1, 3]]$ quantum code. By identifying $1 \equiv \boldsymbol{X}, \omega \equiv \boldsymbol{Z}$, we recognize the two rows of $H$ as the stabilizer generators $\boldsymbol{M}_1, \boldsymbol{M}_2$. The dual of the Hamming code is a linear code, so linear combinations of the rows are contained in the code. Adding the rows and multiplying by $\omega$ we obtain
$$
\omega(1, \bar{\omega}, 0, \bar{\omega}, 1) = (\omega, 1, 0, 1, \omega),
$$ {#eq-7.203}
which is $\boldsymbol{M}_4$. And if we add $\boldsymbol{M}_4$ to $\boldsymbol{M}_2$ and multiply by $\bar{\omega}$, we find
$$
\bar{\omega}(\omega, 0, \omega, \bar{\omega}, \bar{\omega}) = (1, 0, 1, \omega, \omega),
$$ {#eq-7.204}
which is $\boldsymbol{M}_3$.

The $[[5, 1, 3]]$ code is just one example of a quite general construction. Consider a subcode $C$ of $\mathrm{GF}(4)^n$ that is additive (closed under addition), and self-orthogonal (contained in its dual) with respect to the symplectic inner product. This $\mathrm{GF}(4)$ code can be identified with the stabilizer of a binary QECC with length $n$. If the $\mathrm{GF}(4)$ code contains $2^{n-k}$ codewords, then the QECC has $k$ encoded qubits. The distance $d$ of the QECC is the minimum weight of a vector in $C^\perp \setminus C$.

Another example of a self-orthogonal linear $\mathrm{GF}(4)$ code is the dual of the $m = 3$ Hamming code with
$$
n = \frac{1}{3}(4^3 - 1) = 21.
$$ {#eq-7.205}
The Hamming code has $4^{n-m}$ codewords, and its dual has $4^m = 2^6$ codewords. We immediately obtain a QECC with parameters
$$
[[21, 15, 3]],
$$ {#eq-7.206}
that can correct one error.

[^fn-calderbank]: Calderbank, Rains, Shor, and Sloane, "Quantum error correction via codes over $\mathrm{GF}(4)$," quant-ph/9608006.
