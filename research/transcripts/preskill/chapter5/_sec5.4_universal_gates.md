# Section 5.4: Universal Quantum Gates [PDF Pages 33-45]

<!-- ============================================================ -->
<!-- Source: chap5.pdf, Physical Pages: 33-45                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 33 -->
## 5.4 Universal quantum gates

We must address one more fundamental question about quantum computation; how do we construct an adequate set of quantum gates? In other words, what constitutes a universal quantum computer?

We will find a pleasing answer. Any generic two-qubit gate suffices for universal quantum computation. That is, for all but a set of measure zero of $4 \times 4$ unitary matrices, if we can apply that matrix to any pair of qubits, then we can construct a circuit acting on $n$ qubits which computes a transformation coming as close as we please to any element of $U(2^n)$. Mathematically, this is not a particularly deep result, but physically it is significant. It means that, in the quantum world, as long as we can devise a generic interaction between any two qubits, and we can implement that interaction accurately, we can build up any quantum computation, no matter how complex. Nontrivial computation is ubiquitous in quantum theory.

Aside from this general result, it is also of some interest to exhibit particular universal gate sets that might be particularly easy to implement physically. We will discuss a few examples.

### 5.4.1 Notions of universality

In our standard circuit model of quantum computation, we imagine that our circuit has a finite set of “hard-wired” quantum gates
$$
\mathcal{G} = \{\boldsymbol{U}_1, \boldsymbol{U}_2, \dots, \boldsymbol{U}_m\},
$$ {#eq-5.80}
where $\boldsymbol{U}_j$ acts on $k_j$ qubits, and $k_j \le k$ (a constant) for each $j$. Normally we also assume that the gate $\boldsymbol{U}_j$ can be applied to any $k_j$ of the $n$ qubits in the computer. Actually, placing some kind of geometric locality constraints on the gates would not drastically change our analysis of complexity, as long as we can construct (a good approximation to a) a SWAP gate (which swaps the positions of two neighboring qubits) using our gate set. If we want to perform $\boldsymbol{U}_j$ on $k_j$ qubits that are widely separated, we may first perform a series of SWAP gates to bring the qubits together,

<!-- Page 34 -->
then perform the gate, and finally perform SWAP gates to return the qubits to their original positions.

When we say the gate set $\mathcal{G}$ is universal we mean that the unitary transformations that can be constructed as quantum circuits using this gate set are dense in the unitary group $U(2^n)$, up to an overall phase. That is for any $V \in U(2^n)$ and any $\delta > 0$, there is a unitary $\tilde{V}$ achieved by a finite circuit such that
$$
\|\tilde{V} - e^{i\phi}V\|_{\sup} \le \delta
$$ {#eq-5.81}
for some phase $e^{i\phi}$. (It is natural to use the sup norm to define the deviation of the circuit from the target unitary, but we would reach similar conclusions using any reasonable topology on $U(2^n)$.) Sometimes it is useful to relax this definition of universality; for example we might settle for encoded universality, meaning that the circuits are dense not in $U(2^n)$ but rather some subgroup $U(N)$, where $N$ is exponential (or at least superpolynomial) in $n$.

There are several variations on the notion of universality that are noteworthy, because they illuminate the general theory or are useful in applications.

(1) *Exact universality.* If we are willing to allow uncountable gate sets, then we can assert that for certain gate sets we can construct a circuit that achieves an arbitrary unitary transformation exactly. We will see that two-qubit gates are exactly universal — any element of $U(2^n)$ can be constructed as a finite circuit of two qubit gates. Another example is that the two-qubit CNOT gate, combined with arbitrary single-qubit gates, is exactly universal (Exercise 5.2).

In fact the CNOT gate is not special in this respect. Any “entangling” two-qubit gate, when combined with arbitrary single-qubit gates, is universal (Exercise 5.6). We say a two-qubit gate is entangling if it maps some product state to a state which is not a product state.

An example of a two-gate which is not entangling is a “local gate” — a product unitary $\boldsymbol{V} = \boldsymbol{A} \otimes \boldsymbol{B}$; another example is the SWAP gate, or any gate “locally equivalent” to SWAP, i.e., of the form
$$
\boldsymbol{V} = (\boldsymbol{A} \otimes \boldsymbol{B})(\mathbf{SWAP})(\boldsymbol{C} \otimes \boldsymbol{D}).
$$ {#eq-5.82}
In fact these are the only non-entangling two-qubit gates. Every two-qubit unitary which is not local or locally equivalent to SWAP is entangling, and hence universal when combined with arbitrary single-qubit gates.

(2) *Generic universality.* Gates acting on two or more qubits which are not local are typically universal. For example, almost any two-qubit gate is universal, if the gate can be applied to any pair of the $n$ qubits. By “almost any” we mean except for a set of measure zero in $U(4)$.

<!-- Page 35 -->
(3) *Particular finite universal gate sets.* It is shown in the Exercises 5.3-5.5 that each one of the following gate sets is universal:
$$
\mathcal{G} = \{\boldsymbol{H}, \Lambda(\boldsymbol{S})\}, \quad \{\boldsymbol{H}, \boldsymbol{T}, \Lambda(\boldsymbol{X})\}, \quad \{\boldsymbol{H}, \boldsymbol{S}, \Lambda^2(\boldsymbol{X})\},
$$ {#eq-5.83}
where $\boldsymbol{H}, \boldsymbol{S}, \boldsymbol{T}$ are the single-qubit gates
$$
\boldsymbol{H} = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad \boldsymbol{S} = \begin{pmatrix} e^{-i\pi/4} & 0 \\ 0 & e^{i\pi/4} \end{pmatrix}, \quad \boldsymbol{T} = \begin{pmatrix} e^{-i\pi/8} & 0 \\ 0 & e^{i\pi/8} \end{pmatrix}.
$$ {#eq-5.84}
In Bloch sphere language, the “Hadamard gate” $\boldsymbol{H} = \frac{1}{\sqrt{2}}(\boldsymbol{X} + \boldsymbol{Z})$ is a rotation by $\pi$ about the axis $\hat{x} + \hat{z}$, $\boldsymbol{S} = \exp\left(-i\frac{\pi}{4}\boldsymbol{Z}\right)$ is a rotation by $\pi/2$ about the $\hat{z}$ axis, and $\boldsymbol{T} = \exp\left(-i\frac{\pi}{8}\boldsymbol{Z}\right)$ is a rotation by $\pi/4$ about the $\hat{z}$ axis. By $\Lambda(\boldsymbol{S})$ we mean the two-qubit [gate] in which $\boldsymbol{S}$ is applied to the target qubit iff the control qubit is $|1\rangle$. More generally, we use the notation $\Lambda(\boldsymbol{U})$, where $\boldsymbol{U}$ is a single-qubit gate, to denote the two-qubit gate
$$
\Lambda(\boldsymbol{U}) = |0\rangle\langle 0| \otimes \boldsymbol{I} + |1\rangle\langle 1| \otimes \boldsymbol{U};
$$ {#eq-5.85}
likewise we use $\Lambda^2(\boldsymbol{U})$ to denote the three-qubit gate
$$
\Lambda^2(\boldsymbol{U}) = (\boldsymbol{I} - |11\rangle\langle 11|) \otimes \boldsymbol{I} + |11\rangle\langle 11| \otimes \boldsymbol{U},
$$ {#eq-5.86}
etc.

That particular finite gates sets are universal is especially important in the theory of quantum fault tolerance, in which highly accurate logical gates acting on encoded quantum states are constructed from noisy physical gates. As we’ll discuss in Chapter 8, only a discrete set of logical gates can be well protected against noise, where the set depends on how the quantum information is encoded. The goal of fault-tolerant gate constructions is to achieve a universal set of such protected gates.

(4) *Efficient circuits of universal gates.* The above results concern only the “reachability” of arbitrary $n$-qubit unitaries; they say nothing about the circuit size needed for a good approximation. Yet the circuit size is highly relevant if we want to approximate one universal gate set by using another one, or if we want to approximate the steps in an ideal quantum algorithm to acceptable accuracy.

We already know that circuits with size exponential in $n$ are needed to approximate arbitrary $n$-qubit unitaries using a finite gate set. However, we will see that, for any fixed $k$, a $k$-qubit unitary can be approximated to accuracy $\varepsilon$ using a circuit whose size scales with the error like $\operatorname{polylog}(1/\varepsilon)$. This result, the Solovay-Kitaev theorem, holds for any universal gate set which is “closed under inverse” — that is, such that the inverse of each gate in the set can be constructed exactly using a finite circuit.

<!-- Page 36 -->
The Solovay-Kitaev theorem (which we prove in §5.4.4) tells us that one universal gate set can accurately approximate another one at a modest cost; therefore a characterization of the complexity of a computation based on quantum circuit size is not very sensitive to how the universal gate set is chosen. For example, suppose I build a unitary transformation $\boldsymbol{U}$ using $T$ gates chosen from gate set $\mathcal{G}_1$, and I want to approximate $\boldsymbol{U}$ to constant accuracy $\varepsilon$ using gates chosen from gate set $\mathcal{G}_2$. It will suffice to approximate each gate from $\mathcal{G}_1$ to accuracy $\varepsilon/T$, which can be achieved using a circuit of $\operatorname{polylog}(T/\varepsilon)$ gates from $\mathcal{G}_2$. Therefore $\boldsymbol{U}$ can be approximated with all together $O(T\operatorname{polylog}(T))$ $\mathcal{G}_2$ gates.

Another consequence of the Solovay-Kitaev theorem concerns our conclusion that polynomial-size circuits can reach (to constant accuracy) only a tiny fraction of $U(2^n)$. How is the conclusion modified if we build circuits using arbitrary $k$-qubit unitaries (where $k$ is constant) rather than gates chosen from a finite gate set? Because approximating the $k$-qubit unitaries using the finite gate set inflates the circuit size by only a $\operatorname{polylog}(T)$ factor, if we can achieve an accuracy-$\delta$ approximation using a circuit of size $T$ built from arbitrary $k$-qubit unitaries, then we can also achieve an accuracy-$(2\delta)$ approximation using a circuit of size $T\operatorname{polylog}(T/\delta)$ built from a finite gate set. Thus the criterion eq.(5.79) for reaching all unitaries to accuracy $\delta$ using circuits of size $T$ constructed from the finite gate set is replaced by
$$
T \operatorname{polylog}(T/\delta) \ge 2^{2n} \frac{\log(C/2\delta)}{\log n}.
$$ {#eq-5.87}
if we use circuits constructed from arbitrary $k$-qubit gates. The required circuit size is smaller than exponential by only a $\operatorname{poly}(n)$ factor. The group $U(2^n)$ is unimaginably vast not because we are limited to a discrete set of gates, but rather because we are unable to manipulate more than a constant number of qubits at a time.

### 5.4.2 Two-qubit gates are exactly universal

We will show in two steps that an arbitrary element of $U(2^n)$ can be achieved by a finite circuit of two-qubit gates. First we will show how to express an element of $U(N)$ as a product of “$2 \times 2$” unitaries; then we will show how to obtain any $2 \times 2$ unitary from a circuit of two-qubit unitaries.

What is a $2 \times 2$ unitary? Fix a standard orthonormal basis $\{|0\rangle, |1\rangle, |2\rangle, \dots |N - 1\rangle\}$ for an $N$-dimensional space. We say a unitary transformation $\boldsymbol{U}$ is $2 \times 2$ if it acts nontrivially only in the two-dimensional subspace spanned by two basis elements $|i\rangle$ and $|j\rangle$; that is, $\boldsymbol{U}$ decomposes

<!-- Page 37 -->
as a direct sum
$$
\boldsymbol{U} = \boldsymbol{U}^{(2)} \oplus \boldsymbol{I}^{(N-2)},
$$ {#eq-5.88}
where $\boldsymbol{U}^{(2)}$ is a $2 \times 2$ unitary matrix acting on the span of $|i\rangle$ and $|j\rangle$, and $\boldsymbol{I}^{(N-2)}$ is the identity matrix acting on the complementary $(N - 2)$-dimensional subspace.

We should be careful not to confuse a $2 \times 2$ unitary with a two-qubit unitary acting on the $n$-qubit space of dimension $N = 2^n$. A two-qubit unitary $\boldsymbol{U}$ decomposes as a tensor product
$$
\boldsymbol{U} = \boldsymbol{U}^{(4)} \otimes \boldsymbol{I}^{(2^{n-2})},
$$ {#eq-5.89}
where $\boldsymbol{U}^{(4)}$ is a $4 \times 4$ unitary matrix acting on a pair of qubits, and $\boldsymbol{I}^{(2^{n-2})}$ is the identity matrix acting on the remaining $n - 2$ qubits. We can regard the two-qubit unitary as a direct sum of $2^{n-2}$ $4 \times 4$ blocks, with each block labeled by a basis state of the $(n - 2)$-qubit Hilbert space, and $\boldsymbol{U}^{(4)}$ acting on each block.

Let’s see how to express $U \in U(N)$ as a product of $2 \times 2$ unitaries. Consider the action of $\boldsymbol{U}$ on the basis state $|0\rangle$:
$$
\boldsymbol{U}|0\rangle = \sum_{i=0}^{N-1} a_i |i\rangle.
$$ {#eq-5.90}
We can see that $\boldsymbol{U}|0\rangle$ can be written as $\boldsymbol{W}_0 |0\rangle$, where $\boldsymbol{W}_0$ is a product of $(N - 1)$ $2 \times 2$ unitaries which act as follows:
$$
\begin{aligned}
|0\rangle &\mapsto a_0 |0\rangle + b_0 |1\rangle, \\
b_0 |1\rangle &\mapsto a_1 |1\rangle + b_1 |2\rangle, \\
b_1 |2\rangle &\mapsto a_2 |2\rangle + b_2 |3\rangle, \\
&\ \ \vdots \\
b_{N-2} |N-2\rangle &\mapsto a_{N-2} |N-2\rangle + a_{N-1} |N-1\rangle.
\end{aligned}
$$ {#eq-5.91}
Next define $\boldsymbol{U}_1 = \boldsymbol{W}_0^{-1} \boldsymbol{U}$, and note that $\boldsymbol{U}_1 |0\rangle = |0\rangle$, so $\boldsymbol{U}_1$ acts nontrivially only in the $(N - 1)$-dimensional span of $\{|1\rangle, |2\rangle, \dots |N - 1\rangle\}$. By the same construction as above, we construct $\boldsymbol{W}_1$ as a product of $(N - 2)$ $2 \times 2$ unitaries such that $\boldsymbol{W}_1 |0\rangle = |0\rangle$ and $\boldsymbol{W}_1 |1\rangle = \boldsymbol{U}_1 |1\rangle$, then define $\boldsymbol{U}_2 = \boldsymbol{W}_1^{-1} \boldsymbol{U}_1$ such that $\boldsymbol{U}_2$ preserves both $|0\rangle$ and $|1\rangle$. Proceeding in this way we construct $\boldsymbol{W}_2, \boldsymbol{W}_3, \dots \boldsymbol{W}_{N-2}$ such that
$$
\boldsymbol{W}_{N-2}^{-1} \boldsymbol{W}_{N-3}^{-1} \dots \boldsymbol{W}_1^{-1} \boldsymbol{W}_0^{-1} \boldsymbol{U} = \boldsymbol{I};
$$ {#eq-5.92}
that is, we may express $\boldsymbol{U}$ as
$$
\boldsymbol{U} = \boldsymbol{W}_0 \boldsymbol{W}_1 \dots \boldsymbol{W}_{N-3} \boldsymbol{W}_{N-2},
$$ {#eq-5.93}

<!-- Page 38 -->
a product of $(N - 1) + (N - 2) + \dots + 2 + 1 = \frac{1}{2}N(N - 1)$ $2 \times 2$ unitaries.

Now it remains to show that we can construct any $2 \times 2$ unitary as a circuit of two-qubit unitaries. It will be helpful to notice that the three-qubit gate $\Lambda^2(\boldsymbol{U}^2)$ can be constructed as a circuit of $\Lambda(\boldsymbol{U})$, $\Lambda(\boldsymbol{U}^\dagger)$, and $\Lambda(\boldsymbol{X})$ gates. Using the notation
```
     |
  ---|---
     |
   +---+
   | U |
   +---+
     |
```
for the $\Lambda(\boldsymbol{U})$ gate, the circuit
```
x ───●───────────────●───────●─────── x
     │               │       │
y ───●───────●───┼───●───┼───│─────── y
     │       │   │   │   │   │
   +----+  +---+ │ +----+│ +---+
   |U^2 | =| U | │ | U† |│ | U |
   +----+  +---+ │ +----+│ +---+
                 ●───────●
```
does the job. We can check that the power of $\boldsymbol{U}$ applied to the third qubit is
$$
y - (x \oplus y) + x = y - (x + y - 2xy) + x = 2xy.
$$ {#eq-5.94}
That is, $\boldsymbol{U}^2$ is applied if $x = y = 1$, and the identity is applied otherwise; hence this circuit achieves the $\Lambda^2(\boldsymbol{U}^2)$ gate. Since every unitary $\boldsymbol{V}$ has a square root $\boldsymbol{U}$ such that $\boldsymbol{V} = \boldsymbol{U}^2$, the construction shows that, using two-qubit gates, we can achieve $\Lambda^2(\boldsymbol{V})$ for any single-qubit $\boldsymbol{V}$.

Generalizing this construction, we can find a circuit that constructs $\Lambda^m(\boldsymbol{U}^2)$ using $\Lambda^{m-1}(\boldsymbol{U})$, $\Lambda^{m-1}(\boldsymbol{X})$, $\Lambda(\boldsymbol{U})$, and $\Lambda(\boldsymbol{U}^\dagger)$ gates. If we replace the $\Lambda(\boldsymbol{X})$ gates in the previous circuit by $\Lambda^{m-1}(\boldsymbol{X})$ gates, and replace the last $\Lambda(\boldsymbol{U})$ gate by $\Lambda^{n-1}(\boldsymbol{U})$, then, if we denote the $m$ control bits by $x_1, x_2, x_3, \dots x_m$, the power of $\boldsymbol{U}$ applied to the last qubit is
$$
\begin{aligned}
&x_m + x_1 x_2 x_3 \dots x_{m-1} - (x_m \oplus x_1 x_2 x_3 \dots x_{m-1}) \\
&= x_m + x_1 x_2 x_3 \dots x_{m-1} - (x_m + x_1 x_2 x_3 \dots x_{m-1} - 2x_1 x_2 x_3 \dots x_{m-1} x_m) \\
&= 2x_1 x_2 x_3 \dots x_{m-1} x_m,
\end{aligned}
$$ {#eq-5.95}
where we have used the identity $x \oplus y = x + y - 2xy$. Now $\boldsymbol{U}^2$ is applied if $x_1 = x_2 = \dots = x_m = 1$ and the identity is applied otherwise; this circuit achieves the $\Lambda^m(\boldsymbol{U}^2)$ gate.

<!-- Page 39 -->
Using the construction recursively, we see that with two-qubit gates we can construct $\Lambda^2(\boldsymbol{V})$ for any $\boldsymbol{V}$, then with these gates and two-qubit gates we can construct $\Lambda^3(\boldsymbol{V})$ for any $\boldsymbol{V}$, which allows us to construct $\Lambda^4(\boldsymbol{V})$ for any $\boldsymbol{V}$ and so on. We have shown, therefore, how to construct the $n$-qubit gate $\Lambda^{n-1}(\boldsymbol{V})$ for any $\boldsymbol{V}$ using a circuit of two-qubit gates.

To complete the argument showing that any element of $U(2^n)$ is a product of two-qubit unitaries, it will suffice to show that arbitrary $2 \times 2$ unitaries can be constructed from $\Lambda^{n-1}(\boldsymbol{V})$ and two-qubit gates. Note that $\Lambda^{n-1}(\boldsymbol{V})$ is, in fact, a $2 \times 2$ unitary — it applies $\boldsymbol{V}$ in the two-dimensional space spanned by the two computational basis states
$$
\{|111\dots 110\rangle, \quad |111\dots 111\rangle\}.
$$ {#eq-5.96}
If we wish to apply $\boldsymbol{V}$ in the space spanned by computational states $\{|x\rangle, |y\rangle\}$ instead, we can use a permutation $\boldsymbol{\Sigma}$ of the computational basis states with the action
$$
\begin{aligned}
\boldsymbol{\Sigma} : \quad &|x\rangle \mapsto |111\dots 110\rangle, \\
&|y\rangle \mapsto |111\dots 111\rangle,
\end{aligned}
$$ {#eq-5.97}
constructing
$$
\boldsymbol{\Sigma}^{-1} \circ \Lambda^{n-1}(\boldsymbol{V}) \circ \boldsymbol{\Sigma}.
$$ {#eq-5.98}
This is to be read from right to left, with $\boldsymbol{\Sigma}$ acting first and $\boldsymbol{\Sigma}^{-1}$ acting last. But we have already seen in §5.2.2 how to construct an arbitrary permutation of computational basis states using $\Lambda^{n-1}(\boldsymbol{X})$ gates and (single-qubit) NOT gates, and we now know how to construct $\Lambda^{n-1}(\boldsymbol{X})$ (a special case of $\Lambda^{n-1}(\boldsymbol{U})$) from two-qubit gates. Therefore, using two-qubit gates, we have constructed the general $2 \times 2$ unitary (in the computational basis) as in eq.(5.98). That completes the proof that any element of $U(2^n)$ can be achieved by a circuit of two-qubit gates. In fact we have proven a somewhat stronger result: that the two-qubit gates $\{\Lambda(\boldsymbol{U})\}$, where $\boldsymbol{U}$ is an arbitrary single-qubit gate, constitute an exactly universal gate set.

### 5.4.3 Finite universal gate sets

*Denseness on the circle.* A finite gate set is universal if circuits constructed using that gate set are dense in $U(2^n)$. As a first simple example of denseness, consider the group $U(1)$ of rotations of the circle, e.g. the rotations of the Bloch sphere about the $\hat{z}$ axis:
$$
\left\{ \boldsymbol{U}(\theta) = \exp\left( i\frac{\theta}{2}\boldsymbol{\sigma}_3 \right), \quad \theta \in [0, 4\pi) \right\}.
$$ {#eq-5.99}

<!-- Page 40 -->
We claim that the positive integer powers of $\boldsymbol{U}(4\pi\alpha)$ are dense in $U(1)$ if $\alpha \in [0, 1)$ is irrational. Equivalently, the points
$$
\{n\alpha \pmod 1, \quad n = 1, 2, 3, \dots\}
$$ {#eq-5.100}
are dense in the unit interval.

To see why, first note that the points $\{n\alpha \pmod 1\}$ are all distinct, since $n\alpha = m\alpha + k$ for integers $k$ and $n \neq m$ would imply that $\alpha$ is a rational number $\alpha = k/(n - m)$. Now consider open intervals of width $\varepsilon$ centered on each of the $N$ points $\{n\alpha \pmod 1, n = 1, 2, 3, \dots, N\}$. For $N\varepsilon > 1$, at least two of these intervals must intersect — if all intervals were disjoint then their total length $N\varepsilon$ would exceed the length of the interval. Hence there exist distinct positive integers $n$ and $m$ less than $1/\varepsilon$ such that $|n - m|\alpha \pmod 1 < \varepsilon$; in other words, the positive integer $r = |n - m| < 1/\varepsilon$ satisfies $r\alpha \pmod 1 < \varepsilon$. Now the positive integer multiples of $r\alpha \pmod 1$ are equally spaced points on the unit interval separated by less than $\varepsilon$. Therefore, for sufficiently large $M$, the intervals of width $\varepsilon$ centered on the points $\{kr\alpha \pmod 1, k = 1, 2, 3, \dots, M\}$ fill the unit interval. Since $\varepsilon$ can be any positive real number, we conclude that the points $\{n\alpha \pmod 1, n = 1, 2, 3, \dots\}$ are dense in the interval.

*Powers of a generic gate.* Generalizing this argument, consider the positive integer powers of a generic element of $U(N)$. In a suitable basis, $\boldsymbol{U} \in U(N)$ is diagonal, with eigenvalues
$$
\{e^{i\theta_1/2}, e^{i\theta_2/2}, \dots, e^{i\theta_N/2}\}.
$$ {#eq-5.101}
Since rational numbers are countable and real numbers are not, for a generic $\boldsymbol{U}$ (that is, for all elements of $U(N)$ except for a set of measure zero) each $\theta_i/\pi$ and $\theta_i/\theta_j$ is an irrational number. For each positive integer $k$, the eigenvalues $\{e^{-ik\theta_i/2}, i = 1, 2, \dots, N\}$ of $\boldsymbol{U}^k$ define a point on the $N$-dimensional torus (the product of $N$ circles), and as $k$ ranges over all positive integers, these points densely fill the whole $N$-torus. We conclude that for any generic $\boldsymbol{U}$, the elements $\{\boldsymbol{U}^k, k = 1, 2, 3, \dots\}$ are dense in the group $U(1)^N$, i.e., come as close as we please to every unitary matrix which is diagonal in the same basis as $\boldsymbol{U}$.

Note that this argument does not provide any upper bound on how large $k$ must be for $\boldsymbol{U}^k$ to be $\varepsilon$-close to any specified element of $U(1)^N$. In fact, the required value of $k$ could be extremely large if, for some $m$ and $i$, $|m\theta_i \pmod{4\pi}| \ll \varepsilon$. It might be hard (that is, require many gates) to approximate a specified unitary transformation with circuits of commuting quantum gates, because the unitary achieved by the circuit only depends on how many times each gate is applied, not on the order in which the gates are applied. It is much easier (requires fewer gates) to achieve a good approximation using circuits of noncommuting gates.

<!-- Page 41 -->
If the gates are noncommuting, then the order in which the gates are applied matters, and many more unitaries can be reached by circuits of specified size than if the gates are noncommuting.

*Reaching the full Lie algebra.* Suppose we can construct the two gates $\boldsymbol{U} = \exp(i\boldsymbol{A}), \boldsymbol{V} = \exp(i\boldsymbol{B}) \in U(N)$, where $\boldsymbol{A}$ and $\boldsymbol{B}$ are $N \times N$ Hermitian matrices. If these are generic gates, positive powers of $\boldsymbol{U}$ come as close as we please to $e^{i\alpha\boldsymbol{A}}$ for any real $\alpha$ and positive powers of $\boldsymbol{V}$ come as close as we please to $e^{i\beta\boldsymbol{B}}$ for any real $\beta$. That is enough to ensure that there is a finite circuit constructed from $\boldsymbol{U}$ and $\boldsymbol{V}$ gates that comes as close as we please to $e^{i\boldsymbol{C}}$, where $\boldsymbol{C}$ is any Hermitian element of the Lie algebra generated by $\boldsymbol{A}$ and $\boldsymbol{B}$.

We say that a unitary transformation $\boldsymbol{U}$ is *reachable* if for any $\varepsilon > 0$ there is a finite circuit achieving $\tilde{\boldsymbol{U}}$ which is $\varepsilon$-close to $\boldsymbol{U}$ in the sup norm. Noting that
$$
\lim_{n\to\infty} (e^{i\alpha\boldsymbol{A}/n}e^{i\beta\boldsymbol{B}/n})^n = \lim_{n\to\infty} \left( 1 + \frac{i}{n}(\alpha\boldsymbol{A} + \beta\boldsymbol{B}) + O\left(\frac{1}{n^2}\right) \right)^n = e^{i(\alpha\boldsymbol{A} + \beta\boldsymbol{B})},
$$ {#eq-5.102}
we see that any $e^{i(\alpha\boldsymbol{A} + \beta\boldsymbol{B})}$ is reachable if each $e^{i\alpha\boldsymbol{A}/n}$ and $e^{i\beta\boldsymbol{B}/n}$ is reachable. Furthermore, because
$$
\lim_{n\to\infty} \left( e^{i\boldsymbol{A}/\sqrt{n}}e^{i\boldsymbol{B}/\sqrt{n}}e^{-i\boldsymbol{A}/\sqrt{n}}e^{-i\boldsymbol{B}/\sqrt{n}} \right)^n = \lim_{n\to\infty} \left( 1 - \frac{1}{n}(\boldsymbol{AB} - \boldsymbol{BA}) + O\left(\frac{1}{n^{3/2}}\right) \right)^n = e^{-[\boldsymbol{A}, \boldsymbol{B}]},
$$ {#eq-5.103}
we see that $e^{-[\boldsymbol{A}, \boldsymbol{B}]}$ is also reachable.

For example, positive integer powers of a generic element of $SU(2)$ allow us to reach a $U(1)$ subgroup; if we orient our axes on the Bloch sphere appropriately, this is the subgroup generated by the Pauli operator $\boldsymbol{Z}$. Positive integer powers of a second generic element of $SU(2)$ allow us to reach a different $U(1)$ subgroup, generated by $\tilde{\boldsymbol{X}} = \boldsymbol{X} + \gamma\boldsymbol{Z}$ (for some real $\gamma$) with an appropriate choice of axes. Because $[\boldsymbol{Z}, \boldsymbol{X}] = i\boldsymbol{Y}$, the elements $\{\boldsymbol{Z}, \tilde{\boldsymbol{X}}, -i[\boldsymbol{Z}, \tilde{\boldsymbol{X}}]\}$ span the three-dimensional $SU(2)$ Lie algebra. It follows that circuits built from any two generic elements of $SU(2)$ suffice to reach any element of $SU(2)$.

This observation applies to higher-dimensional Lie algebras as well. For example, the $SU(4)$ Lie algebra is 15 dimensional. It contains various lower-dimensional subalgebras, such as the Lie algebras of the $SU(4)$ subgroups $U(1)^3$, $SU(2) \times SU(2) \times U(1)$, $SU(3) \times U(1)$, etc. But two generic elements of the $SU(4)$ Lie algebra already suffice to general the full Lie algebra. The generated algebra closes on one of the lower-dimensional

<!-- Page 42 -->
subalgebras only if some nested commutators vanish “by accident,” a criterion satisfied by only a set of measure zero among all pairs of $SU(4)$ generators. Actually, as we have already noted, a generic element of $SU(4)$ allows us to reach the torus $U(1)^3$, and no nontrivial subgroup of $SU(4)$ contains two generic $U(1)^3$ subgroups. Therefore, circuits built from two generic two-qubit gates suffice to reach any two-qubit gate (up to an overall phase). And since we can reach any element of $U(2^n)$ with two-qubit gates, a pair of generic two-qubit gates provides a universal gate set, assuming we can apply the gates to any pair of qubits.

But in fact just one generic two-qubit gate is already enough, if we are free to choose not just the pair of qubits on which the gate acts but also the ordering of the qubits. That is, a generic two-qubit gate does not commute with the operator SWAP which interchanges the two qubits. If $\boldsymbol{U}$ is a generic two-qubit gate, then
$$
\boldsymbol{V} = \mathbf{SWAP} \circ \boldsymbol{U} \circ \mathbf{SWAP}
$$ {#eq-5.104}
(the same gate applied to the same two qubits, but in the opposite order) is another two-qubit gate not commuting with $\boldsymbol{U}$. Positive powers of $\boldsymbol{U}$ reach one $U(1)^3$ subgroup of $SU(4)$ while positive powers of $\boldsymbol{V}$ reach a different $U(1)^3$, so that circuits built from $\boldsymbol{U}$ and $\boldsymbol{V}$ reach all of $SU(4)$.

Even nongeneric universal gates, in particular gates whose eigenvalues are all rational multiples of $\pi$, can suffice for universality. One example discussed in the homework is the gate set $\{\mathrm{CNOT}, \boldsymbol{H}, \boldsymbol{T}\}$, where $\boldsymbol{H}$ rotates the Bloch sphere by the angle $\pi$ about the axis $\frac{1}{\sqrt{2}}(\hat{x} + \hat{z})$, and $\boldsymbol{T}$ rotates the Bloch sphere by the angle $\pi/4$ about the $\hat{z}$ axis. If we replaced $\boldsymbol{T}$ with the $\pi/2$ rotation $\boldsymbol{T}^2$, then the gate set would not be universal; in that case the only achievable single-qubit rotations would be those in a finite subgroup of $SU(2)$, the symmetry group of the cube. But $SU(2)$ has few such finite nonabelian subgroups (the only finite nonabelian subgroups of the rotation group $SO(3)$ are the symmetry groups of regular polygons and of regular three-dimensional polyhedra, the platonic solids). If the gate set reaches beyond these finite subgroups it will reach either a $U(1)$ subgroup of $SU(2)$ or all of $SU(2)$.

### 5.4.4 The Solovay-Kitaev approximation

Up until now our discussion of universal gates has focused on reachability and has ignored complexity. But when we have a finite universal gate set, we want to know not only *whether* we can approximate a desired unitary transformation to accuracy $\varepsilon$, but also *how hard* it is to achieve that approximation. How large a circuit suffices? The question really has two parts. (1) Given a unitary transformation $\boldsymbol{U}$, how large a quantum

<!-- Page 43 -->
circuit is needed to construct $\tilde{\boldsymbol{U}}$ such that $\|\tilde{\boldsymbol{U}} - e^{i\phi}\boldsymbol{U}\|_{\sup} \le \varepsilon$? (2) How large a classical circuit is needed to find the quantum circuit that achieves $\tilde{\boldsymbol{U}}$? We will see that, for any universal set of gates (closed under inverse) used to approximate elements of a unitary group of constant dimension, the answer to both questions is $\operatorname{polylog}(1/\varepsilon)$. We care about the answer to the second question because it would not be very useful to know that $\boldsymbol{U}$ can be well approximated by small quantum circuits if these circuits are very hard to find.

We will prove this result by devising a recursive algorithm which achieves successively better and better approximations. We say that a finite repertoire of unitary transformations $\mathcal{R}$ is an “$\varepsilon$-net” in $U(N)$ if every element of $U(N)$ is no more than distance $\varepsilon$ away (in the sup norm) from some element of $\mathcal{R}$, and we say that $\mathcal{R}$ is “closed under inverse” if the inverse of every element of $\mathcal{R}$ is also in $\mathcal{R}$. The key step of the recursive algorithm is to show that if $\mathcal{R}$ is an $\varepsilon$-net, closed under inverse, then we can construct a new repertoire $\mathcal{R}'$, also closed under inverse, with the following properties: (1) each element of $\mathcal{R}'$ is achieved by a circuit of at most 5 gates from $\mathcal{R}$. (2) $\mathcal{R}'$ is an $\varepsilon'$-net, where
$$
\varepsilon' = C\varepsilon^{3/2},
$$ {#eq-5.105}
and $C$ is a constant.

Before explaining how this step works, let’s see why it ensures that we can approximate any unitary using a quantum circuit with size polylogarithmic in the accuracy. Suppose to start with that we have found an $\varepsilon_0$-net $\mathcal{R}_0$, closed under inverse, where each element of $\mathcal{R}_0$ can be achieved by a circuit with no more than $L_0$ gates chosen from our universal gate set. If $\varepsilon_0 < 1/C^2$, then we can invoke the recursive step to find an $\varepsilon_1$-net $\mathcal{R}_1$, where $\varepsilon_1 < \varepsilon_0$, and each element of $\mathcal{R}_1$ can be achieved by a circuit of $L_1 = 5L_0$ gates. By repeating this step $k$ times, we can make the error $\varepsilon_k$ much smaller than the level-0 error $\varepsilon_0$. Iterating the relation
$$
C^2\varepsilon_k = (C^2\varepsilon_{k-1})^{3/2}
$$ {#eq-5.106}
$k$ times we obtain
$$
C^2\varepsilon_k = (C^2\varepsilon_0)^{(3/2)^k},
$$ {#eq-5.107}
and by taking logs of both sides we find
$$
\left(\frac{3}{2}\right)^k = \frac{\log(1/C^2\varepsilon_k)}{\log(1/C^2\varepsilon_0)}.
$$ {#eq-5.108}
After $k$ recursive steps the circuit size for each unitary in the $\varepsilon_k$-net $\mathcal{R}_k$

<!-- Page 44 -->
is no larger than $L_k$ where
$$
L_k / L_0 = 5^k = \left( \left(\frac{3}{2}\right)^k \right)^{\log 5 / \log(3/2)} = \left( \frac{\log(1/C^2\varepsilon_k)}{\log(1/C^2\varepsilon_0)} \right)^{\log 5 / \log(3/2)}.
$$ {#eq-5.109}
Thus the circuit size scales with the accuracy $\varepsilon_k$ as $[\log(1/\varepsilon_k)]^{3.97}$.

Now let’s see how the $\varepsilon'$-net $\mathcal{R}'$ is constructed from the $\varepsilon$-net $\mathcal{R}$. For any $\boldsymbol{U} \in SU(N)$ there is an element $\tilde{\boldsymbol{U}} \in \mathcal{R}$ such that $\|\boldsymbol{U} - \tilde{\boldsymbol{U}}\|_{\sup} \le \varepsilon$, or equivalently $\|\boldsymbol{U}\tilde{\boldsymbol{U}}^{-1} - \boldsymbol{I}\|_{\sup} \le \varepsilon$. Now we will find $\boldsymbol{W}$, constructed as a circuit of 4 elements of $\mathcal{R}$, such that $\|\boldsymbol{U}\tilde{\boldsymbol{U}}^{-1} - \boldsymbol{W}\|_{\sup} \le \varepsilon'$, or equivalently $\|\boldsymbol{U} - \boldsymbol{W}\tilde{\boldsymbol{U}}\|_{\sup} \le \varepsilon'$. Thus $\boldsymbol{U}$ is approximated to accuracy $\varepsilon'$ by $\boldsymbol{W}\tilde{\boldsymbol{U}}$, which is achieved by a circuit of 5 elements of $\mathcal{R}$.

We may write $\boldsymbol{U}\tilde{\boldsymbol{U}}^{-1} = e^{i\boldsymbol{A}}$, where $\boldsymbol{A} = O(\varepsilon)$. (By $\boldsymbol{A} = O(\varepsilon)$ we mean $\|\boldsymbol{A}\|_{\sup} = O(\varepsilon)$, i.e., $\|\boldsymbol{A}\|_{\sup}$ is bounded above by a constant times $\varepsilon$ for $\varepsilon$ sufficiently small.) It is possible to find Hermitian $\boldsymbol{B}, \boldsymbol{C}$, both $O(\varepsilon^{1/2})$, such that $[\boldsymbol{B}, \boldsymbol{C}] = -i\boldsymbol{A}$. Furthermore, because $\mathcal{R}$ is an $\varepsilon$-net, there is an element $e^{i\tilde{\boldsymbol{B}}}$ of $\mathcal{R}$ which is $\varepsilon$-close to $e^{i\boldsymbol{B}}$, and an element $e^{i\tilde{\boldsymbol{C}}}$ of $\mathcal{R}$ which is $\varepsilon$-close to $e^{i\boldsymbol{C}}$. It follows that $\boldsymbol{B} - \tilde{\boldsymbol{B}} = O(\varepsilon)$ and $\boldsymbol{C} - \tilde{\boldsymbol{C}} = O(\varepsilon)$.

Now we consider the circuit
$$
\boldsymbol{W} = e^{i\tilde{\boldsymbol{B}}} e^{i\tilde{\boldsymbol{C}}} e^{-i\tilde{\boldsymbol{B}}} e^{-i\tilde{\boldsymbol{C}}} = \boldsymbol{I} - [\tilde{\boldsymbol{B}}, \tilde{\boldsymbol{C}}] + O(\varepsilon^{3/2});
$$ {#eq-5.110}
the remainder term is cubic order in $\tilde{\boldsymbol{B}}$ and $\tilde{\boldsymbol{C}}$, hence $O(\varepsilon^{3/2})$. First note that the inverse of this circuit, $e^{i\tilde{\boldsymbol{C}}} e^{i\tilde{\boldsymbol{B}}} e^{-i\tilde{\boldsymbol{C}}} e^{-i\tilde{\boldsymbol{B}}}$, can also be constructed as a size-4 circuit of gates from $\mathcal{R}$. Furthermore,
$$
\begin{aligned}
\boldsymbol{W} &= \boldsymbol{I} - [\boldsymbol{B} + O(\varepsilon), \boldsymbol{C} + O(\varepsilon)] + O(\varepsilon^{3/2}) = \boldsymbol{I} + i\boldsymbol{A} + O(\varepsilon^{3/2}) \\
&= e^{i\boldsymbol{A}} + O(\varepsilon^{3/2});
\end{aligned}
$$ {#eq-5.111}
thus $\boldsymbol{W}$, a circuit of 4 gates from $\mathcal{R}$, approximates $\boldsymbol{U}\tilde{\boldsymbol{U}}^{-1}$ to $O(\varepsilon^{3/2})$ accuracy, as we wanted to show.

Finally, let’s consider the classical computational cost of finding the quantum circuit which approximates a unitary transformation. The classical algorithm receives a unitary transformation $\boldsymbol{U}$ as input, and produces as output a quantum circuit evaluating $\tilde{\boldsymbol{U}}$, which approximates $\boldsymbol{U}$ to accuracy $\varepsilon$. To improve the accuracy of the approximation to $\varepsilon'$, we need to call the accuracy-$\varepsilon$ algorithm three times, to find circuits evaluating $\tilde{\boldsymbol{U}}$, $e^{i\tilde{\boldsymbol{B}}}$, and $e^{i\tilde{\boldsymbol{C}}}$. Therefore, if the classical cost of the accuracy-$\varepsilon$ algorithm is $t$, the classical cost of the improved accuracy-$\varepsilon'$ algorithm is $t' = 3t + \text{constant}$, where the additive constant is needed to cover the cost

<!-- Page 45 -->
of tasks that do not scale with $\varepsilon$, such as finding the matrices $\boldsymbol{B}$ and $\boldsymbol{C}$ satisfying $[\boldsymbol{B}, \boldsymbol{C}] = -i\boldsymbol{A}$. After $k$ iterations, the classical cost scales like
$$
O(3^k) = O\left( \left[ \log(1/\varepsilon_k) \right]^{\log 3 / \log(3/2)} \right) = O\left( \left[ \log(1/\varepsilon_k) \right]^{2.71} \right),
$$ {#eq-5.112}
polylogarithmic in the accuracy achieved by the level-$k$ version of the algorithm.

What we have accomplished is a bit surprising. By composing unitary transformations with $O(\varepsilon)$ errors we have obtained unitary transformations with smaller $O(\varepsilon^{3/2})$ errors. How could we achieve such sharp results with such blunt tools? The secret is that we have constructed our circuit so that the $O(\varepsilon)$ errors cancel, leaving only the higher-order errors. This would not have worked if $\mathcal{R}$ had not been closed under inverse. If instead of the inverses of $e^{i\tilde{\boldsymbol{B}}}$ and $e^{i\tilde{\boldsymbol{C}}}$ we had been forced to use $O(\varepsilon)$ approximations to these inverses, the cancellations would not have occurred, and our quest for an improved approximation would have failed. But if our universal gate set allows us to construct the exact inverse of each element of the gate set, then we can use the Solovay-Kitaev approach to recursively improve the approximation.

This scheme works for any universal gate set that is closed under inverse. For particular gate sets improved approximations are possible. For example, the gate set $\{\boldsymbol{H}, \boldsymbol{T}\}$ can be used to approximate an arbitrary single-qubit unitary to accuracy $\varepsilon$ using $O(\log(1/\varepsilon))$ gates, a substantial improvement over $O([\log(1/\varepsilon)]^{3.97})$ established by the general argument, and the circuits achieving this improved overhead cost can be efficiently constructed.
