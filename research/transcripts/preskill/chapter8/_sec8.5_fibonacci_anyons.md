# Section 8.5: Fibonacci Anyons, Quantum Dimension, Pentagon/Hexagon Equations, and Universal Quantum Computation [PDF Pages 51-62]

<!-- ============================================================ -->
<!-- Source: chap8.pdf, Physical Pages: 51-62                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 51 -->
independent of $n$). The basis states of this qudit can be chosen to be $\{|a, b, c; \mu\rangle\}$, where $\mu$ labels an element of the basis for the fusion space $V_{abc}^1$.

*Braiding.* In the topological quantum computer, a braid is executed by performing a sequence of exchanges, each acting on a pair of neighboring particles. The effect of each exchange in the standard basis is described by the $B$-matrix. How is $B$ represented acting on our encoding of the topological vector space (using qudits)? Suppressing fusion states, our basis for two-qudit states can be denoted $|a, b, \bar{c}\rangle |d, e, \bar{f}\rangle$. But in the topological quantum computer, the labels $d$ and $\bar{c}$ always match, and therefore to perform our simulation of braiding we need only consider two-qudit states whose labels match in this sense:

– Figure: B-matrix action on two matching qudits: braid crossing of incoming lines $e$ and $b$ equals $\sum_g (B_{aeb}^f)_d^g$ times uncrossed lines with intermediate charge $g$ –

Then the action of the $B$-matrix on these basis states is

$$
B: |a, b, \bar{d}\rangle |d, e, \bar{f}\rangle \mapsto \sum_g |a, e, \bar{g}\rangle |g, b, \bar{f}\rangle \left(B_{aeb}^f\right)_d^g.
$$ {#eq-8.94}

As desired, we have represented the $B$ as a $d^2 \times d^2$ matrix acting on a pair of neighboring qudits.

*Fusion.* Fusion of a pair of anyons can be simulated by a two-qudit measurement, which can be reduced to a single-qudit measurement with a little help from the $F$-matrix:

– Figure: Fusion simulated by F-move on two qudits: uncoupled lines $b, e$ equal $\sum_g (F_{abe}^f)_d^g$ times intermediate vertical line $g$ fusing $b, e$ –

Consider a basis state $|a, b, \bar{d}\rangle |d, e, \bar{f}\rangle$ for a pair of neighboring qudits; what is the amplitude for the anyon pair $(be)$ to have trivial total charge? Using an $F$-move, the state can be expanded as

$$
\begin{aligned}
F: |a, b, \bar{d}\rangle |d, e, \bar{f}\rangle &\mapsto \sum_g |a, g, \bar{f}\rangle |b, \bar{g}, e\rangle \left(F_{abe}^f\right)_d^g \\
&= |a, 1, \bar{f}\rangle |b, 1, e\rangle \left(F_{abe}^f\right)_d^1 + \sum_{g \neq 1} |a, g, \bar{f}\rangle |b, \bar{g}, e\rangle \left(F_{abe}^f\right)_d^g;
\end{aligned}
$$ {#eq-8.95}

<!-- Page 52 -->
we have separated the sum over $g$ into the component for which $(be)$ fuses to 1, plus the remainder. After the $F$-move (which is just a particular two-qudit unitary gate), we can sample the probability that $(be)$ fuses to 1 by performing a projective measurement of the second qudit in the basis $\{|b, \bar{g}, e\rangle\}$, and recording whether $g = 1$.

This completes our demonstration that a quantum circuit can simulate efficiently a topological quantum computer.

## 9.14 Fibonacci anyons

Now we have established that topological quantum computation is no more powerful than the quantum circuit model --- any problem that can be solved efficiently by braiding nonabelian anyons can also be solved efficiently with a quantum circuit. But is it as powerful? Can we simulate a universal quantum computer by braiding anyons? The answer depends on the specific properties of the anyons: some nonabelian anyon models are universal, others are not. To find the answer for a particular anyon model, we need to understand the properties of the representations of the braid group that are determined by the $F$-matrix and $R$-matrix.

Rather than give a general discussion, we will study one especially simple nonabelian anyon model, and demonstrate its computational universality. This model is the very simplest nonabelian model --- conformal field theorists call it the "Yang-Lee model," but I will call it the "Fibonacci model" for reasons that will soon be clear.

In the Fibonacci model there are only two labels --- the trivial label, which I will now denote 0, and a single nontrivial label that I will call 1, where $\bar{1} = 1$. And there is only one nontrivial fusion rule:

$$
1 \times 1 = 0 + 1;
$$ {#eq-8.96}

when two anyons are brought together they either annihilate, or fuse to become a single anyon. The model is nonabelian because two anyons can fuse in two distinguishable ways.

Consider the standard basis for the Hilbert space $V_{1^n}^b$ of $n$ anyons, where each basis element describes a distinguishable way in which the $n$ anyons could fuse to give total charge $b \in \{0, 1\}$. If the two anyons furthest to the left were fused first, the resulting charge could be 0 or 1; this charge could then fuse with the third anyon, yielding a total charge of 0 or 1, and so on. Finally, the last anyon fuses with the total charge of the first $n - 1$ anyons to give the total charge $b$. Altogether $n - 2$ intermediate charges $b_1, b_2, b_3, \dots, b_{n-2}$ appear in this description of the fusion process; thus the corresponding basis element can be designated with a binary string of length $n - 2$. If the total charge is 0, the result of fusing the

<!-- Page 53 -->
first $n - 1$ anyons *has* to be 1, so the basis states are labeled by strings of length $n - 3$.

However, *not all* binary strings are allowed --- a 0 must always be followed by a 1. There cannot be two zeros in a row because when the charge 0 fuses with 1, a total charge of 1 is the only possible outcome. Otherwise, there is no restriction on the sequence. Therefore, the basis states are in one-to-one with the binary strings that do not contain two successive 0's.

Thus the dimensions $N_n^0 \equiv N_{1^n}^0$ of the topological Hilbert spaces $V_{1^n}^0$ obey a simple recursion relation. If the fusion of the first two particles yields trivial total charge, then the remaining $n - 2$ particles can fuse in $N_{n-2}^0$ distinguishable ways, and if the fusion of the first two particles yields an anyon with nontrivial charge, then that anyon can fuse with the other $n - 2$ anyons in $N_{n-1}^0$ ways; therefore,

$$
N_n^0 = N_{n-1}^0 + N_{n-2}^0.
$$ {#eq-8.97}

Since $N_1^0 = 0$ and $N_2^0 = 1$, the solution to this recursion relation is

$$
\begin{array}{rcccccccccc}
n &=& 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 \dots \\
N_n^0 &=& 0 & 1 & 1 & 2 & 3 & 5 & 8 & 13 & 21 \dots
\end{array}
$$ {#eq-8.98}

--- the dimensions are Fibonacci numbers (which is why I am calling this model the "Fibonacci model").

The Fibonacci numbers grow with $n$ at a rate $N_n^0 \approx C \phi^n$, where $\phi$ is the golden mean $\phi = \frac{1}{2}(1 + \sqrt{5}) \approx 1.618$. Because $\phi$ governs the rate at which the Hilbert space enlarges as anyons are added, we say that $d = \phi$ is the *quantum dimension* of the Fibonacci anyon. That this "dimension" is an irrational number illustrates vividly that the topological Hilbert space has no natural decomposition as a tensor product of subsystems --- instead, the topologically encoded quantum information is a collective property of the $n$ anyons.

## 9.15 Quantum dimension

We will return shortly to the properties of the Fibonacci model, but first let's explore more deeply the concept of quantum dimension. For a general anyon model, how should the dimension $d_a$ of label $a$ be defined? For this purpose, it is convenient to imagine a physical process in which two $a\bar{a}$ pairs are created (each with trivial total charge); then the particle $a$ from the pair on the right fuses with the antiparticle $\bar{a}$ from the pair on the left. Do these particles annihilate?

With suitable phase conventions, the *amplitude* for the annihilation to occur is a real number in the unit interval $[0, 1]$. Let us define this

<!-- Page 54 -->
number to be $1/d_a$, where $d_a$ is the quantum dimension of $a$ (and $1/d_a^2$ is the *probability* that annihilation occurs). Note that it is clear from this definition that $d_a = d_{\bar{a}}$. For the case in which the $a$ is the label of an irreducible representation $R_a$ of a group $G$, the dimension is just $d_a = |R_a|$, the dimension of the representation. This is easily understood pictorially:

– Figure: Left: two separate loops of $a\bar{a} = 1$. Right: partner swapped loop $= 1/d_a$ –

If two pairs are created and then each pair annihilates immediately, the world lines of the pairs form two closed loops, and $|R|$ counts the number of distinct "colors" that propagate around each loop. But if the particle from each pair annihilates the antiparticle from the other pair, there is only one closed loop and therefore one sum over colors; if we normalize the process on the left to unity, the amplitude for the process on the right is suppressed by a factor of $1/|R|$. To say the same thing in an equation, the normalized state of an $R\bar{R}$ pair is

$$
|R\bar{R}\rangle = \frac{1}{\sqrt{|R|}} \sum_i |i\rangle |\bar{i}\rangle,
$$ {#eq-8.99}

where $\{|i\rangle\}$ denotes an orthonormal basis for $R$ and $\{|\bar{i}\rangle\}$ is a basis for $\bar{R}$. Suppose that two pairs $|R\bar{R}\rangle$ and $|R'\bar{R}'\rangle$ are created; if the pairs are fused after swapping partners, the amplitude for annihilation is

$$
\begin{aligned}
\langle R\bar{R}, R'\bar{R}' | R\bar{R}', R'\bar{R}\rangle &= \frac{1}{|R|^2} \sum_{i, i', j, j'} \langle j\bar{j}, j'\bar{j}' | i\bar{i}', i'\bar{i}\rangle \\
&= \frac{1}{|R|^2} \sum_{i, i', j, j'} \delta_{ji} \delta_{ji'} \delta_{j'i'} \delta_{j'i} = \frac{1}{|R|^2} \sum_i \delta_{ii} = \frac{1}{|R|}.
\end{aligned}
$$ {#eq-8.100}

In general, though, the quantum dimension has no direct interpretation in terms of counting "colors," and there is no reason why it has to be an integer.

How are such quantum dimensions related to the dimensions of topological Hilbert spaces? To see the connection, it is very useful to alter our normalization conventions. Notice we can introduce many "zigzags" in the world line of a particle of type $a$ by creating many $a\bar{a}$ pairs, and

<!-- Page 55 -->
fusing the particle from each pair with the antiparticle from the neighboring pair. However, each zigzag reduces the amplitude by another factor of $1/d_a$. We can compensate for these factors of $1/d_a$ if we weight each pair creation or annihilation event by a factor of $\sqrt{d_a}$. With this new convention, we can bend the world line of a particle forward or backward in time without paying any penalty:

– Figure: World line zigzag with factor $\sqrt{d_a}$ at each bend equals straight line $a$ –

Now the weight assigned to a world line is a topological invariant (it is unchanged when we distort the line), and a world line of type $a$ forming a closed loop is weighted by $d_a$.

With our new conventions, we can justify this sequence of manipulations:

– Figure: Diagrammatic derivation: $d_a d_b = (\text{loop } a)(\text{loop } b) = (\text{nested loop}) = \sum_{c, \mu} \dots = \sum_c N_{ab}^c d_c$ –

Each diagram represents an inner product of two (unconventionally normalized) states. We have inserted a complete sum over the labels ($c$) and the corresponding fusion states ($\mu$) that can arise when $a$ and $b$ fuse. Exploiting the topological invariance of the diagram, we have then turned it "inside out," then contracted the fusion states (acquiring the factor $N_{ab}^c$ which counts the possible values of $\mu$).

The equation that we have derived,

$$
d_a d_b = \sum_c N_{ab}^c d_c \equiv \sum_c (N_a)_b^c d_c,
$$ {#eq-8.101}

<!-- Page 56 -->
says that the vector $\vec{d}$, whose components are the quantum dimensions, is an eigenvector with eigenvalue $d_a$ of the matrix $N_a$ that describes how the label $a$ fuses with other labels:

$$
N_a \vec{d} = d_a \vec{d}.
$$ {#eq-8.102}

Furthermore, since $N_a$ has nonnegative entries and all components of $\vec{d}$ are positive, $d_a$ is the largest eigenvalue of $N_a$ and is nondegenerate. (This simple observation is sometimes called the *Perron-Frobenius theorem*.) For $n$ anyons, each with label $a$, the topological Hilbert space $V_{aaa\cdots a}^b$ for the sector with total charge $b$ has dimension

$$
N_{aaa\cdots a}^b = \sum_{\{b_i\}} N_{aa}^{b_1} N_{ab_1}^{b_2} N_{ab_2}^{b_3} \cdots N_{ab_{n-2}}^b = \langle b | (N_a)^{n-1} |a\rangle.
$$ {#eq-8.103}

The matrix $N_a$ can be diagonalized, and expressed as

$$
N_a = |v\rangle d_a \langle v| + \cdots,
$$ {#eq-8.104}

where

$$
|v\rangle = \frac{\vec{d}}{\mathcal{D}}, \quad \mathcal{D} = \sqrt{\sum_c d_c^2},
$$ {#eq-8.105}

and subleading eigenvalues have been omitted; therefore

$$
N_{aaa\cdots a}^b = d_a^n d_b / \mathcal{D}^2 + \cdots,
$$ {#eq-8.106}

where the ellipsis represents terms that are exponentially suppressed for large $n$. We see that the quantum dimension $d_a$ controls the rate of growth of the $n$-particle Hilbert space for anyons of type $a$.

Because the label 0 with trivial charge fuses trivially, we have $d_0 = 1$. In the case of the Fibonacci model, it follows from the fusion rule $1 \times 1 = 0 + 1$ that $d_1^2 = 1 + d_1$, which is solved by $d_1 = \phi$ as we found earlier; therefore $\mathcal{D}^2 = d_0^2 + d_1^2 = 1 + \phi^2 = 2 + \phi$. Our formula becomes

$$
N_{111\cdots 1}^0 = \left(\frac{1}{2 + \phi}\right) \phi^n,
$$ {#eq-8.107}

which is an excellent approximation to the Fibonacci numbers even for modest values of $n$.

Suppose that an $a\bar{a}$ pair and a $b\bar{b}$ pair are both created. If the $a$ and $b$ particles are fused, with what probability $p(ab \to c)$ will their total charge be $c$? This question can be answered using the same kind of graphical manipulations:

<!-- Page 57 -->
– Figure: Diagrammatic calculation: $d_a d_b p(ab \to c) = \sum_\mu \dots = N_{ab}^c d_c$ –

Dividing by $d_a d_b$ to restore the proper renormalization of the inner product, we conclude that

$$
p(ab \to c) = \frac{N_{ab}^c d_c}{d_a d_b},
$$ {#eq-8.108}

which generalizes the formula $p(a\bar{a} \to 1) = 1/d_a^2$ that we used to define the quantum dimension, and satisfies the normalization condition

$$
\sum_c p(ab \to c) = 1.
$$ {#eq-8.109}

To arrive at another interpretation of the quantum dimension, imagine that a dense gas of anyons is created, which is then permitted to anneal for awhile --- anyons collide and fuse, gradually reducing the population of particles. Eventually, but long before the thermal equilibrium is attained, the collision rate becomes so slow that the fusion process effectively turns off. By this stage, whatever the initial distribution of particles types, a steady state distribution is attained that is preserved by collisions. If in the steady state particles of type $a$ appear with probability $p_a$, then

$$
\sum_{ab} p_a p_b p(ab \to c) = p_c.
$$ {#eq-8.110}

Using

$$
\sum_a N_{ab}^c d_a = \sum_a N_{b\bar{c}}^{\bar{a}} d_{\bar{a}} = d_b d_{\bar{c}} = d_b d_c,
$$ {#eq-8.111}

we can easily verify that this condition is satisfied by

$$
p_a = \frac{d_a^2}{\mathcal{D}^2}.
$$ {#eq-8.112}

We conclude that if anyons are created in a random process, those carrying labels with larger quantum dimension are more likely to be produced, in keeping with the property that anyons with larger dimension have more quantum states.

<!-- Page 58 -->
## 9.16 Pentagon and hexagon equations

To assess the computational power of an anyon model like the Fibonacci model, we need to know the braiding properties of the anyons, which are determined by the $R$ and $F$ matrices. We will see that the braiding rules are highly constrained by algebraic consistency conditions. For the Fibonacci model, these consistency conditions suffice to determine a unique braiding rule that is compatible with the fusion rules.

Consistency conditions arise because we can make a sequence of "$F$-moves" and "$R$-moves" to obtain an isomorphism relating two topological Hilbert spaces. The isomorphism can be regarded as a unitary matrix that relates the canonical orthonormal bases for two different spaces; this unitary transformation does not depend on the particular sequence of moves from which the isomorphism is constructed, only on the initial and final bases.

For example, there are five different ways to fuse four particles (without any particle exchanges), which are related by $F$-moves:

– Figure: The Pentagon Diagram connecting five 4-particle fusion trees via five $F$-moves –

The basis shown furthest to the left in this pentagon diagram is the "left standard basis" $\{|\text{left}; a, b\rangle\}$, in which particles 1 and 2 are fused first, the resulting charge $a$ is fused with particle 3 to yield charge $b$, and then finally $b$ is fused with particle 4 to yield the total charge 5. The basis shown furthest to the right is the "right standard basis" $\{|\text{right}; c, d\rangle\}$, in which the particles are fused from right to left instead of left to right. Across the top of the pentagon, these two bases are related by two $F$-

<!-- Page 59 -->
moves, and we obtain

$$
|\text{left}; a, b\rangle = \sum_{c, d} |\text{right}; c, d\rangle (F_{12c}^5)_a^d (F_{a34}^5)_b^c.
$$ {#eq-8.113}

Across the bottom of the pentagon, the bases are related by three $F$-moves, and we find

$$
|\text{left}; a, b\rangle = \sum_{c, d, e} |\text{right}; c, d\rangle (F_{234}^d)_e^c (F_{1e4}^5)_b^d (F_{123}^b)_a^e.
$$ {#eq-8.114}

Equating our two expressions for $|\text{left}; a, b\rangle$, we obtain the *pentagon equation*:

$$
(F_{12c}^5)_a^d (F_{a34}^5)_b^c = \sum_e (F_{234}^d)_e^c (F_{1e4}^5)_b^d (F_{123}^b)_a^e.
$$ {#eq-8.115}

Another nontrivial consistency condition is found by considering the various ways that three particles can fuse:

– Figure: The Hexagon Diagram connecting six 3-particle fusion trees via $F$ and $R$ moves –

The basis $\{|\text{left}; a\rangle\}$ furthest to the left in this hexagon diagram is obtained if the particles are arranged in the order 123, and particles 1 and 2 are fused first, while the basis $\{|\text{right}, c\rangle\}$ furthest to the right is obtained if the particles are arranged in order 231, and particles 1 and 3 are fused first. Across the top of the hexagon, the two bases are related by the sequence of moves $FRF$:

$$
|\text{left}, a\rangle = \sum_{b, c} |\text{right}; c\rangle (F_{231}^4)_b^c R_{1b}^4 (F_{123}^4)_a^b.
$$ {#eq-8.116}

Across the bottom of the hexagon, the bases are related by the sequence of moves $RFR$, and we find

$$
|\text{left}, a\rangle = \sum_c |\text{right}; c\rangle R_{13}^c (F_{213}^4)_a^c R_{12}^a.
$$ {#eq-8.117}

<!-- Page 60 -->
Equating our two expressions for $|\text{left}; a\rangle$, we obtain the *hexagon equation*:

$$
R_{13}^c (F_{213}^4)_a^c R_{12}^a = \sum_b (F_{231}^4)_b^c R_{1b}^4 (F_{123}^4)_a^b.
$$ {#eq-8.118}

A beautiful theorem, which I will not prove here, says that there are no further conditions that must be imposed to ensure the consistency of braiding and fusing. That is, for any choice of an initial and final basis for $n$ anyons, *all* sequences of $R$-moves and $F$-moves that take the initial basis to the final basis yield the *same* isomorphism, provided that the pentagon equation and hexagon equation are satisfied. This theorem is an instance of the *MacLane coherence theorem*, a fundamental result in category theory. The pentagon and hexagon equations together are called the *Moore-Seiberg polynomial equations* --- their relevance to physics was first appreciated in studies of (1+1)-dimensional conformal field theory during the 1980's.

A solution to the polynomial equations defines a viable anyon model. Therefore, there is a systematic procedure for constructing anyon models:

1. Choose a set of labels and assume a fusion rule.
2. Solve the polynomial equations for $R$ and $F$.

If no solutions exist, then the hypothetical fusion rule is incompatible with the principles of local quantum physics and must be rejected. If there is more than one solution (not related to one another by any reshuffling of the labels, redefinition of bases, etc.), then each distinct solution defines a distinct model with the assumed fusion rule.

To illustrate the procedure, consider the polynomial equations for the Fibonacci fusion rule. There are only two $F$-matrices that arise, which we will denote as

$$
F_{0111} \equiv F_0, \quad F_{1111} \equiv F_1.
$$ {#eq-8.119}

$F_0$ is really the $1 \times 1$ matrix

$$
(F_0)_a^b = \delta_a^1 \delta_1^b,
$$ {#eq-8.120}

while $F_1$ is a $2 \times 2$ matrix. The pentagon equation becomes

$$
(F_c)_a^d (F_a)_b^c = \sum_e (F_d)_e^c (F_e)_b^d (F_b)_a^e.
$$ {#eq-8.121}

The general solution for $F \equiv F_1$ is

$$
F = \begin{pmatrix} \tau & e^{i\phi}\sqrt{\tau} \\ e^{-i\phi}\sqrt{\tau} & -\tau \end{pmatrix},
$$ {#eq-8.122}

<!-- Page 61 -->
where $e^{i\phi}$ is an arbitrary phase (which we can set to 1 with a suitable phase convention), and $\tau = (\sqrt{5} - 1)/2 = \phi - 1 \approx .618$, which satisfies

$$
\tau^2 + \tau = 1.
$$ {#eq-8.123}

The $2 \times 2$ $R$-matrix that describes a counterclockwise exchange of two Fibonacci anyons has two eigenvalues --- $R^0$ for the case where the total charge of the pair of anyons is trivial, and $R^1$ for the case where the total charge is nontrivial. The hexagon equation becomes

$$
R^c (F)_a^c R^a = (F)_0^c (F)_a^0 + (F)_1^c R^1 (F)_a^1.
$$ {#eq-8.124}

Using the expression for $F$ found by solving the pentagon equation, we can solve the hexagon equation for $R$, finding

$$
R = \begin{pmatrix} e^{4\pi i/5} & 0 \\ 0 & -e^{2\pi i/5} \end{pmatrix}, \quad F = \begin{pmatrix} \tau & \sqrt{\tau} \\ \sqrt{\tau} & -\tau \end{pmatrix}.
$$ {#eq-8.125}

The only other solution is the complex conjugate of this one; this second solution really describes the same model, but with clockwise and counterclockwise braiding interchanged. Therefore, an anyon model with the Fibonacci fusion rule really *does* exist, and it is essentially unique.

## 9.17 Simulating a quantum circuit with Fibonacci anyons

Now we know enough to address whether a universal quantum computer can be simulated using Fibonacci anyons. We need to explain how qubits can be encoded with anyons, and how a universal set of quantum gates can be realized.

First we note that the Hilbert space $V_4^0 \equiv V_{1111}^0$ has dimension $N_4^0 = 2$; therefore a qubit can be encoded by four anyons with trivial total charge. The anyons are lined up in order 1234, numbered from left to right; in the standard basis state $|0\rangle$, anyons number 1 and number 2 fuse to yield total charge 0, while in the standard basis state $|1\rangle$, anyons 1 and 2 fuse to yield total charge 1. Acting on this standard basis, the braid group generator $\sigma_1$ (counterclockwise exchange of particles 1 and 2) is represented by

$$
\sigma_1 \mapsto R = \begin{pmatrix} e^{4\pi i/5} & 0 \\ 0 & -e^{2\pi i/5} \end{pmatrix},
$$ {#eq-8.126}

while the generator $\sigma_2$ is represented by

$$
\sigma_2 \mapsto B = F^{-1} R F, \quad F = \begin{pmatrix} \tau & \sqrt{\tau} \\ \sqrt{\tau} & -\tau \end{pmatrix}.
$$ {#eq-8.127}

<!-- Page 62 -->
These matrices generate a representation of the braid group $B_3$ on three strands whose image is dense in $\text{SU}(2)$. Indeed, $R$ and $B$ generate $\mathbb{Z}_{10}$ subgroups of $\text{U}(2)$, about two distinct axes, and there is no finite subgroup of $\text{U}(2)$ that contains both of these subgroups --- therefore, the representation closes on the group containing all elements of $\text{U}(2)$ with determinant equal to a 10th root of unity. Similarly, for $n$ anyons with trivial total charge, the image of the representation of the braid group is dense in $\text{SU}(N_n^0)$.

To simulate a quantum circuit acting on $n$ qubits, altogether $4n$ anyons are used. We have just seen that by braiding within each cluster of four anyons, arbitrary single-qubit gates can be realized. To complete a universal set, we will need two-qubit gates as well. But two neighboring qubits are encoded by eight anyons, and exchanges of these anyons generate a representation of $B_8$ whose image is dense in $\text{SU}(N_8^0) = \text{SU}(13)$, which of course includes the $\text{SU}(4)$ that acts on the two encoded qubits. Therefore, each gate in a universal set can be simulated with arbitrary accuracy by some finite braid.

Since we can braid clockwise as well as counterclockwise, the inverse of each exchange gate is also in our repertoire. Therefore, we can apply the Solovay-Kitaev theorem to conclude that the universal gates of the circuit model can be simulated to accuracy $\varepsilon$ with braids of length $\text{poly}(\log(1/\varepsilon))$. It follows that an ideal quantum circuit with $L$ gates acting on all together $n$ qubits can be simulated to fixed accuracy using $4n$ anyons and a braid of length $O(L \cdot \text{poly}(\log(L)))$. As desired, we have shown that a universal quantum computer can be simulated efficiently with Fibonacci anyons. Note that, in contrast to the simulation using the nonabelian superconductor model, no intermediate measurements are needed to realize the universal gates.

In the analysis above, we have assumed that there are no errors in the simulation other than those limiting the accuracy of the Solovay-Kitaev approximation to the ideal gates. It is therefore implicit that the temperature is small enough compared to the energy gap of the model that thermally excited anyons are too rare to cause trouble, that the anyons are kept far enough apart from one another that uncontrolled exchange of charge can be neglected, and in general that errors in the topological quantum computation are unimportant. If the error rate is small but not completely negligible, then the standard theory of quantum fault tolerance can be invoked to boost the accuracy of the simulation as needed, at an additional overhead cost polylogarithmic in $L$. The fault-tolerant procedure should include a method for controlling the "leakage" of the encoded qubits --- that is, to prevent the drift of the clusters of four qubits from the two-dimensional computational space $V_4^0$ to its three-dimensional orthogonal complement $V_4^1$.
