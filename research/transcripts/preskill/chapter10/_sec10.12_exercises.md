# Section 10.12: Exercises [PDF Pages 87-101]

<!-- ============================================================ -->
<!-- Source: chap10.pdf, Physical Pages: 87-101                    -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 87 -->
# Exercises

## 10.1 Positivity of quantum relative entropy

a) Show that $\ln x \le x - 1$ for all positive real $x$, with equality iff $x = 1$.

b) The (classical) relative entropy of a probability distribution $\{p(x)\}$ relative to $\{q(x)\}$ is defined as
$$
D(p\|q) \equiv \sum_x p(x) (\log p(x) - \log q(x)) .
$$ {#eq-10.377}

Show that
$$
D(p\|q) \ge 0 ,
$$ {#eq-10.378}

with equality iff the probability distributions are identical. **Hint:** Apply the inequality from (a) to $\ln(q(x)/p(x))$.

<!-- Page 88 -->
c) The quantum relative entropy of the density operator $\boldsymbol{\rho}$ with respect to $\boldsymbol{\sigma}$ is defined as
$$
D(\boldsymbol{\rho}\|\boldsymbol{\sigma}) = \mathrm{tr}\,\boldsymbol{\rho}(\log \boldsymbol{\rho} - \log \boldsymbol{\sigma}) .
$$ {#eq-10.379}

Let $\{p_i\}$ denote the eigenvalues of $\boldsymbol{\rho}$ and $\{q_a\}$ denote the eigenvalues of $\boldsymbol{\sigma}$. Show that
$$
D(\boldsymbol{\rho}\|\boldsymbol{\sigma}) = \sum_i p_i \left( \log p_i - \sum_a D_{ia} \log q_a \right) ,
$$ {#eq-10.380}

where $D_{ia}$ is a doubly stochastic matrix. Express $D_{ia}$ in terms of the eigenstates of $\boldsymbol{\rho}$ and $\boldsymbol{\sigma}$. (A matrix is doubly stochastic if its entries are nonnegative real numbers, where each row and each column sums to one.)

d) Show that if $D_{ia}$ is doubly stochastic, then (for each $i$)
$$
\log \left( \sum_a D_{ia} q_a \right) \ge \sum_a D_{ia} \log q_a ,
$$ {#eq-10.381}

with equality only if $D_{ia} = 1$ for some $a$.

e) Show that
$$
D(\boldsymbol{\rho}\|\boldsymbol{\sigma}) \ge D(p\|r) ,
$$ {#eq-10.382}

where $r_i = \sum_a D_{ia} q_a$.

f) Show that $D(\boldsymbol{\rho}\|\boldsymbol{\sigma}) \ge 0$, with equality iff $\boldsymbol{\rho} = \boldsymbol{\sigma}$.

## 10.2 Properties of von Neumann entropy

a) Use nonnegativity of quantum relative entropy to prove the *subadditivity* of von Neumann entropy
$$
H(\boldsymbol{\rho}_{AB}) \le H(\boldsymbol{\rho}_A) + H(\boldsymbol{\rho}_B) ,
$$ {#eq-10.383}

with equality iff $\boldsymbol{\rho}_{AB} = \boldsymbol{\rho}_A \otimes \boldsymbol{\rho}_B$. **Hint:** Consider the relative entropy of $\boldsymbol{\rho}_{AB}$ and $\boldsymbol{\rho}_A \otimes \boldsymbol{\rho}_B$.

b) Use subadditivity to prove the concavity of the von Neumann entropy:
$$
H\left( \sum_x p_x \boldsymbol{\rho}_x \right) \ge \sum_x p_x H(\boldsymbol{\rho}_x) .
$$ {#eq-10.384}

**Hint:** Consider
$$
\boldsymbol{\rho}_{AB} = \sum_x p_x (\boldsymbol{\rho}_x)_A \otimes (|x\rangle\langle x|)_B ,
$$ {#eq-10.385}

where the states $\{|x\rangle_B\}$ are mutually orthogonal.

c) Use the condition
$$
H(\boldsymbol{\rho}_{AB}) = H(\boldsymbol{\rho}_A) + H(\boldsymbol{\rho}_B) \quad \text{iff} \quad \boldsymbol{\rho}_{AB} = \boldsymbol{\rho}_A \otimes \boldsymbol{\rho}_B
$$ {#eq-10.386}

to show that, if all $p_x$\x27s are nonzero,
$$
H\left( \sum_x p_x \boldsymbol{\rho}_x \right) = \sum_x p_x H(\boldsymbol{\rho}_x)
$$ {#eq-10.387}

iff all the $\boldsymbol{\rho}_x$\x27s are identical.

<!-- Page 89 -->
## 10.3 Monotonicity of quantum relative entropy

Quantum relative entropy has a property called *monotonicity*:
$$
D(\boldsymbol{\rho}_A\|\boldsymbol{\sigma}_A) \le D(\boldsymbol{\rho}_{AB}\|\boldsymbol{\sigma}_{AB}) ;
$$ {#eq-10.388}

The relative entropy of two density operators on a system $AB$ cannot be less than the induced relative entropy on the subsystem $A$.

a) Use monotonicity of quantum relative entropy to prove the *strong subadditivity* property of von Neumann entropy. **Hint:** On a tripartite system $ABC$, consider the relative entropy of $\boldsymbol{\rho}_{ABC}$ and $\boldsymbol{\rho}_A \otimes \boldsymbol{\rho}_{BC}$.

b) Use monotonicity of quantum relative entropy to show that the action of a quantum channel $\mathcal{N}$ cannot increase relative entropy:
$$
D(\mathcal{N}(\boldsymbol{\rho})\|\mathcal{N}(\boldsymbol{\sigma})) \le D(\boldsymbol{\rho}\|\boldsymbol{\sigma}) ,
$$ {#eq-10.389}

**Hint:** Recall that any quantum channel has an isometric dilation.

## 10.4 Hypothesis testing

The (classical) relative entropy $D(p\|q)$ characterizes the difference between the distributions $p(x)$ and $q(x)$ in a sense that is useful for hypothesis testing. Suppose that an unknown distribution is sampled $n \gg 1$ times, and we find that outcome $x$ occurs $np(x)$ times. We would like to assess whether these outcomes are compatible with sampling from a hypothetical distribution $q(x)$. As discussed in §10.1.4, the probability of obtaining this result if we are actually sampling from $q(x)$ may be estimated as
$$
\text{Probability} = 2^{-nD(p\|q)} .
$$ {#eq-10.390}

a) Suppose
$$
q(x) = p(x) + \varepsilon(x), \quad \sum_x \varepsilon(x) = 0 .
$$ {#eq-10.391}

Write $D(p\|q)$ as a function of $p(x)$ and $\varepsilon(x)$, expanded to quadratic order in $\varepsilon(x)$. For this purpose, suppose that the logarithms in the definition of relative entropy are natural logs rather than logs to the base 2.

b) Suppose that
$$
\|\varepsilon\|_1 = \sum_x |\varepsilon(x)| = \delta .
$$ {#eq-10.392}

Using the quadratic approximation found in (a), find the minimal value of $D(p\|q)$ and the hypothetical distribution $q(x) = p(x) + \varepsilon(x)$ that minimizes it.

c) Suppose we toss a coin $n$ times, and the outcome "heads" is observed $n\left(\frac{1}{2} + \frac{\delta}{2}\right)$ times. Hence $p(\text{heads}) = \frac{1}{2} + \frac{\delta}{2}$ and $p(\text{tails}) = \frac{1}{2} - \frac{\delta}{2}$. Consider the hypothesis that the coin is unbiased: $q(\text{heads}) = q(\text{tails}) = \frac{1}{2}$. Compute the relative entropy $D(p\|q)$ to quadratic order in $\delta$.

d) A coin is tossed 1 million times. Use the result of (c) to estimate the probability of the coin coming up heads 505,000 times, assuming that the coin is unbiased.

## 10.5 Separability and majorization

The hallmark of entanglement is that in an entangled state the whole is less random than its parts. But in a separable state the correlations are essentially <!-- Page 90 --> classical and so are expected to adhere to the classical principle that the parts are less disordered than the whole. The objective of this problem is to make this expectation precise by showing that if the bipartite (mixed) state $\boldsymbol{\rho}_{AB}$ is separable, then
$$
\lambda(\boldsymbol{\rho}_{AB}) \prec \lambda(\boldsymbol{\rho}_A) , \quad \lambda(\boldsymbol{\rho}_{AB}) \prec \lambda(\boldsymbol{\rho}_B) .
$$ {#eq-10.393}

Here $\lambda(\boldsymbol{\rho})$ denotes the vector of eigenvalues of $\boldsymbol{\rho}$, and $\prec$ denotes majorization.

A separable state can be realized as an ensemble of pure product states, so that if $\boldsymbol{\rho}_{AB}$ is separable, it may be expressed as
$$
\boldsymbol{\rho}_{AB} = \sum_a p_a |\psi_a\rangle\langle\psi_a| \otimes |\varphi_a\rangle\langle\varphi_a| .
$$ {#eq-10.394}

We can also diagonalize $\boldsymbol{\rho}_{AB}$, expressing it as
$$
\boldsymbol{\rho}_{AB} = \sum_j r_j |e_j\rangle\langle e_j| ,
$$ {#eq-10.395}

where $\{|e_j\rangle\}$ denotes an orthonormal basis for $AB$; then by the HJW theorem, there is a unitary matrix $V$ such that
$$
\sqrt{r_j}|e_j\rangle = \sum_a V_{ja} \sqrt{p_a} |\psi_a\rangle \otimes |\varphi_a\rangle .
$$ {#eq-10.396}

Also note that $\boldsymbol{\rho}_A$ can be diagonalized, so that
$$
\boldsymbol{\rho}_A = \sum_a p_a |\psi_a\rangle\langle\psi_a| = \sum_\mu s_\mu |f_\mu\rangle\langle f_\mu| ;
$$ {#eq-10.397}

here $\{|f_\mu\rangle\}$ denotes an orthonormal basis for $A$, and by the HJW theorem, there is a unitary matrix $U$ such that
$$
\sqrt{p_a}|\psi_a\rangle = \sum_\mu U_{a\mu}\sqrt{s_\mu}|f_\mu\rangle .
$$ {#eq-10.398}

Now show that there is a doubly stochastic matrix $D$ such that
$$
r_j = \sum_\mu D_{j\mu} s_\mu .
$$ {#eq-10.399}

That is, you must check that the entries of $D_{j\mu}$ are real and nonnegative, and that $\sum_j D_{j\mu} = 1 = \sum_\mu D_{j\mu}$. Thus we conclude that $\lambda(\boldsymbol{\rho}_{AB}) \prec \lambda(\boldsymbol{\rho}_A)$. Just by interchanging $A$ and $B$, the same argument also shows that $\lambda(\boldsymbol{\rho}_{AB}) \prec \lambda(\boldsymbol{\rho}_B)$.

**Remark:** Note that it follows from the Schur concavity of Shannon entropy that, if $\boldsymbol{\rho}_{AB}$ is separable, then the von Neumann entropy has the properties $H(AB) \ge H(A)$ and $H(AB) \ge H(B)$. Thus, for separable states, conditional entropy is nonnegative: $H(A|B) = H(AB) - H(B) \ge 0$ and $H(B|A) = H(AB) - H(A) \ge 0$. In contrast, if $H(A|B)$ is negative, then according to the hashing inequality the state of $AB$ has positive distillable entanglement $-H(A|B)$, and therefore is surely not separable.

## 10.6 Additivity of squashed entanglement

Suppose that Alice holds systems $A, A\x27$ and Bob holds systems $B, B\x27$. How is the entanglement of $AA\x27$ with $BB\x27$ related to the entanglement of $A$ with $B$ and $A\x27$ with $B\x27$? In this problem we will show that the squashed entanglement is superadditive,
$$
E_{\text{sq}}(\boldsymbol{\rho}_{ABA\x27B\x27}) \ge E_{\text{sq}}(\boldsymbol{\rho}_{AB}) + E_{\text{sq}}(\boldsymbol{\rho}_{A\x27B\x27})
$$ {#eq-10.400}

<!-- Page 91 -->
and is strictly additive for a tensor product,
$$
E_{\text{sq}}(\boldsymbol{\rho}_{AB} \otimes \boldsymbol{\rho}_{A\x27B\x27}) = E_{\text{sq}}(\boldsymbol{\rho}_{AB}) + E_{\text{sq}}(\boldsymbol{\rho}_{A\x27B\x27}) .
$$ {#eq-10.401}

a) Use the chain rule for mutual information eq.(10.201) and eq.(10.202) and the nonnegativity of quantum conditional mutual information to show that
$$
I(AA\x27; BB\x27|C) \ge I(A; B|C) + I(A\x27; B\x27|AC) ,
$$ {#eq-10.402}

and show that eq.(10.400) follows.

b) Show that for any extension $\boldsymbol{\rho}_{ABC} \otimes \boldsymbol{\rho}_{A\x27B\x27C\x27}$ of the product state $\boldsymbol{\rho}_{AB} \otimes \boldsymbol{\rho}_{A\x27B\x27}$, we have
$$
I(AA\x27; BB\x27|CC\x27) \le I(A; B|C) + I(A\x27; B\x27|C\x27) .
$$ {#eq-10.403}

Conclude that
$$
E_{\text{sq}}(\boldsymbol{\rho}_{AB} \otimes \boldsymbol{\rho}_{A\x27B\x27}) \le E_{\text{sq}}(\boldsymbol{\rho}_{AB}) + E_{\text{sq}}(\boldsymbol{\rho}_{A\x27B\x27}) ,
$$ {#eq-10.404}

which, when combined with eq.(10.400), implies eq.(10.401).

## 10.7 The first law of von Neumann entropy

Writing the density operator in terms of its *modular Hamiltonian* $\boldsymbol{K}$ as in §10.2.6,
$$
\boldsymbol{\rho} = \frac{e^{-\boldsymbol{K}}}{\mathrm{tr}(e^{-\boldsymbol{K}})} ,
$$ {#eq-10.405}

consider how the entropy $S(\boldsymbol{\rho}) = -\mathrm{tr}\,(\boldsymbol{\rho}\ln \boldsymbol{\rho})$ changes when the density operator is perturbed slightly:
$$
\boldsymbol{\rho} \to \boldsymbol{\rho}\x27 = \boldsymbol{\rho} + \delta\boldsymbol{\rho} .
$$ {#eq-10.406}

Since $\boldsymbol{\rho}$ and $\boldsymbol{\rho}\x27$ are both normalized density operators, we have $\mathrm{tr}(\delta\boldsymbol{\rho}) = 0$. Show that
$$
S(\boldsymbol{\rho}\x27) - S(\boldsymbol{\rho}) = \mathrm{tr}(\boldsymbol{\rho}\x27\boldsymbol{K}) - \mathrm{tr}(\boldsymbol{\rho}\boldsymbol{K}) + O\left((\delta\boldsymbol{\rho})^2\right) ;
$$ {#eq-10.407}

that is,
$$
\delta S = \delta \langle\boldsymbol{K}\rangle
$$ {#eq-10.408}

to first order in the small change in $\boldsymbol{\rho}$. This statement generalizes the first law of thermodynamics; for the case of a thermal density operator with $\boldsymbol{K} = \boldsymbol{H}/T$ (where $\boldsymbol{H}$ is the Hamiltonian and $T$ is the temperature), it becomes the more familiar statement
$$
\delta E = \delta\langle\boldsymbol{H}\rangle = T\delta S .
$$ {#eq-10.409}

## 10.8 Distinguishing two nonorthogonal pure states

a) Consider an ensemble in which the two pure states of a single qubit
$$
|\varphi_0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |\varphi_1\rangle = \begin{pmatrix} \cos(\theta/2) \\ \sin(\theta/2) \end{pmatrix}
$$ {#eq-10.410}

occur equiprobably, where $\theta \in [0, 2\pi)$. The two states both lie in the $xz$ plane of the Bloch sphere, and the angle between them is $\theta$. Suppose that a state is drawn from this ensemble and then the Pauli observable
$$
\boldsymbol{Z} = |0\rangle\langle 0| - |1\rangle\langle 1|
$$ {#eq-10.411}

<!-- Page 92 -->
is measured. Compute the information gain achieved by this measurement.

b) Now suppose that, instead of $\boldsymbol{Z}$, the rotated observable
$$
\boldsymbol{Z}\x27 = |\psi\rangle\langle\psi| - |\psi^\perp\rangle\langle\psi^\perp|
$$ {#eq-10.412}

is measured, where
$$
|\psi\rangle = \begin{pmatrix} \cos(\theta/4 - \pi/4) \\ \sin(\theta/4 - \pi/4) \end{pmatrix}, \quad |\psi^\perp\rangle = \begin{pmatrix} \cos(\theta/4 + \pi/4) \\ \sin(\theta/4 + \pi/4) \end{pmatrix} .
$$ {#eq-10.413}

Compute the information gain in this case. Make a plot showing the two functions of $\theta$ computed in parts (a) and (b). Which has the higher information gain?

c) For $\theta = \pi/2$ and for $\theta = 2\pi/3$, find the numerical value of the information gain, in bits, achieved by measuring $\boldsymbol{Z}$ and $\boldsymbol{Z}\x27$.

## 10.9 The Peres–Wootters POVM.

Consider the Peres–Wootters information source described in §10.6.4. It prepares one of the three states
$$
|\Phi_a\rangle = |\varphi_a\rangle \otimes |\varphi_a\rangle, \quad a = 1, 2, 3,
$$ {#eq-10.414}

each occurring with *a priori* probability $\frac{1}{3}$, where the $|\varphi_a\rangle$\x27s are defined in eq.(10.219).

a) Express the density matrix
$$
\boldsymbol{\rho} = \frac{1}{3} \left( \sum_a |\Phi_a\rangle\langle\Phi_a| \right) ,
$$ {#eq-10.415}

in terms of the Bell basis of maximally entangled states $\{|\phi^\pm\rangle, |\psi^\pm\rangle\}$, and compute $H(\boldsymbol{\rho})$.

b) For the three vectors $|\Phi_a\rangle, a = 1, 2, 3$, construct the "pretty good measurement" defined in eq.(10.232). (Again, expand the $|\Phi_a\rangle$\x27s in the Bell basis.) In this case, the PGM is an orthogonal measurement. Express the elements of the PGM basis in terms of the Bell basis.

c) Compute the mutual information of the PGM outcome and the preparation.

## 10.10 An adaptive protocol

Consider again the Peres-Wootters ensemble in which the three two-qubit states
$$
|\Phi_a\rangle = |\varphi_a\rangle \otimes |\varphi_a\rangle, \quad a = 1, 2, 3
$$ {#eq-10.416}

occur equiprobably. A state is drawn from this ensemble, and we are to measure the two-qubit state with the goal of gaining information about the value of $a$. Instead of doing the collective measurement described in §10.6.4, consider an adaptive strategy in which the two qubits are measured separately. On the first qubit we perform the POVM with the three outcomes
$$
\boldsymbol{E}_a = \frac{2}{3} (\boldsymbol{I} - |\varphi_a\rangle\langle\varphi_a|) , \quad a = 1, 2, 3 ;
$$ {#eq-10.417}

this measurement excludes one of the three states, but provides no information to distinguish the other two states. Then we perform a measurement on the second qubit that is conditioned on the outcome of the first measurement. Guided by the results of Exercise 10.8, choose the most informative measurement to perform <!-- Page 93 --> on the second qubit, and then compute the information gain achieved by this adaptive procedure. Compare with the information gain achieved by the collective measurement described in §10.6.4.

## 10.11 An ensemble of four pure states

a) Consider an ensemble in which the four pure states of a single qubit
$$
|\varphi_0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \quad |\varphi_1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}, \quad |\varphi_2\rangle = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \end{pmatrix}, \quad |\varphi_3\rangle = \begin{pmatrix} \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} \end{pmatrix} ,
$$ {#eq-10.418}

occur equiprobably. Compute the information gain achieved by measuring $\boldsymbol{Z}$ for a state drawn from this ensemble.

b) Now compute the information gain achieved by measuring $\boldsymbol{Z}\x27$ for $\theta = \pi/2$. Compare with the result of (a).

## 10.12 An infinite ensemble

a) We now consider an ensemble with an infinite number of possible pure states, namely the uniform distribution on $\theta \in [0, 2\pi)$ where
$$
|\varphi(\theta)\rangle = \begin{pmatrix} \cos(\theta/2) \\ \sin(\theta/2) \end{pmatrix} .
$$ {#eq-10.419}

That is, when a state is sampled from this ensemble, a value in the interval $[\theta, \theta + d\theta]$ occurs with probability $d\theta/2\pi$. How much information do we gain about the value of $\theta$ by measuring $\boldsymbol{Z}$? To avoid having to take a difference of infinite quantities, answer this question by computing the conditional entropy $H(Y|\theta)$ and using
$$
I(\theta; Y) = H(Y) - H(Y|\theta) ,
$$ {#eq-10.420}

where $Y$ denotes the probability distribution of measurement outcomes.

b) Hoping to gain more information, let\x27s try a POVM with many outcomes rather than a two-outcome orthogonal measurement. Choose the POVM elements to be
$$
\boldsymbol{E}_k = \frac{2}{n} |\varphi(\theta_k)\rangle\langle\varphi(\theta_k)| , \quad k = 0, 1, 2, \dots, n-1 ,
$$ {#eq-10.421}

where
$$
\theta_k = \frac{2\pi k}{n} .
$$ {#eq-10.422}

Check the normalization condition
$$
\sum_k \boldsymbol{E}_k = \boldsymbol{I} ,
$$ {#eq-10.423}

and compute the information gain achieved by this measurement. Compare with the result of (a).

## 10.13 Approximate cloning and the depolarizing channel

Consider a qubit channel $\mathcal{N}_\theta^{A \to B}$ with the isometric dilation $U_\theta^{A \to BEF}$ which acts on an orthonormal basis as
$$
|0\rangle_A \mapsto |\phi_0\rangle_{BEF} = \cos\theta |00\rangle_{BE}|0\rangle_F + \sin\theta |\psi^+\rangle_{BE}|1\rangle_F ,
$$ {#eq-10.424}
$$
|1\rangle_A \mapsto |\phi_1\rangle_{BEF} = \cos\theta |11\rangle_{BE}|1\rangle_F + \sin\theta |\psi^+\rangle_{BE}|0\rangle_F ,
$$ {#eq-10.425}

<!-- Page 94 -->
where
$$
|\psi^+\rangle = \frac{1}{\sqrt{2}} (|01\rangle + |10\rangle) ,
$$ {#eq-10.426}

and $0 \le \theta \le \pi/2$. Here we have split the channel\x27s environment into two parts labeled $E$ and $F$, and we have constructed the isometry to be symmetric under the interchange of $B$ and $E$. Hence the channel $\mathcal{N}_\theta^{A \to B}$ obtained by tracing out $EF$ is identical to the channel $\mathcal{N}_\theta^{A \to E}$ obtained by tracing out $BF$. It follows that $\mathcal{N}_\theta^{A \to B}$ has zero capacity. To reach this conclusion, note that if Alice sends a quantum state to Bob via many uses of the isometry $U^{A \to BEF}$, and Bob (who receives the output system $B$) is able to decode the state with high fidelity, then Eve (who receives the output system $E$) receives the same output as Bob and therefore she can decode the state as well. Thus the no-cloning theorem ensures that high-fidelity decoding of the output is not possible.

a) The channel $\mathcal{N}_\theta^{A \to B}$ is actually a Pauli channel, which can be expressed as
$$
\mathcal{N}_\theta(\rho) = f(\theta)\rho + g(\theta)Z\rho Z + h(\theta)\frac{I}{2} .
$$ {#eq-10.427}

Find the functions $f, g$, and $h$.

b) We may choose a value $\theta = \theta_0$ such that $g(\theta_0) = 0$, in which case $\mathcal{N}$ becomes a depolarizing channel with error probability $p$:
$$
\mathcal{N}_{\theta_0}(\rho) = \left( 1 - \frac{4p}{3} \right) \rho + \left( \frac{4p}{3} \right) \frac{I}{2} .
$$ {#eq-10.428}

Find this value $\theta_0$ and the corresponding value of $p$. Our no-cloning argument shows that the depolarizing channel with this error probability $p$ has zero capacity.

c) Tracing out $F$ from the isometry $U^{A \to BEF}$, we obtain a channel $\mathcal{N}^{A \to BE}$, which may be regarded as an approximate cloning machine. If Alice sends a pure state $|\psi\rangle$ through the channel, the marginal density operators $\rho_B$ and $\rho_E$ received by Bob and Eve are identical, each approximating the input state with fidelity
$$
F = \langle\psi|\rho_B|\psi\rangle = \langle\psi|\rho_E|\psi\rangle .
$$ {#eq-10.429}

For the value $\theta = \theta_0$ found in (b), compute the fidelity achieved by this approximate cloner.

d) For $\theta \neq \theta_0$, we have $g(\theta) \neq 0$, and therefore the fidelity achieved by the approximate cloner depends on the pure state input $|\psi\rangle$. In that case we may consider the worst-case fidelity $F_{\min}(\theta)$, the lowest value of $F$ achieved for any pure state input to $\mathcal{N}^{A \to BE}$. Find the value $\theta = \theta_1$ such that this worst-case fidelity is as large as possible and compute $F_{\min}(\theta_1)$. (Be sure to recall that $g(\theta)$ changes sign at $\theta = \theta_0$.)

## 10.14 Information gain for a quantum state drawn from the uniform ensemble

Suppose Alice prepares a quantum state drawn from the ensemble $\{\boldsymbol{\rho}(x), p(x)\}$ and Bob performs a measurement $\{\boldsymbol{E}(y)\}$ yielding outcome $y$ with probability $p(y|x) = \mathrm{tr}\,(\boldsymbol{E}(y)\boldsymbol{\rho}(x))$. As noted in §10.6.1, Bob\x27s information gain about Alice\x27s <!-- Page 95 --> preparation is the mutual information $I(X; Y) = H(X) - H(X|Y)$. If $x$ is a continuous variable, while $y$ is discrete, it is more convenient to use the symmetry of mutual information to write $I(X; Y) = H(Y) - H(Y|X)$, where
$$
H(Y|X) = \sum_y \int dx \cdot p(x) \cdot p(y|x) \cdot \log p(y|x) ;
$$ {#eq-10.430}

here $p(x)$ is a probability *density* (that is, $p(x)dx$ is the probability for $x$ to lie in the interval $[x, x + dx]$).

For example, suppose that Alice prepares an arbitrary pure state $|\varphi\rangle$ chosen from the uniform ensemble in a $d$-dimensional Hilbert space, and Bob performs an orthogonal measurement projecting onto the basis $\{|e_y\rangle\}$, hoping to learn something about what Alice prepared. Then Bob obtains outcome $y$ with probability
$$
p(y|\theta) = |\langle e_y|\varphi\rangle|^2 \equiv \cos^2 \theta
$$ {#eq-10.431}

where $\theta$ is the angle between $|\varphi\rangle$ and $|e_y\rangle$. Because Alice\x27s ensemble is uniform, Bob\x27s outcomes are also uniformly distributed; hence $H(Y) = \log d$. Furthermore, the measurement outcome $y$ reveals only information about $\theta$; Bob learns nothing else about $|\varphi\rangle$. Therefore, eq.(10.430) implies that the information gain may be expressed as
$$
I(X; Y) = \log d - d \int d\theta \cdot p(\theta) \cdot \cos^2 \theta \cdot \log \cos^2 \theta .
$$ {#eq-10.432}

Here $p(\theta)d\theta$ is the probability density for the vector $|\varphi\rangle$ to point in a direction making angle $\theta$ with the axis $|e_y\rangle$, where $0 \le \theta \le \pi/2$.

a) Show that
$$
p(\theta) \cdot d\theta = -(d - 1) \left[ 1 - \cos^2 \theta \right]^{d-2} \cdot d\cos^2 \theta .
$$ {#eq-10.433}

**Hint:** Choose a basis in which the fixed axis $|e_y\rangle$ is
$$
|e_y\rangle = (1, \vec{0})
$$ {#eq-10.434}

and write
$$
|\varphi\rangle = (e^{i\phi}\cos\theta, \psi^\perp) ,
$$ {#eq-10.435}

where $\theta \in [0, \pi/2]$, and $|\psi^\perp\rangle$ denotes a complex $(d-1)$-component vector with length $\sin\theta$. Now note that the phase $\phi$ resides on a circle of radius $\cos\theta$ (and hence circumference $2\pi\cos\theta$), while $|\psi^\perp\rangle$ lies on a sphere of radius $\sin\theta$ (thus the volume of the sphere, up to a multiplicative numerical constant, is $\sin^{2d-3}\theta$).

b) Now evaluate the integral eq. (10.432) to show that the information gain from the measurement, in *nats*, is
$$
I(X; Y) = \ln d - \left( \frac{1}{2} + \frac{1}{3} + \dots + \frac{1}{d} \right) .
$$ {#eq-10.436}

(Information is expressed in nats if logarithms are natural logarithms; $I$ in nats is related to $I$ in bits by $I_{\text{bits}} = I_{\text{nats}}/\ln 2$.) **Hint:** To evaluate the integral
$$
\int_0^1 dx\,(1 - x)^p x \ln x ,
$$ {#eq-10.437}

<!-- Page 96 -->
observe that
$$
x \ln x = \left. \frac{d}{ds} x^s \right|_{s=1} ,
$$ {#eq-10.438}

and then calculate $\int_0^1 dx\,(1 - x)^p x^s$ by integrating by parts repeatedly.

c) Show that in the limit of large $d$, the information gain, in *bits*, approaches
$$
I_{d=\infty} = \frac{1 - \gamma}{\ln 2} = .60995\dots ,
$$ {#eq-10.439}

where $\gamma = .57721\dots$ is Euler\x27s constant.

Our computed value of $H(Y|X)$ may be interpreted in another way: Suppose we fix an orthogonal measurement, choose a typical state, and perform the measurement repeatedly on that chosen state. Then the measurement outcomes will not be uniformly distributed. Instead the entropy of the outcomes will fall short of maximal by .60995 bits, in the limit of large Hilbert space dimension.

## 10.15 Fano’s inequality

Suppose $X = \{x, p(x)\}$ is a probability distribution for a letter $x$ drawn from an alphabet of $d$ possible letters, and that $XY$ is the joint distribution for $x$ and another random variable $y$ which is correlated with $x$. Upon receiving $y$ we estimate the value of $x$ by evaluating a function $\hat{x}(y)$. We may anticipate that if our estimate is usually correct, then the conditional entropy $H(X|Y)$ must be small. In this problem we will confirm that expectation.

Let $e \in \{0, 1\}$ denote a binary random variable which takes the value $e = 0$ if $x = \hat{x}(y)$ and takes the value $e = 1$ if $x \neq \hat{x}(y)$, and let $XYE$ denote the joint distribution for $x, y, e$. The *error probability* $P_e$ is the probability that $e = 1$, averaged over this distribution. Our goal is to derive an upper bound on $H(X|Y)$ depending on $P_e$.

a) Show that
$$
H(X|Y) = H(X|YE) + H(E|Y) - H(E|XY) .
$$ {#eq-10.440}

Note that $H(E|XY) = 0$ because $e$ is determined when $x$ and $y$ are known, and that $H(E|Y) \le H(E)$ because mutual information is nonnegative. Therefore,
$$
H(X|Y) \le H(X|YE) + H(E) .
$$ {#eq-10.441}

b) Noting that
$$
H(X|YE) = p(e = 0) H(X|Y, e = 0) + p(e = 1) H(X|Y, e = 1) ,
$$ {#eq-10.442}

and that $H(X|Y, e = 0) = 0$ (because $x = \hat{x}(y)$ is determined by $y$ when there is no error), show that
$$
H(X|YE) \le P_e \log_2(d - 1) .
$$ {#eq-10.443}

c) Finally, show that
$$
H(X|Y) \le H_2(P_e) + P_e \log_2(d - 1) ,
$$ {#eq-10.444}

which is *Fano\x27s inequality*.

d) Use Fano\x27s inequality to derive eq.(10.55), hence completing the proof that the classical channel capacity $C$ is an upper bound on achievable rates for communication over a noisy channel with negligible error probability.

<!-- Page 97 -->
## 10.16 A quantum version of Fano’s inequality

a) In a $d$-dimensional system, suppose a density operator $\boldsymbol{\rho}$ approximates the pure state $|\psi\rangle$ with fidelity
$$
F = \langle\psi|\boldsymbol{\rho}|\psi\rangle = 1 - \varepsilon .
$$ {#eq-10.445}

Show that
$$
H(\boldsymbol{\rho}) \le H_2(\varepsilon) + \varepsilon \log_2(d - 1) .
$$ {#eq-10.446}

**Hint:** Recall that if a complete orthogonal measurement performed on the state $\boldsymbol{\rho}$ has the distribution of outcomes $X$, then $H(\boldsymbol{\rho}) \le H(X)$, where $H(X)$ is the Shannon entropy of $X$.

b) As in §10.7.2, suppose that the noisy channel $\mathcal{N}^{A \to B}$ acts on the pure state $\psi_{RA}$, and is followed by the decoding map $\mathcal{D}^{B \to C}$. Show that
$$
H(R)_\rho - I_c(R\rangle B)_\rho \le 2H(RC)_\sigma ,
$$ {#eq-10.447}

where
$$
\boldsymbol{\rho}_{RB} = \mathcal{N}(\psi_{RA}), \quad \boldsymbol{\sigma}_{RC} = \mathcal{D} \circ \mathcal{N}(\psi_{RA}) .
$$ {#eq-10.448}

Therefore, if the decoder\x27s output (the state of $RC$) is almost pure, then the coherent information of the channel $\mathcal{N}$ comes close to matching its input entropy. **Hint:** Use the data processing inequality $I_c(R\rangle C)_\sigma \le I_c(R\rangle B)_\rho$ and the subadditivity of von Neumann entropy. It is convenient to consider the joint pure state of the reference system, the output, and environments of the dilations of $\mathcal{N}$ and $\mathcal{D}$.

c) Suppose that the decoding map recovers the channel input with high fidelity,
$$
F(\mathcal{D} \circ \mathcal{N}(\psi_{RA}), \psi_{RC}) = 1 - \varepsilon .
$$ {#eq-10.449}

Show that
$$
H(R)_\rho - I_c(R\rangle B)_\rho \le 2H_2(\varepsilon) + 2\varepsilon \log_2(d^2 - 1) ,
$$ {#eq-10.450}

assuming that $R$ and $C$ are $d$-dimensional. This is a quantum version of Fano\x27s inequality, which we may use to derive an upper bound on the quantum channel capacity of $\mathcal{N}$.

## 10.17 Mother protocol for the GHZ state

The mother resource inequality expresses an asymptotic resource conversion that can be achieved if Alice, Bob, and Eve share $n$ copies of the pure state $\phi_{ABE}$: by sending $\frac{n}{2}I(A; E)$ qubits to Bob, Alice can destroy the correlations of her state with Eve\x27s state, so that Bob alone holds the purification of Eve\x27s state, and furthermore Alice and Bob share $\frac{n}{2}I(A; B)$ ebits of entanglement at the end of the protocol; here $I(A; E)$ and $I(A; B)$ denote quantum mutual informations evaluated in the state $\phi_{ABE}$.

Normally, the resource conversion can be realized with arbitrarily good fidelity only in the limit $n \to \infty$. But in this problem we will see that the conversion can be perfect if Alice, Bob and Eve share only $n = 2$ copies of the three-qubit GHZ state
$$
|\phi\rangle_{ABE} = \frac{1}{\sqrt{2}} (|000\rangle + |111\rangle) .
$$ {#eq-10.451}

<!-- Page 98 -->
The protocol achieving this perfect conversion uses the notion of *coherent classical communication* defined in Chapter 4.

a) Show that in the GHZ state $|\phi\rangle_{ABE}$, $I(A; E) = I(A; B) = 1$. Thus, for this state, the mother inequality becomes
$$
2\langle\phi_{ABE}\rangle + [q \to q]_{AB} \ge [qq]_{AB} + 2\langle\phi\x27_{B_1E}\rangle .
$$ {#eq-10.452}

b) Suppose that in the GHZ state Alice measures the Pauli operator $X$, gets the outcome $+1$ and broadcasts her outcome to Bob and Eve. What state do Bob and Eve then share? What if Alice gets the outcome $-1$ instead?

c) Suppose that Alice, Bob, and Eve share just one copy of the GHZ state $\phi^{ABE}$. Find a protocol such that, after one unit of *coherent classical communication* from Alice to Bob, the shared state becomes $|\phi^+\rangle_{AB} \otimes |\phi^+\rangle_{BE}$, where $|\phi^+\rangle = (|00\rangle + |11\rangle)/\sqrt{2}$ is a maximally entangled Bell pair.

d) Now suppose that Alice, Bob, and Eve start out with two copies of the GHZ state, and suppose that Alice and Bob can borrow an ebit of entanglement, which will be repaid later, to catalyze the resource conversion. Use coherent superdense coding to construct a protocol that achieves the (catalytic) conversion eq. (10.452) *perfectly*.

## 10.18 Degradability of amplitude damping and erasure

The qubit amplitude damping channel $\mathcal{N}_{\text{a.d.}}^{A \to B}(p)$ discussed in §3.4.3 has the dilation $\boldsymbol{U}^{A \to BE}$ such that
$$
\begin{aligned}
\boldsymbol{U} : |0\rangle_A &\mapsto |0\rangle_B \otimes |0\rangle_E , \\
|1\rangle_A &\mapsto \sqrt{1 - p}\,|1\rangle_B \otimes |0\rangle_E + \sqrt{p}\,|0\rangle_B \otimes |1\rangle_E ;
\end{aligned}
$$
a qubit in its "ground state" $|0\rangle_A$ is unaffected by the channel, while a qubit in the "excited state" $|1\rangle_A$ decays to the ground state with probability $p$, and the decay process excites the environment. Note that $\boldsymbol{U}$ is invariant under interchange of systems $B$ and $E$ accompanied by transformation $p \leftrightarrow (1 - p)$. Thus the channel complementary to $\mathcal{N}_{\text{a.d.}}^{A \to B}(p)$ is $\mathcal{N}_{\text{a.d.}}^{A \to E}(1 - p)$.

a) Show that $\mathcal{N}_{\text{a.d.}}^{A \to B}(p)$ is degradable for $p \le 1/2$. Therefore, the quantum capacity of the amplitude damping channel is its optimized one-shot coherent information. **Hint:** It suffices to show that
$$
\mathcal{N}_{\text{a.d.}}^{A \to E}(1 - p) = \mathcal{N}_{\text{a.d.}}^{B \to E}(q) \circ \mathcal{N}_{\text{a.d.}}^{A \to B}(p) ,
$$ {#eq-10.453}

where $0 \le q \le 1$.

The *erasure channel* $\mathcal{N}_{\text{erase}}^{A \to B}(p)$ has the dilation $\boldsymbol{U}^{A \to BE}$ such that
$$
\boldsymbol{U} : |\psi\rangle_A \mapsto \sqrt{1 - p}\,|\psi\rangle_B \otimes |e\rangle_E + \sqrt{p}\,|e\rangle_B \otimes |\psi\rangle_E ;
$$ {#eq-10.454}

Alice\x27s system passes either to Bob (with probability $1 - p$) or to Eve (with probability $p$), while the other party receives the "erasure symbol" $|e\rangle$, which is orthogonal to Alice\x27s Hilbert space. Because $\boldsymbol{U}$ is invariant under interchange of systems $B$ and $E$ accompanied by the transformation $p \leftrightarrow (1 - p)$, the channel complementary to $\mathcal{N}_{\text{erase}}^{A \to B}(p)$ is $\mathcal{N}_{\text{erase}}^{A \to E}(1 - p)$.

b) Show that $\mathcal{N}_{\text{erase}}^{A \to B}(p)$ is degradable for $p \le 1/2$. Therefore, the quantum capacity <!-- Page 99 --> of the erasure channel is its optimized one-shot coherent information. **Hint:** It suffices to show that
$$
\mathcal{N}_{\text{erase}}^{A \to E}(1 - p) = \mathcal{N}_{\text{erase}}^{B \to E}(q) \circ \mathcal{N}_{\text{erase}}^{A \to B}(p) ,
$$ {#eq-10.455}

where $0 \le q \le 1$.

c) Show that for $p \le 1/2$ the quantum capacity of the erasure channel is
$$
Q(\mathcal{N}_{\text{erase}}^{A \to B}(p)) = (1 - 2p) \log_2 d ,
$$ {#eq-10.456}

where $A$ is $d$-dimensional, and that the capacity vanishes for $1/2 \le p \le 1$.

## 10.19 Quantum Singleton bound

As noted in chapter 7, an $[[n, k, d]]$ quantum error-correcting code ($k$ protected qubits in a block of $n$ qubits, with code distance $d$) must obey the constraint
$$
n - k \ge 2(d - 1) ,
$$ {#eq-10.457}

the *quantum Singleton bound*. This bound is actually a corollary of a stronger statement which you will prove in this exercise.

Suppose that in the pure state $\phi_{RA}$ the reference system $R$ is maximally entangled with a code subspace of $A$, and that $E_1$ and $E_2$ are two disjoint correctable subsystems of system $A$ (erasure of either $E_1$ or $E_2$ can be corrected). You are to show that
$$
\log |A| - \log |R| \ge \log |E_1| + \log |E_2| .
$$ {#eq-10.458}

Let $E^c$ denote the subsystem of $A$ complementary to $E_1 E_2$, so that $A = E^c E_1 E_2$.

a) Recalling the error correction conditions $\boldsymbol{\rho}_{RE_1} = \boldsymbol{\rho}_R \otimes \boldsymbol{\rho}_{E_1}$ and $\boldsymbol{\rho}_{RE_2} = \boldsymbol{\rho}_R \otimes \boldsymbol{\rho}_{E_2}$, show that $\phi_{RE^c E_1 E_2}$ has the property
$$
H(R) = H(E^c) - \frac{1}{2} I(E^c; E_1) - \frac{1}{2} I(E^c; E_2) .
$$ {#eq-10.459}

b) Show that eq.(10.459) implies eq.(10.458).

## 10.20 Noisy superdense coding and teleportation.

a) By converting the entanglement achieved by the mother protocol into classical communication, prove the noisy superdense coding resource inequality:
$$
\text{Noisy } SD : \quad \langle\phi_{ABE}\rangle + H(A)[q \to q] \ge I(A; B)[c \to c] .
$$ {#eq-10.460}

Verify that this matches the standard noiseless superdense coding resource inequality when $\phi$ is a maximally entangled state of $AB$.

b) By converting the entanglement achieved by the mother protocol into quantum communication, prove the noisy teleportation resource inequality:
$$
\text{Noisy } TP : \quad \langle\phi_{ABE}\rangle + I(A; B)[c \to c] \ge I_c(A\rangle B)[q \to q] .
$$ {#eq-10.461}

Verify that this matches the standard noiseless teleportation resource inequality when $\phi$ is a maximally entangled state of $AB$.

## 10.21 The cost of erasure

*Erasure* of a bit is a process in which the state of the bit is reset to 0. Erasure is *irreversible* — knowing only the final state 0 after erasure, we cannot determine whether the initial state before erasure was 0 or 1. This irreversibility implies that erasure incurs an unavoidable thermodynamic cost. According to *Landauer\x27s <!-- Page 100 --> Principle*, erasing a bit at temperature $T$ requires work $W \ge kT \ln 2$. In this problem you will verify that a particular procedure for achieving erasure adheres to Landauer\x27s Principle.

Suppose that the two states of the bit both have zero energy. We erase the bit in two steps. In the first step, we bring the bit into contact with a reservoir at temperature $T > 0$, and wait for the bit to come to thermal equilibrium with the reservoir. In this step the bit "forgets" its initial value, but the bit is not yet erased because it has not been reset.

We reset the bit in the second step, by slowly turning on a control field $\lambda$ which splits the degeneracy of the two states. For $\lambda \ge 0$, the state 0 has energy $E_0 = 0$ and the state 1 has energy $E_1 = \lambda$. After the bit thermalizes in step one, the value of $\lambda$ increases gradually from the initial value $\lambda = 0$ to the final value $\lambda = \infty$; the increase in $\lambda$ is slow enough that the qubit remains in thermal equilibrium with the reservoir at all times. As $\lambda$ increases, the probability $P(0)$ that the qubit is in the state 0 approaches unity — *i.e.*, the bit is reset to the state 0, which has zero energy.

(a) For $\lambda \neq 0$, find the probability $P(0)$ that the qubit is in the state 0 and the probability $P(1)$ that the qubit is in the state 1.

(b) How much work is required to increase the control field from $\lambda$ to $\lambda + d\lambda$?

(c) How much work is expended as $\lambda$ increases slowly from $\lambda = 0$ to $\lambda = \infty$? (You will have to evaluate an integral, which can be done analytically.)

## 10.22 Proof of the decoupling inequality

In this problem we complete the derivation of the decoupling inequality sketched in §10.9.1.

a) Verify eq.(10.350).

To derive the expression for $\mathbb{E}_{\boldsymbol{U}}[\boldsymbol{M}_{AA\x27}(\boldsymbol{U})]$ in eq.(10.354), we first note that the invariance property eq.(10.339) implies that $\mathbb{E}_{\boldsymbol{U}}[\boldsymbol{M}_{AA\x27}(\boldsymbol{U})]$ commutes with $\boldsymbol{V} \otimes \boldsymbol{V}$ for any unitary $\boldsymbol{V}$. Therefore, by Schur\x27s lemma, $\mathbb{E}_{\boldsymbol{U}}[\boldsymbol{M}_{AA\x27}(\boldsymbol{U})]$ is a weighted sum of projections onto irreducible representations of the unitary group. The tensor product of two fundamental representations of $\boldsymbol{U}(d)$ contains two irreducible representations — the symmetric and antisymmetric tensor representations. Therefore we may write
$$
\mathbb{E}_{\boldsymbol{U}}[\boldsymbol{M}_{AA\x27}(\boldsymbol{U})] = c_{\text{sym}} \boldsymbol{\Pi}_{AA\x27}^{(\text{sym})} + c_{\text{anti}} \boldsymbol{\Pi}_{AA\x27}^{(\text{anti})} ;
$$ {#eq-10.462}

here $\boldsymbol{\Pi}_{AA\x27}^{(\text{sym})}$ is the orthogonal projector onto the subspace of $AA\x27$ symmetric under the interchange of $A$ and $A\x27$, $\boldsymbol{\Pi}_{AA\x27}^{(\text{anti})}$ is the projector onto the antisymmetric subspace, and $c_{\text{sym}}, c_{\text{anti}}$ are suitable constants. Note that
$$
\begin{aligned}
\boldsymbol{\Pi}_{AA\x27}^{(\text{sym})} &= \frac{1}{2} (\boldsymbol{I}_{AA\x27} + \boldsymbol{S}_{AA\x27}) , \\
\boldsymbol{\Pi}_{AA\x27}^{(\text{anti})} &= \frac{1}{2} (\boldsymbol{I}_{AA\x27} - \boldsymbol{S}_{AA\x27}) ,
\end{aligned}
$$ {#eq-10.463}

where $\boldsymbol{S}_{AA\x27}$ is the swap operator, and that the symmetric and antisymmetric subspaces have dimension $\frac{1}{2}|A|(|A| + 1)$ and dimension $\frac{1}{2}|A|(|A| - 1)$ respectively.

Even if you are not familiar with group representation theory, you might regard eq.(10.462) as obvious. We may write $\boldsymbol{M}_{AA\x27}(\boldsymbol{U})$ as a sum of two terms, one symmetric and the other antisymmetric under the interchange of $A$ and $A\x27$. The <!-- Page 101 --> expectation of the symmetric part must be symmetric, and the expectation value of the antisymmetric part must be antisymmetric. Furthermore, averaging over the unitary group ensures that no symmetric state is preferred over any other.

b) To evaluate the constant $c_{\text{sym}}$, multiply both sides of eq.(10.462) by $\boldsymbol{\Pi}_{AA\x27}^{(\text{sym})}$ and take the trace of both sides, thus finding
$$
c_{\text{sym}} = \frac{|A_1| + |A_2|}{|A| + 1} .
$$ {#eq-10.464}

c) To evaluate the constant $c_{\text{anti}}$, multiply both sides of eq.(10.462)) by $\boldsymbol{\Pi}_{AA\x27}^{(\text{anti})}$ and take the trace of both sides, thus finding
$$
c_{\text{anti}} = \frac{|A_1| - |A_2|}{|A| - 1} .
$$ {#eq-10.465}

d) Using
$$
c_{\boldsymbol{I}} = \frac{1}{2} (c_{\text{sym}} + c_{\text{anti}}) , \quad c_{\boldsymbol{S}} = \frac{1}{2} (c_{\text{sym}} - c_{\text{anti}})
$$ {#eq-10.466}

prove eq.(10.355).
