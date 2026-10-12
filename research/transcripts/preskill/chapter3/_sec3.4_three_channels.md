# Section 3.4 Transcript: Three quantum channels

**Source**: `quarto/assets/pdf/preskill/chap3.pdf` (Pages 24–34 top)  
**Status**: Complete, faithful transcript including all mathematical expressions and formatting.

---

## 3.4 Three quantum channels (p. 24)

The best way to familiarize ourselves with the concept of a quantum channel is to study a few examples. We will now consider three examples (all interesting and useful) of channels acting on a single qubit. If we wish we may imagine that the channel $\mathcal{E}$ describes the fate of quantum information that is transmitted with some loss of fidelity from a sender to a receiver. Or, if we prefer, we may imagine that the transmission is in time rather than space; that is, $\mathcal{E}$ describes the time evolution of a quantum system that interacts with its environment.

### 3.4.1 Depolarizing channel (p. 24)

The depolarizing channel is a model of a decohering qubit that has particularly nice symmetry properties. We can describe it by saying that, with probability $1-p$ the qubit remains intact, while with probability $p$ an “error” occurs. The error can be of any one of three types, where each type of error is equally likely. If $\{|0\rangle, |1\rangle\}$ is an orthonormal basis for the qubit, the three types of errors can be characterized as:

1. Bit flip error:
$$
\begin{aligned}
|0\rangle &\mapsto |1\rangle \\
|1\rangle &\mapsto |0\rangle
\end{aligned}
\quad\text{or}\quad
|\psi\rangle \mapsto \boldsymbol{\sigma}_1 |\psi\rangle, \quad
\boldsymbol{\sigma}_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},
$$

2. Phase flip error:
$$
\begin{aligned}
|0\rangle &\mapsto |0\rangle \\
|1\rangle &\mapsto -|1\rangle
\end{aligned}
\quad\text{or}\quad
|\psi\rangle \mapsto \boldsymbol{\sigma}_3 |\psi\rangle, \quad
\boldsymbol{\sigma}_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$

3. Both:
$$
\begin{aligned}
|0\rangle &\mapsto +i|1\rangle \\
|1\rangle &\mapsto -i|0\rangle
\end{aligned}
\quad\text{or}\quad
|\psi\rangle \mapsto \boldsymbol{\sigma}_2 |\psi\rangle, \quad
\boldsymbol{\sigma}_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}.
$$

If an error occurs, then $|\psi\rangle$ evolves to an ensemble of the three states $\boldsymbol{\sigma}_1|\psi\rangle, \boldsymbol{\sigma}_2|\psi\rangle, \boldsymbol{\sigma}_3|\psi\rangle$, all occurring with equal likelihood.

*Unitary representation.* The depolarizing channel mapping qubit $A$ to $A$ can be realized by an isometry mapping $A$ to $AE$, where $E$ is a four-dimensional environment, acting as
$$
\boldsymbol{U}_{A \to AE} : |\psi\rangle_A \mapsto \sqrt{1-p} \, |\psi\rangle_A \otimes |0\rangle_E + \sqrt{\frac{p}{3}} \left( \boldsymbol{\sigma}_1|\psi\rangle_A \otimes |1\rangle_E + \boldsymbol{\sigma}_2|\psi\rangle_A \otimes |2\rangle_E + \boldsymbol{\sigma}_3|\psi\rangle_A \otimes |3\rangle_E \right).
\tag{3.83}
$$
The environment evolves to one of four mutually orthogonal states that “keep a record” of what transpired; if we could only measure the environment in the basis $\{|a\rangle_E, a = 0, 1, 2, 3\}$, we would know what kind of error had occurred (and we would be able to intervene and reverse the error).

*Operator-sum representation.* To obtain an operator-sum representation of the channel, we evaluate the partial trace over the environment in the $\{|a\rangle_E\}$ basis. Then
$$
\boldsymbol{M}_a = {}_E\langle a|\boldsymbol{U},
\tag{3.84}
$$
so that
$$
\boldsymbol{M}_0 = \sqrt{1-p} \, \boldsymbol{I}, \quad \boldsymbol{M}_1 = \sqrt{\frac{p}{3}} \, \boldsymbol{\sigma}_1, \quad \boldsymbol{M}_2 = \sqrt{\frac{p}{3}} \, \boldsymbol{\sigma}_2, \quad \boldsymbol{M}_3 = \sqrt{\frac{p}{3}} \, \boldsymbol{\sigma}_3.
\tag{3.85}
$$
Using $\boldsymbol{\sigma}_i^2 = \boldsymbol{I}$, we can readily check the normalization condition
$$
\sum_a \boldsymbol{M}_a^\dagger \boldsymbol{M}_a = \left((1-p) + 3\frac{p}{3}\right) \boldsymbol{I} = \boldsymbol{I}.
\tag{3.86}
$$
A general initial density matrix $\boldsymbol{\rho}$ of the qubit evolves as
$$
\boldsymbol{\rho} \mapsto \boldsymbol{\rho}' = (1-p)\boldsymbol{\rho} + \frac{p}{3} \left( \boldsymbol{\sigma}_1 \boldsymbol{\rho} \boldsymbol{\sigma}_1 + \boldsymbol{\sigma}_2 \boldsymbol{\rho} \boldsymbol{\sigma}_2 + \boldsymbol{\sigma}_3 \boldsymbol{\rho} \boldsymbol{\sigma}_3 \right),
\tag{3.87}
$$
where we are summing over the four (in principle distinguishable) possible final states of the environment.

*Relative-state representation.* We can also characterize the channel by introducing a reference qubit $R$ and describing how a maximally-entangled state of the two qubits $RA$ evolves, when the channel acts only on $A$. There are four mutually orthogonal maximally entangled states, which may be denoted
$$
\begin{aligned}
|\phi^+\rangle &= \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle), \\
|\phi^-\rangle &= \frac{1}{\sqrt{2}}(|00\rangle - |11\rangle), \\
|\psi^+\rangle &= \frac{1}{\sqrt{2}}(|01\rangle + |10\rangle), \\
|\psi^-\rangle &= \frac{1}{\sqrt{2}}(|01\rangle - |10\rangle).
\end{aligned}
\tag{3.88}
$$
If the initial state is $|\phi^+\rangle_{RA}$, then when the depolarizing channel acts on qubit $A$, the entangled state evolves as
$$
|\phi^+\rangle\langle\phi^+| \mapsto (1-p)|\phi^+\rangle\langle\phi^+| + \frac{p}{3} \left( |\psi^+\rangle\langle\psi^+| + |\psi^-\rangle\langle\psi^-| + |\phi^-\rangle\langle\phi^-| \right).
\tag{3.89}
$$
The “worst possible” quantum channel has $p = 3/4$, for in that case the initial entangled state evolves as
$$
|\phi^+\rangle\langle\phi^+| \mapsto \frac{1}{4} \left( |\phi^+\rangle\langle\phi^+| + |\phi^-\rangle\langle\phi^-| + |\psi^+\rangle\langle\psi^+| + |\psi^-\rangle\langle\psi^-| \right) = \frac{1}{4}\boldsymbol{I};
\tag{3.90}
$$
it becomes the maximally mixed density matrix on $RA$. By the relative-state method, then, we see that a pure state $|\psi\rangle$ of qubit $A$ evolves as
$$
(|\psi\rangle\langle\psi|)_A \mapsto {}_R\langle\psi^*| 2 \left( \frac{1}{4}\boldsymbol{I}_{RA} \right) |\psi^*\rangle_R = \frac{1}{2}\boldsymbol{I}_A,
\tag{3.91}
$$
where the factor of two has been inserted because here we have used the standard normalization of the entangled states, instead of the unconventional normalization used in our earlier discussion of the relative-state method. We see that, for $p = 3/4$, the qubit is mapped to the maximally mixed density operator on $A$, irrespective of the value of the initial state $|\psi\rangle_A$. It is as though the channel threw away the initial quantum state, and replaced it by completely random junk.

An alternative way to express the evolution of the maximally entangled state is
$$
|\phi^+\rangle\langle\phi^+| \mapsto \left(1 - \frac{4}{3}p\right) |\phi^+\rangle\langle\phi^+| + \frac{4}{3}p \left( \frac{1}{4}\boldsymbol{I}_{RA} \right).
\tag{3.92}
$$
Thus instead of saying that an error occurs with probability $p$, with errors of three types all equally likely, we could instead say that an error occurs with probability $4/3p$, where the error completely “randomizes” the state (at least we can say that for $p \le 3/4$). The existence of two natural ways to define an “error probability” for this channel can sometimes cause confusion.

One useful measure of how well the channel preserves the original quantum information is called the “entanglement fidelity” $F_e$. It quantifies how “close” the final density matrix is to the original maximally entangled state $|\phi^+\rangle$ after the action of $I \otimes \mathcal{E}$:
$$
F_e = \langle\phi^+|\boldsymbol{\rho}'|\phi^+\rangle.
\tag{3.93}
$$
For the depolarizing channel, we have $F_e = 1 - p$, and we can interpret $F_e$ as the probability that no error occurred.

*Bloch-sphere representation.* It is also instructive to see how the depolarizing channel acts on the Bloch sphere. An arbitrary density matrix for a single qubit can be written as
$$
\boldsymbol{\rho}(\vec{P}) = \frac{1}{2} \left( \boldsymbol{I} + \vec{P} \cdot \vec{\boldsymbol{\sigma}} \right),
\tag{3.94}
$$
where $\vec{P}$ is the “spin polarization” of the qubit. The depolarizing channel maps this state to
$$
\boldsymbol{\rho}' = \left( 1 - \frac{4}{3}p \right) \boldsymbol{\rho} + \frac{4}{3}p \boldsymbol{I} = \boldsymbol{\rho}(\vec{P}')
\tag{3.95}
$$
[Note: Text in original has $+\frac{4}{3}p\boldsymbol{I}$; physically $+\frac{4}{3}p\frac{\boldsymbol{I}}{2}$ would preserve trace, which yields $\vec{P}'$ below]
where
$$
\vec{P}' = \left( 1 - \frac{4}{3}p \right) \vec{P}
\tag{3.96}
$$
Hence the Bloch sphere contracts uniformly under the action of the channel (for $p \le 3/4$); the spin polarization shrinks by the factor $1 - \frac{4}{3}p$ (which is why we call it the depolarizing channel).

*Reversibility?* Why do we say that the channel is not invertible? Evidently we can reverse a uniform contraction of the sphere with a uniform inflation. But the trouble is that the inflation of the Bloch sphere is not a channel, because it is not positive. Inflation will take some values of $\vec{P}$ with $|\vec{P}| \le 1$ to values with $|\vec{P}| > 1$, and so will take a density operator to an operator with a negative eigenvalue. Decoherence can shrink the ball, but no physical process can blow it up again! A channel running backwards in time is not a channel.

### 3.4.2 Dephasing channel (p. 27)

Our next example is the dephasing channel, also called the *phase-damping channel*. This case is particularly instructive, because it provides a revealing caricature of decoherence in realistic physical situations, with all inessential mathematical details stripped away.

*Unitary representation.* An isometric representation of the channel is
$$
\begin{aligned}
|0\rangle_A &\mapsto \sqrt{1-p} \, |0\rangle_A \otimes |0\rangle_E + \sqrt{p} \, |0\rangle_A \otimes |1\rangle_E, \\
|1\rangle_A &\mapsto \sqrt{1-p} \, |1\rangle_A \otimes |0\rangle_E + \sqrt{p} \, |1\rangle_A \otimes |2\rangle_E.
\end{aligned}
\tag{3.97}
$$
In this case, unlike the depolarizing channel, qubit $A$ does not make any transitions in the $\{|0\rangle, |1\rangle\}$ basis. Instead, the environment “scatters” off of the qubit occasionally (with probability $p$), being kicked into the state $|1\rangle_E$ if $A$ is in the state $|0\rangle_A$ and into the state $|2\rangle_E$ if $A$ is in the state $|1\rangle_A$. Furthermore, also unlike the depolarizing channel, the channel picks out a preferred basis for qubit $A$; the basis $\{|0\rangle, |1\rangle\}$ is the only basis in which bit flips never occur.

*Kraus operators.* Evaluating the partial trace over $E$ in the $\{|0\rangle_E, |1\rangle_E, |2\rangle_E\}$ basis, we obtain the Kraus operators
$$
\boldsymbol{M}_0 = \sqrt{1-p} \, \boldsymbol{I}, \quad \boldsymbol{M}_1 = \sqrt{p} \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}, \quad \boldsymbol{M}_2 = \sqrt{p} \begin{pmatrix} 0 & 0 \\ 0 & 1 \end{pmatrix}.
\tag{3.98}
$$
It is easy to check that $\boldsymbol{M}_0^2 + \boldsymbol{M}_1^2 + \boldsymbol{M}_2^2 = \boldsymbol{I}$. In this case, three Kraus operators are not really needed; a representation with two Kraus operators is possible. Expressing
$$
\boldsymbol{M}_1 = \frac{\sqrt{p}}{2} (\boldsymbol{I} + \boldsymbol{\sigma}_3), \quad \boldsymbol{M}_2 = \frac{\sqrt{p}}{2} (\boldsymbol{I} - \boldsymbol{\sigma}_3),
\tag{3.99}
$$
we find
$$
\mathcal{E}(\boldsymbol{\rho}) = \sum_a \boldsymbol{M}_a \boldsymbol{\rho} \boldsymbol{M}_a = \left( 1 - \frac{1}{2}p \right) \boldsymbol{\rho} + \frac{1}{2}p \, \boldsymbol{\sigma}_3 \boldsymbol{\rho} \boldsymbol{\sigma}_3,
\tag{3.100}
$$
so an alternative description of the channel is that $\boldsymbol{\sigma}_3$ is applied with probability $p/2$ and nothing happens with probability $(1 - p/2)$. An initial density matrix $\boldsymbol{\rho}$ evolves to
$$
\mathcal{E}\begin{pmatrix} \rho_{00} & \rho_{01} \\ \rho_{10} & \rho_{11} \end{pmatrix} = \begin{pmatrix} \rho_{00} & (1-p)\rho_{01} \\ (1-p)\rho_{10} & \rho_{11} \end{pmatrix};
\tag{3.101}
$$
the on-diagonal terms in $\boldsymbol{\rho}$ remain invariant while the off-diagonal terms decay.

*Continuous dephasing.* We may also consider dephasing that occurs continuously in time. Suppose that the probability of a scattering event per unit time is $\Gamma$, so that $p = \Gamma \Delta t \ll 1$ when a brief time interval $\Delta t$ elapses. The evolution over a time $t = n\Delta t$ is governed by $\mathcal{E}^n$ ($\mathcal{E}$ repeated $n$ times in succession), so that the off-diagonal terms in the density operator become suppressed by
$$
(1-p)^n = (1 - \Gamma t / n)^n \to e^{-\Gamma t},
\tag{3.102}
$$
taking the limit $n \to \infty$ with $t$ fixed. Thus, if we prepare an initial pure state $\alpha|0\rangle + \beta|1\rangle$, then after a time $t \gg \Gamma^{-1}$, the density operator evolves as
$$
\begin{pmatrix} |\alpha|^2 & \alpha\beta^* \\ \alpha^*\beta & |\beta|^2 \end{pmatrix} \mapsto \begin{pmatrix} |\alpha|^2 & 0 \\ 0 & |\beta|^2 \end{pmatrix};
\tag{3.103}
$$
The state decoheres, in the preferred basis $\{|0\rangle, |1\rangle\}$.

*Bloch-sphere representation.* We can compute how the polarization of the density operator evolves using the representation of the channel eq.(3.100), finding
$$
\boldsymbol{\rho}(\vec{P}) = \frac{1}{2} \left( \boldsymbol{I} + \vec{P} \cdot \vec{\boldsymbol{\sigma}} \right) \mapsto \boldsymbol{\rho}(\vec{P}')
\tag{3.104}
$$
where
$$
P'_{1,2} = (1-p)P_{1,2}, \quad P'_3 = P_3;
\tag{3.105}
$$
the Bloch ball shrinks to a prolate spheroid aligned with the $z$ axis. Under continuous dephasing, the ball deflates in the $x$-$y$ plane, degenerating to the $z$ axis in the limit of large $\Gamma t$.

You might wonder whether there is a quantum channel which causes just one component of the polarization to decay, mapping the Bloch ball to an oblate spheroid which touches the Bloch sphere along its equator. In fact no such map can be completely positive (the *no-pancake theorem*). Up to a unitary change of basis, a pancake map shrinks the value of $P_2$ while preserving $P_1$ and $P_3$, which is equivalent to taking the transpose of the density operator with nonzero probability, and we have seen in §3.2.6 that the transpose map is not completely positive.

*Interpretation.* We might interpret the phase-damping channel as describing a heavy “classical” particle (e.g., an interstellar dust grain) interacting with a background gas of light particles (e.g., the 3K microwave photons). We can imagine that the dust is initially prepared in a superposition of position eigenstates $|\psi\rangle = \frac{1}{\sqrt{2}}(|x\rangle + |-x\rangle)$ (or more realistically a superposition of position-space wavepackets with little overlap). We might be able to monitor the behavior of the dust particle, but it is hopeless to keep track of the quantum state of all the photons that scatter from the particle; for our purposes, the quantum state of the particle is described by the density matrix $\boldsymbol{\rho}$ obtained by tracing over the photon degrees of freedom.

Our analysis of the phase damping channel indicates that if photons are scattered by the dust particle at a rate $\Gamma$, then the off-diagonal terms in $\boldsymbol{\rho}$ decay like $\exp(-\Gamma t)$, and so become completely negligible for $t \gg \Gamma^{-1}$. At that point, the coherence of the superposition of position eigenstates is completely lost – there is no chance that we can recombine the wavepackets and induce them to interfere. If we attempt to do a double-slit interference experiment with dust grains, we will not see any interference pattern if it takes a time $t \gg \Gamma^{-1}$ for the grain to travel from the source to the screen.

The dust grain is heavy. Because of its large inertia, its state of motion is little affected by the scattered photons. Thus, there are two disparate time scales relevant to its dynamics. On the one hand, there is a damping time scale, the time for a significant amount of the particle’s momentum to be transfered to the photons, which is a long time for such a heavy particle. On the other hand, there is the decoherence time scale. In this model, the time scale for decoherence is of order $\Gamma$, the time for a single photon to be scattered by the dust grain, which is far shorter than the damping time scale. For a macroscopic object, decoherence is fast.

As we have already noted, the phase-damping channel picks out a preferred basis for decoherence, which in our “interpretation” we have assumed to be the position-eigenstate basis. Physically, decoherence prefers the spatially localized states of the dust grain because the interactions of photons and grains are localized in space. Grains in distinguishable positions tend to scatter the photons of the environment into mutually orthogonal states.

Even if the separation between the “grains” were so small that it could not be resolved very well by the scattered photons, the decoherence process would still work in a similar way. Perhaps photons that scatter off grains at positions $x$ and $-x$ are not mutually orthogonal, but instead have an overlap
$$
\langle\gamma_+|\gamma_-\rangle = 1 - \varepsilon, \quad \varepsilon \ll 1.
\tag{3.106}
$$
The phase-damping channel would still describe this situation, but with $p$ replaced by $p\varepsilon$ (if $p$ is still the probability of a scattering event). Thus, the decoherence rate would become $\Gamma_{\mathrm{dec}} = \varepsilon\Gamma_{\mathrm{scat}}$, where $\Gamma_{\mathrm{scat}}$ is the scattering rate.

The intuition we distill from this simple model applies to a wide variety of physical situations. A coherent superposition of macroscopically distinguishable states of a “heavy” object decoheres very rapidly compared to its damping rate. The spatial locality of the interactions of the system with its environment gives rise to a preferred “local” basis for decoherence. The same principle applies to Schrödinger’s unfortunate cat, delicately prepared in a coherent superposition of its dead state and its alive state, two states that are easily distinguished by spatially localized probes. The cat quickly interacts with its environment, which is “scattered” into one of two mutually orthogonal states perfectly correlated with the cat’s state in the $\{|\mathrm{dead}\rangle, |\mathrm{alive}\rangle\}$ basis, thus transforming the cat into an incoherent mixture of those two basis states.

*Visibility.* On the other hand, for microscopic systems the time scale for decoherence need not be short compared to dynamical time scales. Consider for example a single atom, initially prepared in a uniform superposition of its ground state $|0\rangle$ and an excited state $|1\rangle$ with energy $\hbar\omega$ above the ground state energy. Neglecting decoherence, after time $t$ the atom’s state will be
$$
|\psi(t)\rangle = \frac{1}{\sqrt{2}} \left( |0\rangle + e^{-i\omega t}|1\rangle \right).
\tag{3.107}
$$
If dephasing occurs in the $\{|0\rangle, |1\rangle\}$ basis with rate $\Gamma$, the off-diagonal terms in the density operator decay, yielding the density operator
$$
\boldsymbol{\rho}(t) = \frac{1}{2} \begin{pmatrix} 1 & e^{i\omega t}e^{-\Gamma t} \\ e^{-i\omega t}e^{-\Gamma t} & 1 \end{pmatrix}.
\tag{3.108}
$$
If after time $t$ we measure the atom in the basis
$$
|\pm\rangle = \frac{1}{\sqrt{2}} (|0\rangle \pm |1\rangle),
\tag{3.109}
$$
the probability of the $+$ outcome is
$$
\mathrm{Prob}(+, t) = \langle+|\boldsymbol{\rho}(t)|+\rangle = \frac{1}{2} \left( 1 + e^{-\Gamma t}\cos\omega t \right).
\tag{3.110}
$$
In principle this time dependence of the probability can be measured by varying the time $t$ between the preparation and measurement, and by repeating the experiment many times for each $t$ to estimate the probability with high statistical confidence. The decoherence rate $\Gamma$ can be determined experimentally by fitting the declining visibility of the coherent oscillations of $\mathrm{Prob}(+, t)$ to a decaying exponential function of $t$.

### 3.4.3 Amplitude-damping channel (p. 31)

The amplitude-damping channel is a schematic model of the decay of an excited state of a (two-level) atom due to spontaneous emission of a photon. By detecting the emitted photon (“observing the environment”) we can perform a POVM that gives us information about the initial preparation of the atom.

*Unitary representation.* We denote the atomic ground state by $|0\rangle_A$ and the excited state of interest by $|1\rangle_A$. The “environment” is the electromagnetic field, assumed initially to be in its vacuum state $|0\rangle_E$. After we wait a while, there is a probability $p$ that the excited state has decayed to the ground state and a photon has been emitted, so that the environment has made a transition from the state $|0\rangle_E$ (“no photon”) to the state $|1\rangle_E$ (“one photon”). This evolution is described by a unitary transformation that acts on atom and environment according to
$$
\begin{aligned}
|0\rangle_A \otimes |0\rangle_E &\mapsto |0\rangle_A \otimes |0\rangle_E \\
|1\rangle_A \otimes |0\rangle_E &\mapsto \sqrt{1-p} \, |1\rangle_A \otimes |0\rangle_E + \sqrt{p} \, |0\rangle_A \otimes |1\rangle_E.
\end{aligned}
\tag{3.111}
$$
(Of course, if the atom starts out in its ground state, and the environment in its vacuum state, then no transition occurs.)

*Kraus operators.* By evaluating the partial trace over the environment in the basis $\{|0\rangle_E, |1\rangle_E\}$, we find the Kraus operators
$$
\boldsymbol{M}_0 = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{1-p} \end{pmatrix}, \quad \boldsymbol{M}_1 = \begin{pmatrix} 0 & \sqrt{p} \\ 0 & 0 \end{pmatrix},
\tag{3.112}
$$
and we can check that
$$
\boldsymbol{M}_0^\dagger \boldsymbol{M}_0 + \boldsymbol{M}_1^\dagger \boldsymbol{M}_1 = \begin{pmatrix} 1 & 0 \\ 0 & 1-p \end{pmatrix} + \begin{pmatrix} 0 & 0 \\ 0 & p \end{pmatrix} = \boldsymbol{I}.
\tag{3.113}
$$
The operator $\boldsymbol{M}_1$ induces a “quantum jump,” the decay from $|1\rangle_A$ to $|0\rangle_A$, and $\boldsymbol{M}_0$ describes how the state changes if no jump occurs. The density matrix evolves as
$$
\begin{aligned}
\boldsymbol{\rho} \mapsto \mathcal{E}(\boldsymbol{\rho}) &= \boldsymbol{M}_0 \boldsymbol{\rho} \boldsymbol{M}_0^\dagger + \boldsymbol{M}_1 \boldsymbol{\rho} \boldsymbol{M}_1^\dagger \\
&= \begin{pmatrix} \rho_{00} & \sqrt{1-p} \, \rho_{01} \\ \sqrt{1-p} \, \rho_{10} & (1-p) \, \rho_{11} \end{pmatrix} + \begin{pmatrix} p\rho_{11} & 0 \\ 0 & 0 \end{pmatrix} \\
&= \begin{pmatrix} \rho_{00} + p\rho_{11} & \sqrt{1-p} \, \rho_{01} \\ \sqrt{1-p} \, \rho_{10} & (1-p) \, \rho_{11} \end{pmatrix}.
\end{aligned}
\tag{3.114}
$$
*Time dependence.* If $\Gamma$ is the spontaneous decay rate per unit time, then the decay occurs with probability $p = \Gamma \Delta t \ll 1$ in a small time interval $\Delta t$. We find the density operator after time $t = n\Delta t$ by applying the channel $n$ times in succession. The $\rho_{11}$ matrix element then decays as
$$
\rho_{11} \mapsto (1-p)^n \rho_{11}, \quad\text{where}\quad (1-p)^n = (1 - \Gamma t / n)^n \to e^{-\Gamma t},
\tag{3.115}
$$
the expected exponential decay law, while the off-diagonal entries decay by the factor $(1-p)^{n/2} = e^{-\Gamma t/2}$; hence we find
$$
\boldsymbol{\rho}(t) = \begin{pmatrix} \rho_{00} + (1 - e^{-\Gamma t})\rho_{11} & e^{-\Gamma t/2}\rho_{01} \\ e^{-\Gamma t/2}\rho_{10} & e^{-\Gamma t}\rho_{11} \end{pmatrix}.
\tag{3.116}
$$
It is customary to use “$T_1$” to denote the exponential decay time for the excited population, and to use “$T_2$” to denote the exponential decay time for the off-diagonal terms in the density operator. In some systems where dephasing is very rapid $T_2$ is much shorter than $T_1$, but we see that for the amplitude-damping channel these two times are related and comparable:
$$
T_2 = 2\Gamma^{-1} = 2T_1.
\tag{3.117}
$$
By the time that $t \gg T_1$, the atom is in its ground state with high probability ($\rho_{00}(t) \approx 1$).

*Watching the environment.* So far we have described the evolution of the qubit under the assumption that the state of the environment is not observed. But now suppose we surround the atom with photon detectors, so we know whether a photon has been emitted or not. Rather than a channel, then, we consider a POVM performed on the atom.

Returning to the joint unitary dynamics of system and environment, we see that a coherent superposition of the atomic ground and excited states evolves as
$$
(\alpha|0\rangle_A + \beta|1\rangle_A) \otimes |0\rangle_E \mapsto (\alpha|0\rangle_A + \beta\sqrt{1-p} \, |1\rangle_A) \otimes |0\rangle_E + \beta\sqrt{p} \, |0\rangle_A \otimes |1\rangle_E;
\tag{3.118}
$$
To describe the system evolving continuously in time, we may consider applying this unitary map $n \gg 1$ times in succession, but where photons emitted at different times are perfectly distinguishable and hence orthogonal. The resulting POVM has $n+1$ Kraus operators, associated with the vacuum state of the environment and $n$ different possible single photon states:
$$
\boldsymbol{M}_0 = \begin{pmatrix} 1 & 0 \\ 0 & \sqrt{(1-p)^n} \end{pmatrix}, \quad \boldsymbol{M}_k = \begin{pmatrix} 0 & \sqrt{(1-p)^{k-1}p} \\ 0 & 0 \end{pmatrix},
\tag{3.119}
$$
for $k = 1, 2, \dots n$. Taking the continuous-time limit we find that if no spontaneous decay occurs for time $t$, the corresponding Kraus operator is
$$
\boldsymbol{M}_0 = \begin{pmatrix} 1 & 0 \\ 0 & e^{-\Gamma t/2} \end{pmatrix}.
\tag{3.120}
$$
If we detect a photon (and so project out a single-photon state of the environment), then we have prepared the state $|0\rangle_A$ of the atom. Not only that, we have prepared a state in which we know with certainty that the initial atomic state was the excited state $|1\rangle_A$; if the atom had started out in the ground state than it could not have decayed and no photon could have been detected.

On the other hand, if we detect no photon, and our photon detector has perfect efficiency, then we have projected out the vacuum state of the environment, and so have prepared the atomic state
$$
\boldsymbol{M}_0 (\alpha|0\rangle + \beta|1\rangle) = \alpha|0\rangle + e^{-\Gamma t/2}\beta|1\rangle,
\tag{3.121}
$$
up to a normalization factor. As time goes by, the *a posteriori* quantum state has larger and larger overlap with the ground state, because if it had started out in the excited state it should have decayed by now. In the limit $t \to \infty$ our POVM becomes an orthogonal measurement: either a photon is detected, in which case the initial state of the atom must have been $|1\rangle$, or no photon is detected, in which case the initial state must have been $|0\rangle$. It's odd but true: we can project out the state $|0\rangle$ of the atom by *not* detecting anything.
