# Section 10.6: Accessible Information [PDF Pages 46-57]

<!-- ============================================================ -->
<!-- Source: chap10.pdf, Physical Pages: 46-57                     -->
<!-- Transcribed: 2026-10-12                                       -->
<!-- ============================================================ -->

<!-- Page 46 -->
## 10.6 Accessible Information

### 10.6.1 How much can we learn from a measurement?

Consider a game played by Alice and Bob. Alice prepares a quantum state drawn from the ensemble $\mathcal{E} = \{\boldsymbol{\rho}(x), p(x)\}$ and sends the state to Bob. Bob knows this ensemble, but not the particular state that Alice chose to send. After receiving the state, Bob performs a POVM with elements $\{\boldsymbol{E}(y)\} \equiv \boldsymbol{E}$, hoping to find out as much as he can about what Alice sent. The conditional probability that Bob obtains outcome $y$ if Alice sent $\boldsymbol{\rho}(x)$ is $p(y|x) = \mathrm{tr}\left(\boldsymbol{E}(y)\boldsymbol{\rho}(x)\right)$, and the joint distribution governing Alice's preparation and Bob's measurement is $p(x, y) = p(y|x)p(x)$.

Before he measures, Bob's ignorance about Alice's state is quantified by $H(X)$, the number of "bits per letter" needed to specify $x$; after he measures his ignorance is reduced to $H(X|Y) = H(XY) - H(Y)$. The improvement in Bob's knowledge achieved by the measurement is Bob's *information gain*, the mutual information
$$
I(X; Y) = H(X) - H(X|Y).
$$ {#eq-10.204}

Bob's best strategy (his *optimal measurement*) maximizes this information gain. The best information gain Bob can achieve,
$$
\mathrm{Acc}(\mathcal{E}) = \max_{\boldsymbol{E}} I(X; Y),
$$ {#eq-10.205}
is a property of the ensemble $\mathcal{E}$ called the *accessible information* of $\mathcal{E}$.

If the states $\{\boldsymbol{\rho}(x)\}$ are mutually orthogonal they are perfectly distinguishable. Bob can identify Alice's state with certainty by choosing $\boldsymbol{E}(x)$ to be the projector onto the support of $\boldsymbol{\rho}(x)$; Then $p(y|x) = \delta_{x,y} = p(x|y)$, hence $H(X|Y) = \langle -\log p(x|y)\rangle = 0$ and $\mathrm{Acc}(\mathcal{E}) = H(X)$. Bob's task is more challenging if Alice's states are not orthogonal. Then no measurement will identify the state perfectly, so $H(X|Y)$ is necessarily positive and $\mathrm{Acc}(\mathcal{E}) < H(X)$.

<!-- Page 47 -->
Though there is no simple general formula for the accessible information of an ensemble, we can derive a useful upper bound, called the *Holevo bound*. For the special case of an ensemble of pure states $\mathcal{E} = \{|\varphi(x)\rangle, p(x)\}$, the Holevo bound becomes
$$
\mathrm{Acc}(\mathcal{E}) \le H(\boldsymbol{\rho}), \quad \text{where} \quad \boldsymbol{\rho} = \sum_x p(x) |\varphi(x)\rangle\langle\varphi(x)|,
$$ {#eq-10.206}
and a sharper statement is possible for an ensemble of mixed states, as we will see. Since the entropy for a quantum system with dimension $d$ can be no larger than $\log d$, the Holevo bound asserts that Alice, by sending $n$ qubits to Bob ($d = 2^n$) can convey no more than $n$ bits of information. This is true even if Bob performs a sophisticated collective measurement on all the qubits at once, rather than measuring them one at a time.

Therefore, if Alice wants to convey classical information to Bob by sending qubits, she can do no better than treating the qubits as though they were classical, sending each qubit in one of the two orthogonal states $\{|0\rangle, |1\rangle\}$ to transmit one bit. This statement is not so obvious. Alice might try to stuff more classical information into a single qubit by sending a state chosen from a large alphabet of pure single-qubit signal states, distributed uniformly on the Bloch sphere. But the enlarged alphabet is to no avail, because as the number of possible signals increases the signals also become less distinguishable, and Bob is not able to extract the extra information Alice hoped to deposit in the qubit.

If we can send information more efficiently by using an alphabet of mutually orthogonal states, why should we be interested in the accessible information for an ensemble of non-orthogonal states? There are many possible reasons. Perhaps Alice finds it easier to send signals, like coherent states, which are imperfectly distinguishable rather than mutually orthogonal. Or perhaps Alice sends signals to Bob through a noisy channel, so that signals which are orthogonal when they enter the channel are imperfectly distinguishable by the time they reach Bob.

The accessible information game also arises when an experimental physicist tries to measure an unknown classical force using a quantum system as a probe. For example, to measure the $z$-component of a magnetic field, we may prepare a spin-$\frac{1}{2}$ particle pointing in the $x$-direction; the spin precesses for time $t$ in the unknown field, producing an ensemble of possible final states (which will be an ensemble of mixed states if the initial preparation is imperfect, or if decoherence occurs during the experiment). The more information we can gain about the final state of the spin, the more accurately we can determine the value of the magnetic field.

### 10.6.2 Holevo bound

Recall that quantum mutual information obeys monotonicity --- if a quantum channel maps $B$ to $B'$, then $I(A; B) \ge I(A; B')$. We derive the Holevo bound by applying monotonicity of mutual information to the accessible information game. We will suppose that Alice records her chosen state in a classical register $X$ and Bob likewise records his measurement outcome in another register $Y$, so that Bob's information gain is the mutual information $I(X; Y)$ of the two registers. After Alice's preparation of her system $A$, the joint state of $XA$ is
$$
\boldsymbol{\rho}_{XA} = \sum_x p(x) |x\rangle\langle x| \otimes \boldsymbol{\rho}(x).
$$ {#eq-10.207}

<!-- Page 48 -->
Bob's measurement is a quantum channel mapping $A$ to $AY$ according to
$$
\boldsymbol{\rho}(x) \mapsto \sum_y \boldsymbol{M}(y)\boldsymbol{\rho}(x)\boldsymbol{M}(y)^\dagger \otimes |y\rangle\langle y|,
$$ {#eq-10.208}
where $\boldsymbol{M}(y)^\dagger \boldsymbol{M}(y) = \boldsymbol{E}(y)$, yielding the state for $XAY$
$$
\boldsymbol{\rho}'_{XAY} = \sum_{x,y} p(x) |x\rangle\langle x| \otimes \boldsymbol{M}(y)\boldsymbol{\rho}(x)\boldsymbol{M}(y)^\dagger \otimes |y\rangle\langle y|.
$$ {#eq-10.209}
Now we have
$$
I(X; Y)_{\boldsymbol{\rho}'} \le I(X; AY)_{\boldsymbol{\rho}'} \le I(X; A)_{\boldsymbol{\rho}},
$$ {#eq-10.210}
where the subscript indicates the state in which the mutual information is evaluated; the first inequality uses strong subadditivity in the state $\boldsymbol{\rho}'$, and the second uses monotonicity under the channel mapping $\boldsymbol{\rho}$ to $\boldsymbol{\rho}'$.

The quantity $I(X; A)$ is an intrinsic property of the ensemble $\mathcal{E}$; it is denoted $\chi(\mathcal{E})$ and called the *Holevo chi* of the ensemble. We have shown that however Bob chooses his measurement his information gain is bounded above by the Holevo chi; therefore,
$$
\mathrm{Acc}(\mathcal{E}) \le \chi(\mathcal{E}) := I(X; A)_{\boldsymbol{\rho}}.
$$ {#eq-10.211}
This is the Holevo bound.

Now let's calculate $I(X; A)_{\boldsymbol{\rho}}$ explicitly. We note that
$$
\begin{aligned}
H(XA) &= -\mathrm{tr}_{XA}\left(\sum_x p(x)|x\rangle\langle x| \otimes \boldsymbol{\rho}(x) \log\left(\sum_{x'} p(x')|x'\rangle\langle x'| \otimes \boldsymbol{\rho}(x')\right)\right) \\
&= -\sum_x \mathrm{tr}_A \, p(x)\boldsymbol{\rho}(x)(\log p(x) + \log \boldsymbol{\rho}(x)) \\
&= H(X) + \sum_x p(x)H(\boldsymbol{\rho}(x)),
\end{aligned}
$$ {#eq-10.212}
and therefore
$$
H(A|X) = H(XA) - H(X) = \sum_x p(x) H(\boldsymbol{\rho}(x)).
$$ {#eq-10.213}
Using $I(X; A) = H(A) - H(A|X)$, we then find
$$
\chi(\mathcal{E}) = I(X; A) = H(\boldsymbol{\rho}_A) - \sum_x p(x) H(\boldsymbol{\rho}_A(x)) \equiv H(A)_\mathcal{E} - \langle H(A)\rangle_\mathcal{E}
$$ {#eq-10.214}
For an ensemble of pure states, $\chi$ is just the entropy of the density operator arising from the ensemble, but for an ensemble $\mathcal{E}$ of mixed states it is a strictly smaller quantity --- the difference between the entropy $H(\boldsymbol{\rho}_\mathcal{E})$ of the convex sum of signal states and the convex sum $\langle H\rangle_\mathcal{E}$ of the signal state entropies; this difference is always nonnegative because of the concavity of the entropy function (or because mutual information is nonnegative).

### 10.6.3 Monotonicity of Holevo chi

Since Holevo chi is the mutual information $I(X; A)$ of the classical register $X$ and the quantum system $A$, the monotonicity of mutual information also implies the monotonicity of $\chi$. If $\mathcal{N}: A \to A'$ is a quantum channel, then $I(X; A') \le I(X; A)$ and therefore
$$
\chi(\mathcal{E}') \le \chi(\mathcal{E}),
$$ {#eq-10.215}

<!-- Page 49 -->
where
$$
\mathcal{E} = \{\boldsymbol{\rho}(x), p(x)\} \quad \text{and} \quad \mathcal{E}' = \{\boldsymbol{\rho}'(x) = \mathcal{N}(\boldsymbol{\rho}(x)), p(x)\}.
$$ {#eq-10.216}
A channel cannot increase the Holevo chi of an ensemble.

Its monotonicity provides a further indication that $\chi(\mathcal{E})$ is a useful measure of the information encoded in an ensemble of quantum states; the decoherence described by a quantum channel can reduce this quantity, but never increases it. In contrast, the von Neumann entropy may either increase or decrease under the action of a channel. Mapping pure states to mixed states can increase $H$, but a channel might instead map the mixed states in an ensemble to a fixed pure state $|0\rangle\langle 0|$, decreasing $H$ and improving the purity of each signal state, but without improving the distinguishability of the states.

We discussed the asymptotic limit $H(\boldsymbol{\rho})$ on quantum compression per letter in §10.3.2. There we considered unitary decoding; invoking the monotonicity of Holevo chi clarifies why more general decoders cannot do better. Suppose we compress and decompress the ensemble $\mathcal{E}^{\otimes n}$ using an encoder $\mathcal{N}_e$ and a decoder $\mathcal{N}_d$, where both maps are quantum channels:
$$
\mathcal{E}^{\otimes n} \xrightarrow{\mathcal{N}_e} \tilde{\mathcal{E}}^{(n)} \xrightarrow{\mathcal{N}_d} \tilde{\mathcal{E}}'^{(n)} \approx \mathcal{E}^{\otimes n}
$$ {#eq-10.217}
The Holevo chi of the input pure-state product ensemble is additive, $\chi(\mathcal{E}^{\otimes n}) = H(\boldsymbol{\rho}^{\otimes n}) = n H(\boldsymbol{\rho})$, and $\chi$ of a $d$-dimensional system is no larger than $\log_2 d$; therefore if the ensemble $\tilde{\mathcal{E}}^{(n)}$ is compressed to $q$ qubits per letter, then because of the monotonicity of $\chi$ the decompressed ensemble $\tilde{\mathcal{E}}'^{(n)}$ has Holevo chi per letter $\frac{1}{n}\chi(\tilde{\mathcal{E}}'^{(n)}) \le q$. If the decompressed output ensemble has high fidelity with the input ensemble, its $\chi$ per letter should nearly match the $\chi$ per letter of the input ensemble, hence
$$
q \ge \frac{1}{n}\chi(\tilde{\mathcal{E}}'^{(n)}) \ge H(\boldsymbol{\rho}) - \delta
$$ {#eq-10.218}
for any positive $\delta$ and sufficiently large $n$. We conclude that high-fidelity compression to fewer than $H(\boldsymbol{\rho})$ qubits per letter is impossible asymptotically, even when the compression and decompression maps are arbitrary channels.

### 10.6.4 Improved distinguishability through coding: an example

To better acquaint ourselves with the concept of accessible information, let's consider a single-qubit example. Alice prepares one of the three possible pure states
$$
\begin{aligned}
|\varphi_1\rangle &= |\!\uparrow_{\hat{n}_1}\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}, \\
|\varphi_2\rangle &= |\!\uparrow_{\hat{n}_2}\rangle = \begin{pmatrix} -\frac{1}{2} \\ \frac{\sqrt{3}}{2} \end{pmatrix}, \\
|\varphi_3\rangle &= |\!\uparrow_{\hat{n}_3}\rangle = \begin{pmatrix} -\frac{1}{2} \\ -\frac{\sqrt{3}}{2} \end{pmatrix};
\end{aligned}
$$ {#eq-10.219}
a spin-$\frac{1}{2}$ object points in one of three directions that are symmetrically distributed in the $xz$-plane. Each state has *a priori* probability $\frac{1}{3}$. Evidently, Alice's signal states are nonorthogonal:
$$
\langle\varphi_1|\varphi_2\rangle = \langle\varphi_1|\varphi_3\rangle = \langle\varphi_2|\varphi_3\rangle = -\frac{1}{2}.
$$ {#eq-10.220}

<!-- Page 50 -->
Bob's task is to find out as much as he can about what Alice prepared by making a suitable measurement. The density matrix of Alice's ensemble is
$$
\boldsymbol{\rho} = \frac{1}{3}\left(|\varphi_1\rangle\langle\varphi_1| + |\varphi_2\rangle\langle\varphi_2| + |\varphi_3\rangle\langle\varphi_3|\right) = \frac{1}{2}\boldsymbol{I},
$$ {#eq-10.221}
which has $H(\boldsymbol{\rho}) = 1$. Therefore, the Holevo bound tells us that the mutual information of Alice's preparation and Bob's measurement outcome cannot exceed 1 bit.

In fact, though, the accessible information is considerably less than the one bit allowed by the Holevo bound. In this case, Alice's ensemble has enough symmetry that it is not hard to guess the optimal measurement. Bob may choose a POVM with three outcomes, where
$$
\boldsymbol{E}_a = \frac{2}{3}(\boldsymbol{I} - |\varphi_a\rangle\langle\varphi_a|), \quad a = 1, 2, 3;
$$ {#eq-10.222}
we see that
$$
p(a|b) = \langle\varphi_b|\boldsymbol{E}_a|\varphi_b\rangle = \begin{cases}
0 & a = b, \\
\frac{1}{2} & a \neq b.
\end{cases}
$$ {#eq-10.223}
The measurement outcome $a$ *excludes* the possibility that Alice prepared $a$, but leaves equal *a posteriori* probabilities ($p = \frac{1}{2}$) for the other two states. Bob's information gain is
$$
I = H(X) - H(X|Y) = \log_2 3 - 1 = .58496.
$$ {#eq-10.224}
To show that this measurement is really optimal, we may appeal to a variation on a theorem of Davies, which assures us that an optimal POVM can be chosen with three $\boldsymbol{E}_a$'s that share the same three-fold symmetry as the three states in the input ensemble. This result restricts the possible POVM's enough so that we can check that eq.(10.222) is optimal with an explicit calculation. Hence we have found that the ensemble $\mathcal{E} = \{|\varphi_a\rangle, p_a = \frac{1}{3}\}$ has accessible information
$$
\mathrm{Acc}(\mathcal{E}) = \log_2\left(\frac{3}{2}\right) = .58496\dots
$$ {#eq-10.225}
The Holevo bound is not saturated.

Now suppose that Alice has enough cash so that she can afford to send two qubits to Bob, where again each qubit is drawn from the ensemble $\mathcal{E}$. The obvious thing for Alice to do is prepare one of the *nine* states
$$
|\varphi_a\rangle \otimes |\varphi_b\rangle, \quad a, b = 1, 2, 3,
$$ {#eq-10.226}
each with $p_{ab} = 1/9$. Then Bob's best strategy is to perform the POVM eq.(10.222) on each of the two qubits, achieving a mutual information of $.58496$ bits per qubit, as before.

But, determined to do better, Alice and Bob decide on a different strategy. Alice will prepare one of *three* two-qubit states
$$
|\Phi_a\rangle = |\varphi_a\rangle \otimes |\varphi_a\rangle, \quad a = 1, 2, 3,
$$ {#eq-10.227}
each occurring with *a priori* probability $p_a = 1/3$. Considered one-qubit at a time, Alice's choice is governed by the ensemble $\mathcal{E}$, but now her two qubits have (classical) correlations --- both are prepared the same way.

The three $|\Phi_a\rangle$'s are linearly independent, and so span a three-dimensional subspace

<!-- Page 51 -->
of the four-dimensional two-qubit Hilbert space. In Exercise 10.9, you will show that the density operator
$$
\boldsymbol{\rho} = \frac{1}{3}\left(\sum_{a=1}^3 |\Phi_a\rangle\langle\Phi_a|\right),
$$ {#eq-10.228}
has the nonzero eigenvalues $1/2, 1/4, 1/4$, so that
$$
H(\boldsymbol{\rho}) = -\frac{1}{2}\log_2\frac{1}{2} - 2\left(\frac{1}{4}\log_2\frac{1}{4}\right) = \frac{3}{2}.
$$ {#eq-10.229}
The Holevo bound requires that the accessible information *per qubit* is no more than $3/4$ bit, which is at least consistent with the possibility that we can exceed the $.58496$ bits per qubit attained by the nine-state method.

Naively, it may seem that Alice won't be able to convey as much classical information to Bob, if she chooses to send one of only three possible states instead of nine. But on further reflection, this conclusion is not obvious. True, Alice has fewer signals to choose from, but the signals are *more distinguishable*; we have
$$
\langle\Phi_a|\Phi_b\rangle = \frac{1}{4}, \quad a \neq b,
$$ {#eq-10.230}
instead of eq.(10.220). It is up to Bob to exploit this improved distinguishability in his choice of measurement. In particular, Bob will find it advantageous to perform *collective* measurements on the two qubits instead of measuring them one at a time.

It is no longer obvious what Bob's optimal measurement will be. But Bob can invoke a general procedure that, while not guaranteed optimal, is usually at least pretty good. We'll call the POVM constructed by this procedure a "pretty good measurement" (or PGM).

Consider some collection of vectors $|\tilde{\Phi}_a\rangle$ that are not assumed to be orthogonal or normalized. We want to devise a POVM that can distinguish these vectors reasonably well. Let us first construct
$$
\boldsymbol{G} = \sum_a |\tilde{\Phi}_a\rangle\langle\tilde{\Phi}_a|;
$$ {#eq-10.231}
This is a positive operator on the space spanned by the $|\tilde{\Phi}_a\rangle$'s. Therefore, on that subspace, $\boldsymbol{G}$ has an inverse, $\boldsymbol{G}^{-1}$ and that inverse has a positive square root $\boldsymbol{G}^{-1/2}$. Now we define
$$
\boldsymbol{E}_a = \boldsymbol{G}^{-1/2}|\tilde{\Phi}_a\rangle\langle\tilde{\Phi}_a|\boldsymbol{G}^{-1/2},
$$ {#eq-10.232}
and we see that
$$
\sum_a \boldsymbol{E}_a = \boldsymbol{G}^{-1/2}\left(\sum_a |\tilde{\Phi}_a\rangle\langle\tilde{\Phi}_a|\right)\boldsymbol{G}^{-1/2} = \boldsymbol{G}^{-1/2}\boldsymbol{G}\boldsymbol{G}^{-1/2} = \boldsymbol{I},
$$ {#eq-10.233}
on the span of the $|\tilde{\Phi}_a\rangle$'s. If necessary, we can augment these $\boldsymbol{E}_a$'s with one more positive operator, the projection $\boldsymbol{E}_0$ onto the orthogonal complement of the span of the $|\tilde{\Phi}_a\rangle$'s, and so construct a POVM. This POVM is the PGM associated with the vectors $|\tilde{\Phi}_a\rangle$.

In the special case where the $|\tilde{\Phi}_a\rangle$'s are orthogonal,
$$
|\tilde{\Phi}_a\rangle = \sqrt{\lambda_a}|\phi_a\rangle,
$$ {#eq-10.234}

<!-- Page 52 -->
(where the $|\phi_a\rangle$'s are orthonormal), we have
$$
\begin{aligned}
\boldsymbol{E}_a &= \sum_{b,c} (|\phi_b\rangle \lambda_b^{-1/2}\langle\phi_b|)(|\phi_a\rangle \lambda_a \langle\phi_a|)(|\phi_c\rangle \lambda_c^{-1/2}\langle\phi_c|) \\
&= |\phi_a\rangle\langle\phi_a|;
\end{aligned}
$$ {#eq-10.235}
this is the orthogonal measurement that perfectly distinguishes the $|\phi_a\rangle$'s and so clearly is optimal. If the $|\tilde{\Phi}_a\rangle$'s are linearly independent but not orthogonal, then the PGM is again an orthogonal measurement (because $n$ one-dimensional operators in an $n$-dimensional space can constitute a POVM only if mutually orthogonal --- see Exercise 3.11), but in that case the measurement may not be optimal.

In Exercise 10.9, you'll construct the PGM for the vectors $|\Phi_a\rangle$ in eq.(10.227), and you'll show that
$$
\begin{aligned}
p(a|a) &= \langle\Phi_a|\boldsymbol{E}_a|\Phi_a\rangle = \frac{1}{3}\left(1 + \frac{1}{\sqrt{2}}\right)^2 = .971405, \\
p(b|a) &= \langle\Phi_a|\boldsymbol{E}_b|\Phi_a\rangle = \frac{1}{6}\left(1 - \frac{1}{\sqrt{2}}\right)^2 = .0142977
\end{aligned}
$$ {#eq-10.236}
(for $b \neq a$). It follows that the conditional entropy of the input is
$$
H(X|Y) = .215894,
$$ {#eq-10.237}
and since $H(X) = \log_2 3 = 1.58496$, the information gain is
$$
I(X; Y) = H(X) - H(X|Y) = 1.369068,
$$ {#eq-10.238}
a mutual information of $.684534$ bits per qubit. Thus, the improved distinguishability of Alice's signals has indeed paid off --- we have exceeded the $.58496$ bits that can be extracted from a single qubit. We still didn't saturate the Holevo bound ($I \le 1.5$ in this case), but we came a lot closer than before.

This example, first described by Peres and Wootters, teaches some useful lessons. First, Alice is able to convey more information to Bob by "pruning" her set of codewords. She is better off choosing among fewer signals that are more distinguishable than more signals that are less distinguishable. An alphabet of three letters encodes more than an alphabet of nine letters.

Second, Bob is able to read more of the information if he performs a collective measurement instead of measuring each qubit separately. His optimal orthogonal measurement projects Alice's signal onto a basis of *entangled* states.

### 10.6.5 Classical capacity of a quantum channel

This example illustrates how coding and collective measurement can enhance accessible information, but while using the code narrowed the gap between the accessible information and the Holevo chi of the ensemble, it did not close the gap completely. As is often the case in information theory, we can characterize the accessible information more precisely by considering an asymptotic i.i.d. setting. To be specific, we'll consider the task of sending classical information reliably through a noisy quantum channel $\mathcal{N}^{A \to B}$.

An ensemble of input signal states $\mathcal{E} = \{\boldsymbol{\rho}(x), p(x)\}$ prepared by Alice is mapped by the channel to an ensemble of output signals $\mathcal{E}' = \{\mathcal{N}(\boldsymbol{\rho}(x)), p(x)\}$. If Bob measures the

<!-- Page 53 -->
output his optimal information gain
$$
\mathrm{Acc}(\mathcal{E}') \le I(X; B) = \chi(\mathcal{E}')
$$ {#eq-10.239}
is bounded above by the Holevo chi of the output ensemble $\mathcal{E}'$. To convey as much information through the channel as possible, Alice and Bob may choose the input ensemble $\mathcal{E}$ that maximizes the Holevo chi of the output ensemble $\mathcal{E}'$. The maximum value
$$
\chi(\mathcal{N}) := \max_{\mathcal{E}} \chi(\mathcal{E}') = \max_{\mathcal{E}} I(X; B)
$$ {#eq-10.240}
of $\chi(\mathcal{E}')$ is a property of the channel, which we will call the *Holevo chi of $\mathcal{N}$*.

As we've seen, Bob's actual optimal information gain in this *single-shot* setting may fall short of $\chi(\mathcal{E}')$ in general. But instead of using the channel just once, suppose that Alice and Bob use the channel $n \gg 1$ times, where Alice sends signal states chosen from a code, and Bob performs an optimal measurement to decode the signals he receives. Then an information gain of $\chi(\mathcal{N})$ bits per letter really can be achieved asymptotically as $n \to \infty$.

Let's denote Alice's ensemble of encoded $n$-letter signal states by $\tilde{\mathcal{E}}^{(n)}$, denote the ensemble of classical labels carried by the signals by $\tilde{X}^n$, and denote Bob's ensemble of measurement outcomes by $\tilde{Y}^n$. Let's say that the code has rate $R$ if Alice may choose from among $2^{nR}$ possible signals to send. If classical information can be sent through the channel with rate $R - o(1)$ such that Bob can decode the signal with negligible error probability as $n \to \infty$, then we say the rate $R$ is *achievable*. The classical capacity $C(\mathcal{N})$ of the quantum channel $\mathcal{N}^{A \to B}$ is the supremum of all achievable rates.

As in our discussion of the capacity of a classical channel in §10.1.5, we suppose that $\tilde{X}^n$ is the uniform ensemble over the $2^{nR}$ possible messages, so that $H(\tilde{X}^n) = nR$. Furthermore, the conditional entropy per letter $\frac{1}{n}H(\tilde{X}^n|\tilde{Y}^n)$ approaches zero as $n \to \infty$ if the error probability is asymptotically negligible; therefore,
$$
\begin{aligned}
R &\le \frac{1}{n}\left(I(\tilde{X}^n; \tilde{Y}^n) + o(1)\right) \\
&\le \frac{1}{n}\left(\max_{\mathcal{E}^{(n)}} I(X^n; B^n) + o(1)\right) = \frac{1}{n}\left(\chi(\mathcal{N}^{\otimes n}) + o(1)\right),
\end{aligned}
$$ {#eq-10.241}
where we obtain the first inequality as in eq.(10.52) and the second inequality by invoking the Holevo bound, optimized over all possible $n$-letter input ensembles. We therefore infer that
$$
C(\mathcal{N}) \le \lim_{n \to \infty} \frac{1}{n}\chi(\mathcal{N}^{\otimes n});
$$ {#eq-10.242}
the classical capacity is bounded above by the asymptotic Holevo chi per letter of the product channel $\mathcal{N}^{\otimes n}$.

In fact this upper bound is actually an achievable rate, and hence equal to the classical capacity $C(\mathcal{N})$. However, this formula for the classical capacity is not very useful as it stands, because it requires that we optimize the Holevo chi over message ensembles of arbitrary length; we say that the formula for capacity is *regularized* if, as in this case, it involves taking a limit in which the number of channel uses tends to infinity. It would be far preferable to reduce our expression for $C(\mathcal{N})$ to a *single-letter formula* involving just one use of the channel. In the case of a classical channel, the reduction of the regularized expression to a single-letter formula was possible, because the conditional entropy for $n$ uses of the channel is additive as in eq.(10.49).

<!-- Page 54 -->
For quantum channels the situation is more complicated, as channels are known to exist such that the Holevo chi is strictly superadditive:
$$
\chi(\mathcal{N}_1 \otimes \mathcal{N}_2) > \chi(\mathcal{N}_1) + \chi(\mathcal{N}_2).
$$ {#eq-10.243}
Therefore, at least for some channels, we are stuck with the not-very-useful regularized formula for the classical capacity. But we can obtain a single-letter formula for the optimal achievable communication rate if we put a restriction on the code used by Alice and Bob. In general, Alice is entitled to choose input codewords which are entangled across the many uses of the channel, and when such entangled codes are permitted the computation of the classical channel capacity may be difficult. But suppose we demand that all of Alice's codewords are product states. With that proviso the Holevo chi becomes subadditive, and we may express the optimal rate as
$$
C_1(\mathcal{N}) = \chi(\mathcal{N}).
$$ {#eq-10.244}
$C_1(\mathcal{N})$ is called the *product-state capacity* of the channel.

Let's verify the subadditivity of $\chi$ for product-state codes. The product channel $\mathcal{N}^{\otimes n}$ maps product states to product states; hence if Alice's input signals are product states then so are Bob's output signals, and we can express Bob's $n$-letter ensemble as
$$
\mathcal{E}^{(n)} = \{\boldsymbol{\rho}(x_1) \otimes \boldsymbol{\rho}(x_2) \otimes \dots \otimes \boldsymbol{\rho}(x_n), p(x_1 x_2 \dots x_n)\},
$$ {#eq-10.245}
which has Holevo chi
$$
\chi(\mathcal{E}^{(n)}) = I(X^n; B^n) = H(B^n) - H(B^n|X^n).
$$ {#eq-10.246}
(Here $\mathcal{E}^{(n)}$ is the output ensemble received by Bob when Alice sends product-state codewords, but to simplify the notation we have dropped the prime (indicating output) and tilde (indicating codewords) used earlier, e.g. in eq.(10.239) and eq.(10.241). We do not assume that the probability distribution $p(x_1 x_2 \dots x_n)$ factorizes; hence the $n$ letters received by Bob, though unentangled, can be classically correlated.) While the von Neumann entropy is subadditive,
$$
H(B^n) \le \sum_{i=1}^n H(B_i);
$$ {#eq-10.247}
the (negated) conditional entropy
$$
-H(B^n|X^n) = -\sum_{\vec{x}} p(\vec{x}) H(\boldsymbol{\rho}(\vec{x}))
$$ {#eq-10.248}
(see eq.(10.214)) is not subadditive in general. But for the product-state ensemble eq.(10.245), since the entropy of a product is additive, we have
$$
\begin{aligned}
H(B^n|X^n) &= \sum_{x_1, x_2, \dots, x_n} p(x_1 x_2 \dots x_n)\left(\sum_{i=1}^n H(\boldsymbol{\rho}(x_i))\right) \\
&= \sum_{i=1}^n \sum_{x_i} p_i(x_i) H(\boldsymbol{\rho}(x_i)) = \sum_{i=1}^n H(B_i|X_i)
\end{aligned}
$$ {#eq-10.249}
where $X_i = \{x_i, p_i(x_i)\}$ is the marginal probability distribution for the $i$th letter. Eq.(10.249) is a quantum analog of eq.(10.49), which holds for product-state ensembles

<!-- Page 55 -->
but not in general for entangled ensembles. Combining eq.(10.246), (10.247), (10.249), we have
$$
I(X^n; B^n) \le \sum_{i=1}^n (H(B_i) - H(B_i|X_i)) = \sum_i I(X_i; B_i) \le n\chi(\mathcal{N}).
$$ {#eq-10.250}
Therefore the Holevo chi of a channel is subadditive when restricted to product-state codewords, as we wanted to show.

We won't give a careful argument here that $C_1(\mathcal{N})$ is an asymptotically achievable rate using product-state codewords; we'll just give a rough sketch of the idea. We demonstrate achievability with a random coding argument similar to Shannon's. Alice fixes an input ensemble $\mathcal{E} = \{\boldsymbol{\rho}(x), p(x)\}$, and samples from the product ensemble $\mathcal{E}^{\otimes n}$ to generate a codeword; that is, the codeword
$$
\boldsymbol{\rho}(\vec{x}) = \boldsymbol{\rho}(x_1) \otimes \boldsymbol{\rho}(x_2) \otimes \dots \otimes \boldsymbol{\rho}(x_n)
$$ {#eq-10.251}
is selected with probability $p(\vec{x}) = p(x_1)p(x_2)\dots p(x_n)$. (In fact Alice should choose each $\boldsymbol{\rho}(\vec{x})$ to be pure to optimize the communication rate.) This codeword is sent via $n$ uses of the channel $\mathcal{N}$, and Bob receives the product state
$$
\mathcal{N}^{\otimes n}(\boldsymbol{\rho}(\vec{x})) = \mathcal{N}(\boldsymbol{\rho}(x_1)) \otimes \mathcal{N}(\boldsymbol{\rho}(x_2)) \otimes \dots \otimes \mathcal{N}(\boldsymbol{\rho}(x_n)).
$$ {#eq-10.252}
Averaged over codewords, the joint state of Alice's classical register $X^n$ and Bob's system $B^n$ is
$$
\boldsymbol{\rho}_{X^n B^n} = \sum_{\vec{x}} p(\vec{x}) |\vec{x}\rangle\langle\vec{x}| \otimes \mathcal{N}^{\otimes n}(\boldsymbol{\rho}(\vec{x})).
$$ {#eq-10.253}

To decode, Bob performs a POVM designed to distinguish the codewords effectively; a variant of the pretty good measurement described in §10.6.4 does the job well enough. The state Bob receives is mostly supported on a typical subspace with dimension $2^{n(H(B) + o(1))}$, and for each typical codeword that Alice sends, what Bob receives is mostly supported on a much smaller typical subspace with dimension $2^{n(H(B|X) + o(1))}$. The key point is that ratio of the dimensions of these spaces is exponential in the mutual information of $X$ and $B$:
$$
\frac{2^{n(H(B|X) + o(1))}}{2^{n(H(B) - o(1))}} = 2^{-n(I(X; B) - o(1))}.
$$ {#eq-10.254}
Each of Bob's POVM elements has support on the typical subspace arising from a particular one of Alice's codewords. The probability that any codeword is mapped purely by accident to the decoding subspace of a different codeword is suppressed by the ratio eq.(10.254). Therefore, the probability of a decoding error remains small even when there are $2^{nR}$ codewords to distinguish, for $R = I(X; B) - o(1)$.

We complete the argument with standard Shannonisms. Since the probability of a decoding error is small when we average over codes, it must also be small, averaged over codewords, for a particular sequence of codes. Then by pruning half of the codewords, reducing the rate by a negligible amount, we can ensure that the decoding errors are improbable for every codeword in the code. Therefore $I(X; B)$ is an achievable rate for classical communication. Optimizing over all product-state input ensembles, we obtain eq.(10.244).

To turn this into an honest argument, we would need to specify Bob's decoding measurement more explicitly and do a careful error analysis. This gets a bit technical, so

<!-- Page 56 -->
we'll skip the details. Somewhat surprisingly, though, it turns out to be easier to prove capacity theorems when quantum channels are used for other tasks besides sending classical information. We'll turn to that in §10.7.

### 10.6.6 Entanglement-breaking channels

Though Holevo chi is superadditive for some quantum channels, there are classes of channels for which chi is additive, and for any such channel $\mathcal{N}$ the classical capacity is $C = \chi(\mathcal{N})$ without any need for regularization. For example, consider *entanglement-breaking channels*. We say that $\mathcal{N}^{A \to B}$ is entanglement breaking if for any input state $\boldsymbol{\rho}_{RA}$, $I \otimes \mathcal{N}(\boldsymbol{\rho}_{RA})$ is a separable state on $RA$ --- the action of $\mathcal{N}$ on $A$ always breaks its entanglement with $R$. We claim that if $\mathcal{N}_1$ is entanglement breaking, and $\mathcal{N}_2$ is an arbitrary channel, then
$$
\chi(\mathcal{N}_1 \otimes \mathcal{N}_2) \le \chi(\mathcal{N}_1) + \chi(\mathcal{N}_2).
$$ {#eq-10.255}
To bound the chi of the product channel, consider an input ensemble
$$
\boldsymbol{\rho}_{X A_1 A_2} = \sum_x p(x) |x\rangle\langle x| \otimes \boldsymbol{\rho}(x)_{A_1 A_2},
$$ {#eq-10.256}
which is mapped by $\mathcal{N}_1 \otimes \mathcal{N}_2$ to
$$
\boldsymbol{\rho}'_{X B_1 B_2} = (I \otimes \mathcal{N}_1 \otimes \mathcal{N}_2)(\boldsymbol{\rho}_{X A_1 A_2}).
$$ {#eq-10.257}
By tracing out the second output system we find
$$
\boldsymbol{\rho}'_{X B_1} = I \otimes \mathcal{N}_1(\boldsymbol{\rho}_{X A_1}) = \sum_x p(x) |x\rangle\langle x| \otimes \mathcal{N}_1(\boldsymbol{\rho}(x)_{A_1}),
$$ {#eq-10.258}
which, by the definition of $\chi(\mathcal{N}_1)$ implies
$$
I(X; B_1)_{\boldsymbol{\rho}'} \le \chi(\mathcal{N}_1).
$$ {#eq-10.259}
We can easily check that, for any three systems $A$, $B$, and $C$,
$$
I(A; BC) = I(A; B) + I(AB; C) - I(C; B) \le I(A; B) + I(AB; C),
$$ {#eq-10.260}
so that in particular
$$
I(X; B_1 B_2)_{\boldsymbol{\rho}'} \le \chi(\mathcal{N}_1) + I(X B_1; B_2)_{\boldsymbol{\rho}'}.
$$ {#eq-10.261}
Eq.(10.261) holds for any channels $\mathcal{N}_1$ and $\mathcal{N}_2$; now to obtain eq.(10.255) it suffices to show that
$$
I(X B_1; B_2)_{\boldsymbol{\rho}'} \le \chi(\mathcal{N}_2)
$$ {#eq-10.262}
for entanglement breaking $\mathcal{N}_1$.

If $\mathcal{N}_1$ is entanglement breaking, then $\boldsymbol{\rho}(x)_{A_1 A_2}$ is mapped by $\mathcal{N}_1$ to a separable state:
$$
\mathcal{N}_1 \otimes I : \boldsymbol{\rho}(x)_{A_1 A_2} \mapsto \sum_y p(y|x) \boldsymbol{\sigma}(x, y)_{B_1} \otimes \boldsymbol{\tau}(x, y)_{A_2}.
$$ {#eq-10.263}
Therefore,
$$
\boldsymbol{\rho}'_{X B_1 B_2} = \sum_{x,y} p(x) p(y|x) |x\rangle\langle x| \otimes \boldsymbol{\sigma}(x, y)_{B_1} \otimes [\mathcal{N}_2(\boldsymbol{\tau}(x, y))]_{B_2}
$$ {#eq-10.264}

<!-- Page 57 -->
may be regarded as the marginal state (after tracing out $Y$) of
$$
\boldsymbol{\omega}'_{XY B_1 B_2} = \sum_{x,y} p(x, y) |x, y\rangle\langle x, y| \otimes \boldsymbol{\sigma}(x, y) \otimes \mathcal{N}_2(\boldsymbol{\tau}(x, y)).
$$ {#eq-10.265}
Furthermore, because $\boldsymbol{\omega}'$ becomes a product state when conditioned on $(x, y)$, we find
$$
I(B_1; B_2 | XY)_{\boldsymbol{\omega}'} = 0,
$$ {#eq-10.266}
and using strong subadditivity together with the definition of conditional mutual information we obtain
$$
\begin{aligned}
I(XB_1; B_2)_{\boldsymbol{\rho}'} &= I(XB_1; B_2)_{\boldsymbol{\omega}'} \le I(XY B_1; B_2)_{\boldsymbol{\omega}'} \\
&= I(XY; B_2)_{\boldsymbol{\omega}'} + I(B_1; B_2 | XY)_{\boldsymbol{\omega}'} = I(XY; B_2)_{\boldsymbol{\omega}'}.
\end{aligned}
$$ {#eq-10.267}
Finally, noting that
$$
\mathrm{tr}_{B_1}\boldsymbol{\omega}'_{XY B_1 B_2} = \sum_{x,y} p(x, y) |x, y\rangle\langle x, y| \otimes \mathcal{N}_2(\boldsymbol{\tau}(x, y))
$$ {#eq-10.268}
and recalling the definition of $\chi(\mathcal{N}_2)$, we see that $I(XY; B_2)_{\boldsymbol{\omega}'} \le \chi(\mathcal{N}_2)$, establishing eq.(10.262), and therefore eq.(10.255).

An example of an entanglement-breaking channel is a *classical-quantum channel*, also called a *c-q channel*, which acts according to
$$
\mathcal{N}^{A \to B} : \boldsymbol{\rho}_A \mapsto \sum_x \langle x|\boldsymbol{\rho}_A|x\rangle \boldsymbol{\sigma}(x)_B,
$$ {#eq-10.269}
where $\{|x\rangle\}$ is an orthonormal basis. In effect, the channel performs a complete orthogonal measurement on the input state and then prepares an output state conditioned on the measurement outcome. The measurement breaks the entanglement between system $A$ and any other system with which it was initially entangled. Therefore, c-q channels are entanglement breaking and have additive Holevo chi.
