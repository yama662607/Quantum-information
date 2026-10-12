# Section 10.9: The Decoupling Inequality [PDF Pages 74-84]

<!-- ============================================================ -->
<!-- Source: chap10.pdf, Physical Pages: 74-84                     -->
<!-- Transcribed: 2026-10-12                                       -->
<!-- ============================================================ -->

<!-- Page 74 -->
## 10.9 The Decoupling Inequality

Achievable rates for quantum protocols are derived by using random codes, much as in classical Shannon theory. But this similarity between classical and quantum Shannon theory is superficial — at a deeper conceptual level, quantum protocols differ substantially from classical ones. Indeed, the decoupling principle underlies many of the key findings of quantum Shannon theory, providing a unifying theme that ties together many different results. In particular, the mother and father resource inequalities, and hence all their descendants enumerated above, follow from an inequality that specifies a sufficient condition for decoupling.

This *decoupling inequality* addresses the following question: Suppose that Alice and Eve share a quantum state $\boldsymbol{\sigma}_{AE}$, where $A$ is an $n$-qubit system. This state may be mixed, but in general $A$ and $E$ are correlated; that is, $I(A; E) > 0$. Now Alice starts discarding qubits one at a time, where each qubit is a randomly selected two-dimensional subsystem of what Alice holds. Each time Alice discards a qubit, her correlation with $E$ grows weaker. How many qubits should she discard so that the subsystem she retains has a negligible correlation with Eve's system $E$?

<!-- Page 75 -->
To make the question precise, we need to formalize what it means to discard a random qubit. More generally, suppose that $A$ has dimension $|A|$, and Alice decomposes $A$ into subsystems $A_1$ and $A_2$, then discards $A_1$ and retains $A_2$. We would like to consider many possible ways of choosing the discarded system with specified dimension $|A_1|$. Equivalently, we may consider a fixed decomposition $A = A_1 A_2$, where we apply a unitary transformation $\boldsymbol{U}$ to $A$ before discarding $A_1$. Then discarding a random subsystem with dimension $|A_1|$ is the same thing as applying a random unitary $\boldsymbol{U}$ before discarding the fixed subsystem $A_1$:

```
             +----+      A1
        A /--|    |-----------
         /   | U  |
  \sigma_{AE} |    |-----------
         \   +----+      A2
        E \-------------------
```

To analyze the consequences of discarding a random subsystem, then, we will need to be able to compute the expectation value of a function $f(\boldsymbol{U})$ when we average $\boldsymbol{U}$ uniformly over the group of unitary $|A| \times |A|$ matrices. We denote this expectation value as $\mathbb{E}_{\boldsymbol{U}}[f(\boldsymbol{U})]$; to perform computations we will only need to know that $\mathbb{E}_{\boldsymbol{U}}$ is suitably normalized, and is invariant under left or right multiplication by any constant unitary matrix $\boldsymbol{V}$:
$$
\mathbb{E}_{\boldsymbol{U}}[1] = 1, \quad \mathbb{E}_{\boldsymbol{U}}[f(\boldsymbol{U})] = \mathbb{E}_{\boldsymbol{U}}[f(\boldsymbol{V}\boldsymbol{U})] = \mathbb{E}_{\boldsymbol{U}}[f(\boldsymbol{U}\boldsymbol{V})].
$$ {#eq-10.339}
These conditions uniquely define $\mathbb{E}_{\boldsymbol{U}}[f(\boldsymbol{U})]$, which is sometimes described as the integral over the unitary group using the *invariant measure* or *Haar measure* on the group.

If we apply the unitary transformation $\boldsymbol{U}$ to $A$, and then discard $A_1$, the marginal state of $A_2 E$ is
$$
\boldsymbol{\sigma}_{A_2 E}(\boldsymbol{U}) := \mathrm{tr}_{A_1}\left((\boldsymbol{U}_A \otimes \boldsymbol{I}_E) \boldsymbol{\sigma}_{AE} (\boldsymbol{U}_A^\dagger \otimes \boldsymbol{I}_E)\right).
$$ {#eq-10.340}
The decoupling inequality expresses how close (in the $L^1$ norm) $\boldsymbol{\sigma}_{A_2 E}$ is to a product state when we average over $\boldsymbol{U}$:
$$
\left(\mathbb{E}_{\boldsymbol{U}}\left[\|\boldsymbol{\sigma}_{A_2 E}(\boldsymbol{U}) - \boldsymbol{\sigma}_{A_2}^{\max} \otimes \boldsymbol{\sigma}_E\|_1\right]\right)^2 \le \frac{|A_2| \cdot |E|}{|A_1|} \mathrm{tr}\left(\boldsymbol{\sigma}_{AE}^2\right),
$$ {#eq-10.341}
where
$$
\boldsymbol{\sigma}_{A_2}^{\max} := \frac{1}{|A_2|} \boldsymbol{I}
$$ {#eq-10.342}
denotes the maximally mixed state on $A_2$, and $\boldsymbol{\sigma}_E$ is the marginal state $\mathrm{tr}_A \boldsymbol{\sigma}_{AE}$.

<!-- Page 76 -->
This inequality has interesting consequences even in the case where there is no system $E$ at all and $\boldsymbol{\sigma}_A$ is pure, where it becomes
$$
\mathbb{E}_{\boldsymbol{U}}\left[\|\boldsymbol{\sigma}_{A_2}(\boldsymbol{U}) - \boldsymbol{\sigma}_{A_2}^{\max}\|_1\right] \le \sqrt{\frac{|A_2|}{|A_1|} \mathrm{tr}\left(\boldsymbol{\sigma}_A^2\right)} = \sqrt{\frac{|A_2|}{|A_1|}}.
$$ {#eq-10.343}
Eq.(10.343) implies that, for a randomly chosen pure state of the bipartite system $A = A_1 A_2$, where $|A_2|/|A_1| \ll 1$, the density operator on $A_2$ is very nearly maximally mixed with high probability. One can likewise show that the expectation value of the entanglement entropy of $A_1 A_2$ is very close to the maximal value: $\mathbb{E}[H(A_2)] \ge \log_2 |A_2| - |A_2|/(2|A_1| \ln 2)$. Thus, if for example $A_2$ is 50 qubits and $A_1$ is 100 qubits, the typical entropy deviates from maximal by only about $2^{-50} \approx 10^{-15}$.

### 10.9.1 Proof of the decoupling inequality

To prove the decoupling inequality, we will first bound the distance between $\boldsymbol{\sigma}_{A_2 E}$ and a product state in the $L^2$ norm, and then use the Cauchy-Schwarz inequality to obtain a bound on the $L^1$ distance. Eq.(10.341) follows from
$$
\mathbb{E}_{\boldsymbol{U}}\left[\|\boldsymbol{\sigma}_{A_2 E}(\boldsymbol{U}) - \boldsymbol{\sigma}_{A_2}^{\max} \otimes \boldsymbol{\sigma}_E\|_2^2\right] \le \frac{1}{|A_1|} \mathrm{tr}\left(\boldsymbol{\sigma}_{AE}^2\right),
$$ {#eq-10.344}
combined with
$$
(\mathbb{E}[f(\boldsymbol{U})])^2 \le \mathbb{E}[f(\boldsymbol{U})^2] \quad \text{and} \quad \|M\|_1^2 \le d \|M\|_2^2
$$ {#eq-10.345}
(for nonnegative $f$), which implies
$$
(\mathbb{E}[\|\cdot\|_1])^2 \le \mathbb{E}[\|\cdot\|_1^2] \le |A_2| \cdot |E| \cdot \mathbb{E}[\|\cdot\|_2^2].
$$ {#eq-10.346}
We also note that
$$
\begin{aligned}
\|\boldsymbol{\sigma}_{A_2 E} - \boldsymbol{\sigma}_{A_2}^{\max} \otimes \boldsymbol{\sigma}_E\|_2^2 &= \mathrm{tr}\left(\boldsymbol{\sigma}_{A_2 E} - \boldsymbol{\sigma}_{A_2}^{\max} \otimes \boldsymbol{\sigma}_E\right)^2 \\
&= \mathrm{tr}\left(\boldsymbol{\sigma}_{A_2 E}^2\right) - \frac{1}{|A_2|}\mathrm{tr}\left(\boldsymbol{\sigma}_E^2\right),
\end{aligned}
$$ {#eq-10.347}
because
$$
\mathrm{tr}\left(\boldsymbol{\sigma}_{A_2}^{\max}\right)^2 = \frac{1}{|A_2|};
$$ {#eq-10.348}
therefore, to prove eq.(10.344) it suffices to show
$$
\mathbb{E}_{\boldsymbol{U}}\left[\mathrm{tr}\left(\boldsymbol{\sigma}_{A_2 E}^2(\boldsymbol{U})\right)\right] \le \frac{1}{|A_2|}\mathrm{tr}\left(\boldsymbol{\sigma}_E^2\right) + \frac{1}{|A_1|}\mathrm{tr}\left(\boldsymbol{\sigma}_{AE}^2\right).
$$ {#eq-10.349}
We can facilitate the computation of $\mathbb{E}_{\boldsymbol{U}}\left[\mathrm{tr}\left(\boldsymbol{\sigma}_{A_2 E}^2(\boldsymbol{U})\right)\right]$ using a clever trick. For any bipartite system $BC$, imagine introducing a second copy $B'C'$ of the system. Then (Exercise 10.22)
$$
\mathrm{tr}_C\left(\boldsymbol{\sigma}_C^2\right) = \mathrm{tr}_{BCB'C'}\left((\boldsymbol{I}_{BB'} \otimes \boldsymbol{S}_{CC'})(\boldsymbol{\sigma}_{BC} \otimes \boldsymbol{\sigma}_{B'C'})\right),
$$ {#eq-10.350}
where $\boldsymbol{S}_{CC'}$ denotes the swap operator, which acts as
$$
\boldsymbol{S}_{CC'} : |i\rangle_C \otimes |j\rangle_{C'} \mapsto |j\rangle_C \otimes |i\rangle_{C'}.
$$ {#eq-10.351}

<!-- Page 77 -->
In particular, then,
$$
\begin{aligned}
\mathrm{tr}_{A_2 E}\left(\boldsymbol{\sigma}_{A_2 E}^2(\boldsymbol{U})\right) &= \mathrm{tr}_{AEA'E'}\left((\boldsymbol{I}_{A_1 A'_1} \otimes \boldsymbol{S}_{A_2 A'_2} \otimes \boldsymbol{S}_{EE'})(\boldsymbol{\sigma}_{AE}(\boldsymbol{U}) \otimes \boldsymbol{\sigma}_{A'E'}(\boldsymbol{U}))\right) \\
&= \mathrm{tr}_{AEA'E'}\left((\boldsymbol{M}_{AA'}(\boldsymbol{U}) \otimes \boldsymbol{S}_{EE'})(\boldsymbol{\sigma}_{AE} \otimes \boldsymbol{\sigma}_{A'E'})\right),
\end{aligned}
$$ {#eq-10.352}
where
$$
\boldsymbol{M}_{AA'}(\boldsymbol{U}) = \left(\boldsymbol{U}_A^\dagger \otimes \boldsymbol{U}_{A'}^\dagger\right)\left(\boldsymbol{I}_{A_1 A'_1} \otimes \boldsymbol{S}_{A_2 A'_2}\right)\left(\boldsymbol{U}_A \otimes \boldsymbol{U}_{A'}\right).
$$ {#eq-10.353}
The expectation value of $\boldsymbol{M}_{AA'}(\boldsymbol{U})$ is evaluated in Exercise 10.22; there we find
$$
\mathbb{E}_{\boldsymbol{U}}[\boldsymbol{M}_{AA'}(\boldsymbol{U})] = c_I \boldsymbol{I}_{AA'} + c_S \boldsymbol{S}_{AA'}
$$ {#eq-10.354}
where
$$
c_I = \frac{1}{|A_2|}\frac{1 - 1/|A_1|^2}{1 - 1/|A|^2} \le \frac{1}{|A_2|}, \quad c_S = \frac{1}{|A_1|}\frac{1 - 1/|A_2|^2}{1 - 1/|A|^2} \le \frac{1}{|A_1|}.
$$ {#eq-10.355}
Plugging into eq.(10.352), we then obtain
$$
\begin{aligned}
\mathbb{E}_{\boldsymbol{U}}\left[\mathrm{tr}_{A_2 E}\left(\boldsymbol{\sigma}_{A_2 E}^2(\boldsymbol{U})\right)\right] &\le \mathrm{tr}_{AEA'E'}\left(\left(\frac{1}{|A_2|}\boldsymbol{I}_{AA'} + \frac{1}{|A_1|}\boldsymbol{S}_{AA'}\right) \otimes \boldsymbol{S}_{EE'} (\boldsymbol{\sigma}_{AE} \otimes \boldsymbol{\sigma}_{A'E'})\right) \\
&= \frac{1}{|A_2|}\mathrm{tr}\left(\boldsymbol{\sigma}_E^2\right) + \frac{1}{|A_1|}\mathrm{tr}\left(\boldsymbol{\sigma}_{AE}^2\right),
\end{aligned}
$$ {#eq-10.356}
thus proving eq.(10.349) as desired.

### 10.9.2 Proof of the mother inequality

The mother inequality eq.(10.327) follows from the decoupling inequality eq.(10.341) in an i.i.d. setting. Suppose Alice, Bob, and Eve share the pure state $\phi_{ABE}^{\otimes n}$. Then there are jointly typical subspaces of $A^n, B^n$, and $E^n$, which we denote by $\bar{A}, \bar{B}, \bar{E}$, such that
$$
|\bar{A}| = 2^{n(H(A) + o(1))}, \quad |\bar{B}| = 2^{n(H(B) + o(1))}, \quad |\bar{E}| = 2^{n(H(E) + o(1))}.
$$ {#eq-10.357}
Furthermore, the normalized pure state $\phi'_{\bar{A}\bar{B}\bar{E}}$ obtained by projecting $\phi_{ABE}^{\otimes n}$ onto $\bar{A} \otimes \bar{B} \otimes \bar{E}$ deviates from $\phi_{ABE}^{\otimes n}$ by distance $o(1)$ in the $L^1$ norm.

In order to transfer the purification of $E^n$ to Bob, Alice first projects $A^n$ onto its typical subspace, succeeding with probability $1 - o(1)$, and compresses the result. She then divides her compressed system $\bar{A}$ into two parts $\bar{A}_1 \bar{A}_2$, and applies a random unitary to $\bar{A}$ before sending $\bar{A}_1$ to Bob. Quantum state transfer is achieved if $\bar{A}_2$ decouples from $\bar{E}$.

Because $\phi'_{\bar{A}\bar{B}\bar{E}}$ is close to $\phi_{ABE}^{\otimes n}$, we can analyze whether the protocol is successful by supposing the initial state is $\phi'_{\bar{A}\bar{B}\bar{E}}$ rather than $\phi_{ABE}^{\otimes n}$. According to the decoupling

<!-- Page 78 -->
inequality
$$
\begin{aligned}
\left(\mathbb{E}_{\boldsymbol{U}}\left[\|\boldsymbol{\sigma}_{\bar{A}_2 \bar{E}}(\boldsymbol{U}) - \boldsymbol{\sigma}_{\bar{A}_2}^{\max} \otimes \boldsymbol{\sigma}_{\bar{E}}\|_1\right]\right)^2 &\le \frac{|\bar{A}| \cdot |\bar{E}|}{|\bar{A}_1|^2} \mathrm{tr}\left(\boldsymbol{\sigma}_{\bar{A}\bar{E}}^2\right) \\
&= \frac{1}{|\bar{A}_1|^2} 2^{n(H(A) + H(E) + o(1))} \mathrm{tr}\left(\boldsymbol{\sigma}_{\bar{A}\bar{E}}^2\right) \\
&= \frac{1}{|\bar{A}_1|^2} 2^{n(H(A) + H(E) - H(B) + o(1))};
\end{aligned}
$$ {#eq-10.358}
here we have used properties of typical subspaces in the second line, as well as the property that $\boldsymbol{\sigma}_{\bar{A}\bar{E}}$ and $\boldsymbol{\sigma}_{\bar{B}}$ have the same nonzero eigenvalues, because $\phi'_{\bar{A}\bar{B}\bar{E}}$ is pure.

Eq.(10.358) bounds the $L^1$ distance of $\boldsymbol{\sigma}_{\bar{A}_2 \bar{E}}(\boldsymbol{U})$ from a product state when averaged over all unitaries, and therefore suffices to ensure the existence of at least one unitary transformation $\boldsymbol{U}$ such that the $L^1$ distance is bounded above by the right-hand side. Therefore, by choosing this $\boldsymbol{U}$, Alice can decouple $\bar{A}_2$ from $E^n$ to $o(1)$ accuracy in the $L^1$ norm by sending to Bob
$$
\log_2 |\bar{A}_1| = \frac{n}{2}(H(A) + H(E) - H(B) + o(1)) = \frac{n}{2}(I(A; E) + o(1))
$$ {#eq-10.359}
qubits, suitably chosen from the (compressed) typical subspace of $A^n$. Alice retains $|\bar{A}_2| = n H(A) - \frac{n}{2} I(A; E) - o(n)$ qubits of her compressed system, which are nearly maximally mixed and uncorrelated with $E^n$; hence at the end of the protocol she shares with Bob this many qubit pairs, which have high fidelity with a maximally entangled state. Since $\phi_{ABE}$ is pure, and therefore $H(A) = \frac{1}{2}(I(A; E) + I(A; B))$, we conclude that Alice and Bob distill $\frac{n}{2} I(A; B) - o(n)$ ebits of entanglement, thus proving the mother resource inequality.

We can check that this conclusion is plausible using a crude counting argument. Disregarding the $o(n)$ corrections in the exponent, the state $\phi_{ABE}^{\otimes n}$ is nearly maximally mixed on a typical subspace of $A^n E^n$ with dimension $2^{n H(AE)}$, i.e. the marginal state on $\bar{A}\bar{E}$ can be realized as a nearly uniform ensemble of this many mutually orthogonal states. If $\bar{A}_1$ is randomly chosen and sufficiently small, we expect that, for each state in this ensemble, $\bar{A}_1$ is nearly maximally entangled with a subsystem of the much larger system $\bar{A}_2 \bar{E}$, and that the marginal states on $\bar{A}_2 \bar{E}$ arising from different states in the $\bar{A}\bar{E}$ ensemble have a small overlap. Therefore, we anticipate that tracing out $\bar{A}_1$ yields a state on $\bar{A}_2 \bar{E}$ which is nearly maximally mixed on a subspace with dimension $|\bar{A}_1| 2^{n H(AE)}$. Approximate decoupling occurs when this state attains full rank on $\bar{A}_2 \bar{E}$, since in that case it is close to maximally mixed on $\bar{A}_2 \bar{E}$ and therefore close to a product state on its support. The state transfer succeeds, therefore, provided
$$
|\bar{A}_1| 2^{n H(AE)} \approx |\bar{A}_2| \cdot |\bar{E}| = \frac{|\bar{A}| \cdot |\bar{E}|}{|\bar{A}_1|} \approx \frac{2^{n(H(A) + H(E))}}{|\bar{A}_1|} \implies |\bar{A}_1|^2 \approx 2^{n I(A; E)},
$$ {#eq-10.360}
as in eq.(10.359).

Our derivation of the mother resource inequality, based on random coding, does not exhibit any concrete protocol that achieves the claimed rate, nor does it guarantee the existence of any protocol in which the required quantum processing can be executed efficiently. Concerning the latter point, it is notable that our derivation of the decoupling inequality applies not just to the expectation value averaged uniformly over the unitary group, but also to any average over unitary transformations which satisfies eq.(10.354). In fact, this identity is satisfied by a uniform average over the Clifford group, which

<!-- Page 79 -->
means that there is some Clifford transformation on $\bar{A}$ which achieves the rates specified in the mother resource inequality. Any Clifford transformation on $n$ qubits can be reached by a circuit with $O(n^2)$ gates. Since it is also known that Schumacher compression can be achieved by a polynomial-time quantum computation, Alice's encoding operation can be carried out efficiently.

In fact, after compressing, Alice encodes the quantum information she sends to Bob using a stabilizer code (with Clifford encoder $\boldsymbol{U}$), and Bob's task, after receiving $\bar{A}_1$ is to correct the erasure of $\bar{A}_2$. Bob can replace each erased qubit by the standard state $|0\rangle$, and then measure the code's check operators. With high probability, there is a unique Pauli operator acting on the erased qubits that restores Bob's state to the code space, and the recovery operation can be efficiently computed using linear algebra. Hence, Bob's part of the mother protocol, like Alice's, can be executed efficiently. (Projections onto typical subspaces are used in the proof of the mother inequality, but not in the protocol itself, so we don't need to worry about whether these projections can be performed efficiently.)

### 10.9.3 Proof of the father inequality

*One-shot version.*
In the one-shot version of the father protocol, Alice and Bob share a pair of maximally entangled systems $A_1 B_1$, and in addition Alice holds input state $\boldsymbol{\rho}_{A_2}$ of system $A_2$ which she wants to convey to Bob. Alice encodes $\boldsymbol{\rho}_{A_2}$ by applying a unitary transformation $\boldsymbol{V}$ to $A = A_1 A_2$, then sends $A$ to Bob via the noisy quantum channel $\mathcal{N}^{A \to B_2}$. Bob applies a decoding map $\mathcal{D}^{B_1 B_2 \to \tilde{A}_2}$ jointly to the channel output and his half of the entangled state he shares with Alice, hoping to recover Alice's input state with high fidelity:

```
  B1 -------------------------------------------+
                                                |
  A1 \----+----+                                |  +-----+
      \---|    |                                +--|     |
          | V  |--- A ---+----+--- B2 -------------|  D  |---- \tilde{A}_2
  A2 /----|    |         | N  |                    |     |
    /     +----+         +----+                 +--|     |
                                                |  +-----+
```

We would like to know how much shared entanglement suffices for Alice and Bob to succeed.

This question can be answered using the decoupling inequality. First we introduce a reference system $R'$ which is maximally entangled with $A_2$; then Bob succeeds if his decoder can extract the purification of $R'$. Because the system $R' B_1$ is maximally entangled with $A_1 A_2$, the encoding unitary $\boldsymbol{V}$ acting on $A_1 A_2$ can be replaced by its transpose $\boldsymbol{V}^T$ acting on $R' B_1$. We may also replace $\mathcal{N}$ by its Stinespring dilation $\boldsymbol{U}^{A_1 A_2 \to B_2 E}$, so that the extended output state $\phi$ of $R' B_1 B_2 E$ is pure:

```
  R' \----------------------------------           R' \----+----+-------------
      \                                                \---|    |
  B1 --\--------------------------------           B1 -----| V^T|-------------
        \                                                  |    |
         \----+----+----+----+--- B2                       +----+
  A1 -----|   |    |    |    |
          | V |    | U  |    |                     A1 \----+----+--- B2
  A2 -----|   |    |    |    |--- E                        |    |
          +---+----+----+----+                     A2 -----| U  |--- E
                                                           +----+
```

<!-- Page 80 -->
Finally we invoke the decoupling principle — if $R'$ and $E$ decouple, then $R'$ is purified by a subsystem of $B_1 B_2$, which means that Bob can recover $\boldsymbol{\rho}_{A_2}$ with a suitable decoding map.

If we consider $\boldsymbol{V}$, and hence also $\boldsymbol{V}^T$, to be a random unitary, then we may describe the situation this way: We have a tripartite pure state $\phi_{R B_2 E}$, where $R = R' B_1$, and we would like to know whether the marginal state of $R' E$ is close to a product state when the random subsystem $B_1$ is discarded from $R$. This is exactly the question addressed by the decoupling inequality, which in this case may be expressed as
$$
\left(\mathbb{E}_{\boldsymbol{V}}\left[\|\boldsymbol{\sigma}_{R' E}(\boldsymbol{V}) - \boldsymbol{\sigma}_{R'}^{\max} \otimes \boldsymbol{\sigma}_E\|_1\right]\right)^2 \le \frac{|R| \cdot |E|}{|B_1|^2} \mathrm{tr}\left(\boldsymbol{\sigma}_{RE}^2\right).
$$ {#eq-10.361}
Eq.(10.361) asserts that the $L^1$ distance from a product state is bounded above when averaged uniformly over all unitary $\boldsymbol{V}$'s; therefore there must be some particular encoding unitary $\boldsymbol{V}$ that satisfies the same bound. We conclude that near-perfect decoupling of $R' E$, and therefore high-fidelity decoding of $B_2$, is achievable provided that
$$
|A_1| = |B_1| \gg |R'| \cdot |E| \, \mathrm{tr}\left(\boldsymbol{\sigma}_{RE}^2\right) = |A_2| \cdot |E| \, \mathrm{tr}\left(\boldsymbol{\sigma}_{B_2}^2\right),
$$ {#eq-10.362}
where to obtain the second equality we use the purity of $\phi_{R B_2 E}$ and recall that the reference system $R'$ is maximally entangled with $A_2$, and therefore has the same dimension.

*i.i.d. version.*
In the i.i.d. version of the father protocol, Alice and Bob achieve high fidelity entanglement-assisted quantum communication through $n$ uses of the quantum channel $\mathcal{N}^{A \to B}$. The code they use for this purpose can be described in the following way: Consider an input density operator $\boldsymbol{\rho}_A$ of system $A$, which is purified by a reference system $R$. Sending the purified input state $\psi_{RA}$ through $\boldsymbol{U}^{A \to BE}$, the isometric dilation of $\mathcal{N}^{A \to B}$, generates the tripartite pure state $\phi_{RBE}$. Evidently applying $\left(\boldsymbol{U}^{A \to BE}\right)^{\otimes n}$ to $\psi_{RA}^{\otimes n}$ produces $\phi_{RBE}^{\otimes n}$.

But now suppose that before transmitting the state to Bob, Alice projects $A^n$ onto its typical subspace $\bar{A}$, succeeding with probability $1 - o(1)$ in preparing a state of $\bar{A}\bar{R}$ that is nearly maximally entangled, where $\bar{R}$ is the typical subspace of $R^n$. Imagine dividing $\bar{R}$ into a randomly chosen subsystem $B_1$ and its complementary subsystem $R'$; then there is a corresponding decomposition of $\bar{A} = A_1 A_2$ such that $A_1$ is very nearly maximally entangled with $B_1$ and $A_2$ is very nearly maximally entangled with $R'$.

If we interpret $B_1$ as Bob's half of an entangled state of $A_1 B_1$ shared with Alice, this becomes the setting where the one-shot father protocol applies, if we ignore the small deviation from maximal entanglement in $A_1 B_1$ and $R' A_2$. As for our analysis of the i.i.d. mother protocol, we apply the one-shot father inequality not to $\phi_{RBE}^{\otimes n}$, but rather to the nearby state $\phi'_{\bar{R}\bar{B}\bar{E}}$, where $\bar{B}$ and $\bar{E}$ are the typical subspaces of $B^n$ and $E^n$ respectively. Applying eq.(10.361), and using properties of typical subspaces, we can bound the square of the $L^1$ deviation of $R'\bar{E}$ from a product state, averaged over the choice of $B_1$, by
$$
\frac{|\bar{R}| \cdot |\bar{E}|}{|B_1|^2} \mathrm{tr}\left(\boldsymbol{\sigma}_{\bar{B}}^2\right) = \frac{2^{n(H(R) + H(E) - H(B) + o(1))}}{|B_1|^2} = \frac{2^{n(I(R; E) + o(1))}}{|B_1|^2};
$$ {#eq-10.363}
hence the bound also applies for some particular way of choosing $B_1$. This choice defines

<!-- Page 81 -->
the code used by Alice and Bob in a protocol which consumes
$$
\log_2 |B_1| = \frac{n}{2} I(R; E) + o(n)
$$ {#eq-10.364}
ebits of entanglement, and conveys from Alice to Bob
$$
n H(R) - \frac{n}{2} I(R; E) - o(n) = \frac{n}{2} I(R; B) - o(n)
$$ {#eq-10.365}
high-fidelity qubits. This proves the father resource inequality.

### 10.9.4 Quantum channel capacity revisited

In §10.8.1 we showed that the coherent information is an achievable rate for quantum communication over a noisy quantum channel. That derivation, a corollary of the father resource inequality, applied to a catalytic setting, in which shared entanglement between sender and receiver can be borrowed and later repaid. It is useful to see that the same rate is achievable without catalysis, a result we can derive from an alternative version of the decoupling inequality.

This version applies to the setting depicted here:

```
              R \----+----+--- |0> (R1)
                 \   | V  |
  \psi_{RA}       \--|    |--- R2
                  /  +----+
                 /
              A /----+----+--- B
                     | U  |
                     |    |--- E
                     +----+
```

A density operator $\boldsymbol{\rho}_A$ for system $A$, with purification $\psi_{RA}$, is transmitted through a channel $\mathcal{N}^{A \to B}$ which has the isometric dilation $\boldsymbol{U}^{A \to BE}$. The reference system $R$ has a decomposition into subsystems $R_1 R_2$. We apply a random unitary transformation $\boldsymbol{V}$ to $R$, then project $R_1$ onto a fixed vector $|0\rangle_{R_1}$, and renormalize the resulting state. In effect, then we are projecting $R$ onto a subspace with dimension $|R_2|$, which purifies a corresponding code subspace of $A$. This procedure prepares a normalized pure state $\phi_{R_2 B E}$, and a corresponding normalized marginal state $\boldsymbol{\sigma}_{R_2 E}$ of $R_2 E$.

If $R_2$ decouples from $E$, then $R_2$ is purified by a subsystem of $B$, which means that the code subspace of $A$ can be recovered by a decoder applied to $B$. A sufficient condition for approximate decoupling can be derived from the inequality
$$
\left(\mathbb{E}_{\boldsymbol{V}}\left[\|\boldsymbol{\sigma}_{R_2 E}(\boldsymbol{V}) - \boldsymbol{\sigma}_{R_2}^{\max} \otimes \boldsymbol{\sigma}_E\|_1\right]\right)^2 \le |R_2| \cdot |E| \, \mathrm{tr}\left(\boldsymbol{\sigma}_{RE}^2\right).
$$ {#eq-10.366}
Eq.(10.366) resembles eq.(10.341) and can be derived by a similar method. Note that the right-hand side of eq.(10.366) is enhanced by a factor of $|R_1|$ relative to the right-hand side of eq.(10.341). This factor arises because after projecting $R_1$ onto the fixed state $|0\rangle$ we need to renormalize the state by multiplying by $|R_1|$, while on the other hand the projection suppresses the expected distance squared from a product state by a factor $|R_1|$.

In the i.i.d. setting where the noisy channel is used $n$ times, we consider $\phi_{RBE}^{\otimes n}$, and project onto the jointly typical subspaces $\bar{R}, \bar{B}, \bar{E}$ of $R^n, B^n, E^n$ respectively, succeeding with high probability. We choose a code by projecting $\bar{R}$ onto a random subspace with dimension $|R_2|$. Then, the right-hand side of eq.(10.366) becomes
$$
|R_2| \cdot 2^{n(H(E) - H(B) + o(1))},
$$ {#eq-10.367}
and since the inequality holds when we average uniformly over $\boldsymbol{V}$, it surely holds for

<!-- Page 82 -->
some particular $\boldsymbol{V}$. That unitary defines a code which achieves decoupling and has the rate
$$
\frac{1}{n} \log_2 |R_2| = H(E) - H(B) - o(1) = I_c(R \rangle B) - o(1).
$$ {#eq-10.368}
Hence the coherent information is an achievable rate for high-fidelity quantum communication over the noisy channel.

### 10.9.5 Black holes as mirrors

As our final application of the decoupling inequality, we consider a highly idealized model of black hole dynamics. Suppose that Alice holds a $k$-qubit system $A$ which she wants to conceal from Bob. To be safe, she discards her qubits by tossing them into a large black hole, where she knows Bob will not dare to follow. The black hole $B$ is an $(n - k)$-qubit system, which grows to $n$ qubits after merging with $A$, where $n$ is much larger than $k$.

Black holes are not really completely black — they emit Hawking radiation. But qubits leak out of an evaporating black hole very slowly, at a rate per unit time which scales like $n^{-1/2}$. Correspondingly, it takes time $\Theta(n^{3/2})$ for the black hole to radiate away a significant fraction of its qubits. Because the black hole Hilbert space is so enormous, this is a very long time, about $10^{67}$ years for a solar mass black hole, for which $n \approx 10^{78}$. Though Alice's qubits might not remain secret forever, she is content knowing that they will be safe from Bob for $10^{67}$ years.

But in her haste, Alice fails to notice that her black hole is very, very old. It has been evaporating for so long that it has already radiated away more than half of its qubits. Let's assume that the joint state of the black hole and its emitted radiation is pure, and furthermore that the radiation is a Haar-random subsystem of the full system.

Because the black hole $B$ is so old, $|B|$ is much smaller than the dimension of the radiation subsystem; therefore, as in eq.(10.343), we expect the state of $B$ to be very nearly maximally mixed with high probability. We denote by $R_B$ the subsystem of the emitted radiation which purifies $B$; thus the state of $B R_B$ is very nearly maximally entangled. We assume that $R_B$ has been collected by Bob and is under his control.

To keep track of what happens to Alice's $k$ qubits, we suppose that her $k$-qubit system $A$ is maximally entangled with a reference system $R_A$. After $A$ enters the black hole, Bob waits for a while, until the $k'$-qubit system $A'$ is emitted in the black hole's Hawking radiation. After retrieving $A'$, Bob hopes to recover the purification of $R_A$ by applying a suitable decoding map to $A' R_B$. Can he succeed?

We've learned that Bob can succeed with high fidelity if the remaining black hole system $B'$ decouples from Alice's reference system $R_A$. Let's suppose that the qubits emitted in the Hawking radiation are chosen randomly; that is, $A'$ is a Haar-random $k'$-qubit subsystem of the $n$-qubit system $AB$, as depicted here:

<!-- Page 83 -->
```
        RB ========================================= RB
       //                                            (Bob)
      //
     B  \==========+----+--------------------------- A'
                   |    |                            (Bob)
     A  /----------| U  |=========================== B'
       /           |    |
      RA           +----+
       \-------------------------------------------- RA
     (Alice)
```

The double lines indicate the very large systems $B$ and $B'$, and single lines the smaller systems $A$ and $A'$. Because the radiated qubits are random, we can determine whether $R_A B'$ decouples using the decoupling inequality, which for this case becomes
$$
\mathbb{E}_{\boldsymbol{U}}\left[\|\boldsymbol{\sigma}_{B' R_A}(\boldsymbol{U}) - \boldsymbol{\sigma}_{B'}^{\max} \otimes \boldsymbol{\sigma}_{R_A}\|_1\right] \le \sqrt{\frac{|A B R_A|}{|A'|^2} \mathrm{tr}\left(\boldsymbol{\sigma}_{A B R_A}^2\right)}.
$$ {#eq-10.369}
Because the state of $A R_A$ is pure, and $B$ is maximally entangled with $R_B$, we have $\mathrm{tr}\left(\boldsymbol{\sigma}_{A B R_A}^2\right) = 1/|B|$, and therefore the Haar-averaged $L^1$ distance of $\boldsymbol{\sigma}_{B' R_A}$ from a product state is bounded above by
$$
\sqrt{\frac{|A R_A|}{|A'|^2}} = \frac{|A|}{|A'|}.
$$ {#eq-10.370}
Thus, if Bob waits for only $k' = k + c$ qubits of Hawking radiation to be emitted after Alice tosses in her $k$ qubits, Bob can decode her qubits with excellent fidelity $F \ge 1 - 2^{-c}$.

Alice made a serious mistake. Rather than waiting for $\Omega(n)$ qubits to emerge from the black hole, Bob can already decode Alice's secret quite well when he has collected just a few more than $k$ qubits. And Bob is an excellent physicist, who knows enough about black hole dynamics to infer the encoding unitary transformation $\boldsymbol{U}$, information he uses to find the right decoding map.

We could describe the conclusion, more prosaically, by saying that the random unitary $\boldsymbol{U}$ applied to $AB$ encodes a good quantum error-correcting code, which achieves high-fidelity entanglement-assisted transmission of quantum information though an erasure channel with a high erasure probability. Of the $n$ input qubits, only $k'$ randomly selected qubits are received by Bob; the rest remain inside the black hole and hence are inaccessible. The input qubits, then, are erased with probability $p = (n - k')/n$, while nearly error-free qubits are recovered from the input qubits at a rate
$$
R = \frac{k}{n} = 1 - p - \frac{k' - k}{n};
$$ {#eq-10.371}
in the limit $n \to \infty$ with $c = k' - k$ fixed, this rate approaches $1 - p$, the entanglement-assisted quantum capacity of the erasure channel.

So far, we've assumed that the emitted system $A'$ is a randomly selected subsystem of $AB$. That won't be true for a real black hole. However, it is believed that the internal dynamics of actual black holes mixes quantum information quite rapidly (the *fast scrambling conjecture*). For a black hole with temperature $T$, it takes time of order $\hbar/kT$ for each qubit to be emitted in the Hawking radiation, and a time longer by only a factor of $\log n$ for the dynamics to mix the black hole degrees of freedom sufficiently for our decoupling estimate to hold with reasonable accuracy. For a solar mass black

<!-- Page 84 -->
hole, Alice's qubits are revealed just a few milliseconds after she deposits them, much faster than the $10^{67}$ years she had hoped for! Because Bob holds the system $R_B$ which purifies $B$, and because he knows the right decoding map to apply to $A' R_B$, the black hole behaves like an information mirror — Alice's qubits bounce right back!

If Alice is more careful, she will dump her qubits into a young black hole instead. If we assume that the initial black hole $B$ is in a pure state, then $\boldsymbol{\sigma}_{A B R_A}$ is also pure, and the Haar-averaged $L^1$ distance of $\boldsymbol{\sigma}_{B' R_A}$ from a product state is bounded above by
$$
\sqrt{\frac{|A B R_A|}{|A'|^2}} = \sqrt{\frac{2^{n+k}}{2^{2k'}}} = \frac{1}{2^c}
$$ {#eq-10.372}
after
$$
k' = \frac{1}{2}(n + k) + c
$$ {#eq-10.373}
qubits are emitted. In this case, Bob needs to wait a long time, until more than half of the qubits in $AB$ are radiated away. Once Bob has acquired $k + 2c$ more qubits than the number still residing in the black hole, he is empowered to decode Alice's $k$ qubits with fidelity $F \ge 1 - 2^{-c}$. In fact, there is nothing special about Alice's subsystem $A$; by adjusting his decoding map appropriately, Bob can decode any $k$ qubits he chooses from among the $n$ qubits in the initial black hole $AB$.

There is far more to learn about quantum information processing by black holes, an active topic of current research, but we will not delve further into this fascinating topic here. We can be confident, though, that the tools and concepts of quantum information theory discussed in this book will be helpful for addressing the many unresolved mysteries of quantum gravity, as well as many other open questions in the physical sciences.
