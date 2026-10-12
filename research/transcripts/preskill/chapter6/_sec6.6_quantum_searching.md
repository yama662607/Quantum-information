# Section 6.6: Quantum Searching [PDF Pages 34-38]

<!-- ============================================================ -->
<!-- Source: chap6.pdf, Physical Pages: 34-38                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 34 -->
## 6.6 Quantum Searching

For the hardest instances of NP-hard problems, no better method is known than exhaustive search for a solution. For example, suppose that for some efficiently computable Boolean function
$$
f : \{0, 1\}^n \longrightarrow \{0, 1\};
$$ {#eq-6.147}
we wish to determine whether there is an $x$ such that $f(x) = 1$. We could search for a solution by trying all of the $N = 2^n$ possible values of the input $x$, but that might require time $O(N \text{polylog} N)$ — assuming we can evaluate $f$ in time $O(\text{polylog} N)$. That's very slow, yet if $f$ has no structure that we know how to exploit, we might not know how to do better.

<!-- Page 35 -->
We can model this situation in the black box setting. Suppose we are promised that the function evaluated by the box has the form
$$
f_w(x) = \begin{cases} 0 & x \neq w, \\ 1 & x = w, \end{cases}
$$ {#eq-6.148}
where $x \in \{0, 1, 2, \dots, N - 1\}$ for some unknown $w$. Our task is to find $w$, the *marked string*. Classically, we'll need to query the box more than $N/2$ times to find $w$ with success probability above $1/2$. This is a black-box version of an NP-hard problem, where there is a unique witness accepted by a circuit, but the problem has no structure, so there is no better option than exhaustive searching.

Now we ask, can exhaustive search be done faster on a quantum computer? The answer is yes, using *Grover's algorithm*. With quantum queries, we can find the marked string using $O(\sqrt{N})$ queries. Thus we can solve NP-hard problems by exhaustive search in time $O(\sqrt{N} \text{polylog} N)$.

We say that Grover's algorithm achieves a *quadratic speedup* relative to exhaustive search on a classical computer. Though the speedup is only quadratic rather than exponential, Grover's algorithm is interesting because of its broad applicability. And it is rather remarkable: in effect we can interrogate $N$ potential witnesses by asking $O(\sqrt{N})$ questions.

In the quantum setting, the black box applies the unitary
$$
U_w : |x\rangle \otimes |y\rangle \mapsto |x\rangle \otimes |y \oplus f_w(x)\rangle,
$$ {#eq-6.149}
where $x \in \{0, 1\}^n$ and $y \in \{0, 1\}^n$. By the standard trick, $U_w$ becomes a *phase oracle*:
$$
U_w : |x\rangle \otimes |-\rangle \mapsto (-1)^{f_w(x)}|x\rangle \otimes |-\rangle
$$ {#eq-6.150}
where
$$
(-1)^{f_w(x)} = \begin{cases} 1 & x \neq w, \\ -1 & x = w. \end{cases}
$$ {#eq-6.151}
Ignoring the output register (which is unaffected by $U_w$), we can express $U_w$ acting on input as
$$
U_w = I - 2|w\rangle\langle w|.
$$ {#eq-6.152}
We can express a general $n$-qubit state $|\psi\rangle$ as
$$
U_w : |\psi\rangle = a|w\rangle + b|\psi^\perp\rangle \mapsto -a|w\rangle + b|\psi^\perp\rangle,
$$ {#eq-6.153}
where $\langle w|\psi^\perp\rangle = 0$. That is, we resolve $|\psi\rangle$ into a component along $|w\rangle$ and a component in the hyperplane orthogonal to $|w\rangle$. $U_w$ induces a reflection of the vector $|\psi\rangle$ about this hyperplane.

The first step in Grover's algorithm is to prepare the uniform superposition of all values of $x$:
$$
|s\rangle = H^{\otimes n}|0\rangle = \frac{1}{\sqrt{N}}\sum_{x=0}^{N-1}|x\rangle;
$$ {#eq-6.154}
this state $|s\rangle$ has overlap with the marked string $|w\rangle$
$$
\langle w|s\rangle = \frac{1}{\sqrt{N}}.
$$ {#eq-6.155}

<!-- Page 36 -->
The next step is to apply the *Grover iteration* many times in succession, where each iteration enhances the overlap of the quantum superposition with the marked state $|w\rangle$, while suppressing the amplitude for each $|x\rangle$ with $x \neq w$. This iteration is
$$
U_{\text{Grover}} = U_s U_w
$$ {#eq-6.156}
where $U_w$ is the query and
$$
U_s = 2|s\rangle\langle s| - I
$$ {#eq-6.157}
reflects a vector about the axis determined by $|s\rangle$. Note that $U_s$ is easy to construct as a quantum circuit. It can be expressed as
$$
U_s = H^{\otimes n}(2|0\rangle\langle 0| - I)H^{\otimes n}
$$ {#eq-6.158}
since $H^{\otimes n}$ maps $|s\rangle$ to $|0\rangle$, where $H$ is the single qubit Hadamard gate. Furthermore a multiply controlled $Z$ gate can be formed from a multiply controlled-not gate $\Lambda^{n-1}(X)$ where the target qubit has a Hadamard before and after the gate, and we know that $\Lambda^{n-1}(X)$ can be constructed from $O(n)$ Toffoli gates. Finally, we can conjugate by $X^{\otimes n}$ so the phase gate is triggered by $|00..0\rangle$ rather than $|11..1\rangle$. Thus $U_s$ is realized by a circuit of size $O(\log N)$.

What does $U_{\text{Grover}}$ do? It preserves the plane spanned by $|s\rangle$ and $|w\rangle$, so we may confine our attention to that plane. First, $U_w$ reflects $|s\rangle$ about the axis $|w^\perp\rangle$ (the vector $\perp$ to $|w\rangle$ in the span of $|s\rangle$ and $|w\rangle$). Then $U_s$ reflects $U_w|s\rangle$ about the axis $|s\rangle$. The net effect of $U_{\text{Grover}}$, then, is a counterclockwise rotation in the plane by the angle $2\theta$, where $\theta$ is initial angle between $|s\rangle$ and $|w\rangle$. Each time we repeat the Grover iteration the state vector rotates further in the counterclockwise direction by $2\theta$.

The initial angle $\theta$ between $|s\rangle$ and $|w^\perp\rangle$ is given by $\sin\theta = \langle w|s\rangle = 1/\sqrt{N}$. For $N \gg 1$, then, we have $\theta = 1/\sqrt{N} + O(1/N^{3/2})$. If we repeat the Grover iteration $T$ times, then the vector is rotated away from the $|w^\perp\rangle$ axis by $(2T + 1)\theta$.

We may choose $T$ such that $(2T + 1)\theta = \pi/2 + \delta$ where $|\delta| \le \theta/2 \approx \frac{1}{2\sqrt{N}}$. Then if we measure in the computational basis, we find the outcome $|w\rangle$ with probability $\text{Prob}(w) = \cos^2\delta \ge 1 - \delta^2 \ge 1 - \frac{1}{4N}$. Thus we find $|w\rangle$ with success probability close to 1 using $T \approx \frac{\pi}{4\theta} \approx \frac{\pi}{4}\sqrt{N}$ Grover iterations, making use of $T$ quantum queries to the black box. This is Grover's quadratic speedup.

Suppose now that there are $r$ marked states, where $r$ is known. Classically, with each query the probability of finding a solution ($w_i$ such that $f(w_i) = 1$) is $r/N$, so we need $O(N/r)$ queries to find a solution with constant success probability. Quantumly, the uniform superposition of the marked states
$$
|\text{marked}\rangle = \frac{1}{\sqrt{r}}\sum_{i=1}^r |w_i\rangle
$$ {#eq-6.159}
has overlap with $|s\rangle = \frac{1}{\sqrt{N}}\sum_{x=0}^{N-1}|x\rangle$
$$
\langle\text{marked}|s\rangle = \sqrt{\frac{r}{N}} = \sin\theta
$$ {#eq-6.160}
and the Grover iteration again rotates by $2\theta$ in the plane spanned by $|s\rangle$ and $|\text{marked}\rangle$ (because the query reflects about the axis perpendicular to $|\text{marked}\rangle$).

As above, then, for $N/r \gg 1$, we achieve success probability $\text{Prob} = 1 - O(r/N)$

<!-- Page 37 -->
in $T \approx \pi/4 \sqrt{N/r}$ queries. Again, the speedup is quadratic: The number of quantum queries needed to find a solution is
$$
\#\text{quantum queries} = O(\sqrt{\#\text{classical queries}}).
$$ {#eq-6.161}
What if $r$ is *not* known a priori? As a function of the number of queries the success probability oscillates, where the period of the oscillation is $T \approx \pi/2\sqrt{N/r}$. If we choose $T$ uniformly at random in the interval $T = \{0, 1, 2, \dots, T_{\max} \approx \pi/4\sqrt{N}\}$, then if there is a solution ($r > 0$), a solution will be found with $\text{Prob} \ge 1/2 + O(1/N)$. If we repeat $m$ times, sampling a different random value of $T$ each time, we will find a solution apart from a small failure probability $\approx 2^{-m}$. Therefore, we can use Grover's algorithm to solve a decision problem in NP with high success probability, in
$$
\text{time} = O(\sqrt{N}\text{polylog} N),
$$ {#eq-6.162}
since we can compute the circuit that evaluates $f(x)$ in (classical or quantum) time $O(\text{polylog} N)$.

### 6.6.1 Generalized Search

In some cases, the problem may have structure that can be exploited to search faster for a solution. In that case, some strings are better candidates than others to be solutions, and so we ought to be able to search more efficiently by spending more time testing likely solutions instead of less likely ones.

For the case of Grover's exhaustive search of a function without any apparent structure, we started the algorithm by preparing
$$
|s\rangle = H^{\otimes n}|0\rangle = \frac{1}{\sqrt{N}}\sum_{x=0}^{N-1}|x\rangle,
$$ {#eq-6.163}
which has overlap $\sin\theta = 1/\sqrt{N}$ with the solution $|w\rangle$, and hence would yield the uniform distribution on $x$ if we measured in the computational basis. For a function with structure we may be able to construct an efficiently computable unitary $U$ such that $U|0\rangle = \sin\theta|w\rangle + \cos\theta|\psi^\perp\rangle$ where $\sin^2\theta > 1/N$. In that case, we can conduct Grover's algorithm with $H^{\otimes n}$ replaced by $U$, and $U_s$ replaced by
$$
\tilde{U}_s = U(2|0\rangle\langle 0| - I)U^\dagger.
$$ {#eq-6.164}
Thus $\tilde{U}_s$ reflects in the axis $U|0\rangle$ rather than $|s\rangle$. The analysis of the algorithm is the same as before, and in the case where there exists a unique solution, we can find it with high probability in $T \approx \frac{\pi}{4\theta} < \frac{\pi}{4}\sqrt{N}$ queries.

Specifically, because of the structure of the function, we might be able to exclude all except $M < N$ inputs as potential solutions. Then, classically, we could find the solution in $O(M)$ queries, while quantumly only $O(\sqrt{M})$ queries suffice, if we can construct $U$ such that
$$
U|0\rangle = \frac{1}{\sqrt{M}}\sum_{i=1}^M |x_i\rangle,
$$ {#eq-6.165}
the uniform superposition of the candidate solutions.

For example, suppose that classical search for a solution can be accelerated by a

<!-- Page 38 -->
classical heuristic — that is, a function $g$ that takes a randomly generated seed $r$ in a set $R$ to a trial solution:
$$
g : r \mapsto g(r) \quad \text{where } r \in R.
$$ {#eq-6.166}
The heuristic is useful if trial solutions generated by the heuristic are more likely to be accepted than trial solutions chosen uniformly at random
$$
\left\langle \frac{\# \text{ of soln. in } g(R)}{|R|} \right\rangle > \left\langle \frac{\text{total } \# \text{ of soln.}}{N} \right\rangle,
$$ {#eq-6.167}
where the bracket $\langle\cdot\rangle$ indicates the expectation value evaluated for a probability distribution on black-box functions. Then the number of classical queries to find a solution, using the heuristic, with constant success probability is
$$
T_{\text{classical}} = O\left( \left\langle \frac{|R|}{\# \text{ of soln. in } g(R)} \right\rangle \right).
$$ {#eq-6.168}
To exploit the heuristic in quantum searching, we apply Grover's algorithm to searching in the space of seeds instead of the full search space. The heuristic is realized as an efficiently computable unitary:
$$
|r\rangle \otimes |0\rangle \mapsto |r\rangle \otimes |g(r)\rangle.
$$ {#eq-6.169}
We can query the box with $|g(r)\rangle$ and then run the evaluation of $g$ backwards to erase garbage:
$$
\begin{aligned}
|r\rangle \otimes |0\rangle \otimes |y\rangle &\mapsto |r\rangle \otimes |g(r)\rangle \otimes |y\rangle \mapsto |r\rangle \otimes |g(r)\rangle \otimes |y \oplus f(g(r))\rangle \\
&\mapsto |r\rangle \otimes |0\rangle \otimes |y \oplus f(g(r))\rangle
\end{aligned}
$$ {#eq-6.170}
This composite oracle can be consulted to search $R$ for a state marked by the function $f \circ g$ (i.e. for a state marked by $f$ in $g(R)$, the range of $g$). The number of quantum queries used is
$$
T_{\text{quantum}} = O\left( \left\langle \sqrt{\frac{|R|}{\# \text{ of soln. in } g(R)}} \right\rangle \right)
$$ {#eq-6.171}
(for each black box there is a quadratic speed up). Furthermore, the square root function is concave: $\langle\sqrt{F}\rangle = \sum_a p_a \sqrt{F_a} \le \sqrt{\sum_a p_a F_a} = \sqrt{\langle F\rangle}$ where $\{p_a\}$ is a probability distribution, and here $F_a$ represents the classical query complexity for a black box function labeled by $a$. Thus,
$$
T_{\text{quantum}} \le O\left( \sqrt{\left\langle \frac{|R|}{\# \text{ of soln. in } g(R)} \right\rangle} \right) = O(\sqrt{T_{\text{classical}}}).
$$ {#eq-6.172}
The speedup is quadratic, as for unstructured search.
