# Section 2.5: Ambiguity of the ensemble interpretation [PDF Pages 26-35]

<!-- ============================================================ -->
<!-- Source: chap2.pdf, Physical Pages: 26-35                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 26 -->
## 2.5 Ambiguity of the ensemble interpretation

### 2.5.1 Convexity

Recall that an operator $\boldsymbol{\rho}$ acting on a Hilbert space $\mathcal{H}$ can be interpreted as a density operator if it satisfies the three properties:

(1) $\boldsymbol{\rho}$ is self-adjoint.
(2) $\boldsymbol{\rho}$ is nonnegative.
(3) $\text{tr}(\boldsymbol{\rho}) = 1$.

<!-- Page 27 -->
It follows immediately that, given two density matrices $\boldsymbol{\rho}_1$ and $\boldsymbol{\rho}_2$, we can always construct another density matrix as a convex linear combination of the two:

$$
\boldsymbol{\rho}(\lambda) = \lambda \boldsymbol{\rho}_1 + (1-\lambda) \boldsymbol{\rho}_2
$$ {#eq-2.97}

is a density matrix for any real $\lambda$ satisfying $0 \le \lambda \le 1$. We easily see that $\boldsymbol{\rho}(\lambda)$ satisfies (1) and (3) if $\boldsymbol{\rho}_1$ and $\boldsymbol{\rho}_2$ do. To check (2), we evaluate

$$
\langle\psi|\boldsymbol{\rho}(\lambda)|\psi\rangle = \lambda \langle\psi|\boldsymbol{\rho}_1|\psi\rangle + (1-\lambda)\langle\psi|\boldsymbol{\rho}_2|\psi\rangle \ge 0;
$$ {#eq-2.98}

$\langle\boldsymbol{\rho}(\lambda)\rangle$ is guaranteed to be nonnegative because $\langle\boldsymbol{\rho}_1\rangle$ and $\langle\boldsymbol{\rho}_2\rangle$ are. We have, therefore, shown that in a Hilbert space $\mathcal{H}$ of dimension $d$, the density operators are a *convex subset* of the real vector space of $d \times d$ Hermitian operators. (A subset of a vector space is said to be convex if the set contains the straight line segment connecting any two points in the set.)

Most density operators can be expressed as a sum of other density operators in many different ways. But the pure states are special in this regard --- it is *not* possible to express a pure state as a convex sum of two other states. Consider a pure state $\boldsymbol{\rho} = |\psi\rangle\langle\psi|$, and let $|\psi_\perp\rangle$ denote a vector orthogonal to $|\psi\rangle$, $\langle\psi_\perp|\psi\rangle = 0$. Suppose that $\boldsymbol{\rho}$ can be expanded as in eq. (2.97); then

$$
\langle\psi_\perp|\boldsymbol{\rho}|\psi_\perp\rangle = 0 = \lambda \langle\psi_\perp|\boldsymbol{\rho}_1|\psi_\perp\rangle + (1-\lambda)\langle\psi_\perp|\boldsymbol{\rho}_2|\psi_\perp\rangle.
$$ {#eq-2.99}

Since the right hand side is a sum of two nonnegative terms, and the sum vanishes, both terms must vanish. If $\lambda$ is not 0 or 1, we conclude that $\boldsymbol{\rho}_1$ and $\boldsymbol{\rho}_2$ are orthogonal to $|\psi_\perp\rangle$. But since $|\psi_\perp\rangle$ can be *any* vector orthogonal to $|\psi\rangle$, we see that $\boldsymbol{\rho}_1 = \boldsymbol{\rho}_2 = \boldsymbol{\rho}$.

The vectors in a convex set that cannot be expressed as a linear combination of other vectors in the set are called the *extremal points* of the set. We have just shown that the pure states are extremal points of the set of density matrices. Furthermore, *only* the pure states are extremal, because any mixed state can be written $\boldsymbol{\rho} = \sum_i p_i |i\rangle\langle i|$ in the basis in which it is diagonal, and so is a convex sum of pure states.

We have already encountered this structure in our discussion of the special case of the Bloch sphere. We saw that the density operators are a (unit) ball in the three-dimensional set of $2 \times 2$ Hermitian matrices with unit trace. The ball is convex, and its extremal points are the points on the boundary. Similarly, the $d \times d$ density operators are a convex subset of the $(d^2 - 1)$-dimensional set of $d \times d$ Hermitian matrices with unit trace, and the extremal points of the set are the pure states.

<!-- Page 28 -->
However, the $2 \times 2$ case is atypical in one respect: for $d > 2$, the points on the boundary of the set of density matrices are not necessarily pure states. The boundary of the set consists of all density matrices with at least one vanishing eigenvalue (since there are nearby matrices with negative eigenvalues). Such a density matrix need not be pure, for $d > 2$, since the number of nonvanishing eigenvalues can exceed one.

### 2.5.2 Ensemble preparation

The convexity of the set of density matrices has a simple and enlightening physical interpretation. Suppose that a preparer agrees to prepare one of two possible states; with probability $\lambda$, the state $\boldsymbol{\rho}_1$ is prepared, and with probability $1-\lambda$, the state $\boldsymbol{\rho}_2$ is prepared. (A random number generator might be employed to guide this choice.) To evaluate the expectation value of any observable $\boldsymbol{M}$, we average over *both* the choices of preparation *and* the outcome of the quantum measurement:

$$
\begin{aligned}
\langle\boldsymbol{M}\rangle &= \lambda \langle\boldsymbol{M}\rangle_1 + (1-\lambda)\langle\boldsymbol{M}\rangle_2 \\
&= \lambda\,\text{tr}(\boldsymbol{M}\boldsymbol{\rho}_1) + (1-\lambda)\text{tr}(\boldsymbol{M}\boldsymbol{\rho}_2) \\
&= \text{tr}(\boldsymbol{M}\boldsymbol{\rho}(\lambda)).
\end{aligned}
$$ {#eq-2.100}

All expectation values are thus indistinguishable from what we would obtain if the state $\boldsymbol{\rho}(\lambda)$ had been prepared instead. Thus, we have an operational procedure, given methods for preparing the states $\boldsymbol{\rho}_1$ and $\boldsymbol{\rho}_2$, for preparing any convex combination.

Indeed, for any mixed state $\boldsymbol{\rho}$, there are an infinite variety of ways to express $\boldsymbol{\rho}$ as a convex combination of other states, and hence an infinite variety of procedures we could employ to prepare $\boldsymbol{\rho}$, all of which have exactly the same consequences for any conceivable observation of the system. But a pure state is different; it can be prepared in only one way. (This is what is "pure" about a pure state.) Every pure state is an eigenstate of some observable, e.g., for the state $\boldsymbol{\rho} = |\psi\rangle\langle\psi|$, measurement of the projection $\boldsymbol{E} = |\psi\rangle\langle\psi|$ is guaranteed to have the outcome 1. (For example, recall that every pure state of a single qubit is "spin-up" along some axis.) Since $\boldsymbol{\rho}$ is the only state for which the outcome of measuring $\boldsymbol{E}$ is 1 with 100% probability, there is no way to reproduce this observable property by choosing one of several possible preparations. Thus, the preparation of a pure state is unambiguous (we can infer a unique preparation if we have many copies of the state to experiment with), but the preparation of a mixed state is always ambiguous.

<!-- Page 29 -->
How ambiguous is it? Since any $\boldsymbol{\rho}$ can be expressed as a sum of pure states, let's confine our attention to the question: in how many ways can a density operator be expressed as a convex sum of pure states?

Mathematically, this is the question: in how many ways can $\boldsymbol{\rho}$ be written as a sum of extremal states?

As a first example, consider the "maximally mixed" state of a single qubit:

$$
\boldsymbol{\rho} = \frac{1}{2}\boldsymbol{I}.
$$ {#eq-2.101}

This can indeed be prepared as an ensemble of pure states in an infinite variety of ways. For example,

$$
\boldsymbol{\rho} = \frac{1}{2} |\uparrow_z\rangle\langle\uparrow_z| + \frac{1}{2} |\downarrow_z\rangle\langle\downarrow_z|,
$$ {#eq-2.102}

so we obtain $\boldsymbol{\rho}$ if we prepare either $|\uparrow_z\rangle$ or $|\downarrow_z\rangle$, each occurring with probability $1/2$. But we also have

$$
\boldsymbol{\rho} = \frac{1}{2} |\uparrow_x\rangle\langle\uparrow_x| + \frac{1}{2} |\downarrow_x\rangle\langle\downarrow_x|,
$$ {#eq-2.103}

so we obtain $\boldsymbol{\rho}$ if we prepare either $|\uparrow_x\rangle$ or $|\downarrow_x\rangle$, each occurring with probability $1/2$. Now the preparation procedures are undeniably different. Yet there is no possible way to tell the difference by making observations of the spin.

More generally, the point at the center of the Bloch ball is the sum of any two antipodal points on the sphere --- preparing either $|\uparrow_{\hat{n}}\rangle$ or $|\downarrow_{\hat{n}}\rangle$, each occurring with probability $1/2$, will generate $\boldsymbol{\rho} = \frac{1}{2}\boldsymbol{I}$.

Only in the case where $\boldsymbol{\rho}$ has two (or more) degenerate eigenvalues will there be distinct ways of generating $\boldsymbol{\rho}$ from an ensemble of mutually orthogonal pure states, but there is no good reason to confine our attention to ensembles of mutually orthogonal pure states. The point at the center of the Bloch ball can also be prepared as

$$
\boldsymbol{\rho}(\vec{P}) = \frac{1}{2}(\boldsymbol{I} + \vec{P} \cdot \vec{\boldsymbol{\sigma}})
$$ {#eq-2.104}

<!-- Page 30 -->
with $0 < |\vec{P}| < 1$. This can also be expressed as

$$
\boldsymbol{\rho}(\vec{P}) = \lambda \boldsymbol{\rho}(\hat{n}_1) + (1-\lambda) \boldsymbol{\rho}(\hat{n}_2)
$$ {#eq-2.105}

provided $\vec{P} = \lambda \hat{n}_1 + (1-\lambda)\hat{n}_2$ (in other words, if $\vec{P}$ lies on the line segment connecting the points $\hat{n}_1$ and $\hat{n}_2$ on the sphere). Evidently, for any $\vec{P}$, we can express $\boldsymbol{\rho}(\vec{P})$ as a convex sum of the pure states associated with any chord of the Bloch ball that passes through $\vec{P}$. All such chords constitute a two-parameter family.

The highly ambiguous nature of the preparation of a mixed quantum state is one of the characteristic features of quantum information, in sharp contrast to classical probability distributions. Consider, for example, the case of a probability distribution for a single classical bit. The two extremal distributions are those in which either 0 or 1 occurs with 100% probability. Any probability distribution for the bit is a convex sum of these two extremal points. Similarly, if there are $d$ possible states, there are $d$ extremal distributions, and any probability distribution has a unique decomposition into extremal ones (the convex set of probability distributions is a simplex, the convex hull of its $d$ vertices). If 0 occurs with 21% probability, 1 with 33% probability, and 2 with 46% probability, the "preparation" that gave rise to this distribution is completely unique.

### 2.5.3 Faster than light?

Let us return to the perspective that a mixed state of system $A$ arises because $A$ is entangled with system $B$, and use it to further explore the implications of the ambiguity of ensemble preparations. If qubit $A$ has the density matrix

$$
\boldsymbol{\rho}_A = \frac{1}{2} |\uparrow_z\rangle\langle\uparrow_z| + \frac{1}{2} |\downarrow_z\rangle\langle\downarrow_z|,
$$ {#eq-2.106}

this density matrix could arise from an entangled pure state of a bipartite system $|\psi\rangle_{AB}$ with the Schmidt decomposition

$$
|\psi\rangle_{AB} = \frac{1}{\sqrt{2}} (|\uparrow_z\rangle_A |\uparrow_z\rangle_B + |\downarrow_z\rangle_A |\downarrow_z\rangle_B).
$$ {#eq-2.107}

Therefore, the ensemble interpretation of $\boldsymbol{\rho}_A$ in which either $|\uparrow_z\rangle_A$ or $|\downarrow_z\rangle_A$ is prepared (each with probability $p=1/2$) can be realized by performing a measurement of qubit $B$. We measure qubit $B$ in the $\{|\uparrow_z\rangle_B, |\downarrow_z\rangle_B\}$ basis; if we get the result $|\uparrow_z\rangle_B$ we have prepared $|\uparrow_z\rangle_A$, and if we get the result $|\downarrow_z\rangle_B$ we have prepared $|\downarrow_z\rangle_A$.

However, as we have already seen, the Schmidt basis is not unique because $\boldsymbol{\rho}_A$ has degenerate eigenvalues. We can apply simultaneous unitary transformations to qubits $A$ and $B$ without modifying the bipartite pure state $|\psi\rangle_{AB}$. Thus, for any unit 3-vector $\hat{n}$, $|\psi\rangle_{AB}$ has a Schmidt decomposition of the form

$$
|\psi\rangle_{AB} = \frac{1}{\sqrt{2}} (|\uparrow_{\hat{n}}\rangle_A |\uparrow_{\hat{n}'}\rangle_B + |\downarrow_{\hat{n}}\rangle_A |\downarrow_{\hat{n}'}\rangle_B).
$$ {#eq-2.108}

We see that by measuring qubit $B$ in a suitable basis, we can realize any interpretation of $\boldsymbol{\rho}_A$ as an ensemble of two pure states.

<!-- Page 31 -->
This property seems to suggest a mechanism for faster-than-light communication. Many copies of $|\psi\rangle_{AB}$ are prepared. Alice takes all of the $A$ qubits to the Andromeda galaxy and Bob keeps all of the $B$ qubits on earth. When Bob wants to send a one-bit message to Alice, he chooses to measure either $\boldsymbol{\sigma}_1$ or $\boldsymbol{\sigma}_3$ for all his spins, thus preparing Alice's spins in either the $\{|\uparrow_z\rangle_A, |\downarrow_z\rangle_A\}$ or $\{|\uparrow_x\rangle_A, |\downarrow_x\rangle_A\}$ ensembles. (Since $V$ is real in this case, $V = V^*$ and $\hat{n} = \hat{n}'$.) To read the message, Alice immediately measures her spins to see which ensemble has been prepared.

This scheme has a flaw. Though the two preparation methods are surely different, both ensembles are described by precisely the same density matrix $\boldsymbol{\rho}_A = \frac{1}{2}\boldsymbol{I}$. There is no measurement that Alice can perform that distinguishes the two ensembles, and hence no way for Alice to know what Bob did. The "message" is indecipherable.

Bob's action changes the description of the state of $A$ from Alice's point of view, but Alice cannot detect this change unless Bob sends her classical information telling her what he did. Bob can choose to prepare Alice's spins in the $|\uparrow_z\rangle$ basis or the $|\uparrow_x\rangle$ basis, but Alice can't tell which choice Bob made until he phones her to tell her. When Alice receives Bob's phone call, she can sort her measurement records into subensembles, and then she will have a way to distinguish Bob's two preparation methods, but in this case there is certainly no faster-than-light communication, because Alice had to receive Bob's phone call before she could perform her test.

### 2.5.4 Quantum erasure

We had said that the density matrix $\boldsymbol{\rho}_A = \frac{1}{2}\boldsymbol{I}$ describes a spin in an incoherent mixture of the pure states $|\uparrow_z\rangle_A$ and $|\downarrow_z\rangle_A$. This was to be distinguished from coherent superpositions of these states, such as

$$
|\uparrow_x, \downarrow_x\rangle = \frac{1}{\sqrt{2}} (|\uparrow_z\rangle \pm |\downarrow_z\rangle);
$$ {#eq-2.109}

<!-- Page 32 -->
in the case of a coherent superposition, the relative phase of the two states has observable consequences (distinguishes $|\uparrow_x\rangle$ from $|\downarrow_x\rangle$). In the case of an incoherent mixture, the relative phase is completely unobservable. The superposition becomes incoherent if spin $A$ becomes entangled with another spin $B$, and spin $B$ is inaccessible.

Heuristically, the states $|\uparrow_z\rangle_A$ and $|\downarrow_z\rangle_A$ can interfere (the relative phase of these states can be observed) only if we have no information about whether the spin state is $|\uparrow_z\rangle_A$ or $|\downarrow_z\rangle_A$. More than that, interference can occur only if there is in principle no possible way to find out whether the spin is up or down along the $z$-axis. Entangling spin $A$ with spin $B$ destroys interference (causes spin $A$ to decohere) because it is possible in principle for us to determine if spin $A$ is up or down along $\hat{z}$ by performing a suitable measurement of spin $B$.

But we have now seen that the statement that entanglement causes decoherence requires a qualification. Suppose that Bob measures spin $B$ along the $\hat{x}$-axis, obtaining either the result $|\uparrow_x\rangle_B$ or $|\downarrow_x\rangle_B$, and that he sends his measurement result to Alice. Now Alice's spin is a pure state (either $|\uparrow_x\rangle_A$ or $|\downarrow_x\rangle_A$) and in fact a coherent superposition of $|\uparrow_z\rangle_A$ and $|\downarrow_z\rangle_A$. We have managed to recover the purity of Alice's spin before the jaws of decoherence could close!

Suppose that Bob allows his spin to pass through a Stern--Gerlach apparatus oriented along the $\hat{z}$-axis. Well, of course, Alice's spin can't behave like a coherent superposition of $|\uparrow_z\rangle_A$ and $|\downarrow_z\rangle_A$; all Bob has to do is look to see which way his spin moved, and he will know whether Alice's spin is up or down along $\hat{z}$. But suppose that Bob does not look. Instead, he carefully refocuses the two beams without maintaining any record of whether his spin moved up or down, and then allows the spin to pass through a second Stern--Gerlach apparatus oriented along the $\hat{x}$-axis. This time he looks, and communicates the result of his $\boldsymbol{\sigma}_1$ measurement to Alice. Now the coherence of Alice's spin has been restored!

This situation has been called a quantum eraser. Entangling the two spins creates a "measurement situation" in which the coherence of $|\uparrow_z\rangle_A$ and $|\downarrow_z\rangle_A$ is lost because we can find out if spin $A$ is up or down along $\hat{z}$ by observing spin $B$. But when we measure spin $B$ along $\hat{x}$, this information is "erased." Whether the result is $|\uparrow_x\rangle_B$ or $|\downarrow_x\rangle_B$ does not tell us anything about whether spin $A$ is up or down along $\hat{z}$, because Bob has been careful not to retain the "which way" information that he might have acquired by looking at the first Stern--Gerlach apparatus. Therefore, it is possible again for spin $A$ to behave like a coherent superposition of $|\uparrow_z\rangle_A$ and $|\downarrow_z\rangle_A$ (and it does, after Alice hears about Bob's result).

We can best understand the quantum eraser from the ensemble viewpoint. Alice has many spins selected from an ensemble described by $\boldsymbol{\rho}_A = \frac{1}{2}\boldsymbol{I}$, and there is no way for her to observe interference between $|\uparrow_z\rangle_A$ and $|\downarrow_z\rangle_A$. When Bob makes his measurement along $\hat{x}$, a particular preparation of the ensemble is realized. However, this has no effect that Alice can perceive --- her spin is still described by $\boldsymbol{\rho}_A = \frac{1}{2}\boldsymbol{I}$ as before. But, when Alice receives Bob's phone call, she can select a subensemble of her spins that are all in the pure state $|\uparrow_x\rangle_A$. The information that Bob sends allows Alice to distill purity from a maximally mixed state.

<!-- Page 33 -->
Another wrinkle on the quantum eraser is sometimes called *delayed choice*. This just means that the situation we have described is really completely symmetric between Alice and Bob, so it can't make any difference who measures first. (Indeed, if Alice's and Bob's measurements are spacelike separated events, there is no invariant meaning to which came first; it depends on the frame of reference of the observer.) Alice could measure all of her spins today (say along $\hat{x}$) before Bob has made his mind up how he will measure his spins. Next week, Bob can decide to "prepare" Alice's spins in the states $|\uparrow_{\hat{n}}\rangle_A$ and $|\downarrow_{\hat{n}}\rangle_A$ (that is the "delayed choice"). He then tells Alice which were the $|\uparrow_{\hat{n}}\rangle_A$ spins, and she can check her measurement record to verify that

$$
\langle\sigma_1\rangle_{\hat{n}} = \hat{n} \cdot \hat{x}.
$$ {#eq-2.110}

The results are the same, irrespective of whether Bob "prepares" the spins before or after Alice measures them.

We have claimed that the density matrix $\boldsymbol{\rho}_A$ provides a complete physical description of the state of subsystem $A$, because it characterizes all possible measurements that can be performed on $A$. One might object that the quantum eraser phenomenon demonstrates otherwise. Since the information received from Bob enables Alice to recover a pure state from the mixture, how can we hold that everything Alice can know about $A$ is encoded in $\boldsymbol{\rho}_A$?

I prefer to say that quantum erasure illustrates the principle that "information is physical." The state $\boldsymbol{\rho}_A$ of system $A$ is not the same thing as $\boldsymbol{\rho}_A$ accompanied by the information that Alice has received from Bob. This information (which attaches labels to the subensembles) changes the physical description. That is, we should include Alice's "state of knowledge" in our description of her system. An ensemble of spins for which Alice has no information about whether each spin is up or down is a *different* physical state than an ensemble in which Alice knows which spins are up and which are down. This "state of knowledge" need not really be the state of a human mind; any (inanimate) record that labels the subensemble will suffice.

<!-- Page 34 -->
### 2.5.5 The HJW theorem

So far, we have considered the quantum eraser only in the context of a single qubit, described by an ensemble of equally probable mutually orthogonal states, (i.e., $\boldsymbol{\rho}_A = \frac{1}{2}\boldsymbol{I}$). The discussion can be considerably generalized.

We have already seen that a mixed state of any quantum system can be realized as an ensemble of pure states in an infinite number of different ways. For a density matrix $\boldsymbol{\rho}_A$, consider one such realization:

$$
\boldsymbol{\rho}_A = \sum_i p_i |\phi_i\rangle\langle\phi_i|, \quad \sum_i p_i = 1.
$$ {#eq-2.111}

Here the states $\{|\phi_i\rangle_A\}$ are all normalized vectors, but we do not assume that they are mutually orthogonal. Nevertheless, $\boldsymbol{\rho}_A$ can be realized as an ensemble, in which each pure state $|\phi_i\rangle\langle\phi_i|$ occurs with probability $p_i$. For any such $\boldsymbol{\rho}_A$, we can construct a "purification" of $\boldsymbol{\rho}_A$, a bipartite pure state $|\Phi_1\rangle_{AB}$ that yields $\boldsymbol{\rho}_A$ when we perform a partial trace over $\mathcal{H}_B$. One such purification is of the form

$$
|\Phi_1\rangle_{AB} = \sum_i \sqrt{p_i} |\phi_i\rangle_A \otimes |\alpha_i\rangle_B,
$$ {#eq-2.112}

where the vectors $|\alpha_i\rangle_B \in \mathcal{H}_B$ are mutually orthogonal and normalized,

$$
\langle\alpha_i|\alpha_j\rangle = \delta_{ij}.
$$ {#eq-2.113}

Clearly, then,

$$
\text{tr}_B (|\Phi_1\rangle\langle\Phi_1|) = \boldsymbol{\rho}_A.
$$ {#eq-2.114}

Furthermore, we can imagine performing an orthogonal measurement in system $B$ that projects onto the $\{|\alpha_i\rangle_B\}$ basis. (The $|\alpha_i\rangle_B$'s might not span $\mathcal{H}_B$, but in the state $|\Phi_1\rangle_{AB}$, measurement outcomes orthogonal to all the $|\alpha_i\rangle_B$'s never occur.) The outcome $|\alpha_i\rangle_B$ will occur with probability $p_i$, and will prepare the pure state $|\phi_i\rangle\langle\phi_i|$ of system $A$. Thus, given the purification $|\Phi_1\rangle_{AB}$ of $\boldsymbol{\rho}_A$, there is a measurement we can perform in system $B$ that realizes the $|\phi_i\rangle_A$ ensemble interpretation of $\boldsymbol{\rho}_A$. When the measurement outcome in $B$ is known, we have successfully extracted one of the pure states $|\phi_i\rangle_A$ from the mixture $\boldsymbol{\rho}_A$.

What we have just described is a generalization of preparing $|\uparrow_z\rangle_A$ by measuring spin $B$ along $\hat{z}$ (in our discussion of two entangled qubits). But to generalize the notion of a quantum eraser, we wish to see that in the state $|\Phi_1\rangle_{AB}$, we can realize a different ensemble interpretation of $\boldsymbol{\rho}_A$ by performing a different measurement of $B$. So let

$$
\boldsymbol{\rho}_A = \sum_\mu q_\mu |\psi_\mu\rangle\langle\psi_\mu|,
$$ {#eq-2.115}

<!-- Page 35 -->
be another realization of the same density matrix $\boldsymbol{\rho}_A$ as an ensemble of pure states. For this ensemble as well, there is a corresponding purification

$$
|\Phi_2\rangle_{AB} = \sum_\mu \sqrt{q_\mu} |\psi_\mu\rangle_A \otimes |\beta_\mu\rangle_B,
$$ {#eq-2.116}

where again the $\{|\beta_\mu\rangle_B\}$'s are orthonormal vectors in $\mathcal{H}_B$. So in the state $|\Phi_2\rangle_{AB}$, we can realize the ensemble by performing a measurement in $\mathcal{H}_B$ that projects onto the $\{|\beta_\mu\rangle_B\}$ basis.

Now, how are $|\Phi_1\rangle_{AB}$ and $|\Phi_2\rangle_{AB}$ related? In fact, we can easily show that

$$
|\Phi_1\rangle_{AB} = (\boldsymbol{I}_A \otimes \boldsymbol{U}_B)|\Phi_2\rangle_{AB};
$$ {#eq-2.117}

the two states differ by a unitary change of basis acting in $\mathcal{H}_B$ alone, or

$$
|\Phi_1\rangle_{AB} = \sum_\mu \sqrt{q_\mu} |\psi_\mu\rangle_A \otimes |\gamma_\mu\rangle_B,
$$ {#eq-2.118}

where

$$
|\gamma_\mu\rangle_B = \boldsymbol{U}_B |\beta_\mu\rangle_B,
$$ {#eq-2.119}

is yet another orthonormal basis for $\mathcal{H}_B$. We see, then, that there is a single purification $|\Phi_1\rangle_{AB}$ of $\boldsymbol{\rho}_A$, such that we can realize either the $\{|\phi_i\rangle_A\}$ ensemble or $\{|\psi_\mu\rangle_A\}$ ensemble by choosing to measure the appropriate observable in system $B$!

Similarly, we may consider many ensembles that all realize $\boldsymbol{\rho}_A$, where the maximum number of pure states appearing in any of the ensembles is $d$. Then we may choose a Hilbert space $\mathcal{H}_B$ of dimension $d$, and a pure state $|\Phi\rangle_{AB} \in \mathcal{H}_A \otimes \mathcal{H}_B$, such that any one of the ensembles can be realized by measuring a suitable observable of $B$. This is the HJW theorem (for Hughston, Jozsa, and Wootters); it expresses the quantum eraser phenomenon in its most general form.

In fact, the HJW theorem is an easy corollary to the Schmidt decomposition. Both $|\Phi_1\rangle_{AB}$ and $|\Phi_2\rangle_{AB}$ have Schmidt decompositions, and because both yield the same $\boldsymbol{\rho}_A$ when we take the partial trace over $B$, these decompositions must have the form

$$
\begin{aligned}
|\Phi_1\rangle_{AB} &= \sum_k \sqrt{\lambda_k} |k\rangle_A \otimes |k'_1\rangle_B, \\
|\Phi_2\rangle_{AB} &= \sum_k \sqrt{\lambda_k} |k\rangle_A \otimes |k'_2\rangle_B,
\end{aligned}
$$ {#eq-2.120}

where the $\lambda_k$'s are the eigenvalues of $\boldsymbol{\rho}_A$ and the $|k\rangle_A$'s are the corresponding eigenvectors. But since $\{|k'_1\rangle_B\}$ and $\{|k'_2\rangle_B\}$ are both orthonormal bases for $\mathcal{H}_B$, there is a unitary $\boldsymbol{U}_B$ such that

$$
|k'_1\rangle_B = \boldsymbol{U}_B |k'_2\rangle_B,
$$ {#eq-2.121}

from which eq. (2.117) immediately follows.
