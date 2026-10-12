# Section 4.3: More Bell inequalities [PDF Pages 17-27]

<!-- ============================================================ -->
<!-- Source: chap4.pdf, Physical Pages: 17-27                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 17 -->
## 4.3 More Bell inequalities

### 4.3.1 CHSH inequality

Experimental tests of Einstein locality typically are based on another form of the Bell inequality, which applies to a situation in which Alice can measure either one of two observables $a$ and $a'$, while Bob can measure either $b$ or $b'$. Suppose that the observables $a, a', b, b'$ take values in $\{\pm 1\}$, and are functions of hidden random variables.

If $a, a' = \pm 1$, it follows that either $a + a' = 0$, in which case $a - a' = \pm 2$, or else $a - a' = 0$, in which case $a + a' = \pm 2$; therefore
$$
C \equiv (a + a')b + (a - a')b' = \pm 2.
\tag{4.31}
$$
(Here is where the local hidden-variable assumption sneaks in --- we have imagined that values in $\{\pm 1\}$ can be assigned simultaneously to all four observables, even though it is impossible to measure both of $a$ and $a'$, or both of $b$ and $b'$.) Evidently
$$
|\langle C \rangle| \le \langle |C| \rangle = 2,
\tag{4.32}
$$
so that
$$
|\langle ab \rangle + \langle a'b \rangle + \langle ab' \rangle - \langle a'b' \rangle| \le 2.
\tag{4.33}
$$

<!-- Page 18 -->
This result is called the CHSH inequality (for Clauser-Horne-Shimony-Holt). It holds for any random variables $a, a', b, b'$ taking values in $\pm 1$ that are governed by a joint probability distribution.

To see that quantum mechanics violates the CHSH inequality, let $a, a'$ denote the Hermitian operators
$$
a = \vec{\sigma}^{(A)} \cdot \hat{a}, \quad a' = \vec{\sigma}^{(A)} \cdot \hat{a}',
\tag{4.34}
$$
acting on a qubit in Alice's possession, where $\hat{a}, \hat{a}'$ are unit 3-vectors. Similarly, let $b, b'$ denote
$$
b = \vec{\sigma}^{(B)} \cdot \hat{b}, \quad b' = \vec{\sigma}^{(B)} \cdot \hat{b}',
\tag{4.35}
$$
acting on Bob's qubit. Each observable has eigenvalues $\pm 1$ so that an outcome of a measurement of the observable takes values in $\pm 1$.

Recall that if Alice and Bob share the maximally-entangled state $|\psi^-\rangle$, then
$$
\langle\psi^-| (\vec{\sigma}^{(A)} \cdot \hat{a})(\vec{\sigma}^{(B)} \cdot \hat{b}) |\psi^-\rangle = -\hat{a} \cdot \hat{b} = -\cos\theta,
\tag{4.36}
$$
where $\theta$ is the angle between $\hat{a}$ and $\hat{b}$. Consider the case where $\hat{a}', \hat{b}, \hat{a}, \hat{b}'$ are coplanar and separated by successive $45^\circ$ angles, so that the quantum-mechanical predictions are
$$
\begin{aligned}
\langle ab \rangle &= \langle a'b \rangle = \langle ab' \rangle = -\cos\frac{\pi}{4} = -\frac{1}{\sqrt{2}}, \\
\langle a'b' \rangle &= -\cos\frac{3\pi}{4} = \frac{1}{\sqrt{2}}.
\end{aligned}
\tag{4.37}
$$
The CHSH inequality then becomes
$$
4 \cdot \frac{1}{\sqrt{2}} = 2\sqrt{2} \le 2,
\tag{4.38}
$$
which is clearly violated by the quantum-mechanical prediction.

### 4.3.2 Maximal violation

In fact the case just considered provides the largest possible quantum-mechanical violation of the CHSH inequality, as we can see by the following argument. Suppose that $a, a', b, b'$ are Hermitian operators with eigenvalues $\pm 1$, so that
$$
a^2 = a'^2 = b^2 = b'^2 = I,
\tag{4.39}
$$

<!-- Page 19 -->
and suppose that "Alice's observables" $a, a'$ commute with "Bob's observables" $b, b'$:
$$
0 = [a, b] = [a, b'] = [a', b] = [a', b'].
\tag{4.40}
$$
Defining
$$
C = ab + a'b + ab' - a'b',
\tag{4.41}
$$
we evaluate
$$
C^2 = \begin{array}{cccc}
I & +aa' & +bb' & -aa'bb' \\
+a'a & +I & +a'abb' & -bb' \\
+b'b & +aa'b'b & +I & -aa' \\
-a'ab'b & -b'b & -a'a & +I
\end{array},
\tag{4.42}
$$
using eq. (4.39). All the quadratic terms cancel pairwise, so that we are left with
$$
\begin{aligned}
C^2 &= 4I - aa'bb' + a'abb' + aa'b'b - a'ab'b \\
&= 4I - [a, a'][b, b'].
\end{aligned}
\tag{4.43}
$$
Now recall that the sup norm $\|M\|_{\sup}$ of a bounded operator $M$ is defined by
$$
\|M\|_{\sup} = \sup_{|\psi\rangle} \left(\frac{\|M|\psi\rangle\|}{\||\psi\rangle\|}\right);
\tag{4.44}
$$
that is, the sup norm of $M$ is the maximum eigenvalue of $\sqrt{M^\dagger M}$. It is easy to verify that the sup norm has the properties
$$
\begin{aligned}
\|MN\|_{\sup} &\le \|M\|_{\sup} \cdot \|N\|_{\sup}, \\
\|M + N\|_{\sup} &\le \|M\|_{\sup} + \|N\|_{\sup}.
\end{aligned}
\tag{4.45}
$$
A Hermitian operator with eigenvalues $\pm 1$ has unit sup norm, so that
$$
\|C^2\|_{\sup} \le 4 + 4\|a\|_{\sup} \cdot \|a'\|_{\sup} \cdot \|b\|_{\sup} \cdot \|b'\|_{\sup} = 8.
\tag{4.46}
$$
Because $C$ is Hermitian,
$$
\|C^2\|_{\sup} = \|C\|_{\sup}^2,
\tag{4.47}
$$
and therefore
$$
\|C\|_{\sup} \le 2\sqrt{2},
\tag{4.48}
$$
which is known as Cirel'son's inequality.

<!-- Page 20 -->
The CHSH inequality is the statement $|\langle C \rangle| \le 2$. Quantum mechanically, the absolute value of the expectation value of the Hermitian operator $C$ can be no larger than its largest eigenvalue,
$$
|\langle C \rangle| \le \|C\|_{\sup} \le 2\sqrt{2}.
\tag{4.49}
$$
We saw that this upper bound is saturated in the case where $a', b, a, b'$ are separated by successive $45^\circ$ angles. Thus the violation of the CHSH inequality that we found is the largest violation allowed by quantum theory.

### 4.3.3 Quantum strategies outperform classical strategies

The CHSH inequality is a limitation on the strength of the correlations between the two parts of a bipartite classical system, and the Cirel'son inequality is a limitation on the strength of the correlations between the two parts of a bipartite quantum system. We can deepen our appreciation of how quantum correlations differ from classical correlations by considering a game for which quantum strategies outperform classical strategies.

Alice and Bob are playing a game with Charlie. Charlie prepares two bits $x, y \in \{0, 1\}$; then he sends $x$ to Alice and $y$ to Bob. After receiving the input bit $x$, Alice is to produce an output bit $a \in \{0, 1\}$, and after receiving $y$, Bob is to produce output bit $b \in \{0, 1\}$. But Alice and Bob are not permitted to communicate, so that Alice does not know $y$ and Bob does not know $x$.

Alice and Bob win the game if their output bits are related to the input bits according to
$$
a \oplus b = x \land y,
\tag{4.50}
$$
where $\oplus$ denotes the sum modulo 2 (the XOR gate) and $\land$ denotes the product (the AND gate). Can Alice and Bob find a strategy that enables them to win the game every time, no matter how Charlie chooses the input bits?

No, it is easy to see that there is no such strategy. Let $a_0, a_1$ denote the value of Alice's output if her input is $x = 0, 1$ and let $b_0, b_1$ denote Bob's output if his input is $y = 0, 1$. For Alice and Bob to win for all possible inputs, their output bits must satisfy
$$
\begin{aligned}
a_0 \oplus b_0 &= 0, \\
a_0 \oplus b_1 &= 0, \\
a_1 \oplus b_0 &= 0, \\
a_1 \oplus b_1 &= 1.
\end{aligned}
\tag{4.51}
$$

<!-- Page 21 -->
But this is impossible, since by summing the four equations we obtain $0 = 1$.

Suppose that Charlie generates the input bits at random. Then there is a very simple strategy that enables Alice and Bob to win the game three times out of four: they always choose the output $a = b = 0$ so that they lose only if the input is $x = y = 1$. The CHSH inequality can be regarded as the statement that, if Alice and Bob share no quantum entanglement, then there is no better strategy.

To connect this statement with our previous formulation of the CHSH inequality, define random variables taking values $\pm 1$ as
$$
\begin{aligned}
a &= (-1)^{a_0}, & a' &= (-1)^{a_1}, \\
b &= (-1)^{b_0}, & b' &= (-1)^{b_1}.
\end{aligned}
\tag{4.52}
$$
Then the CHSH inequality says that for any joint probability distribution governing $a, a', b, b' \in \{\pm 1\}$, the expectation values satisfy
$$
\langle ab \rangle + \langle ab' \rangle + \langle a'b \rangle - \langle a'b' \rangle \le 2.
\tag{4.53}
$$
Furthermore, if we denote by $p_{xy}$ the probability that eq. (4.51) is satisfied when the input bits are $(x, y)$, then
$$
\begin{aligned}
\langle ab \rangle &= 2p_{00} - 1, \\
\langle ab' \rangle &= 2p_{01} - 1, \\
\langle a'b \rangle &= 2p_{10} - 1, \\
\langle a'b' \rangle &= 1 - 2p_{11};
\end{aligned}
\tag{4.54}
$$
for example $\langle ab \rangle = p_{00} - (1 - p_{00}) = 2p_{00} - 1$, because the value of $ab$ is $+1$ when Alice and Bob win and $-1$ when they lose. The CHSH inequality eq. (4.53) becomes
$$
2(p_{00} + p_{01} + p_{10} + p_{11}) - 4 \le 2,
\tag{4.55}
$$
or
$$
\langle p \rangle \equiv \frac{1}{4}(p_{00} + p_{01} + p_{10} + p_{11}) \le \frac{3}{4},
\tag{4.56}
$$
where $\langle p \rangle$ denotes the probability of winning averaged over a uniform ensemble for the input bits. Thus, if the input bits are random, Alice and Bob cannot attain a probability of winning higher than $3/4$.

It is worthwhile to consider how the assumption that Alice and Bob take actions governed by "local hidden variables" limits their success in playing the game. Although Alice and Bob do not share any quantum entanglement, they are permitted to share a table of random numbers that

<!-- Page 22 -->
they may consult to produce their output bits. Thus we may imagine that hidden variables drawn from an ensemble of possible values guide Alice and Bob to make correlated decisions. These correlations are limited by locality --- Alice does not know Bob's input and Bob does not know Alice's. In fact, we have learned that for playing this game their shared randomness is of no value --- their best strategy does not use the shared randomness at all.

But if Alice and Bob share quantum entanglement, they can devise a better strategy. Based on the value of her input bit, Alice decides to measure one of two Hermitian observables with eigenvalues $\pm 1$: $a$ if $x = 0$ and $a'$ if $x = 1$. Similarly, Bob measures $b$ if $y = 0$ and $b'$ if $y = 1$. Then the quantum-mechanical expectation values of these observables satisfy the Cirel'son inequality
$$
\langle ab \rangle + \langle ab' \rangle + \langle a'b \rangle - \langle a'b' \rangle \le 2\sqrt{2},
\tag{4.57}
$$
and the probability that Alice and Bob win the game is constrained by
$$
2(p_{00} + p_{01} + p_{10} + p_{11}) - 4 \le 2\sqrt{2},
\tag{4.58}
$$
or
$$
\langle p \rangle \equiv \frac{1}{4}(p_{00} + p_{01} + p_{10} + p_{11}) \le \frac{1}{2} + \frac{1}{2\sqrt{2}} \approx .853.
\tag{4.59}
$$
Furthermore, we have seen that this inequality can be saturated if Alice and Bob share a maximally entangled state of two qubits, and the observables $a, a', b, b'$ are chosen appropriately.

Thus we have found that Alice and Bob can play the game more successfully with quantum entanglement than without it. At least for this purpose, shared quantum entanglement is a more powerful resource than shared classical randomness. But even the power brought by entanglement has limits, limits embodied by the Cirel'son inequality.

### 4.3.4 All entangled pure states violate Bell inequalities

Separable states do not violate Bell inequalities. For example, in the case of a separable pure state, if $a$ is an observable acting on Alice's qubit, and $b$ is an observable acting on Bob's, then
$$
\langle ab \rangle = \langle a \rangle \langle b \rangle.
\tag{4.60}
$$
No Bell-inequality violation can occur, because we have already seen that a (local) hidden-variable theory does exist that correctly reproduces the predictions of quantum theory for a pure state of a single qubit. A general

<!-- Page 23 -->
separable state is just a probabilistic mixture of separable pure states, so that the correlations between the subsystems are entirely classical, and the Bell inequalities apply.

On the other hand, we have seen that a maximally entangled state such as $|\psi^-\rangle$ is Bell-inequality violating. But what about pure states that are only partially entangled such as
$$
|\phi\rangle = \alpha |00\rangle + \beta |11\rangle?
\tag{4.61}
$$
Any pure state of two qubits can be expressed this way in the Schmidt basis; with suitable phase conventions, $\alpha$ and $\beta$ are real and nonnegative.

Suppose that Alice and Bob both measure along an axis in the $x$-$z$ plane, so that their observables are
$$
\begin{aligned}
a &= \sigma_3^{(A)} \cos\theta_A + \sigma_1^{(A)} \sin\theta_A, \\
b &= \sigma_3^{(B)} \cos\theta_B + \sigma_1^{(B)} \sin\theta_B.
\end{aligned}
\tag{4.62}
$$
The state $|\phi\rangle$ has the properties
$$
\begin{aligned}
\langle\phi| \sigma_3 \otimes \sigma_3 |\phi\rangle &= 1, \quad &\langle\phi| \sigma_1 \otimes \sigma_1 |\phi\rangle &= 2\alpha\beta, \\
\langle\phi| \sigma_3 \otimes \sigma_1 |\phi\rangle &= 0 &= \langle\phi| \sigma_1 \otimes \sigma_3 |\phi\rangle,
\end{aligned}
\tag{4.63}
$$
so that the quantum-mechanical expectation value of $ab$ is
$$
\langle ab \rangle = \langle\phi| ab |\phi\rangle = \cos\theta_A \cos\theta_B + 2\alpha\beta \sin\theta_A \sin\theta_B
\tag{4.64}
$$
(and we recover $\cos(\theta_A - \theta_B)$ in the maximally entangled case $\alpha = \beta = 1/\sqrt{2}$). Now let us consider, for simplicity, the (nonoptimal!) special case
$$
\theta_A = 0, \quad \theta_A' = \frac{\pi}{2}, \quad \theta_B' = -\theta_B,
\tag{4.65}
$$
so that the quantum predictions are:
$$
\begin{aligned}
\langle ab \rangle &= \cos\theta_B = \langle ab' \rangle, \\
\langle a'b \rangle &= 2\alpha\beta \sin\theta_B = -\langle a'b' \rangle.
\end{aligned}
\tag{4.66}
$$
Plugging into the CHSH inequality, we obtain
$$
|\cos\theta_B - 2\alpha\beta \sin\theta_B| \le 1,
\tag{4.67}
$$
and we easily see that violations occur for $\theta_B$ close to $0$ or $\pi$. Expanding to linear order in $\theta_B$, the left-hand side is
$$
\simeq 1 - 2\alpha\beta\theta_B,
\tag{4.68}
$$

<!-- Page 24 -->
which surely exceeds 1 for $\alpha\beta > 0$ and $\theta_B$ negative and small.

We have shown that *any* entangled pure state of two qubits violates some Bell inequality. It is not hard to generalize the argument to an arbitrary bipartite pure state. For bipartite pure states, then, "entangled" is equivalent to "Bell-inequality violating." For bipartite mixed states, however, we will see later that the situation is more subtle.

### 4.3.5 Photons

Experiments that test the Bell inequality usually are done with entangled photons, not with spin-$\frac{1}{2}$ objects. What are the quantum-mechanical predictions for photons?

Recall from §2.2.2 that for a photon traveling in the $\hat{z}$ direction, we use the notation $|x\rangle, |y\rangle$ for the states that are linearly polarized along the $x$ and $y$ axes respectively. In terms of these basis states, the states that are linearly polarized along "horizontal" and "vertical" axes that are rotated by angle $\theta$ relative to the $x$ and $y$ axes can be expressed as
$$
|H(\theta)\rangle = \begin{pmatrix} \cos\theta \\ \sin\theta \end{pmatrix}, \quad |V(\theta)\rangle = \begin{pmatrix} -\sin\theta \\ \cos\theta \end{pmatrix}.
\tag{4.69}
$$
We can construct a $2\times 2$ matrix whose eigenstates are $|H(\theta)\rangle$ and $|V(\theta)\rangle$, with respective eigenvalues $\pm 1$; it is
$$
\tau(\theta) \equiv |H(\theta)\rangle\langle H(\theta)| - |V(\theta)\rangle\langle V(\theta)| = \begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix}.
\tag{4.70}
$$
The generator of rotations about the $\hat{z}$ axis is $J = \sigma_2$, and the eigenstates of $J$ with eigenvalues $\pm 1$ are the circularly polarized states
$$
|+\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 \\ i \end{pmatrix}, \quad |-\rangle = \frac{1}{\sqrt{2}} \begin{pmatrix} i \\ 1 \end{pmatrix}.
\tag{4.71}
$$
Suppose that an excited atom emits two photons that come out back to back, with vanishing angular momentum and even parity. The two-photon states
$$
\begin{array}{c}
|+\rangle_A |-\rangle_B \\
|-\rangle_A |+\rangle_B
\end{array}
\tag{4.72}
$$
are invariant under rotations about $\hat{z}$. The photons have opposite values of $J_z$, but the same *helicity* (angular-momentum along the axis of propagation), since they are propagating in opposite directions. Under a

<!-- Page 25 -->
reflection in the $y$-$z$ plane, the polarization states are modified according to
$$
|x\rangle \to -|x\rangle, \quad |y\rangle \to |y\rangle,
\tag{4.73}
$$
or
$$
|+\rangle \to +i |-\rangle, \quad |-\rangle \to -i |+\rangle;
\tag{4.74}
$$
therefore, the parity eigenstates are *entangled* states
$$
\frac{1}{\sqrt{2}} (|+\rangle_A |-\rangle_B \pm |-\rangle_A |+\rangle_B).
\tag{4.75}
$$
The state with $J_z = 0$ and even parity, then, expressed in terms of the linear polarization states, is
$$
\begin{aligned}
&-\frac{i}{\sqrt{2}} (|+-\rangle_{AB} + |-+\rangle_{AB}) \\
&= \frac{1}{\sqrt{2}} (|xx\rangle_{AB} + |yy\rangle_{AB}) \equiv |\phi^+\rangle_{AB}.
\end{aligned}
\tag{4.76}
$$
Because of invariance under rotations about $\hat{z}$, the state has this form irrespective of how we orient the $x$ and $y$ axes.

Alice or Bob can use a polarization analyzer to project the polarization state of a photon onto the basis $\{|H(\theta)\rangle, |V(\theta)\rangle\}$, and hence measure $\tau(\theta)$. For two photons in the state $|\phi^+\rangle$, if Alice orients her polarizer with angle $\theta_A$ and Bob with angle $\theta_B$, then the correlations of their measurement outcomes are encoded in the expectation value
$$
\langle\phi^+| \tau^{(A)}(\theta_A) \tau^{(B)}(\theta_B) |\phi^+\rangle.
\tag{4.77}
$$
Using rotational invariance:
$$
\begin{aligned}
&= \langle\phi^+| \tau^{(A)}(0) \tau^{(B)}(\theta_B - \theta_A) |\phi^+\rangle \\
&= \frac{1}{2} \langle x| \tau^{(B)}(\theta_B - \theta_A) |x\rangle - \frac{1}{2} \langle y| \tau^{(B)}(\theta_B - \theta_A) |y\rangle \\
&= \cos 2(\theta_B - \theta_A).
\end{aligned}
\tag{4.78}
$$
Recall that for the measurement of qubits on the Bloch sphere, we found the similar expression $\cos\theta$, where $\theta$ is the angle between Alice's polarization axis and Bob's. Here we have $\cos 2\theta$ instead, because photons have spin-1 rather than spin-$\frac{1}{2}$.

If Alice measures one of the two observables $a = \tau^{(A)}(\theta_A)$ or $a' = \tau^{(A)}(\theta_A')$ and Bob measures either $b = \tau^{(B)}(\theta_B)$ or $b' = \tau^{(B)}(\theta_B')$, then under the local hidden-variable assumption the CHSH inequality applies.

<!-- Page 26 -->
If we plug in the quantum predictions for the expectation values, we obtain
$$
|\cos 2(\theta_B - \theta_A) + \cos 2(\theta_B - \theta_A') + \cos 2(\theta_B' - \theta_A) - \cos 2(\theta_B' - \theta_A')| \le 2.
\tag{4.79}
$$
The maximal violation that saturates Cirel'son's inequality --- left-hand side equal to $2\sqrt{2}$ --- occurs when $\theta_A', \theta_B, \theta_A$ and $\theta_B'$ are separated by successive $22\frac{1}{2}^\circ$ angles, so that
$$
\begin{aligned}
\frac{1}{\sqrt{2}} &= \cos 2(\theta_B - \theta_A) = \cos 2(\theta_B - \theta_A') \\
&= \cos 2(\theta_B' - \theta_A) = -\cos 2(\theta_B' - \theta_A').
\end{aligned}
\tag{4.80}
$$

### 4.3.6 Experiments and loopholes

*Locality loophole.* Experiments with entangled pairs of photons have tested the CHSH inequality in the form eq. (4.79). The experiments confirm the quantum predictions, and demonstrate convincingly that the CHSH inequality is violated. These experiments, then, seem to show that Nature cannot be accurately described by a local hidden-variable theory.

Or do they? A skeptic might raise objections. For example, in the derivation of the CHSH inequality, we assumed that after Alice decides to measure either $a$ or $a'$, no information about Alice's decision reaches Bob's detector before Bob measures (and likewise, we assumed that if Bob measures first, no information about Bob's decision reaches Alice before she measures). Otherwise, the marginal probability distribution for Bob's outcomes could be updated after Alice's measurement and before Bob's, so that the CHSH inequality need not apply. The assumption that no such update can occur is justified by relativistic causality if Alice's decision and measurement are events spacelike separated from Bob's decision and measurement. The skeptic would insist that the experiment fulfill this condition, which is called the *locality loophole*.

In 1982, Aspect and collaborators conducted an experiment that addressed the locality loophole. Two entangled photons were produced in the decay of an excited calcium atom, and each photon was directed by a switch to one of two polarization analyzers, chosen pseudo-randomly. The photons were detected about 12m apart, corresponding to a light travel time of about 40 ns. This time was considerably longer than either the cycle time of the switch, or the difference in the times of arrival of the two photons. Therefore the "decision" about which observable to measure was made after the photons were already in flight, and the events that selected the axes for the measurement of photons $A$ and $B$ were spacelike

<!-- Page 27 -->
separated. The results were consistent with the quantum predictions, and violated the CHSH inequality by five standard deviations. Since Aspect, many other experiments have confirmed this finding, including ones in which detectors $A$ and $B$ are kilometers apart.

*Detection loophole.* Another objection that the skeptic might raise is called the *detection loophole*. In experiments with photons, the detection efficiency is low. Most entangled photon pairs do not result in detections at both $A$ and $B$. Among the things that can go wrong: a photon might be absorbed before reaching the detector, a photon might miss the detector, or a photon might arrive in the detector but fail to trigger it. Data is accepted by the experiment only when two photons are detected in coincidence, and in testing the CHSH inequality, we must assume that the data collected is a fair sample of all the entangled pairs.

But, what if the local hidden variables govern not just *what* polarization state is detected, but also *whether* the detector fires at all? Then the data collected might be a biased sample, and the CHSH inequality need not apply.

In Exercise 4.??, we will show that the detection loophole can be closed if the photons are detected with an efficiency above 82.84%. Current experiments with photons don't approach the necessary efficiency. Experiments that use ion traps have tested the CHSH inequality with detection efficiency close to 100%, but these experiments do not address the locality loophole. No experiment that simultaneously closes the locality and detection loopholes has yet been done.

*Free-will loophole.* Suppose that an experiment is done in which the photon detection efficiency is perfect, and in which Alice and Bob appear to make spacelike-separated decisions. A skeptic might still resist the conclusion that local hidden-variable theories are ruled out, by invoking the *free-will loophole*. Conceivably, the decisions that Alice and Bob make about what to measure are themselves governed by the local hidden variables. Then their decisions might be correlated with the values of the hidden variables that determine the measurement outcomes, so that they are unable to obtain a fair sample of the distribution of the hidden variables, and the CHSH inequality might be violated.

All of us have to decide for ourselves how seriously to take this objection.
