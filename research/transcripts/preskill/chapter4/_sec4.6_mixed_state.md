# Section 4.6: Mixed-state entanglement [PDF Pages 41-45]

<!-- ============================================================ -->
<!-- Source: chap4.pdf, Physical Pages: 41-45                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 41 -->
## 4.6 Mixed-state entanglement

The crucial property of quantum entanglement is that it cannot be created *locally*. Up to now in this chapter we have limited our attention to the properties of entangled *pure* states, but it is important to recognize that mixed states can be entangled, too.

Recall that a bipartite pure state $|\Psi\rangle_{AB}$ is *separable* if and only if it is a product state $|\Psi\rangle_{AB} = |\alpha\rangle_A \otimes |\beta\rangle_B$. We say that a bipartite mixed state $\bm{\rho}_{AB}$ is separable if and only if it can be realized as an ensemble of separable pure states,
$$
\bm{\rho}_{AB} = \sum_i p_i (|\alpha_i\rangle\langle\alpha_i|)_A \otimes (|\beta_i\rangle\langle\beta_i|)_B,
\tag{4.112}
$$
where the $p_i$'s are positive and sum to one. Alternatively, we may say that $\bm{\rho}_{AB}$ is separable if and only if it can be expressed as
$$
\bm{\rho}_{AB} = \sum_{i,j} p_{ij} \bm{\rho}_{A,i} \otimes \bm{\rho}_{B,j},
\tag{4.113}
$$

<!-- Page 42 -->
where each $\bm{\rho}_{A,i}$ and $\bm{\rho}_{B,j}$ is a density operator, and the $p_{ij}$'s are positive and sum to one. Thus if a state is separable, the correlations between the state of part $A$ and the state of part $B$ are entirely classical, and embodied by the joint probability distribution $p_{ij}$. The two criteria eq. (4.112) and eq. (4.113) are equivalent because $\bm{\rho}_{A,i}$ and $\bm{\rho}_{B,j}$ can be realized as an ensemble of pure states.

Of course, it may be possible to realize a separable mixed state as an ensemble of entangled pure states as well. A simple example is that the random state $\bm{\rho} = \frac{1}{4}\bm{I} \otimes \bm{I}$ of two qubits can be expressed as either
$$
\bm{\rho} = \frac{1}{4}(|00\rangle\langle 00| + |01\rangle\langle 01| + |10\rangle\langle 10| + |11\rangle\langle 11|)
\tag{4.114}
$$
(an ensemble of product states) or
$$
\bm{\rho} = \frac{1}{4}(|\phi^+\rangle\langle\phi^+| + |\phi^-\rangle\langle\phi^-| + |\psi^+\rangle\langle\psi^+| + |\psi^-\rangle\langle\psi^-|)
\tag{4.115}
$$
(an ensemble of maximally entangled states). The state is separable if and only if there is *some* way to represent is as an ensemble of product states. As for a pure state, if a mixed state is not separable, we say that it is *inseparable* or *entangled*.

Consider two distantly separated parties Alice and Bob who carry out a protocol involving *local operations and classical communication*. That is, Alice is permitted to perform quantum operations on her system $A$, Bob is permitted to perform quantum operations on his system $B$, and Alice and Bob are permitted to exchange classical bits as many times as they want. But no exchange of qubits is permitted. Then if Alice and Bob share a separable state to start with, their state will still be separable at the end of the protocol. The reason is that neither a local operation nor exchange of a classical bit can increase the Schmidt number of a bipartite pure state from the value 1 to a value greater than 1. Of course, Alice and Bob might have a mixed state, but in each step of the protocol an ensemble of product states is transformed to another ensemble of product states. Alice and Bob cannot create entanglement locally if they have none to begin with. In discussions of entanglement, the concept of a protocol that uses only Local Operations and Classical Communication is so prevalent that we will find it convenient to use the abbreviation *LOCC*.

On the other hand, with LOCC, Alice and Bob can prepare *any* separable state. To prepare $\bm{\rho}_{AB}$ in eq. (4.112), Alice generates random numbers to sample the probability distribution $\{p_i\}$; if outcome $i$ is found, she informs Bob, and Alice prepares the $|\alpha_i\rangle_A$ while Bob prepares $|\beta_i\rangle_B$.

<!-- Page 43 -->
### 4.6.1 Positive-partial-transpose criterion for separability

Now, consider a bipartite density operator $\bm{\rho}_{AB}$ on $\mathcal{H}_A \otimes \mathcal{H}_B$, presented as (say) a matrix in some basis. We would like to know whether $\bm{\rho}_{AB}$ is separable. How do we decide? It is not obvious how to devise an efficient algorithm that will definitively answer whether $\bm{\rho}_{AB}$ can be realized as an ensemble of product states. However, it is useful to note that there are necessary conditions for separability that are easy to check.

Recall that relative to a specified orthonormal basis $\{|i\rangle\}$ for a Hilbert space $\mathcal{H}$, a transpose operation $T$ can be defined --- the transpose acts on a basis for the linear operators according to
$$
T : |i\rangle\langle j| \to (|i\rangle\langle j|)^T = |j\rangle\langle i|;
\tag{4.116}
$$
its action on a matrix $M_{ij}$ expressed in this basis is
$$
(M^T)_{ij} = M_{ji}.
\tag{4.117}
$$
Evidently transposition preserves the trace of the matrix $\bm{M}$. If $\bm{M}$ is Hermitian, then its transpose is its complex conjugate, which has the same (real) eigenvalues. Therefore, the transpose of a density operator is another density operator with the same eigenvalues --- the transpose is a trace-preserving positive map.

But we saw in §3.?? that the transpose, although positive, is not *completely positive*; that is, the *partial transpose* $I \otimes T$ can map a bipartite positive operator to an operator that is not positive. For example, the maximally entangled state
$$
|\Phi\rangle = \frac{1}{\sqrt{N}}\sum_{i=0}^{N-1} |i\rangle_A \otimes |i\rangle_B
\tag{4.118}
$$
has density operator
$$
\bm{\rho} = \frac{1}{N}\sum_{i,j}|ii\rangle\langle jj|.
\tag{4.119}
$$
Its partial transpose is
$$
(I \otimes T)(\bm{\rho}) = \frac{1}{N}\sum_{i,j}|ij\rangle\langle ji| = \frac{1}{N}(\text{SWAP});
\tag{4.120}
$$
the SWAP operator has eigenstates with eigenvalue $+1$ (symmetric states) and eigenstates with eigenvalue $-1$ (antisymmetric states) --- hence it is not positive. We will use the notation
$$
\bm{\rho}^{PT} = (I \otimes T)(\bm{\rho})
\tag{4.121}
$$

<!-- Page 44 -->
for the partial transpose of the bipartite density operator $\bm{\rho}$.

While the partial transpose is not a positive map in general, it *is* positive acting on separable states. The partial transpose of $\bm{\rho}_{AB}$ in eq. (4.113) is
$$
\bm{\rho}_{AB}^{PT} = \sum_{i,j} p_{ij}\bm{\rho}_{A,i} \otimes \bm{\rho}_{B,j}^T;
\tag{4.122}
$$
since $\bm{\rho}_{B,j}^T$ is a density operator, so is $\bm{\rho}_{AB}^{PT}$. Thus we arrive at a useful necessary condition for separability.

*Positive partial-transpose criterion for separability:* If $\bm{\rho}_{AB}$ is separable, then $\bm{\rho}_{AB}^{PT}$ is nonnegative.

We will say that a bipartite density operator is *PPT* (for "positive partial transpose) if its partial transpose is nonnegative.

Thus, if we are presented with a density operator $\bm{\rho}_{AB}$, we may compute the eigenvalues of $\bm{\rho}_{AB}^{PT}$; if negative eigenvalues are found, then $\bm{\rho}_{AB}$ is known to be inseparable. But because the PPT condition is necessary but not sufficient for separability, if $\bm{\rho}_{AB}^{PT}$ is found to be nonnegative, then whether $\bm{\rho}_{AB}$ is separable remains unsettled. The PPT criterion is sometimes called the *Peres-Horodecki criterion* for separability.

Let's apply the PPT criterion to a two-qubit state of the form
$$
\bm{\rho}(\lambda) = \lambda|\phi^+\rangle\langle\phi^+| + \frac{1}{4}(1-\lambda)\bm{I}.
\tag{4.123}
$$
This state may also be expressed as
$$
\bm{\rho}(F) = F|\phi^+\rangle\langle\phi^+| + \frac{1}{3}(1-F)\left(|\phi^-\rangle\langle\phi^-| + |\psi^+\rangle\langle\psi^+| + |\psi^-\rangle\langle\psi^-|\right),
\tag{4.124}
$$
where $(1-F) = \frac{3}{4}(1-\lambda)$, and as we saw in §3.??, it results from subjecting half of the state $|\phi^+\rangle$ to the depolarizing channel with error probability $p = 1 - F$. This state is sometimes called a *Werner state* with fidelity $F$.

Now
$$
(|\phi^+\rangle\langle\phi^+|)^{PT} = \frac{1}{2}(\text{SWAP}) = \frac{1}{2}\bm{I} - |\psi^-\rangle\langle\psi^-|,
\tag{4.125}
$$
where the second equality follows from the property that $|\phi^\pm\rangle, |\psi^+\rangle$ (which are symmetric) are eigenvalues of SWAP with eigenvalue 1, and $|\psi^-\rangle$ (which is antisymmetric) is an eigenstate of SWAP with eigenvalue $-1$. Since also $\bm{I}^{PT} = \bm{I}$, we see that the partial transpose of a Werner state is
$$
\begin{aligned}
\bm{\rho}(\lambda)^{PT} &= \lambda\left(\frac{1}{2}\bm{I} - |\psi^-\rangle\langle\psi^-|\right) + \frac{1}{4}(1-\lambda)\bm{I} \\
&= \frac{1}{4}(1+\lambda)\bm{I} - \lambda|\psi^-\rangle\langle\psi^-|.
\end{aligned}
\tag{4.126}
$$

<!-- Page 45 -->
This operator has a negative eigenvalue if $\lambda > 1/3$, and we conclude that the Werner state is inseparable for $\lambda > 1/3$. Therefore, if half of the maximally entangled state $|\phi^+\rangle$ is subjected to the depolarizing channel with error probability $p < 1/2$, the resulting state remains entangled.

Although we won't prove it here, it turns out that for the case of two-qubit states, the PPT criterion is both necessary and sufficient for separability. Thus the Werner state with $\lambda < 1/3$ (or $F < 1/2$) is separable.

While we found that a bipartite pure state is entangled if and only if it violates some Bell inequality, this equivalence does not hold for mixed states. You will show in Exercise 4.?? that for a Werner state with $\lambda = 1/2$ (or any smaller value of $\lambda$) there is a local hidden-variable theory that fully accounts for the correlations between measurements of Alice's qubit and Bob's. Thus, Werner states with $1/3 < \lambda < 1/2$ are inseparable states that violate no Bell inequality.

Oddly, though a Werner state with $1/3 < \lambda < 1/2$ is not Bell-inequality violating, it is nonetheless a shared resource more powerful than classical randomness. You will also show in Exercise 4.?? that by consuming a Werner state Alice and Bob can teleport a qubit in an unknown state with fidelity
$$
F_{\text{teleport}} = \frac{1}{2}(1+\lambda).
\tag{4.127}
$$
This fidelity exceeds the maximal fidelity $F_{\text{teleport}} = 2/3$ that can be achieved without any shared entanglement, for any $\lambda > 1/3$ --- that is, for any inseparable Werner state, whether Bell-inequality violating or not. Even if well described by local hidden variables, an entangled mixed state can be useful.

It seems rather strange that shared entangled states described by local hidden-variable theory should be a more powerful resource than classical shared randomness. Further observations to be discussed in §5.?? will deepen our grasp of the situation. There we will find that if Alice and Bob share *many copies* of the Werner state $\bm{\rho}(\lambda)$ with $1/3 < \lambda < 1/2$, then while local hidden variables provide an adequate description of the correlations if Alice and Bob are restricted to measuring the pairs *one at a time*, violations of Bell inequalities still arise if they are permitted to perform more general kinds of measurements. These observations illustrate that mixed-state entanglement is a surprisingly subtle and elusive concept.
