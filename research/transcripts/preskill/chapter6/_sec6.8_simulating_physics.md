# Section 6.8: Using quantum computers to simulate quantum physics

## Transcript (English Original)

### 6.8 Using quantum computers to simulate quantum physics [chap6.pdf#page=41]

Sadly, we now know some things that quantum computers cannot do. But happily, there are also some important things that they can do.

- They can solve the hidden subgroup problem for finitely generated abelian groups, with an exponential speedup (in the oracle model) relative to classical algorithms.
- They can speed up, quadratically, exhaustive search for solutions to combinatorial problems.

What else can they do?

#### 6.8.1 Simulating time evolution of local Hamiltonians [chap6.pdf#page=41]

An important application for quantum computers is simulating the time evolution of quantum systems. The simulation is efficient if the Hamiltonian $H$ is local.

For a system of $n$ qubits, we say that $H$ is $k$-local if
$$
H = \sum_a H_a,
$$ (6.187)
where each term $H_a$ acts non-trivially on at most $k$ qubits — i.e. $H_a = \tilde{H}_a \otimes I^{n-k}$, and $\tilde{H}_a$ acts on some set of at most $k$ qubits. (Of course, we may use a similar definition for a system of $d$-dimensional subsystems for constant $d > 2$, rather than qubits.) We say that $H$ is local if it is $k$-local for some constant $k$.

There is a stronger notion of locality we sometimes use, which can be called geometrical locality or spatial locality. A $k$-local Hamiltonian is geometrically local in $D$ dimensions if the qubits can be arranged in (flat) $D$-dimensional space with a bounded number of qubits per unit volume, and the $k$ qubits upon which $H_a$ acts non-trivially are all contained in a ball of constant radius. In this sense there are no long-range interactions among the qubits. $H$ is geometrically local if it is geometrically $k$-local in $D$ dimensions for some constant $D$ and $k$.

If we write $H = \sum_a H_a$ where there is a unique $H_a$ for each set of $k$ qubits, then the expansion of a $k$-local $H$ contains at most $\binom{n}{k} = O(n^k)$ terms, and the expansion of a geometrically local $H$ contains $O(n)$ terms (each of the $n$ qubits is contained in a constant number of interacting sets). Let us also assume that each $H_a$ is bounded
$$
\|H_a\|_\infty \le h \quad \text{for all } a, \text{ where } h \text{ is a constant}.
$$ (6.188)

[chap6.pdf#page=42]
Physicists are interested in geometrically local Hamiltonians because they seem to provide an accurate description of Nature. Therefore, it is noteworthy that quantum circuits can simulate quantum evolution governed by a local Hamiltonian efficiently: evolution of $n$ qubits for time $t$ can be simulated to constant accuracy using a circuit whose size is polynomial in $n$ and $t$.

We can formulate the problem this way: suppose we are given an initial quantum state $|\psi(0)\rangle$, or a classical description of a quantum circuit that prepares the state. Our goal is to construct
$$
|\psi(t)\rangle = U(t)|\psi(0)\rangle
$$ (6.189)
where $U(t)$ satisfies $\frac{d}{dt}U(t) = -iH(t)U(t)$ and the boundary condition $U(0) = I$. (Thus $U(t) = e^{-iHt}$ in the case where $H$ is time independent). We will settle for computing $|\psi(t)\rangle$ to accuracy $\delta$, i.e. constructing $|\tilde{\psi}(t)\rangle$ where
$$
\||\tilde{\psi}(t)\rangle - |\psi(t)\rangle\| < \delta.
$$ (6.190)
Depending on the situation, we might be satisfied if $\delta$ is a sufficiently small constant, or we might impose the stricter requirement that the error is smaller than some specified power of the size $n$ of the system. To relate this simulation task to a task that can be described classically, suppose the goal is to sample from the probability distribution
$$
\langle\psi(t)|\Pi_a|\psi(t)\rangle
$$ (6.191)
where $\Pi_a$ projects onto an eigenstate with eigenvalue $a$ of an observable $A$ that can be measured efficiently by a quantum computer. Classically this task is believed to be hard at least in some cases, because the unitary matrix $U(t)$ is exponentially large ($2^n \times 2^n$). But quantumly we can do the simulation efficiently if $H$ is a local Hamiltonian.

To simulate continuous time evolution on a classical or quantum computer, we choose a small step size $\Delta$, and approximate evolution for time $t$ by a sequence of $t/\Delta$ steps. (If $H$ is actually time dependent, assume $\Delta$ is small enough that the change of $H$ during a time interval of width $\Delta$ can be neglected.) We wish to attain accuracy
$$
\|\tilde{U}(t) - U(t)\|_\infty < \delta,
$$ (6.192)
where $\tilde{U}$ is the simulated unitary and $U$ is the ideal unitary. Hence the error per time step should be less than $\delta\Delta/t$.

Suppose $H = \sum_a H_a$ is a sum of $M$ $k$-local terms, and let's consider the geometrically local case, where $M = O(n)$. We will show below that a single time step can be simulated by a product of $M$ local "gates" (unitary transformations that act on a constant number of qubits) where each such "gate" has an error $O(\Delta^2 h^2)$. Therefore the simulation of evolution for time $t$ uses all together $Mt/\Delta$ gates where we require
$$
\frac{Mt}{\Delta}\Delta^2 h^2 \approx \delta \implies \Delta = O\left(\frac{\delta}{h^2 Mt}\right).
$$ (6.193)
Therefore the total number of gates is
$$
L = O\left(\frac{h^2(Mt)^2}{\delta}\right).
$$ (6.194)
Furthermore each "gate" can be simulated to accuracy $O(\Delta^2 h^2)$ with a universal gate [chap6.pdf#page=43] set using $\mathrm{polylog}\left(\frac{1}{\Delta^2 h^2}\right) = \mathrm{polylog}\left(\frac{h^2(Mt)^2}{\delta^2}\right)$ gates, according to the Solovay-Kitaev theorem. We conclude that the simulation can be done with a quantum circuit of size
$$
L = O\left(\frac{h^2(Mt)^2}{\delta}\mathrm{polylog}\left(\frac{h^2(Mt)^2}{\delta^2}\right)\right).
$$ (6.195)
In the case where $H$ is geometrically local, $M = O(n) = O(V)$, where $V$ is the spatial volume of the system. Since $h$ is a constant, we find that the cost of simulating time evolution with fixed accuracy scales like
$$
L = O(\Omega^2 \mathrm{polylog}\,\Omega),
$$ (6.196)
where $\Omega = Vt$ is the simulated volume of spacetime.

Now we need to explain how to simulate a single time step. We'll use the idea that $\exp\left(\sum_a A_a\right)$ can be approximated by $\prod_a \exp(A_a)$ if $\|A\| \ll 1$. To check the accuracy we expand the exponentials:
$$
\begin{aligned}
\exp\left(\sum_a A_a\right) - \prod_a \exp(A_a) &= \left(1 + \sum_a A_a + \frac{1}{2}\sum_{a,b} A_a A_b + \dots\right) - \prod_a \left(1 + A_a + \frac{1}{2}A_a^2 + \dots\right) \\
&= \left(1 + \sum_a A_a + \frac{1}{2}\sum_{a,b} A_a A_b + \dots\right) - \left(1 + \sum_a A_a + \sum_a \frac{1}{2}A_a^2 + \sum_{a<b} A_a A_b + \dots\right) \\
&= \frac{1}{2}\left(\sum_{a<b} A_a A_b + \sum_{a<b} A_b A_a\right) - \sum_{a<b} A_a A_b + \dots \\
&= -\frac{1}{2}\sum_{a<b} [A_a, A_b] + \dots
\end{aligned}
$$ (6.197)
(where $+ \dots$ denotes terms higher order in $A_a$). Writing $H = \sum_a H_a$, then, we find that
$$
e^{-iH\Delta} - \prod_a e^{-iH_a\Delta} = \frac{1}{2}\Delta^2 \sum_{a<b} [H_a, H_b] + \text{h.o.}
$$ (6.198)
Now, how many non-vanishing commutators $\{[H_a, H_b]\}$ can occur in this sum? Let's suppose the Hamiltonian is geometrically local, in which case there are $O(n)$ terms in $H$, and each term fails to commute with a constant number of terms. So, there are $O(n) = O(M)$ non-vanishing commutators. We conclude that (in the geometrically local case)
$$
\left\|e^{-iH\Delta} - \prod_a e^{-iH_a\Delta}\right\| = O(M\Delta^2 h^2).
$$ (6.199)
Since $\prod_a e^{-iH_a\Delta}$ is a product of $M$ "gates," we have verified that the accuracy per gate is $O(\Delta^2 h^2)$ (Note that terms arising from the higher-order terms in the expansion of the exponential are of order $M\Delta^3 h^3$, and therefore systematically suppressed by another factor of $\Delta h = O(\delta/hMt) = O((\delta/L)^{1/2})$.)

So far we have shown that, for a geometrically local $H$ that is a sum of bounded terms, evolution in a spacetime volume $\Omega$ can be achieved with a quantum circuit of size
$$
L = O(\Omega^2 \mathrm{polylog}\,\Omega).
$$ (6.200)

[chap6.pdf#page=44]
The resources needed for the simulation scale like the square of the simulated volume (up to a log factor). Can this be improved?

An improved approximation to $\exp\left(\sum_a A_a\right)$ is the subject of an exercise. Instead of $\prod_a e^{A_a}$ we use $\prod_{a\to} e^{\frac{1}{2}A_a} \prod_{a\leftarrow} e^{\frac{1}{2}A_a}$, where $\prod_{a\to}$ denotes the product in ascending order, and $\prod_{a\leftarrow}$ denotes the product in descending order. The exercise shows that, for geometrically local $H$,
$$
\left\|e^{-iH\Delta} - \prod_{a\to} e^{\frac{1}{2}H_a\Delta} \prod_{a\leftarrow} e^{\frac{1}{2}H_a\Delta}\right\| = O(M\Delta^3 h^3),
$$ (6.201)
i.e. the error per gate is $O(h^3\Delta^3)$ instead of $O(h^2\Delta^2)$. For an accurate simulation, we choose
$$
\frac{Mt}{\Delta}(\Delta^3 h^3) \approx \delta \implies \Delta \approx \left(\frac{\delta}{h^3 Mt}\right)^{1/2};
$$ (6.202)
the number of gates is
$$
\frac{Mt}{\Delta} \approx \frac{h^{3/2}(Mt)^{3/2}}{\delta^{1/2}},
$$ (6.203)
and the Solovay-Kitaev blowup factor is $\mathrm{polylog}\left(\frac{1}{\Delta^3 h^3}\right) = \mathrm{polylog}\left(\frac{h^{3/2}(Mt)^{3/2}}{\delta^{3/2}}\right) = \mathrm{polylog}\left(\frac{hMt}{\delta}\right)$. We conclude that spacetime volume $\Omega$ can be simulated with a circuit of size
$$
L = O(\Omega^{3/2}\mathrm{polylog}\,\Omega).
$$ (6.204)
The improved approximation in each time step increases the circuit size by only a factor of 2.

The accuracy of this Trotter-Suzuki approximation to $e^{-iH\Delta}$ can be improved further, so that
$$
\|e^{-iH\Delta} - \text{approximation}\| = O\left(c_p M (h\Delta)^{p+1}\right)
$$ (6.205)
where $p$ is any power, the constant $c_p$ depends on $p$, and the improved approximation increases the number of gates by a factor that depends on $p$. With this approximation, we choose
$$
\frac{Mt}{\Delta}(h\Delta)^{p+1} \approx \delta \implies \Delta \approx \frac{\delta^{1/p}}{h^{(p+1)/p}(Mt)^{1/p}},
$$ (6.206)
so that the number of gates is
$$
\frac{Mt}{\Delta} \approx \frac{h^{(p+1)/p}(Mt)^{(p+1)/p}}{\delta^{1/p}}.
$$ (6.207)
Including the Solovay-Kitaev log factor, we can do the simulation with a circuit of size
$$
L = O(\Omega^{1+\epsilon}\mathrm{polylog}\,\Omega),
$$ (6.208)
where $\epsilon = 1/p$. In fact, though, the factor $c_p$ grows exponentially with $p = 1/\epsilon$; this happens because each time we increase the value of $p$ by 1, we pay the price of increasing the circuit size by a constant factor. But anyway, as we systematically improve the approximation, the circuit size comes closer and closer to scaling linearly with the simulated volume, though it never quite makes it. Somehow, Nature manages to simulate herself with "resources" scaling like $\Omega$ (and without any error!), but this approximation method using a universal quantum computer does not do quite as well. There are other simulation methods that more nearly match the scaling Nature achieves.

[chap6.pdf#page=45]
Whether the quantum circuit model can simulate Nature efficiently is an important issue, because it addresses whether this model is the right one for studying what problems can be solved with reasonable resources by computers that are in principle physically realizable. We believe that the classical Turing machine model is not the right model, because it seems to be incapable of efficiently simulating general quantum systems, even ones for which the Hamiltonian is geometrically local. The quantum circuit model is presumably stronger, but is it really strong enough?

Particle physicists model fundamental physics using quantum field theory (QFT). Some predictions of QFT can be computed classically, and the success of such predictions provides the evidence that QFT is a good model. But we don't know how to efficiently simulate on a classical computer the real-time evolution of, for example, nuclear matter governed by quantum chromodynamics. Can we do such simulations efficiently on a quantum computer?

The question is subtle because the number of qubits per unit volume is formally infinite in QFT (there are degrees of freedom at arbitrarily small distances) and although the Hamiltonian is local, the terms in the Hamiltonian do not necessarily have bounded norm. On the other hand, in a physical process of interest, we can usually assume that the energy density per unit volume is bounded above. In that case, we expect that the very-short-distance degrees of freedom are not so relevant, so that we can attain reasonable accuracy by approximating continuous space with a finite density of lattice points per unit volume, and that furthermore the terms in the local Hamiltonian can be well approximated by operators with bounded norm. A reasonable expectation is that the complexity of a simulation of the dynamics scales polynomially in $\Omega\rho_{\max} = (Vt\rho_{\max}) = E_{\max}t$ where $\rho_{\max}$ is the maximal energy per unit volume, and $E_{\max}$ is an upper bound on the total energy. But there is no rigorous theorem establishing such scaling. Though physicists have a pretty good grasp of the properties of QFT (as indicated by the agreement between theory and experimental data), rigorous mathematical results pertaining to QFT are still quite technical and incomplete, particularly in three spatial dimensions (where we live).

Our understanding is even less satisfactory for physical processes in which gravitational effects are important. Can the quantum circuit model simulate quantum gravity efficiently? If so, quantum computers may turn out to be a powerful tool for deepening our understanding of quantum gravity. If not, then we still have not found the computational model that fully captures the computational power that is potentially realizable in Nature.

#### 6.8.2 Estimating energy eigenvalues and preparing energy eigenstates [chap6.pdf#page=45]

We have argued that a quantum computer can efficiently simulate the time evolution of a quantum system with a local Hamiltonian; i.e., it can solve the time-dependent Schroedinger equation. Another thing that physicists and chemists want to do is solve the time-independent Schroedinger equation; i.e., compute the energy eigenvalues of a Hamiltonian. For example, chemists say that estimating the ground state energy of a molecule to "chemical accuracy" (about one part in a million) is valuable for predicting the properties of chemical reactions. In general, finding the energy eigenvalues of a local Hamiltonian seems to be a hard problem classically because we need to diagonalize a $2^n \times 2^n$ matrix for a system of $n$ qubits. In some cases this may be easy, for example [chap6.pdf#page=46] if the matrix is very sparse and has a simple structure, but in some physically relevant cases efficient classical algorithms are not known.

Sometimes, if we express $H$ in a "natural" basis we find that all the off-diagonal terms in the matrix are non-positive, i.e.
$$
H = cI - h
$$ (6.209)
where $I$ is the identity and $h$ has only non-negative entries. In that case, the ground state $|\psi_0\rangle$ of $H$ (the eigenvector with the lowest eigenvalue) can be expressed as $|\psi_0\rangle = \sum_i c_i |i\rangle$ where $|i\rangle$ is a basis element and all $c_i$ can be chosen non-negative. That is because $|\psi_0\rangle$ maximizes
$$
\langle\psi_0|h|\psi_0\rangle = \sum c_i^* c_j h_{ij}
$$ (6.210)
and so it is optimal to choose $c_i^* c_j \ge 0$ for all $i$ and $j$. When all the $c_i$ are nonnegative, there are quantum Monte Carlo sampling algorithms that can find the $\{c_i\}$ efficiently and accurately in practice. But if the off-diagonal terms in $H$ have both $+$ and $-$ signs, then sampling algorithms might not work well because there can be delicate cancellations between positive and negative terms contributing to $\langle\psi_0|h|\psi_0\rangle$. Computational physicists call this the sign problem.

But on a quantum computer, we can estimate eigenvalues of a unitary matrix $U$ using the phase estimation algorithm. To obtain $m$ bits of accuracy, we prepare an $m$-qubit register in a uniform superposition state, and execute this circuit:

-figure-

The measured value of $k$ provides an estimate of the eigenvalue to $m$ bits of accuracy. To perform $U^t$ conditioned on $t$ we simulate $e^{-iHt}$ for $t \in T \times \{1, 2, 4, 8, \dots 2^{m-1}\}$. This suffices to find the fractional part of $\frac{ET}{2\pi}$ to $m$-bit accuracy, where $E$ is an eigenvalue of the Hamiltonian $H$. We choose the step size in the simulation of $e^{-iHt}$ so that the accuracy is $\delta \approx 2^{-m}$ for $t = 2^m T$. If the Hamiltonian is geometrically local, we have seen that this approximation can be achieved with a circuit size (neglecting a log factor)
$$
L = O\left(\frac{h^2(nt)^2}{\delta}\right) = O\left(h^2(nT)^2 \times \frac{2^{2m}}{2^{-m}}\right) = O\left((hT)^2 n^2 2^{3m}\right).
$$ (6.211)

For a particular preparation of the input state $|\psi\rangle$, suppose we repeat the computation many times, and plot a histogram of the results:

-figure-

The location of each narrow peak estimates an energy eigenvalue $E_a$, modulo $2\pi/T$. The height of the peak estimates $|\langle E_a|\psi\rangle|^2$ — the overlap $|\psi\rangle$ with the corresponding energy eigenstate $|E_a\rangle$. To compute the energy eigenvalue to accuracy polynomial in $n$, we choose
$$
\delta \approx 2^{-m} \approx 1/n^c \implies m = c \log_2 n.
$$ (6.212)

[chap6.pdf#page=47]
The algorithm is efficient: the quantum circuit size is
$$
O\left(2^{3m} h^2(nT)^2\right) = O(n^{3c} n^2).
$$ (6.213)

However, if we want to estimate (say) the ground state energy $E_0$ to polynomial accuracy in quantum polynomial time, we must be able to prepare a state $|\psi\rangle$ whose overlap with the ground state $|E_0\rangle$ is no worse than polynomially small:
$$
|\langle E_0|\psi\rangle|^2 > 1/\mathrm{poly}(n).
$$ (6.214)
If that is the case, we can get a good estimate of $E_0$ in only polynomially many trials. As a bonus, when we obtain the value $E_0$ for the measured eigenvalue $E_0$, then we have projected state $|\psi\rangle$ onto the ground state $|E_0\rangle$, and therefore we can compute further properties of $|E_0\rangle$, such as the distribution $\mathrm{Prob}(a) = \langle E_0|\Pi_a|E_0\rangle$, where $\Pi_a$ is projector onto eigenspace of an efficiently measurable observable.

The catch is that the overlap of a randomly chosen $n$-qubit state with $|E_0\rangle$ is exponentially small, so preparing $|\psi\rangle$ with a polynomially small overlap is not necessarily easy. One way we might attempt to construct a state with a significant overlap with the ground state is by appealing to the quantum adiabatic theorem. We prepare the ground state of a Hamiltonian $H_{\mathrm{easy}}$ whose ground state is easy to find classically. Then we simulate Schroedinger evolution governed by a time-dependent Hamiltonian $H(t)$ such that
$$
H(0) = H_{\mathrm{easy}}, \quad H(T) = H_{\mathrm{hard}}, \quad 0 \le t \le T,
$$ (6.215)
where $H_{\mathrm{hard}}$ is the Hamiltonian whose ground state we wish to construct. For example, we might choose
$$
H(t) = (1 - t/T)H_{\mathrm{easy}} + (t/T)H_{\mathrm{hard}}.
$$ (6.216)

The quantum adiabatic theorem says that if $|\psi(0)\rangle$ has a large overlap with the ground state of $H_{\mathrm{easy}}$, then $|\psi(T)\rangle$ has a large overlap with the ground state of $H_{\mathrm{hard}}$, if $T$ is long enough (i.e. the Hamiltonian $H(t)$ changes slowly enough). But how slow is slow enough? Let $E_0(t)$ denote the energy of the ground state of $H(t)$ and let $E_1(t)$ denote the energy of the first excited state of $H(t)$. Define $\Delta = \min_{t\in[0,T]} (E_1(t) - E_0(t))$; we say $\Delta$ is the minimum energy gap between the ground and first excited state. Then the adiabatic theorem says that $T > A/\Delta^c$ is slow enough, where $A$ and $c$ are constants independent of the number of qubits $n$. Therefore, we have a complete polynomial algorithm for computing the ground state energy of a local Hamiltonian to polynomial accuracy in polynomial time provided that
$$
\Delta = \frac{1}{\mathrm{poly}(n)}.
$$ (6.217)
But if $\Delta$ becomes exponentially small in $n$ during the evolution in which $H(t)$ interpolates between $H_{\mathrm{easy}}$ and $H_{\mathrm{hard}}$, then this algorithm may require exponential time.

Unfortunately, we'll see that it follows from weak complexity-theoretic assumptions that there are local Hamiltonians for which computing ground state energy is hard even for a quantum computer. (For example, otherwise we would be able to solve efficiently any problem in NP using a quantum computer, which seems unlikely.) So the minimum energy gap $\Delta$ must be smaller than polynomially small in such cases.

On the other hand, it is reasonable to be hopeful that computing ground state energy for quantum systems will be an important application of quantum computing. For example, as previously noted, chemists say it is valuable to compute the energy of the [chap6.pdf#page=48] electronic ground state of a molecule with atomic nuclei at fixed positions to accuracy $\approx 10^{-6}$ (chemical accuracy). They also claim that it is an adequate approximation to express
$$
H = \sum_{a=1}^M H_a
$$ (6.218)
and each $H_a$ acts on $\le 4$ basis functions. Hence this Hamiltonian is local. Furthermore, chemists assert (without proof) that it is possible to evolve adiabatically from the Hartree-Fock Hamiltonian (which they can solve classically) to the full configuration interaction (FCI) Hamiltonian (which they want to solve, but don't know how to solve classically in general) while the gap satisfies $\Delta \ge \text{constant}$. If that is true, quantum computers are likely to be a powerful tool for studying molecular chemistry.
