# Section 2.6: How far apart are two quantum states? [PDF Pages 36-41]

<!-- ============================================================ -->
<!-- Source: chap2.pdf, Physical Pages: 36-41                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 36 -->
## 2.6 How far apart are two quantum states?

### 2.6.1 Fidelity and Uhlmann's theorem

The distinguishability of two pure states $|\psi\rangle$ and $|\phi\rangle$ is quantified by the deviation from 1 of their overlap $|\langle\phi|\psi\rangle|^2$, also called fidelity. For two density operators $\rho$ and $\sigma$ the fidelity is defined by

$$
F(\rho, \sigma) \equiv \left( \text{tr}\sqrt{\rho^{1/2} \sigma \rho^{1/2}} \right)^2.
$$ {#eq-2.122}

(Some authors use the name "fidelity" for the square root of this quantity.) The fidelity is nonnegative, vanishes if $\rho$ and $\sigma$ have support on mutually orthogonal subspaces, and attains its maximum value 1 if and only if the two states are identical. If $\rho = |\psi\rangle\langle\psi|$ is a pure state, then the fidelity is

$$
F(\rho, \sigma) = \langle\psi|\sigma|\psi\rangle.
$$ {#eq-2.123}

Suppose we perform an orthogonal measurement on $\rho$ with the two outcomes: "Yes" if the state is $|\psi\rangle$, "No" if the state is orthogonal to $|\psi\rangle$. Then the fidelity is the probability that the outcome is "Yes."

We may also express the fidelity in terms of the $L^1$ norm,

$$
F(\rho, \sigma) = \|\sigma^{1/2} \rho^{1/2}\|_1^2,
$$ {#eq-2.124}

where

$$
\|A\|_1 = \text{tr}\sqrt{A^\dagger A}.
$$ {#eq-2.125}

<!-- Page 37 -->
The $L^1$ norm is also sometimes called the trace norm. (For Hermitian $A$, $\|A\|_1$ is just the sum of the absolute values of its eigenvalues.) The fidelity $F(\rho, \sigma)$ is actually symmetric in its two arguments, although the symmetry is not manifest in eq. (2.122). To verify the symmetry, note that for any Hermitian $A$ and $B$, the $L^1$ norm obeys

$$
\|AB\|_1 = \|BA\|_1.
$$ {#eq-2.126}

This holds because $BAAB$ and $ABBA$ have the same eigenvalues --- if $|\psi\rangle$ is an eigenstate of $ABBA$ with eigenvalue $\lambda$, then $BA|\psi\rangle$ is an eigenstate of $BAAB$ with eigenvalue $\lambda$.

It is useful to know how the fidelity of two density operators is related to the overlap of their purifications. We say that $|\Phi\rangle_{AB}$ is a purification of the density operator $\rho_A$ if

$$
\rho_A = \text{tr}_B (|\Phi\rangle\langle\Phi|).
$$ {#eq-2.127}

If

$$
\rho = \sum_i p_i |i\rangle\langle i|,
$$ {#eq-2.128}

where $\{|i\rangle_A\}$ is an orthonormal basis for system $A$, then a particular purification of $\rho$ has the form

$$
|\Phi_\rho\rangle = \sum_i \sqrt{p_i} |i\rangle_A \otimes |i\rangle_B,
$$ {#eq-2.129}

where $\{|i\rangle_B\}$ is an orthonormal basis for system $B$. According to the HJW theorem, a general purification has the form

$$
|\Phi_\rho(V)\rangle = I \otimes V |\Phi_\rho\rangle
$$ {#eq-2.130}

where $V$ is unitary, which may also be written

$$
|\Phi_\rho(V)\rangle = (\rho^{1/2} \otimes V) |\tilde{\Phi}\rangle,
$$ {#eq-2.131}

where $|\tilde{\Phi}\rangle$ is the unconventionally normalized maximally entangled state

$$
|\tilde{\Phi}\rangle_{AB} = \sum_i |i\rangle_A \otimes |i\rangle_B.
$$ {#eq-2.132}

If $\rho$ and $\sigma$ are two density operators on $A$, the inner product of their purifications on $AB$ can be expressed as

$$
\langle\Phi_\sigma(W)|\Phi_\rho(V)\rangle = \langle\tilde{\Phi}| \sigma^{1/2} \rho^{1/2} \otimes W^\dagger V |\tilde{\Phi}\rangle.
$$ {#eq-2.133}

<!-- Page 38 -->
Noting that

$$
U \otimes I |\tilde{\Phi}\rangle = \sum_{i,j} |j\rangle \otimes |i\rangle U_{ji} = \sum_{i,j} |j\rangle \otimes |i\rangle U^T_{ij} = I \otimes U^T |\tilde{\Phi}\rangle,
$$ {#eq-2.134}

we have

$$
\langle\Phi_\sigma(W)|\Phi_\rho(V)\rangle = \langle\tilde{\Phi}| \sigma^{1/2} \rho^{1/2} U \otimes I |\tilde{\Phi}\rangle = \text{tr}\left( \sigma^{1/2} \rho^{1/2} U \right),
$$ {#eq-2.135}

where $U = (W^\dagger V)^T$.

Now we may use the polar decomposition

$$
A = U' \sqrt{A^\dagger A},
$$ {#eq-2.136}

where $U'$ is unitary, to rewrite the inner product as

$$
\langle\Phi_\sigma(W)|\Phi_\rho(V)\rangle = \text{tr}\left( U U' \sqrt{\rho^{1/2} \sigma \rho^{1/2}} \right) = \sum_a \lambda_a \langle a| U U' |a\rangle,
$$ {#eq-2.137}

where $\{\lambda_a\}$ are the nonnegative eigenvalues of $\sqrt{\rho^{1/2} \sigma \rho^{1/2}}$ and $\{|a\rangle\}$ are the corresponding eigenvectors. It is now evident that the inner product has the largest possible absolute value when we choose $U = {U'}^{-1}$, and hence we conclude

$$
F(\rho, \sigma) = \left( \text{tr}\sqrt{\rho^{1/2} \sigma \rho^{1/2}} \right)^2 = \max_{V,W} |\langle\Phi_\sigma(W)|\Phi_\rho(V)\rangle|^2.
$$ {#eq-2.138}

The fidelity of two density operators is the maximal possible overlap of their purifications, a result called Uhlmann's theorem.

One corollary of Uhlmann's theorem is the monotonicity of fidelity:

$$
F(\rho_{AB}, \sigma_{AB}) \le F(\rho_A, \sigma_A),
$$ {#eq-2.139}

which says that tracing out a subsystem cannot decrease the fidelity of two density operators. Monotonicity means, unsurprisingly, that throwing away a subsystem does not make two quantum states easier to distinguish. It follows from Uhlmann's theorem because any state purifying $\rho_{AB}$ also provides a purification of $A$; therefore the optimal overlap of the purifications of $\rho_{AB}$ and $\sigma_{AB}$ is surely achievable by purifications of $\rho_A$ and $\sigma_A$.

### 2.6.2 Relations among distance measures

There are other possible ways besides fidelity for quantifying the difference between quantum states $\rho$ and $\sigma$, such as the distance between the states using the $L^1$ or $L^2$ norm,

$$
\|\rho - \sigma\|_1 \quad \text{or} \quad \|\rho - \sigma\|_2,
$$ {#eq-2.140}

<!-- Page 39 -->
where the $L^2$ norm of an operator is defined by

$$
\|A\|_2 = \sqrt{\text{tr} A^\dagger A}.
$$ {#eq-2.141}

(For Hermitian $A$, $\|A\|_2$ is the square root of the sum of the squares of its eigenvalues.) The $L^1$ distance is a particularly natural measure of state distinguishability, because (as shown in Exercise 2.5) it can be interpreted as the distance between the corresponding probability distributions achieved by the optimal measurement for distinguishing the states. Although the fidelity, $L^1$ distance, and $L^2$ distance are not simply related to one another in general, there are useful inequalities relating these different measures.

If $\{|\lambda_i|, i = 0, 1, 2, \dots, d-1\}$ denotes the eigenvalues of $\sqrt{A^\dagger A}$, then

$$
\|A\|_1 = \sum_{i=0}^{d-1} |\lambda_i|; \quad \|A\|_2 = \sqrt{\sum_{i=0}^{d-1} |\lambda_i|^2}.
$$ {#eq-2.142}

If we regard $\|A\|_1$ as the inner product of the two vectors $(1, 1, 1, \dots, 1)$ and $(|\lambda_0|, |\lambda_1|, \dots, |\lambda_{d-1}|)$, then from the Cauchy-Schwarz inequality we find

$$
\|A\|_1 \le \sqrt{d} \|A\|_2.
$$ {#eq-2.143}

Because of the factor of $\sqrt{d}$ on the right hand side, for a high-dimensional system density operators which are close together in the $L^2$ norm might not be close in the $L^1$ norm.

There is, however, a dimension-independent inequality relating the $L^1$ distance between $\rho$ and $\sigma$ and the $L^2$ distance between their square roots:

$$
\|\sqrt{\rho} - \sqrt{\sigma}\|_2^2 \le \|\rho - \sigma\|_1.
$$ {#eq-2.144}

To derive this inequality, we first expand the difference of square roots in its basis of eigenvectors,

$$
\sqrt{\rho} - \sqrt{\sigma} = \sum_i \lambda_i |i\rangle\langle i|,
$$ {#eq-2.145}

and note that the absolute value of this difference may be written as

$$
|\sqrt{\rho} - \sqrt{\sigma}| = \sum_i |\lambda_i| |i\rangle\langle i| = (\sqrt{\rho} - \sqrt{\sigma}) U = U (\sqrt{\rho} - \sqrt{\sigma}),
$$ {#eq-2.146}

where

$$
U = \sum_i \text{sign}(\lambda_i) |i\rangle\langle i|.
$$ {#eq-2.147}

<!-- Page 40 -->
Using

$$
\rho - \sigma = \frac{1}{2}(\sqrt{\rho} - \sqrt{\sigma})(\sqrt{\rho} + \sqrt{\sigma}) + \frac{1}{2}(\sqrt{\rho} + \sqrt{\sigma})(\sqrt{\rho} - \sqrt{\sigma})
$$ {#eq-2.148}

and the cyclicity of the trace, we find

$$
\begin{aligned}
\text{tr}(\rho - \sigma)U &= \text{tr}|\sqrt{\rho} - \sqrt{\sigma}|(\sqrt{\rho} + \sqrt{\sigma}) = \sum_i |\lambda_i| \langle i|\sqrt{\rho} + \sqrt{\sigma}|i\rangle \\
&\ge \sum_i |\lambda_i| |\langle i|\sqrt{\rho} - \sqrt{\sigma}|i\rangle| = \sum_i |\lambda_i|^2 = \|\sqrt{\rho} - \sqrt{\sigma}\|_2^2.
\end{aligned}
$$ {#eq-2.149}

Finally, using

$$
\|\rho - \sigma\|_1 = \text{tr}|\rho - \sigma| \ge \text{tr}(\rho - \sigma)U,
$$ {#eq-2.150}

which is true for any unitary $U$, we obtain eq. (2.144).

This $L^2$ distance between square roots can be related to fidelity. First we note that

$$
\|\sqrt{\rho} - \sqrt{\sigma}\|_2^2 = \text{tr}(\sqrt{\rho} - \sqrt{\sigma})^2 = 2 - 2\,\text{tr}(\sqrt{\rho}\sqrt{\sigma}),
$$ {#eq-2.151}

since $\text{tr}\,\rho = \text{tr}\,\sigma = 1$. From the polar decomposition $A = U\sqrt{A^\dagger A}$ (where $U$ is unitary), we see that $\text{tr}\sqrt{A^\dagger A} \ge |\text{tr} A|$, and therefore

$$
\sqrt{F(\rho, \sigma)} = \text{tr}\sqrt{\rho^{1/2} \sigma \rho^{1/2}} \ge |\text{tr}(\sqrt{\rho}\sqrt{\sigma})|;
$$ {#eq-2.152}

hence, from eq. (2.144) and eq. (2.151),

$$
\sqrt{F(\rho, \sigma)} \ge 1 - \frac{1}{2}\|\sqrt{\rho} - \sqrt{\sigma}\|_2^2 \ge 1 - \frac{1}{2}\|\rho - \sigma\|_1.
$$ {#eq-2.153}

Eq. (2.153) tells us that if $\rho$ and $\sigma$ are close to one another in the $L^1$ norm, then their fidelity is close to one.

The $L^1$ distance also provides an upper bound on fidelity:

$$
F(\rho, \sigma) \le 1 - \frac{1}{4}\|\rho - \sigma\|_1^2.
$$ {#eq-2.154}

To derive eq. (2.154) we first show that it holds with equality for pure states. Any two vectors $|\psi\rangle$ and $|\phi\rangle$ lie in some two-dimensional subspace, and by choosing a basis and phase conventions appropriately we may write

$$
|\psi\rangle = \begin{pmatrix} \cos\theta/2 \\ \sin\theta/2 \end{pmatrix}, \quad |\phi\rangle = \begin{pmatrix} \sin\theta/2 \\ \cos\theta/2 \end{pmatrix},
$$ {#eq-2.155}

<!-- Page 41 -->
for some angle $\theta$; then

$$
|\psi\rangle\langle\psi| - |\phi\rangle\langle\phi| = \begin{pmatrix} \cos\theta & 0 \\ 0 & -\cos\theta \end{pmatrix},
$$ {#eq-2.156}

and

$$
|\langle\phi|\psi\rangle|^2 = \sin^2\theta.
$$ {#eq-2.157}

Therefore,

$$
\||\psi\rangle\langle\psi| - |\phi\rangle\langle\phi|\|_1^2 = (2\cos\theta)^2 = 4(1 - F(|\psi\rangle\langle\psi|, |\phi\rangle\langle\phi|)).
$$ {#eq-2.158}

Next, note that $L^1$ distance, like fidelity, is monotonic:

$$
\|\rho_{AB} - \sigma_{AB}\|_1 \ge \|\rho_A - \sigma_A\|_1.
$$ {#eq-2.159}

This follows because the $L^1$ distance is the optimal distance between probability distributions when we measure the two states, and the optimal measurement for distinguishing $\rho_A$ and $\sigma_A$ is also a possible measurement for $\rho_{AB}$ and $\sigma_{AB}$, one that happens to act trivially on $B$.

Finally, we invoke Uhlmann's theorem. If $\rho_{AB}$ and $\sigma_{AB}$ are the purifications of $\rho_A$ and $\sigma_A$ with the largest possible overlap, then

$$
F(\rho_A, \sigma_A) = F(\rho_{AB}, \sigma_{AB}) = 1 - \frac{1}{4}\|\rho_{AB} - \sigma_{AB}\|_1^2 \le 1 - \frac{1}{4}\|\rho_A - \sigma_A\|_1^2,
$$ {#eq-2.160}

where the first equality uses Uhlmann's theorem, the second uses eq. (2.158), and the final inequality uses monotonicity. By combining eq. (2.160) with eq. (2.153) we have

$$
1 - \sqrt{F(\rho, \sigma)} \le \frac{1}{2}\|\rho - \sigma\|_1 \le \sqrt{1 - F(\rho, \sigma)};
$$ {#eq-2.161}

hence $\rho$ and $\sigma$ are close to one another in the $L^1$ norm if and only if their fidelity is close to one.
