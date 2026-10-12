# Section 3.5 Transcript: Master equations for open quantum systems

**Source**: `quarto/assets/pdf/preskill/chap3.pdf` (Pages 34–41 top)  
**Status**: Complete, faithful transcript including all mathematical expressions and formatting.

---

## 3.5 Master equations for open quantum systems (p. 34)

### 3.5.1 Markovian evolution (p. 34)

Quantum channels provide a general description of the evolution of density operators, including the evolution of pure states to mixed states (decoherence). In the same sense, unitary transformations provide a general description of coherent quantum evolution. But in the case of coherent evolution, we often find it very convenient to characterize the dynamics of a quantum system with a *Hamiltonian*, which describes the evolution over an infinitesimal time interval. The dynamics is then encoded in a differential equation, the *Schrödinger equation*, and we may calculate the evolution over a finite time interval by integrating the equation, that is, by piecing together the evolution over many infinitesimal intervals. Likewise, it is often possible to describe the (not necessarily coherent) evolution of a density operator, at least to a good approximation, by a differential equation which is called the *master equation*.

It is not obvious that there should be a differential equation that describes the decoherence of an open system. Such a description is possible only if the evolution of the quantum system is *Markovian*, that is, *local in time*. For the evolution of the density operator $\boldsymbol{\rho}(t)$ to be governed by a (first-order) differential equation in $t$, $\boldsymbol{\rho}(t + dt)$ must be completely determined by $\boldsymbol{\rho}(t)$.

In the case of an open system $A$, we are to imagine that its evolution is actually unitary on the extended system $AE$, where $E$ is the environment. But though the evolution of $AE$ may be governed by a Schrödinger equation, that’s not enough to ensure that the time evolution is Markovian for $A$ by itself. The trouble is that information can flow from $A$ to $E$ and then return at a later time. In that case the density operator $\boldsymbol{\rho}_A(t + dt)$ is not fully determined by $\boldsymbol{\rho}_A(t)$; we need to know $\boldsymbol{\rho}_A$ at earlier times as well.

This quandary arises because information flow is a two-way street. An open system (whether classical or quantum) is *dissipative* because information and energy can flow from the system to the environment. But that means that information can also flow back from environment to system, resulting in non-Markovian *fluctuations* of the system. This inescapable connection underlies the *fluctuation-dissipation theorem*, a widely applicable tool of statistical physics.

For any open system these fluctuations are inevitable, and an exact Markovian description of quantum dynamics is impossible. Nevertheless, a Markovian description can be a very good approximation if there is a clean separation between the typical correlation time of the fluctuations and the time scale of the evolution that we want to follow. Crudely speaking, we may denote by $(\Delta t)_{\mathrm{env}}$ the time it takes for the environment to “forget” information it acquired from the system — after time $(\Delta t)_{\mathrm{env}}$ we can regard that information as lost forever, and neglect the possibility that the information may return to influence the subsequent evolution of the system.

To describe the evolution we “coarse-grain” in time, perceiving the dynamics through a filter that screens out the high frequency components of the motion with $\omega \gg (\Delta t_{\mathrm{coarse}})^{-1}$. An approximately Markovian description should be possible for $(\Delta t)_{\mathrm{env}} \ll (\Delta t_{\mathrm{coarse}})$; we may neglect the memory of the reservoir if we are unable to resolve its effects. This Markovian approximation is useful if the time scale of the dynamics that we want to observe is long compared to $(\Delta t_{\mathrm{coarse}})$, for example if the damping time scale $(\Delta t)_{\mathrm{damp}}$ satisfies
$$
(\Delta t)_{\mathrm{damp}} \gg (\Delta t_{\mathrm{coarse}} \gg (\Delta t)_{\mathrm{env}}.
\tag{3.122}
$$
This is a good approximation in some physical settings, like an atom interacting with the radiation field, but more dubious in other cases, like an electron spin interacting with nuclear spins in a semiconductor.

We could attempt to derive the master equation starting with the Schrödinger equation for $AE$, treating the coupling between $A$ and $E$ in time-dependent perturbation theory, and carefully introducing a frequency cutoff, but we won't do that here. Instead let’s take it for granted that the dynamics is Markovian, and use the theory of quantum channels to infer the form of the master equation.

### 3.5.2 The Liouvillian (p. 35)

For a closed quantum system, time evolution is governed by a self-adjoint Hamiltonian $\boldsymbol{H}$ according to
$$
|\psi(t + dt)\rangle = (\boldsymbol{I} - idt\boldsymbol{H}) |\psi(t)\rangle,
\tag{3.123}
$$
and correspondingly the density operator evolves as
$$
\boldsymbol{\rho}(t + dt) = \boldsymbol{\rho}(t) - idt[\boldsymbol{H}, \boldsymbol{\rho}(t)].
\tag{3.124}
$$
In the case of an open quantum system, Markovian evolution for the infinitesimal time interval $dt$ may be expressed as
$$
\boldsymbol{\rho}(t + dt) = \mathcal{E}_{dt}(\boldsymbol{\rho}(t)),
\tag{3.125}
$$
where $\mathcal{E}_{dt}$ is a quantum channel. By adopting this Markovian form, we take the view that, after each infinitesimal time increment in the joint evolution of the system and its environment, the state of the environment is discarded and replaced by a fresh state of the environment unentangled with the system. We already made this assumption implicitly when discussing continuous-time dephasing and spontaneous decay in §3.4.

Expanding $\mathcal{E}_{dt}$ to linear order,
$$
\mathcal{E}_{dt} = \boldsymbol{I} + dt\mathcal{L}
\tag{3.126}
$$
we find
$$
\dot{\boldsymbol{\rho}} = \mathcal{L}(\boldsymbol{\rho}),
\tag{3.127}
$$
where the linear map $\mathcal{L}$ generating time evolution is called the *Liouvillian* or *Lindbladian*. This evolution equation has the formal solution
$$
\boldsymbol{\rho}(t) = \lim_{n\to\infty} \left(1 + \frac{\mathcal{L}t}{n}\right)^n (\boldsymbol{\rho}(0)) = e^{\mathcal{L}t}(\boldsymbol{\rho}(0))
\tag{3.128}
$$
if $\mathcal{L}$ is time independent.

The channel has an operator-sum representation
$$
\boldsymbol{\rho}(t + dt) = \mathcal{E}_{dt}(\boldsymbol{\rho}(t)) = \sum_a \boldsymbol{M}_a \boldsymbol{\rho}(t) \boldsymbol{M}_a^\dagger = \boldsymbol{\rho}(t) + O(dt),
\tag{3.129}
$$
where, if we retain only terms up to linear order in $dt$, we may assume without loss of generality that $\boldsymbol{M}_0 = \boldsymbol{I} + O(dt)$, and that $\boldsymbol{M}_a$ is of order $\sqrt{dt}$ for $a > 0$. Each of the Kraus operators $\boldsymbol{M}_{1,2,\dots}$ describes a possible “quantum jump” that the system might undergo, which occurs during time interval $dt$ with probability $O(dt)$, and $\boldsymbol{M}_0$ describes how the system evolves when no jump occurs. We may write
$$
\begin{aligned}
\boldsymbol{M}_0 &= \boldsymbol{I} + (-i\boldsymbol{H} + \boldsymbol{K})dt, \\
\boldsymbol{M}_a &= \sqrt{dt} \, \boldsymbol{L}_a,
\end{aligned}
\tag{3.130}
$$
where $\boldsymbol{H}$ and $\boldsymbol{K}$ are both hermitian and $\boldsymbol{L}_a, \boldsymbol{H}$, and $\boldsymbol{K}$ are all zeroth order in $dt$. In fact, we can determine $\boldsymbol{K}$ by invoking the Kraus-operator completeness relation; keeping terms up to linear order in $O(dt)$, we find
$$
\boldsymbol{I} = \sum_a \boldsymbol{M}_a^\dagger \boldsymbol{M}_a = \boldsymbol{I} + dt \left( 2\boldsymbol{K} + \sum_{a>0} \boldsymbol{L}_a^\dagger \boldsymbol{L}_a \right) + \cdots,
\tag{3.131}
$$
or
$$
\boldsymbol{K} = -\frac{1}{2} \sum_{a>0} \boldsymbol{L}_a^\dagger \boldsymbol{L}_a.
\tag{3.132}
$$
Substituting into eq. (3.129), we obtain the Lindblad master equation:
$$
\dot{\boldsymbol{\rho}} = \mathcal{L}(\boldsymbol{\rho}) = -i[\boldsymbol{H}, \boldsymbol{\rho}] + \sum_{a>0} \left( \boldsymbol{L}_a \boldsymbol{\rho} \boldsymbol{L}_a^\dagger - \frac{1}{2}\boldsymbol{L}_a^\dagger \boldsymbol{L}_a \boldsymbol{\rho} - \frac{1}{2}\boldsymbol{\rho}\boldsymbol{L}_a^\dagger \boldsymbol{L}_a \right).
\tag{3.133}
$$
This is the general Markovian evolution law for quantum states in the Schrödinger picture, assuming time evolution is a trace-preserving completely positive linear map. The first term in $\mathcal{L}(\boldsymbol{\rho})$ is the familiar Hamiltonian term generating unitary evolution. The other terms describe the possible transitions that the system may undergo due to interactions with the environment. The operators $\boldsymbol{L}_a$ are called *Lindblad operators* or *quantum jump operators*. Each $\boldsymbol{L}_a \boldsymbol{\rho} \boldsymbol{L}_a^\dagger$ term induces one of the possible quantum jumps, while the terms $-1/2\boldsymbol{L}_a^\dagger \boldsymbol{L}_a \boldsymbol{\rho} - 1/2\boldsymbol{\rho}\boldsymbol{L}_a^\dagger \boldsymbol{L}_a$ are needed to normalize properly the case in which no jumps occur.

Alternatively, we can describe the evolution using the Heisenberg picture. Then instead of eq.(3.129), the density operator is time-independent, while an operator $\boldsymbol{A}$ evolves according to
$$
\boldsymbol{A}(t + dt) = \mathcal{E}^*_{dt}(\boldsymbol{A}(t)) = \sum_a \boldsymbol{M}_a^\dagger \boldsymbol{A}(t) \boldsymbol{M}_a,
\tag{3.134}
$$
and hence
$$
\dot{\boldsymbol{A}} = \mathcal{L}^*(\boldsymbol{A}) = i[\boldsymbol{H}, \boldsymbol{A}] + \sum_{a>0} \left( \boldsymbol{L}_a^\dagger \boldsymbol{A} \boldsymbol{L}_a - \frac{1}{2}\boldsymbol{L}_a^\dagger \boldsymbol{L}_a \boldsymbol{A} - \frac{1}{2}\boldsymbol{A}\boldsymbol{L}_a^\dagger \boldsymbol{L}_a \right).
\tag{3.135}
$$
Heisenberg-picture time evolution is unital rather than trace preserving; the identity operator $\boldsymbol{I}$ does not evolve.

As for any nonunitary quantum channel, we have the freedom to redefine the Kraus operators in the operator-sum representation of $\mathcal{E}_{dt}$, replacing $\{\boldsymbol{M}_a\}$ by operators $\{\boldsymbol{N}_\mu\}$ which differ by a unitary change of basis. In particular, invoking this freedom for the jump operators (while leaving $\boldsymbol{M}_0$ untouched), we may replace $\{\boldsymbol{L}_a\}$ by $\{\boldsymbol{L}'_\mu\}$ where
$$
\boldsymbol{L}'_\mu = \sum_a V_{\mu a} \boldsymbol{L}_a
\tag{3.136}
$$
and $V_{\mu a}$ is a unitary matrix. We say that these two ways of choosing the jump operators are two different *unravelings* of the same Markovian dynamics.

The master equation describes what happens when the system interacts with an unobserved environment, but we may also consider what happens if the environment is continuously monitored. In that case each quantum jump is detected; we update the quantum state of the system whenever a jump occurs, and an initial pure state remains pure at all later times. Specifically, a jump of type $a$ occurs during the interval $(t, t + dt)$ with probability
$$
\mathrm{Prob}(a) = dt \langle\psi(t)|\boldsymbol{L}_a^\dagger \boldsymbol{L}_a|\psi(t)\rangle,
\tag{3.137}
$$
and when a type-$a$ jump is detected the updated state is
$$
|\psi(t + dt)\rangle = \frac{\boldsymbol{L}_a |\psi(t)\rangle}{\|\boldsymbol{L}_a |\psi(t)\rangle\|},
\tag{3.138}
$$
while when no jump occurs the state evolves as
$$
|\psi(t + dt)\rangle = \frac{\boldsymbol{M}_0 |\psi(t)\rangle}{\|\boldsymbol{M}_0 |\psi(t)\rangle\|}.
\tag{3.139}
$$
This stochastic Schrödinger evolution can be numerically simulated; each simulated quantum trajectory is different, but averaging over a sample of many such trajectories reproduces the evolution of the density operator as described by the master equation. Simulating the stochastic Schrödinger equation may have advantages over simulating the master equation, since it is less costly to follow the evolution of a $d$-dimensional state vector than a $d \times d$ density matrix.

### 3.5.3 Damped harmonic oscillator (p. 38)

As an example to illustrate the master equation, consider the case of a harmonic oscillator coupled to the electromagnetic field via
$$
\boldsymbol{H}' = \sum_k g_k (\boldsymbol{a}\boldsymbol{b}_k^\dagger + \boldsymbol{a}^\dagger \boldsymbol{b}_k),
\tag{3.140}
$$
where $\boldsymbol{a}$ is the annihilation operator of the oscillator, $\boldsymbol{b}_k^\dagger$ creates a photon in mode $k$, and $g_k$ is a coupling constant. Let’s also suppose that the environment is at zero temperature; then the excitation level of the oscillator can cascade down by successive emission of photons, but no absorption of photons will occur. If each photon, once emitted, never interacts again with the oscillator, the evolution is Markovian, and there is only one Lindblad jump operator:
$$
\boldsymbol{L} = \sqrt{\Gamma} \boldsymbol{a}.
\tag{3.141}
$$
Here $\Gamma$ is the rate for the oscillator to decay from the first excited ($n = 1$) state to the ground ($n = 0$) state, which can be computed as $\Gamma = \sum_k \Gamma_k$, where $\Gamma_k$ is the rate for emission into mode $k$. The rate for the decay from level $n$ to $n-1$ is $n\Gamma$. (The $n$th level of excitation of the oscillator may be interpreted as a state of $n$ noninteracting particles; the rate is $n\Gamma$ because any one of the $n$ particles can decay.)

The Schrödinger-picture master equation in the Lindblad form becomes
$$
\dot{\boldsymbol{\rho}} = -i[\boldsymbol{H}_0, \boldsymbol{\rho}] + \Gamma\left( \boldsymbol{a}\boldsymbol{\rho}\boldsymbol{a}^\dagger - \frac{1}{2}\boldsymbol{a}^\dagger \boldsymbol{a}\boldsymbol{\rho} - \frac{1}{2}\boldsymbol{\rho}\boldsymbol{a}^\dagger \boldsymbol{a} \right),
\tag{3.142}
$$
where $\boldsymbol{H}_0 = \omega\boldsymbol{a}^\dagger \boldsymbol{a}$ is the Hamiltonian of the oscillator, while in the Heisenberg picture an operator $\boldsymbol{A}$ evolves according to
$$
\dot{\boldsymbol{A}} = i[\boldsymbol{H}_0, \boldsymbol{A}] + \Gamma\left( \boldsymbol{a}^\dagger \boldsymbol{A}\boldsymbol{a} - \frac{1}{2}\boldsymbol{a}^\dagger \boldsymbol{a}\boldsymbol{A} - \frac{1}{2}\boldsymbol{A}\boldsymbol{a}^\dagger \boldsymbol{a} \right).
\tag{3.143}
$$
The jump term describes the damping of the oscillator due to photon emission.

To study the effect of the jumps, consider the Heisenberg-picture evolution of the annihilation operator $\boldsymbol{a}(t)$. We can solve the master equation by making an ansatz $\boldsymbol{a}(t) = f(t)\boldsymbol{a}$, where $f(t)$ is a function of time, and then checking the self-consistency of the ansatz. Plugging into eq.(3.143) we find
$$
\begin{aligned}
\dot{f}(t)\boldsymbol{a} &= i\omega f(t)[\boldsymbol{a}^\dagger \boldsymbol{a}, \boldsymbol{a}] + \Gamma f(t) \left( \boldsymbol{a}^\dagger \boldsymbol{a}\boldsymbol{a} - \frac{1}{2}\boldsymbol{a}^\dagger \boldsymbol{a}\boldsymbol{a} - \frac{1}{2}\boldsymbol{a}\boldsymbol{a}^\dagger \boldsymbol{a} \right) \\
&= \left( i\omega + \frac{\Gamma}{2} \right) f(t)[\boldsymbol{a}^\dagger, \boldsymbol{a}]\boldsymbol{a} \implies \dot{f}(t) = -\left( i\omega + \frac{\Gamma}{2} \right) f(t),
\end{aligned}
\tag{3.144}
$$
which integrates to $f(t) = e^{-i\omega t - \Gamma t/2} f(0)$. We conclude that
$$
\boldsymbol{a}(t) = e^{-i\omega t - \Gamma t/2} \boldsymbol{a}(0),
\tag{3.145}
$$
and therefore the occupation number of the oscillator $\boldsymbol{n} = \boldsymbol{a}^\dagger \boldsymbol{a}$ decays in the Heisenberg picture according to
$$
\boldsymbol{n}(t) = e^{-\Gamma t} \boldsymbol{n}(0).
\tag{3.146}
$$
Thus $\Gamma$ is indeed the damping rate of the oscillator. If we interpret the $n$th excitation state of the oscillator as a state of $n$ noninteracting particles, each with a decay probability $\Gamma$ per unit time, then eq. (3.146) is just the exponential law satisfied by the population of decaying particles.

More interesting is what the master equation tells us about decoherence. In our amplitude damping model, it is the annihilation operator $\boldsymbol{a}$ and its adjoint that appear in the coupling $\boldsymbol{H}'$ of oscillator to environment, so we can anticipate that the oscillator's state will decohere in the basis of $\boldsymbol{a}$ eigenstates. The coherent state
$$
|\alpha\rangle = e^{-|\alpha|^2/2} e^{\alpha \boldsymbol{a}^\dagger} |0\rangle = e^{-|\alpha|^2/2} \sum_{n=0}^\infty \frac{\alpha^n}{\sqrt{n!}} |n\rangle,
\tag{3.147}
$$
is the normalized eigenstate of $\boldsymbol{a}$ with complex eigenvalue $\alpha$. The operator $\boldsymbol{a}$ is not Hermitian, and two coherent states with distinct eigenvalues $\alpha$ and $\beta$ are not orthogonal; rather
$$
|\langle\alpha|\beta\rangle|^2 = e^{-|\alpha|^2} e^{-|\beta|^2} e^{2\mathrm{Re}(\alpha^*\beta)} = \exp(-|\alpha - \beta|^2),
\tag{3.148}
$$
so the overlap is very small when $|\alpha - \beta|$ is large.

The solution to the Schrödinger-picture master equation is worked out in Exercise 3.9, where we find that an initial coherent state remains coherent, but with a decaying amplitude; after time $t$ the state $|\alpha\rangle$ evolves as
$$
|\alpha\rangle \mapsto |\alpha e^{-\Gamma t/2}\rangle
\tag{3.149}
$$
(in the rotating frame where the Hamiltonian evolution of the oscillator has been transformed away). We may also consider what happens when the initial state is a superposition of coherent states (a “cat state”)
$$
|\psi\rangle = N_{\alpha,\beta} (|\alpha\rangle + |\beta\rangle),
\tag{3.150}
$$
(where $N_{\alpha,\beta}$ is a normalization factor), or
$$
\boldsymbol{\rho} = N_{\alpha,\beta}^2 \left( |\alpha\rangle\langle\alpha| + |\alpha\rangle\langle\beta| + |\beta\rangle\langle\alpha| + |\beta\rangle\langle\beta| \right).
\tag{3.151}
$$
The off-diagonal terms in this density operator evolve as
$$
|\alpha\rangle\langle\beta| \mapsto e^{i\phi(\alpha,\beta)} e^{-\Gamma t|\alpha - \beta|^2/2} |\alpha e^{-\Gamma t/2}\rangle\langle\beta e^{-\Gamma t/2}|,
\tag{3.152}
$$
where $e^{i\phi(\alpha,\beta)}$ is a phase factor. Thus the off-diagonal terms decay exponentially with time, at a rate
$$
\Gamma_{\mathrm{decohere}} = \frac{1}{2}\Gamma |\alpha - \beta|^2
\tag{3.153}
$$
proportional to $|\alpha - \beta|^2$, the square of the separation of the two coherent states in phase space; the decoherence rate is much larger than the damping rate $\Gamma$ for $|\alpha - \beta|^2 \gg 1$.

This behavior is easy to interpret. The expectation value of the occupation number $\boldsymbol{n}$ in a coherent state is $\langle\boldsymbol{n}\rangle = \langle\alpha|\boldsymbol{a}^\dagger \boldsymbol{a}|\alpha\rangle = |\alpha|^2$. Therefore, if $\alpha, \beta$ have comparable moduli but significantly different phases (as for a superposition of minimum uncertainty wave packets centered at positions $x$ and $-x$), the decoherence rate is comparable to $\Gamma\langle\boldsymbol{n}\rangle$, the rate for emission of a single photon. This rate is very large compared to the rate for a significant fraction of the oscillator energy to be dissipated, if $n$ is large.

We can also consider an oscillator coupled to an environment with a nonzero temperature. Again, the decoherence rate is roughly the rate for a single photon to be emitted or absorbed, but the rate may be much faster than at zero temperature. Because the photon modes with frequency comparable to the oscillator frequency $\omega$ have a thermal occupation number
$$
n_\gamma \approx \frac{T}{\hbar\omega},
\tag{3.154}
$$
(for $T \gg \hbar\omega$), the interaction rate is further enhanced by the factor $n_\gamma$. For an oscillator with energy $E = \hbar\omega n_{\mathrm{osc}}$, we have
$$
\frac{\Gamma_{\mathrm{decohere}}}{\Gamma_{\mathrm{damp}}} \sim n_{\mathrm{osc}} n_\gamma \sim \frac{E}{\hbar\omega}\frac{T}{\hbar\omega} \sim \frac{m\omega^2 x^2}{\hbar\omega}\frac{T}{\hbar\omega} \sim x^2 \frac{mT}{\hbar^2} \sim \frac{x^2}{\lambda_T^2},
\tag{3.155}
$$
where $x$ is the amplitude of oscillation and $\lambda_T$ is the thermal de Broglie wavelength of the oscillating object. For macroscopic objects, decoherence is really *fast*.
