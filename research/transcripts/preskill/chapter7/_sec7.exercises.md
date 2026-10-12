# Exercises Transcript: Chapter 7 Quantum Error Correction

**Source:** John Preskill, *Quantum Information and Computation* (Physics 219 / Computer Science 219), Chapter 7: Quantum Error Correction, pp. 80–86 (Physical pp. 86–92).

---

## Exercises

### 7.1 Phase error-correcting code
a) Construct stabilizer generators for an $n = 3, k = 1$ code that can correct a single bit flip; that is, ensure that recovery is possible for any of the errors in the set $\mathcal{E} = \{\boldsymbol{III}, \boldsymbol{XII}, \boldsymbol{IXI}, \boldsymbol{IIX}\}$. Find an orthonormal basis for the two-dimensional code subspace.
b) Construct stabilizer generators for an $n = 3, k = 1$ code that can correct a single phase error; that is, ensure that recovery is possible for any of the errors in the set $\mathcal{E} = \{\boldsymbol{III}, \boldsymbol{ZII}, \boldsymbol{IZI}, \boldsymbol{IIZ}\}$. Find an orthonormal basis for the two-dimensional code subspace.

### 7.2 Error-detecting codes
a) Construct stabilizer generators for an $[[n, k, d]] = [[3, 0, 2]]$ quantum code. With this code, we can detect any single-qubit error. Find the encoded state. (Does it look familiar?)
b) Two QECC's $C_1$ and $C_2$ (with the same length $n$) are *equivalent* if a permutation of qubits, combined with single-qubit unitary transformations, transforms the code subspace of $C_1$ to that of $C_2$. Are all $[[3, 0, 2]]$ stabilizer codes equivalent?
c) Does a $[[3, 1, 2]]$ stabilizer code exist?

### 7.3 Maximal entanglement
Consider the $[[5, 1, 3]]$ quantum code, whose stabilizer generators are $M_1 = \boldsymbol{XZZXI}$, and $M_{2,3,4}$ obtained by cyclic permutations of $M_1$, and choose the encoded operation $\bar{\boldsymbol{Z}}$ to be $\bar{\boldsymbol{Z}} = \boldsymbol{ZZZZZ}$. From the encoded states $|\bar{0}\rangle$ with $\bar{\boldsymbol{Z}}|\bar{0}\rangle = |\bar{0}\rangle$ and $|\bar{1}\rangle$ with $\bar{\boldsymbol{Z}}|\bar{1}\rangle = -|\bar{1}\rangle$, construct the $n = 6, k = 0$ code whose encoded state is
$$
\frac{1}{\sqrt{2}} (|0\rangle \otimes |\bar{0}\rangle + |1\rangle \otimes |\bar{1}\rangle) . \tag{7.314}
$$
a) Construct a set of stabilizer generators for this $n = 6, k = 0$ code.
b) Find the distance of this code. (Recall that for a $k = 0$ code, the distance is defined as the minimum weight of any element of the stabilizer.)
c) Find $\boldsymbol{\rho}^{(3)}$, the density matrix that is obtained if three qubits are selected and the remaining three are traced out.

### 7.4 Codewords and nonlocality
For the $[[5, 1, 3]]$ code with stabilizer generators and logical operators as in the preceding problem,
a) Express $\bar{\boldsymbol{Z}}$ as a weight-3 Pauli operator, a tensor product of $\boldsymbol{I}$'s, $\boldsymbol{X}$'s, and $\boldsymbol{Z}$'s (no $\boldsymbol{Y}$'s). Note that because the code is cyclic, all cyclic permutations of your expression are equivalent ways to represent $\bar{\boldsymbol{Z}}$.
b) Use the Einstein locality assumption (local hidden variables) to predict a relation between the five (cyclically related) observables found in (a) and the observable $\boldsymbol{ZZZZZ}$. Is this relation among observables satisfied for the state $|\bar{0}\rangle$?
c) What would Einstein say?

### 7.5 Generalized Shor code
For integer $m \ge 2$, consider the $n = m^2, k = 1$ generalization of Shor's nine-qubit code, with code subspace spanned by the two states:
$$
\begin{aligned}
|\bar{0}\rangle &= (|000\dots 0\rangle + |111\dots 1\rangle)^{\otimes m} , \\
|\bar{1}\rangle &= (|000\dots 0\rangle - |111\dots 1\rangle)^{\otimes m} .
\end{aligned} \tag{7.315}
$$
a) Construct stabilizer generators for this code, and construct the logical operations $\bar{\boldsymbol{Z}}$ and $\bar{\boldsymbol{X}}$ such that
$$
\begin{aligned}
\bar{\boldsymbol{Z}}|\bar{0}\rangle &= |\bar{0}\rangle , & \bar{\boldsymbol{X}}|\bar{0}\rangle &= |\bar{1}\rangle , \\
\bar{\boldsymbol{Z}}|\bar{1}\rangle &= -|\bar{1}\rangle , & \bar{\boldsymbol{X}}|\bar{1}\rangle &= |\bar{0}\rangle .
\end{aligned} \tag{7.316}
$$
b) What is the distance of this code?
c) Suppose that $m$ is odd, and suppose that each of the $n = m^2$ qubits is subjected to the depolarizing channel with error probability $p$. How well does this code protect the encoded qubit? Specifically, (i) estimate the probability, to leading nontrivial order in $p$, of a logical bit-flip error $|\bar{0}\rangle \leftrightarrow |\bar{1}\rangle$, and (ii) estimate the probability, to leading nontrivial order in $p$, of a logical phase error $|\bar{0}\rangle \to |\bar{0}\rangle, |\bar{1}\rangle \to -|\bar{1}\rangle$.
d) Consider the asymptotic behavior of your answer to (c) for $m$ large. What condition on $p$ should be satisfied for the code to provide good protection against (i) bit flips and (ii) phase errors, in the $n \to \infty$ limit?

### 7.6 Encoding circuits
For an $[[n, k, d]]$ quantum code, an encoding transformation is a unitary $\boldsymbol{U}$ that acts as
$$
\boldsymbol{U} : |\psi\rangle \otimes |0\rangle^{\otimes (n-k)} \to |\bar{\psi}\rangle , \tag{7.317}
$$
where $|\psi\rangle$ is an arbitrary $k$-qubit state, and $|\bar{\psi}\rangle$ is the corresponding encoded state. Design a quantum circuit that implements the encoding transformation for
a) Shor's $[[9, 1, 3]]$ code.
b) Steane's $[[7, 1, 3]]$ code.

### 7.7 Shortening a quantum code
a) Consider a binary $[[n, k, d]]$ stabilizer code. Show that it is possible to choose the $n - k$ stabilizer generators so that at most two act nontrivially on the last qubit. (That is, the remaining $n - k - 2$ generators apply $\boldsymbol{I}$ to the last qubit.)
b) These $n - k - 2$ stabilizer generators that apply $\boldsymbol{I}$ to the last qubit will still commute and are still independent if we drop the last qubit. Hence they are the generators for a code with length $n - 1$ and $k + 1$ encoded qubits. Show that if the original code is nondegenerate, then the distance of the shortened code is at least $d - 1$. (Hint: First show that if there is a weight-$t$ element of the $(n - 1)$-qubit Pauli group that commutes with the stabilizer of the shortened code, then there is an element of the $n$-qubit Pauli group of weight at most $t + 1$ that commutes with the stabilizer of the original code.)
c) Apply the code-shortening procedure of (a) and (b) to the $[[5, 1, 3]]$ QECC. Do you recognize the code that results? (Hint: It may be helpful to exploit the freedom to perform a change of basis on some of the qubits.)

### 7.8 Codes for qudits
A *qudit* is a $d$-dimensional quantum system. The Pauli operators $\boldsymbol{I}, \boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z}$ acting on qubits can be generalized to qudits as follows. Let $\{|0\rangle, |1\rangle, \dots, |d - 1\rangle\}$ denote an orthonormal basis for the Hilbert space of a single qudit. Define the operators:
$$
\begin{aligned}
\boldsymbol{X} &: |j\rangle \to |j + 1 \pmod d\rangle , \\
\boldsymbol{Z} &: |j\rangle \to \omega^j |j\rangle ,
\end{aligned} \tag{7.318}
$$
where $\omega = \exp(2\pi i/d)$. Then the $d \times d$ Pauli operators $\boldsymbol{E}_{r,s}$ are
$$
\boldsymbol{E}_{r,s} \equiv \boldsymbol{X}^r \boldsymbol{Z}^s , \quad r, s = 0, 1, \dots, d - 1 \tag{7.319}
$$
a) Are the $\boldsymbol{E}_{r,s}$'s a basis for the space of operators acting on a qudit? Are they unitary? Evaluate $\operatorname{tr}(\boldsymbol{E}_{r,s}^\dagger \boldsymbol{E}_{t,u})$.
b) The Pauli operators obey
$$
\boldsymbol{E}_{r,s}\boldsymbol{E}_{t,u} = (\eta_{r,s;t,u})\boldsymbol{E}_{t,u}\boldsymbol{E}_{r,s} , \tag{7.320}
$$
where $\eta_{r,s;t,u}$ is a phase. Evaluate this phase.
The $n$-fold tensor products of these qudit Pauli operators form a group $G_n^{(d)}$ of order $d^{2n+1}$ (and if we mod out its $d$-element center, we obtain the group $\bar{G}_n^{(d)}$ of order $d^{2n}$). To construct a stabilizer code for qudits, we choose an abelian subgroup of $G_n^{(d)}$ with $n - k$ generators; the code is the simultaneous eigenstate with eigenvalue one of these generators. If $d$ is prime, then the code subspace has dimension $d^k$: $k$ logical qudits are encoded in a block of $n$ qudits.
c) Explain how the dimension might be different if $d$ is not prime. (Hint: Consider the case $d = 4$ and $n = 1$.)

### 7.9 Syndrome measurement for qudits
Errors on qudits are diagnosed by measuring the stabilizer generators. For this purpose, we may invoke the two-qudit gate SUM (which generalizes the controlled-NOT), acting as
$$
\mathrm{SUM} : |j\rangle \otimes |k\rangle \to |j\rangle \otimes |k + j \pmod d\rangle . \tag{7.321}
$$
a) Describe a quantum circuit containing SUM gates that can be executed to measure an $n$-qudit observable of the form
$$
\bigotimes_a \boldsymbol{Z}_a^{s_a} . \tag{7.322}
$$
If $d$ is prime, then for each $r, s = 0, 1, 2, \dots, d - 1$, there is a single-qudit unitary operator $\boldsymbol{U}_{r,s}$ such that
$$
\boldsymbol{U}_{r,s}\boldsymbol{E}_{r,s}\boldsymbol{U}_{r,s}^\dagger = \boldsymbol{Z} . \tag{7.323}
$$
b) Describe a quantum circuit containing SUM gates and $\boldsymbol{U}_{r,s}$ gates that can be executed to measure an arbitrary element of $G_n^{(d)}$ of the form
$$
\bigotimes_a \boldsymbol{E}_{r_a, s_a} . \tag{7.324}
$$

### 7.10 Error-detecting codes for qudits
A qudit with $d = 3$ is called a *qutrit*. Consider a qutrit stabilizer code with length $n = 3$ and $k = 1$ encoded qutrit defined by the two stabilizer generators
$$
\boldsymbol{ZZZ} , \quad \boldsymbol{XXX} . \tag{7.325}
$$
a) Do the generators commute?
b) Find the distance of this code.
c) In terms of the orthonormal basis $\{|0\rangle, |1\rangle, |2\rangle\}$ for the qutrit, write out explicitly an orthonormal basis for the three-dimensional code subspace.
d) Construct the stabilizer generators for an $n = 3m$ qutrit code (where $m$ is any positive integer), with $k = n - 2$, that can detect one error.
e) Construct the stabilizer generators for a qudit code that detects one error, with parameters $n = d, k = d - 2$.

### 7.11 Error-correcting code for qudits
Consider an $n = 5, k = 1$ qudit stabilizer code with stabilizer generators
$$
\begin{array}{lllll}
\boldsymbol{X} & \boldsymbol{Z} & \boldsymbol{Z}^{-1} & \boldsymbol{X}^{-1} & \boldsymbol{I} \\
\boldsymbol{I} & \boldsymbol{X} & \boldsymbol{Z} & \boldsymbol{Z}^{-1} & \boldsymbol{X}^{-1} \\
\boldsymbol{X}^{-1} & \boldsymbol{I} & \boldsymbol{X} & \boldsymbol{Z} & \boldsymbol{Z}^{-1} \\
\boldsymbol{Z}^{-1} & \boldsymbol{X}^{-1} & \boldsymbol{I} & \boldsymbol{X} & \boldsymbol{Z}
\end{array} \tag{7.326}
$$
(the second, third, and fourth generators are obtained from the first by a cyclic permutation of the qudits).
a) Find the order of each generator. Are the generators really independent? Do they commute? Is the fifth cyclic permutation $\boldsymbol{Z} \boldsymbol{Z}^{-1} \boldsymbol{X}^{-1} \boldsymbol{I} \boldsymbol{X}$ independent of the rest?
b) Find the distance of this code. Is the code nondegenerate?
c) Construct the encoded operations $\bar{\boldsymbol{X}}$ and $\bar{\boldsymbol{Z}}$, each expressed as an operator of weight 3. (Be sure to check that these operators obey the right commutation relations for any value of $d$.)

### 7.12 Good CSS codes
In §7.16 we derived the *quantum Gilbert-Varshamov bound*:
$$
|\mathcal{E}^{(2)}| - 1 < 2^{n-k} \left(\frac{1 - 2^{-2n}}{1 - 2^{-2k}}\right) . \tag{7.327}
$$
This is a sufficient condition for the existence of a (possibly degenerate) binary stabilizer code that can correct all Pauli operators in a set $\mathcal{E}$; here $|\mathcal{E}^{(2)}|$ denotes the number of distinct Pauli operators of the form $\boldsymbol{E}_a^\dagger \boldsymbol{E}_b$, where $\boldsymbol{E}_a, \boldsymbol{E}_b \in \mathcal{E}$. One consequence of this bound is that there exist "good" $[[n, k, d = 2t + 1]]$ stabilizer codes that achieve an asymptotic rate $R = k/n = 1 - H_2(2t/n) - (2t/n) \log_2 3$.

The purpose of this exercise is to show that good Calderbank-Shor-Steane (CSS) codes exist.
a) Derive a quantum Gilbert-Varshamov bound for CSS codes. Denote by $\mathcal{E}^X$ the set of $X$-type errors that the code can correct (those that can be expressed as a tensor product of $X$'s and $I$'s) and denote by $\mathcal{E}^Z$ the set of $Z$-type errors that the code can correct (those that can be expressed as a tensor product of $Z$'s and $I$'s). Denote by $\mathcal{E}^{X(2)}$ the set of $\{\boldsymbol{E}_a^\dagger \boldsymbol{E}_b\}$ where $\boldsymbol{E}_a, \boldsymbol{E}_b \in \mathcal{E}^X$, and similarly for $\mathcal{E}^{Z(2)}$. The quantum Gilbert-Varshamov bound for CSS codes is a sufficient condition for the existence of a CSS code with $n_X$ stabilizer generators of the $X$ type and $n_Z$ stabilizer generators of the $Z$ type that can correct all errors in $\mathcal{E}^X$ and $\mathcal{E}^Z$, expressed as an inequality involving $n_X, n_Z, |\mathcal{E}^{X(2)}|$ and $|\mathcal{E}^{Z(2)}|$.
b) Use the quantum Gilbert-Varshamov bound for CSS codes to show the existence of CSS codes that achieve the asymptotic rate $R = k/n = 1 - H_2(2t_X/n) - H_2(2t_Z/n)$, where the code can correct $t_X$ $X$ errors and $t_Z$ $Z$ errors.

### 7.13 A cleaning lemma for CSS codes
In §7.14 we proved the *cleaning lemma* for stabilizer codes, which says the following: For an $[[n, k]]$ stabilizer code, let $M$ denote a subset of the $n$ qubits in the code block, and let $M^c$ denote the complementary set of qubits. If $x$ is one of the code's logical Pauli operators, we say that $x$ can be *cleaned* on $M$ if there is a logically equivalent Pauli operator $x' = xy$ (where $y$ is an element of the code stabilizer $S$) such that $x'$ acts nontrivially only on $M^c$:
$$
x' = \boldsymbol{I}_M \otimes \boldsymbol{Q}_{M^c} . \tag{7.328}
$$
We say that $x$ can be *supported* on $M$ if it can be cleaned on $M^c$. Let $g(M)$ denote the number of independent logical Pauli operators that can be supported on $M$ and let $g(M^c)$ denote the number of independent Pauli operators that can be supported on $M^c$. Then the cleaning lemma asserts that
$$
g(M) + g(M^c) = 2k . \tag{7.329}
$$
In particular, therefore, if no logical operator can be supported on $M$, then the complete $k$-qubit logical Pauli group can be supported on its complement.

Now consider the case of an $[[n, k]]$ CSS stabilizer code, where all generators of the code stabilizer can be chosen to be either of the $X$ type (a tensor product of $X$'s and $I$'s) or the $Z$ type (a tensor product of $Z$'s and $I$'s); furthermore, the generators of the logical Pauli group can also be chosen to be either $X$ type or $Z$ type. Let $g^X(M)$ denote the number of independent $X$-type logical Pauli operators supported on $M$, and let $g^Z(M^c)$ denote the number of independent $Z$-type logical Pauli operators supported on $M^c$. Show that
$$
g^X(M) + g^Z(M^c) = k . \tag{7.330}
$$
It follows that if no $X$-type logical Pauli operators can be supported on $M$, then all $Z$-type logical operators can be supported on its complement.

### 7.14 Bound on $D$-dimensional codes
In class (and in the notes) we proved a bound on $[[n, k, d]]$ for local stabilizer codes in 2 dimensions: $kd^2 = O(n)$, where $k$ is the number of encoded qubits, $d$ is the code distance, and $n$ is the code length.

Using similar reasoning, derive a bound on $D$-dimensional stabilizer codes of the form $kd^\alpha = O(n)$. Express $\alpha$ in terms of $D$.

### 7.15 Price of a code
The distance $d$ of a stabilizer code is the size of the smallest set of qubits in the code block that supports a nontrivial logical operator. In contrast, the *price* $p$ of a code is defined as the size of the smallest set of qubits that supports *all* of the code's logical operators. Evidently $p \ge d$.
a) What is the price of the $[[7, 1, 3]]$ quantum code?
b) Use the cleaning lemma to show that $p \le n - d + 1$.
c) Show that $p \ge k + d - 1$. (Hint: Use this result proved in class (and in the notes): Suppose that the code block can be divided into three parts $ABC$ such that $A$ and $B$ are both correctable. Then $k \le |C|$, where $|C|$ is the number of qubits in $C$.)
d) For an $[[n, k, d]]$ stabilizer code, prove the *quantum Singleton bound*: $n - k \ge 2(d - 1)$.

### 7.16 Price of a local code
Using the holographic principle and the union lemma (described in class and in the notes), derive a bound on the price $p$ of a $D$-dimensional stabilizer code of the form $pd^\beta = O(n)$. Express $\beta$ in terms of $D$.

### 7.17 Higher-dimensional toric codes
To understand the logical operators of the 2D toric code, we found it convenient to use the concept of a *chain complex*. We defined vector spaces $V_0, V_1, V_2$ over $\mathbb{F}_2$ and boundary operators $\partial_1, \partial_2$ such that
$$
V_2 \xrightarrow{\partial_2} V_1 \xrightarrow{\partial_1} V_0 \tag{7.331}
$$
and
$$
\partial_1 \circ \partial_2 = 0 . \tag{7.332}
$$
For example, for the purpose of formulating the $Z$-type logical operators of the toric code, vectors in $V_2$ are *2-chains*, which assign a bit to each lattice plaquette, vectors in $V_1$ are *1-chains*, which assign a bit to each edge, and vectors in $V_0$ are *0-chains*, which assign a bit to each site. We saw that a 2-chain $\omega$ may be interpreted as a stabilizer element (a product of $Z$-type plaquette operators), a 1-chain $\epsilon$ may be interpreted as a $Z$-type error operator, and the 0-chain $\sigma = \partial_1 \epsilon$ may be interpreted as the syndrome of $\epsilon$ (determined by measuring the $X$-type site operators). The property $\partial_1 \circ \partial_2 = 0$ expresses that a $Z$-type stabilizer operator has a trivial syndrome.

A $Z$-type operator which lies in the code stabilizer $S$ is the boundary $\partial_2 \omega$ of some 2-chain $\omega$; it is contained in the image of $\partial_2$. A $Z$-type operator $\epsilon$ which lies in the normalizer $S^\perp$ (commutes with the stabilizer) is a *1-cycle* with trivial boundary, $\partial_1 \epsilon = 0$; it is contained in the kernel of $\partial_1$. Thus the code's $Z$-type logical Pauli operators are elements of the coset space $\operatorname{Ker}(\partial_1)/\operatorname{Im}(\partial_2)$.

We have also seen how this chain-complex language can be applied to any CSS stabilizer code. In this problem, we'll apply it to toric codes in more than 2 dimensions.

Consider a 3D version of the toric code defined on an $L \times L \times L$ cubic lattice with periodic boundary conditions. Qubits reside on lattice links. There is a weight-4 $Z$-type stabilizer generator associated with each lattice plaquette, and a weight-6 $X$-type stabilizer generator associated with each lattice site.
a) Construct a chain complex suited for describing the $Z$-type logical operators of this code, and find the logical operators. How many encoded qubits are there? What is the minimal weight $d_Z$ of a $Z$-type logical operator?
b) Construct a chain complex suited for describing the $X$-type logical operators of this code, and find the logical operators. Check that these $X$-type logical operators have the expected commutation relations with the $Z$-type logical operators. What is the minimal weight $d_X$ of an $X$-type logical operator?

Consider a 4D version of the toric code defined on an $L \times L \times L \times L$ hypercubic lattice with periodic boundary conditions. Qubits reside on lattice plaquettes. There is a weight-6 $Z$-type stabilizer generator associated with each lattice cube, and a weight-6 $X$-type stabilizer generator associated with each lattice link.
c) Construct a chain complex suited for describing the $Z$-type logical operators of this code, and find the logical operators. How many encoded qubits are there? What is the minimal weight $d_Z$ of a $Z$-type logical operator?
d) Construct a chain complex suited for describing the $X$-type logical operators of this code, and find the logical operators. Check that these $X$-type logical operators have the expected commutation relations with the $Z$-type logical operators. What is the minimal weight $d_X$ of an $X$-type logical operator?
