# Section 7.14: Cleaning Lemma for Stabilizer Codes

**Source:** Preskill Lecture Notes, Chapter 7, pp. 43–44 (Physical pages 49–50).

---

The *cleaning lemma* for stabilizer codes says the following: For an $[[n, k]]$ stabilizer code, let $M$ denote a subset of the $n$ qubits in the code block, and let $M^c$ denote the complementary set of qubits. If $x$ is one of the code's logical Pauli operators, we say that $x$ can be *cleaned* on $M$ if there is a logically equivalent Pauli operator $x' = xy$ (where $y$ is an element of the code stabilizer $S$) such that $x'$ acts nontrivially only on $M^c$:
$$
x' = I_M \otimes Q_{M^c}.
$$ {#eq-7.183}
We say that $x$ can be *supported* on $M$ if it can be cleaned on $M^c$. Let $g(M)$ denote the number of independent logical Pauli operators that can be supported on $M$ and let $g(M^c)$ denote the number of independent Pauli operators that can be supported on $M^c$. Then the cleaning lemma asserts that
$$
g(M) + g(M^c) = 2k.
$$ {#eq-7.184}
In particular, therefore, if no logical operator can be supported on $M$, then the complete $k$-qubit logical Pauli group can be supported on its complement.

We say that the subset $M$ is *correctable* if erasure of the qubits in $M$ is a correctable error. From the error correction conditions for stabilizer codes, we may say that if $M$ is correctable, then any Pauli operator supported on $M$ either anticommutes with the stabilizer or is contained in the stabilizer. Conversely, if $M$ is not correctable, then there is a nontrivial Pauli operator supported on $M$ which commutes with the stabilizer and is not contained in the stabilizer; that is, if $M$ is not correctable, then there is a nontrivial logical operator supported on $M$.

To prove the cleaning lemma we proceed as follows. We regard the abelianized $n$-qubit Pauli group $P$ as a $(2n)$-dimensional vector space over the binary field $\mathbb{F}_2$, and say that the vectors $x$ and y are orthogonal if the corresponding elements of $P$ commute. Let $P_M$ denote the subspace of $P$ which is supported on the subset $M$ of the $n$ qubits. Let $S$ denote the stabilizer of an $[[n, k]]$ quantum stabilizer code. Let $[T]$ denote the dimension of a subspace $T$.

We may express $S$ as
$$
S = S_M \oplus S_{M^c} \oplus S'.
$$ {#eq-7.185}
Here $S_M = S \cap P_M$ is the subspace of $S$ which is supported on $M$, $S_{M^c} = S \cap P_{M^c}$ is the subspace of $S$ which is supported on $M^c$, and $S'$ is a third subspace of $S$. For any vector $x$, we may consider its *restriction* $x|_M$ to the set $M$. For a Pauli operator $x = x_1 \otimes x_2$, with $x_1$ supported on $M$ and $x_2$ supported on $M^c$, its restriction to $M$ is $x_1 \otimes I$.

Now consider the restriction $S'|_M$ of $S'$ to $M$. We claim that $[S_M \oplus S'|_M] = [S_M \oplus S'] = [S_M] + [S']$. That is, linearly independent vectors in $S_M + S'$ remain linearly independent when restricted to $M$. If this were not so, then a nontrivial linear combination of these vectors would have a trivial restriction to $M$, and would therefore be contained in $S_{M^c}$.

Let's compute the dimension $[(S^\perp)_M]$ of $(S^\perp)_M = S^\perp \cap P_M$, where $S^\perp$ is the orthogonal complement of $S$ in $P$. Note that, because $S_{M^c}$ is trivially orthogonal to $P_M$, $(S^\perp)_M$ is the orthogonal complement in $P_M$ of the restriction $(S_M \oplus S')|_M$ of $S_M \oplus S'$ to $M$. Therefore, by counting dimensions,
$$
\left[\left(S^\perp\right)_M\right] = [P_M] - [S_M \oplus S'|_M] = [P_M] - [S_M] - [S'].
$$ {#eq-7.186}
By applying the same reasoning with $M$ replaced by $M^c$, we have
$$
\left[\left(S^\perp\right)_{M^c}\right] = [P_{M^c}] - [S_{M^c} \oplus S'|_{M^c}] = [P_{M^c}] - [S_{M^c}] - [S'].
$$ {#eq-7.187}
Logical operators supported on $M$ are elements of $P_M$ which commute with the stabilizer and are not contained in the stabilizer (and same for $M^c$); therefore
$$
\begin{aligned}
g(M) &= \left[\left(S^\perp\right)_M\right] - [S_M] = [P_M] - 2[S_M] - [S'], \\
g(M^c) &= \left[\left(S^\perp\right)_{M^c}\right] - [S_{M^c}] = [P_{M^c}] - 2[S_{M^c}] - [S'],
\end{aligned}
$$ {#eq-7.188}
and hence
$$
\begin{aligned}
g(M) + g(M^c) &= [P_M] + [P_{M^c}] - 2\left([S_M] + [S_{M^c}] + [S']\right) \\
&= [P] - 2[S] = 2n - 2(n-k) = 2k,
\end{aligned}
$$ {#eq-7.189}
as we wanted to show.

An important caveat: For a logical operator $x \in S^\perp \setminus S$, there might exist $y, y'$ in $S$ such that $xy$ is supported on $M$ and $xy'$ is supported on $M^c$. Therefore, we may not conclude from eq.(7.184) that each of the code's $2k$ independent logical Pauli operators can be supported on either $M$ or $M^c$. Consider, for example, the toric code with $k = 2$, where $M$ is a narrow strip of qubits that winds around one cycle of the torus. This strip supports the code's string logical operators $X_1$ and $Z_2$, where 1,2 denote the two protected qubits, and $M^c$ also supports these same two logical operators; hence $g(M) = 2$ and $g(M^c) = 2$. But neither $M$ nor $M^c$ supports $X_2$ or $Z_1$, the string logical operators that wind around the complementary cycle of the torus.

If erasure of $M$ is correctable, then $g(M) = 0$ and we conclude that $g(M^c) = 2k$, so that all logical Pauli operators may be supported on $M^c$. We will use this consequence of the cleaning lemma in the arguments below.
