# Section 10.2: Von Neumann Entropy [PDF Pages 19-30]

<!-- ============================================================ -->
<!-- Source: chap10.pdf, Physical Pages: 19-30                    -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 19 -->
## 10.2 Von Neumann Entropy

In classical information theory, we often consider a source that prepares messages of $n$ letters ($n \gg 1$), where each letter is drawn independently from an ensemble $X = \{x, p(x)\}$. We have seen that the Shannon entropy $H(X)$ is the number of incompressible bits of information carried per letter (asymptotically as $n \to \infty$).

We may also be interested in correlations among messages. The correlations between two ensembles of letters $X$ and $Y$ are characterized by conditional probabilities $p(y|x)$. We have seen that the mutual information

$$
I(X; Y) = H(X) - H(X|Y) = H(Y) - H(Y|X),
$$ {#eq-10.56}

is the number of bits of information per letter about $X$ that we can acquire by reading $Y$ (or vice versa). If the $p(y|x)$'s characterize a noisy channel, then, $I(X; Y)$ is the amount of information per letter that can be transmitted through the channel (given the a priori distribution $X$ for the channel inputs).

We would like to generalize these considerations to quantum information. We may imagine a source that prepares messages of $n$ letters, but where each letter is chosen from an ensemble of quantum states. The signal alphabet consists of a set of quantum states $\{\rho(x)\}$, each occurring with a specified a priori probability $p(x)$.

As we discussed at length in Chapter 2, the probability of any outcome of any measurement of a letter chosen from this ensemble, if the observer has no knowledge about

<!-- Page 20 -->
which letter was prepared, can be completely characterized by the density operator

$$
\rho = \sum_x p(x) \rho(x);
$$ {#eq-10.57}

for a POVM $E = \{E_a\}$, the probability of outcome $a$ is

$$
\mathrm{Prob}(a) = \mathrm{tr}(E_a \rho).
$$ {#eq-10.58}

For this (or any) density operator, we may define the *von Neumann entropy*

$$
H(\rho) = -\mathrm{tr}(\rho \log \rho).
$$ {#eq-10.59}

Of course, we may choose an orthonormal basis $\{|a\rangle\}$ that diagonalizes $\rho$,

$$
\rho = \sum_a \lambda_a |a\rangle\langle a|;
$$ {#eq-10.60}

the vector of eigenvalues $\lambda(\rho)$ is a probability distribution, and the von Neumann entropy of $\rho$ is just the Shannon entropy of this distribution,

$$
H(\rho) = H(\lambda(\rho)).
$$ {#eq-10.61}

If $\rho_A$ is the density operator of system $A$, we will sometimes use the notation

$$
H(A) := H(\rho_A).
$$ {#eq-10.62}

Our convention is to denote quantum systems with $A, B, C, \dots$ and classical probability distributions with $X, Y, Z, \dots$.

In the case where the signal alphabet $\{|\varphi(x)\rangle, p(x)\}$ consists of mutually orthogonal pure states, the quantum source reduces to a classical one; all of the signal states can be perfectly distinguished, and $H(\rho) = H(X)$, where $X$ is the classical ensemble $\{x, p(x)\}$. The quantum source is more interesting when the signal states $\{\rho(x)\}$ are not mutually commuting. We will argue that the von Neumann entropy quantifies the incompressible information content of the quantum source (in the case where the signal states are pure) much as the Shannon entropy quantifies the information content of a classical source.

Indeed, we will find that von Neumann entropy plays multiple roles. It quantifies not only the quantum information content per letter of the pure-state ensemble (the minimum number of qubits per letter needed to reliably encode the information) but also its classical information content (the maximum amount of information per letter—in bits, not qubits—that we can gain about the preparation by making the best possible measurement). And we will see that von Neumann entropy enters quantum information in yet other ways — for example, quantifying the entanglement of a bipartite pure state. Thus quantum information theory is largely concerned with the interpretation and uses of von Neumann entropy, much as classical information theory is largely concerned with the interpretation and uses of Shannon entropy.

In fact, the mathematical machinery we need to develop quantum information theory is very similar to Shannon's mathematics (typical sequences, random coding, $\dots$); so similar as to sometimes obscure that the conceptual context is really quite different. The central issue in quantum information theory is that nonorthogonal quantum states cannot be perfectly distinguished, a feature with no classical analog.

<!-- Page 21 -->
### 10.2.1 Mathematical properties of $H(\rho)$

There are a handful of properties of the von Neumann entropy $H(\rho)$ which are frequently useful, many of which are closely analogous to corresponding properties of the Shannon entropy $H(X)$. Proofs of some of these are Exercises 10.1, 10.2, 10.3.

1. *Pure states.* A pure state $\rho = |\varphi\rangle\langle\varphi|$ has $H(\rho) = 0$.
2. *Unitary invariance.* The entropy is unchanged by a unitary change of basis,

$$
H(U\rho U^{-1}) = H(U\rho U^\dagger) = H(\rho),
$$ {#eq-10.63}

because $H(\rho)$ depends only on the eigenvalues of $\rho$.

3. *Maximum.* If $\rho$ has $d$ nonvanishing eigenvalues, then

$$
H(\rho) \le \log d,
$$ {#eq-10.64}

with equality when all the nonzero eigenvalues are equal. The entropy is maximized when the quantum state is maximally mixed.

4. *Concavity.* For $\lambda_1, \lambda_2, \dots, \lambda_n \ge 0$ and $\lambda_1 + \lambda_2 + \dots + \lambda_n = 1$,

$$
H(\lambda_1 \rho_1 + \dots + \lambda_n \rho_n) \ge \lambda_1 H(\rho_1) + \dots + \lambda_n H(\rho_n).
$$ {#eq-10.65}

The von Neumann entropy is larger if we are more ignorant about how the state was prepared. This property is a consequence of the concavity of the $\log$ function.

5. *Subadditivity.* Consider a bipartite system $AB$ in the state $\rho_{AB}$. Then

$$
H(AB) \le H(A) + H(B)
$$ {#eq-10.66}

(where $\rho_A = \mathrm{tr}_B(\rho_{AB})$ and $\rho_B = \mathrm{tr}_A(\rho_{AB})$), with equality only for $\rho_{AB} = \rho_A \otimes \rho_B$. Thus, entropy is additive for uncorrelated systems, but otherwise the entropy of the whole is less than the sum of the entropy of the parts. This property is the quantum generalization of subadditivity of Shannon entropy:

$$
H(XY) \le H(X) + H(Y).
$$ {#eq-10.67}

6. *Bipartite pure states.* If the state $\rho_{AB}$ of the bipartite system $AB$ is pure, then

$$
H(A) = H(B),
$$ {#eq-10.68}

because $\rho_A$ and $\rho_B$ have the same nonzero eigenvalues.

7. *Quantum mutual information.* As in the classical case, we define the mutual information of two quantum systems as

$$
I(A; B) = H(A) + H(B) - H(AB),
$$ {#eq-10.69}

which is nonnegative because of the subadditivity of von Neumann entropy, and zero only for a product state $\rho_{AB} = \rho_A \otimes \rho_B$.

8. *Triangle inequality (Araki-Lieb inequality).* For a bipartite system,

$$
H(AB) \ge |H(A) - H(B)|.
$$ {#eq-10.70}

To derive the triangle inequality, consider the tripartite pure state $|\psi\rangle_{ABC}$ which purifies $\rho_{AB} = \mathrm{tr}_C(|\psi\rangle\langle\psi|)$. Since $|\psi\rangle$ is pure, $H(A) = H(BC)$ and $H(C) = H(AB)$; applying subadditivity to $BC$ yields $H(A) \le H(B) + H(C) = H(B) + H(AB)$. The same inequality applies with $A$ and $B$ interchanged, from which we obtain eq.(10.70).

<!-- Page 22 -->
The triangle inequality contrasts sharply with the analogous property of Shannon entropy,

$$
H(XY) \ge H(X), H(Y).
$$ {#eq-10.71}

The Shannon entropy of just part of a classical bipartite system cannot be greater than the Shannon entropy of the whole system. Not so for the von Neumann entropy! For example, in the case of an entangled bipartite pure quantum state, we have $H(A) = H(B) > 0$, while $H(AB) = 0$. The entropy of the global system vanishes because our ignorance is minimal — we know as much about $AB$ as the laws of quantum physics will allow. But we have incomplete knowledge of the parts $A$ and $B$, with our ignorance quantified by $H(A) = H(B)$. For a quantum system, but not for a classical one, information can be encoded in the correlations among the parts of the system, yet be invisible when we look at the parts one at a time.

Equivalently, a property that holds classically but not quantumly is

$$
H(X|Y) = H(XY) - H(Y) \ge 0.
$$ {#eq-10.72}

The Shannon conditional entropy $H(X|Y)$ quantifies our remaining ignorance about $X$ when we know $Y$, and equals zero when knowing $Y$ makes us certain about $X$. On the other hand, the von Neumann conditional entropy,

$$
H(A|B) = H(AB) - H(B),
$$ {#eq-10.73}

can be negative; in particular we have $H(A|B) = -H(A) = -H(B) < 0$ if $\rho_{AB}$ is an entangled pure state. How can it make sense that "knowing" the subsystem $B$ makes us "more than certain" about the subsystem $A$? We'll return to this intriguing question in §10.8.2.

When $X$ and $Y$ are perfectly correlated, then $H(XY) = H(X) = H(Y)$; the conditional entropy is $H(X|Y) = H(Y|X) = 0$ and the mutual information is $I(X; Y) = H(X)$. In contrast, for a bipartite pure state of $AB$, the quantum state for which we may regard $A$ and $B$ as perfectly correlated, the mutual information is $I(A; B) = 2H(A) = 2H(B)$. In this sense the quantum correlations are stronger than classical correlations.

### 10.2.2 Mixing, measurement, and entropy

The Shannon entropy also has a property called Schur concavity, which means that if $X = \{x, p(x)\}$ and $Y = \{y, q(y)\}$ are two ensembles such that $p \prec q$, then $H(X) \ge H(Y)$. Recall that $p \prec q$ ($q$ majorizes $p$) means that "$p$ is at least as random as $q$" in the sense that $p = Dq$ for some doubly stochastic matrix $D$. Thus Schur concavity of $H$ says that an ensemble with more randomness has higher entropy.

The von Neumann entropy $H(\rho)$ of a density operator is the Shannon entropy of its vector of eigenvalues $\lambda(\rho)$. Furthermore, we showed in Exercise 2.6 that if the quantum state ensemble $\mathcal{E} = \{|\varphi(x)\rangle, p(x)\}$ realizes $\rho$, then $p \prec \lambda(\rho)$; therefore $H(\rho) \le H(X)$, where equality holds only for an ensemble of mutually orthogonal states. The decrease in entropy $H(X) - H(\rho)$ quantifies how distinguishability is lost when we mix nonorthogonal pure states. As we will soon see, the amount of information we can gain by measuring $\rho$ is no more than $H(\rho)$ bits, so some of the information about which state was prepared has been irretrievably lost if $H(\rho) < H(X)$.

<!-- Page 23 -->
If we perform an orthogonal measurement on $\rho$ by projecting onto the basis $\{|y\rangle\}$, then outcome $y$ occurs with probability

$$
q(y) = \langle y|\rho|y\rangle = \sum_a |\langle y|a\rangle|^2 \lambda_a, \quad \text{where} \quad \rho = \sum_a \lambda_a |a\rangle\langle a|
$$ {#eq-10.74}

and $\{|a\rangle\}$ is the basis in which $\rho$ is diagonal. Since $D_{ya} = |\langle y|a\rangle|^2$ is a doubly stochastic matrix, $q \prec \lambda(\rho)$ and therefore $H(Y) \ge H(\rho)$, where equality holds only if the measurement is in the basis $\{|a\rangle\}$. Mathematically, the conclusion is that for a nondiagonal and nonnegative Hermitian matrix, the diagonal elements are more random than the eigenvalues. Speaking more physically, the outcome of an orthogonal measurement is easiest to predict if we measure an observable which commutes with the density operator, and becomes less predictable if we measure in a different basis.

This majorization property has a further consequence, which will be useful for our discussion of quantum compression. Suppose that $\rho$ is a density operator of a $d$-dimensional system, with eigenvalues $\lambda_1 \ge \lambda_2 \ge \dots \ge \lambda_d$ and that $E' = \sum_{i=1}^{d'} |e_i\rangle\langle e_i|$ is a projector onto a subspace $\Lambda$ of dimension $d' \le d$ with orthonormal basis $\{|e_i\rangle\}$. Then

$$
\mathrm{tr}(\rho E') = \sum_{i=1}^{d'} \langle e_i|\rho|e_i\rangle \le \sum_{a=1}^{d'} \lambda_a,
$$ {#eq-10.75}

where the inequality follows because the diagonal elements of $\rho$ in the basis $\{|e_i\rangle\}$ are majorized by the eigenvalues of $\rho$. In other words, if we perform a two-outcome orthogonal measurement, projecting onto either $\Lambda$ or its orthogonal complement $\Lambda^\perp$, the probability of projecting onto $\Lambda$ is no larger than the sum of the $d'$ largest eigenvalues of $\rho$ (the Ky Fan dominance principle).

### 10.2.3 Strong subadditivity

In addition to the subadditivity property $I(X; Y) \ge 0$, correlations of classical random variables obey a further property called *strong subadditivity*:

$$
I(X; YZ) \ge I(X; Y).
$$ {#eq-10.76}

This is the eminently reasonable statement that the correlations of $X$ with $YZ$ are at least as strong as the correlations of $X$ with $Y$ alone.

There is another useful way to think about (classical) strong subadditivity. Recalling the definition of mutual information we have

$$
\begin{aligned}
I(X; YZ) - I(X; Y) &= -\left\langle \log \frac{p(x)p(y, z)}{p(x, y, z)} + \log \frac{p(x, y)}{p(x)p(y)} \right\rangle \\
&= -\left\langle \log \frac{p(x, y)}{p(y)} \frac{p(y, z)}{p(y)} \frac{p(y)}{p(x, y, z)} \right\rangle \\
&= -\left\langle \log \frac{p(x|y)p(z|y)}{p(x, z|y)} \right\rangle \\
&= \sum_y p(y) I(X; Z|y) \ge 0,
\end{aligned}
$$ {#eq-10.77}

where in the last line we used $p(x, y, z) = p(x, z|y)p(y)$. For each fixed $y$, $p(x, z|y)$ is a normalized probability distribution with nonnegative mutual information; hence $I(X; YZ) - I(X; Y)$ is a convex combination of nonnegative terms and therefore nonnegative. The quantity $I(X; Z|Y) := I(X; YZ) - I(X; Y)$ is called the *conditional mutual information*, because it quantifies how strongly $X$ and $Z$ are correlated when $Y$ is

<!-- Page 24 -->
known; strong subadditivity can be restated as the nonnegativity of conditional mutual information,

$$
I(X; Z|Y) \ge 0.
$$ {#eq-10.78}

The identities in eq.(10.77) demonstrate that $I(X; Z|Y)$ is symmetric under interchange of $X$ and $Z$, although this is not manifest in the expression $I(X; Z|Y) = I(X; YZ) - I(X; Y)$.

One might ask under what conditions strong subadditivity is satisfied as an equality; that is, when does the conditional mutual information vanish? Since $I(X; Z|Y)$ is a sum of nonnegative terms, each of these terms must vanish if $I(X; Z|Y) = 0$. Therefore for each $y$ with $p(y) > 0$, we have $I(X; Z|y) = 0$. The mutual information vanishes only for a product distribution; therefore

$$
p(x, z|y) = p(x|y)p(z|y) \implies p(x, y, z) = p(x|y)p(z|y)p(y).
$$ {#eq-10.79}

This means that the correlations between $x$ and $z$ arise solely from their shared correlation with $y$, in which case we say that $x$ and $z$ are conditionally independent.

Correlations of quantum systems also obey strong subadditivity:

$$
I(A; BC) - I(A; B) := I(A; C|B) \ge 0.
$$ {#eq-10.80}

But while the proof is elementary in the classical case, in the quantum setting strong subadditivity is a rather deep result with many important consequences. We will postpone the proof until §10.8.3, where we will be able to justify the quantum statement by giving it a clear operational meaning.

We'll also see in Exercise 10.3 that strong subadditivity follows easily from another deep property, the monotonicity of relative entropy:

$$
D(\rho_A\|\sigma_A) \le D(\rho_{AB}\|\sigma_{AB}),
$$ {#eq-10.81}

where

$$
D(\rho\|\sigma) := \mathrm{tr} \rho (\log \rho - \log \sigma).
$$ {#eq-10.82}

We won't discuss the details, but it turns out that the quantum relative entropy of $\rho$ with respect to $\sigma$ can be interpreted as a measure of the distinguishability of the two states in the context of hypothesis testing, much as the classical relative entropy $D(p\|q)$ is a measure of distinguishability of probability distributions as discussed in §10.1.4. Hence the monotonicity of quantum relative entropy amounts to the reasonable statement that quantum states on $AB$ become no easier to distinguish when we look at only the subsystem $A$ than when we look at the full system $AB$. It also follows (Exercise 10.3), that the action of a quantum channel $\mathcal{N}$ cannot increase relative entropy:

$$
D(\mathcal{N}(\rho)\|\mathcal{N}(\sigma)) \le D(\rho\|\sigma).
$$ {#eq-10.83}

There are a few other ways of formulating strong subadditivity which are helpful to keep in mind. By expressing the quantum mutual information in terms of the von Neumann entropy we find

$$
H(ABC) + H(B) \le H(AB) + H(BC).
$$ {#eq-10.84}

While $A, B, C$ are three disjoint quantum systems, we may view $AB$ and $BC$ as overlapping systems with intersection $B$ and union $ABC$; then strong subadditivity says that the sum of the entropies of two overlapping systems is at least as large as the sum of the

<!-- Page 25 -->
entropies of their union and their intersection. In terms of conditional entropy, strong subadditivity becomes

$$
H(A|B) \ge H(A|BC);
$$ {#eq-10.85}

loosely speaking, our ignorance about $A$ when we know only $B$ is no smaller than our ignorance about $A$ when we know both $B$ and $C$, but with the proviso that for quantum information "ignorance" can sometimes be negative!

As in the classical case, it is instructive to consider the condition for equality in strong subadditivity. What does it mean for systems to have quantum conditional independence, $I(A; C|B) = 0$? It is easy to formulate a sufficient condition. Suppose that system $B$ has a decomposition as a direct sum of tensor products of Hilbert spaces

$$
\mathcal{H}_B = \bigoplus_j \mathcal{H}_{B_j} = \bigoplus_j \mathcal{H}_{B_j^L} \otimes \mathcal{H}_{B_j^R},
$$ {#eq-10.86}

and that the state of $ABC$ has the block diagonal form

$$
\rho_{ABC} = \bigoplus_j p_j \rho_{A B_j^L} \otimes \rho_{B_j^R C}.
$$ {#eq-10.87}

In each block labeled by $j$ the state is a tensor product, with conditional mutual information

$$
I(A; C|B_j) = I(A; B_j C) - I(A; B_j) = I(A; B_j^L) - I(A; B_j^L) = 0;
$$ {#eq-10.88}

What is less obvious is that the converse is also true — any state with $I(A; C|B) = 0$ has a decomposition as in eq.(10.87). This is a useful fact, though we will not give the proof here.

### 10.2.4 Monotonicity of mutual information

Strong subadditivity implies another important property of quantum mutual information, its monotonicity — a quantum channel acting on system $B$ cannot increase the mutual information of $A$ and $B$. To derive monotonicity, suppose that a quantum channel $\mathcal{N}^{B \to B'}$ maps $B$ to $B'$. Like any quantum channel, $\mathcal{N}$ has an isometric extension, its Stinespring dilation $U^{B \to B'E}$, mapping $B$ to $B'$ and a suitable environment system $E$. Since the isometry $U$ does not change the eigenvalues of the density operator, it preserves the entropy of $B$ and of $AB$,

$$
H(B) = H(B'E), \quad H(AB) = H(AB'E),
$$ {#eq-10.89}

which implies

$$
\begin{aligned}
I(A; B) &= H(A) + H(B) - H(AB) \\
&= H(A) + H(B'E) - H(AB'E) = I(A; B'E).
\end{aligned}
$$ {#eq-10.90}

From strong subadditivity, we obtain

$$
I(A; B) = I(A; B'E) \ge I(A; B')
$$ {#eq-10.91}

the desired statement of monotonicity.

<!-- Page 26 -->
### 10.2.5 Entropy and thermodynamics

The concept of entropy first entered science through the study of thermodynamics, and the mathematical properties of entropy we have enumerated have many interesting thermodynamic implications. Here we will just mention a few ways in which the nonnegativity and monotonicity of quantum relative entropy relate to ideas encountered in thermodynamics.

There are two distinct ways to approach the foundations of quantum statistical physics. In one, we consider the evolution of an isolated closed quantum system, but ask what we will observe if we have access to only a portion of the full system. Even though the evolution of the full system is unitary, the evolution of a subsystem is not, and the subsystem may be accurately described by a thermal ensemble at late times. Information which is initially encoded locally in an out-of-equilibrium state becomes encoded more and more nonlocally as the system evolves, eventually becoming invisible to an observer confined to the subsystem.

In the other approach, we consider the evolution of an open system $A$, in contact with an unobserved environment $E$, and track the evolution of $A$ only. From a fundamental perspective this second approach may be regarded as a special case of the first, since $AE$ is closed, with $A$ as a privileged subsystem. In practice, though, it is often more convenient to describe the evolution of an open system using a master equation as in Chapter 3, and to analyze evolution toward thermal equilibrium without explicit reference to the environment.

*Free energy and the second law.*
Tools of quantum Shannon theory can help us understand why the state of an open system with Hamiltonian $H$ might be expected to be close to the thermal Gibbs state

$$
\rho_\beta = \frac{e^{-\beta H}}{\mathrm{tr}(e^{-\beta H})},
$$ {#eq-10.92}

where $kT = \beta^{-1}$ is the temperature. Here let's observe one noteworthy feature of this state. For an arbitrary density operator $\rho$, consider its free energy

$$
F(\rho) = E(\rho) - \beta^{-1} S(\rho)
$$ {#eq-10.93}

where $E(\rho) = \langle H\rangle_\rho$ denotes the expectation value of the Hamiltonian in this state; for this subsection we respect the conventions of thermodynamics by denoting von Neumann entropy by $S(\rho)$ rather than $H(\rho)$ (lest $H$ be confused with the Hamiltonian $H$), and by using natural logarithms. Expressing $F(\rho)$ and the free energy $F(\rho_\beta)$ of the Gibbs state as

$$
\begin{aligned}
F(\rho) &= \mathrm{tr}(\rho H) - \beta^{-1} S(\rho) = \beta^{-1} \mathrm{tr}\rho (\ln \rho + \beta H), \\
F(\rho_\beta) &= -\beta^{-1} \ln(\mathrm{tr} e^{-\beta H}),
\end{aligned}
$$ {#eq-10.94}

we see that the relative entropy of $\rho$ and $\rho_\beta$ is

$$
D(\rho\|\rho_\beta) = \mathrm{tr}(\rho \ln \rho) - \mathrm{tr}(\rho \ln \rho_\beta) = \beta(F(\rho) - F(\rho_\beta)) \ge 0,
$$ {#eq-10.95}

with equality only for $\rho = \rho_\beta$. The nonnegativity of relative entropy implies that at a given temperature $\beta^{-1}$, the Gibbs state $\rho_\beta$ has the lowest possible free energy. Our open

<!-- Page 27 -->
system, in contact with a thermal reservoir at temperature $\beta^{-1}$, will prefer the Gibbs state if it wishes to minimize its free energy.

What can we say about the approach to thermal equilibrium of an open system? We may anticipate that the joint unitary evolution of system and reservoir induces a quantum channel $\mathcal{N}$ acting on the system alone, and we know that relative entropy is monotonic — if

$$
\mathcal{N} : \rho \mapsto \rho', \quad \mathcal{N} : \sigma \mapsto \sigma',
$$ {#eq-10.96}

then

$$
D(\rho'\|\sigma') \le D(\rho\|\sigma).
$$ {#eq-10.97}

Furthermore, if the Gibbs state is an equilibrium state, we expect this channel to preserve the Gibbs state

$$
\mathcal{N} : \rho_\beta \mapsto \rho_\beta;
$$ {#eq-10.98}

therefore,

$$
D(\rho'\|\rho_\beta) = \beta(F(\rho') - F(\rho_\beta)) \le \beta(F(\rho) - F(\rho_\beta)) = D(\rho\|\rho_\beta),
$$ {#eq-10.99}

and hence

$$
F(\rho') \le F(\rho).
$$ {#eq-10.100}

Any channel that preserves the Gibbs state cannot increase the free energy; instead, free energy of an out-of-equilibrium state is monotonically decreasing under open-state evolution. This statement is a version of the second law of thermodynamics.

We'll have more to say about how quantum information theory illuminates thermodynamics in §10.8.4.

### 10.2.6 Bekenstein's entropy bound

Similar ideas lead to Bekenstein's bound on entropy in quantum field theory. The field-theoretic details, though interesting, would lead us far afield. The gist is that Bekenstein proposed an inequality relating the energy and the entropy in a bounded spatial region. This bound was motivated by gravitational physics, but can be formulated without reference to gravitation, and follows from properties of relative entropy.

A subtlety is that entropy of a region is infinite in quantum field theory, because of contributions coming from arbitrarily short-wavelength quantum fluctuations near the boundary of the region. Therefore we have to make a subtraction to define a finite quantity. The natural way to do this is to subtract away the entropy of the same region in the vacuum state of the theory, as any finite energy state in a finite volume has the same structure as the vacuum at very short distances. Although the vacuum is a pure state, it, and any other reasonable state, has a marginal state in a finite region which is highly mixed, because of entanglement between the region and its complement.

For the purpose of our discussion here, we may designate any mixed state $\rho_0$ we choose supported in the bounded region as the "vacuum," and define a corresponding "modular Hamiltonian" $K$ by

$$
\rho_0 = \frac{e^{-K}}{\mathrm{tr}(e^{-K})}.
$$ {#eq-10.101}

<!-- Page 28 -->
That is, we regard the state as the thermal mixed state of $K$, with the temperature arbitrarily set to unity (which is just a normalization convention for $K$). Then by rewriting eq.(10.95) we see that, for any state $\rho$, $D(\rho\|\rho_0) \ge 0$ implies

$$
S(\rho) - S(\rho_0) \le \mathrm{tr}(\rho K) - \mathrm{tr}(\rho_0 K).
$$ {#eq-10.102}

The left-hand side, the entropy with vacuum entropy subtracted, is not larger than the right-hand side, the (modular) energy with vacuum energy subtracted. This is one version of Bekenstein's bound. Here $K$, which is dimensionless, can be loosely interpreted as $ER$, where $E$ is the energy contained in the region and $R$ is its linear size.

While the bound follows easily from nonnegativity of relative entropy, the subtle part of the argument is recognizing that the (suitably subtracted) expectation value of the modular Hamiltonian is a reasonable way to define $ER$. The detailed justification for this involves properties of relativistic quantum field theory that we won't go into here. Suffice it to say that, because we constructed $K$ by regarding the marginal state of the vacuum as the Gibbs state associated with the Hamiltonian $K$, we expect $K$ to be linear in the energy, and dimensional analysis then requires inclusion of the factor of $R$ (in units with $\hbar = c = 1$).

Bekenstein was led to conjecture such a bound by thinking about black hole thermodynamics. Leaving out numerical factors, just to get a feel for the orders of magnitude of things, the entropy of a black hole with circumference $\sim R$ is $S \sim R^2/G$, and its mass (energy) is $E \sim R/G$, where $G$ is Newton's gravitational constant; hence $S \sim ER$ for a black hole. Bekenstein realized that unless $S = O(ER)$ for arbitrary states and regions, we could throw extra stuff into the region, making a black hole with lower entropy than the initial state, thus violating the (generalized) second law of thermodynamics. Though black holes provided the motivation, $G$ drops out of the inequality, which holds even in nongravitational relativistic quantum field theories.

### 10.2.7 Entropic uncertainty relations

The uncertainty principle asserts that noncommuting observables cannot simultaneously have definite values. To translate this statement into mathematics, recall that a Hermitian observable $A$ has spectral representation

$$
A = \sum_x |x\rangle a(x) \langle x|
$$ {#eq-10.103}

where $\{|x\rangle\}$ is the orthonormal basis of eigenvectors of $A$ and $\{a(x)\}$ is the corresponding vector of eigenvalues; if $A$ is measured in the state $\rho$, the outcome $a(x)$ occurs with probability $p(x) = \langle x|\rho|x\rangle$. Thus $A$ has expectation value $\mathrm{tr}(\rho A)$ and variance

$$
(\Delta A)^2 = \mathrm{tr}(\rho A^2) - (\mathrm{tr}\rho A)^2.
$$ {#eq-10.104}

Using the Cauchy-Schwarz inequality, we can show that if $A$ and $B$ are two Hermitian observables and $\rho = |\psi\rangle\langle\psi|$ is a pure state, then

$$
\Delta A \Delta B \ge \frac{1}{2} |\langle\psi|[A, B]|\psi\rangle|.
$$ {#eq-10.105}

Eq.(10.105) is a useful statement of the uncertainty principle, but has drawbacks. It depends on the state $|\psi\rangle$ and for that reason does not fully capture the incompatibility of the two observables. Furthermore, the variance does not characterize very well the

<!-- Page 29 -->
unpredictability of the measurement outcomes; entropy would be a more informative measure.

In fact there are entropic uncertainty relations which do not suffer from these deficiencies. If we measure a state $\rho$ by projecting onto the orthonormal basis $\{|x\rangle\}$, the outcomes define a classical ensemble

$$
X = \{x, p(x) = \langle x|\rho|x\rangle\};
$$ {#eq-10.106}

that is, a probability vector whose entries are the diagonal elements of $\rho$ in the $x$-basis. The Shannon entropy $H(X)$ quantifies how uncertain we are about the outcome before we perform the measurement. If $\{|z\rangle\}$ is another orthonormal basis, there is a corresponding classical ensemble $Z$ describing the probability distribution of outcomes when we measure the same state $\rho$ in the $z$-basis. If the two bases are incompatible, there is a tradeoff between our uncertainty about $X$ and about $Z$, captured by the inequality

$$
H(X) + H(Z) \ge \log \left(\frac{1}{c}\right) + H(\rho),
$$ {#eq-10.107}

where

$$
c = \max_{x, z} |\langle x|z\rangle|^2.
$$ {#eq-10.108}

The second term on the right-hand side, which vanishes if $\rho$ is a pure state, reminds us that our uncertainty increases when the state is mixed. Like many good things in quantum information theory, this entropic uncertainty relation follows from the monotonicity of the quantum relative entropy.

For each measurement there is a corresponding quantum channel, realized by performing the measurement and printing the outcome in a classical register,

$$
\begin{aligned}
\mathcal{M}_X : \rho &\mapsto \sum_x |x\rangle\langle x|\rho|x\rangle\langle x| =: \rho_X, \\
\mathcal{M}_Z : \rho &\mapsto \sum_z |z\rangle\langle z|\rho|z\rangle\langle z| =: \rho_Z.
\end{aligned}
$$ {#eq-10.109}

The Shannon entropy of the measurement outcome distribution is also the von Neumann entropy of the corresponding channel's output state,

$$
H(X) = H(\rho_X), \quad H(Z) = H(\rho_Z);
$$ {#eq-10.110}

the entropy of this output state can be expressed in terms of the relative entropy of input and output, and the entropy of the channel input, as in

$$
H(X) = -\mathrm{tr}\rho_X \log \rho_X = -\mathrm{tr}\rho \log \rho_X = D(\rho\|\rho_X) + H(\rho).
$$ {#eq-10.111}

Using the monotonicity of relative entropy under the action of the channel $\mathcal{M}_Z$, we have

$$
D(\rho\|\rho_X) \ge D(\rho_Z\|\mathcal{M}_Z(\rho_X)),
$$ {#eq-10.112}

where

$$
D(\rho_Z\|\mathcal{M}_Z(\rho_X)) = -H(\rho_Z) - \mathrm{tr}\rho_Z \log \mathcal{M}_Z(\rho_X),
$$ {#eq-10.113}

and

$$
\mathcal{M}_Z(\rho_X) = \sum_{x, z} |z\rangle\langle z|x\rangle\langle x|\rho|x\rangle\langle x|z\rangle\langle z|.
$$ {#eq-10.114}

<!-- Page 30 -->
Writing

$$
\log \mathcal{M}_Z(\rho_X) = \sum_z |z\rangle \log \left( \sum_x \langle z|x\rangle\langle x|\rho|x\rangle\langle x|z\rangle \right) \langle z|,
$$ {#eq-10.115}

we see that

$$
-\mathrm{tr}\rho_Z \log \mathcal{M}_Z(\rho_X) = -\sum_z \langle z|\rho|z\rangle \log \left( \sum_x \langle z|x\rangle\langle x|\rho|x\rangle\langle x|z\rangle \right).
$$ {#eq-10.116}

Now, because $-\log(\cdot)$ is a monotonically decreasing function, we have

$$
\begin{aligned}
-\log \left( \sum_x \langle z|x\rangle\langle x|\rho|x\rangle\langle x|z\rangle \right) &\ge -\log \left( \max_{x, z} |\langle x|z\rangle|^2 \sum_x \langle x|\rho|x\rangle \right) \\
&= \log \left(\frac{1}{c}\right),
\end{aligned}
$$ {#eq-10.117}

and therefore

$$
-\mathrm{tr}\rho_Z \log \mathcal{M}_Z(\rho_X) \ge \log \left(\frac{1}{c}\right).
$$ {#eq-10.118}

Finally, putting together eq.(10.111), (10.112), (10.113), (10.118), we find

$$
\begin{aligned}
H(X) - H(\rho) &= D(\rho\|\rho_X) \ge D(\rho_Z\|\mathcal{M}_Z(\rho_X)) \\
&= -H(Z) - \mathrm{tr}\rho_Z \log \mathcal{M}_Z(\rho_X) \ge -H(Z) + \log \left(\frac{1}{c}\right),
\end{aligned}
$$ {#eq-10.119}

which is equivalent to eq.(10.107).

We say that two different bases $\{|x\rangle\}$, $\{|z\rangle\}$ for a $d$-dimensional Hilbert space are *mutually unbiased* if for all $x, z$

$$
|\langle x|z\rangle|^2 = \frac{1}{d};
$$ {#eq-10.120}

thus, if we measure any $x$-basis state $|x\rangle$ in the $z$-basis, all $d$ outcomes are equally probable. For measurements in two mutually unbiased bases performed on a pure state, the entropic uncertainty relation becomes

$$
H(X) + H(Z) \ge \log d.
$$ {#eq-10.121}

Clearly this inequality is tight, as it is saturated by $x$-basis (or $z$-basis) states, for which $H(X) = 0$ and $H(Z) = \log d$.
