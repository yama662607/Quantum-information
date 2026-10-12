# Section 4.12: Exercises [PDF Pages 59-70]

<!-- ============================================================ -->
<!-- Source: chap4.pdf, Physical Pages: 59-70                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

# 4.12 Exercises [📄 chap4.pdf](/assets/pdf/preskill/chap4.pdf#page=59)

<!-- Page 59 -->
## 4.1 Hardy's theorem

<!-- Page 60 -->
Bob (in Boston) and Claire (in Chicago) share many identically prepared copies of the two-qubit state
$$
|\psi\rangle = \sqrt{(1-2x)} |00\rangle + \sqrt{x} |01\rangle + \sqrt{x} |10\rangle , \tag{4.154}
$$
where $x$ is a real number between $0$ and $1/2$. They conduct many trials in which each measures his/her qubit in the basis $\{|0\rangle, |1\rangle\}$, and they learn that if Bob's outcome is $1$ then Claire's is always $0$, and if Claire's outcome is $1$ then Bob's is always $0$.

Bob and Claire conduct further experiments in which Bob measures in the basis $\{|0\rangle, |1\rangle\}$ and Claire measures in the orthonormal basis $\{|\varphi\rangle, |\varphi^\perp\rangle\}$. They discover that if Bob's outcome is $0$, then Claire's outcome is always $\varphi$ and never $\varphi^\perp$. Similarly, if Claire measures in the basis $\{|0\rangle, |1\rangle\}$ and Bob measures in the basis $\{|\varphi\rangle, |\varphi^\perp\rangle\}$, then if Claire's outcome is $0$, Bob's outcome is always $\varphi$ and never $\varphi^\perp$.

a) Express the basis $\{|\varphi\rangle, |\varphi^\perp\rangle\}$ in terms of the basis $\{|0\rangle, |1\rangle\}$.

Bob and Claire now wonder what will happen if they both measure in the basis $\{|\varphi\rangle, |\varphi^\perp\rangle\}$. Their friend Albert, a firm believer in local realism, predicts that it is impossible for both to obtain the outcome $\varphi^\perp$ (a prediction known as *Hardy's theorem*). Albert argues as follows:

> When both Bob and Claire measure in the basis $\{|\varphi\rangle, |\varphi^\perp\rangle\}$, it is reasonable to consider what might have happened if one or the other had measured in the basis $\{|0\rangle, |1\rangle\}$ instead.
>
> So suppose that Bob and Claire both measure in the basis $\{|\varphi\rangle, |\varphi^\perp\rangle\}$, and that they both obtain the outcome $\varphi^\perp$. Now if Bob had measured in the basis $\{|0\rangle, |1\rangle\}$ instead, we can be certain that his outcome would have been $1$, since experiment has shown that if Bob had obtained $0$ then Claire could not have obtained $\varphi^\perp$. Similarly, if Claire had measured in the basis $\{|0\rangle, |1\rangle\}$, then she certainly would have obtained the outcome $1$. We conclude that if Bob and Claire both measured in the basis $\{|0\rangle, |1\rangle\}$, both would have obtained the outcome $1$. But this is a contradiction, for experiment has shown that it is not possible for both Bob and Claire to obtain the outcome $1$ if they both measure in the basis $\{|0\rangle, |1\rangle\}$.
>
> We are therefore forced to conclude that if Bob and Claire both measure in the basis $\{|\varphi\rangle, |\varphi^\perp\rangle\}$, it is impossible for both to obtain the outcome $\varphi^\perp$.

<!-- Page 61 -->
Though impressed by Albert's reasoning, Bob and Claire decide to investigate what predictions can be inferred from quantum mechanics.

b) If Bob and Claire both measure in the basis $\{|\varphi\rangle, |\varphi^\perp\rangle\}$, what is the quantum-mechanical prediction for the probability $P(x)$ that both obtain the outcome $\varphi^\perp$?

c) Find the "maximal violation" of Hardy's theorem: show that the maximal value of $P(x)$ is $P[(3-\sqrt{5})/2] = (5\sqrt{5}-11)/2 \approx .0902$.

d) Bob and Claire conduct an experiment that confirms the prediction of quantum mechanics. What was wrong with Albert's reasoning?

## 4.2 Closing the detection loophole

Recall that the *CHSH inequality*
$$
|\langle ab\rangle + \langle a'b\rangle + \langle ab'\rangle - \langle a'b'\rangle| \le 2 \tag{4.155}
$$
holds if the random variables $a, b, a'b'$ take values $\pm 1$ and are governed by a joint probability distribution. The maximal violation of this inequality by the quantum-mechanical predictions occurs when the left-hand-side is $2\sqrt{2}$, which is achieved if Alice and Bob share the maximally entangled state $|\phi^+\rangle$, $a, a'$ are measurements of Alice's qubit along axes $\hat{x}$ and $\hat{z}$, and $b, b'$ are measurements of Bob's qubit along axes $(\hat{x} + \hat{z})/\sqrt{2}$ and $(\hat{x} - \hat{z})/\sqrt{2}$.

Alice and Bob have done a beautiful experiment measuring the polarizations of entangled photon pairs, and have confirmed the CHSH inequality violation predicted by quantum mechanics. Albert is skeptical. He points out that the detectors used by Alice and Bob in their experiment are not very efficient. Usually, when Alice detects a photon, Bob does not, and when Bob detects a photon, Alice does not. Therefore, they discard the data for most of the photon pairs, and retain the results only in the case when two photons are detected in coincidence. In their analysis of the data, Alice and Bob assume that their results are based on a fair sample of the probability distribution governing the measured variables. But Albert argues that their conclusions could be evaded if *whether* a photon is detected is correlated with the *outcome* of the polarization measurement.

Alice and Bob wonder how much they will need to improve their detector efficiency to do an experiment that will impress Albert.

Alice can choose to orient her detector along any axis, and if she aligns the detector with the axis $a$, then ideally the detector will

<!-- Page 62 -->
click when her qubit's spin is pointing up along $a$, but because of detector inefficiencies it sometimes fails to click even though the qubit points up. For pair number $i$, let $x_i \in \{0, 1\}$ be a variable indicating whether Alice's detector would click when aligned with $a$ — if there would be a click then $x_i = 1$, and if there would be no click then $x_i = 0$. Since the detector is imperfect, $x_i$ may be $0$ even though the qubit points up along $a$. Similarly, $x'_i \in \{0, 1\}$ indicates whether Alice's detector would click if aligned with $a'$, $y_i \in \{0, 1\}$ indicates whether Bob's detector would click if aligned with $b$ and $y'_i \in \{0, 1\}$ indicates whether Bob's detector would click if aligned with $b'$. Under the assumption of local realism, each pair can be assigned values of $x, x', y, y'$ that are determined by local hidden variables.

Alice and Bob are free to decide how to align their detectors in each measurement; therefore they can fairly sample the values of $x, x', y, y'$ and infer from their measurements the values of
$$
\begin{aligned}
P_{++}(ab) &= N^{-1} \sum_{i=1}^N x_i y_i , \\
P_{++}(a'b) &= N^{-1} \sum_{i=1}^N x'_i y_i , \\
P_{++}(ab') &= N^{-1} \sum_{i=1}^N x_i y'_i , \\
P_{++}(a'b') &= N^{-1} \sum_{i=1}^N x'_i y'_i , \tag{4.156}
\end{aligned}
$$
where $N$ is the total number of pairs tested. Here e.g. $P_{++}(ab)$ is the probability that both detectors click when Alice and Bob orient their detectors along $a$ and $b$ (including the effects of detector inefficiency).

a) If $x, x', y, y' \in \{0, 1\}$, show that
$$
x y + x y' + x' y - x' y' \le x + y . \tag{4.157}
$$

b) Show that
$$
P_{++}(ab) + P_{++}(a'b) + P_{++}(ab') - P_{++}(a'b') \le P_+(a) + P_+(b) ; \tag{4.158}
$$
here $P_+(a)$ denotes the probability that Alice's detector clicks if oriented along $a$, and $P_+(b)$ denotes the probability that Bob's detector clicks if oriented along $b$.

<!-- Page 63 -->
c) Now compare with the predictions of quantum mechanics, where Alice's detector has efficiency $\eta_A$ and Bob's detector has efficiency $\eta_B$. This means that Alice's detector clicks with probability $P = \eta_A P_{\text{perf}}$, where $P_{\text{perf}}$ is the probability of a click if her detector were perfect, and similarly for Bob. Choosing the $a, a', b, b'$ that maximally violate the CHSH inequality, show that the quantum-mechanical predictions violate eq. (4.158) only if
$$
\frac{\eta_A \eta_B}{\eta_A + \eta_B} > \frac{1}{1 + \sqrt{2}} . \tag{4.159}
$$
Thus, if $\eta_A = \eta_B$, Alice and Bob require detectors with efficiency above $82.84\%$ to overcome Albert's objection.

## 4.3 Teleportation with continuous variables

One complete orthonormal basis for the Hilbert space of two particles on the real line is the (separable) position eigenstate basis $\{|q_1\rangle \otimes |q_2\rangle\}$. Another is the entangled basis $\{|Q, P\rangle\}$, where
$$
|Q, P\rangle = \frac{1}{\sqrt{2\pi}} \int dq\, e^{i P q} |q\rangle \otimes |q + Q\rangle ; \tag{4.160}
$$
these are the simultaneous eigenstates of the relative position operator $\boldsymbol{Q} \equiv \boldsymbol{q}_2 - \boldsymbol{q}_1$ and the total momentum operator $\boldsymbol{P} \equiv \boldsymbol{p}_1 + \boldsymbol{p}_2$.

a) Verify that
$$
\langle Q', P' | Q, P \rangle = \delta(Q' - Q) \delta(P' - P) . \tag{4.161}
$$

b) Since the states $\{|Q, P\rangle\}$ are a basis, we can expand a position eigenstate as
$$
|q_1\rangle \otimes |q_2\rangle = \int dQ dP\, |Q, P\rangle \langle Q, P | (|q_1\rangle \otimes |q_2\rangle) . \tag{4.162}
$$
Evaluate the coefficients $\langle Q, P | (|q_1\rangle \otimes |q_2\rangle)$.

c) Alice and Bob have prepared the entangled state $|Q, P\rangle_{AB}$ of two particles $A$ and $B$; Alice has kept particle $A$ and Bob has particle $B$. Now Alice has received an unknown single-particle wavepacket $|\psi\rangle_C = \int dq\, |q\rangle_C\,{}_C\langle q|\psi\rangle_C$ that she intends to teleport to Bob. Design a protocol that they can execute to achieve the teleportation. What should Alice measure? What information should she send to Bob? What should Bob do when he receives this information, so that particle $B$ will be prepared in the state $|\psi\rangle_B$?

<!-- Page 64 -->
## 4.4 Teleportation with mixed states.

An operational way to define entanglement is that an entangled state can be used to teleport an unknown quantum state with better fidelity than could be achieved with local operations and classical communication only. In this exercise, you will show that there are mixed states that are entangled in this sense, yet do not violate any Bell inequality. Hence, for mixed states (in contrast to pure states) "entangled" and "Bell-inequality-violating" are not equivalent.

Consider a "noisy" entangled pair with density matrix
$$
\boldsymbol{\rho}(\lambda) = (1 - \lambda) |\psi^-\rangle\langle\psi^-| + \lambda \frac{1}{4} \boldsymbol{1} . \tag{4.163}
$$

a) Find the fidelity $F$ that can be attained if the state $\boldsymbol{\rho}(\lambda)$ is used to teleport a qubit from Alice to Bob. [Hint: Recall that you showed in an earlier exercise that a "random guess" has fidelity $F = \frac{1}{2}$.]

b) For what values of $\lambda$ is the fidelity found in (a) better than what can be achieved if Alice measures her qubit and sends a classical message to Bob? [Hint: Earlier, you showed that $F = 2/3$ can be achieved if Alice measures her qubit. In fact this is the best possible $F$ attainable with classical communication.]

c) Compute
$$
\operatorname{Prob}(\uparrow_{\hat{n}} \uparrow_{\hat{m}}) \equiv \operatorname{tr}\left(\boldsymbol{E}_A(\hat{n}) \boldsymbol{E}_B(\hat{m}) \boldsymbol{\rho}(\lambda)\right) , \tag{4.164}
$$
where $\boldsymbol{E}_A(\hat{n})$ is the projection of Alice's qubit onto $|\uparrow_{\hat{n}}\rangle$ and $\boldsymbol{E}_B(\hat{m})$ is the projection of Bob's qubit onto $|\uparrow_{\hat{m}}\rangle$.

d) Consider the case $\lambda = 1/2$. Show that in this case the state $\boldsymbol{\rho}(\lambda)$ violates no Bell inequalities. Hint: It suffices to construct a local hidden-variable model that correctly reproduces the spin correlations found in (c), for $\lambda = 1/2$. Suppose that the hidden variable $\hat{\alpha}$ is uniformly distributed on the unit sphere, and that there are functions $f_A$ and $f_B$ such that
$$
\operatorname{Prob}_A(\uparrow_{\hat{n}}) = f_A(\hat{\alpha} \cdot \hat{n}), \quad \operatorname{Prob}_B(\uparrow_{\hat{m}}) = f_B(\hat{\alpha} \cdot \hat{m}) . \tag{4.165}
$$
The problem is to find $f_A$ and $f_B$ (where $0 \le f_{A, B} \le 1$) with the properties
$$
\begin{aligned}
\int_{\hat{\alpha}} f_A(\hat{\alpha} \cdot \hat{n}) &= 1/2 , \quad \int_{\hat{\alpha}} f_B(\hat{\alpha} \cdot \hat{m}) = 1/2 , \\
\int_{\hat{\alpha}} f_A(\hat{\alpha} \cdot \hat{n}) f_B(\hat{\alpha} \cdot \hat{m}) &= \operatorname{Prob}(\uparrow_{\hat{n}} \uparrow_{\hat{m}}) . \tag{4.166}
\end{aligned}
$$

<!-- Page 65 -->
## 4.5 Quantum key distribution

Alice and Bob want to execute a quantum key distribution protocol. Alice is equipped to prepare either one of the two states $|u\rangle$ or $|v\rangle$. These two states, in a suitable basis, can be expressed as
$$
|u\rangle = \begin{pmatrix} \cos\alpha \\ \sin\alpha \end{pmatrix} , \quad |v\rangle = \begin{pmatrix} \sin\alpha \\ \cos\alpha \end{pmatrix} , \tag{4.167}
$$
where $0 < \alpha < \pi/4$. Alice decides at random to send either $|u\rangle$ or $|v\rangle$ to Bob, and Bob is to make a measurement to determine what she sent. Since the two states are not orthogonal, Bob cannot distinguish the states perfectly.

a) Bob realizes that he can't expect to be able to identify Alice's qubit every time, so he settles for a procedure that is successful only some of the time. He performs a POVM with three possible outcomes: $\neg u$, $\neg v$, or $\text{DON'T KNOW}$. If he obtains the result $\neg u$, he is certain that $|v\rangle$ was sent, and if he obtains $\neg v$, he is certain that $|u\rangle$ was sent. If the result is $\text{DON'T KNOW}$, then his measurement is inconclusive. This POVM is defined by the operators
$$
\begin{aligned}
\boldsymbol{F}_{\neg u} &= A(\boldsymbol{I} - |u\rangle\langle u|) , \quad \boldsymbol{F}_{\neg v} = A(\boldsymbol{I} - |v\rangle\langle v|) , \\
\boldsymbol{F}_{\text{DK}} &= (1 - 2A)\boldsymbol{I} + A(|u\rangle\langle u| + |v\rangle\langle v|) , \tag{4.168}
\end{aligned}
$$
where $A$ is a positive real number. How should Bob choose $A$ to minimize the probability of the outcome DK, and what is this minimal DK probability (assuming that Alice chooses from $\{|u\rangle, |v\rangle\}$ equiprobably)? [Hint: If $A$ is too large, $\boldsymbol{F}_{\text{DK}}$ will have negative eigenvalues, and eq. (4.168) will not be a POVM.]

b) Design a quantum key distribution protocol using Alice's source and Bob's POVM.

c) Of course, Eve also wants to know what Alice is sending to Bob. Hoping that Alice and Bob won't notice, she intercepts each qubit that Alice sends, by performing an orthogonal measurement that projects onto the basis $\left\{\begin{pmatrix} 1 \\ 0 \end{pmatrix}, \begin{pmatrix} 0 \\ 1 \end{pmatrix}\right\}$. If she obtains the outcome $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$, she sends the state $|u\rangle$ on to Bob, and if she obtains the outcome $\begin{pmatrix} 0 \\ 1 \end{pmatrix}$, she sends $|v\rangle$ on to Bob. Therefore each time Bob's POVM has a conclusive outcome, Eve knows with certainty what that outcome is. But Eve's tampering causes detectable errors; sometimes Bob obtains a "conclusive"

<!-- Page 66 -->
outcome that actually differs from what Alice sent. What is the probability of such an error?

## 4.6 Minimal disturbance

In Exercise 2.1, we studied a game in which Alice decides at random (equiprobably) whether to prepare one of two possible pure states of a single qubit, either
$$
|\psi\rangle = \begin{pmatrix} \cos\alpha \\ \sin\alpha \end{pmatrix} , \quad \text{or} \quad |\tilde{\psi}\rangle = \begin{pmatrix} \sin\alpha \\ \cos\alpha \end{pmatrix} , \tag{4.169}
$$
and sends the state to Bob. By performing an orthogonal measurement in the basis $\{|0\rangle, |1\rangle\}$, Bob can identify the state with minimal error probability
$$
(p_{\text{error}})_{\text{optimal}} = \sin^2\alpha = \frac{1}{2}(1 - \sin\theta) , \tag{4.170}
$$
where we have defined $\theta$ by
$$
\langle\psi|\tilde{\psi}\rangle \equiv \cos\theta = \sin(2\alpha) . \tag{4.171}
$$

But now let's suppose that Eve wants to *eavesdrop* on the state as it travels from Alice to Bob. Like Bob, she wishes to extract optimal information that distinguishes $|\psi\rangle$ from $|\tilde{\psi}\rangle$, and she also wants to minimize the disturbance introduced by her eavesdropping, so that Alice and Bob are not likely to notice that anything is amiss.

Eve realizes that the optimal POVM can be achieved by measurement operators
$$
\boldsymbol{M}_0 = |\phi_0\rangle\langle 0| , \quad \boldsymbol{M}_1 = |\phi_1\rangle\langle 1| , \tag{4.172}
$$
where the vectors $|\phi_0\rangle$, and $|\phi_1\rangle$ are arbitrary. If Eve performs this measurement, then Bob receives the state
$$
\boldsymbol{\rho}' = \cos^2\alpha |\phi_0\rangle\langle\phi_0| + \sin^2\alpha |\phi_1\rangle\langle\phi_1| , \tag{4.173}
$$
if Alice sent $|\psi\rangle$, and the state
$$
\tilde{\boldsymbol{\rho}}' = \sin^2\alpha |\phi_0\rangle\langle\phi_0| + \cos^2\alpha |\phi_1\rangle\langle\phi_1| , \tag{4.174}
$$
if Alice sent $|\tilde{\psi}\rangle$.

Eve wants the average fidelity of the state received by Bob to be as large as possible. The quantity that she wants to minimize, which

<!-- Page 67 -->
we will call the "disturbance" $D$, measures how close this average fidelity is to one:
$$
D = 1 - \frac{1}{2}(F + \tilde{F}) , \tag{4.175}
$$
where
$$
F = \langle\psi|\boldsymbol{\rho}'|\psi\rangle , \quad \tilde{F} = \langle\tilde{\psi}|\tilde{\boldsymbol{\rho}}'|\tilde{\psi}\rangle . \tag{4.176}
$$
The purpose of this exercise is to examine how effectively Eve can reduce the disturbance by choosing her measurement operators properly.

a) Show that $F + \tilde{F}$ can be expressed as
$$
F + \tilde{F} = \langle\phi_0|\boldsymbol{A}|\phi_0\rangle + \langle\phi_1|\boldsymbol{B}|\phi_1\rangle , \tag{4.177}
$$
where
$$
\begin{aligned}
\boldsymbol{A} &= \begin{pmatrix} 1 - 2\cos^2\alpha\sin^2\alpha & \cos\alpha\sin\alpha \\ \cos\alpha\sin\alpha & 2\cos^2\alpha\sin^2\alpha \end{pmatrix} , \\
\boldsymbol{B} &= \begin{pmatrix} 2\cos^2\alpha\sin^2\alpha & \cos\alpha\sin\alpha \\ \cos\alpha\sin\alpha & 1 - 2\cos^2\alpha\sin^2\alpha \end{pmatrix} . \tag{4.178}
\end{aligned}
$$

b) Show that if $|\phi_0\rangle$ and $|\phi_1\rangle$ are chosen optimally, the minimal disturbance that can be attained is
$$
D_{\min}(\cos^2\theta) = \frac{1}{2}\left(1 - \sqrt{1 - \cos^2\theta + \cos^4\theta}\right) . \tag{4.179}
$$
[Hint: We can choose $|\phi_0\rangle$ and $|\phi_1\rangle$ to maximize the two terms in eq. (4.177) independently. The maximal value is the maximal eigenvalue of $\boldsymbol{A}$, which since the eigenvalues sum to 1, can be expressed as $\lambda_{\max} = \frac{1}{2}\left(1 + \sqrt{1 - 4 \cdot \det\boldsymbol{A}}\right)$.] Of course, Eve could reduce the disturbance further were she willing to settle for a less than optimal probability of guessing Alice's state correctly.

c) Sketch a plot of the function $D_{\min}(\cos^2\theta)$. Interpret its value for $\cos\theta = 1$ and $\cos\theta = 0$. For what value of $\theta$ is $D_{\min}$ largest? Find $D_{\min}$ and $(p_{\text{error}})_{\text{optimal}}$ for this value of $\theta$.

## 4.7 Approximate cloning

The no-cloning theorem shows that we can't build a unitary machine that will make a perfect copy of an unknown quantum state. But

<!-- Page 68 -->
suppose we are willing to settle for an *imperfect* copy — what fidelity might we achieve?

Consider a machine that acts on three qubit states according to
$$
\begin{aligned}
|000\rangle_{ABC} &\to \sqrt{\frac{2}{3}} |00\rangle_{AB} |0\rangle_C + \sqrt{\frac{1}{3}} |\psi^+\rangle_{AB} |1\rangle_C \\
|100\rangle_{ABC} &\to \sqrt{\frac{2}{3}} |11\rangle_{AB} |1\rangle_C + \sqrt{\frac{1}{3}} |\psi^+\rangle_{AB} |0\rangle_C . \tag{4.180}
\end{aligned}
$$

a) Is such a device physically realizable, in principle?

If the machine operates on the initial state $|\psi\rangle_A |00\rangle_{BC}$, it produces an pure entangled state $|\Psi\rangle_{ABC}$ of the three qubits. But if we observe qubit $A$ alone, its final state is the density operator $\boldsymbol{\rho}'_A = \operatorname{tr}_{BC}(|\Psi\rangle_{ABC}\langle\Psi|)$. Similarly, the qubit $B$, observed in isolation, has the final state $\boldsymbol{\rho}'_B$. It is easy to see that $\boldsymbol{\rho}'_A = \boldsymbol{\rho}'_B$ — these are the identical, but imperfect, copies of the input pure state $|\psi\rangle_A$.

b) The mapping from the initial state $|\psi\rangle_A\langle\psi|$ to the final state $\boldsymbol{\rho}'_A$ of qubit $A$ defines a superoperator $\$$. Find an operator-sum representation of $\$$.

c) For $|\psi\rangle_A = a|0\rangle_A + b|1\rangle_A$, find $\boldsymbol{\rho}'_A$, and compute its fidelity $F \equiv {}_A\langle\psi|\boldsymbol{\rho}'_A|\psi\rangle_A$.

## 4.8 We're so sorry, Uncle Albert

Consider the $n$-qubit "cat" state
$$
|\psi\rangle_n = \sqrt{\frac{1}{2}} (|000\dots 0\rangle + |111\dots 1\rangle) . \tag{4.181}
$$
This state can be characterized as the simultaneous eigenstate (with eigenvalue 1) of the $n$ operators
$$
\begin{aligned}
&\boldsymbol{\sigma}_3 \otimes \boldsymbol{\sigma}_3 \otimes \boldsymbol{I} \otimes \boldsymbol{I} \otimes \dots \otimes \boldsymbol{I} \otimes \boldsymbol{I} \otimes \boldsymbol{I} \\
&\boldsymbol{I} \otimes \boldsymbol{\sigma}_3 \otimes \boldsymbol{\sigma}_3 \otimes \boldsymbol{I} \otimes \dots \otimes \boldsymbol{I} \otimes \boldsymbol{I} \otimes \boldsymbol{I} \\
&\dots \\
&\boldsymbol{I} \otimes \boldsymbol{I} \otimes \boldsymbol{I} \otimes \boldsymbol{I} \otimes \dots \otimes \boldsymbol{I} \otimes \boldsymbol{\sigma}_3 \otimes \boldsymbol{\sigma}_3 \\
&\boldsymbol{\sigma}_1 \otimes \boldsymbol{\sigma}_1 \otimes \boldsymbol{\sigma}_1 \otimes \dots \otimes \boldsymbol{\sigma}_1 \otimes \boldsymbol{\sigma}_1 \otimes \boldsymbol{\sigma}_1 \tag{4.182}
\end{aligned}
$$

a) Show that $|\psi\rangle_n$ is an eigenstate of the operator
$$
(\boldsymbol{\sigma}_1 + i\boldsymbol{\sigma}_2)^{\otimes n} + (\boldsymbol{\sigma}_1 - i\boldsymbol{\sigma}_2)^{\otimes n} , \tag{4.183}
$$
and compute its eigenvalue.

<!-- Page 69 -->
b) If we believe in local hidden variables, then we believe that, for each of the $n$ qubits, both $\boldsymbol{\sigma}_1$ and $\boldsymbol{\sigma}_2$ have definite values once the hidden variables are specified. If so, then what can we say about the modulus of $(\boldsymbol{\sigma}_1 + i\boldsymbol{\sigma}_2)^{\otimes n}$ or $(\boldsymbol{\sigma}_1 - i\boldsymbol{\sigma}_2)^{\otimes n}$, assuming definite values for the hidden variables?

c) From (b), derive an upper bound on
$$
\frac{1}{2} \left| (\boldsymbol{\sigma}_1 + i\boldsymbol{\sigma}_2)^{\otimes n} + (\boldsymbol{\sigma}_1 - i\boldsymbol{\sigma}_2)^{\otimes n} \right| \tag{4.184}
$$
that follows from the local hidden-variable hypothesis.

d) Compare with (a). What would Einstein say?

## 4.9 Entanglement manipulation

a) Twenty-five players on the New York Yankees, and twenty-five players on the San Diego Padres, want to share a 50-qubit cat state. The Yankees prepare a 26-qubit cat state, and give one of the qubits to Alice; so do the Padres. Now Alice is to sew the states together and prepare the 50-qubit state. What should she do? [Hint: Think about stabilizers.]

b) After joining the Yankees, Alice assumed custody of one of the qubits in their 25-qubit cat state. But today she has been traded! Alice is ordered to pull her qubit out of the cat state, leaving an undamaged 24-qubit cat state for the other players. What should she do? [Hint: Think about stabilizers.]

## 4.10 Peres-Horodecki criterion in $d$ dimensions

Recall that a *Werner state* of a pair of qubits can be expressed as
$$
\boldsymbol{\rho}(\lambda) = \lambda |\phi^+\rangle\langle\phi^+| + \frac{1}{4}(1 - \lambda)\boldsymbol{I} , \tag{4.185}
$$
and that the *partial transpose* $\boldsymbol{\rho}_{AB}^{PT}$ of a bipartite density operator $\boldsymbol{\rho}_{AB}$ is defined as
$$
\boldsymbol{\rho}_{AB}^{PT} \equiv (\boldsymbol{I}_A \otimes T_B)(\boldsymbol{\rho}_{AB}) \tag{4.186}
$$
where $T$ is the transpose operation that acts in the computational basis $\{|i\rangle\}$ as
$$
T(|i\rangle\langle j|) = |j\rangle\langle i| . \tag{4.187}
$$
We saw in class that the partial transpose of the Werner state $\boldsymbol{\rho}(\lambda)$ is negative for $\lambda > 1/3$; therefore, by the *Peres-Horodecki criterion*, the Werner state is inseparable for $\lambda > 1/3$.

<!-- Page 70 -->
a) One natural way to generalize the Werner state to a pair of $d$-dimensional systems is to consider
$$
\boldsymbol{\rho}_\Phi(\lambda) = \lambda |\Phi\rangle\langle\Phi| + \frac{1}{d^2}(1 - \lambda)\boldsymbol{I} , \tag{4.188}
$$
where $|\Phi\rangle$ is the maximally entangled state
$$
|\Phi\rangle = \frac{1}{\sqrt{d}} \sum_{i=1}^d |i\rangle \otimes |i\rangle . \tag{4.189}
$$
Show that
$$
(|\Phi\rangle\langle\Phi|)^{PT} = \frac{1}{d} (\boldsymbol{I} - 2\boldsymbol{E}_{\text{antisym}}) , \tag{4.190}
$$
where $\boldsymbol{E}_{\text{antisym}}$ is the projector onto the space that is antisymmetric under interchange of the two systems $A$ and $B$.

b) For what values of $\lambda$ does the state $\boldsymbol{\rho}_\Phi(\lambda)$ have a negative partial transpose?

c) If the Werner state for two qubits is chosen to be
$$
\boldsymbol{\rho}(\lambda) = \lambda |\psi^-\rangle\langle\psi^-| + \frac{1}{4}(1 - \lambda)\boldsymbol{I} , \tag{4.191}
$$
then another natural way to generalize the Werner state to a pair of $d$-dimensional systems is to consider
$$
\boldsymbol{\rho}_{\text{anti}}(\lambda) = \lambda \left(\frac{1}{\frac{1}{2}d(d-1)}\right) \boldsymbol{E}_{\text{antisym}} + \frac{1}{d^2}(1 - \lambda)\boldsymbol{I} . \tag{4.192}
$$
For what values of $\lambda$ does $\boldsymbol{\rho}_{\text{anti}}(\lambda)$ have a negative partial transpose?
