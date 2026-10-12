# Section 7.10: Stabilizer Codes [PDF Pages 33-40]

<!-- ============================================================ -->
<!-- Source: chap7.pdf, Physical Pages: 33-40                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 33 -->
## 7.10 Stabilizer Codes

### 7.10.1 General formulation

We will be able to construct a (nondegenerate) $[[5, 1, 3]]$ quantum code, but to do so, we will need a more powerful procedure for constructing quantum codes than the CSS procedure.

Recall that to establish a criterion for when error recovery is possible, we found it quite useful to expand an error superoperator in terms of the $n$-qubit Pauli operators. But up until now we have not exploited the group structure of these operators (a product of Pauli operators is a Pauli operator). In fact, we will see that group theory is a powerful tool for constructing QECC’s.

For a single qubit, we will find it more convenient now to choose all of the Pauli operators to be represented by real matrices, so I will now use a notation in which $\boldsymbol{Y}$ denotes the anti-hermitian matrix

$$
\boldsymbol{Y} = \boldsymbol{Z}\boldsymbol{X} = i\sigma_y = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix},
$$ {#eq-7.116}

satisfying $\boldsymbol{Y}^2 = -\boldsymbol{I}$. Then the operators

$$
\{\pm\boldsymbol{I}, \pm\boldsymbol{X}, \pm\boldsymbol{Y}, \pm\boldsymbol{Z}\} \equiv \pm\{\boldsymbol{I}, \boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z}\},
$$ {#eq-7.117}

are the elements of a group of order 8.^1

^1 It is not the quaternionic group but the *other* non-abelian group of order 8 — the symmetry group of the square. The element $\boldsymbol{Y}$, of order 4, can be regarded as the $90^\circ$ rotation of the plane, while $\boldsymbol{X}$ and $\boldsymbol{Z}$ are reflections about two orthogonal axes.

The $n$-fold tensor products of single-qubit Pauli operators also form a group

$$
G_n = \pm\{\boldsymbol{I}, \boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z}\}^{\otimes n},
$$ {#eq-7.118}

of order $|G_n| = 2^{2n+1}$ (since there are $4^n$ possible tensor products, and another factor of 2 for the $\pm$ sign) we will refer to $G_n$ as the *$n$-qubit Pauli group*. (In fact, we will use the term “Pauli group” both to refer to the abstract group $G_n$, and to its dimension-$2^n$ faithful unitary representation by tensor products of $2 \times 2$ matrices; its only irreducible representation of dimension greater than 1.) Note that $G_n$ has the two element center $Z_2 = \{\pm\boldsymbol{I}^{\otimes n}\}$. If we quotient out its center, we obtain the group $\bar{G}_n \equiv G_n/Z_2$; this group can also be regarded as a binary vector space of dimension $2^{2n}$, a property that we will exploit below.

The ($2^n$-dimensional representation of the) Pauli group $G_n$ evidently has these properties:

<!-- Page 34 -->

(i) Each $\boldsymbol{M} \in G_n$ is unitary, $\boldsymbol{M}^{-1} = \boldsymbol{M}^\dagger$.
(ii) For each element $\boldsymbol{M} \in G_n$, $\boldsymbol{M}^2 = \pm\boldsymbol{I} \equiv \pm\boldsymbol{I}^{\otimes n}$. Furthermore, $\boldsymbol{M}^2 = \boldsymbol{I}$ if the number of $\boldsymbol{Y}$’s in the tensor product is even, and $\boldsymbol{M}^2 = -\boldsymbol{I}$ if the number of $\boldsymbol{Y}$’s is odd.
(iii) If $\boldsymbol{M}^2 = \boldsymbol{I}$, then $\boldsymbol{M}$ is hermitian ($\boldsymbol{M} = \boldsymbol{M}^\dagger$); if $\boldsymbol{M}^2 = -\boldsymbol{I}$, then $\boldsymbol{M}$ is anti-hermitian ($\boldsymbol{M} = -\boldsymbol{M}^\dagger$).
(iv) Any two elements $\boldsymbol{M}, \boldsymbol{n} \in G_n$ either commute or anti-commute: $\boldsymbol{M}\boldsymbol{n} = \pm\boldsymbol{n}\boldsymbol{M}$.

We will use the Pauli group to characterize a QECC in the following way: Let $S$ denote an abelian subgroup of the $n$-qubit Pauli group $G_n$. Thus all elements of $S$ acting on $\mathcal{H}_{2^n}$ can be simultaneously diagonalized. Then the *stabilizer code* $\mathcal{H}_S \subseteq \mathcal{H}_{2^n}$ associated with $S$ is the simultaneous eigenspace with eigenvalue 1 of all elements of $S$. That is,

$$
|\psi\rangle \in \mathcal{H}_S \quad \text{iff} \quad \boldsymbol{M}|\psi\rangle = |\psi\rangle \text{ for all } \boldsymbol{M} \in S.
$$ {#eq-7.119}

The group $S$ is called the *stabilizer* of the code, since it preserves all of the codewords.

The group $S$ can be characterized by its generators. These are elements $\{\boldsymbol{M}_i\}$ that are *independent* (no one can be expressed as a product of others) and such that each element of $S$ can be expressed as a product of elements of $\{\boldsymbol{M}_i\}$. If $S$ has $n - k$ generators, we can show that the code space $\mathcal{H}_S$ has dimension $2^k$ — there are $k$ encoded qubits.

To verify this, first note that each $\boldsymbol{M} \in S$ must satisfy $\boldsymbol{M}^2 = \boldsymbol{I}$; if $\boldsymbol{M}^2 = -\boldsymbol{I}$, then $\boldsymbol{M}$ cannot have the eigenvalue $+1$. Furthermore, for each $\boldsymbol{M} \neq \pm\boldsymbol{I}$ in $G_n$ that squares to one, the eigenvalues $+1$ and $-1$ have equal degeneracy. This is because for each $\boldsymbol{M} \neq \pm\boldsymbol{I}$, there is an $\boldsymbol{n} \in G_n$ that anti-commutes with $\boldsymbol{M}$,

$$
\boldsymbol{n}\boldsymbol{M} = -\boldsymbol{M}\boldsymbol{n};
$$ {#eq-7.120}

therefore, $\boldsymbol{M}|\psi\rangle = |\psi\rangle$ if and only if $\boldsymbol{M}(\boldsymbol{n}|\psi\rangle) = -\boldsymbol{n}|\psi\rangle$, and the action of the unitary $\boldsymbol{n}$ establishes a $1-1$ correspondence between the $+1$ eigenstates of $\boldsymbol{M}$ and the $-1$ eigenstates. Hence there are $\frac{1}{2}(2^n) = 2^{n-1}$ mutually orthogonal states that satisfy

$$
\boldsymbol{M}_1|\psi\rangle = |\psi\rangle,
$$ {#eq-7.121}

where $\boldsymbol{M}_1$ is one of the generators of $S$.

Now let $\boldsymbol{M}_2$ be another element of $G_n$ that commutes with $\boldsymbol{M}_1$ such that $\boldsymbol{M}_2 \neq \pm\boldsymbol{I}, \pm\boldsymbol{M}_1$. We can find an $\boldsymbol{n} \in G_n$ that commutes with $\boldsymbol{M}_1$ but anti-commutes with $\boldsymbol{M}_2$; therefore $\boldsymbol{n}$ preserves the $+1$ eigenspace of $\boldsymbol{M}_1$, but within this space, it interchanges the $+1$ and $-1$ eigenstates of $\boldsymbol{M}_2$. It follows that the space satisfying

$$
\boldsymbol{M}_1|\psi\rangle = \boldsymbol{M}_2|\psi\rangle = |\psi\rangle,
$$ {#eq-7.122}

has dimension $2^{n-2}$.

Continuing in this way, we note that if $\boldsymbol{M}_j$ is independent of $\{\boldsymbol{M}_1, \boldsymbol{M}_2, \dots, \boldsymbol{M}_{j-1}\}$, then there is an $\boldsymbol{n}$ that commutes with $\boldsymbol{M}_1, \dots, \boldsymbol{M}_{j-1}$, but anti-commutes with $\boldsymbol{M}_j$ (we’ll discuss in more detail below how such an $\boldsymbol{n}$ can be found). Therefore, restricted to the space with $\boldsymbol{M}_1 = \boldsymbol{M}_2 = \dots = \boldsymbol{M}_{j-1} = 1$, $\boldsymbol{M}_j$ has as many $+1$ eigenvectors as $-1$ eigenvectors. So adding another generator always cuts the dimension of the simultaneous eigenspace in half. With $n - k$ generators, the dimension of the remaining space is $2^n (1/2)^{n-k} = 2^k$.

The stabilizer language is useful because it provides a simple way to characterize the errors that the code can detect and correct. We may think of the $n - k$ stabilizer generators $\boldsymbol{M}_1, \dots, \boldsymbol{M}_{n-k}$, as the *check operators* of the code, the collective observables that we measure to diagnose the errors. If the encoded information is undamaged, then

<!-- Page 35 -->

we will find $\boldsymbol{M}_i = 1$ for each of the generators; but if $\boldsymbol{M}_i = -1$ for some $i$, then the data is orthogonal to the code subspace and an error has been detected.

Recall that the error superoperator can be expanded in terms of elements $\boldsymbol{E}_a$ of the Pauli group. A particular $\boldsymbol{E}_a$ either commutes or anti-commutes with a particular stabilizer generator $\boldsymbol{M}$. If $\boldsymbol{E}_a$ and $\boldsymbol{M}$ commute, then

$$
\boldsymbol{M}\boldsymbol{E}_a|\psi\rangle = \boldsymbol{E}_a\boldsymbol{M}|\psi\rangle = \boldsymbol{E}_a|\psi\rangle,
$$ {#eq-7.123}

for $|\psi\rangle \in \mathcal{H}_S$, so the error preserves the value $\boldsymbol{M} = 1$. But if $\boldsymbol{E}_a$ and $\boldsymbol{M}$ anti-commute, then

$$
\boldsymbol{M}\boldsymbol{E}_a|\psi\rangle = -\boldsymbol{E}_a\boldsymbol{M}|\psi\rangle = -\boldsymbol{E}_a|\psi\rangle,
$$ {#eq-7.124}

so that the error flips the value of $\boldsymbol{M}$, and the error can be detected by measuring $\boldsymbol{M}$. For stabilizer generators $\boldsymbol{M}_i$ and errors $\boldsymbol{E}_a$, we may write

$$
\boldsymbol{M}_i\boldsymbol{E}_a = (-1)^{s_{ia}} \boldsymbol{E}_a\boldsymbol{M}_i.
$$ {#eq-7.125}

The $s_{ia}$’s, $i = 1, \dots, n-k$ constitute a *syndrome* for the error $\boldsymbol{E}_a$, as $(-1)^{s_{ia}}$ will be the result of measuring $\boldsymbol{M}_i$ if the error $\boldsymbol{E}_a$ occurs. In the case of a nondegenerate code, the $s_{ia}$’s will be distinct for all $\boldsymbol{E}_a \in \mathcal{E}$, so that measuring the $n - k$ stabilizer generators will diagnose the error completely.

More generally, let us find a condition to be satisfied by the stabilizer that is sufficient to ensure that error recovery is possible. Recall that it is sufficient that, for each $\boldsymbol{E}_a, \boldsymbol{E}_b \in \mathcal{E}$, and normalized $|\psi\rangle$ in the code subspace, we have

$$
\langle\psi|\boldsymbol{E}_a^\dagger\boldsymbol{E}_b|\psi\rangle = C_{ab},
$$ {#eq-7.126}

where $C_{ab}$ is independent of $|\psi\rangle$. We can see that this condition is satisfied provided that, for each $\boldsymbol{E}_a, \boldsymbol{E}_b \in \mathcal{E}$, one of the following holds:

1) $\boldsymbol{E}_a^\dagger\boldsymbol{E}_b \in S$,
2) There is an $\boldsymbol{M} \in S$ that anti-commutes with $\boldsymbol{E}_a^\dagger\boldsymbol{E}_b$.

**Proof:** In case (1) $\langle\psi|\boldsymbol{E}_a^\dagger\boldsymbol{E}_b|\psi\rangle = \langle\psi|\psi\rangle = 1$, for $|\psi\rangle \in \mathcal{H}_S$. In case (2), suppose $\boldsymbol{M} \in S$ and $\boldsymbol{M}\boldsymbol{E}_a^\dagger\boldsymbol{E}_b = -\boldsymbol{E}_a^\dagger\boldsymbol{E}_b\boldsymbol{M}$. Then

$$
\begin{aligned}
\langle\psi|\boldsymbol{E}_a^\dagger\boldsymbol{E}_b|\psi\rangle &= \langle\psi|\boldsymbol{E}_a^\dagger\boldsymbol{E}_b\boldsymbol{M}|\psi\rangle \\
&= -\langle\psi|\boldsymbol{M}\boldsymbol{E}_a^\dagger\boldsymbol{E}_b|\psi\rangle = -\langle\psi|\boldsymbol{E}_a^\dagger\boldsymbol{E}_b|\psi\rangle,
\end{aligned}
$$ {#eq-7.127}

and therefore $\langle\psi|\boldsymbol{E}_a^\dagger\boldsymbol{E}_b|\psi\rangle = 0$.

Thus, a *stabilizer code* that corrects $\{\mathcal{E}\}$ is a space $\mathcal{H}_S$ fixed by an abelian subgroup $S$ of the Pauli group, where either (1) or (2) is satisfied by each $\boldsymbol{E}_a^\dagger\boldsymbol{E}_b$ with $\boldsymbol{E}_{a,b} \in \mathcal{E}$. The code is *nondegenerate* if condition (1) is not satisfied for any $\boldsymbol{E}_a^\dagger\boldsymbol{E}_b$.

Evidently we could also just as well choose the code subspace to be any one of the $2^{n-k}$ simultaneous eigenspaces of $n - k$ independent commuting elements of $G_n$. But in fact all of these codes are equivalent. We may regard two stabilizer codes as *equivalent* if they differ only according to how the qubits are labeled, and how the basis for each single-qubit Hilbert space is chosen — that is the stabilizer of one code is transformed to the stabilizer of the other by a permutation of the qubits together with a tensor product of single-qubit transformations. If we partition the stabilizer generators into two sets $\{\boldsymbol{M}_1, \dots, \boldsymbol{M}_j\}$ and $\{\boldsymbol{M}_{j+1}, \dots, \boldsymbol{M}_{n-k}\}$, then there exists an $\boldsymbol{n} \in G_n$ that commutes with each member of the first set and anti-commutes with each member of the second

<!-- Page 36 -->

set. Applying $\boldsymbol{n}$ to $|\psi\rangle \in \mathcal{H}_S$ preserves the eigenvalues of the first set while flipping the eigenvalues of the second set. Since $\boldsymbol{n}$ is just a tensor product of single-qubit unitary transformations, there is no loss of generality (up to equivalence) in choosing all of the eigenvalues to be one. Furthermore, since minus signs don’t really matter when the stabilizer is specified, we may just as well say that two codes are equivalent if, up to phases, the stabilizers differ by a permutation of the $n$ qubits, and permutations on each individual qubits of the operators $\boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z}$.

Recovery may fail if there is an $\boldsymbol{E}_a^\dagger\boldsymbol{E}_b$ that *commutes* with the stabilizer but does not lie in the stabilizer. This is an operator that preserves the code subspace $\mathcal{H}_S$ but may act nontrivially in that space; thus it can modify encoded information. Since $\boldsymbol{E}_a|\psi\rangle$ and $\boldsymbol{E}_b|\psi\rangle$ have the same syndrome, we might mistakenly interpret an $\boldsymbol{E}_a$ error as an $\boldsymbol{E}_b$ error; the effect of the error together with the attempt at recovery is that $\boldsymbol{E}_b^\dagger\boldsymbol{E}_a$ gets applied to the data, which can cause damage.

A stabilizer code with distance $d$ has the property that each $\boldsymbol{E} \in G_n$ of weight less than $d$ either lies in the stabilizer or anti-commutes with some element of the stabilizer. The code is nondegenerate if the stabilizer contains no elements of weight less than $d$. A distance $d = 2t + 1$ code can correct $t$ errors, and a distance $s + 1$ code can detect $s$ errors or correct $s$ errors at known locations.

### 7.10.2 Symplectic Notation

Properties of stabilizer codes are often best explained and expressed using the language of linear algebra. The stabilizer $S$ of the code, an order $2^{n-k}$ abelian subgroup of the Pauli group with all elements squaring to the identity, can equivalently be regarded as a dimension $n - k$ closed linear subspace of $\mathbb{F}_2^{2n}$, self orthogonal with respect to a certain (symplectic) inner product.

The group $\bar{G}_n = G_n/Z_2$ is isomorphic to the binary vector space $\mathbb{F}_2^{2n}$. We establish this by observing that, since $\boldsymbol{Y} = \boldsymbol{Z}\boldsymbol{X}$, any element $\boldsymbol{M}$ of the Pauli group (up to the $\pm$ sign) can be expressed as a product of $\boldsymbol{Z}$’s and $\boldsymbol{X}$’s; we may write

$$
\boldsymbol{M} = \boldsymbol{Z}_M \cdot \boldsymbol{X}_M,
$$ {#eq-7.128}

where $\boldsymbol{Z}_M$ is a tensor product of $\boldsymbol{Z}$’s and $\boldsymbol{X}_M$ is a tensor product of $\boldsymbol{X}$’s. More explicitly, a Pauli operator may be written as

$$
(\alpha|\beta) \equiv \boldsymbol{Z}(\alpha)\boldsymbol{X}(\beta) = \bigotimes_{i=1}^n \boldsymbol{Z}^{\alpha_i} \cdot \bigotimes_{i=1}^n \boldsymbol{X}^{\beta_i},
$$ {#eq-7.129}

where $\alpha$ and $\beta$ are binary strings of length $n$. (Then $\boldsymbol{Y}$ acts at the locations where $\alpha$ and $\beta$ “collide.”) Multiplication in $\bar{G}_n$ maps to addition in $\mathbb{F}_2^{2n}$:

$$
(\alpha|\beta)(\alpha'|\beta') = (-1)^{\alpha' \cdot \beta} (\alpha + \alpha' | \beta + \beta');
$$ {#eq-7.130}

the phase arises because $\alpha' \cdot \beta$ counts the number of times a $\boldsymbol{Z}$ is interchanged with a $\boldsymbol{X}$ as the product is rearranged into the standard form of eq. (7.129).

It follows from eq. (7.130) that the commutation properties of the Pauli operators can be expressed in the form

$$
(\alpha|\beta)(\alpha'|\beta') = (-1)^{\alpha \cdot \beta' + \alpha' \cdot \beta} (\alpha'|\beta')(\alpha|\beta)
$$ {#eq-7.131}

<!-- Page 37 -->

Thus two Pauli operators commute if and only if the corresponding vectors are orthogonal with respect to the “symplectic” inner product

$$
\alpha \cdot \beta' + \alpha' \cdot \beta.
$$ {#eq-7.132}

We also note that the square of a Pauli operator is

$$
(\alpha|\beta)^2 = (-1)^{\alpha \cdot \beta} \boldsymbol{I},
$$ {#eq-7.133}

since $\alpha \cdot \beta$ counts the number of $\boldsymbol{Y}$’s in the operator; it squares to the identity if and only if

$$
\alpha \cdot \beta = 0.
$$ {#eq-7.134}

Note that a closed subspace, where each element has this property, is automatically self-orthogonal, since

$$
\alpha \cdot \beta' + \alpha' \cdot \beta = (\alpha + \alpha') \cdot (\beta + \beta') - \alpha \cdot \beta - \alpha' \cdot \beta' = 0;
$$ {#eq-7.135}

in the group language, that is, a subgroup of $G_n$ with each element squaring to $\boldsymbol{I}$ is automatically abelian.

Using the linear algebra language, some of the statements made earlier about the Pauli group can be easily verified by counting linear constraints. Elements are independent if the corresponding vectors are linearly independent over $\mathbb{F}_2^{2n}$, so we may think of the $n - k$ generators of the stabilizer as a basis for a linear subspace of dimension $n - k$. We will use the notation $S$ to denote both the linear space and the corresponding abelian group. Then $S^\perp$ denotes the dimension-$n + k$ space of vectors that are orthogonal to each vector in $S$ (with respect to the symplectic inner product). Note that $S^\perp$ contains $S$, since all vectors in $S$ are mutually orthogonal. In the group language, corresponding to $S^\perp$ is the normalizer (or centralizer) group $N(S)$ ($\equiv S^\perp$) of $S$ in $G_n$ — the subgroup of $G_n$ containing all elements that commute with each element of $S$. Since $S$ is abelian, it is contained in its own normalizer, which also contains other elements (to be further discussed below). The stabilizer of a distance $d$ code has the property that each $(\alpha|\beta)$ whose weight $\sum_i (\alpha_i \lor \beta_i)$ is less than $d$ either lies *in* the stabilizer subspace $S$ or lies *outside* the orthogonal space $S^\perp$.

A code can be characterized by its stabilizer, a stabilizer by its generators, and the $n - k$ generators can be represented by an $(n - k) \times 2n$ matrix

$$
H = (H_Z | H_X).
$$ {#eq-7.136}

Here each row is a Pauli operator, expressed in the $(\alpha|\beta)$ notation. The syndrome of an error $\boldsymbol{E}_a = (\alpha_a | \beta_a)$ is determined by its commutation properties with the generators $\boldsymbol{M}_i = (\alpha'_i | \beta'_i)$; that is

$$
s_{ia} = (\alpha_a | \beta_a) \cdot (\alpha'_i | \beta'_i) = \alpha_a \cdot \beta'_i + \alpha'_i \cdot \beta_a.
$$ {#eq-7.137}

In the case of a nondegenerate code, each error has a distinct syndrome. If the code is degenerate, there may be several errors with the same syndrome, but we may apply any one of the $\boldsymbol{E}_a^\dagger$ corresponding to the observed syndrome in order to recover.

### 7.10.3 Some examples of stabilizer codes

**(a) The nine-qubit code.** This $[[9, 1, 3]]$ code has eight stabilizer generators that can

<!-- Page 38 -->

be expressed as

$$
\begin{aligned}
&\boldsymbol{Z}_1\boldsymbol{Z}_2, \quad \boldsymbol{Z}_2\boldsymbol{Z}_3, \quad \boldsymbol{Z}_4\boldsymbol{Z}_5, \quad \boldsymbol{Z}_5\boldsymbol{Z}_6, \quad \boldsymbol{Z}_7\boldsymbol{Z}_8, \quad \boldsymbol{Z}_8\boldsymbol{Z}_9, \\
&\boldsymbol{X}_1\boldsymbol{X}_2\boldsymbol{X}_3\boldsymbol{X}_4\boldsymbol{X}_5\boldsymbol{X}_6, \quad \boldsymbol{X}_4\boldsymbol{X}_5\boldsymbol{X}_6\boldsymbol{X}_7\boldsymbol{X}_8\boldsymbol{X}_9.
\end{aligned}
$$ {#eq-7.138}

In the notation of eq. (7.136) these become

$$
\left(\begin{array}{ccc|ccc|ccc|ccccccccc}
1 & 1 & 0 & & & & & & & & & & & & & & & \\
0 & 1 & 1 & & 0 & & & 0 & & & & & & & & & & \\
\hline
& & & 1 & 1 & 0 & & & & & & & & & & & & \\
& 0 & & 0 & 1 & 1 & & 0 & & & & & 0 & & & & & \\
\hline
& & & & & & 1 & 1 & 0 & & & & & & & & & \\
& 0 & & & 0 & & 0 & 1 & 1 & & & & & & & & & \\
\hline
& & & & & & & & & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 0 & 0 \\
& & & & 0 & & & & & 0 & 0 & 0 & 1 & 1 & 1 & 1 & 1 & 1
\end{array}\right)
$$

**(b) The seven-qubit code.** This $[[7, 1, 3]]$ code has six stabilizer generators, which can be expressed as

$$
\tilde{H} = \begin{pmatrix} H_{\text{ham}} & 0 \\ 0 & H_{\text{ham}} \end{pmatrix},
$$ {#eq-7.139}

where $H_{\text{ham}}$ is the $3 \times 7$ parity-check matrix of the classical $[7, 4, 3]$ Hamming code. The three check operators

$$
\begin{aligned}
\boldsymbol{M}_1 &= \boldsymbol{Z}_1\boldsymbol{Z}_3\boldsymbol{Z}_5\boldsymbol{Z}_7, \\
\boldsymbol{M}_2 &= \boldsymbol{Z}_2\boldsymbol{Z}_3\boldsymbol{Z}_6\boldsymbol{Z}_7, \\
\boldsymbol{M}_3 &= \boldsymbol{Z}_4\boldsymbol{Z}_5\boldsymbol{Z}_6\boldsymbol{Z}_7,
\end{aligned}
$$ {#eq-7.140}

detect the bit flips, and the three check operators

$$
\begin{aligned}
\boldsymbol{M}_4 &= \boldsymbol{X}_1\boldsymbol{X}_3\boldsymbol{X}_5\boldsymbol{X}_7, \\
\boldsymbol{M}_5 &= \boldsymbol{X}_2\boldsymbol{X}_3\boldsymbol{X}_6\boldsymbol{X}_7, \\
\boldsymbol{M}_6 &= \boldsymbol{X}_4\boldsymbol{X}_5\boldsymbol{X}_6\boldsymbol{X}_7,
\end{aligned}
$$ {#eq-7.141}

detect the phase errors. The space with $\boldsymbol{M}_1 = \boldsymbol{M}_2 = \boldsymbol{M}_3 = 1$ is spanned by the codewords that satisfy the Hamming parity check. Recalling that a Hadamard change of basis interchanges $\boldsymbol{Z}$ and $\boldsymbol{X}$, we see that the space with $\boldsymbol{M}_4 = \boldsymbol{M}_5 = \boldsymbol{M}_6$ is spanned by codewords that satisfy the Hamming parity check in the Hadamard-rotated basis. Indeed, we constructed the seven-qubit code by demanding that the Hamming parity check be satisfied in both bases. The generators commute because the Hamming code contains its dual code; *i.e.*, each row of $H_{\text{ham}}$ satisfies the Hamming parity check.

**(c) CSS codes.** Recall whenever an $[n, k, d]$ classical code $C$ contains its dual code $C^\perp$, we can perform the CSS construction to obtain an $[[n, 2k - n, d]]$ quantum code. The stabilizer of this code can be written as

$$
\tilde{H} = \begin{pmatrix} H & 0 \\ 0 & H \end{pmatrix}
$$ {#eq-7.142}

where $H$ is the $(n - k) \times n$ parity check matrix of $C$. As for the seven-qubit code, the stabilizers commute because $C$ contains $C^\perp$, and the code subspace

<!-- Page 39 -->

is spanned by states that satisfy the $H$ parity check in both the $F$-basis and the $P$-basis. Equivalently, codewords obey the $H$ parity check and are invariant under

$$
|v\rangle \to |v + w\rangle,
$$ {#eq-7.143}

where $w \in C^\perp$.

**(d) More general CSS codes.** Consider, more generally, a stabilizer whose generators can each be chosen to be either a product of $\boldsymbol{Z}$’s $(\alpha|0)$ or a product of $\boldsymbol{X}$’s $(0|\beta)$. Then the generators have the form

$$
\tilde{H} = \begin{pmatrix} H_Z & 0 \\ 0 & H_X \end{pmatrix}.
$$ {#eq-7.144}

Now, what condition must $H_X$ and $H_Z$ satisfy if the $\boldsymbol{Z}$-generators and $\boldsymbol{X}$-generators are to commute? Since $\boldsymbol{Z}$’s must collide with $\boldsymbol{X}$’s an even number of times, we have

$$
H_X H_Z^T = H_Z H_X^T = 0.
$$ {#eq-7.145}

But this is just the requirement that the dual $C_X^\perp$ of the code whose parity check is $H_X$ be contained in the code $C_Z$ whose parity check is $H_Z$. In other words, this QECC fits into the CSS framework, with

$$
C_2 = C_X^\perp \subseteq C_1 = C_Z.
$$ {#eq-7.146}

So we may characterize CSS codes as those and only those for which the stabilizer has generators of the form eq. (7.144).

However there is a caveat. The code defined by eq. (7.144) will be nondegenerate if errors are restricted to weight less than $d = \min(d_Z, d_X)$ (where $d_Z$ is the distance of $C_Z$, and $d_X$ the distance of $C_X$). But the true distance of the QECC could exceed $d$. For example, the 9-qubit code is in this generalized sense a CSS code. But in that case the classical code $C_X$ is distance 1, reflecting that, *e.g.*, $\boldsymbol{Z}_1\boldsymbol{Z}_2$ is contained in the stabilizer. Nevertheless, the distance of the CSS code is $d = 3$, since no weight-2 Pauli operator lies in $S^\perp \setminus S$.

### 7.10.4 Encoded qubits

We have seen that the troublesome errors are those in $S^\perp \setminus S$ — those that commute with the stabilizer, but lie outside of it. These Pauli operators are also of interest for another reason: they can be regarded as the “logical” operations that act on the encoded data that is protected by the code.

Appealing to the “linear algebra” viewpoint, we can see that the normalizer $S^\perp$ of the stabilizer contains $n + k$ independent generators — in the $2n$-dimensional space of the $(\alpha|\beta)$’s, the subspace containing the vectors that are orthogonal to each of $n - k$ linearly independent vectors has dimension $2n - (n - k) = n + k$. Of the $n + k$ vectors that span this space, $n - k$ can be chosen to be the generators of the stabilizer itself. The remaining $2k$ generators preserve the code subspace because they commute with the stabilizer, but act nontrivially on the $k$ encoded qubits.

In fact, these $2k$ operations can be chosen to be the single-qubit operators $\bar{\boldsymbol{Z}}_i, \bar{\boldsymbol{X}}_i, i = 1, 2, \dots, k$, where $\bar{\boldsymbol{Z}}_i, \bar{\boldsymbol{X}}_i$ are the Pauli operators $\boldsymbol{Z}$ and $\boldsymbol{X}$ acting on the encoded qubit labeled by $i$. First, note that we can extend the $n - k$ stabilizer generators to a maximal

<!-- Page 40 -->

set of $n$ commuting operators. The $k$ operators that we add to the set may be denoted $\bar{\boldsymbol{Z}}_1, \dots, \bar{\boldsymbol{Z}}_k$. We can then regard the simultaneous eigenstates of $\bar{\boldsymbol{Z}}_1, \dots, \bar{\boldsymbol{Z}}_k$ (in the code subspace $\mathcal{H}_S$) as the logical basis states $|\bar{z}_1, \dots, \bar{z}_k\rangle$, with $\bar{z}_j = 0$ corresponding to $\bar{\boldsymbol{Z}}_j = 1$ and $\bar{z}_j = 1$ corresponding to $\bar{\boldsymbol{Z}}_j = -1$.

The remaining $k$ generators of the normalizer may be chosen to be mutually commuting and to commute with the stabilizer, but then they will not commute with any of the $\bar{\boldsymbol{Z}}_i$’s. By invoking a Gram-Schmidt orthonormalization procedure, we can choose these generators, denoted $\bar{\boldsymbol{X}}_i$, to diagonalize the symplectic form, so that

$$
\bar{\boldsymbol{Z}}_i\bar{\boldsymbol{X}}_j = (-1)^{\delta_{ij}}\bar{\boldsymbol{X}}_j\bar{\boldsymbol{Z}}_i.
$$ {#eq-7.147}

Thus, each $\bar{\boldsymbol{X}}_j$ flips the eigenvalue of the corresponding $\bar{\boldsymbol{Z}}_j$, and it can so be regarded as the Pauli operator $\boldsymbol{X}$ acting on encoded qubit $i$.

**(a) The 9-qubit Code.** As we have discussed previously, the logical operators can be chosen to be

$$
\begin{aligned}
\bar{\boldsymbol{Z}} &= \boldsymbol{X}_1\boldsymbol{X}_2\boldsymbol{X}_3, \\
\bar{\boldsymbol{X}} &= \boldsymbol{Z}_1\boldsymbol{Z}_4\boldsymbol{Z}_7.
\end{aligned}
$$ {#eq-7.148}

These anti-commute with one another (an $\boldsymbol{X}$ and a $\boldsymbol{Z}$ collide at position 1), commute with the stabilizer generators, and are independent of the generators (no element of the stabilizer contains three $\boldsymbol{X}$’s or three $\boldsymbol{Z}$’s).

**(b) The 7-qubit code.** We have seen that

$$
\begin{aligned}
\bar{\boldsymbol{X}} &= \boldsymbol{X}_1\boldsymbol{X}_2\boldsymbol{X}_3, \\
\bar{\boldsymbol{Z}} &= \boldsymbol{Z}_1\boldsymbol{Z}_2\boldsymbol{Z}_3;
\end{aligned}
$$ {#eq-7.149}

then $\bar{\boldsymbol{X}}$ adds an odd Hamming codeword and $\bar{\boldsymbol{Z}}$ flips the phase of an odd Hamming codeword. These operations implement a bit flip and phase flip respectively in the basis $\{|\bar{0}\rangle_F, |\bar{1}\rangle_F\}$ defined in eq. (7.102).
