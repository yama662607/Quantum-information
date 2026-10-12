# Section 3.6 Transcript: Non-Markovian noise

**Source**: `quarto/assets/pdf/preskill/chap3.pdf` (Pages 41–47 top)  
**Status**: Complete, faithful transcript including all mathematical expressions and formatting.

---

## 3.6 Non-Markovian noise (p. 41)

### 3.6.1 Gaussian phase noise (p. 41)

The master equation describes the evolution of a quantum system subject to Markovian noise, but in some experimental systems the Markovian approximation is not very accurate. In this section we will discuss some of the features of decoherence for a system subjected to non-Markovian noise.

As a simple example, consider a single qubit with energy eigenstates $|0\rangle$ and $|1\rangle$, where the energy splitting between the two states fluctuates. For example, the qubit could be a spin-$\frac{1}{2}$ particle in a magnetic field pointing along the $z$-axis, where the magnetic field is not perfectly controlled in the laboratory. The Hamiltonian for this system is
$$
\boldsymbol{H} = -\frac{1}{2}\omega_{01}\boldsymbol{\sigma}_3 - \frac{1}{2}f(t)\boldsymbol{\sigma}_3,
\tag{3.156}
$$
where $f(t)$ is the fluctuating component of the magnetic field. This is a model of *classical noise*, arising not because the system interacts with an unobserved environment, but rather because a term in the system’s Hamiltonian fluctuates.

The function $f$ is treated stochastically; that is, we consider an ensemble of possible functions $\{f\}$, each with an assigned probability weight $\mu(f)$. We imagine that the actual $f(t)$ in each run of the experiment is selected by sampling from this distribution, and predict the observed behavior of the system by averaging over the distribution $\mu(f)$. The model is particularly simple because the unperturbed Hamiltonian $\boldsymbol{H}_0 = \frac{1}{2}\omega_{01}\boldsymbol{\sigma}_3$ [Note: sign convention in text vs eq.(3.156)] commutes with the noise term $\boldsymbol{H}_f = \frac{1}{2}f(t)\boldsymbol{\sigma}_3$, and in fact we can transform $\boldsymbol{H}_0$ away by going to the interaction picture.

The fluctuations induce dephasing of the qubit in the energy eigenstate basis. To analyze the dephasing, we will make a further simplifying assumption, that the noise is Gaussian. Whether the noise is classical of quantum, this Gaussian approximation often applies in laboratory situations where the system is weakly coupled to many different fluctuating variables in the environment. We denote averaging over the distribution $\mu(f)$ by $[\cdot]$, and assume the distribution to be stationary with mean zero; that is $[f(t)] = 0$, and $[f(t)f(t')] = K(t - t')$ is a function only of the difference $t - t'$, which is called the *covariance* of the distribution. The Gaussian distribution can be characterized by its generating functional $Z[J]$, which can be expressed in terms of the covariance as
$$
Z[J] \equiv \left[ e^{\int dt J(t)f(t)} \right]_f = \exp\left( \frac{1}{2}\int dt dt' J(t)K(t - t')J(t') \right).
\tag{3.157}
$$
An initial density operator $\boldsymbol{\rho}(0)$ evolves in time $T$ to
$$
\boldsymbol{\rho}(T) = \left[ \exp\left( i\int_0^T \frac{1}{2}f(t)\boldsymbol{\sigma}_3 \right) \boldsymbol{\rho}(0) \exp\left( -i\int_0^T \frac{1}{2}f(t)\boldsymbol{\sigma}_3 \right) \right].
\tag{3.158}
$$
The energy eigenstates $|0\rangle\langle0|$ or $|1\rangle\langle1|$ are not affected, but using eq.(3.157) we see that the coefficients of the off-diagonal entries $|0\rangle\langle1|$ and $|1\rangle\langle0|$ decay by the factor
$$
\exp\left( -\frac{1}{2}\int_0^T dt \int_0^T dt' K(t - t') \right) = \exp\left( -\frac{1}{2}\int_0^T dt \int_0^T dt' \int_{-\infty}^\infty \frac{d\omega}{2\pi} e^{-i\omega(t - t')}\tilde{K}(\omega) \right);
\tag{3.159}
$$
here we have introduced the Fourier transform $\tilde{K}(\omega)$ of the covariance $K(t)$, which is said to be the *spectral density* or *power spectrum* of the noise. Doing the $t$ and $t'$ integrals we obtain
$$
\exp\left( -\frac{1}{2}\int_{-\infty}^\infty \frac{d\omega}{2\pi} \tilde{K}(\omega) W_T(\omega) \right)
\tag{3.160}
$$
where $W_T(\omega)$ is the smooth window function
$$
W_T(\omega) = \left| \int_0^T dt e^{-i\omega t} \right|^2 = \frac{4}{\omega^2}\sin^2(\omega T/2),
\tag{3.161}
$$
which has most of its support on the interval $[0, 2\pi/T]$.

Assuming that $\tilde{K}(\omega = 0)$ is finite, we expect that for $T$ sufficiently large, $\tilde{K}(\omega)$ can be regarded as approximately constant in the region where $W_T(\omega)$ is supported. Using $\int_{-\infty}^\infty dx \frac{\sin^2 x}{x^2} = \pi$, we then obtain the decay factor $e^{-\Gamma_2 T}$, where the dephasing rate $\Gamma_2$ is
$$
\Gamma_2 = \tilde{K}(\omega = 0).
\tag{3.162}
$$
(Here we've assumed that $\tilde{K}(\omega)$ is continuous at $\omega = 0$ — otherwise we should average its limiting values as $\omega$ approaches zero from positive and negative values.) If the spectral density is flat (“white noise”), this formula for $\Gamma_2$ applies at any time $T$, but in general, the time scale for which dephasing can be described by a rate $\Gamma_2$ depends on the shape of the noise's spectral density. In effect, an experimentalist who measures the dephasing time $T_2 = \Gamma_2^{-1}$ of a qubit is probing the noise power at low frequency.

Crudely speaking, we expect $\tilde{K}(\omega)$ to be roughly constant in the interval $[0, \omega_c]$, where $\omega_c = 2\pi/\tau_c$, and $\tau_c$ is a characteristic “autocorrelation” or “memory” time of the noise. That is, $\tau_c$ is chosen so that the correlation function $K(t - t')$ is small for $|t - t'| \gg \tau_c$. Thus we see that one can speak of a “dephasing rate” $\Gamma_2$ (and a corresponding dephasing time $T_2 = \Gamma_2^{-1}$) if the evolution is sufficiently “coarse-grained” in time. For the purpose of describing evolution over a time period $T \gg \tau_c$, the window function $W_T(\omega)$ is mostly supported within the interval $[0, \omega_c]$ where $\tilde{K}(\omega)$ is approximately constant; therefore the non-Markovian noise model can be replaced by a corresponding effective Markovian model in which the memory of the fluctuations can be neglected, as in our analysis of dephasing in §3.4.2. But for $T \ll \tau_c$ such a description may not be applicable.

### 3.6.2 Spin echo (p. 43)

Strategies for mitigating the damaging effects of the noise become possible when the noise autocorrelation time $\tau_c$ is long compared to the time scale over which the experimentalist can manipulate the system. For example, when observing the dephasing of a spin evolving for time $T$, we may apply a fast pulse that flips the spin about the $x$-axis at time $T/2$. Then the effects of low-frequency phase noise during the second half of the evolution will tend to compensate for the effects of the phase noise during the first half. This trick is called the *spin echo* phenomenon.

If we use this trick, the damping factor applied to $|0\rangle\langle1|$ is again given by
$$
\exp\left( -\frac{1}{2}\int_{-\infty}^\infty \frac{d\omega}{2\pi} \tilde{K}(\omega)W_T(\omega) \right)
\tag{3.163}
$$
but with a modified window function
$$
W_T(\omega) = \left| \int_0^T dt J(t) e^{i\omega t} \right|^2,
\tag{3.164}
$$
where $J(t)$ is a modulating function that expresses the effect of the spin echo pulse sequence. For example, if we flip the spin at time $T/2$, then $J(t)$ is $+1$ in the interval $[0, T/2]$ and $-1$ in the interval $[T/2, T]$; therefore
$$
\begin{aligned}
W_T(w) &= \frac{1}{\omega^2} \left| 1 - 2e^{i\omega T/2} + e^{i\omega T} \right|^2 \\
&= \frac{1}{\omega^2} \left| \frac{1 - e^{i\omega T/2}}{1 + e^{i\omega T/2}} (1 - e^{i\omega T}) \right|^2 \\
&= \tan^2(\omega T/4) \cdot \frac{4}{\omega^2}\sin^2(\omega t/2).
\end{aligned}
\tag{3.165}
$$
[Note: Text has $W_T(w)$ and $\sin^2(\omega t/2)$ in eq.(3.165); physically $W_T(\omega)$ and $\sin^2(\omega T/2)$]

In effect, the spin echo modifies $\tilde{K}(\omega)$ by the multiplicative factor $\tan^2(\omega T/4)$, which suppresses the low frequency noise.

The suppression can be improved further by using more pulses. In practice, pulses have bounded strength and nonzero duration, which places limitations on the effectiveness of this strategy.

### 3.6.3 Qubits as noise spectrometers (p. 44)

Now let's consider a different model of classical noise, in which the fluctuating term does not commute with the unperturbed Hamiltonian:
$$
\boldsymbol{H} = -\frac{1}{2}\omega_{01}\boldsymbol{\sigma}_3 + f(t)\boldsymbol{\sigma}_1.
\tag{3.166}
$$
In this model the fluctuating field can induce transitions among the energy eigenstates, at a rate that can be computed using lowest-order interaction-picture perturbation theory if the noise is weak. The probability that a qubit prepared in the state $|1\rangle$ at time $0$ is observed in the state $|0\rangle$ at time $T$, averaged over the fluctuating classical field, is
$$
\begin{aligned}
\mathrm{Prob}(1 \to 0) &= \left[ \left| -i \int_0^T dt f(t) e^{-i\omega_{01}t} \langle0|\boldsymbol{\sigma}_1|1\rangle \right|^2 \right] \\
&= \int_0^T dt \int_0^T dt' e^{-i\omega_{01}(t - t')} [f(t)f(t')] \\
&= \int_{-\infty}^\infty \frac{d\omega}{2\pi} \tilde{K}(\omega) W_T(\omega - \omega_{01}).
\end{aligned}
\tag{3.167}
$$
This expression is similar to the formula eq.(3.160) for the off-diagonal term in the density operator obtained in the dephasing model, except that now the center of the window function has been shifted to the frequency $\omega_{01}$ of the transition.

As before, if we consider the observation time $T$ to be large compared to the autocorrelation time $\tau_c$ of the noise, then the support of the window function is narrow, and $\tilde{K}(\omega)$ is approximately constant in the window. Thus, after a suitable coarse-graining of the time evolution, we may identify a rate for the decay of the qubit
$$
\Gamma_\downarrow = \tilde{K}(\omega = \omega_{01}).
\tag{3.168}
$$
Similarly, for the transition from ground state to excited state, we find
$$
\Gamma_\uparrow = \tilde{K}(\omega = -\omega_{01}).
\tag{3.169}
$$
Thus negative frequency noise transfers energy from the noise reservoir to the qubit, exciting the qubit, while positive frequency noise transfers energy from qubit to the noise reservoir, returning the excited qubit to the ground state. (Dephasing of a qubit, in contrast, involves a negligible exchange of energy and therefore is controlled by low frequency noise.) We conclude that an experimentalist capable of varying the energy splitting $\omega_{01}$ and measuring the qubit’s transition rate can determine how the noise power depends on the frequency.

For the case we have considered in which the noise source is classical, $f(t)$ and $f(t')$ are real commuting variables; therefore $K(t)$ is an even function of $t$ and correspondingly $\tilde{K}(\omega)$ is an even function of $\omega$. Classical noise is spectrally symmetric, and the rates for excitation and decay are equal.

On the other hand, noise driven by a quantized thermal “bath” can be spectrally asymmetric. When the qubit comes to thermal equilibrium with the bath, up and down transitions occur at equal rates. If $p_0$ denotes the probability that the qubit is in the ground state $|0\rangle$ and $p_1$ denotes the probability that the qubit is in the excited state $|1\rangle$, then in equilibrium
$$
p_0 \Gamma_\uparrow = p_1 \Gamma_\downarrow \implies \frac{\tilde{K}(-\omega_{01})}{\tilde{K}(\omega_{01})} = \frac{p_1}{p_0} = e^{-\beta\omega_{01}};
\tag{3.170}
$$
the ratio of noise strengths at positive and negative frequencies is given (for a thermal bath) by a Boltzmann factor; this property of the noise is called the *Kubo-Martin-Schwinger (KMS) condition*. The noise becomes classical in the high-temperature limit $\beta\omega_{01} \ll 1$, and is in the deeply quantum regime for $\beta\omega_{01} \gg 1$.

### 3.6.4 Spin-boson model at nonzero temperature (p. 45)

To turn our model of classical dephasing noise into a quantum model, we replace the stochastic classical field $f(t)$ by an operator acting on a quantized bath. The noise will still be Gaussian if the bath is a system of harmonic oscillators, uncoupled to one another and each coupled linearly to the dephasing qubit. The Hamiltonian for the system $A$ and bath $B$ is
$$
\boldsymbol{H}_A + \boldsymbol{H}_B + \boldsymbol{H}_{AB} = -\frac{1}{2}\omega_{01}\boldsymbol{\sigma}_3 + \sum_k \omega_k \boldsymbol{a}_k^\dagger \boldsymbol{a}_k - \frac{1}{2}\boldsymbol{\sigma}_3 \left( \sum_k g_k \boldsymbol{a}_k + g_k^* \boldsymbol{a}_k^\dagger \right),
\tag{3.171}
$$
which is called the *spin-boson model*, as it describes a single spin-$\frac{1}{2}$ particle coupled to many bosonic variables. This is a model of dephasing because the coupling of the spin to the bath is diagonal in the spin’s energy eigenstate basis. (Otherwise the physics of the model would be harder to analyze.) Despite its simplicity, the spin-boson model provides a reasonably realistic description of dephasing for a qubit weakly coupled to many degrees of freedom in the environment.

If there are many oscillators, the sum over $k$ can be approximated by a frequency integral:
$$
\sum_k |g_k|^2 \approx \int_0^\infty d\omega J(\omega),
\tag{3.172}
$$
where $J(\omega)$ is said to be the *spectral function* of the oscillator bath. Let’s assume that the bath is in thermal equilibrium at temperature $\beta^{-1}$. In principle, the coupling to the system could tweak the equilibrium distribution of the bath, but we assume that this effect is negligible, because the bath is much bigger than the system. The fluctuations of the bath are Gaussian, and the average over the ensemble of classical functions in our previous analysis can be replaced by the thermal expectation value:
$$
[f(t)f(0)] \mapsto \langle \boldsymbol{f}(t)\boldsymbol{f}(0) \rangle_\beta \equiv \mathrm{tr}\left( e^{-\beta\boldsymbol{H}_B} \boldsymbol{f}(t)\boldsymbol{f}(0) \right),
\tag{3.173}
$$
where now $\boldsymbol{f}(t)$ denotes the operator
$$
\boldsymbol{f}(t) = e^{it\boldsymbol{H}_B} \boldsymbol{f}(0) e^{-it\boldsymbol{H}_B} = \sum_k \left( g_k \boldsymbol{a}_k e^{-i\omega_k t} + g_k^* \boldsymbol{a}_k^\dagger e^{i\omega_k t} \right).
\tag{3.174}
$$
We see that
$$
K_\beta(t) \equiv \langle \boldsymbol{f}(t)\boldsymbol{f}(0) \rangle_\beta = \sum_k |g_k|^2 \langle e^{-i\omega_k t}\boldsymbol{a}_k \boldsymbol{a}_k^\dagger + e^{i\omega_k t}\boldsymbol{a}_k^\dagger \boldsymbol{a}_k \rangle_\beta.
\tag{3.175}
$$
From the Planck distribution, we find
$$
\begin{aligned}
\langle \boldsymbol{a}_k^\dagger \boldsymbol{a}_k \rangle_\beta &= \frac{1}{e^{\beta\omega_k} - 1} = \frac{1}{2}\coth(\beta\omega_k/2) - \frac{1}{2}, \\
\langle \boldsymbol{a}_k \boldsymbol{a}_k^\dagger \rangle_\beta &= \langle \boldsymbol{a}_k^\dagger \boldsymbol{a}_k + 1 \rangle_\beta = \frac{1}{2}\coth(\beta\omega_k/2) + \frac{1}{2},
\end{aligned}
\tag{3.176}
$$
and by Fourier transforming we obtain the spectral density of the noise
$$
\begin{aligned}
\tilde{K}_\beta(\omega) &\equiv \int_{-\infty}^\infty dt e^{i\omega t} K_\beta(t) \\
&= \sum_k |g_k|^2 \left( 2\pi\delta(\omega - \omega_k)\langle \boldsymbol{a}_k \boldsymbol{a}_k^\dagger \rangle_\beta + 2\pi\delta(\omega + \omega_k)\langle \boldsymbol{a}_k^\dagger \boldsymbol{a}_k \rangle_\beta \right),
\end{aligned}
\tag{3.177}
$$
which may be written as
$$
\begin{aligned}
\tilde{K}_\beta(\omega) &= \pi J(\omega) (\coth(\beta\omega/2) + 1), \quad \omega > 0, \\
\tilde{K}_\beta(\omega) &= \pi J(\omega) (\coth(\beta\omega/2) - 1), \quad \omega < 0.
\end{aligned}
\tag{3.178}
$$
Thus, as we anticipated, the noise power spectrum exhibits the spectral asymmetry required by the KMS condition — the spectral density $\tilde{K}_\beta(-\omega)$ of the noise at negative frequency is supressed relative to the spectral density $\tilde{K}_\beta(\omega)$ at positive frequency by the Boltzmann factor $e^{-\beta\omega}$.

Since the window function $W_T(\omega)$ is an even function of $\omega$, only the even part of $\tilde{K}_\beta(\omega)$ contributes to the attenuation of $|0\rangle\langle1|$; the attenuation factor
$$
\exp\left( -\frac{1}{2}\int_{-\infty}^\infty \frac{d\omega}{2\pi} \tilde{K}_\beta(\omega)W_T(\omega) \right),
\tag{3.179}
$$
therefore becomes
$$
\exp\left( -\int_0^\infty d\omega J(\omega) \frac{2\sin^2(\omega T/2)}{\omega^2} \coth(\beta\omega/2) \right).
\tag{3.180}
$$
A dephasing rate can be identified if the spectral function $J(\omega)$ behaves suitably at low frequency; the attenuation factor is $e^{-\Gamma_2 T}$ in the limit $T \to \infty$ where
$$
\Gamma_2 = \lim_{\omega\to0} \tilde{K}_\beta(\omega) = \lim_{\omega\to0} 2\pi J(\omega)/(\beta\omega),
\tag{3.181}
$$
assuming that this limit exists. The noise is said to be *Ohmic* if $J(\omega) \approx A\omega$ is linear in $\omega$ at low frequency, and in that case the dephasing rate becomes $\Gamma_2 = 2\pi A\beta^{-1}$ in the limit of long time $T$.
