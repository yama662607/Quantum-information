# Section 5.3: Quantum Circuits [PDF Pages 22-32]

<!-- ============================================================ -->
<!-- Source: chap5.pdf, Physical Pages: 22-32                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 22 -->
## 5.3 Quantum Circuits

Now we are ready to formulate a mathematical model of a quantum computer. We will generalize the circuit model of classical computation to the quantum circuit model of quantum computation.

A classical computer processes bits. It is equipped with a finite set of gates that can be applied to sets of bits. A quantum computer processes qubits. We will assume that it too is equipped with a discrete set of fundamental components, called quantum gates. Each quantum gate is a unitary transformation that acts on a fixed number of qubits. In a quantum computation, a finite number $n$ of qubits are initially set to the value $|00\dots 0\rangle$. A circuit is executed that is constructed from a finite number of quantum gates acting on these qubits. Finally, an orthogonal measurement of all the qubits (or a subset of the qubits) is performed,

<!-- Page 23 -->
projecting each measured qubit onto the basis $\{|0\rangle, |1\rangle\}$. The outcome of this measurement is the result of the computation.

Several features of this model invite comment:

(1) *Preferred decomposition into subsystems.* It is implicit but important that the Hilbert space of the device has a preferred decomposition into a tensor product of low-dimensional subsystems, in this case the qubits. Of course, we could have considered a tensor product of, say, qutrits instead. But anyway we assume there is a natural decomposition into subsystems that is respected by the quantum gates — the gates act on only a few subsystems at a time. Mathematically, this feature of the gates is crucial for establishing a clearly defined notion of quantum complexity. Physically, the fundamental reason for a natural decomposition into subsystems is locality; feasible quantum gates must act in a bounded spatial region, so the computer decomposes into subsystems that interact only with their neighbors.

(2) *Finite instruction set.* Since unitary transformations form a continuum, it may seem unnecessarily restrictive to postulate that the machine can execute only those quantum gates chosen from a discrete set. We nevertheless accept such a restriction, because we do not want to invent a new physical implementation each time we are faced with a new computation to perform. (When we develop the theory of fault-tolerant quantum computing we will see that only a discrete set of quantum gates can be well protected from error, and we’ll be glad that we assumed a finite gate set in our formulation of the quantum circuit model.)

(3) *Unitary gates and orthogonal measurements.* We might have allowed our quantum gates to be trace-preserving completely positive maps, and our final measurement to be a POVM. But since we can easily simulate a TPCP map by performing a unitary transformation on an extended system, or a POVM by performing an orthogonal measurement on an extended system, the model as formulated is of sufficient generality.

(4) *Simple preparations.* Choosing the initial state of the $n$ input qubits to be $|00\dots 0\rangle$ is merely a convention. We might want the input to be some nontrivial classical bit string instead, and in that case we would just include NOT gates in the first computational step of the circuit to flip some of the input bits from 0 to 1. What is important, though, is that the initial state is easy to prepare. If we allowed the input state to be a complicated entangled state of the $n$ qubits, then we might be hiding the difficulty of executing the quantum algorithm in the difficulty of preparing the input state. We start with a product state instead, regarding it as uncontroversial that preparation of a product state is easy.

(5) *Simple measurements.* We might allow the final measurement to be a collective measurement, or a projection onto a different basis. But

<!-- Page 24 -->
any such measurement can be implemented by performing a suitable unitary transformation followed by a projection onto the standard basis $\{|0\rangle, |1\rangle\}^n$. Complicated collective measurements can be transformed into measurements in the standard basis only with some difficulty, and it is appropriate to take into account this difficulty when characterizing the complexity of an algorithm.

(6) *Measurements delayed until the end.* We might have allowed measurements at intermediate stages of the computation, with the subsequent choice of quantum gates conditioned on the outcome of those measurements. But in fact the same result can always be achieved by a quantum circuit with all measurements postponed until the end. (While we can postpone the measurements in principle, it might be very useful in practice to perform measurements at intermediate stages of a quantum algorithm.)

A quantum gate, being a unitary transformation, is reversible. In fact, a classical reversible computer is a special case of a quantum computer. A classical reversible gate
$$
x \to y = f(x),
$$ {#eq-5.48}
implementing a permutation of $k$-bit strings, can be regarded as a unitary transformation $U$ acting on $k$ qubits, which maps the "computational basis" of product states
$$
\{|x_i\rangle, i = 0, 1, \dots 2^k - 1\}
$$ {#eq-5.49}
to another basis of product states $\{|y_i\rangle\}$ according to
$$
U|x_i\rangle = |y_i\rangle.
$$ {#eq-5.50}
Since $U$ maps one orthonormal basis to another it is manifestly unitary. A quantum computation constructed from such reversible classical gates takes $|0\dots 0\rangle$ to one of the computational basis states, so that the outcome of the final measurement in the $\{|0\rangle, |1\rangle\}$ basis is deterministic.

There are four main issues concerning our model that we would like to address in this Chapter. The first issue is *universality*. The most general unitary transformation that can be performed on $n$ qubits is an element of $U(2^n)$. Our model would seem incomplete if there were transformations in $U(2^n)$ that we were unable to reach. In fact, we will see that there are many ways to choose a discrete set of universal quantum gates. Using a universal gate set we can construct circuits that compute a unitary transformation coming as close as we please to any element in $U(2^n)$.

Thanks to universality, there is also a machine independent notion of *quantum complexity*. We may define a new complexity class BQP

<!-- Page 25 -->
("bounded-error quantum polynomial time") — the class of languages that can be decided with high probability by polynomial-size uniform quantum circuit families. Since one universal quantum computer can simulate another efficiently, the class does not depend on the details of our hardware (on the universal gate set that we have chosen).

Notice that a quantum computer can easily simulate a probabilistic classical computer: it can prepare $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$ and then project to $\{|0\rangle, |1\rangle\}$, generating a random bit. Therefore BQP certainly contains the class BPP. But as we discussed in Chapter 1, it seems quite reasonable to expect that BQP is actually larger than BPP, because a probabilistic classical computer cannot easily simulate a quantum computer. The fundamental difficulty is that the Hilbert space of $n$ qubits is huge, of dimension $2^n$, and hence the mathematical description of a typical vector in the space is exceedingly complex.

Our second issue is to better characterize the resources needed to *simulate a quantum computer on a classical computer*. We will see that, despite the vastness of Hilbert space, a classical computer can simulate an $n$-qubit quantum computer even if limited to an amount of memory space that is polynomial in $n$. This means the BQP is contained in the complexity class PSPACE, the decision problems that can be solved with polynomial space, but may require exponential time. We also know that NP is contained in PSPACE, because we can determine whether a verifier $V(x, y)$ accepts the input $x$ for any witness $y$ by running the verifier for all possible witnesses. Though there are an exponential number of candidate witnesses to interrogate, each one can be checked in polynomial time and space.

The third important issue we should address is *accuracy*. The class BQP is defined formally under the idealized assumption that quantum gates can be executed with perfect precision. Clearly, it is crucial to relax this assumption in any realistic implementation of quantum computation. A polynomial size quantum circuit family that solves a hard problem would not be of much interest if the quantum gates in the circuit were required to have exponential accuracy. In fact, we will show that this is not the case. An idealized $T$-gate quantum circuit can be simulated with acceptable accuracy by noisy gates, provided that the error probability per gate scales like $1/T$.

The fourth important issue is *coverage*. We saw that polynomial-size classical circuits can reach only a tiny fraction of all Boolean functions, because there are many more functions than circuits. A similar issue arises for unitary transformations — the unitary group acting on $n$ qubits is vast, and there are not nearly enough polynomial-size quantum circuits to explore it thoroughly. Most quantum states of $n$ qubits can never

<!-- Page 26 -->
be realized in Nature, because they cannot be prepared using reasonable resources.

Despite this limited reach of polynomial-size quantum circuits, quantum computers nevertheless pose a serious challenge to the strong Church–Turing thesis, which contends that any physically reasonable model of computation can be simulated by probabilistic classical circuits with at worst a polynomial slowdown. We have good reason to believe that classical computers are unable in general to simulate quantum computers efficiently, in complexity theoretic terms that
$$
\text{BPP} \neq \text{BQP},
$$ {#eq-5.51}
yet this remains an unproven conjecture. Proving $\text{BPP} \neq \text{BQP}$ is a great challenge, and no proof should be expected soon. Indeed, a corollary would be
$$
\text{BPP} \neq \text{PSPACE},
$$ {#eq-5.52}
which would settle a long-standing and pivotal open question in classical complexity theory.

It might be less unrealistic to hope for a proof that $\text{BPP} \neq \text{BQP}$ follows from another standard conjecture of complexity theory such as $\text{P} \neq \text{NP}$, though no such proof has been found so far. The most persuasive evidence we have suggesting that $\text{BPP} \neq \text{BQP}$ is that there are some problems which *seem* to be hard for classical circuits yet can be solved efficiently by quantum circuits.

It seems likely, then, that the classification of complexity will be different depending on whether we use a classical computer or a quantum computer to solve problems. If such a separation really holds, it is the quantum classification that should be regarded as the more fundamental, for it is better founded on the physical laws that govern the universe.

### 5.3.1 Accuracy

Let's discuss the issue of accuracy. We imagine that we wish to implement a computation in which the quantum gates $\boldsymbol{U}_1, \boldsymbol{U}_2, \dots, \boldsymbol{U}_T$ are applied sequentially to the initial state $|\varphi_0\rangle$. The state prepared by our ideal quantum circuit is
$$
|\varphi_T\rangle = \boldsymbol{U}_T \boldsymbol{U}_{T-1} \dots \boldsymbol{U}_2 \boldsymbol{U}_1 |\varphi_0\rangle.
$$ {#eq-5.53}
But in fact our gates do not have perfect accuracy. When we attempt to apply the unitary transformation $\boldsymbol{U}_t$, we instead apply some "nearby" unitary transformation $\tilde{\boldsymbol{U}}_t$. If we wish to include environmental decoherence in our model of how the actual unitary deviates from the ideal

<!-- Page 27 -->
one, we may regard $\tilde{\boldsymbol{U}}_t$ as a transformation acting jointly on the system and environment, where the ideal unitary is a product $\boldsymbol{U}_t \otimes \boldsymbol{V}_t$, with $\boldsymbol{U}_t$ acting on the computer and $\boldsymbol{V}_t$ acting on the environment.

The errors cause the actual state of the computer to wander away from the ideal state. How far does it wander? After one step, the ideal state would be
$$
|\varphi_1\rangle = \boldsymbol{U}_1 |\varphi_0\rangle.
$$ {#eq-5.54}
But if the actual transformation $\tilde{\boldsymbol{U}}_1$ where applied instead the state would be
$$
\tilde{\boldsymbol{U}}_1 |\varphi_0\rangle = |\varphi_1\rangle + |E_1\rangle,
$$ {#eq-5.55}
where
$$
|E_1\rangle = (\tilde{\boldsymbol{U}}_1 - \boldsymbol{U}_1)|\varphi_0\rangle
$$ {#eq-5.56}
is an unnormalized vector. (We could also suppose that the initial state deviates from $|\varphi_0\rangle$, which would contribute an additional error to the computation that does not depend on the size of the circuit. We'll ignore that error because we are trying to understand how the error scales with the circuit size.)

Now, if $\tilde{\boldsymbol{U}}_t$ denotes the actual gate applied at step $t$, $|\tilde{\varphi}_t\rangle$ denotes the actual state after $t$ steps, and $|\varphi_t\rangle$ denotes the ideal state, then we may write
$$
\begin{aligned}
|\tilde{\varphi}_t\rangle &= \tilde{\boldsymbol{U}}_t |\tilde{\varphi}_{t-1}\rangle = \boldsymbol{U}_t |\varphi_{t-1}\rangle + (\tilde{\boldsymbol{U}}_t - \boldsymbol{U}_t)|\varphi_{t-1}\rangle + \tilde{\boldsymbol{U}}_t (|\tilde{\varphi}_{t-1}\rangle - |\varphi_{t-1}\rangle) \\
&= |\varphi_t\rangle + |E_t\rangle + \tilde{\boldsymbol{U}}_t (|\tilde{\varphi}_{t-1}\rangle - |\varphi_{t-1}\rangle),
\end{aligned}
$$ {#eq-5.57}
where $|E_t\rangle = (\tilde{\boldsymbol{U}}_t - \boldsymbol{U}_t)|\varphi_{t-1}\rangle$. Hence,
$$
\begin{aligned}
|\tilde{\varphi}_2\rangle &= \tilde{\boldsymbol{U}}_2 |\tilde{\varphi}_1\rangle = |\varphi_2\rangle + |E_2\rangle + \tilde{\boldsymbol{U}}_2 |E_1\rangle, \\
|\tilde{\varphi}_3\rangle &= \tilde{\boldsymbol{U}}_3 |\tilde{\varphi}_2\rangle = |\varphi_3\rangle + |E_3\rangle + \tilde{\boldsymbol{U}}_3 |E_2\rangle + \tilde{\boldsymbol{U}}_3 \tilde{\boldsymbol{U}}_2 |E_1\rangle,
\end{aligned}
$$ {#eq-5.58}
and so forth, and after $T$ steps we obtain
$$
|\tilde{\varphi}_T\rangle = |\varphi_T\rangle + |E_T\rangle + \tilde{\boldsymbol{U}}_T |E_{T-1}\rangle + \tilde{\boldsymbol{U}}_T \tilde{\boldsymbol{U}}_{T-1}|E_{T-2}\rangle + \dots + \tilde{\boldsymbol{U}}_T \tilde{\boldsymbol{U}}_{T-1} \dots \tilde{\boldsymbol{U}}_2 |E_1\rangle.
$$ {#eq-5.59}
Thus we have expressed the difference between $|\tilde{\varphi}_T\rangle$ and $|\varphi_T\rangle$ as a sum of $T$ remainder terms. The worst case yielding the largest deviation of $|\tilde{\varphi}_T\rangle$ from $|\varphi_T\rangle$ occurs if all remainder terms line up in the same direction, so that the errors interfere constructively. Therefore, we conclude that
$$
\begin{aligned}
\| |\tilde{\varphi}_T\rangle - |\varphi_T\rangle \| &\le \| |E_T\rangle \| + \| |E_{T-1}\rangle \| \\
&\quad + \dots + \| |E_2\rangle \| + \| |E_1\rangle \|,
\end{aligned}
$$ {#eq-5.60}

<!-- Page 28 -->
where we have used the property $\|\boldsymbol{U}|E_t\rangle\| = \||E_t\rangle\|$ for any unitary $\boldsymbol{U}$.

Let $\|\boldsymbol{A}\|_{\sup}$ denote the sup norm of the operator $\boldsymbol{A}$ — that is, the largest eigenvalue of $\sqrt{\boldsymbol{A}^\dagger \boldsymbol{A}}$. We then have
$$
\| |E_t\rangle \| = \| (\tilde{\boldsymbol{U}}_t - \boldsymbol{U}_t)|\varphi_{t-1}\rangle \| \le \| \tilde{\boldsymbol{U}}_t - \boldsymbol{U}_t \|_{\sup}
$$ {#eq-5.61}
(since $|\varphi_{t-1}\rangle$ is normalized). Now suppose that, for each value of $t$, the error in our quantum gate is bounded by
$$
\| \tilde{\boldsymbol{U}}_t - \boldsymbol{U}_t \|_{\sup} \le \varepsilon;
$$ {#eq-5.62}
then after $T$ quantum gates are applied, we have
$$
\| |\tilde{\varphi}_T\rangle - |\varphi_T\rangle \| \le T\varepsilon;
$$ {#eq-5.63}
in this sense, the accumulated error in the state grows linearly with the length of the computation.

The distance bounded in eq.(5.62) can equivalently be expressed as $\|\boldsymbol{W}_t - \boldsymbol{I}\|_{\sup}$, where $\boldsymbol{W}_t = \tilde{\boldsymbol{U}}_t \boldsymbol{U}_t^\dagger$. Since $\boldsymbol{W}_t$ is unitary, each of its eigenvalues is a phase $e^{i\theta}$, and the corresponding eigenvalue of $\boldsymbol{W}_t - \boldsymbol{I}$ has modulus
$$
|e^{i\theta} - 1| = (2 - 2\cos\theta)^{1/2},
$$ {#eq-5.64}
so that eq.(5.62) is the requirement that each eigenvalue satisfies
$$
\cos\theta > 1 - \varepsilon^2/2,
$$ {#eq-5.65}
(or $|\theta| \lesssim \varepsilon$, for $\varepsilon$ small). The origin of eq.(5.63) is clear. In each time step, $|\tilde{\varphi}\rangle$ rotates relative to $|\varphi\rangle$ by (at worst) an angle of order $\varepsilon$, and the distance between the vectors increases by at most of order $\varepsilon$.

How much accuracy is good enough? In the final step of our computation, we perform an orthogonal measurement, and the probability of outcome $a$, in the ideal case, is
$$
p(a) = |\langle a | \varphi_T \rangle|^2.
$$ {#eq-5.66}
Because of the errors, the actual probability is
$$
\tilde{p}(a) = |\langle a | \tilde{\varphi}_T \rangle|^2.
$$ {#eq-5.67}
It is shown in Exercise 2.5 that the $L^1$ distance between the ideal and actual probability distributions satisfies
$$
\frac{1}{2}\|\tilde{p} - p\|_1 = \frac{1}{2}\sum_a |\tilde{p}(a) - p(a)| \le \| |\tilde{\varphi}_T\rangle - |\varphi_T\rangle \| \le T\varepsilon.
$$ {#eq-5.68}

<!-- Page 29 -->
Therefore, if we keep $T\varepsilon$ fixed (and small) as $T$ gets large, the error in the probability distribution also remains fixed (and small).

If we use a quantum computer to solve a decision problem, we want the actual quantum circuit to get the right answer with success probability $\frac{1}{2} + \tilde{\delta}$, where $\tilde{\delta}$ is a positive constant. If the ideal quantum circuit contains $T$ gates and has success probability $\frac{1}{2} + \delta$, where $\delta > 0$, eq.(5.68) shows that $\tilde{\delta}$ is also positive provided $\varepsilon < \delta/T$. We should be able to solve hard problems using quantum computers as long as we can improve the accuracy of the gates linearly with the circuit size. This is still a demanding requirement, since performing very accurate quantum gates is a daunting challenge for the hardware builder. Fortunately, we will be able to show, using the theory of quantum fault tolerance, that *physical* gates with constant accuracy (independent of $T$) suffice to achieve *logical* gates acting on encoded quantum states with accuracy improving like $1/T$, as is required for truly scalable quantum computing.

### 5.3.2 BQP $\subseteq$ PSPACE

A randomized classical computer can simulate any quantum circuit if we grant the classical computer enough time and storage space. But how much memory does the classical computer require? Naively, since the simulation of an $n$-qubit circuit involves manipulating matrices of size $2^n$, it may seem that an amount of memory space exponential in $n$ is needed. But we will now show that the classical simulation of a quantum computer can be done to acceptable accuracy (albeit very slowly!) in polynomial space. This means that the quantum complexity class BQP is contained in the class PSPACE of problems that can be solved with polynomial space on a classical computer.

The object of the randomized classical simulation is to sample from a probability distribution that closely approximates the distribution of measurement outcomes for the specified quantum circuit. We will actually exhibit a classical simulation that performs a potentially harder task — estimating the probability $p(a)$ for each possible outcome $a$ of the final measurement, which can be expressed as
$$
p(a) = |\langle a | \boldsymbol{U} | 0 \rangle|^2,
$$ {#eq-5.69}
where
$$
\boldsymbol{U} = \boldsymbol{U}_T \boldsymbol{U}_{T-1} \dots \boldsymbol{U}_2 \boldsymbol{U}_1,
$$ {#eq-5.70}
is a product of $T$ quantum gates. Each $\boldsymbol{U}_t$, acting on the $n$ qubits, can be represented by a $2^n \times 2^n$ unitary matrix, characterized by the complex matrix elements
$$
\langle y | \boldsymbol{U}_t | x \rangle,
$$ {#eq-5.71}

<!-- Page 30 -->
where $x, y \in \{0, 1 \dots, 2^n - 1\}$. Writing out the matrix multiplication explicitly, we have
$$
\begin{aligned}
\langle a | \boldsymbol{U} | 0 \rangle = \sum_{\{x_t\}} &\langle a | \boldsymbol{U}_T | x_{T-1} \rangle \langle x_{T-1} | \boldsymbol{U}_{T-1} | x_{T-2} \rangle \dots \\
&\dots \langle x_2 | \boldsymbol{U}_2 | x_1 \rangle \langle x_1 | \boldsymbol{U}_1 | 0 \rangle.
\end{aligned}
$$ {#eq-5.72}
Eq.(5.72) is a sort of "path integral" representation of the quantum computation – the probability amplitude for the final outcome $a$ is expressed as a coherent sum of amplitudes for each of a vast number ($2^{n(T-1)}$) of possible computational paths that begin at 0 and terminate at $a$ after $T$ steps.

Our classical simulator is to add up the $2^{n(T-1)}$ complex numbers in eq.(5.72) to compute $\langle a | \boldsymbol{U} | 0 \rangle$. The first problem we face is that finite size classical circuits do integer arithmetic, while the matrix elements $\langle y | \boldsymbol{U}_t | x \rangle$ need not be rational numbers. The classical simulator must therefore settle for an approximate calculation to reasonable accuracy. Each term in the sum is a product of $T$ complex factors, and there are $2^{n(T-1)}$ terms in the sum. The accumulated errors are sure to be small if we express the matrix elements to $m$ bits of accuracy, with $m$ large compared to $nT \log T$. Therefore, we can replace each complex matrix element by pairs of signed integers — the binary expansions, each $m$ bits long, of the real and imaginary parts of the matrix element.

Our simulator will need to compute each term in the sum eq.(5.72) and accumulate a total of all the terms. But each addition requires only a modest amount of scratch space, and furthermore, since only the accumulated subtotal need be stored for the next addition, not much space is needed to sum all the terms, even though there are exponentially many.

So it only remains to consider the evaluation of a typical term in the sum, a product of $T$ matrix elements. We will require a classical circuit that evaluates
$$
\langle y | \boldsymbol{U}_t | x \rangle;
$$ {#eq-5.73}
this circuit receives the $2n$-bit input $(x, y)$, and outputs the $2m$-bit value of the (complex) matrix element. Given a circuit that performs this function, it will be easy to build a circuit that multiplies the complex numbers together without using much space.

This task would be difficult if $\boldsymbol{U}_t$ were an arbitrary $2^n \times 2^n$ unitary transformation. But now we may appeal to the properties we have demanded of our quantum gate set — the gates from a discrete set, and each gate acts on a bounded number of qubits. Because there are a fixed finite number of gates, there are only a fixed number of gate subroutines that our simulator needs to be able to call. And because the gate acts on only a few qubits, nearly all of its matrix elements vanish (when $n$ is large),

<!-- Page 31 -->
and the value $\langle y | \boldsymbol{U}_t | x \rangle$ can be determined (to the required accuracy) by a simple circuit requiring little memory.

For example, in the case of a single-qubit gate acting on the first qubit, we have
$$
\langle y_{n-1} \dots y_1 y_0 | \boldsymbol{U}_t | x_{n-1} \dots x_1 x_0 \rangle = 0 \text{ if } y_{n-1} \dots y_1 \neq x_{n-1} \dots x_1.
$$ {#eq-5.74}
A simple circuit can compare $x_1$ with $y_1$, $x_2$ with $y_2$, etc., and output zero if the equality is not satisfied. In the event of equality, the circuit outputs one of the four complex numbers
$$
\langle y_0 | \boldsymbol{U}_t | x_0 \rangle,
$$ {#eq-5.75}
to $m$ bits of precision. A simple classical circuit can encode the $8m$ bits of this $2 \times 2$ complex-valued matrix. Similarly, a simple circuit, requiring only space polynomial in $m$, can evaluate the matrix elements of any gate of fixed size.

We see, then, that a classical computer with memory space scaling like $nT \log T$ suffices to simulate a quantum circuit with $T$ gates acting on $n$ qubits. If we wished to consider quantum circuits with superpolynomial size $T$, we would need a lot of memory, but for a quantum circuit families with size $\mathrm{poly}(n)$, a polynomial amount of space is enough. We have shown that $\text{BQP} \subseteq \text{PSPACE}$.

But it is also evident that the simulation we have described requires exponential time, because we need to evaluate the sum of $2^{n(T-1)}$ complex numbers (where each term in the sum is a product of $T$ complex numbers). Though most of these terms vanish, there are still an exponentially large number of nonvanishing terms to sum.

### 5.3.3 Most unitary transformations require large quantum circuits

We saw that any Boolean function can be computed by an exponential-size classical circuit, and also that exponential-size circuits are needed to compute most functions. What are the corresponding statements about unitary transformations and quantum circuits? We will postpone for now consideration of how large a quantum circuit *suffices* to reach any unitary transformation, focusing instead on showing that exponential-size quantum circuits are *required* to reach most unitaries.

The question about quantum circuits is different than the corresponding question about classical circuits because there is a finite set of Boolean functions acting on $n$ input bits, and a continuum of unitary transformations acting on $n$ qubits. Since the quantum circuits are countable (if the quantum computer's gate set is finite), and the unitary transformations

<!-- Page 32 -->
are not, we can't reach arbitrary unitaries with finite-size circuits. We'll be satisfied to accurately *approximate* an arbitrary unitary.

As noted in our discussion of quantum circuit accuracy, to ensure that we have a good approximation in the $L^1$ norm to the probability distribution for any measurement performed after applying a unitary transformation, it suffices for the actual unitary $\tilde{U}$ to be close to the ideal unitary $U$ in the sup norm. Therefore we will say that $\tilde{U}$ is $\delta$-close to $U$ if $\|\tilde{U} - U\|_{\sup} \le \delta$. How large should the circuit size $T$ be if we want to approximate any $n$-qubit unitary to accuracy $\delta$?

If we imagine drawing a ball of radius $\delta$ (in the sup norm) centered at each unitary achieved by some circuit with $T$ gates, we want the balls to cover the unitary group $U(N)$, where $N = 2^n$. The number $N_{\text{balls}}$ of balls needed satisfies
$$
N_{\text{balls}} \ge \frac{\mathrm{Vol}(U(N))}{\mathrm{Vol}(\delta\text{-ball})},
$$ {#eq-5.76}
where $\mathrm{Vol}(U(N))$ means the total volume of the unitary group and $\mathrm{Vol}(\delta\text{-ball})$ means the volume of a single ball with radius $\delta$. The geometry of $U(N)$ is actually curved, but we may safely disregard that subtlety — all we need to know is that $U(N)$ contains a ball centered at the identity element with a small but constant radius $C$ (independent of $N$). Ignoring the curvature, because $U(N)$ has real dimension $N^2$, the volume of this ball (a lower bound on the volume of $U(N)$) is $\Omega_{N^2} C^{N^2}$, where $\Omega_{N^2}$ denotes the volume of a unit ball in flat space; likewise, the volume of a $\delta$-ball is $\Omega_{N^2}\delta^{N^2}$. We conclude that
$$
N_{\text{balls}} \ge \left(\frac{C}{\delta}\right)^{N^2}.
$$ {#eq-5.77}

On the other hand, if our universal set contains a constant number of quantum gates (independent of $n$), and each gate acts on no more than $k$ qubits, where $k$ is a constant, then the number of ways to choose the quantum gate at step $t$ of a circuit is no more than $\text{constant} \times \binom{n}{k} = \mathrm{poly}(n)$. Therefore the number $N_T$ of quantum circuits with $T$ gates acting on $n$ qubits is
$$
N_T \le (\mathrm{poly}(n))^T.
$$ {#eq-5.78}
We conclude that if we want to reach every element of $U(N)$ to accuracy $\delta$ with circuits of size $T$, hence $N_T \ge N_{\text{balls}}$, we require
$$
T \ge 2^{2n} \frac{\log(C/\delta)}{\log(\mathrm{poly}(n))};
$$ {#eq-5.79}
the circuit size must be exponential. With polynomial-size quantum circuits, we can achieve a good approximation to unitaries that occupy only an exponentially small fraction of the volume of $U(2^n)$!

<!-- Page 33 -->
Reaching any desired quantum state by applying a suitable quantum circuit to a fixed initial (e.g., product) state is easier than reaching any desired unitary, but still hard, because the volume of the $2^n$-dimensional $n$-qubit Hilbert space is exponential in $n$. Hence, circuits with size exponential in $n$ are required. Future quantum engineers will know the joy of exploring Hilbert space, but no matter how powerful their technology, most quantum states will remain far beyond their grasp. It's humbling.
