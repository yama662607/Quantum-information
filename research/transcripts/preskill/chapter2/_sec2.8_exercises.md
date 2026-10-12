# 2.8 Exercises [📄 chap2.pdf](/assets/pdf/preskill/chap2.pdf#page=43)

## 2.1 Fidelity of measurement

a) For two states $|\psi_1\rangle$ and $|\psi_2\rangle$ in an $N$-dimensional Hilbert space, define the relative angle $\theta$ between the states by
$$
|\langle\psi_2|\psi_1\rangle| \equiv \cos\theta, \tag{2.164}
$$
where $0 \le \theta \le \pi/2$. Suppose that the two states are selected at random. Find the probability distribution $p(\theta)d\theta$ for the relative angle. Hint: We can choose a basis such that
$$
\begin{aligned}
|\psi_1\rangle &= (1, \vec{0}) \tag{2.165} \\
|\psi_2\rangle &= (e^{i\phi}\cos\theta, \psi_2^\perp). \tag{2.166}
\end{aligned}
$$
"Selected at random" means that the probability distribution for the normalized vector $|\psi_2\rangle$ is uniform on the (real) $(2N-1)$-sphere (this is the unique distribution that is invariant under arbitrary unitary transformations). Note that, for fixed $\theta$, $e^{i\phi}$ parametrizes a circle of radius $\cos\theta$, and $|\psi_2^\perp\rangle$ is a vector that lies on a $(2N-3)$-sphere of radius $\sin\theta$.

b) A density operator $\boldsymbol{\rho}$ is said to approximate a pure state $|\psi\rangle$ with fidelity
$$
F = \langle\psi|\boldsymbol{\rho}|\psi\rangle. \tag{2.167}
$$
Imagine that a state $|\psi_1\rangle$ in an $N$-dimensional Hilbert space is selected at random, and we guess at random that the state is $|\psi_2\rangle$. On the average, what will be the fidelity of our guess?

c) When we measure, we collect information and cause a disturbance -- an unknown state is replaced by a different state that is known. Suppose that the state $|\psi\rangle$ is selected at random, and then an orthogonal measurement is performed, projecting onto an orthonormal basis $\{|\boldsymbol{E}_a\rangle\}$. After the measurement, the state (averaged over all possible outcomes) is described by the density matrix
$$
\boldsymbol{\rho} = \sum_a \boldsymbol{E}_a |\psi\rangle\langle\psi| \boldsymbol{E}_a, \tag{2.168}
$$
where $\boldsymbol{E}_a = |\boldsymbol{E}_a\rangle\langle\boldsymbol{E}_a|$; this $\boldsymbol{\rho}$ approximates $|\psi\rangle$ with fidelity
$$
F = \sum_a (\langle\psi|\boldsymbol{E}_a|\psi\rangle)^2. \tag{2.169}
$$
Evaluate $F$, averaged over the choice of $|\psi\rangle$. Hint: Use Bayes's rule and the result from (a) to find the probability distribution for the angle $\theta$ between the state $|\psi\rangle$ and the projected state $\boldsymbol{E}_a|\psi\rangle / \|\boldsymbol{E}_a|\psi\rangle\|$. Then evaluate $\langle\cos^2\theta\rangle$ in this distribution.

Remark: The improvement in $F$ in the answer to (c) compared to the answer to (b) is a crude measure of how much we learned by making the measurement.

## 2.2 Measurement without disturbance?

Charlie prepares the system $A$ in one of two nonorthogonal states, $|\phi\rangle_A$ or $|\tilde{\phi}\rangle_A$, and he challenges Alice to collect some information about which state he prepared without in any way disturbing the state. Alice has an idea about how to meet the challenge.

Alice intends to prepare a second "ancillary" system $B$ in the state $|\beta\rangle_B$, and then apply to the composite system $AB$ a unitary transformation $\boldsymbol{U}$ that acts according to
$$
\begin{aligned}
\boldsymbol{U} : |\phi\rangle_A \otimes |\beta\rangle_B &\to |\phi\rangle_A \otimes |\beta'\rangle_B \\
|\tilde{\phi}\rangle_A \otimes |\beta\rangle_B &\to |\tilde{\phi}\rangle_A \otimes |\tilde{\beta}'\rangle_B, \tag{2.170}
\end{aligned}
$$
which does indeed leave the state of system $A$ undisturbed. Then she plans to perform a measurement on system $B$ that is designed to distinguish the states $|\beta'\rangle_B$ and $|\tilde{\beta}'\rangle_B$.

a) What do you think of Alice's idea? Hint: What does the unitarity of $\boldsymbol{U}$ tell you about how the states $|\beta'\rangle_B$ and $|\tilde{\beta}'\rangle_B$ are related to one another?

b) Would you feel differently if the states $|\phi\rangle_A$ and $|\tilde{\phi}\rangle_A$ were orthogonal?

## 2.3 Quantum bit commitment

The Yankees are playing the Dodgers in the World Series. Alice is sure that she knows who will win. Alice doesn't like Bob, so she doesn't want to tell him who the winner will be. But after the Series is over, Alice wants to be able to convince Bob that she knew the outcome all along. What to do?

Bob suggests that Alice write down her choice (0 if the Yankees will win, 1 if the Dodgers will win) on a piece of paper, and lock the paper in a box. She is to give the box to Bob, but she will keep the key for herself. Then, when she is ready to reveal her choice, she will send the key to Bob, allowing him to open the box and read the paper.

Alice rejects this proposal. She doesn't trust Bob, and she knows that he is a notorious safe cracker. Who's to say whether he will be able to open the box and sneak a look, even if he doesn't have the key?

Instead, Alice proposes to certify her honesty in another way, using quantum information. To commit to a value $a \in \{0, 1\}$ of her bit, she prepares one of two distinguishable density operators ($\boldsymbol{\rho}_0$ or $\boldsymbol{\rho}_1$) of the bipartite system $AB$, sends system $B$ to Bob, and keeps system $A$ for herself. Later, to unveil her bit, Alice sends system $A$ to Bob, and he performs a measurement to determine whether the state of $AB$ is $\boldsymbol{\rho}_0$ or $\boldsymbol{\rho}_1$. This protocol is called quantum bit commitment.

We say that the protocol is binding if, after commitment, Alice is unable to change the value of her bit. We say that the protocol is concealing if, after commitment and before unveiling, Bob is unable to discern the value of the bit. The protocol is secure if it is both binding and concealing.

Show that if a quantum bit commitment protocol is concealing, then it is not binding. Thus quantum bit commitment is insecure.

Hint: First argue that without loss of generality, we may assume that the states $\boldsymbol{\rho}_0$ and $\boldsymbol{\rho}_1$ are both pure. Then apply the HJW Theorem.

Remark: Note that the conclusion that quantum bit commitment is insecure still applies even if the shared bipartite state ($\boldsymbol{\rho}_0$ or $\boldsymbol{\rho}_1$) is prepared during many rounds of quantum communication between Alice and Bob, where in each round one party performs a quantum operation on his/her local system and on a shared message system, and then sends the message system to the other party.

## 2.4 Completeness of subsystem correlations

Consider a bipartite system $AB$. Suppose that many copies of the (not necessarily pure) state $\boldsymbol{\rho}_{AB}$ have been prepared. An observer Alice with access only to subsystem $A$ can measure the expectation value of any observable of the form $\boldsymbol{M}_A \otimes \boldsymbol{I}_B$, while an observer Bob with access only to subsystem $B$ can measure the expectation value of any observable of the form $\boldsymbol{I}_A \otimes \boldsymbol{N}_B$. Neither of these observers, working alone, can expect to gain enough information to determine the joint state $\boldsymbol{\rho}_{AB}$.

But now suppose that Alice and Bob can communicate, exchanging (classical) information about how their measurement outcomes are correlated. Thereby, they can jointly determine the expectation value of any observable of the form $\boldsymbol{M}_A \otimes \boldsymbol{N}_B$ (an observable whose eigenstates are separable direct products states of the form $|\phi\rangle_A \otimes |\chi\rangle_B$).

The point of this exercise is to show that if Alice and Bob have complete knowledge of the nature of the correlations between subsystems $A$ and $B$ (know the expectation values of any tensor product observable $\boldsymbol{M}_A \otimes \boldsymbol{N}_B$), then in fact they know everything about the bipartite state $\boldsymbol{\rho}_{AB}$ -- there will be no surprises when they measure entangled observables, those whose eigenstates are entangled states.

a) Let $\{\boldsymbol{M}_a, a = 1, 2, \dots, d^2\}$ denote a set of $d^2$ linearly independent self-adjoint operators acting on a Hilbert space $\mathcal{H}$ of dimension $d$. Show that if $\boldsymbol{\rho}$ is a density operator acting on $\mathcal{H}$, and $\mathrm{tr}(\boldsymbol{\rho}\boldsymbol{M}_a)$ is known for each $a$, then $\langle\phi|\boldsymbol{\rho}|\phi\rangle$ is known for any vector $|\phi\rangle$ in $\mathcal{H}$.

b) Show that if $\langle\phi|\boldsymbol{\rho}|\phi\rangle$ is known for each vector $|\phi\rangle$, then $\boldsymbol{\rho}$ is completely known.

c) Show that if $\{\boldsymbol{M}_a\}$ denotes a basis for self-adjoint operators on $\mathcal{H}_A$, and $\{\boldsymbol{N}_b\}$ denotes a basis for self-adjoint operators on $\mathcal{H}_B$, then $\{\boldsymbol{M}_a \otimes \boldsymbol{N}_b\}$ is a basis for the self-adjoint operators on $\mathcal{H}_A \otimes \mathcal{H}_B$.

Remark: It follows from (c) alone that the correlations of the "local" observables determine the expectation values of all the observables. Parts (a) and (b) serve to establish that $\boldsymbol{\rho}$ is completely determined by the expectation values of a complete set of observables.

d) State and prove the result corresponding to (c) that applies to a $n$-part system with Hilbert space $\mathcal{H}_1 \otimes \mathcal{H}_2 \otimes \dots \otimes \mathcal{H}_n$.

e) Discuss how the world would be different if quantum states resided in a real Hilbert space rather than a complex Hilbert space. Consider, in particular, whether (c) is true for symmetric operators acting on a real vector space.

## 2.5 Optimal measurement distinguishing two quantum states

Consider two quantum states described by density operators $\boldsymbol{\rho}$ and $\boldsymbol{\sigma}$ in an $d$-dimensional Hilbert space, and consider the complete orthogonal measurement $\{\boldsymbol{E}_a, a = 0, 1, 2, \dots, d-1\}$, where the $\boldsymbol{E}_a$'s are one-dimensional projectors satisfying
$$
\sum_{a=0}^{d-1} \boldsymbol{E}_a = \boldsymbol{I}. \tag{2.171}
$$
When the measurement is performed, outcome $a$ occurs with probability $p_a = \mathrm{tr}(\boldsymbol{\rho}\boldsymbol{E}_a)$ if the state is $\boldsymbol{\rho}$ and with probability $q_a = \mathrm{tr}(\boldsymbol{\sigma}\boldsymbol{E}_a)$ if the state is $\boldsymbol{\sigma}$.

The $L^1$ distance between the two probability distributions is defined as
$$
d(p, q) \equiv \|p - q\|_1 \equiv \sum_{a=0}^{d-1} |p_a - q_a|; \tag{2.172}
$$
this distance is zero if the two distributions are identical, and attains its maximum value two if the two distributions have support on disjoint sets.

a) Show that
$$
d(p, q) \le \sum_{i=0}^{d-1} |\lambda_i| = \|\boldsymbol{\rho} - \boldsymbol{\sigma}\|_1 \equiv d(\boldsymbol{\rho}, \boldsymbol{\sigma}), \tag{2.173}
$$
where the $\lambda_i$'s are the eigenvalues of the Hermitian operator $\boldsymbol{\rho} - \boldsymbol{\sigma}$. Hint: Working in the basis in which $\boldsymbol{\rho} - \boldsymbol{\sigma}$ is diagonal, find an expression for $|p_a - q_a|$, and then find an upper bound on $|p_a - q_a|$. Finally, use the completeness property eq.(2.171) to bound $d(p, q)$.

b) Find a choice for the orthogonal projector $\{\boldsymbol{E}_a\}$ that saturates the upper bound eq.(2.173).

c) If the states $\boldsymbol{\rho} = |\psi\rangle\langle\psi|$ and $\boldsymbol{\sigma} = |\phi\rangle\langle\phi|$ are pure, show that
$$
d(p, q) \le 2 \| |\psi\rangle - |\phi\rangle \| \tag{2.174}
$$
where $\|\cdot\|$ denotes the Hilbert space norm.

## 2.6 What probability distributions are consistent with a mixed state?

A density operator $\boldsymbol{\rho}$, expressed in the orthonormal basis $\{|\alpha_i\rangle\}$ that diagonalizes it, is
$$
\boldsymbol{\rho} = \sum_i p_i |\alpha_i\rangle\langle\alpha_i|. \tag{2.175}
$$
We would like to realize this density operator as an ensemble of pure states $\{|\phi_\mu\rangle\}$, where $|\phi_\mu\rangle$ is prepared with a specified probability $q_\mu$. This preparation is possible if the $|\phi_\mu\rangle$'s can be chosen so that
$$
\boldsymbol{\rho} = \sum_\mu q_\mu |\phi_\mu\rangle\langle\phi_\mu|. \tag{2.176}
$$
We say that a probability vector $q$ (a vector whose components are nonnegative real numbers that sum to 1) is majorized by a probability vector $p$ (denoted $q \prec p$), if there exists a doubly stochastic matrix $D$ such that
$$
q_\mu = \sum_i D_{\mu i} p_i. \tag{2.177}
$$
A matrix is doubly stochastic if its entries are nonnegative real numbers such that $\sum_\mu D_{\mu i} = \sum_i D_{\mu i} = 1$. That the columns sum to one assures that $D$ maps probability vectors to probability vectors (i.e., is stochastic). That the rows sum to one assures that $D$ maps the uniform distribution to itself. Applied repeatedly, $D$ takes any input distribution closer and closer to the uniform distribution (unless $D$ is a permutation, with one nonzero entry in each row and column). Thus we can view majorization as a partial order on probability vectors such that $q \prec p$ means that $q$ is more nearly uniform than $p$ (or equally close to uniform, in the case where $D$ is a permutation).

Show that normalized pure states $\{|\phi_\mu\rangle\}$ exist such that eq.(2.176) is satisfied if and only if $q \prec p$, where $p$ is the vector of eigenvalues of $\boldsymbol{\rho}$.

Hint: Recall that, according to the HJW Theorem, if eq.(2.175) and eq.(2.176) are both satisfied then there is a unitary matrix $V_{\mu i}$ such that
$$
\sqrt{q_\mu} |\phi_\mu\rangle = \sum_i \sqrt{p_i} V_{\mu i} |\alpha_i\rangle. \tag{2.178}
$$
You may also use (but need not prove) Horn's Lemma: if $q \prec p$, then there exists a unitary (in fact, orthogonal) matrix $U_{\mu i}$ such that $q = Dp$ and $D_{\mu i} = |U_{\mu i}|^2$.

## 2.7 Alice does Bob a favor

Alice, in Anaheim, and Bob, in Boston, share a bipartite pure state $|\Psi\rangle$, which can be expressed in the Schmidt form
$$
|\Psi\rangle = \sum_i \sqrt{p_i} |\alpha_i\rangle \otimes |\beta_i\rangle, \tag{2.179}
$$
where $\{|\alpha_i\rangle\}$ is an orthonormal basis for Alice's system $A$, $\{|\beta_i\rangle\}$ is an orthonormal basis for Bob's system $B$, and the $\{p_i\}$ are nonnegative real numbers summing to 1. Bob is supposed to perform a complete orthogonal local measurement on $B$, characterized by the set of projectors $\{\boldsymbol{E}_a^B\}$ -- if the measurement outcome is $a$, then Bob's measurement prepares the state
$$
|\Psi\rangle \mapsto |\Psi_a\rangle = \frac{(\boldsymbol{I} \otimes \boldsymbol{E}_a^B)|\Psi\rangle}{\langle\Psi|(\boldsymbol{I} \otimes \boldsymbol{E}_a^B)|\Psi\rangle^{1/2}}. \tag{2.180}
$$
$|\Psi_a\rangle$ can also be expressed in the Schmidt form if we choose appropriate orthonormal bases for $A$ and $B$ that depend on the measurement outcome. The new Schmidt basis elements can be written as
$$
|\alpha'_{a,i}\rangle = \boldsymbol{U}_a^A |\alpha_i\rangle, \quad |\beta'_{a,i}\rangle = \boldsymbol{U}_a^B |\beta_i\rangle, \tag{2.181}
$$
where $\boldsymbol{U}_a^A, \boldsymbol{U}_a^B$ are unitary.

Unfortunately, Bob's measurement apparatus is broken, though he still has the ability to perform local unitary transformations on $B$. Show that Alice can help Bob out by performing a measurement that is "locally equivalent" to Bob's. That is, there are orthogonal projectors $\{\boldsymbol{E}_a^A\}$ and unitary transformations $\boldsymbol{V}_a^A, \boldsymbol{V}_a^B$ such that
$$
|\Psi_a\rangle = \boldsymbol{V}_a^A \otimes \boldsymbol{V}_a^B \left( \frac{(\boldsymbol{E}_a^A \otimes \boldsymbol{I})|\Psi\rangle}{\langle\Psi|(\boldsymbol{E}_a^A \otimes \boldsymbol{I})|\Psi\rangle^{1/2}} \right) \tag{2.182}
$$
for each $a$, and furthermore, both Alice's measurement and Bob's yield outcome $a$ with the same probability. This means that instead of Bob doing the measurement, the same effect can be achieved if Alice measures instead, tells Bob the outcome, and both Alice and Bob perform the appropriate unitary transformations. Construct $\boldsymbol{E}_a^A$ (this is most conveniently done by expressing both $\boldsymbol{E}_a^A$ and $\boldsymbol{E}_a^B$ in the Schmidt bases for $|\Psi\rangle$) and express $\boldsymbol{V}_a^A$ and $\boldsymbol{V}_a^B$ in terms of $\boldsymbol{U}_a^A$ and $\boldsymbol{U}_a^B$.

Remark: This result shows that for any protocol involving local operations and "two-way" classical communication (2-LOCC) that transforms an initial bipartite pure state to a final bipartite pure state, the same transformation can be achieved by a "one-way" (1-LOCC) protocol in which all classical communication is from Alice to Bob (the Lo-Popescu Theorem). In a two-way LOCC protocol, Alice and Bob take turns manipulating the state for some finite (but arbitrarily large) number of rounds. In each round, one party or the other performs a measurement on her/his local system and broadcasts the outcome to the other party. Either party might use a local "ancilla" system in performing the measurement, but we may include all ancillas used during the protocol in the bipartite pure state $|\Psi\rangle$. Though a party might discard information about the measurement outcome, or fail to broadcast the information to the other party, we are entitled to imagine that the complete information about the outcomes is known to both parties at each step (incomplete information is just equivalent to the special case in which the parties choose not to use all the information). Thus the state is pure after each step.

The solution to the exercise shows that a round of a 2-LOCC protocol in which Bob measures can be simulated by an operation performed by Alice and a local unitary applied by Bob. Thus, we can allow Alice to perform all the measurements herself. When she is through she sends all the outcomes to Bob, and he can apply the necessary product of unitary transformations to complete the protocol.

## 2.8 The power of noncontextuality

We may regard a quantum state as an assignment of probabilities to projection operators. That is, according to Born's rule, if $\boldsymbol{\rho}$ is a density operator and $\boldsymbol{E}$ is a projector, then $p(\boldsymbol{E}) = \mathrm{tr}(\boldsymbol{\rho}\boldsymbol{E})$ is the probability that the outcome $\boldsymbol{E}$ occurs, if $\boldsymbol{E}$ is one of a complete set of orthogonal projectors associated with a particular quantum measurement. A notable feature of this rule is that the assignment of a probability $p(\boldsymbol{E})$ to $\boldsymbol{E}$ is noncontextual. This means that, while the probability $p(\boldsymbol{E})$ depends on the state $\boldsymbol{\rho}$, it does not depend on how we choose the rest of the projectors that complete the orthogonal set containing $\boldsymbol{E}$.

In a hidden variable theory, the probabilistic description of quantum measurement is derived from a more fundamental and complete deterministic description. The outcome of a measurement could be perfectly predicted if the values of the hidden variables were precisely known -- then the probability $p(\boldsymbol{E})$ could take only the values 0 and 1. The standard probabilistic predictions of quantum theory arise when we average over the unknown values of the hidden variables. The purpose of this exercise is to show that such deterministic assignments conflict with noncontextuality. Thus a hidden variable theory, if it is to agree with the predictions of quantum theory after averaging, must be contextual.

Let $\{\boldsymbol{I}, \boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z}\}$ denote the single-qubit observables
$$
\begin{aligned}
\boldsymbol{I} &= \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad \boldsymbol{X} = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \\
\boldsymbol{Y} &= \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \boldsymbol{Z} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
\end{aligned} \tag{2.183}
$$
and consider the nine two-qubit observables:
$$
\begin{pmatrix}
\boldsymbol{X} \otimes \boldsymbol{I} & \boldsymbol{I} \otimes \boldsymbol{X} & \boldsymbol{X} \otimes \boldsymbol{X} \\
\boldsymbol{I} \otimes \boldsymbol{Y} & \boldsymbol{Y} \otimes \boldsymbol{I} & \boldsymbol{Y} \otimes \boldsymbol{Y} \\
\boldsymbol{X} \otimes \boldsymbol{Y} & \boldsymbol{Y} \otimes \boldsymbol{X} & \boldsymbol{Z} \otimes \boldsymbol{Z}
\end{pmatrix}. \tag{2.184}
$$
The three observables in each row and in each column are mutually commuting, and so can be simultaneously diagonalized. In fact the simultaneous eigenstates of any two operators in a row or column (the third operator is not independent of the other two) are a complete basis for the four-dimensional Hilbert space of the two qubits. Thus we can regard the array eq.(2.184) as a way of presenting six different ways to choose a complete set of one-dimensional projectors for two qubits.

Each of these observables has eigenvalues $\pm 1$, so that in a deterministic and noncontextual model of measurement (for a fixed value of the hidden variables), each can be assigned a definite value, either $+1$ or $-1$.

a) Any noncontextual deterministic assignment has to be consistent with the multiplicative structure of the observables. For example, the product of the three observables in the top row is the identity $\boldsymbol{I} \otimes \boldsymbol{I}$. Therefore, if we assign a value $\pm 1$ to each operator, the number of $-1$'s assigned to the first row must be even. Compute the product of the three observables in each row and each column to find the corresponding constraints.

b) Show that there is no way to satisfy all six constraints simultaneously.

Thus a deterministic and noncontextual assignment does not exist.

## 2.9 Schmidt-decomposable states

We have seen that any vector in a bipartite Hilbert space $\mathcal{H}_{AB} = \mathcal{H}_A \otimes \mathcal{H}_B$ can be expressed in the Schmidt form: Given the vector $|\psi\rangle_{AB} \in \mathcal{H}_A \otimes \mathcal{H}_B$, where $\mathcal{H}_A$ and $\mathcal{H}_B$ are both $d$-dimensional, we can choose orthonormal bases $\{|i\rangle_A\}$ for $\mathcal{H}_A$ and $\{|i\rangle_B\}$ for $\mathcal{H}_B$ so that
$$
|\psi\rangle_{AB} = \sum_{i=0}^{d-1} \sqrt{\lambda_i} |i\rangle_A \otimes |i\rangle_B, \tag{2.185}
$$
where the $\lambda_i$'s are real and nonnegative. (We're not assuming here that the vector has unit norm, so the sum of the $\lambda_i$'s is not constrained.) Eq.(2.185) is called the Schmidt decomposition of the vector $|\psi\rangle_{AB}$. Of course, the bases in which the vector has the Schmidt form depend on which vector $|\psi\rangle_{AB}$ is being decomposed.

A unitary transformation acting on $\mathcal{H}_{AB}$ is called a local unitary if it is a tensor product $\boldsymbol{U}_A \otimes \boldsymbol{U}_B$, where $\boldsymbol{U}_A, \boldsymbol{U}_B$ are unitary transformations acting on $\mathcal{H}_A, \mathcal{H}_B$ respectively. The word "local" is used because if the two parts $A$ and $B$ of the system are widely separated from one another, so that Alice can access only part $A$ and Bob can access only part $B$, then Alice and Bob can apply this transformation by each acting locally on her or his part.

a) Now suppose that Alice and Bob choose standard fixed bases $\{|i\rangle_A\}$ and $\{|i\rangle_B\}$ for their respective Hilbert spaces, and are presented with a vector $|\psi\rangle_{AB}$ that is not necessarily in the Schmidt form when expressed in the standard bases. Show that there is a local unitary $\boldsymbol{U}_A \otimes \boldsymbol{U}_B$ that Alice and Bob can apply so that the resulting vector
$$
|\psi'\rangle_{AB} = \boldsymbol{U}_A \otimes \boldsymbol{U}_B |\psi\rangle_{AB} \tag{2.186}
$$
does have the form eq.(2.185) when expressed in the standard bases.

b) Let's verify that the result of (a) makes sense from the point of view of parameter counting. For a generic vector in the Schmidt form, all $\lambda_i$'s are nonvanishing and no two $\lambda_i$'s are equal. Consider the orbit that is generated by letting arbitrary local unitaries act on one fixed generic vector in the Schmidt form. What is the dimension of the orbit, that is, how many real parameters are needed to specify one particular vector on the orbit? (Hint: To do the counting, consider the local unitaries that differ infinitesimally from the identity $\boldsymbol{I}_A \otimes \boldsymbol{I}_B$. Choose a basis for these, and count the number of independent linear combinations of the basis elements that annihilate the Schmidt-decomposed vector.) Compare the dimension of the orbit to the (real) dimension of $\mathcal{H}_{AB}$, and check the consistency with the number of free parameters in eq.(2.185).

A vector $|\psi\rangle_{A_1 \dots A_r}$ in a Hilbert space $\mathcal{H}_{A_1} \otimes \dots \otimes \mathcal{H}_{A_r}$ with $r$ parts is said to be Schmidt decomposable if it is possible to choose orthonormal bases for $\mathcal{H}_{A_1}, \dots, \mathcal{H}_{A_r}$ such that vector can be expressed as
$$
|\psi\rangle_{A_1 \dots A_r} = \sum_i \sqrt{\lambda_i} |i\rangle_{A_1} \otimes |i\rangle_{A_2} \otimes \dots \otimes |i\rangle_{A_r}. \tag{2.187}
$$
Though every vector in a bipartite Hilbert space is Schmidt decomposable, this isn't true for vectors in Hilbert spaces with three or more parts.

c) Consider a generic Schmidt-decomposable vector in the tripartite Hilbert space of three qubits. Find the dimension of the orbit generated by local unitaries acting on this vector.

d) By considering the number of free parameters in the Schmidt form eq.(2.187), and the result of (c), find the (real) dimension of the space of Schmidt-decomposable vectors for three qubits. What is the real codimension of this space in the three-qubit Hilbert space $\mathbb{C}^8$?
