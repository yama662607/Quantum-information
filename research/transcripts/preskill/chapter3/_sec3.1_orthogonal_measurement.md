# Section 3.1: Orthogonal measurement and beyond [PDF Pages 4-11]

<!-- ============================================================ -->
<!-- Source: chap3.pdf, Physical Pages: 4-11                       -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 4 -->
# 3 Foundations II: Measurement and Evolution

## 3.1 Orthogonal measurement and beyond

In Chapter 2 we discussed how to describe the state of an *open* quantum system, one which is part of a larger system. In this Chapter we will extend the theory of open quantum systems further. In particular, we will develop two important concepts: *generalized measurements*, which are performed by making use of an auxiliary system, and *quantum channels*, which describe how open systems evolve.

### 3.1.1 Orthogonal Measurements

An axiom of quantum theory asserts that a measurement may be described as an orthogonal projection operator. But if a measurement of system $S$ is realized by performing an orthogonal measurement on a larger system that contains $S$, the resulting operation performed on $S$ alone need not be an orthogonal projection. We would like to find a mathematical description of such "generalized measurements" on system $S$. But first let's recall how measurement of an arbitrary Hermitian operator can be achieved in principle, following the classic treatment of Von Neumann.

To measure an observable $\boldsymbol{M}$, we will modify the Hamiltonian of the world by turning on a coupling between that observable and another variable that represents the apparatus. Depending on the context, we will refer to the auxiliary system used in the measurement as the "pointer," the "meter," or the "ancilla." (The word "ancilla" just means something extra which is used to achieve a desired goal.) The coupling establishes a correlation between the eigenstates of the observable and the distinguishable states of the pointer, so that we can prepare an eigenstate of the observable by "observing" the pointer.

<!-- Page 5 -->
This may not seem like a fully satisfying model of measurement because we have not explained how to measure the pointer. Von Neumann's attitude was that it is possible in principle to correlate the state of a microscopic quantum system with the value of a macroscopic classical variable, and we may take it for granted that we can perceive the value of the classical variable. A quantum measurement, then, is a procedure for amplifying a property of the microscopic world, making it manifest in the macroscopic world.

We may think of the pointer as a particle of mass $m$ that propagates freely apart from its tunable coupling to the quantum system being measured. Since we intend to measure the position of the pointer, it should be prepared initially in a wavepacket state that is narrow in position space --- but not too narrow, because a vary narrow wave packet will spread too rapidly. If the initial width of the wave packet is $\Delta x$, then the uncertainty in it velocity will be of order $\Delta v = \Delta p/m \sim \hbar/m\Delta x$, so that after a time $t$, the wavepacket will spread to a width

$$
\Delta x(t) \sim \Delta x + \frac{\hbar t}{\Delta x},
$$ {#eq-3.1}

which is minimized for $(\Delta x(t))^2 \sim (\Delta x)^2 \sim \hbar t/m$. Therefore, if the experiment takes a time $t$, the resolution we can achieve for the final position of the pointer is limited by

$$
\Delta x \gtrsim (\Delta x)_{SQL} \sim \sqrt{\frac{\hbar t}{m}},
$$ {#eq-3.2}

the "standard quantum limit." We will choose our pointer to be sufficiently heavy that this limitation is not serious.

The Hamiltonian describing the coupling of the quantum system to the pointer has the form

$$
\boldsymbol{H} = \boldsymbol{H}_0 + \frac{1}{2m}\boldsymbol{P}^2 + \lambda(t)\boldsymbol{M}\otimes\boldsymbol{P},
$$ {#eq-3.3}

where $\boldsymbol{P}^2/2m$ is the Hamiltonian of the free pointer particle (which we will henceforth ignore on the grounds that the pointer is so heavy that spreading of its wavepacket may be neglected), $\boldsymbol{H}_0$ is the unperturbed Hamiltonian of the system to be measured, and $\lambda$ is a coupling constant that we are able to turn on and off as desired. The observable to be measured, $\boldsymbol{M}$, is coupled to the momentum $\boldsymbol{P}$ of the pointer.

If $\boldsymbol{M}$ does not commute with $\boldsymbol{H}_0$, then we have to worry about how the observable $\boldsymbol{M}$ evolves during the course of the measurement. To simplify the analysis, let us suppose that either $[\boldsymbol{M}, \boldsymbol{H}_0] = 0$, or else the measurement is carried out quickly enough that the free evolution of the system can be neglected during the measurement procedure. Then the

<!-- Page 6 -->
Hamiltonian can be approximated as $\boldsymbol{H} \simeq \lambda(t)\boldsymbol{M}\otimes\boldsymbol{P}$. If the coupling $\lambda$ switches on suddenly at time zero and switches off suddenly at time $T$, the resulting time evolution operator is

$$
\boldsymbol{U}(T) \simeq \exp(-i\lambda T \boldsymbol{M}\otimes\boldsymbol{P}).
$$ {#eq-3.4}

Expanding in the basis in which $\boldsymbol{M}$ is diagonal,

$$
\boldsymbol{M} = \sum_a |a\rangle M_a \langle a|,
$$ {#eq-3.5}

we express $\boldsymbol{U}(T)$ as

$$
\boldsymbol{U}(T) = \sum_a |a\rangle \exp(-i\lambda T M_a \boldsymbol{P}) \langle a|.
$$ {#eq-3.6}

Now we recall that $\boldsymbol{P}$ generates a translation of the *position* of the pointer: $\boldsymbol{P} = -i \frac{d}{dx}$ in the position representation, so that $e^{-ix_0\boldsymbol{P}} = \exp\left(-x_0 \frac{d}{dx}\right)$, and by Taylor expanding,

$$
e^{-ix_0\boldsymbol{P}}\psi(x) = \psi(x-x_0);
$$ {#eq-3.7}

In other words $e^{-ix_0\boldsymbol{P}}$ acting on a wavepacket translates the wavepacket by $x_0$. We see that if our quantum system starts in a superposition of $\boldsymbol{M}$ eigenstates, initially unentangled with the position-space wavepacket $|\psi(x)\rangle$ of the pointer, then after time $T$ the quantum state has evolved to

$$
\boldsymbol{U}(T)\left(\sum_a \alpha_a |a\rangle \otimes |\psi(x)\rangle\right) = \sum_a \alpha_a |a\rangle \otimes |\psi(x - \lambda T M_a)\rangle;
$$ {#eq-3.8}

the position of the pointer has become correlated with the value of the observable $\boldsymbol{M}$. If the pointer wavepacket is narrow enough for us to resolve all values of the $M_a$ that occur (that is, the width $\Delta x$ of the packet is small compared to $\lambda T \Delta M_a$, where $\Delta M_a$ is the minimal gap between eigenvalues of $\boldsymbol{M}$), then when we observe the position of the pointer (never mind how!) we will prepare an eigenstate of the observable. With probability $|\alpha_a|^2$, we will detect that the pointer has shifted its position by $\lambda T M_a$, in which case we will have prepared the $\boldsymbol{M}$ eigenstate $|a\rangle$. We conclude that the initial state $|\phi\rangle$ of the quantum system is projected to $|a\rangle$ with probability $|\langle a|\phi\rangle|^2$. This is Von Neumann's model of orthogonal measurement.

The classic example is the Stern--Gerlach apparatus. To measure $\boldsymbol{\sigma}_3$ for a spin-$\frac{1}{2}$ object, we allow the object to pass through a region of inhomogeneous magnetic field

$$
B_3 = \lambda z.
$$ {#eq-3.9}

<!-- Page 7 -->
The magnetic moment of the object is $\mu\vec{\boldsymbol{\sigma}}$, and the coupling induced by the magnetic field is

$$
\boldsymbol{H} = -\lambda\mu z \boldsymbol{\sigma}_3.
$$ {#eq-3.10}

In this case $\boldsymbol{\sigma}_3$ is the observable to be measured, coupled to the position $z$ rather than the momentum of the pointer; thus, because $z$ generates a translation of $P_z$, the coupling imparts an *impulse* to the pointer which is correlated with its spin. We can perceive whether the object is pushed up or down, and so project out the spin state $|\uparrow_z\rangle$ or $|\downarrow_z\rangle$. By rotating the magnet, we could measure the observable $\hat{n}\cdot\vec{\boldsymbol{\sigma}}$ instead.

Thinking more abstractly, suppose that $\{\boldsymbol{E}_a, a = 0, 1, 2, \dots N-1\}$ is a complete set of orthogonal projectors satisfying

$$
\boldsymbol{E}_a \boldsymbol{E}_b = \delta_{ab}\boldsymbol{E}_a, \quad \boldsymbol{E}_a = \boldsymbol{E}_a^\dagger, \quad \sum_a \boldsymbol{E}_a = \boldsymbol{I}.
$$ {#eq-3.11}

To perform an orthogonal measurement with these outcomes, we introduce an $N$-dimensional pointer system with fiducial orthonormal basis states $\{|a\rangle, a = 0, 1, 2, \dots, N-1\}$, and, by coupling the system to the pointer, perform the unitary transformation

$$
\boldsymbol{U} = \sum_{a,b} \boldsymbol{E}_a \otimes |b+a\rangle\langle b|.
$$ {#eq-3.12}

Thus the pointer advances by an amount $a$ if the state of the system is within the support of the projector $\boldsymbol{E}_a$. (The addition in $|b+a\rangle$ is understood to be modulo $N$; we may envision the pointer as a circular dial with $N$ uniformly spaced tick marks.) The unitarity of $\boldsymbol{U}$ is easy to verify:

$$
\begin{aligned}
\boldsymbol{U}\boldsymbol{U}^\dagger &= \left(\sum_{a,b} \boldsymbol{E}_a \otimes |b+a\rangle\langle b|\right) \left(\sum_{c,d} \boldsymbol{E}_c \otimes |d\rangle\langle d+c|\right) \\
&= \sum_{a,b,c,d} \delta_{ac}\boldsymbol{E}_a \otimes \delta_{bd}|b+a\rangle\langle d+c| \\
&= \sum_a \boldsymbol{E}_a \otimes \sum_b |b+a\rangle\langle b+a| = \boldsymbol{I} \otimes \boldsymbol{I}.
\end{aligned}
$$ {#eq-3.13}

This unitary transformation acts on an initial product state of system and pointer according to

$$
\boldsymbol{U} : |\Psi\rangle = |\psi\rangle \otimes |0\rangle \mapsto |\Psi'\rangle = \sum_a \boldsymbol{E}_a |\psi\rangle \otimes |a\rangle;
$$ {#eq-3.14}

if the pointer is then measured in the fiducial basis, the measurement postulate implies that the outcome $a$ occurs with probability

$$
\text{Prob}(a) = \langle\Psi'| (\boldsymbol{I} \otimes |a\rangle\langle a|) |\Psi'\rangle = \langle\psi|\boldsymbol{E}_a|\psi\rangle,
$$ {#eq-3.15}

<!-- Page 8 -->
and that when this outcome occurs the normalized post-measurement state is

$$
\frac{\boldsymbol{E}_a|\psi\rangle}{\|\boldsymbol{E}_a|\psi\rangle\|}.
$$ {#eq-3.16}

If the measurement is performed and its outcome is not known, the initial pure state of the system becomes a mixture of these post-measurement states:

$$
\sum_a \text{Prob}(a)\frac{\boldsymbol{E}_a|\psi\rangle\langle\psi|\boldsymbol{E}_a}{\langle\psi|\boldsymbol{E}_a|\psi\rangle} = \sum_a \boldsymbol{E}_a|\psi\rangle\langle\psi|\boldsymbol{E}_a.
$$ {#eq-3.17}

In fact, the system is described by this density operator once it becomes entangled with the pointer, whether we bother to observe the pointer or not. If the initial state of the system before the measurement is a mixed state with density matrix $\boldsymbol{\rho}$, then by expressing $\boldsymbol{\rho}$ as an ensemble of pure states we conclude that the measurement modifies the state according to

$$
\boldsymbol{\rho} \mapsto \sum_a \boldsymbol{E}_a\boldsymbol{\rho}\boldsymbol{E}_a.
$$ {#eq-3.18}

We see that if, by coupling the system to our pointer, we can execute suitable unitary transformations correlating the system and the pointer, and if we can observe the pointer in its fiducial basis, then we are empowered to perform any conceivable orthogonal measurement on the system.

### 3.1.2 Generalized measurements

In this discussion of orthogonal measurement, the fiducial basis of the pointer had two different roles --- we assumed that the fiducial pointer states become correlated with the system projectors $\{\boldsymbol{E}_a\}$, and also that the measurement of the pointer projects onto the fiducial basis. In principle we could separate these two roles. Perhaps the unitary transformation applied to system and pointer picks out a different preferred basis than the basis in which the pointer is easily measured. Or perhaps the pointer which becomes entangled with the system is itself microscopic, and we may entangle it with a second macroscopic pointer in order to measure the microscopic pointer in whatever basis we prefer.

Suppose, to be concrete, that the system $A$ is a single qubit, and so is the pointer $B$. They interact, resulting in the unitary map

$$
\boldsymbol{U} : (\alpha|0\rangle + \beta|1\rangle)_A \otimes |0\rangle_B \mapsto \alpha|0\rangle_A \otimes |0\rangle_B + \beta|1\rangle_A \otimes |1\rangle_B.
$$ {#eq-3.19}

Measuring the pointer by projecting onto the basis $\{|0\rangle, |1\rangle\}$ would induce an orthogonal measurement of the system, also in the $\{|0\rangle, |1\rangle\}$ basis. But suppose that we measure the pointer in a different basis instead, such as

<!-- Page 9 -->
$\{|\pm\rangle = \frac{1}{\sqrt{2}}(|0\rangle \pm |1\rangle)\}$. Then the measurement postulate dictates that the two outcomes $+$ and $-$ occur equiprobably, and that the corresponding post-measurement states of the system are

$$
\alpha|0\rangle \pm \beta|1\rangle.
$$ {#eq-3.20}

In contrast to an orthogonal measurement of the system, these two post-measurement states are not orthogonal, unless $|\alpha| = |\beta|$. Furthermore, also in contrast to an orthogonal measurement, if two such measurements are performed in rapid succession, the outcomes need not be the same. We use the term *generalized measurement* to mean a measurement, like this one, which is not necessarily an orthogonal projection acting on the system.

It is convenient to describe this measurement procedure by expanding the entangled state of system and pointer in the basis in which the pointer is measured; hence we rewrite eq.(3.19) as

$$
\boldsymbol{U} : |\psi\rangle_A \otimes |0\rangle_B \mapsto \boldsymbol{M}_+|\psi\rangle_A \otimes |+\rangle_B + \boldsymbol{M}_-|\psi\rangle_A \otimes |-\rangle_B,
$$ {#eq-3.21}

where

$$
\boldsymbol{M}_+ = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} = \frac{1}{\sqrt{2}}\boldsymbol{I}, \quad \boldsymbol{M}_- = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} = \frac{1}{\sqrt{2}}\boldsymbol{\sigma}_3.
$$ {#eq-3.22}

Evidently, by measuring $B$ in the basis $\{|\pm\rangle\}$, we prepare $A$ in one of the states $\boldsymbol{M}_\pm|\psi\rangle$, up to a normalization factor.

Now let's generalize this idea to the case where the pointer system $B$ is $N$-dimensional, and the measurement of the pointer projects onto an orthonormal basis $\{|a\rangle, a = 0, 1, 2, \dots, N-1\}$. Again we'll assume that the system $A$ and pointer $B$ are initially in a product state, then an entangling unitary transformation $\boldsymbol{U}$ correlates the system with the pointer. By expanding the action of $\boldsymbol{U}$ in the basis for $B$ we obtain

$$
\boldsymbol{U} : |\psi\rangle_A \otimes |0\rangle_B \mapsto \sum_a \boldsymbol{M}_a|\psi\rangle_A \otimes |a\rangle_B.
$$ {#eq-3.23}

Since $\boldsymbol{U}$ is unitary, it preserves the norm of any input, which means that

$$
1 = \left\| \sum_a \boldsymbol{M}_a|\psi\rangle \otimes |a\rangle \right\|^2 = \sum_{a,b}\langle\psi|\boldsymbol{M}_a^\dagger \boldsymbol{M}_b|\psi\rangle\langle a|b\rangle = \sum_a \langle\psi|\boldsymbol{M}_a^\dagger \boldsymbol{M}_a|\psi\rangle
$$ {#eq-3.24}

for any $|\psi\rangle$; hence

$$
\sum_a \boldsymbol{M}_a^\dagger \boldsymbol{M}_a = \boldsymbol{I}.
$$ {#eq-3.25}

<!-- Page 10 -->
The complete orthogonal measurement projecting onto the pointer basis $\{|a\rangle_B\}$ is equivalent to the incomplete orthogonal measurement on $AB$ with projectors $\{\boldsymbol{I} \otimes |a\rangle\langle a|\}$; the measurement postulate asserts that outcome $a$ occurs with probability

$$
\text{Prob}(a) = \|\boldsymbol{M}_a|\psi\rangle\|^2,
$$ {#eq-3.26}

and that if outcome $a$ occurs the post-measurement state of the system is

$$
\frac{\boldsymbol{M}_a|\psi\rangle}{\|\boldsymbol{M}_a|\psi\rangle\|}.
$$ {#eq-3.27}

The completeness relation $\sum_a \boldsymbol{M}_a^\dagger \boldsymbol{M}_a = \boldsymbol{I}$ ensures that the probabilities sum to one, but the possible post-measurement states need not be mutually orthogonal, nor are the measurements necessarily repeatable. If we perform the measurement twice in succession and obtain outcome $a$ the first time, the conditional probability of obtaining outcome $b$ in the second measurement is

$$
\text{Prob}(b|a) = \frac{\|\boldsymbol{M}_b\boldsymbol{M}_a|\psi\rangle\|^2}{\|\boldsymbol{M}_a|\psi\rangle\|^2}.
$$ {#eq-3.28}

The two measurements agree if $\text{Prob}(b|a) = \delta_{ba}$, which is satisfied for arbitrary initial states of the system only if $\boldsymbol{M}_b\boldsymbol{M}_a = \delta_{ba}\boldsymbol{M}_a$ up to a phase factor, *i.e.* in the case where the measurement is orthogonal.

We see that if the initial state of the system is the density operator $\boldsymbol{\rho}$ (realized as an ensemble of pure states), there is an operator $\boldsymbol{E}_a = \boldsymbol{M}_a^\dagger \boldsymbol{M}_a$ associated with each possible measurement outcome $a$, such that the probability of outcome $a$ is

$$
\text{Prob}(a) = \text{tr}(\boldsymbol{\rho}\boldsymbol{E}_a).
$$ {#eq-3.29}

The measurement operators $\{\boldsymbol{E}_a\}$ form a complete set of Hermitian nonnegative operators; that is, they satisfy the properties:

1. *Hermiticity.* $\boldsymbol{E}_a = \boldsymbol{E}_a^\dagger$.
2. *Positivity.* $\langle\psi|\boldsymbol{E}_a|\psi\rangle \ge 0$ for any vector $|\psi\rangle$; we abbreviate this property by simply writing $\boldsymbol{E}_a \ge 0$.
3. *Completeness.* $\sum_a \boldsymbol{E}_a = \boldsymbol{I}$.

Such a partition of unity by nonnegative operators is called a *positive operator-valued measure*, or *POVM*. (The term *measure* is a bit heavy-handed in this finite-dimensional context; it becomes more apt when the index $a$ can be continuously varying.)

<!-- Page 11 -->
We have seen how a POVM can arise when an orthogonal measurement is performed on a meter after the meter interacts with the system. In fact any POVM can be realized this way. We need only observe that a nonnegative Hermitian operator $\boldsymbol{E}_a$ has a nonnegative square root $\sqrt{\boldsymbol{E}_a}$; more generally, the operator

$$
\boldsymbol{M}_a = \boldsymbol{U}_a\sqrt{\boldsymbol{E}_a}
$$ {#eq-3.30}

obeys $\boldsymbol{M}_a^\dagger \boldsymbol{M}_a = \boldsymbol{E}_a$ where $\boldsymbol{U}_a$ is an arbitrary unitary operator --- eq.(3.30) is the *polar decomposition* of the operator $\boldsymbol{M}_a$. Plugging into eq.(3.23) yields the unitary interaction which realizes the POVM $\{\boldsymbol{E}_a\}$. In this formulation, the post-measurement state corresponding to outcome $a$,

$$
\boldsymbol{U}_a\left(\frac{\sqrt{\boldsymbol{E}_a}|\psi\rangle}{\|\sqrt{\boldsymbol{E}_a}|\psi\rangle\|}\right),
$$ {#eq-3.31}

is arbitrary, since we are free to choose the unitary $\boldsymbol{U}_a$ however we please for each possible outcome. The POVM attributes a probability to each measurement outcome, but provides no guidance regarding the state after the measurement. Indeed, after the measurement we have the freedom to discard the state and replace it by whatever freshly prepared state we desire.
