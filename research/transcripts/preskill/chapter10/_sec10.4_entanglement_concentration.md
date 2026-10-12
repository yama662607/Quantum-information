# Section 10.4 Entanglement Concentration and Dilution

## 10.4 Entanglement Concentration and Dilution

Any bipartite pure state that is not a product state is entangled. But *how* entangled? Can we compare two states and say that one is more entangled than the other?

For example, consider the two bipartite states
$$
\begin{aligned}
|\phi^+\rangle &= \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle), \\
|\psi\rangle &= \sqrt{\frac{2}{3}}|00\rangle + \frac{1}{\sqrt{6}}|11\rangle + \frac{1}{\sqrt{6}}|22\rangle.
\end{aligned} \tag{10.164}
$$
$|\phi^+\rangle$ is a maximally entangled state of two qubits, while $|\psi\rangle$ is a *partially* entangled state of two *qutrits*. Which is more entangled?

It is not immediately clear that the question has a meaningful answer. Why should it be possible to find an unambiguous way of ordering all bipartite pure states according to their degree of entanglement? Can we compare a pair of qutrits with a pair of qubits any more than we can compare apples and oranges?

A crucial feature of entanglement is that it cannot be created by local operations and classical communication (LOCC). In particular, if Alice and Bob share a bipartite pure state, its Schmidt number does not increase if Alice or Bob performs a unitary transformation on her/his share of the state, nor if Alice or Bob measures her/his share, even if Alice and Bob exchange classical messages about their actions and measurement outcomes. Therefore, any quantitative measure of entanglement should have the property that LOCC cannot increase it, and it should also vanish for an unentangled product state. An obvious candidate is the Schmidt number, but on reflection it does not seem very satisfactory. Consider
$$
|\psi_\varepsilon\rangle = \sqrt{1 - 2|\varepsilon|^2} |00\rangle + \varepsilon|11\rangle + \varepsilon|22\rangle, \tag{10.165}
$$
which has Schmidt number 3 for any $|\varepsilon| > 0$. Do we really want to say that $|\psi_\varepsilon\rangle$ is "more entangled" than $|\phi^+\rangle$? Entanglement, after all, can be regarded as a resource -- we might plan to use it for teleportation, for example -- and it seems clear that $|\psi_\varepsilon\rangle$ (for $|\varepsilon| \ll 1$) is a less valuable resource than $|\phi^+\rangle$.

It turns out, though, that there is a natural and useful way to quantify the entanglement of any bipartite pure state. To compare two states, we use LOCC to convert both states to a *common currency* that can be compared directly. The common currency is *maximal* entanglement, and the amount of shared entanglement can be expressed in units of Bell pairs (maximally entangled two-qubit states), also called *ebits* of entanglement.

To quantify the entanglement of a particular bipartite pure state, $|\psi\rangle_{AB}$, imagine preparing $n$ identical copies of that state. Alice and Bob share a large supply of maximally entangled *Bell pairs*. Using LOCC, they are to convert $k$ Bell pairs ($(|\phi^+\rangle_{AB})^{\otimes k}$) to $n$ high-fidelity copies of the desired state ($(|\psi\rangle_{AB})^{\otimes n}$). What is the minimum number $k_{\min}$ of Bell pairs with which they can perform this task?

To obtain a precise answer, we consider the *asymptotic* setting, requiring arbitrarily high-fidelity conversion in the limit of large $n$. We say that a rate $R$ of conversion from $|\phi^+\rangle$ to $|\psi\rangle$ is asymptotically achievable if for any $\varepsilon, \delta > 0$, there is an LOCC protocol with
$$
\frac{k}{n} \le R + \delta, \tag{10.166}
$$
which prepares the target state $|\psi^+\rangle^{\otimes n}$ with fidelity $F \ge 1 - \varepsilon$. We define the *entanglement cost* $E_C$ of $|\psi\rangle$ as the infimum of achievable conversion rates:
$$
E_C(|\psi\rangle) := \inf\{\text{achievable rate for creating } |\psi\rangle \text{ from Bell pairs}\}. \tag{10.167}
$$
Asymptotically, we can create many copies of $|\psi\rangle$ by consuming $E_C$ Bell pairs per copy.

Now imagine that $n$ copies of $|\psi\rangle_{AB}$ are already shared by Alice and Bob. Using LOCC, Alice and Bob are to convert $(|\psi\rangle_{AB})^{\otimes n}$ back to the standard currency: $k'$ Bell pairs $|\phi^+\rangle_{AB}^{\otimes k'}$. What is the maximum number $k'_{\max}$ of Bell pairs they can extract from $|\psi\rangle_{AB}^{\otimes n}$? In this case we say that a rate $R'$ of conversion from $|\psi\rangle$ to $|\phi^+\rangle$ is asymptotically achievable if for any $\varepsilon, \delta > 0$, there is an LOCC protocol with
$$
\frac{k'}{n} \ge R' - \delta, \tag{10.168}
$$
which prepares the target state $|\phi^+\rangle^{\otimes k'}$ with fidelity $F \ge 1 - \varepsilon$. We define the *distillable entanglement* $E_D$ of $|\psi\rangle$ as the supremum of achievable conversion rates:
$$
E_D(|\psi\rangle) := \sup\{\text{achievable rate for distilling Bell pairs from } |\psi\rangle\}. \tag{10.169}
$$
Asymptotically, we can convert many copies of $|\psi\rangle$ to Bell pairs, obtaining $E_D$ Bell pairs per copy of $|\psi\rangle$ consumed.

Since it is an inviolable principle that LOCC cannot create entanglement, it is certain that
$$
E_D(|\psi\rangle) \le E_C(|\psi\rangle); \tag{10.170}
$$
otherwise Alice and Bob could increase their number of shared Bell pairs by converting them to copies of $|\psi\rangle$ and then back to Bell pairs. In fact the entanglement cost and distillable entanglement are equal for bipartite pure states. (The story is more complicated for bipartite mixed states; see §10.5.) Therefore, for pure states at least we may drop the subscript, using $E(|\psi\rangle)$ to denote the entanglement of $|\psi\rangle$. We don't need to distinguish between entanglement cost and distillable entanglement because conversion of entanglement from one form to another is an asymptotically reversible process. $E$ quantifies both what we have to pay in Bell pairs to create $|\psi\rangle$, and the value of $|\psi\rangle$ in Bell pairs for performing tasks like quantum teleportation which consume entanglement.

But what is the value of $E(|\psi\rangle_{AB})$? Perhaps you can guess -- it is
$$
E(|\psi\rangle_{AB}) = H(\bm{\rho}_A) = H(\bm{\rho}_B), \tag{10.171}
$$
the von Neumann entropy of Alice's density operator $\bm{\rho}_A$ (or equivalently Bob's density operator $\bm{\rho}_B$). This is clearly the right answer in the case where $|\psi\rangle_{AB}$ is a product of $k$ Bell pairs. In that case $\bm{\rho}_A$ (or $\bm{\rho}_B$) is $\frac{1}{2}\bm{I}$ for each qubit in Alice's possession
$$
\bm{\rho}_A = \left(\frac{1}{2}\bm{I}\right)^{\otimes k}, \tag{10.172}
$$
and
$$
H(\bm{\rho}_A) = k\, H\left(\frac{1}{2}\bm{I}\right) = k. \tag{10.173}
$$
How do we see that $E = H(\bm{\rho}_A)$ is the right answer for any bipartite pure state?

Though it is perfectly fine to use Bell pairs as the common currency for comparing bipartite entangled states, in the asymptotic setting it is simpler and more natural to allow fractions of a Bell pair, which is what we'll do here. That is, we'll consider a maximally entangled state of two $d$-dimensional systems to be $\log_2 d$ Bell pairs, even if $d$ is not a power of two. So our goal will be to show that Alice and Bob can use LOCC to convert shared maximal entanglement of systems with dimension $d = 2^{n(H(\bm{\rho}_A) + \delta)}$ into $n$ copies of $|\psi\rangle$, for any positive $\delta$ and with arbitrarily good fidelity as $n \to \infty$, and conversely that Alice and Bob can use LOCC to convert $n$ copies of $|\psi\rangle$ into a shared maximally entangled state of $d$-dimensional systems with arbitrarily good fidelity, where $d = 2^{n(H(\bm{\rho}_A) - \delta)}$. This suffices to demonstrate that $E_C(|\psi\rangle) = E_D(|\psi\rangle) = H(\bm{\rho}_A)$.

First let's see that if Alice and Bob share $k = n(H(\bm{\rho}_A) + \delta)$ Bell pairs, then they can prepare $|\psi\rangle_{AB}^{\otimes n}$ with high fidelity using LOCC. They perform this task, called *entanglement dilution*, by combining quantum teleportation with Schumacher compression. To get started, Alice locally creates $n$ copies of $|\psi\rangle_{AC}$, where $A$ and $C$ are systems she controls in her laboratory. Next she wishes to teleport the $C^n$ share of these copies to Bob, but to minimize the consumption of Bell pairs, she should compress $C^n$ before teleporting it.

If $A$ and $C$ are $d$-dimensional, then the bipartite state $|\psi\rangle_{AC}$ can be expressed in terms of its Schmidt basis as
$$
|\psi\rangle_{AC} = \sqrt{p_0}|00\rangle + \sqrt{p_1}|11\rangle + \dots + \sqrt{p_{d-1}}|d-1, d-1\rangle, \tag{10.174}
$$
and $n$ copies of the state can be expressed as
$$
\begin{aligned}
|\psi\rangle_{AC}^{\otimes n} &= \sum_{x_1,\dots,x_n=0}^{d-1} \sqrt{p(x_1)\dots p(x_n)} |x_1 x_2 \dots x_n\rangle_{A^n} \otimes |x_1 x_2 \dots x_n\rangle_{C^n} \\
&= \sum_{\vec{x}} \sqrt{p(\vec{x})} |\vec{x}\rangle_{A^n} \otimes |\vec{x}\rangle_{C^n},
\end{aligned} \tag{10.175}
$$
where $\sum_{\vec{x}} p(\vec{x}) = 1$. If Alice attempts to project onto the $\delta$-typical subspace of $C^n$, she succeeds with high probability
$$
P = \sum_{\delta\text{-typical } \vec{x}} p(\vec{x}) \ge 1 - \varepsilon \tag{10.176}
$$
and when successful prepares the post-measurement state
$$
|\Psi\rangle_{A^n C^n} = P^{-1/2} \sum_{\delta\text{-typical } \vec{x}} \sqrt{p(\vec{x})} |\vec{x}\rangle_{A^n} \otimes |\vec{x}\rangle_{C^n}, \tag{10.177}
$$
such that
$$
\langle\Psi|\psi^{\otimes n}\rangle = P^{-1/2} \sum_{\delta\text{-typical } \vec{x}} p(\vec{x}) = \sqrt{P} \ge \sqrt{1 - \varepsilon}. \tag{10.178}
$$
Since the typical subspace has dimension at most $2^{n(H(\bm{\rho})+\delta)}$, Alice can teleport the $C^n$ half of $|\Psi\rangle$ to Bob with perfect fidelity using no more than $n(H(\bm{\rho}) + \delta)$ Bell pairs shared by Alice and Bob. The teleportation uses LOCC: Alice's entangled measurement, classical communication from Alice to Bob to convey the measurement outcome, and Bob's unitary transformation conditioned on the outcome. Finally, after the teleportation, Bob decompresses, so that Alice and Bob share a state which has high fidelity with $|\psi\rangle_{AB}^{\otimes n}$. This protocol demonstrates that the entanglement cost $E_C$ of $|\psi\rangle$ is not more than $H(\bm{\rho}_A)$.

Now consider the distillable entanglement $E_D$. Suppose Alice and Bob share the state $|\psi\rangle_{AB}^{\otimes n}$. Since $|\psi\rangle_{AB}$ is, in general, a *partially* entangled state, the entanglement that Alice and Bob share is in a diluted form. They wish to *concentrate* their shared entanglement, squeezing it down to the smallest possible Hilbert space; that is, they want to convert it to maximally-entangled pairs. We will show that Alice and Bob can "distill" at least
$$
k' = n(H(\bm{\rho}_A) - \delta) \tag{10.179}
$$
Bell pairs from $|\psi\rangle_{AB}^{\otimes n}$, with high likelihood of success.

To illustrate the concentration of entanglement, imagine that Alice and Bob have $n$ copies of the two-qubit state $|\psi\rangle$, which is
$$
|\psi(p)\rangle = \sqrt{1-p}|00\rangle + \sqrt{p}|11\rangle, \tag{10.180}
$$
where $0 \le p \le 1$, when expressed in its Schmidt basis. That is, Alice and Bob share the state
$$
|\psi(p)\rangle^{\otimes n} = (\sqrt{1-p}|00\rangle + \sqrt{p}|11\rangle)^{\otimes n}. \tag{10.181}
$$
When we expand this state in the $\{|0\rangle, |1\rangle\}$ basis, we find $2^n$ terms, in each of which Alice and Bob hold exactly the same binary string of length $n$.

Now suppose Alice (or Bob) performs a local measurement on her (his) $n$ qubits, measuring the total spin along the $z$-axis
$$
\bm{\sigma}_3^{\mathrm{total}} = \sum_{i=1}^n \bm{\sigma}_3^{(i)}. \tag{10.182}
$$
Equivalently, the measurement determines the Hamming weight of Alice's $n$ qubits, the number of $|1\rangle$'s in Alice's $n$-bit string; that is, the number of spins pointing up.

In the expansion of $|\psi(p)\rangle^{\otimes n}$ there are $\binom{n}{m}$ terms in which Alice's string has Hamming weight $m$, each occurring with the same amplitude: $(1-p)^{(n-m)/2} p^{m/2}$. Hence the probability that Alice's measurement finds Hamming weight $m$ is
$$
p(m) = \binom{n}{m}(1-p)^{n-m}p^m. \tag{10.183}
$$
Furthermore, because Alice is careful not to acquire any additional information besides the Hamming weight when she conducts the measurement, by measuring the Hamming weight $m$ she prepares a uniform superposition of all $\binom{n}{m}$ strings with $m$ up spins.

Because Alice and Bob have perfectly correlated strings, if Bob were to measure the Hamming weight of his qubits he would find the same outcome as Alice. Alternatively, Alice could report her outcome to Bob in a classical message, saving Bob the trouble of doing the measurement himself. Thus, Alice and Bob share a maximally entangled state
$$
\sum_{i=1}^D |i\rangle_A \otimes |i\rangle_B, \tag{10.184}
$$
where the sum runs over the $D = \binom{n}{m}$ strings with Hamming weight $m$.

For $n$ large the binomial distribution $\{p(m)\}$ approaches a sharply peaked function of $m$ with mean $\mu = np$ and variance $\sigma^2 = np(1-p)$. Hence the probability of a large deviation from the mean,
$$
|m - np| = \Omega(n), \tag{10.185}
$$
is $\exp(-\Omega(n))$. Using Stirling's approximation, it then follows that
$$
2^{n(H(p)-o(1))} \le D \le 2^{n(H(p)+o(1))} \tag{10.186}
$$
with probability approaching one as $n \to \infty$, where $H(p) = -p\log_2 p - (1-p)\log_2(1-p)$ is the entropy function. Thus with high probability Alice and Bob share a maximally entangled state of Hilbert spaces $\mathcal{H}_A$ and $\mathcal{H}_B$ with $\dim(\mathcal{H}_A) = \dim(\mathcal{H}_B) = D$ and $\log_2 D \ge n(H(p) - \delta)$. In this sense Alice and Bob can distill $H(p) - \delta$ Bell pairs per copy of $|\psi\rangle_{AB}$.

Though the number $m$ of up spins that Alice (or Bob) finds in her (his) measurement is typically close to $np$, it can fluctuate about this value. Sometimes Alice and Bob will be lucky, and then will manage to distill more than $H(p)$ Bell pairs per copy of $|\psi(p)\rangle_{AB}$. But the probability of doing substantially better becomes negligible as $n \to \infty$.

The same idea applies to bipartite pure states in larger Hilbert spaces. If $A$ and $B$ are $d$-dimensional systems, then $|\psi\rangle_{AB}$ has the Schmidt decomposition
$$
|\psi(X)\rangle_{AB} = \sum_{x=0}^{d-1} \sqrt{p(x)} |x\rangle_A \otimes |x\rangle_B, \tag{10.187}
$$
where $X$ is the classical ensemble $\{x, p(x)\}$, and $H(\bm{\rho}_A) = H(\bm{\rho}_B) = H(X)$. The Schmidt decomposition of $n$ copies of $|\psi\rangle$ is
$$
\sum_{x_1, x_2, \dots, x_n=0}^{d-1} \sqrt{p(x_1)p(x_2)\dots p(x_n)} |x_1 x_2 \dots x_n\rangle_{A^n} \otimes |x_1 x_2 \dots x_n\rangle_{B^n}. \tag{10.188}
$$
Now Alice (or Bob) can measure the total number of $|0\rangle$'s, the total number of $|1\rangle$'s, etc. in her (his) possession. If she finds $m_0$ $|0\rangle$'s, $m_1$ $|1\rangle$'s, etc., then her measurement prepares a maximally entangled state with Schmidt number
$$
D(m_0, m_1, \dots, m_{d-1}) = \frac{n!}{m_0! m_1! \dots m_{d-1}!} \tag{10.189}
$$
and this outcome occurs with probability
$$
p(m) = D(m_0, m_1, \dots, m_{d-1}) p(0)^{m_0} p(1)^{m_1} \dots p(d-1)^{m_{d-1}}. \tag{10.190}
$$
For $n$ large, Alice will typically find $m_x \approx np(x)$, and again the probability of a large deviation is small, so that, from Stirling's approximation
$$
2^{n(H(X)-o(1))} \le D \le 2^{n(H(X)+o(1))} \tag{10.191}
$$
with high probability. Thus, asymptotically for $n \to \infty$, $n(H(\bm{\rho}_A) - o(1))$ high-fidelity Bell pairs can be distilled from $n$ copies of $|\psi\rangle$, establishing that $E_D(|\psi\rangle) \ge H(\bm{\rho}_A)$, and therefore $E_D(|\psi\rangle) = E_C(|\psi\rangle) = E(|\psi\rangle)$.

This entanglement concentration protocol uses local operations but does not require any classical communication. When Alice and Bob do the same measurement they always get the same outcome, so there is no need for them to communicate. Classical communication really is necessary, though, to perform entanglement dilution. The protocol we described here, based on teleportation, requires two bits of classical one-way communication per Bell pair consumed; in a more clever protocol this can be reduced to $O(\sqrt{n})$ bits, but no further. Since the classical communication cost is sublinear in $n$, the number of bits of classical communication needed per copy of $|\psi\rangle$ becomes negligible in the limit $n \to \infty$.

Here we have discussed the entanglement cost and distillable entanglement for bipartite pure states. An achievable rate for distilling Bell pairs from bipartite mixed states will be derived in §10.8.2.
