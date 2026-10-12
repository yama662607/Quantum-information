# Section 7.13: Some Other Stabilizer Codes

**Source:** Preskill Lecture Notes, Chapter 7, pp. 40–42 (Physical pages 46–48).

---

### 7.13.1 The $[[6, 0, 4]]$ code

A $k = 0$ quantum code has a one-dimensional code subspace; that is, there is only one encoded state. The code cannot be used to store unknown quantum information, but even so, $k = 0$ codes can have interesting properties. Since they can detect and diagnose errors, they might be useful for a study of the correlations in decoherence induced by interactions with the environment.

If $k = 0$, then $S$ and $S^\perp$ coincide — a Pauli operator that commutes with all elements of the stabilizer must lie in the stabilizer. In this case, the distance $d$ is defined as the minimum weight of any Pauli operator in the stabilizer. Thus a distance-$d$ code can "detect $d - 1$ errors;" that is, if any Pauli operator of weight less than $d$ acts on the code state, the result is orthogonal to that state.

Associated with the $[[5, 1, 3]]$ code is a $[[6, 0, 4]]$ code, whose encoded state can be expressed as
$$
|0\rangle \otimes |\bar{0}\rangle + |1\rangle \otimes |\bar{1}\rangle ,
$$ {#eq-7.171}
where $|\bar{0}\rangle$ and $|\bar{1}\rangle$ are the $\bar{Z}$ eigenstates of the $[[5, 1, 3]]$ code. You can verify that this code has distance $d = 4$ (an exercise).

The $[[6, 0, 4]]$ code is interesting because its code state is maximally entangled. We may choose any three qubits from among the six. The density matrix $\rho^{(3)}$ of those three, obtained by tracing over the other three, is totally random, $\rho^{(3)} = \frac{1}{8}\mathbf{I}$. In this sense, the $[[6, 0, 4]]$ state is a natural multiparticle analog of the two-qubit Bell states. It is far "more entangled" than the six-qubit cat state $\frac{1}{\sqrt{2}}(|000000\rangle + |111111\rangle)$. If we measure any one of the six qubits in the cat state, in the $\{|0\rangle, |1\rangle\}$ basis, we know everything about the state we have prepared of the remaining five qubits. But we may measure any observable we please acting on any three qubits in the $[[6, 0, 4]]$ state, and we learn nothing about the remaining three qubits, which are still described by $\rho^{(3)} = \frac{1}{8}\mathbf{I}$.

Our $[[6, 0, 4]]$ state is all the more interesting in that it turns out (but is not so simple to prove) that its generalizations to more qubits do not exist. That is, there are no $[[2n, 0, n + 1]]$ binary quantum codes for $n > 3$. You'll see in the exercises, though, that there are other, nonbinary, maximally entangled states that can be constructed.

### 7.13.2 The $[[2m, 2m - 2, 2]]$ error-detecting codes

The Bell state $|\phi^+\rangle = \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$ is a $[[2, 0, 2]]$ code with stabilizer generators
$$
\begin{aligned}
&ZZ , \\
&XX .
\end{aligned}
$$ {#eq-7.172}
The code has distance two because no weight-one Pauli operator commutes with both generators (none of $X, Y, Z$ commute with both $X$ and $Z$). Correspondingly, a bit flip ($X$) or a phase flip ($Z$), or both ($Y$) acting on either qubit in $|\phi^+\rangle$, takes it to an orthogonal state (one of the other Bell states $|\phi^-\rangle, |\psi^+\rangle, |\psi^-\rangle$).

One way to generalize the Bell states to more qubits is to consider the $n = 4, k = 2$ code with stabilizer generators
$$
\begin{aligned}
&ZZZZ , \\
&XXXX .
\end{aligned}
$$ {#eq-7.173}
This is a distance $d = 2$ code for the same reason as before. The code subspace is spanned by states of even parity ($ZZZZ$) that are invariant under a simultaneous flip of all four qubits ($XXXX$). A basis is:
$$
\begin{aligned}
&|0000\rangle + |1111\rangle , \\
&|0011\rangle + |1100\rangle , \\
&|0101\rangle + |1010\rangle , \\
&|0110\rangle + |1001\rangle .
\end{aligned}
$$ {#eq-7.174}
Evidently, an $X$ or a $Z$ acting on any qubit takes each of these states to a state orthogonal to the code subspace; thus any single-qubit error can be detected.

A further generalization is the $[[2m, 2m - 2, 2]]$ code with stabilizer generators
$$
\begin{aligned}
&ZZ \dots Z , \\
&XX \dots X ,
\end{aligned}
$$ {#eq-7.175}
(the length is required to be even so that the generators will commute). The code subspace is spanned by our familiar friends the $2^{n-2}$ cat states
$$
\frac{1}{\sqrt{2}}(|x\rangle + |\neg x\rangle) ,
$$ {#eq-7.176}
where $x$ is an even-weight string of length $n = 2m$.

### 7.13.3 The $[[8, 3, 3]]$ code

As already noted in our discussion of the $[[5, 1, 3]]$ code, a stabilizer code with generators
$$
\tilde{H} = (H_Z | H_X) ,
$$ {#eq-7.177}
can correct one error if: (1) the columns of $\tilde{H}$ are distinct (a distinct syndrome for each $X$ and $Z$ error) and (2) each sum of a column of $H_Z$ with the corresponding column of $H_X$ is distinct from each column of $\tilde{H}$ and distinct from all other such sums (each $Y$ error can be distinguished from all other one-qubit errors).

We can readily construct a $5 \times 16$ matrix $\tilde{H}$ with this property, and so derive the stabilizer of an $[[8, 3, 3]]$ code; we choose
$$
\tilde{H} = \begin{pmatrix}
H & H^\sigma \\
11111111 & 00000000 \\
00000000 & 11111111
\end{pmatrix} .
$$ {#eq-7.178}
Here $H$ is the $3 \times 8$ matrix
$$
H = \begin{pmatrix}
1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 \\
0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1 & 0
\end{pmatrix}
$$ {#eq-7.179}
whose columns are all the distinct binary strings of length 3, and $H^\sigma$ is obtained from $H$ by performing a suitable permutation of the columns. This permutation is chosen so that the eight sums of columns of $H$ with corresponding columns of $H^\sigma$ are all distinct. We may see by inspection that a suitable choice is
$$
H^\sigma = \begin{pmatrix}
0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 \\
1 & 1 & 0 & 0 & 1 & 1 & 0 & 0
\end{pmatrix}
$$ {#eq-7.180}
as the column sums are then
$$
\begin{pmatrix}
1 & 1 & 0 & 0 & 1 & 1 & 0 & 0 \\
0 & 1 & 1 & 1 & 1 & 0 & 0 & 0 \\
1 & 1 & 0 & 1 & 0 & 0 & 1 & 0
\end{pmatrix} .
$$ {#eq-7.181}
The last two rows of $\tilde{H}$ serve to distinguish each $X$ syndrome from each $Y$ syndrome or $Z$ syndrome, and the above mentioned property of $H^\sigma$ ensures that all $Y$ syndromes are distinct. Therefore, we have constructed a length-8 code with $k = 8 - 5 = 3$ that can correct one error. It is actually the simplest in an infinite class of $[[2^m, 2^m - m - 2, 3]]$ codes constructed by Gottesman, with $m \ge 3$.

The $[[8, 3, 3]]$ quantum code that we have just described is a close cousin of the "extended Hamming code," the self-dual $[8, 4, 4]$ classical code that is obtained from the $[7, 3, 4]$ dual of the Hamming code by adding an extra parity bit. Its parity check matrix (which is also its generator matrix) is
$$
H_{\mathrm{EH}} = \begin{pmatrix}
1 & 0 & 1 & 0 & 1 & 0 & 1 & 0 \\
0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 \\
0 & 0 & 0 & 1 & 1 & 1 & 1 & 0 \\
1 & 1 & 1 & 1 & 1 & 1 & 1 & 1
\end{pmatrix} .
$$ {#eq-7.182}
This matrix $H_{\mathrm{EH}}$ has the property that, not only are its eight columns distinct, but also each sum of two columns is distinct from all columns; since the sum of two columns has 0, not 1, as its fourth bit.
