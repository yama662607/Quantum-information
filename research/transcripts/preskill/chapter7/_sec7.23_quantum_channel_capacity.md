# Section 7.23: The Quantum Channel Capacity

**Source:** Preskill Lecture Notes, Chapter 7, pp. 71–79 (Physical pages 77–85).

---

As we have formulated it up until now, our goal in constructing quantum error correcting codes has been to maximize the distance $d$ of the code, given its length $n$ and the number $k$ of encoded qubits. Larger distance provides better protection against errors, as a distance $d$ code can correct $d - 1$ erasures, or $(d - 1)/2$ errors at unknown locations. We have observed that "good" codes can be constructed, that maintain a finite rate $k/n$ for $n$ large, and correct a number of errors $pn$ that scales linearly with $n$.

Now we will address a related but rather different question about the asymptotic performance of QECC's. Consider a superoperator $\$$ that acts on density operators in a Hilbert space $\mathcal{H}$. Now consider $\$$ acting independently on each copy of $\mathcal{H}$ contained in the $n$-fold tensor product
$$
\mathcal{H}^{(n)} = \mathcal{H} \otimes \dots \otimes \mathcal{H} .
$$ {#eq-7.285}
We would like to select a code subspace $\mathcal{H}_{\text{code}}^{(n)}$ of $\mathcal{H}^{(n)}$ such that quantum information residing in $\mathcal{H}_{\text{code}}^{(n)}$ can be subjected to the superoperator
$$
\$^{(n)} = \$ \otimes \dots \otimes \$ ,
$$ {#eq-7.286}
and yet can still be decoded with high fidelity.

The rate of a code is defined as
$$
R = \frac{\log \mathcal{H}_{\text{code}}^{(n)}}{\log \mathcal{H}^{(n)}} ;
$$ {#eq-7.287}
this is the number of qubits employed to carry one qubit of encoded information. The *quantum channel capacity* $Q(\$)$ of the superoperator $\$$ is the maximum asymptotic rate at which quantum information can be sent over the channel with arbitrarily good fidelity. That is, $Q(\$)$ is the largest number such that for any $R < Q(\$)$ and any $\varepsilon > 0$, there is a code $\mathcal{H}_{\text{code}}^{(n)}$ with rate at least $R$, such that for any $|\psi\rangle \in \mathcal{H}_{\text{code}}^{(n)}$, the state $\rho$ recovered after $|\psi\rangle$ passes through $\$^{(n)}$ has fidelity
$$
F = \langle\psi|\rho|\psi\rangle > 1 - \varepsilon .
$$ {#eq-7.288}

Thus, $Q(\$)$ is a quantum version of the capacity defined by Shannon for a classical noisy channel. As we have already seen in Chapter 5, this $Q(\$)$ is not the only sort of capacity that can be associated with a quantum channel. It is also of considerable interest to ask about $C(\$)$, the maximum rate at which *classical* information can be transmitted through a quantum channel with arbitrarily small probability of error. A formal answer to this question was formulated in §5.4, but only for a restricted class of possible encoding schemes; the general answer is still unknown. The quantum channel capacity $Q(\$)$ is even less well understood than the classical capacity $C(\$)$ of a quantum channel. Note that $Q(\$)$ is not the same thing as the maximum asymptotic rate $k/n$ that can be achieved by "good" $[[n, k, d]]$ QECC's with positive $d/n$. In the case of the quantum channel capacity we need not insist that the code correct *any* possible distribution of $pn$ errors, as long as the errors that cannot be corrected become highly atypical for $n$ large.

Here we will mostly limit the discussion to two interesting examples of quantum channels acting on a single qubit — the quantum erasure channel (for which $Q$ is exactly known), and the depolarizing channel (for which $Q$ is still unknown, but useful upper and lower bounds can be derived).

What are these channels? In the case of the quantum erasure channel, a qubit transmitted through the channel either arrives intact, or (with probability $p$) becomes lost and is never received. We can find a unitary representation of this channel by embedding the qubit in the three-dimensional Hilbert space of a qutrit with orthonormal basis $\{|0\rangle, |1\rangle, |2\rangle\}$. The channel acts according to
$$
\begin{aligned}
|0\rangle \otimes |0\rangle_E &\to \sqrt{1 - p}|0\rangle \otimes |0\rangle_E + \sqrt{p}|2\rangle \otimes |1\rangle_E , \\
|1\rangle \otimes |0\rangle_E &\to \sqrt{1 - p}|1\rangle \otimes |0\rangle_E + \sqrt{p}|2\rangle \otimes |2\rangle_E ,
\end{aligned}
$$ {#eq-7.289}
where $\{|0\rangle_E, |1\rangle_E, |2\rangle_E\}$ are mutually orthogonal states of the environment. The receiver can measure the observable $|2\rangle\langle 2|$ to determined whether the qubit is undamaged or has been "erased."

The depolarizing channel (with error probability $p$) was discussed at length in §3.4.1. We see that, for $p \le 3/4$, we may describe the fate of a qubit transmitted through the channel this way: with probability $1 - q$ (where $q = 4/3 p$), the qubit arrives undamaged, and with probability $q$ it is *destroyed*, in which case it is described by the random density matrix $\frac{1}{2}\mathbf{1}$.

Both the erasure channel and the depolarizing channel destroy a qubit with a specified probability. The crucial difference between the two channels is that in the case of the erasure channel, the receiver knows which qubits have been destroyed; in the case of the depolarizing channel, the damaged qubits carry no identifying marks, which makes recovery more challenging. Of course, for both channels, the sender has no way to know ahead of time which qubits will be obliterated.

## 7.23.1 Erasure channel

The quantum channel capacity of the erasure channel can be precisely determined. First we will derive an upper bound on $Q$, and then we will show that codes exist that achieve high fidelity and attain a rate arbitrarily close to the upper bound.

As the first step in the derivation of an upper bound on the capacity, we show that $Q = 0$ for $p > \frac{1}{2}$.

We observe that the erasure channel can be realized if Alice sends a qubit to Bob, and a third party Charlie decides at random to either *steal* the qubit (with probability $p$) or allow the qubit to pass unscathed to Bob (with probability $1 - p$).

If Alice sends a large number $n$ of qubits, then about $(1 - p)n$ reach Bob, and $pn$ are intercepted by Charlie. Hence for $p > \frac{1}{2}$, Charlie winds up in possession of more qubits than Bob, and if Bob can recover the quantum information encoded by Alice, then certainly Charlie can as well. Therefore, if $Q(p) > 0$ for $p > \frac{1}{2}$, Bob and Charlie can clone the unknown encoded quantum states sent by Alice, which is impossible. (Strictly speaking, they can clone with fidelity $F = 1 - \varepsilon$, for any $\varepsilon > 0$.) We conclude that $Q(p) = 0$ for $p > \frac{1}{2}$.

To obtain a bound on $Q(p)$ in the case $p < \frac{1}{2}$, we will appeal to the following lemma. Suppose that Alice and Bob are connected by both a perfect noiseless channel and a noisy channel with capacity $Q > 0$. And suppose that Alice sends $m$ qubits over the perfect channel and $n$ qubits over the noisy channel. Then the number $r$ of encoded qubits that Bob may recover with arbitrarily high fidelity must satisfy
$$
r \le m + Qn .
$$ {#eq-7.290}
We derive this inequality by noting that Alice and Bob can simulate the $m$ qubits sent over the perfect channel by sending $m/Q$ over the noisy channel and so achieve a rate
$$
R = \frac{r}{m/Q + n} = \left(\frac{r}{m + Qn}\right) Q ,
$$ {#eq-7.291}
over the noisy channel. Were $r$ to exceed $m + Qn$, this rate $R$ would exceed the capacity, a contradiction. Therefore eq.(7.290) is satisfied.

Now consider the erasure channel with error probability $p_1$, and suppose $Q(p_1) > 0$. Then we can bound $Q(p_2)$ for $p_2 \le p_1$ by
$$
Q(p_2) \le 1 - \frac{p_2}{p_1} + \frac{p_2}{p_1} Q(p_1) .
$$ {#eq-7.292}
(In other words, if we plot $Q(p)$ in the $(p, Q)$ plane, and we draw a straight line segment from any point $(p_1, Q_1)$ on the plot to the point $(p = 0, Q = 1)$, then the curve $Q(p)$ must lie on or below the segment in the interval $0 \le p \le p_1$; if $Q(p)$ is twice differentiable, then its second derivative cannot be positive.) To obtain this bound, imagine that Alice sends $n$ qubits to Bob, knowing ahead of time that $n(1 - p_2/p_1)$ specified qubits will arrive safely. The remaining $n(p_2/p_1)$ qubits are erased with probability $p_1$. Therefore, Alice and Bob are using both a perfect channel and an erasure channel with erasure probability $p_1$; eq.(7.290) holds, and the rate $R$ they can attain is bounded by
$$
R \le 1 - \frac{p_2}{p_1} + \frac{p_2}{p_1} Q(p_1) .
$$ {#eq-7.293}
On the other hand, for $n$ large, altogether about $n p_2$ qubits are erased, and $(1 - p_2)n$ arrive safely. Thus Alice and Bob have an erasure channel with erasure probability $p_2$, except that they have the additional advantage of knowing ahead of time that some of the qubits that Alice sends are invulnerable to erasure. With this information, they can be no worse off than without it; eq.(7.292) then follows. The same bound applies to the depolarizing channel as well.

Now, the result $Q(p) = 0$ for $p > 1/2$ can be combined with eq.(7.292). We conclude that the curve $Q(p)$ must be on or below the straight line connecting the points $(p = 0, Q = 1)$ and $(p = 1/2, Q = 0)$, or
$$
Q(p) \le 1 - 2p, \quad 0 \le p \le \frac{1}{2} .
$$ {#eq-7.294}

In fact, there are stabilizer codes that actually attain the rate $1 - 2p$ for $0 \le p \le 1/2$. We can see this by borrowing an idea from Claude Shannon, and averaging over random stabilizer codes. Imagine choosing, in succession, altogether $n - k$ stabilizer generators. Each is selected from among the $4^n$ Pauli operators, where all have equal a priori probability, except that each generator is required to commute with all generators chosen in previous rounds.

Now Alice uses this stabilizer code to encode an arbitrary quantum state in the $2^k$-dimensional code subspace, and sends the $n$ qubits to Bob over an erasure channel with erasure probability $p$. Will Bob be able to recover the state sent by Alice?

Bob replaces each erased qubit by a qubit in the state $|0\rangle$, and then proceeds to measure all $n - k$ stabilizer generators. From this syndrome measurement, he hopes to infer the Pauli operator $\boldsymbol{E}$ acting on the replaced qubits. Once $\boldsymbol{E}$ is known, we can apply $\boldsymbol{E}^\dagger$ to recover a perfect duplicate of the state sent by Alice. For $n$ large, the number of qubits that Bob must replace is about $pn$, and he will recover successfully if there is a unique Pauli operator $\boldsymbol{E}$ that can produce the syndrome that he finds. If more than one Pauli operator acting on the replaced qubits has this same syndrome, then recovery may fail.

How likely is failure? Since there are about $pn$ replaced qubits, there are about $4^{pn}$ Pauli operators with support on these qubits. Furthermore, for any particular Pauli operator $\boldsymbol{E}$, a random stabilizer code generates a random syndrome — each stabilizer generator has probability $1/2$ of commuting with $\boldsymbol{E}$, and probability $1/2$ of anti-commuting with $\boldsymbol{E}$. Therefore, the probability that two Pauli operators have the same syndrome is $(1/2)^{n-k}$.

There is at least one particular Pauli operator acting on the replaced qubits that has the syndrome found by Bob. But the probability that another Pauli operator has this same syndrome (and hence the probability of a recovery failure) is no worse than
$$
P_{\text{fail}} \le 4^{pn} \left(\frac{1}{2}\right)^{n-k} = 2^{-n(1 - 2p - R)} .
$$ {#eq-7.295}
where $R = k/n$ is the rate. Eq.(7.295) bounds the failure probability if we *average* over all stabilizer codes with rate $R$; it follows that at least one particular stabilizer code must exist whose failure probability also satisfies the bound.

For that particular code, $P_{\text{fail}}$ gets arbitrarily small as $n \to \infty$, for any rate $R = 1 - 2p - \delta$ strictly less than $1 - 2p$. Therefore $R = 1 - 2p$ is asymptotically attainable; combining this result with the inequality eq.(7.294) we obtain the capacity of the quantum erasure channel:
$$
Q(p) = 1 - 2p, \quad 0 \le p \le \frac{1}{2} .
$$ {#eq-7.296}

If we wanted assurance that a distinct syndrome could be assigned to all ways of damaging $pn$ erased qubits, then we would require an $[[n, k, d]]$ quantum code with distance $d > pn$. Our Gilbert–Varshamov bound of §7.16 guarantees the existence of such a code for
$$
R < 1 - H_2(p) - p \log_2 3 .
$$ {#eq-7.297}
This rate can be achieved by a code that recovers from *any* of the possible ways of erasing up to $pn$ qubits. It lies strictly below the capacity for $p > 0$, because to achieve high average fidelity, it suffices to be able to correct the *typical* erasures, rather than all possible erasures.

## 7.23.2 Depolarizing channel

The capacity of the depolarizing channel is still not precisely known, but we can obtain some interesting upper and lower bounds.

As for the erasure channel, we can find an upper bound on the capacity by invoking the no-cloning theorem. Recall that for the depolarizing channel with error probability $p < 3/4$, each qubit either passes safely with probability $1 - 4/3 p$, or is randomized (replaced by the maximally mixed state $\rho = \frac{1}{2}\mathbf{1}$) with probability $q = 4/3 p$. An eavesdropper Charlie, then, can simulate the channel by intercepting qubits with probability $q$, and replacing each stolen qubit with a maximally mixed qubit. For $q > 1/2$, Charlie steals more than half the qubits and is in a better position than Bob to decode the state sent by Alice. Therefore, to disallow cloning, the rate at which quantum information is sent from Alice to Bob must be strictly zero for $q > 1/2$ or $p > 3/8$:
$$
Q(p) = 0, \quad p > \frac{3}{8} .
$$ {#eq-7.298}

In fact we can obtain a stronger bound by noting that Charlie can choose a better eavesdropping strategy — he can employ the optimal *approximate* cloner that you studied in a homework problem. This device, applied to each qubit sent by Alice, replaces it by two qubits that each approximate the original with fidelity $F = 5/6$, or
$$
|\psi\rangle\langle\psi| \to \left[(1 - q)|\psi\rangle\langle\psi| + q\frac{1}{2}\mathbf{1}\right]^{\otimes 2} ,
$$ {#eq-7.299}
where $F = 5/6 = 1 - 1/2 q$. By operating the cloner, both Charlie and Bob can receive Alice's state transmitted through the $q = 1/3$ depolarizing channel. Therefore, the attainable rate must vanish; otherwise, by combining the approximate cloner with quantum error correction, Bob and Charlie would be able to clone Alice's unknown state *exactly*. We conclude that the capacity vanishes for $q > 1/3$ or $p > 1/4$:
$$
Q(p) = 0, \quad p > \frac{1}{4} .
$$ {#eq-7.300}
Invoking the bound eq.(7.292) we infer that
$$
Q(p) \le 1 - 4p, \quad 0 \le p \le \frac{1}{4} .
$$ {#eq-7.301}

This result actually coincides with our bound on the rate of $[[n, k, d]]$ codes with $k \ge 1$ and $d \ge 2pn + 1$ found in §7.9. A bound on the capacity is *not* the same thing as a bound on the allowable error probability for an $[[n, k, d]]$ code (and in the latter case the Rains bound is tighter). Still, the similarity of the two results bound may not be a complete surprise, as both bounds are derived from the no-cloning theorem.

We can obtain a lower bound on the capacity by estimating the rate that can be attained through random stabilizer coding, as we did for the erasure channel. Now, when Bob measures the $n - k$ (randomly chosen, commuting) stabilizer generators, he hopes to obtain a syndrome that points to a unique one among the typical Pauli error operators that can arise with nonnegligible probability when the depolarizing channel acts on the $n$ qubits sent by Alice. The number $N_{\text{typ}}$ of typical Pauli operators with total probability $1 - \varepsilon$ can be bounded by
$$
N_{\text{typ}} \le 2^{n(H_2(p) + p\log_2 3 + \delta)} ,
$$ {#eq-7.302}
for any $\delta, \varepsilon > 0$ and $n$ sufficiently large. Bob's attempt at recovery can fail if another among these typical Pauli operators has the same syndrome as the actual error operator. Since a random code assigns a random $(n - k)$-bit syndrome to each Pauli operator, the failure probability can be bounded as
$$
P_{\text{fail}} \le 2^{n(H_2(p) + p\log_2 3 + \delta)} 2^{k-n} + \varepsilon .
$$ {#eq-7.303}
Here the second term bounds the probability of an atypical error, and the first bounds the probability of an ambiguous syndrome in the case of a typical error. We see that the failure probability, averaged over random stabilizer codes, becomes arbitrarily small for large $n$, for any $\delta' < 0$ and rate $R$ such that
$$
R \equiv \frac{k}{n} < 1 - H_2(p) - p\log_2 3 - \delta' .
$$ {#eq-7.304}
If the failure probability, averaged over codes, is small, there is a particular code with small failure probability, and we conclude that the rate $R$ is attainable; the capacity of the depolarizing channel is bounded below as
$$
Q(p) \ge 1 - H_2(p) - p\log_2 3 .
$$ {#eq-7.305}

Not coincidentally, the rate attainable by random coding agrees with the asymptotic form of the quantum Hamming upper bound on the rate of nondegenerate $[[n, k, d]]$ codes with $d > 2pn$; we arrive at both results by assigning a distinct syndrome to each of the typical errors. Of course, the Gilbert–Varshamov lower bound on the rate of $[[n, k, d]]$ codes lies below $Q(p)$, as it is obtained by demanding that the code can correct *all* the errors of weight $pn$ or less, not just the typical ones.

This random coding argument can also be applied to a somewhat more general channel, in which $\boldsymbol{X}, \boldsymbol{Y}$, and $\boldsymbol{Z}$ errors occur at different rates. (We'll call this a "Pauli channel.") If an $\boldsymbol{X}$ error occurs with probability $p_X$, a $\boldsymbol{Y}$ error with probability $p_Y$, a $\boldsymbol{Z}$ error with probability $p_Z$, and no error with probability $p_I \equiv 1 - p_X - p_Y - p_Z$, then the number of typical errors on $n$ qubits is
$$
\frac{n!}{(p_X n)!(p_Y n)!(p_Z n)!(p_I n)!} \sim 2^{n H(p_I, p_X, p_Y, p_Z)} ,
$$ {#eq-7.306}
where
$$
H \equiv H(p_I, p_X, p_Y, p_Z) = -p_I \log_2 p_I - p_X \log_2 p_X - p_Y \log_2 p_Y - p_Z \log_2 p_Z ,
$$ {#eq-7.307}
is the Shannon entropy of the probability distribution $\{p_I, p_X, p_Y, p_Z\}$. Now we find
$$
Q(p_I, p_X, p_Y, p_Z) \ge 1 - H(p_I, p_X, p_Y, p_Z) ;
$$ {#eq-7.308}
if the rate $R$ satisfies $R < 1 - H$, then again it is highly unlikely that a single syndrome of a random stabilizer code will point to more than one typical error operator.

## 7.23.3 Degeneracy and capacity

Our derivation of a lower bound on the capacity of the depolarizing channel closely resembles the argument in §5.1.3 for a lower bound on the capacity of the classical binary symmetric channel. In the classical case, there was a matching upper bound. If the rate were larger, then there would not be enough syndromes to attach to all of the typical errors.

In the quantum case, the derivation of the matching upper bound does not carry through, because a quantum code can be degenerate. We may not need a distinct syndrome for each typical error, as some of the possible errors could act trivially on the code subspace. Indeed, not only does the derivation fail; the matching upper bound is actually false — rates exceeding $1 - H_2(p) - p\log_2 3$ actually *can* be attained.[^fn-shor-smolin]

[^fn-shor-smolin]: P.W. Shor and J.A. Smolin, "Quantum Error-Correcting Codes Need Not Completely Reveal the Error Syndrome" quant-ph/9604006; D.P. DiVincenzo, P.W. Shor, and J.A. Smolin, "Quantum Channel Capacity of Very Noisy Channels," quant-ph/9706061.

Shor and Smolin investigated the rate that can be achieved by concatenated codes, where the outer code is a random stabilizer code, and the inner code is a degenerate code with a relatively small block size. Their idea is that the degeneracy of the inner code will allow enough typical errors to act trivially in the code space that a higher rate can be attained than through random coding alone.

To investigate this scheme, imagine that encoding and decoding are each performed in two stages. In the first stage, using the (random) outer code that she and Bob have agreed on, Alice encodes the state that she has selected in a large $n$-qubit block. In the second stage, Alice encodes each of these $n$-qubits in a block of $m$ qubits, using the inner code. Similarly, when Bob receives the $nm$ qubits, he first decodes each inner block of $m$, and then subsequently decodes the block of $n$.

We can evidently describe this procedure in an alternative language — Alice and Bob are using just the outer code, but the qubits are being transmitted through a composite channel.

This modified channel consists: first the inner encoder, then propagation through the original noisy channel, and finally inner decoding and inner recovery. The rate that can be attained through the original channel, via concatenated coding, is the same as the rate that can be attained through the modified channel, via random coding.

Specifically, suppose that the inner code is an $m$-qubit repetition code, with stabilizer
$$
\boldsymbol{Z}_1\boldsymbol{Z}_2, \; \boldsymbol{Z}_1\boldsymbol{Z}_3, \; \boldsymbol{Z}_1\boldsymbol{Z}_4, \dots, \boldsymbol{Z}_1\boldsymbol{Z}_m .
$$ {#eq-7.309}
This is not much of a quantum code; it has distance 1, since it is insensitive to phase errors — each $\boldsymbol{Z}_j$ commutes with the stabilizer. But in the present context its important feature is it high degeneracy, all $\boldsymbol{Z}_i$ errors are equivalent.

The encoding (and decoding) circuit for the repetition code consists of just $m - 1$ CNOT's, so our composite channel looks like (in the case $m = 3$):

where $\$$ denotes the original noisy channel. (We have also suppressed the final recovery step of the decoding; e.g., if the measured qubits both read 1, we should flip the data qubit. In fact, to simplify the analysis of the composite channel, we will dispense with this step.)

Since we recall that a CNOT propagates bit flips forward (from control to target) and phase flips backward (from target to control), we see that for each possible measurement outcome of the auxiliary qubits, the composite channel is a Pauli channel. If we imagine that this measurement of the $m - 1$ inner block qubits is performed for each of the $n$ qubits of the outer block, then Pauli channels act independently on each of the $n$ qubits, but the channels acting on different qubits have different parameters (error probabilities $p_I^{(i)}, p_X^{(i)}, p_Y^{(i)}, p_Z^{(i)}$ for the $i$th qubit). Now the number of typical error operators acting on the $n$ qubits is
$$
2^{\sum_{i=1}^n H_i}
$$ {#eq-7.310}
where
$$
H_i = H(p_I^{(i)}, p_X^{(i)}, p_Y^{(i)}, p_Z^{(i)}) ,
$$ {#eq-7.311}
is the Shannon entropy of the Pauli channel acting on the $i$th qubit. By the law of large numbers, we will have
$$
\sum_{i=1}^n H_i = n\langle H\rangle ,
$$ {#eq-7.312}
for large $n$, where $\langle H\rangle$ is the Shannon entropy, averaged over the $2^{m-1}$ possible classical outcomes of the measurement of the extra qubits of the inner code. Therefore, the rate that can be attained by the random outer code is
$$
R = \frac{1 - \langle H\rangle}{m} ,
$$ {#eq-7.313}
(we divide by $m$, because the concatenated code has a length $m$ times longer than the random code).

Shor and Smolin discovered that there are repetition codes (values of $m$) for which, in a suitable range of $p$, $1 - \langle H\rangle$ is positive while $1 - H_2(p) - p\log_2 3$ is negative. In this range, then, the capacity $Q(p)$ is nonzero, showing that the lower bound eq.(7.305) is not tight.

A nonvanishing asymptotic rate is attainable through random coding for $1 - H_2(p) - p\log_2 3 > 0$, or $p < p_{\max} \simeq .18929$. If a random outer code is concatenated with a 5-qubit inner repetition code ($m = 5$ turns out to be the optimal choice), then $1 - \langle H\rangle > 0$ for $p < p'_{\max} \simeq .19036$; the maximum error probability for which a nonzero rate is attainable increases by about 0.6%. It is not obvious that the concatenated code should outperform the random code in this range of error probability, though as we have indicated, it might have been expected because of the (phase) degeneracy of the repetition code. Nor is it obvious that $m = 5$ should be the best choice, but this can be verified by an explicit calculation of $\langle H\rangle$.[^fn-shor-25qubit]

[^fn-shor-25qubit]: In fact a very slight further improvement can be achieved by concatenating a random code with the 25-qubit generalized Shor code described in the exercises — then a nonzero rate is attainable for $p < p''_{\max} \simeq .19056$ (another 0.1% better than the maximum tolerable error probability with repetition coding).

The depolarizing channel is one of the very simplest of quantum channels. Yet even for this case, the problem of characterizing and calculating the capacity is largely unsolved. This example illustrates that, due to the possibility of degenerate coding, the capacity problem is considerably more subtle for quantum channels than for classical channels.

We have seen that (if the errors are well described by the depolarizing channel), quantum information can be recovered from a quantum memory with arbitrarily high fidelity, as long as the probability of error per qubit is less than 19%. This is an improvement relative to the 10% error rate that we found could be handled by concatenation of the $[[5, 1, 3]]$ code. In fact $[[n, k, d]]$ codes that can recover from any distribution of up to $pn$ errors do not exist for $p > 1/6$, according to the Rains bound. Nonzero capacity is possible for error rates between 16.7% and 19% because it is sufficient for the QECC to be able to correct the typical errors rather than all possible errors.

However, the claim that recovery is possible even if 19% of the qubits sustain damage is highly misleading in an important respect. This result applies if encoding, decoding, and recovery can be executed flawlessly. But these operations are actually very intricate quantum computations that in practice will certainly be susceptible to error. We will not fully understand how well coding can protect quantum information from harm until we have learned to design an error recovery protocol that is robust even if the execution of the protocol is flawed. Such *fault-tolerant* protocols will be developed in Chapter 8.
