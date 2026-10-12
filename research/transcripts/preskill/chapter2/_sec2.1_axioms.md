# Section 2.1: Axioms of quantum mechanics [PDF Pages 3-7]

<!-- ============================================================ -->
<!-- Source: chap2.pdf, Physical Pages: 3-7                        -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 3 -->
# 2 Foundations I: States and Ensembles

## 2.1 Axioms of quantum mechanics

In this chapter and the next we develop the theory of *open* quantum systems. We say a system is open if it is imperfectly isolated, and therefore exchanges energy and information with its unobserved environment. The motivation for studying open systems is that all realistic systems are open. Physicists and engineers may try hard to isolate quantum systems, but they never completely succeed.

Though our main interest is in open systems we will begin by recalling the theory of closed quantum systems, which *are* perfectly isolated. To understand the behavior of an open system $S$, we will regard $S$ combined with its environment $E$ as a closed system (the whole "universe"), then ask how $S$ behaves when we are able to observe $S$ but not $E$.

Quantum theory is a mathematical model of the physical world. For the case of closed systems we can characterize the model by stating *five axioms*; these specify how to represent states, observables, measurements, and dynamics, and also how to combine two systems to obtain a composite system.

**Axiom 1. States.** A state is a complete description of a physical system. In quantum mechanics, a state is a *ray* in a *Hilbert space*.

What is a Hilbert space?

$a)$ It is a *vector space* over the complex numbers $\mathbb{C}$. Vectors will be denoted $|\psi\rangle$ (Dirac's ket notation).

$b)$ It has an *inner product* $\langle\psi|\varphi\rangle$ that maps an ordered pair of vectors to $\mathbb{C}$, and that has the properties:
$i)$ Positivity: $\langle\psi|\psi\rangle > 0$ for $|\psi\rangle \neq 0$.

<!-- Page 4 -->
$ii)$ Linearity: $\langle\varphi|(a|\psi_1\rangle + b|\psi_2\rangle) = a\langle\varphi|\psi_1\rangle + b\langle\varphi|\psi_2\rangle$.
$iii)$ Skew symmetry: $\langle\varphi|\psi\rangle = \langle\psi|\varphi\rangle^*$.
(The $*$ denotes complex conjugation.)

$c)$ It is *complete* in the norm $\|\psi\| = \langle\psi|\psi\rangle^{1/2}$.

(Completeness is an important proviso in infinite-dimensional function spaces, since it ensures the convergence of certain eigenfunction expansions. But mostly we will be content to work with finite-dimensional inner-product spaces.)

What is a ray? It is an equivalence class of vectors that differ by multiplication by a nonzero complex scalar. For any nonzero ray, we can by convention choose a representative of the class, denoted $|\psi\rangle$, that has unit norm:

$$
\langle\psi|\psi\rangle = 1.
$$ {#eq-2.1}

Thus states correspond to normalized vectors, and the overall phase of the vector has no physical significance: $|\psi\rangle$ and $e^{i\alpha}|\psi\rangle$ describe the same state, where $|e^{i\alpha}| = 1$.

Since every ray corresponds to a possible state, given two states $|\varphi\rangle, |\psi\rangle$, another state can be constructed as the linear *superposition* of the two, $a|\varphi\rangle + b|\psi\rangle$. The *relative* phase in this superposition *is* physically significant; we identify $a|\varphi\rangle + b|\psi\rangle$ with $e^{i\alpha}(a|\varphi\rangle + b|\psi\rangle)$ but *not* with $a|\varphi\rangle + e^{i\alpha}b|\psi\rangle$.

We use the notation $\langle\psi|$ (Dirac's bra notation) for a linear function (a *dual vector*) that takes vectors to complex numbers, defined by $|\varphi\rangle \to \langle\psi|\varphi\rangle$.

**Axiom 2. Observables.** An observable is a property of a physical system that in principle can be measured. In quantum mechanics, an observable is a *self-adjoint operator*.

An operator is a linear map taking vectors to vectors,

$$
\boldsymbol{A} : |\psi\rangle \mapsto \boldsymbol{A}|\psi\rangle, \quad \boldsymbol{A} (a|\psi\rangle + b|\varphi\rangle) = a\boldsymbol{A}|\psi\rangle + b\boldsymbol{A}|\varphi\rangle.
$$ {#eq-2.2}

(We will often denote operators by boldface letters.) The adjoint $\boldsymbol{A}^\dagger$ of the operator $\boldsymbol{A}$ is defined by

$$
\langle\varphi|\boldsymbol{A}\psi\rangle = \langle\boldsymbol{A}^\dagger\varphi|\psi\rangle,
$$ {#eq-2.3}

for all vectors $|\varphi\rangle, |\psi\rangle$ (where here $\boldsymbol{A}|\psi\rangle$ has been denoted as $|\boldsymbol{A}\psi\rangle$). $\boldsymbol{A}$ is self-adjoint if $\boldsymbol{A} = \boldsymbol{A}^\dagger$, or in other words, if $\langle\varphi|\boldsymbol{A}|\psi\rangle = \langle\psi|\boldsymbol{A}|\varphi\rangle^*$ for all vectors $|\varphi\rangle$ and $|\psi\rangle$. If $\boldsymbol{A}$ and $\boldsymbol{B}$ are self adjoint, then so is $\boldsymbol{A}+\boldsymbol{B}$ (because $(\boldsymbol{A} + \boldsymbol{B})^\dagger = \boldsymbol{A}^\dagger + \boldsymbol{B}^\dagger$), but $(\boldsymbol{A}\boldsymbol{B})^\dagger = \boldsymbol{B}^\dagger\boldsymbol{A}^\dagger$, so that $\boldsymbol{A}\boldsymbol{B}$ is self adjoint

<!-- Page 5 -->
only if $\boldsymbol{A}$ and $\boldsymbol{B}$ commute. Note that $\boldsymbol{A}\boldsymbol{B} + \boldsymbol{B}\boldsymbol{A}$ and $i(\boldsymbol{A}\boldsymbol{B} - \boldsymbol{B}\boldsymbol{A})$ are always self-adjoint if $\boldsymbol{A}$ and $\boldsymbol{B}$ are.

A self-adjoint operator in a Hilbert space $\mathcal{H}$ has a spectral representation -- its eigenstates form a complete orthonormal basis in $\mathcal{H}$. We can express a self-adjoint operator $\boldsymbol{A}$ as

$$
\boldsymbol{A} = \sum_n a_n \boldsymbol{E}_n.
$$ {#eq-2.4}

Here each $a_n$ is an eigenvalue of $\boldsymbol{A}$, and $\boldsymbol{E}_n$ is the corresponding orthogonal projection onto the space of eigenvectors with eigenvalue $a_n$. The $\boldsymbol{E}_n$'s satisfy

$$
\begin{aligned}
\boldsymbol{E}_n\boldsymbol{E}_m &= \delta_{n,m}\boldsymbol{E}_n, \\
\boldsymbol{E}_n^\dagger &= \boldsymbol{E}_n.
\end{aligned}
$$ {#eq-2.5}

The orthogonal projector onto the one-dimensional space spanned by the vector $|\psi\rangle$ may be expressed as $|\psi\rangle\langle\psi|$, where $\langle\psi|$ is the bra that annihilates vectors orthogonal to $|\psi\rangle$. Therefore, an alternative notation for the spectral representation of $\boldsymbol{A}$ is

$$
\boldsymbol{A} = \sum_n |n\rangle a_n \langle n|,
$$ {#eq-2.6}

where $\{|n\rangle\}$ is the orthonormal basis of eigenstates of $\boldsymbol{A}$, with $\boldsymbol{A}|n\rangle = a_n|n\rangle$.

(For unbounded operators in an infinite-dimensional space, the definition of self-adjoint and the statement of the spectral theorem are more subtle, but this need not concern us.)

**Axiom 3. Measurement.** A measurement is a process in which information about the state of a physical system is acquired by an observer. In quantum mechanics, the measurement of an observable $\boldsymbol{A}$ prepares an eigenstate of $\boldsymbol{A}$, and the observer learns the value of the corresponding eigenvalue. If the quantum state just prior to the measurement is $|\psi\rangle$, then the outcome $a_n$ is obtained with *a priori probability*

$$
\text{Prob}(a_n) = \|\boldsymbol{E}_n|\psi\rangle\|^2 = \langle\psi|\boldsymbol{E}_n|\psi\rangle;
$$ {#eq-2.7}

if the outcome $a_n$ is attained, then the (normalized) quantum state just after the measurement is

$$
\frac{\boldsymbol{E}_n|\psi\rangle}{\|\boldsymbol{E}_n|\psi\rangle\|}.
$$ {#eq-2.8}

<!-- Page 6 -->
If the measurement is immediately repeated, then according to this rule the same outcome is obtained again, with probability one. If many identically prepared systems are measured, each described by the state $|\psi\rangle$, then the *expectation value* of the outcomes is

$$
\langle a\rangle \equiv \sum_n a_n \text{Prob}(a_n) = \sum_n a_n \langle\psi|\boldsymbol{E}_n|\psi\rangle = \langle\psi|\boldsymbol{A}|\psi\rangle.
$$ {#eq-2.9}

**Axiom 4. Dynamics.** Dynamics describes how a state evolves over time. In quantum mechanics, the time evolution of a closed system is described by a *unitary operator*.

In the *Schr\"odinger picture* of dynamics, if the initial state at time $t$ is $|\psi(t)\rangle$, then the final state $|\psi(t')\rangle$ at time $t'$ can be expressed as

$$
|\psi(t')\rangle = \boldsymbol{U}(t', t)|\psi(t)\rangle,
$$ {#eq-2.10}

where $\boldsymbol{U}(t', t)$ is the unitary time evolution operator. Infinitesimal time evolution is governed by the *Schr\"odinger equation*

$$
\frac{d}{dt}|\psi(t)\rangle = -i\boldsymbol{H}(t)|\psi(t)\rangle,
$$ {#eq-2.11}

where $\boldsymbol{H}(t)$ is a self-adjoint operator, called the *Hamiltonian* of the system. (The Hamiltonian has the dimensions of energy; we have chosen units in which Planck's constant $\hbar = h/2\pi = 1$, so that energy has the dimensions of inverse time.) To first order in the infinitesimal quantity $dt$, the Schr\"odinger equation can be expressed as

$$
|\psi(t+dt)\rangle = (\boldsymbol{I} - i\boldsymbol{H}(t)dt)|\psi(t)\rangle.
$$ {#eq-2.12}

Thus the operator $\boldsymbol{U}(t+dt, t) \equiv \boldsymbol{I} - i\boldsymbol{H}(t)dt$ is unitary; because $\boldsymbol{H}$ is self-adjoint it satisfies $\boldsymbol{U}^\dagger\boldsymbol{U} = \boldsymbol{I}$ to linear order in $dt$. Since a product of unitary operators is unitary, time evolution governed by the Schr\"odinger equation over a finite interval is also unitary. In the case where $\boldsymbol{H}$ is time independent we may write $\boldsymbol{U}(t', t) = e^{-i(t'-t)\boldsymbol{H}}$.

Our final axiom relates the description of a composite quantum system $AB$ to the description of its component parts $A$ and $B$.

**Axiom 5. Composite Systems.** If the Hilbert space of system $A$ is $\mathcal{H}_A$ and the Hilbert space of system $B$ is $\mathcal{H}_B$, then the Hilbert space of the composite systems $AB$ is the *tensor product* $\mathcal{H}_A \otimes \mathcal{H}_B$. If system $A$ is prepared in the state $|\psi\rangle_A$ and system $B$ is prepared in the state $|\varphi\rangle_B$, then the composite system's state is the product $|\psi\rangle_A \otimes |\varphi\rangle_B$.

<!-- Page 7 -->
What is a tensor product of Hilbert spaces? If $\{|i\rangle_A\}$ denotes an orthonormal basis for $\mathcal{H}_A$ and $\{|\mu\rangle_B\}$ a basis for $\mathcal{H}_B$, then the states $|i, \mu\rangle_{AB} \equiv |i\rangle_A \otimes |\mu\rangle_B$ are a basis for $\mathcal{H}_A \otimes \mathcal{H}_B$, where the inner product on $\mathcal{H}_A \otimes \mathcal{H}_B$ is defined by

$$
{}_{AB}\langle i, \mu | j, \nu \rangle_{AB} = \delta_{ij}\delta_{\mu\nu}.
$$ {#eq-2.13}

The tensor product operator $\boldsymbol{M}_A \otimes \boldsymbol{N}_B$ is the operator that applies $\boldsymbol{M}_A$ to system $A$ and $\boldsymbol{N}_B$ to system $B$. Its action on the orthonormal basis $|i, \mu\rangle_{AB}$ is

$$
\boldsymbol{M}_A \otimes \boldsymbol{N}_B |i, \mu\rangle_{AB} = \boldsymbol{M}_A |i\rangle_A \otimes \boldsymbol{N}_B |\mu\rangle_B = \sum_{j, \nu} |j, \nu\rangle_{AB} (\boldsymbol{M}_A)_{ji} (\boldsymbol{N}_B)_{\nu\mu}.
$$ {#eq-2.14}

An operator that acts trivially on system $B$ can be denoted $\boldsymbol{M}_A \otimes \boldsymbol{I}_B$, where $\boldsymbol{I}_B$ is the identity on $\mathcal{H}_B$, and an operator that acts trivially on system $A$ can be denoted $\boldsymbol{I}_A \otimes \boldsymbol{N}_B$.

These five axioms provide a complete mathematical formulation of quantum mechanics. We immediately notice some curious features. One oddity is that the Schr\"odinger equation is linear, while we are accustomed to nonlinear dynamical equations in classical physics. This property seems to beg for an explanation. But far more curious is a mysterious dualism; there are two quite distinct ways for a quantum state to change. On the one hand there is unitary evolution, which is deterministic. If we specify the initial state $|\psi(0)\rangle$, the theory predicts the state $|\psi(t)\rangle$ at a later time. But on the other hand there is measurement, which is probabilistic. The theory does not make definite predictions about the measurement outcomes; it only assigns probabilities to the various alternatives. This is troubling, because it is unclear why the measurement process should be governed by different physical laws than other processes.

The fundamental distinction between evolution and measurement, and in particular the intrinsic randomness of the measurement process, is sometimes called the *measurement problem* of quantum theory. Seeking a more pleasing axiomatic formulation of quantum theory is a worthy task which may eventually succeed. But these five axioms correctly account for all that we currently know about quantum physics, and provide the foundation for all that follows in this book.
