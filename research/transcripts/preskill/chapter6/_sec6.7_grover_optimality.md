# Section 6.7: The Grover Algorithm Is Optimal [PDF Pages 38-41]

<!-- ============================================================ -->
<!-- Source: chap6.pdf, Physical Pages: 38-41                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 38 -->
## 6.7 The Grover Algorithm Is Optimal

Grover's quadratic quantum speedup for exhaustive search is already interesting and potentially important, but surely with more cleverness we can do better, can't we?

No, it turns out that we can't. Grover's algorithm provides the fastest possible quantum search of an unsorted database, if "time" is measured according to the number of queries of the oracle.

Considering the case of a single marked state $|\omega\rangle$, let $\boldsymbol{U}(\omega, T)$ denote a quantum circuit

<!-- Page 39 -->
that calls the oracle $T$ times. We place *no* restriction on the circuit aside from specifying the number of queries; in particular, we place no limit on the number of quantum gates. This circuit is applied to an initial state $|\psi(0)\rangle$, producing a final state
$$
|\psi_\omega(T)\rangle = \boldsymbol{U}(\omega, T)|\psi(0)\rangle.
$$ {#eq-6.173}
Now we are to perform a measurement designed to distinguish among the $N$ possible values of $\omega$. If we are to be able to perfectly distinguish among the possible values, the states $|\psi_\omega(T)\rangle$ must all be mutually orthogonal, and if we are to distinguish correctly with high probability, they must be nearly orthogonal.

Now, if the states $\{|\psi_\omega\rangle\}$ are an orthonormal basis, then, for any fixed normalized vector $|\varphi\rangle$,
$$
\sum_{\omega=0}^{N-1} \| |\psi_\omega\rangle - |\varphi\rangle \|^2 \ge 2N - 2\sqrt{N}.
$$ {#eq-6.174}
(The sum is minimized if $|\varphi\rangle$ is the equally weighted superposition of all the basis elements, $|\varphi\rangle = \frac{1}{\sqrt{N}}\sum_\omega |\psi_\omega\rangle$, as you can show by invoking a Lagrange multiplier to perform the constrained extremization.) Our strategy will be to choose the state $|\varphi\rangle$ suitably so that we can use this inequality to learn something about the number $T$ of oracle calls.

Our circuit with $T$ queries builds a unitary transformation
$$
\boldsymbol{U}(\omega, T) = \boldsymbol{U}_\omega \boldsymbol{U}_T \boldsymbol{U}_\omega \boldsymbol{U}_{T-1} \dots \boldsymbol{U}_\omega \boldsymbol{U}_1,
$$ {#eq-6.175}
where $\boldsymbol{U}_\omega$ is the oracle transformation, and the $\boldsymbol{U}_t$'s are arbitrary non-oracle transformations. For our state $|\varphi(T)\rangle$ we will choose the result of applying $\boldsymbol{U}(\omega, T)$ to $|\psi(0)\rangle$, except with each $\boldsymbol{U}_\omega$ replaced by $\boldsymbol{I}$; that is, the same circuit, but with all queries submitted to the "empty oracle." Hence,
$$
|\varphi(T)\rangle = \boldsymbol{U}_T \boldsymbol{U}_{T-1} \dots \boldsymbol{U}_2 \boldsymbol{U}_1 |\psi(0)\rangle,
$$ {#eq-6.176}
while
$$
|\psi_\omega(T)\rangle = \boldsymbol{U}_\omega \boldsymbol{U}_T \boldsymbol{U}_\omega \boldsymbol{U}_{T-1} \dots \boldsymbol{U}_\omega \boldsymbol{U}_1 |\psi(0)\rangle.
$$ {#eq-6.177}
To compare $|\varphi(T)\rangle$ and $|\psi_\omega(T)\rangle$, we appeal to our previous analysis of the effect of errors on the accuracy of a circuit, regarding the $\omega$ oracle as an "erroneous" implementation of the empty oracle. The norm of the error vector in the $t$-th step is
$$
\begin{aligned}
\| |E(\omega, t)\rangle \| &= \| (\boldsymbol{U}_\omega - \boldsymbol{I})|\varphi(t)\rangle \| \\
&= 2|\langle\omega|\varphi(t)\rangle|,
\end{aligned}
$$ {#eq-6.178}
since $\boldsymbol{U}_\omega = \boldsymbol{I} - 2|\omega\rangle\langle\omega|$. After $T$ queries we have
$$
\| |\psi_\omega(T)\rangle - |\varphi(T)\rangle \| \le 2\sum_{t=1}^T |\langle\omega|\varphi(t)\rangle|.
$$ {#eq-6.179}

<!-- Page 40 -->
From the identity
$$
\begin{aligned}
\left(\sum_{t=1}^T c_t\right)^2 + \frac{1}{2}\sum_{s,t=1}^T (c_s - c_t)^2 &= \sum_{s,t=1}^T \left(c_t c_s + \frac{1}{2}c_s^2 - c_t c_s + \frac{1}{2}c_t^2\right) \\
&= T\sum_{t=1}^T c_t^2,
\end{aligned}
$$ {#eq-6.180}
we obtain the inequality
$$
\left(\sum_{t=1}^T c_t\right)^2 \le T\sum_{t=1}^T c_t^2,
$$ {#eq-6.181}
which applied to eq. (6.179) yields
$$
\| |\psi_\omega(T)\rangle - |\varphi(T)\rangle \|^2 \le 4T\left(\sum_{t=1}^T |\langle\omega|\varphi(t)\rangle|^2\right).
$$ {#eq-6.182}
Summing over $\omega$ we find
$$
\sum_\omega \| |\psi_\omega(T)\rangle - |\varphi(T)\rangle \|^2 \le 4T\sum_{t=1}^T \langle\varphi(t)|\varphi(t)\rangle = 4T^2.
$$ {#eq-6.183}
Invoking eq. (6.174) we conclude that
$$
4T^2 \ge 2N - 2\sqrt{N},
$$ {#eq-6.184}
if the states $|\psi_\omega(T)\rangle$ are mutually orthogonal. We have, therefore, found that any quantum algorithm that can distinguish all the possible values of the marked state must query the oracle $T$ times where
$$
T \ge \sqrt{\frac{N}{2}},
$$ {#eq-6.185}
(ignoring the small correction as $N \to \infty$). This lower bound on the number of queries applies if we are to identify the marked state with a success probability that approaches one for asymptotically large $N$. A simple extension of argument shows that
$$
T \ge \sqrt{\frac{N}{2}}(1 - \sqrt{\varepsilon})^{1/2},
$$ {#eq-6.186}
if instead we settle for success probability at least $1 - \varepsilon$ for each possible choice of the marked string $\omega$.

Grover's algorithm finds $\omega$ in $\frac{\pi}{4}\sqrt{N}$ queries, which exceeds our lower bound by only about 11%. In fact, by a more careful argument, we can derive a tighter lower bound on the number of queries that asymptotically matches what Grover's algorithm achieves. Furthermore, we can show that Grover's circuit attains the best success probability among all circuits with $T$ oracle calls in the case where $T < \frac{\pi}{4}\sqrt{N}$.

One feels a twinge of disappointment (as well as a surge of admiration for Grover) at the realization that the quantum search algorithm cannot be improved in the black box setting. What are the implications for quantum complexity?

For many optimization problems in the NP class, there is no better method known than exhaustive search of all the possible solutions. By exploiting quantum parallelism, we can achieve a quadratic speedup of exhaustive search. Now we have learned that

<!-- Page 41 -->
the quadratic speedup is the best possible if we rely on the power of sheer quantum parallelism — that is, if we don't design our quantum algorithm to exploit the specific structure of the problem we wish to solve.

The optimality of the Grover algorithm might be construed as evidence that $\text{BQP} \not\supseteq \text{NP}$. At least, if it turns out that $\text{NP} \subseteq \text{BQP}$ and $\text{P} \neq \text{NP}$, then the NP problems must share a deeply hidden structure (for which there is currently no evidence) that is well-matched to the peculiar capabilities of quantum circuits.

Even the quadratic speedup may prove useful for a variety of NP-complete optimization problems. But a quadratic speedup, unlike an exponential one, does not really move the frontier between solvability and intractability. Quantum computers may someday outperform classical computers in performing exhaustive search, but only if the clock speed of quantum devices does not lag too far behind that of their classical counterparts.
