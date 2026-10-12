# Section 8.4: Anyon Models Generalized: R-Matrix, F-Matrix, B-Matrix, and Quantum Circuit Simulation [PDF Pages 43-50]

<!-- ============================================================ -->
<!-- Source: chap8.pdf, Physical Pages: 43-50                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 43 -->
– Figure: Diagrammatic representations of orthogonality $\langle ab; c', \mu' | ab; c, \mu\rangle = \delta_c^{c'} \delta_\mu^{\mu'}$ and completeness $\sum_{c, \mu} |ab; c, \mu\rangle \langle ab; c, \mu| = I_{ab}$ (bubble diagrams) –

There are some natural isomorphisms among fusion spaces. First of all, $V_{ab}^c \cong V_{ba}^c$; these vector spaces are associated with different labelings of the two particles (if $a \neq b$) and so should be regarded as distinct, but they are isomorphic spaces because fusion is symmetric. We may also "raise and lower indices" of a fusion space by replacing a label by its conjugate, e.g.,

$$
V_{ab}^c \cong V_{a\bar{c}}^{\bar{b}} \cong V_{ab\bar{c}}^1 \cong V_a^{\bar{b}c} \cong V_{\bar{c}}^{\bar{a}\bar{b}} \cong \cdots;
$$ {#eq-8.70}

in the diagrammatic notation, we have the freedom to reverse the sense of a line while conjugating the line's label. The space $V_{ab\bar{c}}^1$, represented as a diagram with three incoming lines, is the space spanned by the distinguishable ways to obtain the trivial total charge $1$ when fusing three particles with labels $a, b, \bar{c}$.

The charge $1$ deserves its name because it fuses trivially with other particles:

$$
a \times 1 = a.
$$ {#eq-8.71}

Because of the isomorphism $V_{a1}^a \cong V_{a\bar{a}}^1$, we conclude that $\bar{a}$ is the unique label that can fuse with $a$ to yield $1$, and that this fusion can occur in only one way. Similarly, $V_{a1}^a \cong V_1^{a\bar{a}}$ means that pairs of particles created out of the vacuum have conjugate charges.

An anyon model is *nonabelian* if

$$
\dim\left(\bigoplus_c V_{ab}^c\right) = \sum_c N_{ab}^c \ge 2
$$ {#eq-8.72}

for at least some pair of labels $ab$; otherwise the model is *abelian*. In an abelian model, any two particles fuse in a unique way, but in a nonabelian model, there are some pairs of particles that can fuse in more than one way, and there is a Hilbert space of two or more dimensions spanned by these distinguishable states. We will refer to this space as the "topological

<!-- Page 44 -->
Hilbert space" of the pair of anyons, to emphasize that this quantum information is encoded nonlocally --- it is a collective property of the pair, not localized on either particle. Indeed, when the two particles with labels $a$ and $b$ are far apart, different states in the topological Hilbert space look identical locally. Therefore, this quantum information is well hidden, and invulnerable to decoherence due to local interactions with the environment.

It is for this reason that we propose to use nonabelian anyons in the operation of a quantum computer. Of course, nonlocally encoded information is not only hidden from the environment; we are unable to read it ourselves as well. However, with nonabelian anyons, we can have our cake and eat it too! At the conclusion of a quantum computation, when we are ready to perform the readout, we can bring the anyons together in pairs and observe the result of this fusion. In fact, it will suffice to distinguish the case where the charge of the composite is $c = 1$ from the case $c \neq 1$ --- that is, to distinguish a residual particle (unable to decay because of its nontrivial conserved charge) from no particle at all.

Note that for each pair of anyons this topological Hilbert space is finite-dimensional. An anyon model with this property is said to be *rational*. As in our discussion of the topologically degenerate ground state for an abelian model, anyons in rational nonabelian models always have topological spins that are roots of unity.

### 9.12.3 Braiding: the R-matrix

When two particles with labels $a$ and $b$ undergo a counterclockwise exchange, their total charge $c$ is unchanged. Therefore, since the two particles swap positions on the line, the swap induces a natural isomorphism mapping the Hilbert space $V_{ba}^c$ to $V_{ab}^c$; this map is the braid operator

$$
R: V_{ba}^c \to V_{ab}^c.
$$ {#eq-8.73}

If we choose canonical bases $\{|ba; c, \mu\rangle\}$ and $\{|ab; c, \mu'\rangle\}$ for these two spaces, $R$ can be expressed as the unitary matrix

$$
R: |ba; c, \mu\rangle \mapsto \sum_{\mu'} |ab; c, \mu'\rangle (R_{ab}^c)_\mu^{\mu'};
$$ {#eq-8.74}

note that $R$ may have a nontrivial action on the fusion states. When we represent the action of $R$ diagrammatically, it is convenient to fix the positions of the labels $a$ and $b$ on the incoming lines, and twist the lines counterclockwise as they move toward the fusion vertex $(\mu)$ --- the graph with twisted lines represents the state in $V_{ab}^c$ obtained by applying $R$ to $|ba; c, \mu\rangle$, which can be expanded in terms of the canonical basis for $V_{ab}^c$:

<!-- Page 45 -->
– Figure: Diagrammatic representation of $R$-move: incoming lines $a, b$ crossing counterclockwise into vertex $\mu$ equals $\sum_{\mu'} (R_{ba}^c)_\mu^{\mu'}$ times uncrossed lines into vertex $\mu'$ –

The *monodromy operator*

$$
R^2: V_{ab}^c \to V_{ab}^c
$$ {#eq-8.75}

is an isomorphism from $V_{ab}^c$ to itself, representing the effect of winding $a$ counterclockwise around $b$. As we already remarked in our discussion of the nonabelian superconductor, the monodromy operator is equivalent to rotating $c$ by $2\pi$ while rotating $a$ and $b$ by $-2\pi$; therefore, the eigenvalues of the monodromy operator are determined by the topological spins of the particles:

$$
(R_{ab}^c)^2 = e^{-2\pi i J_c} e^{2\pi i J_a} e^{2\pi i J_b} \equiv e^{i(\theta_c - \theta_a - \theta_b)}.
$$ {#eq-8.76}

Furthermore, as we argued for the case of abelian anyons, the topological spin is determined by the braid operator acting on a particle-antiparticle pair with trivial total charge:

$$
e^{-i\theta_a} = R_{a\bar{a}}^1
$$ {#eq-8.77}

(because creating a pair, exchanging, and annihilating is equivalent to rotating the particle by $-2\pi$).

### 9.12.4 Associativity of fusion: the F-matrix

Fusion is associative:

$$
(a \times b) \times c = a \times (b \times c).
$$ {#eq-8.78}

Mathematically, this is an axiom satisfied by the fusion rules of an anyon model. Physically, it is imposed because the total charge of a system of three particles is an intrinsic property of the three particles, and ought not to depend on whether we first fuse $a$ and $b$ and then fuse the result with $c$, or first fuse $b$ and $c$ and then fuse the result with $a$.

Therefore, when three particles with charges $a, b, c$ are fused to yield a total charge of $d$, there are two natural ways to decompose the topological Hilbert space in terms of the fusion spaces of pairs of particles:

$$
V_{abc}^d \cong \bigoplus_e V_{ab}^e \otimes V_{ec}^d \cong \bigoplus_{e'} V_{ae'}^d \otimes V_{bc}^{e'}.
$$ {#eq-8.79}

<!-- Page 46 -->
Correspondingly, there are two natural orthonormal bases for $V_{abc}^d$, which we may denote

$$
\begin{aligned}
|(ab)c \to d; e\mu\nu\rangle &\equiv |ab; e, \mu\rangle \otimes |ec; d, \nu\rangle, \\
|a(bc) \to d; e'\mu'\nu'\rangle &\equiv |ae'; d, \nu'\rangle \otimes |bc; e', \mu'\rangle,
\end{aligned}
$$ {#eq-8.80}

and which are related by a unitary transformation $F$:

$$
|(ab)c \to d; e\mu\nu\rangle = \sum_{e'\mu'\nu'} |a(bc) \to d; e'\mu'\nu'\rangle \left(F_{abc}^d\right)_{e\mu\nu}^{e'\mu'\nu'}.
$$ {#eq-8.81}

– Figure: The $F$-move tree diagram: tree $((ab)e, c)d$ equals $\sum_{e'\mu'\nu'} (F_{abc}^d)_{e\mu\nu}^{e'\mu'\nu'}$ times tree $(a, (bc)e')d$ –

The unitary matrices $F_{abc}^d$ are sometimes called *fusion matrices*; however, rather than risk causing confusion between $F$ and the fusion rules $N_{ab}^c$, I will just call it the *F-matrix*.

### 9.12.5 Many anyons: the standard basis

In an anyonic quantum computer, we process the topological quantum state of $n$ anyons by braiding the anyons. For describing this computation, it is convenient to adopt a standard basis for such a Hilbert space.

Suppose that $n$ anyons with total charge $c$, arranged sequentially along a line, carry labels $a_1, a_2, a_3, \dots, a_n$. Imagine fusing anyons 1 and 2, then fusing the result with anyon 3, then fusing the result with anyon 4, and so on. Associated with fusion in this order is a decomposition of the topological Hilbert space of the $n$ anyons

$$
V_{a_1 a_2 a_3 \cdots a_n}^c \cong \bigoplus_{b_1, b_2, \dots, b_{n-2}} V_{a_1 a_2}^{b_1} \otimes V_{b_1 a_3}^{b_2} \otimes V_{b_2 a_4}^{b_3} \otimes \cdots \otimes V_{b_{n-2} a_n}^c.
$$ {#eq-8.82}

Note that this space does *not* have a natural decomposition as a tensor product of subsystems associated with the localized particles; rather, we have expressed it as a direct sum of many tensor products. For nonabelian anyons, its dimension

$$
\dim\left(V_{a_1 a_2 a_3 \cdots a_n}^c\right) \equiv N_{a_1 a_2 a_3 \cdots a_n}^c = \sum_{b_1, b_2, b_3, \dots, b_{n-2}} N_{a_1 a_2}^{b_1} N_{b_1 a_3}^{b_2} N_{b_2 a_4}^{b_3} \cdots N_{b_{n-2} a_n}^c
$$ {#eq-8.83}

<!-- Page 47 -->
is exponential in $n$; thus the topological Hilbert space is a suitable arena for powerful quantum information processing.

This decomposition of $V_{a_1 a_2 a_3 \cdots a_n}^c$ suggests a standard basis whose elements are labeled by the intermediate charges $b_1, b_2, \dots, b_{n-2}$ and by the basis elements $\{|\mu_j\rangle\}$ for the fusion spaces $V_{b_{j-1} a_{j+1}}^{b_j}$:

$$
\{|a_1 a_2; b_1, \mu_1\rangle |b_1 a_3; b_2, \mu_2\rangle \cdots |b_{n-3} a_{n-1}; b_{n-2}, \mu_{n-2}\rangle |b_{n-2} a_n; c, \mu_{n-1}\rangle\},
$$ {#eq-8.84}

or in diagrammatic notation:

– Figure: The standard comb basis diagram: $a_1$ and $a_2$ fuse to $b_1$ at vertex $\mu_1$, $b_1$ and $a_3$ fuse to $b_2$ at vertex $\mu_2$, ..., up to $b_{n-2}$ and $a_n$ fusing to total charge $c$ at vertex $\mu_{n-1}$ –

Of course, this basis is chosen arbitrarily. If we preferred, we could imagine fusing the particles in a different order, and would obtain a different basis that can be expressed in terms of our standard one with help from the $F$-matrix.

### 9.12.6 Braiding in the standard basis: the B-matrix

We would like to consider what happens to states of the topological vector space $V_{a_1 a_2 a_3 \cdots a_n}^c$ of $n$ anyons when the particles are exchanged with one another. Actually, since exchanges can swap the positions of particles with distinct labels, they may map one topological vector space to another by permuting the labels. Nevertheless, we can consider the direct sums of the vector spaces associated with all the possible permutations of the labels, which will provide a representation of the braid group $B_n$.

We would like to describe how this representation acts on the standard bases for these spaces. It suffices to say how exchanges of neighboring particles are represented; that is, to specify the action of the generators of the braid group. However, so far, we have discussed only the action of the braid group on a pair of particles with definite total charge (the $R$-matrix), which is not in itself enough to tell us its action on the standard bases.

The way out of this quandary is to observe that, by applying the $F$-matrix, we can move from the standard basis to the basis in which the $R$-matrix is block diagonal, apply $R$, and then apply $F^{-1}$ to return to the standard basis:

<!-- Page 48 -->
– Figure: Sequence of three moves: crossed comb $\xrightarrow{F}$ crossed tree $\xrightarrow{R}$ uncrossed tree $\xrightarrow{F^{-1}}$ standard uncrossed comb –

The composition of these three operations, which expresses the effect of braiding in the standard basis, is denoted $B$ and sometimes called the "braid matrix;" but to avoid confusion between $B$ and $R$, I will just call it the *B-matrix*.

Consider exchanging the anyons in positions $j$ and $j+1$ along the line. In our decomposition of $V_{a_1 a_2 a_3 \cdots a_n}^c$, this exchange acts on the space

$$
V_{b_{j-2}, a_j, a_{j+1}}^{b_j} = \bigoplus_{b_{j-1}} V_{b_{j-2}, a_j}^{b_{j-1}} \otimes V_{b_{j-1}, a_{j+1}}^{b_j}.
$$ {#eq-8.85}

To reduce the number of subscripts, we will call this space $V_{acb}^d$, which is transformed by the exchange as

$$
B: V_{acb}^d \to V_{abc}^d.
$$ {#eq-8.86}

Let us express the action of $B$ in terms of the standard bases for the two spaces $V_{acb}^d$ and $V_{abc}^d$.

– Figure: Diagrammatic definition of $B$-matrix: braid crossing of incoming lines $b$ and $c$ on intermediate base $e$ equals $\sum_{e'\mu'\nu'} (B_{abc}^d)_{e\mu\nu}^{e'\mu'\nu'}$ times standard uncrossed tree with intermediate line $e'$ –

To avoid cluttering the equations, I suppress the labels for the fusion space basis elements (it is obvious where they should go). Hence we write

$$
\begin{aligned}
B|(ac)b \to d; e\rangle &= \sum_f B|a(cb) \to d; f\rangle \left(F_{acb}^d\right)_e^f \\
&= \sum_f |a(bc) \to d; f\rangle R_{bc}^f \left(F_{acb}^d\right)_e^f \\
&= \sum_{f, g} |(ab)c \to d; g\rangle \left[(F^{-1})_{abc}^d\right]_f^g R_{bc}^f \left(F_{acb}^d\right)_e^f,
\end{aligned}
$$ {#eq-8.87}

<!-- Page 49 -->
or

$$
B: |(ac)b \to d; e\rangle \mapsto \sum_g |(ab)c \to d; g\rangle \left(B_{abc}^d\right)_e^g,
$$ {#eq-8.88}

where

$$
\left(B_{abc}^d\right)_e^g = \sum_f \left[(F^{-1})_{abc}^d\right]_f^g R_{bc}^f \left(F_{acb}^d\right)_e^f.
$$ {#eq-8.89}

We have expressed the action of the $B$-matrix in the standard basis in terms of the $F$-matrix and $R$-matrix, as desired.

Thus, the representation of the braid group realized by $n$ anyons is completely characterized by the $F$-matrix and the $R$-matrix. Furthermore, we have seen that the $R$ matrix also determines the topological spins of the anyons, so that we have actually constructed a representation of a larger group whose generators include both the exchanges of neighboring particles and $2\pi$ rotations of the particles. A good name for this group would be the *ribbon group*, as its elements are in one-to-one correspondence with the topological classes of braided ribbons (which can be twisted) rather than braided strings; however, mathematicians have already named it "the mapping class group for the sphere with $n$ punctures."

And with that observation we have completed our description of an anyon model in this general setting. The model is specified by: (1) a label set, (2) the fusion rules, (3) the $R$-matrix, and (4) the $F$ matrix.

The mathematical object we have constructed is called a *unitary topological modular functor*, and it is closely related to two other objects that have been much studied: *topological quantum field theories* in 2+1 spacetime dimensions, and *conformal field theories* in 1+1 spacetime dimensions. However, we will just call it an *anyon model*.

## 9.13 Simulating anyons with a quantum circuit

A *topological quantum computation* is executed in three steps:

1. *Initialization:* Particle-antiparticle pairs $c_1\bar{c}_1, c_2\bar{c}_2, c_3\bar{c}_3, \dots, c_m\bar{c}_m$ are created. Each pair is of a specified type and has trivial total charge.
2. *Processing.* The $n = 2m$ particles are guided along trajectories, their world lines following a specified braid.
3. *Readout.* Pairs of neighboring particles are fused together, and it is recorded whether each pair annihilates fully or not. This record is the output of the computation.

<!-- Page 50 -->
(In the case of the nonabelian superconductor model of computation, we allowed the braiding to be conditioned on the outcome of fusing carried out during the processing stage. But now we are considering a model in which all measurements are delayed until the final readout.)

How powerful is this model of computation? I claim that this topological quantum computer can be simulated efficiently by a quantum circuit. Since the topological Hilbert space of $n$ anyons does not have a simple and natural decomposition as a tensor product of small subsystems, this claim may not be immediately obvious. To show it we must explain:

1. How to encode the topological Hilbert space using ordinary qubits.
2. How to represent braiding efficiently using quantum gates.
3. How to simulate the fusion of an anyon pair.

*Encoding.* Since each pair produced during initialization has trivial total charge, the initial state of the $n$ anyons also has trivial total charge. Therefore, the topological Hilbert space is

$$
V_{a_1 a_2 a_3 \cdots a_n}^1 \cong \bigoplus_{b_1, b_2, \dots, b_{n-3}} V_{a_1 a_2}^{b_1} \otimes V_{b_1 a_3}^{b_2} \otimes \cdots \otimes V_{b_{n-3} a_{n-1}}^{\bar{a}_n},
$$ {#eq-8.90}

for some choice of the labels $a_1, a_2, a_3, \dots, a_n$; there are $n - 3$ intermediate charges and $n - 2$ fusion spaces appearing in each summand. Exchanges of the particles swap the labels, but after each exchange the vector space still has the form eq. (9.90) with labels given by some permutation of the original labels.

Although each $n$-anyon topological Hilbert spaces is not itself a tensor products of subsystems, all of these spaces are contained in

$$
(\mathcal{H}_d)^{\otimes (n-2)},
$$ {#eq-8.91}

where

$$
\mathcal{H}_d = \bigoplus_{a, b, c} V_{abc}^1.
$$ {#eq-8.92}

Here, $a, b, c$ are summed over the complete label set of the model (which we have assumed is finite), so that $\mathcal{H}_d$ contains all the possible fusion states of three particles, and the dimension $d$ of $\mathcal{H}_d$ is

$$
d = \sum_{a, b, c} N_{abc}^1.
$$ {#eq-8.93}

Thus the state of $n$ anyons can be encoded in the Hilbert space of $n - 2$ *qudits* for some constant $d$ (which depends on the anyon model but is independent of $n$).
