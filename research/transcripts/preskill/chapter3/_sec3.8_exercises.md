# Section 3.8 Transcript: Exercises

**Source**: `quarto/assets/pdf/preskill/chap3.pdf` (Pages 49–65)  
**Status**: Complete, faithful transcript including all mathematical expressions and formatting.

---

## 3.8 Exercises (p. 49)

### 3.1 Which state did Alice make? (p. 49)

Consider a game in which Alice prepares one of two possible states: either $\boldsymbol{\rho}_1$ with *a priori* probability $p_1$, or $\boldsymbol{\rho}_2$ with *a priori* probability $p_2 = 1 - p_1$. Bob is to perform a measurement and on the basis of the outcome to guess which state Alice prepared. If Bob’s guess is right, he wins; if he guesses wrong, Alice wins.

In this exercise you will find Bob’s best strategy, and determine his optimal probability of error.

Let’s suppose (for now) that Bob performs a POVM with two possible outcomes, corresponding to the two nonnegative Hermitian operators $\boldsymbol{E}_1$ and $\boldsymbol{E}_2 = \boldsymbol{I} - \boldsymbol{E}_1$. If Bob’s outcome is $\boldsymbol{E}_1$, he guesses that Alice’s state was $\boldsymbol{\rho}_1$, and if it is $\boldsymbol{E}_2$, he guesses $\boldsymbol{\rho}_2$. Then the probability that Bob guesses wrong is
$$
p_{\text{error}} = p_1 \text{tr}(\boldsymbol{\rho}_1 \boldsymbol{E}_2) + p_2 \text{tr}(\boldsymbol{\rho}_2 \boldsymbol{E}_1)~.
\tag{3.187}
$$

a) Show that
$$
p_{\text{error}} = p_1 + \sum_i \lambda_i \langle i | \boldsymbol{E}_1 | i \rangle~,
\tag{3.188}
$$
where $\{|i\rangle\}$ denotes the orthonormal basis of eigenstates of the Hermitian operator $p_2 \boldsymbol{\rho}_2 - p_1 \boldsymbol{\rho}_1$, and the $\lambda_i$’s are the corresponding eigenvalues.

b) Bob’s best strategy is to perform the two-outcome POVM that minimizes this error probability. Find the nonnegative operator $\boldsymbol{E}_1$ that minimizes $p_{\text{error}}$, and show that error probability when Bob performs this optimal two-outcome POVM is
$$
(p_{\text{error}})_{\text{optimal}} = p_1 + \sum_{\text{neg}} \lambda_i~,
\tag{3.189}
$$
where $\sum_{\text{neg}}$ denotes the sum over all of the negative eigenvalues of $p_2 \boldsymbol{\rho}_2 - p_1 \boldsymbol{\rho}_1$.

c) It is convenient to express this optimal error probability in terms of the $L^1$ norm of the operator $p_2 \boldsymbol{\rho}_2 - p_1 \boldsymbol{\rho}_1$,
$$
\| p_2 \boldsymbol{\rho}_2 - p_1 \boldsymbol{\rho}_1 \|_1 = \text{tr}|p_2 \boldsymbol{\rho}_2 - p_1 \boldsymbol{\rho}_1| = \sum_{\text{pos}} \lambda_i - \sum_{\text{neg}} \lambda_i~,
\tag{3.190}
$$
the difference between the sum of positive eigenvalues and the sum of negative eigenvalues. Use the property $\text{tr}(p_2 \boldsymbol{\rho}_2 - p_1 \boldsymbol{\rho}_1) = p_2 - p_1$ to show that
$$
(p_{\text{error}})_{\text{optimal}} = \frac{1}{2} - \frac{1}{2} \| p_2 \boldsymbol{\rho}_2 - p_1 \boldsymbol{\rho}_1 \|_1~.
\tag{3.191}
$$
Check whether the answer makes sense in the case where $\boldsymbol{\rho}_1 = \boldsymbol{\rho}_2$ and in the case where $\boldsymbol{\rho}_1$ and $\boldsymbol{\rho}_2$ have support on orthogonal subspaces.

d) Now suppose that Alice decides at random (with $p_1 = p_2 = 1/2$) to prepare one of two pure states $|\psi_1\rangle, |\psi_2\rangle$ of a single qubit, with
$$
|\langle\psi_1|\psi_2\rangle| = \sin(2\alpha)~, \qquad 0 \le \alpha \le \pi/4~.
\tag{3.192}
$$
With a suitable choice of basis, the two states can be expressed as
$$
|\psi_1\rangle = \begin{pmatrix} \cos\alpha \\ \sin\alpha \end{pmatrix}~, \qquad |\psi_2\rangle = \begin{pmatrix} \sin\alpha \\ \cos\alpha \end{pmatrix}~.
\tag{3.193}
$$
Find Bob’s optimal two-outcome measurement, and compute the optimal error probability.

e) Bob wonders whether he can find a better strategy if his POVM $\{\boldsymbol{E}_i\}$ has more than two possible outcomes. Let $p(a|i)$ denote the probability that state $a$ was prepared, given that the measurement outcome was $i$; it can be computed using the relations
$$
\begin{aligned}
p_i p(1|i) &= p_1 p(i|1) = p_1 \text{tr}(\boldsymbol{\rho}_1 \boldsymbol{E}_i)~, \\
p_i p(2|i) &= p_2 p(i|2) = p_2 \text{tr}(\boldsymbol{\rho}_2 \boldsymbol{E}_i)~;
\end{aligned}
\tag{3.194}
$$
here $p(i|a)$ denotes the probability that Bob finds measurement outcome $i$ if Alice prepared the state $\boldsymbol{\rho}_a$, and $p_i$ denotes the probability that Bob finds measurement outcome $i$, averaged over Alice’s choice of state. For each outcome $i$, Bob will make his decision according to which of the two quantities
$$
p(1|i)~, \qquad p(2|i)
\tag{3.195}
$$
is the larger; the probability that he makes a mistake is the smaller of these two quantities. This probability of error, given that Bob obtains outcome $i$, can be written as
$$
p_{\text{error}}(i) = \min(p(1|i), p(2|i)) = \frac{1}{2} - \frac{1}{2} |p(2|i) - p(1|i)|~.
\tag{3.196}
$$
Show that the probability of error, averaged over the measurement outcomes, is
$$
p_{\text{error}} = \sum_i p_i p_{\text{error}}(i) = \frac{1}{2} - \frac{1}{2}\sum_i |\text{tr}(p_2 \boldsymbol{\rho}_2 - p_1 \boldsymbol{\rho}_1)\boldsymbol{E}_i|~.
\tag{3.197}
$$

f) By expanding in terms of the basis of eigenstates of $p_2 \boldsymbol{\rho}_2 - p_1 \boldsymbol{\rho}_1$, show that
$$
p_{\text{error}} \ge \frac{1}{2} - \frac{1}{2}\|p_2 \boldsymbol{\rho}_2 - p_1 \boldsymbol{\rho}_1\|_1~.
\tag{3.198}
$$
(Hint: Use the completeness property $\sum_i \boldsymbol{E}_i = \boldsymbol{I}$.) Since we have already shown that this bound can be saturated with a two-outcome POVM, the POVM with many outcomes is no better.

---

### 3.2 Eavesdropping and disturbance (p. 51)

Alice wants to send a message to Bob. Alice is equipped to prepare either one of the two states $|u\rangle$ or $|v\rangle$. These two states, in a suitable basis, can be expressed as
$$
|u\rangle = \begin{pmatrix} \cos\alpha \\ \sin\alpha \end{pmatrix}~, \qquad |v\rangle = \begin{pmatrix} \sin\alpha \\ \cos\alpha \end{pmatrix}~,
\tag{3.199}
$$
where $0 < \alpha < \pi/4$. Suppose that Alice decides at random to send either $|u\rangle$ or $|v\rangle$ to Bob, and Bob is to make a measurement to determine what she sent. Since the two states are not orthogonal, Bob cannot distinguish the states perfectly.

a) Bob realizes that he can’t expect to be able to identify Alice’s qubit every time, so he settles for a procedure that is successful only some of the time. He performs a POVM with three possible outcomes: $\neg u$, $\neg v$, or DON’T KNOW. If he obtains the result $\neg u$, he is certain that $|v\rangle$ was sent, and if he obtains $\neg v$, he is certain that $|u\rangle$ was sent. If the result is DON’T KNOW, then his measurement is inconclusive. This POVM is defined by the operators
$$
\begin{aligned}
\boldsymbol{E}_{\neg u} &= A(\boldsymbol{I} - |u\rangle\langle u|)~, \qquad \boldsymbol{E}_{\neg v} = A(\boldsymbol{I} - |v\rangle\langle v|)~, \\
\boldsymbol{E}_{\text{DK}} &= (1 - 2A)\boldsymbol{I} + A(|u\rangle\langle u| + |v\rangle\langle v|)~,
\end{aligned}
\tag{3.200}
$$
where $A$ is a positive real number. How should Bob choose $A$ to minimize the probability of the outcome DK, and what is this minimal DK probability (assuming that Alice chooses from $\{|u\rangle, |v\rangle\}$ equiprobably)? Hint: If $A$ is too large, $\boldsymbol{E}_{\text{DK}}$ will have negative eigenvalues, and Eq.(3.200) will not be a POVM.

b) Eve also wants to know what Alice is sending to Bob. Hoping that Alice and Bob won’t notice, she intercepts each qubit that Alice sends, by performing an orthogonal measurement that projects onto the basis
$$
\left\{ \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix} \right\}~.
$$
If she obtains the outcome $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$, she sends the state $|u\rangle$ on to Bob, and if she obtains the outcome $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$, she sends $|v\rangle$ on to Bob. Therefore each time Bob’s POVM has a conclusive outcome, Eve knows with certainty what that outcome is. But Eve’s tampering causes detectable errors; sometimes Bob obtains a “conclusive” outcome that actually differs from what Alice sent. What is the probability of such an error, when Bob’s outcome is conclusive?

---

### 3.3 Minimal disturbance (p. 52)

Consider a game in which Alice decides at random (equiprobably) whether to prepare one of two possible pure states of a single qubit, either
$$
|\psi\rangle = \begin{pmatrix} \cos\alpha \\ \sin\alpha \end{pmatrix}~,
\tag{3.201}
$$
or
$$
|\tilde{\psi}\rangle = \begin{pmatrix} \sin\alpha \\ \cos\alpha \end{pmatrix}~,
\tag{3.202}
$$
and sends the state to Bob. By performing an orthogonal measurement in the basis $\{|0\rangle, |1\rangle\}$, Bob can identify the state with minimal error probability
$$
(p_{\text{error}})_{\text{optimal}} = \sin^2\alpha = \frac{1}{2}(1 - \sin\theta)~,
$$
where we have defined $\theta$ by
$$
\langle\psi|\tilde{\psi}\rangle \equiv \cos\theta = \sin(2\alpha)~.
\tag{3.203}
$$

But now let’s suppose that Eve wants to *eavesdrop* on the state as it travels from Alice to Bob. Like Bob, she wishes to extract optimal information that distinguishes $|\psi\rangle$ from $|\tilde{\psi}\rangle$, and she also wants to minimize the disturbance introduced by her eavesdropping, so that Alice and Bob are not likely to notice that anything is amiss.

Eve realizes that the optimal POVM can be achieved by measurement operators
$$
\boldsymbol{M}_0 = |\phi_0\rangle\langle0|~, \qquad \boldsymbol{M}_1 = |\phi_1\rangle\langle1|~,
\tag{3.204}
$$
where the vectors $|\phi_0\rangle$, and $|\phi_1\rangle$ are arbitrary. If Eve performs this measurement, then Bob receives the state
$$
\boldsymbol{\rho}' = \cos^2\alpha |\phi_0\rangle\langle\phi_0| + \sin^2\alpha |\phi_1\rangle\langle\phi_1|~,
\tag{3.205}
$$
if Alice sent $|\psi\rangle$, and the state
$$
\tilde{\boldsymbol{\rho}}' = \sin^2\alpha |\phi_0\rangle\langle\phi_0| + \cos^2\alpha |\phi_1\rangle\langle\phi_1|~,
\tag{3.206}
$$
if Alice sent $|\tilde{\psi}\rangle$.

Eve wants the average fidelity of the state received by Bob to be as large as possible. The quantity that she wants to minimize, which we will call the “disturbance” $D$, measures how close this average fidelity is to one:
$$
D = 1 - \frac{1}{2}(F + \tilde{F})~,
\tag{3.207}
$$
where
$$
F = \langle\psi|\boldsymbol{\rho}'|\psi\rangle~, \qquad \tilde{F} = \langle\tilde{\psi}|\tilde{\boldsymbol{\rho}}'|\tilde{\psi}\rangle~.
\tag{3.208}
$$
The purpose of this exercise is to examine how effectively Eve can reduce the disturbance by choosing her measurement operators properly.

a) Show that $F + \tilde{F}$ can be expressed as
$$
F + \tilde{F} = \langle\phi_0|\boldsymbol{A}|\phi_0\rangle + \langle\phi_1|\boldsymbol{B}|\phi_1\rangle~,
\tag{3.209}
$$
where
$$
\begin{aligned}
\boldsymbol{A} &= \begin{pmatrix} 1 - 2\cos^2\alpha\sin^2\alpha & \cos\alpha\sin\alpha \\ \cos\alpha\sin\alpha & 2\cos^2\alpha\sin^2\alpha \end{pmatrix}~, \\
\boldsymbol{B} &= \begin{pmatrix} 2\cos^2\alpha\sin^2\alpha & \cos\alpha\sin\alpha \\ \cos\alpha\sin\alpha & 1 - 2\cos^2\alpha\sin^2\alpha \end{pmatrix}~.
\end{aligned}
\tag{3.210}
$$

b) Show that if $|\phi_0\rangle$ and $|\phi_1\rangle$ are chosen optimally, the minimal disturbance that can be attained is
$$
D_{\min}(\cos^2\theta) = \frac{1}{2}\left(1 - \sqrt{1 - \cos^2\theta + \cos^4\theta}\right)~.
\tag{3.211}
$$
[Hint: We can choose $|\phi_0\rangle$ and $|\phi_1\rangle$ to maximize the two terms in eq. (3.209) independently. The maximal value is the maximal eigenvalue of $\boldsymbol{A}$, which since the eigenvalues sum to 1, can be expressed as $\lambda_{\max} = \frac{1}{2}(1 + \sqrt{1 - 4\cdot\det\boldsymbol{A}})$.] Of course, Eve could reduce the disturbance further were she willing to settle for a less than optimal probability of guessing Alice’s state correctly.

c) Sketch a plot of the function $D_{\min}(\cos^2\theta)$. Interpret its value for $\cos\theta = 1$ and $\cos\theta = 0$. For what value of $\theta$ is $D_{\min}$ largest? Find $D_{\min}$ and $(p_{\text{error}})_{\text{optimal}}$ for this value of $\theta$.

---

### 3.4 The price of quantum state encryption (p. 54)

Alice and Bob are working on a top secret project. I can’t tell you exactly what the project is, but I will reveal that Alice and Bob are connected by a perfect quantum channel, and that Alice uses the channel to send quantum states to Bob. Alice and Bob are worried that an eavesdropper (Eve) might intercept some of Alice’s transmissions. By measuring the intercepted quantum state, Eve could learn something about what Alice is sending, and perhaps make an inference about the nature of the project.

To protect against eavesdropping, Alice and Bob decide to *encrypt* the quantum states that Alice sends. They share a *secret key*, a string of random bits about which the eavesdropper knows nothing. By consuming $2n$ bits of secret key, Alice can encrypt, and Bob can decrypt, an arbitrary $n$-qubit state $\boldsymbol{\rho}$. For every possible state $\boldsymbol{\rho}$, the encrypted state looks exactly the same to Eve, so she cannot find out anything about $\boldsymbol{\rho}$.

Here is how the encryption procedure works: We may express the $2n$ bit string $x$ as $x = x_0 x_1 x_2 \cdots x_{n-1}$, where $x_i \in \{0, 1, 2, 3\}$, and denote a tensor product of $n$ Pauli operators as
$$
\boldsymbol{\sigma}(x) = \boldsymbol{\sigma}_{x_0} \otimes \boldsymbol{\sigma}_{x_1} \otimes \cdots \otimes \boldsymbol{\sigma}_{x_{n-1}}
\tag{3.212}
$$
(where $\boldsymbol{\sigma}_0 = \boldsymbol{I}$). Note that $\boldsymbol{\sigma}(x)^2 = \boldsymbol{I}^{\otimes n}$, the identity operator acting on $n$ qubits. To encrypt, Alice consults her random string to determine $x$ (which is chosen uniformly at random), and applies $\boldsymbol{\sigma}(x)$ to the state, obtaining $\boldsymbol{\sigma}(x)\boldsymbol{\rho}\boldsymbol{\sigma}(x)$. To decrypt, Bob, consults the same string and applies $\boldsymbol{\sigma}(x)$ to recover $\boldsymbol{\rho}$.

a) Since Eve does not know the secret key, to her the encrypted state is indistinguishable from
$$
\mathcal{E}(\boldsymbol{\rho}) = \frac{1}{2^{2n}}\sum_x \boldsymbol{\sigma}(x)\boldsymbol{\rho}\boldsymbol{\sigma}(x)~.
\tag{3.213}
$$
Show that, for any $n$-qubit state $\boldsymbol{\rho}$
$$
\mathcal{E}(\boldsymbol{\rho}) = \frac{1}{2^n}\boldsymbol{I}^{\otimes n}~.
\tag{3.214}
$$
Since $\mathcal{E}(\boldsymbol{\rho})$ is independent of $\boldsymbol{\rho}$, no information about $\boldsymbol{\rho}$ is accessible to Eve.

b) Alice wonders if it is possible to encrypt the state using a shorter key. Alice and Bob could use their shared randomness to sample an arbitrary probability distribution. That is, they could agree on a set of $N$ unitary matrices $\{\boldsymbol{U}_a, a = 1, 2, 3, \dots, N\}$, and Alice could encrypt by applying $\boldsymbol{U}_a$ with probability $p_a$. Then Bob could decrypt by applying $\boldsymbol{U}_a^{-1}$. To Eve, the encrypted state would then appear to be
$$
\mathcal{E}'(\boldsymbol{\rho}) = \sum_a p_a \boldsymbol{U}_a \boldsymbol{\rho} \boldsymbol{U}_a^{-1}~.
\tag{3.215}
$$
Show that, if $\mathcal{E}'(\boldsymbol{\rho}) = \boldsymbol{I}^{\otimes n}$, then $p_a \le 2^{-2n}$ for each $a$.

*Hint*: Note that $\mathcal{E}$ has an operator sum representation with Kraus operators $\{\boldsymbol{\sigma}(x)/2^n\}$ and that $\mathcal{E}'$ has an operator sum representation with Kraus operators $\{\sqrt{p_a}\boldsymbol{U}_a\}$. Furthermore $\mathcal{E} = \mathcal{E}'$. Therefore, there exists an $M \times M$ unitary matrix $V_{ax}$ (where $M = \max(N, 2^{2n})$) such that $\sqrt{p_a}\boldsymbol{U}_a = \sum_x V_{ax}\boldsymbol{\sigma}(x)/2^n$. Now express $p_a \text{tr}(\boldsymbol{U}_a \boldsymbol{U}_a^\dagger)$ in terms of $V$.

*Remark*: The result shows that encryption requires $N \ge 2^{2n}$, and that at least $2n$ bits of key are required to specify $\boldsymbol{U}_a$. Thus the encryption scheme in which $\boldsymbol{\sigma}(x)$ is applied is the most efficient possible scheme. (For encryption to be effective, it is enough for $\mathcal{E}(\boldsymbol{\rho})$ to be independent of $\boldsymbol{\rho}$; it is not necessary that $\mathcal{E}(\boldsymbol{\rho}) = \boldsymbol{I}^{\otimes n}/2^n$. But the same result applies under the weaker assumption that $\mathcal{E}(\boldsymbol{\rho})$ is independent of $\boldsymbol{\rho}$.)

---

### 3.5 Unital maps and majorization (p. 55)

Recall that the action of a trace-preserving completely positive (TPCP) map $\mathcal{E}$ can be expressed as
$$
\mathcal{E}(\boldsymbol{\rho}) = \sum_a \boldsymbol{M}_a \boldsymbol{\rho} \boldsymbol{M}_a^\dagger~,
\tag{3.216}
$$
where
$$
\sum_a \boldsymbol{M}_a^\dagger \boldsymbol{M}_a = \boldsymbol{I}~.
\tag{3.217}
$$
A TPCP map is said to be *unital* if $\mathcal{E}(\boldsymbol{I}) = \boldsymbol{I}$, or equivalently if
$$
\sum_a \boldsymbol{M}_a \boldsymbol{M}_a^\dagger = \boldsymbol{I}~.
\tag{3.218}
$$
If $\boldsymbol{A}$ is a nonnegative Hermitian operator with unit trace ($\text{tr}\boldsymbol{A} = 1$), let $\lambda(\boldsymbol{A})$ denote the vector of eigenvalues of $\boldsymbol{A}$, which can be regarded as a probability vector. If $\boldsymbol{A}$ and $\boldsymbol{B}$ are nonnegative Hermitian operators with unit trace, we say that $\boldsymbol{A} \prec \boldsymbol{B}$ (“$\boldsymbol{A}$ is majorized by $\boldsymbol{B}$”) if $\lambda(\boldsymbol{A}) \prec \lambda(\boldsymbol{B})$. (Recall that for two probability vectors $p$ and $q$, we say that $p \prec q$ if there is a doubly stochastic matrix $D$ such that $p = Dq$.)

Show that if $\boldsymbol{\rho}$ is a density operator and $\mathcal{E}$ is a unital map, then
$$
\mathcal{E}(\boldsymbol{\rho}) \prec \boldsymbol{\rho}~.
\tag{3.219}
$$

*Hint*: Express $\boldsymbol{\rho} = \boldsymbol{U}\boldsymbol{\Delta}\boldsymbol{U}^\dagger$ where $\boldsymbol{\Delta}$ is diagonal and $\boldsymbol{U}$ is unitary, and express $\boldsymbol{\rho}' \equiv \mathcal{E}(\boldsymbol{\rho}) = \boldsymbol{V}\boldsymbol{\Delta}'\boldsymbol{V}^\dagger$, where $\boldsymbol{\Delta}'$ is diagonal and $\boldsymbol{V}$ is unitary. Then try to show that the diagonal entries of $\boldsymbol{\Delta}'$ can be expressed as a doubly stochastic matrix acting on the diagonal entries of $\boldsymbol{\Delta}$.

*Remark*: A unital map is the natural quantum generalization of a doubly stochastic map (a doubly stochastic map can be regarded as the special case of a unital map that preserves the basis in which $\boldsymbol{\rho}$ is diagonal). The result of the exercise shows that a unital map takes an input density operator to an output density operator that is no less random than the input.

---

### 3.6 What transformations are possible for bipartite pure states? (p. 56)

Alice and Bob share a bipartite pure state $|\Psi\rangle$. Using a 2-LOCC protocol, they wish to transform it to another bipartite pure state $|\Phi\rangle$. Furthermore, the protocol must be deterministic — the state $|\Phi\rangle$ is obtained with probability one irrespective of the outcomes of the measurements that Alice and Bob perform.

Suppose that these initial and final states have Schmidt decompositions
$$
|\Psi\rangle = \sum_i \sqrt{(p_\Psi)_i} |\alpha_i\rangle \otimes |\beta_i\rangle~, \qquad |\Phi\rangle = \sum_i \sqrt{(p_\Phi)_i} |\alpha'_i\rangle \otimes |\beta'_i\rangle~.
\tag{3.220}
$$

Show that if the deterministic transformation $|\Psi\rangle \mapsto |\Phi\rangle$ is possible, then $p_\Psi \prec p_\Phi$.

*Hints*: Using the Lo-Popescu Theorem from Exercise 2.9, we can reduce the 2-LOCC to an equivalent 1-LOCC. That is, if the deterministic transformation is possible, then there is a generalized measurement that can be applied by Alice, and an operation depending on Alice’s measurement outcome that can be applied by Bob, such that for each possible measurement outcome Alice’s measurement followed by Bob’s operation maps $|\Psi\rangle$ to $|\Phi\rangle$. Recall that a generalized measurement is defined by a set of operators $\{\boldsymbol{M}_a\}$ such that $\sum_a \boldsymbol{M}_a^\dagger \boldsymbol{M}_a = \boldsymbol{I}$, and that the action of the measurement on a pure state $|\psi\rangle$ if outcome $a$ occurs is
$$
|\psi\rangle \mapsto \frac{\boldsymbol{M}_a |\psi\rangle}{\sqrt{\langle\psi|\boldsymbol{M}_a^\dagger \boldsymbol{M}_a|\psi\rangle}}~.
\tag{3.221}
$$
Think about how the 1-LOCC protocol transforms Alice’s density operator. You might want to use the polar decomposition: a matrix $\boldsymbol{A}$ can be expressed as $\sqrt{\boldsymbol{A}\boldsymbol{A}^\dagger}\boldsymbol{U}$, where $\boldsymbol{U}$ is unitary.

*Remark*: The converse is also true. Thus majorization provides the necessary and sufficient condition for the deterministic transformation of one bipartite pure state to another (Nielsen’s Theorem). In this respect, majorization defines a partial order on bipartite pure states such that we may say that $|\Psi\rangle$ is no less entangled than $|\Phi\rangle$ if $p_\Psi \prec p_\Phi$.

---

### 3.7 Fidelity and overlap (p. 57)

The overlap of two probability distributions $\{p_i\}$ and $\{\tilde{p}_i\}$ is defined as
$$
\text{Overlap}(\{p_i\}, \{\tilde{p}_i\}) \equiv \sum_i \sqrt{p_i \cdot \tilde{p}_i}~.
\tag{3.222}
$$
Suppose that we try to distinguish the two states $\boldsymbol{\rho}$ and $\tilde{\boldsymbol{\rho}}$ by performing the POVM $\{\boldsymbol{E}_i\}$. Then the two corresponding probability distributions have the overlap
$$
\text{Overlap}(\boldsymbol{\rho}, \tilde{\boldsymbol{\rho}}; \{\boldsymbol{E}_i\}) \equiv \sum_i \sqrt{\text{tr}(\boldsymbol{\rho}\boldsymbol{E}_i)}\cdot \sqrt{\text{tr}(\tilde{\boldsymbol{\rho}}\boldsymbol{E}_i)}~.
\tag{3.223}
$$
It turns out that the minimal overlap that can be achieved by any POVM is related to the fidelity $F(\boldsymbol{\rho}, \tilde{\boldsymbol{\rho}}) = \|\tilde{\boldsymbol{\rho}}^{1/2}\boldsymbol{\rho}^{1/2}\|_1^2$:
$$
\min_{\{\boldsymbol{E}_i\}} [\text{Overlap}(\boldsymbol{\rho}, \tilde{\boldsymbol{\rho}}; \{\boldsymbol{E}_i\})] = \sqrt{F(\boldsymbol{\rho}, \tilde{\boldsymbol{\rho}})}~.
\tag{3.224}
$$
In this exercise, you will show that the square root of the fidelity is a lower bound on the overlap, but not that the bound can be saturated.

b) The space of linear operators acting on a Hilbert space is itself a Hilbert space, where the inner product $(\boldsymbol{A}, \boldsymbol{B})$ of two operators $\boldsymbol{A}$ and $\boldsymbol{B}$ is
$$
(\boldsymbol{A}, \boldsymbol{B}) \equiv \text{tr}(\boldsymbol{A}^\dagger \boldsymbol{B})~.
\tag{3.225}
$$
For this inner product, the Schwarz inequality becomes
$$
|\text{tr}(\boldsymbol{A}^\dagger \boldsymbol{B})| \le (\text{tr}(\boldsymbol{A}^\dagger \boldsymbol{A}))^{1/2} (\text{tr}(\boldsymbol{B}^\dagger \boldsymbol{B}))^{1/2}~.
\tag{3.226}
$$
Choosing $\boldsymbol{A} = \boldsymbol{\rho}^{1/2}\boldsymbol{E}_i^{1/2}$ and $\boldsymbol{B} = \boldsymbol{U}\tilde{\boldsymbol{\rho}}^{1/2}\boldsymbol{E}_i^{1/2}$ (for an arbitrary unitary $\boldsymbol{U}$), use this form of the Schwarz inequality to show that
$$
\text{Overlap}(\boldsymbol{\rho}, \tilde{\boldsymbol{\rho}}; \{\boldsymbol{E}_i\}) \ge |\text{tr}(\boldsymbol{\rho}^{1/2}\boldsymbol{U}\tilde{\boldsymbol{\rho}}^{1/2})|~.
\tag{3.227}
$$

c) Now use the polar decomposition
$$
\boldsymbol{A} = \boldsymbol{V}\sqrt{\boldsymbol{A}^\dagger \boldsymbol{A}}
\tag{3.228}
$$
(where $\boldsymbol{V}$ is unitary) to write
$$
\tilde{\boldsymbol{\rho}}^{1/2}\boldsymbol{\rho}^{1/2} = \boldsymbol{V}\sqrt{\boldsymbol{\rho}^{1/2}\tilde{\boldsymbol{\rho}}\boldsymbol{\rho}^{1/2}}~,
\tag{3.229}
$$
and by choosing the unitary $\boldsymbol{U}$ in eq. (3.227) to be $\boldsymbol{U} = \boldsymbol{V}^{-1}$, show that
$$
\text{Overlap}(\boldsymbol{\rho}, \tilde{\boldsymbol{\rho}}; \{\boldsymbol{E}_i\}) \ge \sqrt{F(\boldsymbol{\rho}, \tilde{\boldsymbol{\rho}})}~.
\tag{3.230}
$$

d) We can obtain an explicit formula for the fidelity in the case of two states of a single qubit. Using the Bloch parametrization
$$
\boldsymbol{\rho}(\vec{P}) = \frac{1}{2}(\boldsymbol{I} + \vec{\boldsymbol{\sigma}}\cdot\vec{P})~,
\tag{3.231}
$$
show that the fidelity of two single-qubit states with polarization vectors $\vec{P}$ and $\vec{Q}$ is
$$
F(\vec{P}, \vec{Q}) = \frac{1}{2}\left(1 + \vec{P}\cdot\vec{Q} + \sqrt{(1 - \vec{P}^2)(1 - \vec{Q}^2)}\right)~.
\tag{3.232}
$$
*Hint*: First note that the eigenvalues of a $2 \times 2$ matrix can be expressed in terms of the trace and determinant of the matrix. Then evaluate the determinant and trace of $(\boldsymbol{\rho}^{1/2}\tilde{\boldsymbol{\rho}}\boldsymbol{\rho}^{1/2})$, and calculate the fidelity using the corresponding expression for the eigenvalues.

---

### 3.8 Semicausal and semilocal maps in the Heisenberg picture (p. 59)

In the Schrödinger picture, a completely positive (CP) map $\mathcal{E}$ leaves observables fixed and takes an input density operator to an output density operator, $\mathcal{E} : \boldsymbol{\rho}_{\text{in}} \mapsto \boldsymbol{\rho}_{\text{out}} = \mathcal{E}(\boldsymbol{\rho}_{\text{in}})$. In the Heisenberg picture, the dual map $\mathcal{E}^*$ leaves density operators fixed and takes an input observable to an output observable, $\mathcal{E}^* : \boldsymbol{a}_{\text{in}} \mapsto \boldsymbol{a}_{\text{out}} = \mathcal{E}^*(\boldsymbol{a}_{\text{in}})$. If $\mathcal{E}$ has the operator sum representation $\mathcal{E}(\boldsymbol{\rho}) = \sum_a \boldsymbol{M}_a \boldsymbol{\rho} \boldsymbol{M}_a^\dagger$, then its dual has operator sum representation
$$
\mathcal{E}^*(\boldsymbol{a}) = \sum_a \boldsymbol{M}_a^\dagger \boldsymbol{a} \boldsymbol{M}_a~.
\tag{3.233}
$$

a) If $\mathcal{E}$ is a TPCP map, show that its dual $\mathcal{E}^*$ can be represented as
$$
\mathcal{E}^*(\boldsymbol{a}) = {}_C\langle0| \boldsymbol{U}_{AC}^\dagger (\boldsymbol{a}_A \otimes \boldsymbol{I}_C) \boldsymbol{U}_{AC} |0\rangle_C~,
\tag{3.234}
$$
where $\boldsymbol{U}_{AC}$ is a unitary transformation on $AC$, $\boldsymbol{a}_A$ is an observable on $A$, $\boldsymbol{I}_C$ is the identity on $C$, and $|0\rangle_C$ is a fixed pure state in $\mathcal{H}_C$. (You may use the corresponding property of the TPCP map $\mathcal{E}$.)

b) Consider a CP map $\mathcal{E}$ acting on a bipartite quantum system $AB$. We say that $\mathcal{E}$ is *semicausal* if the map does not convey any information from $B$ to $A$. That is, suppose that Alice and Bob share an initial state $\boldsymbol{\rho}_{AB}$. Then if Bob performs an operation on $B$ before the map $\mathcal{E}$ acts, and Alice makes a measurement on $A$ after the map $\mathcal{E}$ acts, Alice’s measurement collects no information about the operation that Bob performed. Show that if $\mathcal{E}$ is semicausal, then there is an operation $\tilde{\mathcal{E}}$ on $A$ such that
$$
\mathcal{E}^*(\boldsymbol{a}_A \otimes \boldsymbol{I}_B) = \tilde{\mathcal{E}}^*(\boldsymbol{a}_A) \otimes \boldsymbol{I}_B~.
\tag{3.235}
$$

c) We say that $\mathcal{E}$ is *semilocal* if it can be performed by means of local operations and one-way quantum communication from $A$ to $B$. That is, there is a message system $C$ that can be passed from Alice to Bob. We may assume that the initial state of $ABC$ is a product $\boldsymbol{\rho}_{AB} \otimes \boldsymbol{\rho}_C$ — the state of the message is uncorrelated with the joint state held by Alice and Bob. To apply $\mathcal{E}$ to $\boldsymbol{\rho}_{AB}$, Alice applies an operation to $AC$, and sends $C$ to Bob. Then Bob applies an operation to $BC$, and discards $C$. Show that if $\mathcal{E}$ is semilocal, then there are CP maps $\mathcal{G}_{AC}$ from $A$ to $AC$ and $\mathcal{F}_{BC}$ from $BC$ to $B$ such that
$$
\mathcal{E}^* = (\mathcal{G}_{AC}^* \otimes \mathcal{I}_B) \circ (\mathcal{I}_A \otimes \mathcal{F}_{BC}^*)~;
\tag{3.236}
$$
here $\circ$ denotes composition of maps, with the map on the right acting first.

d) Using the Heisenberg-picture characterizations of semicausal and semilocal maps found in (b) and (c), show that a semilocal map is semicausal, and express $\tilde{\mathcal{E}}$ in terms of $\mathcal{F}$ and $\mathcal{G}$.

*Remark*. The result (d) is intuitively obvious — communication from Alice to Bob cannot convey a signal from Bob to Alice. What is less obvious is that the converse is also true: every semicausal map is semilocal.

---

### 3.9 Damped harmonic oscillator at zero temperature (p. 60)

Let’s suppose the oscillations of a quantum harmonic oscillator with circular frequency $\omega$ are damped because the oscillator can emit photons with energy $\hbar\omega$. When a photon is emitted, the oscillator makes a transition from the energy eigenstate with energy $E_n = n\hbar\omega$ to the energy eigenstate with energy $E_{n-1} = (n-1)\hbar\omega$, and the photon carries away the lost energy. The probability that a photon is emitted in an infinitesimal time interval $dt$ is $\Gamma dt$; we say that $\Gamma$ is the *emission rate*. Therefore, the coupled evolution of the oscillator and the electromagnetic field for time interval $dt$ can be described as:
$$
\begin{aligned}
|\Psi(0)\rangle &= |\psi\rangle \otimes |0\rangle \mapsto \\
|\Psi(dt)\rangle &= \sqrt{\Gamma dt}\,\boldsymbol{a}|\psi\rangle \otimes |1\rangle + \left(\boldsymbol{I} - \frac{1}{2}\Gamma dt\,\boldsymbol{a}^\dagger \boldsymbol{a}\right)|\psi\rangle \otimes |0\rangle~.
\end{aligned}
\tag{3.237}
$$
Here $|\psi\rangle$ is the initial normalized state vector of the oscillator and $\{|0\rangle, |1\rangle\}$ are orthonormal states of the electromagnetic field; $|0\rangle$ denotes the state in which no photon has been emitted and $|1\rangle$ denotes the state containing one photon. The operator $\boldsymbol{a}$ reduces the excitation level of the oscillator by one unit, and the $\boldsymbol{a}^\dagger \boldsymbol{a}$ factor in the second term is needed to ensure that the evolution is unitary.

a) Check unitarity by verifying that $\langle\Psi(dt)|\Psi(dt)\rangle = 1$, to linear order in the small quantity $dt$.

Because the states $\{|0\rangle, |1\rangle\}$ of the electromagnetic field are orthogonal, the quantum state of the oscillator may decohere. Summing over these basis states, we see that the initial pure state $|\psi\rangle\langle\psi|$ of the oscillator evolves in time $dt$ as
$$
\begin{aligned}
|\psi\rangle\langle\psi| &\mapsto \langle0|\Psi(dt)\rangle\langle\Psi(dt)|0\rangle + \langle1|\Psi(dt)\rangle\langle\Psi(dt)|1\rangle \\
&= \Gamma dt\,\boldsymbol{a}|\psi\rangle\langle\psi|\boldsymbol{a}^\dagger + \left(\boldsymbol{I} - \frac{1}{2}\Gamma dt\,\boldsymbol{a}^\dagger \boldsymbol{a}\right)|\psi\rangle\langle\psi|\left(\boldsymbol{I} - \frac{1}{2}\Gamma dt\,\boldsymbol{a}^\dagger \boldsymbol{a}\right)~;
\end{aligned}
$$
More generally, the initial (not necessarily pure) density operator $\boldsymbol{\rho}$ of the oscillator evolves as
$$
\boldsymbol{\rho} \mapsto \Gamma dt\,\boldsymbol{a}\boldsymbol{\rho}\boldsymbol{a}^\dagger + \left(\boldsymbol{I} - \frac{1}{2}\Gamma dt\,\boldsymbol{a}^\dagger \boldsymbol{a}\right)\boldsymbol{\rho}\left(\boldsymbol{I} - \frac{1}{2}\Gamma dt\,\boldsymbol{a}^\dagger \boldsymbol{a}\right)~.
\tag{3.238}
$$
Now suppose that the initial state of the oscillator is a coherent state
$$
|\alpha\rangle = e^{-|\alpha|^2/2}\sum_{n=0}^\infty \frac{\alpha^n}{\sqrt{n!}}|n\rangle~,
\tag{3.239}
$$
where $\alpha$ is a complex number. For this problem, we will ignore the usual dynamics of the oscillator that causes $\alpha$ to rotate uniformly in time: $\alpha \mapsto \alpha e^{-i\omega t}$; equivalently, we will assume that the dynamics is described in a “rotating frame” such that the rotation of $\alpha$ is transformed away. We will only be interested in how the states of the oscillator are affected by the damping described by eq.(3.238).

b) Show that, to linear order in $dt$,
$$
\left(\boldsymbol{I} - \frac{1}{2}\Gamma dt\,\boldsymbol{a}^\dagger \boldsymbol{a}\right)|\alpha\rangle \approx e^{-\Gamma dt |\alpha|^2/2} |\alpha e^{-\Gamma dt/2}\rangle~.
\tag{3.240}
$$
Note that there are two things to check in eq.(3.240): that the value of $\alpha$ decays with time, and that the normalization of the state decays with time.

c) Verify that, also to linear order in $dt$,
$$
\Gamma dt\,\boldsymbol{a}|\alpha\rangle\langle\alpha|\boldsymbol{a}^\dagger \approx \Gamma dt|\alpha|^2 |\alpha e^{-\Gamma dt/2}\rangle\langle\alpha e^{-\Gamma dt/2}|~,
\tag{3.241}
$$
and thus show that, to linear order in $dt$, $|\alpha\rangle\langle\alpha|$ evolves as
$$
|\alpha\rangle\langle\alpha| \mapsto |\alpha e^{-\Gamma dt/2}\rangle\langle\alpha e^{-\Gamma dt/2}|~.
\tag{3.242}
$$
By considering many consecutive small time increments, argue that, in a finite time $t$, the initial coherent state evolves as
$$
|\alpha\rangle \mapsto |\alpha e^{-\Gamma t/2}\rangle~.
\tag{3.243}
$$
Thus, the state remains a (pure) coherent state at all times, with the value of $\alpha$ decaying exponentially with time. Since the energy stored in the oscillator is proportional to $\alpha^2$, which decays like $e^{-\Gamma t}$, we say that $\Gamma$ is the *damping rate* of the oscillator.

Now consider what happens if the initial state of the oscillator is a superposition of two coherent states:
$$
|\psi\rangle = N_{\alpha,\beta}(|\alpha\rangle + |\beta\rangle)~.
\tag{3.244}
$$
Here $N_{\alpha,\beta}$ is a real nonnegative normalization constant (note that, though the states $|\alpha\rangle$ and $|\beta\rangle$ are both normalized, they are not orthogonal).

d) Evaluate $\langle\beta|\alpha\rangle$, and determine $N_{\alpha,\beta}$.

For example we might choose $\alpha = \xi_0/\sqrt{2}$ and $\beta = -\xi_0/\sqrt{2}$, so that the two superposed coherent states are minimum uncertainty wavepackets (with width $\Delta\xi = 1/\sqrt{2}$) centered at dimensionless positions $\pm\xi_0$. If $|\alpha - \beta| \gg 1$, then the two wavepackets are well separated compared to their width, and we might say that oscillator state $|\psi\rangle$ is “in two places at once.” How quickly will such a superposition of two separated wavepackets decohere?

The initial density operator of the oscillator is
$$
\boldsymbol{\rho} = N_{\alpha,\beta}^2 \left(|\alpha\rangle\langle\alpha| + |\alpha\rangle\langle\beta| + |\beta\rangle\langle\alpha| + |\beta\rangle\langle\beta|\right)~.
\tag{3.245}
$$
We already know from part (c) how the “diagonal” terms $|\alpha\rangle\langle\alpha|$ and $|\beta\rangle\langle\beta|$ evolve, but what about the “off-diagonal” terms $|\alpha\rangle\langle\beta|$ and $|\beta\rangle\langle\alpha|$?

e) Using arguments similar to those used in parts (b) and (c), show that in time $t$, the operator $|\alpha\rangle\langle\beta|$ evolves as
$$
|\alpha\rangle\langle\beta| \mapsto e^{i\phi(\alpha,\beta)} e^{-\Gamma t |\alpha - \beta|^2/2} |\alpha e^{-\Gamma t/2}\rangle\langle\beta e^{-\Gamma t/2}|~,
\tag{3.246}
$$
and find the phase factor $e^{i\phi(\alpha,\beta)}$. Thus the off-diagonal terms decay exponentially with time, at a rate
$$
\Gamma_{\text{decohere}} = \frac{1}{2}\Gamma |\alpha - \beta|^2
\tag{3.247}
$$
proportional to the distance squared $|\alpha - \beta|^2$.

f) Consider an oscillator with mass $m = 1\text{ g}$, circular frequency $\omega = 1\text{ s}^{-1}$ and (very good) quality factor $Q \equiv \omega/\Gamma = 10^9$. Thus the damping time is very long: over 30 years. A superposition of minimum uncertainty wavepackets is prepared, centered at positions $x = \pm 1\text{ cm}$. Estimate the decoherence rate. (Wow! For macroscopic objects, decoherence is really fast!)

---

### 3.10 One-qubit decoherence (p. 63)

The matrices $\boldsymbol{I}, \boldsymbol{\sigma}_1, \boldsymbol{\sigma}_2, \boldsymbol{\sigma}_3$, where $\boldsymbol{\sigma}_{1,2,3}$ are the Pauli matrices and $\boldsymbol{I}$ is the identity matrix, are a basis for the four-dimensional space of $2 \times 2$ matrices. Let us denote $\boldsymbol{I}$ as $\boldsymbol{\sigma}_0$.

a) Let $\mathcal{E}$ be a quantum operation (a completely positive map) acting on the density operator $\boldsymbol{\rho}$ of a single qubit. Show that we may express $\mathcal{E}(\boldsymbol{\rho})$ as
$$
\mathcal{E}(\boldsymbol{\rho}) = \sum_{\mu,\nu=0}^3 \mathcal{E}_{\mu\nu}\boldsymbol{\sigma}_\mu \boldsymbol{\rho} \boldsymbol{\sigma}_\nu~,
\tag{3.248}
$$
where the $\mathcal{E}_{\mu\nu}$’s are complex numbers satisfying $\mathcal{E}_{\mu\nu} = \mathcal{E}_{\nu\mu}^*$.

*Hint*: The operation $\mathcal{E}$ has an operator-sum representation with operation elements $\{\boldsymbol{M}_a\}$. Each $\boldsymbol{M}_a$ can be expanded in the basis $\{\boldsymbol{\sigma}_\mu, \mu = 0, 1, 2, 3\}$.

b) Find four independent conditions that must be satisfied by the $\mathcal{E}_{\mu\nu}$’s in order that the operation $\mathcal{E}$ be trace-preserving (a channel).

c) A Hermitian $2 \times 2$ operator can be expressed as
$$
\boldsymbol{\rho}(P) = \frac{1}{2}\sum_{\mu=0}^3 P_\mu \boldsymbol{\sigma}_\mu~,
\tag{3.249}
$$
where $P_0, P_1, P_2, P_3$ are real numbers. Show that a linear map that takes Hermitian operators to Hermitian operators acts as
$$
\mathcal{E}(\boldsymbol{\rho}(P)) = \boldsymbol{\rho}(P')~,
\tag{3.250}
$$
where $P' = M P$ and $M$ is a real matrix. What is the (real) dimension of the space of such linear maps?

d) Suppose that $\text{tr}\boldsymbol{\rho} = 1$ and that $\mathcal{E}$ is trace preserving, so that $P_0 = P'_0 = 1$. Show that
$$
\vec{P}' = \boldsymbol{M}\vec{P} + \vec{v}~,
\tag{3.251}
$$
where $\vec{P}$ and $\vec{P}'$ are real three-component polarization vectors, $\boldsymbol{M}$ is a real matrix, and $\vec{v}$ is a real three-component vector. What is the (real) dimension of the space of such trace-preserving maps?

e) Express $\vec{v}$ in terms of the $\mathcal{E}_{0k}$’s. *Hint*: Use the result of (b).

f) On a Hilbert space of dimension $d$, the space of linear maps from Hermitian operators to Hermitian operators has real dimension $d^4$. What is the dimension of the space of trace-preserving maps? *Hint*: Count the number of independent conditions that must be imposed to ensure that the map is trace preserving.

---

### 3.11 Orthogonal or not? (p. 64)

Consider a generalized measurement (POVM) on an $d$-dimensional Hilbert space. There are $d$ possible outcomes for the measurement corresponding to the $d$ nonnegative operators $\boldsymbol{E}_a$, $a = 0, 1, 2, \dots, d-1$, where $\sum_{a=0}^{d-1}\boldsymbol{E}_a = \boldsymbol{I}$. Suppose that each $\boldsymbol{E}_a$ is one-dimensional (has one nonzero eigenvalue). Is this POVM necessarily an orthogonal measurement? Explain your answer.

---

### 3.12 Heterodyne measurement of an oscillator (p. 64)

The coherent states $\{|\alpha\rangle, \alpha \in \mathbb{C}\}$ are an overcomplete basis for a one-dimensional harmonic oscillator, satisfying
$$
\langle\beta|\alpha\rangle = \exp\left(-\frac{1}{2}|\beta|^2 + \beta^*\alpha - \frac{1}{2}|\alpha|^2\right)~.
\tag{3.252}
$$

a) Show that
$$
\int d^2\alpha\, \boldsymbol{E}_\alpha = \boldsymbol{I}~,
\tag{3.253}
$$
where
$$
\boldsymbol{E}_\alpha = \frac{1}{\pi}|\alpha\rangle\langle\alpha|~.
\tag{3.254}
$$
*Hint*: Evaluate matrix elements of both sides of the equation between coherent states.

b) Since the $\boldsymbol{E}_\alpha$’s provide a partition of unity, they define a POVM (an “ideal heterodyne measurement” of the oscillator). Suppose that a coherent state $|\beta\rangle$ is prepared, and that an ideal heterodyne measurement is performed, so that the coherent state $|\alpha\rangle$ is obtained with probability distribution $P(\alpha)d^2\alpha = \langle\beta|\boldsymbol{E}_\alpha|\beta\rangle d^2\alpha$. With what fidelity does the measurement outcome $|\alpha\rangle$ approximate the initial coherent state $|\beta\rangle$, averaged over the possible outcomes?

---

### 3.13 Master equation for the depolarizing channel (p. 64)

a) Consider a depolarizing qubit that is subjected to “Pauli errors” at a rate $\tilde{\Gamma}$, where $\boldsymbol{\sigma}_1, \boldsymbol{\sigma}_2$, and $\boldsymbol{\sigma}_3$ errors are all equally likely. The depolarization can be described by a master equation with Lindblad operators $\sqrt{\tilde{\Gamma}/3}\,\boldsymbol{\sigma}_1$, $\sqrt{\tilde{\Gamma}/3}\,\boldsymbol{\sigma}_2$, and $\sqrt{\tilde{\Gamma}/3}\,\boldsymbol{\sigma}_3$. Show that this master equation has the form
$$
\dot{\boldsymbol{\rho}} = -i[\boldsymbol{H}, \boldsymbol{\rho}] - \Gamma\left(\boldsymbol{\rho} - \frac{1}{2}\boldsymbol{I}\right)~.
\tag{3.255}
$$
How is $\Gamma$ related to $\tilde{\Gamma}$?

b) Up to an irrelevant term proportional to the identity, the most general $2 \times 2$ Hermitian matrix is
$$
\boldsymbol{H} = \frac{\omega}{2}\boldsymbol{n}\cdot\vec{\boldsymbol{\sigma}}~,
\tag{3.256}
$$
where $\boldsymbol{n}$ is a unit vector. Use this form of $\boldsymbol{H}$ and the Bloch parametrization
$$
\boldsymbol{\rho} = \frac{1}{2}(\boldsymbol{I} + \vec{P}\cdot\vec{\boldsymbol{\sigma}})~,
\tag{3.257}
$$
to show that the master equation eq. (3.255) can be rewritten as
$$
\dot{\vec{P}} = \omega(\boldsymbol{n} \times \vec{P}) - \Gamma \vec{P}~.
\tag{3.258}
$$
Thus the polarization precesses uniformly with circular frequency $\omega$ about the $\boldsymbol{n}$-axis as it contracts with lifetime $\Gamma^{-1}$.

c) Alice and Bob play a game in which Alice decides to “turn on” one of the two Hamiltonians
$$
\boldsymbol{H} = \frac{\omega}{2}\boldsymbol{\sigma}_3~, \qquad \boldsymbol{H}' = 0~,
\tag{3.259}
$$
and Bob is to guess which Hamiltonian Alice chose. Bob has a supply of qubits, and he can observe whether the qubits “precess” in order to distinguish $\boldsymbol{H}$ from $\boldsymbol{H}'$. However, his qubits are also subject to depolarization at the rate $\Gamma$ as in eq. (3.255). Suppose that Bob prepares his qubits at time 0 with polarization $\vec{P}_0 = (1, 0, 0)$; after time $t$ elapses, (1) find the polarization $\vec{P}(t)$ if the Hamiltonian is $\boldsymbol{H}$ and (2) find the polarization $\vec{P}'(t)$ if the Hamiltonian is $\boldsymbol{H}'$.

d) What is Bob’s optimal measurement for distinguishing the polarizations $\vec{P}(t)$ and $\vec{P}'(t)$ (assuming that Alice is as likely to choose $\boldsymbol{H}$ as $\boldsymbol{H}'$? What is his optimal probability of error $(p_e)_{\text{opt}}(t)$?

e) The probability of error is smallest if Bob waits for a time $t_{\text{best}}$ before measuring. Find $t_{\text{best}}$ as a function of $\Gamma$ and $\omega$. Does your answer make sense in the limits $\Gamma \gg \omega$ and $\Gamma \ll \omega$?
