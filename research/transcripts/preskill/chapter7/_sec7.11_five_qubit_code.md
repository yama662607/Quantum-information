# Section 7.11: The 5-Qubit Code [PDF Pages 40-44]

<!-- ============================================================ -->
<!-- Source: chap7.pdf, Physical Pages: 40-44                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 40 -->
## 7.11 The 5-Qubit Code

All of the QECC’s that we have considered so far are of the CSS type — each stabilizer generator is either a product of $\boldsymbol{Z}$’s or a product of $\boldsymbol{X}$’s. But not all stabilizer codes have this property. An example of a non-CSS stabilizer code is the perfect nondegenerate $[[5, 1, 3]]$ code.

Its four stabilizer generators can be expressed

$$
\begin{aligned}
\boldsymbol{M}_1 &= \boldsymbol{X}\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{X}\boldsymbol{I}, \\
\boldsymbol{M}_2 &= \boldsymbol{I}\boldsymbol{X}\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{X}, \\
\boldsymbol{M}_3 &= \boldsymbol{X}\boldsymbol{I}\boldsymbol{X}\boldsymbol{Z}\boldsymbol{Z}, \\
\boldsymbol{M}_4 &= \boldsymbol{Z}\boldsymbol{X}\boldsymbol{I}\boldsymbol{X}\boldsymbol{Z},
\end{aligned}
$$ {#eq-7.150}

$\boldsymbol{M}_{2,3,4}$ are obtained from $\boldsymbol{M}_1$ by performing a cyclic permutation of the qubits. (The fifth operator obtained by a cyclic permutation of the qubits, $\boldsymbol{M}_5 = \boldsymbol{Z}\boldsymbol{Z}\boldsymbol{X}\boldsymbol{I}\boldsymbol{X} = \boldsymbol{M}_1\boldsymbol{M}_2\boldsymbol{M}_3\boldsymbol{M}_4$ is not independent of the other four.) Since a cyclic permutation of a generator is another generator, the code itself is cyclic — a cyclic permutation of a codeword is a codeword.

Clearly each $\boldsymbol{M}_i$ contains no $\boldsymbol{Y}$’s and so squares to $\boldsymbol{I}$.

<!-- Page 41 -->

For each pair of generators, there are two collisions between an $\boldsymbol{X}$ and a $\boldsymbol{Z}$, so that the generators commute. One can quickly check that each Pauli operator of weight 1 or weight 2 anti-commutes with at least one generator, so that the distance of the code is 3.

Consider, for example, whether there are error operators with support on the first two qubits that commute with all four generators. The weight-2 operator, to commute with the $\boldsymbol{I}\boldsymbol{X}$ in $\boldsymbol{M}_2$ and the $\boldsymbol{X}\boldsymbol{I}$ in $\boldsymbol{M}_3$, must be $\boldsymbol{X}\boldsymbol{X}$. But $\boldsymbol{X}\boldsymbol{X}$ anti-commutes with the $\boldsymbol{X}\boldsymbol{Z}$ in $\boldsymbol{M}_1$ and the $\boldsymbol{Z}\boldsymbol{X}$ in $\boldsymbol{M}_4$.

In the symplectic notation, the stabilizer may be represented as

$$
\tilde{H} = \left(\begin{array}{ccccc|ccccc}
0 & 1 & 1 & 0 & 0 & 1 & 0 & 0 & 1 & 0 \\
0 & 0 & 1 & 1 & 0 & 0 & 1 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 & 1 & 1 & 0 & 1 & 0 & 0 \\
1 & 0 & 0 & 0 & 1 & 0 & 1 & 0 & 1 & 0
\end{array}\right)
$$ {#eq-7.151}

This matrix has a nice interpretation, as each of its columns can be regarded as the *syndrome* of a single-qubit error. For example, the single-qubit bit flip operator $\boldsymbol{X}_j$, commutes with $\boldsymbol{M}_i$ if $\boldsymbol{M}_i$ has an $\boldsymbol{I}$ or $\boldsymbol{X}$ in position $j$, and anti-commutes if $\boldsymbol{M}_i$ has a $\boldsymbol{Z}$ in position $j$. Thus the table

| | $\boldsymbol{X}_1$ | $\boldsymbol{X}_2$ | $\boldsymbol{X}_3$ | $\boldsymbol{X}_4$ | $\boldsymbol{X}_5$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $\boldsymbol{M}_1$ | 0 | 1 | 1 | 0 | 0 |
| $\boldsymbol{M}_2$ | 0 | 0 | 1 | 1 | 0 |
| $\boldsymbol{M}_3$ | 0 | 0 | 0 | 1 | 1 |
| $\boldsymbol{M}_4$ | 1 | 0 | 0 | 0 | 1 |

lists the outcome of measuring $\boldsymbol{M}_{1,2,3,4}$ in the event of a bit flip. (For example, if the first bit flips, the measurement outcomes $\boldsymbol{M}_1 = \boldsymbol{M}_2 = \boldsymbol{M}_3 = 1, \boldsymbol{M}_4 = -1$, diagnose the error.) Similarly, the right half of $\tilde{H}$ can be regarded as the syndrome table for the phase errors.

| | $\boldsymbol{Z}_1$ | $\boldsymbol{Z}_2$ | $\boldsymbol{Z}_3$ | $\boldsymbol{Z}_4$ | $\boldsymbol{Z}_5$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $\boldsymbol{M}_1$ | 1 | 0 | 0 | 1 | 0 |
| $\boldsymbol{M}_2$ | 0 | 1 | 0 | 0 | 1 |
| $\boldsymbol{M}_3$ | 1 | 0 | 1 | 0 | 0 |
| $\boldsymbol{M}_4$ | 0 | 1 | 0 | 1 | 0 |

Since $\boldsymbol{Y}$ anti-commutes with both $\boldsymbol{X}$ and $\boldsymbol{Z}$, we obtain the syndrome for the error $\boldsymbol{Y}_i$ by summing the $i$th columns of the $\boldsymbol{X}$ and $\boldsymbol{Z}$ tables:

| | $\boldsymbol{Y}_1$ | $\boldsymbol{Y}_2$ | $\boldsymbol{Y}_3$ | $\boldsymbol{Y}_4$ | $\boldsymbol{Y}_5$ |
| :--- | :---: | :---: | :---: | :---: | :---: |
| $\boldsymbol{M}_1$ | 1 | 1 | 1 | 1 | 0 |
| $\boldsymbol{M}_2$ | 0 | 1 | 1 | 1 | 1 |
| $\boldsymbol{M}_3$ | 1 | 0 | 1 | 1 | 1 |
| $\boldsymbol{M}_4$ | 1 | 1 | 0 | 1 | 1 |

We find by inspection that the 15 columns of the $\boldsymbol{X}, \boldsymbol{Y}$, and $\boldsymbol{Z}$ syndrome tables are all distinct, and so we verify again that our code is a nondegenerate code that corrects one error. Indeed, the code is perfect — each of the 15 nontrivial binary strings of length 4 appears as a column in one of the tables.

Because of the cyclic property of the code, we can easily characterize all 15 nontrivial

<!-- Page 42 -->

elements of its stabilizer. Aside from $\boldsymbol{M}_1 = \boldsymbol{X}\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{X}\boldsymbol{I}$ and the four operators obtained from it by cyclic permutations of the qubit, the stabilizer also contains

$$
\boldsymbol{M}_3\boldsymbol{M}_4 = -\boldsymbol{Y}\boldsymbol{X}\boldsymbol{X}\boldsymbol{Y}\boldsymbol{I},
$$ {#eq-7.152}

plus its cyclic permutations, and

$$
\boldsymbol{M}_2\boldsymbol{M}_5 = -\boldsymbol{Z}\boldsymbol{Y}\boldsymbol{Y}\boldsymbol{Z}\boldsymbol{I},
$$ {#eq-7.153}

and its cyclic permutations. Evidently, all elements of the stabilizer are weight-4 Pauli operators.

For our logical operators, we may choose

$$
\begin{aligned}
\bar{\boldsymbol{Z}} &= \boldsymbol{Z}\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{Z}, \\
\bar{\boldsymbol{X}} &= \boldsymbol{X}\boldsymbol{X}\boldsymbol{X}\boldsymbol{X}\boldsymbol{X};
\end{aligned}
$$ {#eq-7.154}

these commute with $\boldsymbol{M}_{1,2,3,4}$, square to $\boldsymbol{I}$, and anti-commute with one another. Being weight 5, they are not themselves contained in the stabilizer. Therefore if we don’t mind destroying the encoded state, we can determine the value of $\bar{\boldsymbol{Z}}$ for the encoded qubit by measuring $\boldsymbol{Z}$ of each qubit and evaluating the parity of the outcomes. In fact, since the code is distance three, there are elements of $S^\perp \setminus S$ of weight-three; alternate expressions for $\bar{\boldsymbol{Z}}$ and $\bar{\boldsymbol{X}}$ can be obtained by multiplying by elements of the stabilizer. For example we can choose

$$
\bar{\boldsymbol{Z}} = (\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{Z}) \cdot (-\boldsymbol{Z}\boldsymbol{Y}\boldsymbol{Y}\boldsymbol{Z}\boldsymbol{I}) = -\boldsymbol{I}\boldsymbol{X}\boldsymbol{X}\boldsymbol{I}\boldsymbol{Z},
$$ {#eq-7.155}

(or one of its cyclic permutations), and

$$
\bar{\boldsymbol{X}} = (\boldsymbol{X}\boldsymbol{X}\boldsymbol{X}\boldsymbol{X}\boldsymbol{X}) \cdot (-\boldsymbol{Y}\boldsymbol{X}\boldsymbol{X}\boldsymbol{Y}\boldsymbol{I}) = -\boldsymbol{Z}\boldsymbol{I}\boldsymbol{I}\boldsymbol{Z}\boldsymbol{X},
$$ {#eq-7.156}

(or one of its cyclic permutations). So it is possible to ascertain the value of $\bar{\boldsymbol{X}}$ or $\bar{\boldsymbol{Z}}$ by measuring $\boldsymbol{X}$ or $\boldsymbol{Z}$ of only three of the five qubits in the block, and evaluating the parity of the outcomes.

If we wish, we can construct an orthonormal basis for the code subspace, as follows. Starting from any state $|\psi_0\rangle$, we can obtain

$$
|\Psi_0\rangle = \sum_{\boldsymbol{M} \in S} \boldsymbol{M}|\psi_0\rangle.
$$ {#eq-7.157}

This (unnormalized) state obeys $\boldsymbol{M}'|\Psi_0\rangle = |\Psi_0\rangle$ for each $\boldsymbol{M}' \in S$, since multiplication by an element of the stabilizer merely permutes the terms in the sum. To obtain the $\bar{\boldsymbol{Z}} = 1$ encoded state $|\bar{0}\rangle$, we may start with the state $|00000\rangle$, which is also a $\bar{\boldsymbol{Z}} = 1$ eigenstate, but not in the stabilizer; we find (up to normalization)

$$
\begin{aligned}
|\bar{0}\rangle &= \sum_{\boldsymbol{M} \in S} |00000\rangle \\
&= |00000\rangle + (\boldsymbol{M}_1 + \text{cyclic perms}) |00000\rangle \\
&\quad + (\boldsymbol{M}_3\boldsymbol{M}_4 + \text{cyclic perms}) |00000\rangle + (\boldsymbol{M}_2\boldsymbol{M}_5 + \text{cyclic perms}) |00000\rangle \\
&= |00000\rangle + (|10010\rangle + \text{cyclic perms}) \\
&\quad - (|11110\rangle + \text{cyclic perms}) \\
&\quad - (|01100\rangle + \text{cyclic perms}).
\end{aligned}
$$ {#eq-7.158}

<!-- Page 43 -->

We may then find $|\bar{1}\rangle$ by applying $\bar{\boldsymbol{X}}$ to $|\bar{0}\rangle$, that is by flipping all 5 qubits:

$$
\begin{aligned}
|\bar{1}\rangle = \bar{\boldsymbol{X}}|\bar{0}\rangle &= |11111\rangle + (|01101\rangle + \text{cyclic perms}) \\
&\quad - (|00001\rangle + \text{cyclic perms}) \\
&\quad - (|10011\rangle + \text{cyclic perms}).
\end{aligned}
$$ {#eq-7.159}

How is the syndrome measured? A circuit that can be executed to measure $\boldsymbol{M}_1 = \boldsymbol{X}\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{X}\boldsymbol{I}$ is:

– Figure –

The Hadamard rotations on the first and fourth qubits rotate $\boldsymbol{M}_1$ to the tensor product of $\boldsymbol{Z}$’s $\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{I}$, and the CNOT’s then imprint the value of this operator on the ancilla. The final Hadamard rotations return the encoded block to the standard code subspace. Circuits for measuring $\boldsymbol{M}_{2,3,4}$ are obtained from the above by cyclically permuting the five qubits in the code block.

What about encoding? We want to construct a unitary transformation

$$
\boldsymbol{U}_{\text{encode}} : |0000\rangle \otimes (a|0\rangle + b|1\rangle) \to a|\bar{0}\rangle + b|\bar{1}\rangle.
$$ {#eq-7.160}

We have already seen that $|00000\rangle$ is a $\bar{\boldsymbol{Z}} = 1$ eigenstate, and that $|00001\rangle$ is a $\bar{\boldsymbol{Z}} = -1$ eigenstate. Therefore (up to normalization)

$$
a|\bar{0}\rangle + b|\bar{1}\rangle = \left(\sum_{\boldsymbol{M} \in S} \boldsymbol{M}\right) |0000\rangle \otimes (a|0\rangle + b|1\rangle).
$$ {#eq-7.161}

So we need to figure out how to construct a circuit that applies $(\sum \boldsymbol{M})$ to an initial state.

Since the generators are independent, each element of the stabilizer can be expressed as a product of generators as a unique way, and we may therefore rewrite the sum as

$$
\sum_{\boldsymbol{M} \in S} \boldsymbol{M} = (\boldsymbol{I} + \boldsymbol{M}_4)(\boldsymbol{I} + \boldsymbol{M}_3)(\boldsymbol{I} + \boldsymbol{M}_2)(\boldsymbol{I} + \boldsymbol{M}_1).
$$ {#eq-7.162}

Now to proceed further it is convenient to express the stabilizer in an alternative form. Note that we have the freedom to replace the generator $\boldsymbol{M}_i$ by $\boldsymbol{M}_i\boldsymbol{M}_j$ without changing the stabilizer. This replacement is equivalent to adding the $j$th row to the $i$th row in the matrix $\tilde{H}$. With such row operations, we can perform a Gaussian elimination on the $4 \times 5$ matrix $H_X$, and so obtain the new presentation for the stabilizer

$$
\tilde{H}' = \left(\begin{array}{ccccc|ccccc}
1 & 1 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 \\
0 & 0 & 1 & 1 & 0 & 0 & 1 & 0 & 0 & 1 \\
1 & 1 & 0 & 0 & 0 & 0 & 0 & 1 & 0 & 1 \\
1 & 0 & 1 & 1 & 1 & 0 & 0 & 0 & 1 & 1
\end{array}\right),
$$ {#eq-7.163}

or

$$
\begin{aligned}
\boldsymbol{M}_1 &= \boldsymbol{Y}\boldsymbol{Z}\boldsymbol{I}\boldsymbol{Z}\boldsymbol{Y}, \\
\boldsymbol{M}_2 &= \boldsymbol{I}\boldsymbol{X}\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{X}, \\
\boldsymbol{M}_3 &= \boldsymbol{Z}\boldsymbol{Z}\boldsymbol{X}\boldsymbol{I}\boldsymbol{X}, \\
\boldsymbol{M}_4 &= \boldsymbol{Z}\boldsymbol{I}\boldsymbol{Z}\boldsymbol{Y}\boldsymbol{Y}.
\end{aligned}
$$ {#eq-7.164}

<!-- Page 44 -->

In this form $\boldsymbol{M}_i$ applies an $\boldsymbol{X}$ (flip) only to qubits $i$ and 5 in the block.

Adopting this form for the stabilizer, we can apply $\frac{1}{\sqrt{2}}(\boldsymbol{I} + \boldsymbol{M}_1)$ to a state $|0, z_2, z_3, z_4, z_5\rangle$ by executing the circuit

– Figure –

The Hadamard prepares $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$. If the first qubit is $|0\rangle$, the other operations don’t do anything, so $\boldsymbol{I}$ is applied. But if the first qubit is $|1\rangle$, then $\boldsymbol{X}$ has been applied to this qubit, and the other gates in the circuit apply $\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{I}\boldsymbol{Z}\boldsymbol{Y}$, conditioned on the first qubit being $|1\rangle$. Hence, $\boldsymbol{Y}\boldsymbol{Z}\boldsymbol{I}\boldsymbol{Z}\boldsymbol{Y} = \boldsymbol{M}_1$ has been applied. Similar circuits can be constructed that apply $\frac{1}{\sqrt{2}}(\boldsymbol{I} + \boldsymbol{M}_2)$ to $|z_1, 0, z_3, z_4, z_5\rangle$, and so forth. Apart from the Hadamard gates each of these circuits applies only $\boldsymbol{Z}$’s and conditional $\boldsymbol{Z}$’s to qubits 1 through 4; these qubits never flip. (It was to ensure thus that we performed the Gaussian elimination on $H_X$.) Therefore, we can construct our encoding circuit as

– Figure –

Furthermore, each $\boldsymbol{Z}$ gate acting on $|0\rangle$ can be replaced by the identity, so we may simplify the circuit by eliminating all such gates, obtaining

– Figure –

This procedure can be generalized to construct an encoding circuit for any stabilizer code.

Since the encoding transformation is unitary, we can use its adjoint to decode. And since each gate squares to $\pm\boldsymbol{I}$, the decoding circuit is just the encoding circuit run in reverse.
