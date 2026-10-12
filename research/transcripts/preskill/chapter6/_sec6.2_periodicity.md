# Section 6.2: Periodicity & QFT [PDF Pages 13-18]

<!-- ============================================================ -->
<!-- Source: chap6.pdf, Physical Pages: 13-18                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 13 -->
## 6.2 Periodicity

So far, the one case for which we have found an exponential separation between the speed of a quantum algorithm and the speed of the corresponding classical algorithm is the case of Simon's problem. Simon's algorithm exploits quantum parallelism to speed up the search for the period of a function. Its success encourages us to seek other quantum algorithms designed for other kinds of period finding.

Simon studied periodic functions taking values in $(Z_2)^n$. For that purpose the $n$-bit Hadamard transform $\boldsymbol{H}^{(n)}$ was a powerful tool. If we wish instead to study periodic functions taking values in $Z_{2^n}$, the (discrete) Fourier transform will be a tool of comparable power.

The moral of Simon's problem is that, while finding needles in a haystack may be difficult, finding *periodically* spaced needles in a haystack can be far easier. For example, if we scatter a photon off of a periodic array of needles, the photon is likely to be scattered in one of a set of preferred directions, where the Bragg scattering condition is satisfied. These preferred directions depend on the spacing between the needles, so by scattering just one photon, we can already collect some useful information about the spacing. We should further explore the implications of this metaphor for the construction of efficient quantum algorithms.

So imagine a quantum oracle that computes a function
$$
f : \{0, 1\}^n \to \{0, 1\}^m,
$$ {#eq-6.27}
that has an unknown period $r$, where $r$ is a positive integer satisfying
$$
1 \ll r \ll 2^n.
$$ {#eq-6.28}
That is,
$$
f(x) = f(x + mr),
$$ {#eq-6.29}
where $m$ is any integer such that $x$ and $x + mr$ lie in $\{0, 1, 2, \dots, 2^n - 1\}$. We are to find the period $r$. Classically, this problem is *hard*. If $r$ is, say, of order $2^{n/2}$, we will need to query the oracle of order $2^{n/4}$ times before we are likely to find two values of $x$ that are mapped to the same value of $f(x)$, and hence learn something about $r$. But we will see that there is a quantum algorithm that finds $r$ in time $\text{poly}(n)$.

Even if we know how to compute efficiently the function $f(x)$, it may be a hard problem to determine its period. Our quantum algorithm can be applied to finding, in $\text{poly}(n)$ time, the period of any function that we can compute in $\text{poly}(n)$ time. Efficient period finding allows us to efficiently solve a variety of (apparently) hard problems, such as factoring an integer, or evaluating a discrete logarithm.

The key idea underlying quantum period finding is that the Fourier transform can be evaluated by an efficient quantum circuit (as discovered by Peter Shor). The quantum Fourier transform (QFT) exploits the power of quantum parallelism to achieve an exponential speedup of the well-known (classical) fast Fourier transform (FFT). Since the FFT has such a wide variety of applications, perhaps the QFT will also come into widespread use someday.

<!-- Page 14 -->
### 6.2.1 Finding the period

The QFT is the unitary transformation that acts on the computational basis according to
$$
\text{QFT} : |x\rangle \to \frac{1}{\sqrt{N}} \sum_{y=0}^{N-1} e^{2\pi i x y / N} |y\rangle,
$$ {#eq-6.30}
where $N = 2^n$. For now let's suppose that we can perform the QFT efficiently, and see how it enables us to extract the period of $f(x)$.

Emulating Simon's algorithm, we first query the oracle with the input $\frac{1}{\sqrt{N}}\sum_x |x\rangle$ (easily prepared by applying $\boldsymbol{H}^{(n)}$ to $|0\rangle$), and so prepare the state
$$
\frac{1}{\sqrt{N}} \sum_{x=0}^{N-1} |x\rangle |f(x)\rangle.
$$ {#eq-6.31}
Then we measure the output register, obtaining the result $|f(x_0)\rangle$ for some $0 \le x_0 < r$. This measurement prepares in the input register the coherent superposition of the $A$ values of $x$ that are mapped to $f(x_0)$:
$$
\frac{1}{\sqrt{A}} \sum_{j=0}^{A-1} |x_0 + jr\rangle,
$$ {#eq-6.32}
where
$$
N - r \le x_0 + (A - 1)r < N,
$$ {#eq-6.33}
or
$$
A - 1 < \frac{N}{r} < A + 1.
$$ {#eq-6.34}
Actually, the measurement of the output register is unnecessary. If it is omitted, the state of the input register is an incoherent superposition (summed over $x_0 \in \{0, 1, \dots r-1\}$) of states of the form eq. (6.32). The rest of the algorithm works just as well acting on this initial state.

Now our task is to extract the value of $r$ from the state eq. (6.32) that we have prepared. Were we to measure the input register by projecting onto the computational basis at this point, we would learn nothing about $r$. Instead (cf. Simon's algorithm), we should Fourier transform first and *then* measure.

By applying the QFT to the state eq. (6.32) we obtain
$$
\frac{1}{\sqrt{NA}} \sum_{y=0}^{N-1} e^{2\pi i x_0 y / N} \sum_{j=0}^{A-1} e^{2\pi i j r y / N} |y\rangle.
$$ {#eq-6.35}
If we now measure in the computational basis, the probability of obtaining the outcome $y$ is
$$
\text{Prob}(y) = \frac{A}{N} \left| \frac{1}{A} \sum_{j=0}^{A-1} e^{2\pi i j r y / N} \right|^2.
$$ {#eq-6.36}
This distribution strongly favors values of $y$ such that $yr/N$ is close to an integer. For

<!-- Page 15 -->
example, if $N/r$ happened to be an integer (and therefore equal to $A$), we would have
$$
\text{Prob}(y) = \frac{1}{r} \left| \frac{1}{A} \sum_{j=0}^{A-1} e^{2\pi i j y / A} \right|^2 = \begin{cases} \frac{1}{r} & y = A \cdot (\text{integer}) \\ 0 & \text{otherwise.} \end{cases}
$$ {#eq-6.37}
More generally, we may sum the geometric series
$$
\sum_{j=0}^{A-1} e^{i\theta j} = \frac{e^{iA\theta} - 1}{e^{i\theta} - 1},
$$ {#eq-6.38}
where
$$
\theta_y = \frac{2\pi y r (\text{mod } N)}{N}.
$$ {#eq-6.39}
There are precisely $r$ values of $y$ in $\{0, 1, \dots, N - 1\}$ that satisfy
$$
-\frac{r}{2} \le yr (\text{mod } N) \le \frac{r}{2}.
$$ {#eq-6.40}
(To see this, imagine marking the multiples of $r$ and $N$ on a number line ranging from $0$ to $rN - 1$. For each multiple of $N$, there is a multiple of $r$ no more than distance $r/2$ away.) For each of these values, the corresponding $\theta_y$ satisfies
$$
-\pi \frac{r}{N} \le \theta_y \le \pi \frac{r}{N}.
$$ {#eq-6.41}
Now, since $A - 1 < \frac{N}{r}$, for these values of $\theta_y$ all of the terms in the sum over $j$ in eq. (6.38) lie in the same half-plane, so that the terms interfere constructively and the sum is substantial.

We know that
$$
|1 - e^{i\theta}| \le |\theta|,
$$ {#eq-6.42}
because the straight-line distance from the origin is less than the arc length along the circle, and for $A|\theta| \le \pi$, we know that
$$
|1 - e^{iA\theta}| \ge \frac{2A|\theta|}{\pi},
$$ {#eq-6.43}
because we can see (either graphically or by evaluating its derivative) that this distance is a convex function. We actually have $A < \frac{N}{r} + 1$, and hence $A\theta_y < \pi\left(1 + \frac{r}{N}\right)$, but by applying the above bound to
$$
\left| \frac{e^{i(A-1)\theta} - 1}{e^{i\theta} - 1} + e^{i(A-1)\theta} \right| \ge \left| \frac{e^{i(A-1)\theta} - 1}{e^{i\theta} - 1} \right| - 1,
$$ {#eq-6.44}
we can still conclude that
$$
\left| \frac{e^{iA\theta} - 1}{e^{i\theta} - 1} \right| \ge \frac{2(A-1)|\theta|}{\pi |\theta|} - 1 = \frac{2}{\pi} A - \left(1 + \frac{2}{\pi}\right).
$$ {#eq-6.45}
Ignoring a possible correction of order $2/A$, then, we find
$$
\text{Prob}(y) \ge \left(\frac{4}{\pi^2}\right) \frac{1}{r},
$$ {#eq-6.46}

<!-- Page 16 -->
for each of the $r$ values of $y$ that satisfy eq. (6.40). Therefore, with a probability of at least $4/\pi^2$, the measured value of $y$ will satisfy
$$
k \frac{N}{r} - \frac{1}{2} \le y \le k \frac{N}{r} + \frac{1}{2},
$$ {#eq-6.47}
or
$$
\frac{k}{r} - \frac{1}{2N} \le \frac{y}{N} \le \frac{k}{r} + \frac{1}{2N},
$$ {#eq-6.48}
where $k$ is an integer chosen from $\{0, 1, \dots, r-1\}$. The output of the computation is reasonably likely to be within distance $1/2$ of an integer multiple of $N/r$.

Suppose that we know that $r < M \ll N$. Thus $N/r$ is a rational number with a denominator less than $M$. Two distinct rational numbers, each with denominator less than $M$, can be no closer together than $1/M^2$, since $\frac{a}{b} - \frac{c}{d} = \frac{ad-bc}{bd}$. If the measurement outcome $y$ satisfies eq. (6.47), then there is a *unique* value of $k/r$ (with $r < M$) determined by $y/N$, provided that $N \ge M^2$. This value of $k/r$ can be efficiently extracted from the measured $y/N$, by the continued fraction method.

Now, with probability exceeding $4/\pi^2$, we have found a value of $k/r$ where $k$ is selected (roughly equiprobably) from $\{0, 1, 2, \dots, r-1\}$. It is reasonably likely that $k$ and $r$ are relatively prime (have no common factor), so that we have succeeded in finding $r$. With a query of the oracle, we may check whether $f(x) = f(x+r)$. But if $\text{GCD}(k, r) \neq 1$, we have found only a factor ($r_1$) of $r$.

If we did not succeed, we could test some nearby values of $y$ (the measured value might have been close to the range $-r/2 \le yr(\text{mod } N) \le r/2$ without actually lying inside), or we could try a few multiples of $r$ (the value of $\text{GCD}(k, r)$, if not 1, is probably not large). That failing, we resort to a repetition of the quantum circuit, this time (with probability at least $4/\pi^2$) obtaining a value $k'/r$. Now $k'$, too, may have a common factor with $r$, in which case our procedure again determines a factor ($r_2$) of $r$. But it is reasonably likely that $\text{GCD}(k, k') = 1$, in which case $r = \text{LCM}(r_1, r_2)$. Indeed, we can estimate the probability that randomly selected $k$ and $k'$ are relatively prime as follows: Since a prime number $p$ divides a fraction $1/p$ of all numbers, the probability that $p$ divides both $k$ and $k'$ is $1/p^2$. And $k$ and $k'$ are coprime if and only if there is no prime $p$ that divides both. Therefore,
$$
\text{Prob}(k, k' \text{ coprime}) = \prod_{\text{prime } p} \left(1 - \frac{1}{p^2}\right) = \frac{1}{\zeta(2)} = \frac{6}{\pi^2} \simeq .607
$$ {#eq-6.49}
(where $\zeta(z)$ denotes the Riemann zeta function). Therefore, we are likely to succeed in finding the period $r$ after some constant number (independent of $N$) of repetitions of the algorithm.

### 6.2.2 From FFT to QFT

Now let's consider the implementation of the quantum Fourier transform. The Fourier transform
$$
\sum_x f(x)|x\rangle \to \sum_y \left(\frac{1}{\sqrt{N}}\sum_x e^{2\pi i x y / N} f(x)\right)|y\rangle,
$$ {#eq-6.50}
is multiplication by an $N \times N$ unitary matrix, where the $(x, y)$ matrix element is $(e^{2\pi i / N})^{xy}$. Naively, this transform requires $O(N^2)$ elementary operations. But there is a

<!-- Page 17 -->
well-known and very useful (classical) procedure that reduces the number of operations to $O(N \log N)$. Assuming $N = 2^n$, we express $x$ and $y$ as binary expansions
$$
\begin{aligned}
x &= x_{n-1} \cdot 2^{n-1} + x_{n-2} \cdot 2^{n-2} + \dots + x_1 \cdot 2 + x_0 \\
y &= y_{n-1} \cdot 2^{n-1} + y_{n-2} \cdot 2^{n-2} + \dots + y_1 \cdot 2 + y_0.
\end{aligned}
$$ {#eq-6.51}
In the product of $x$ and $y$, we may discard any terms containing $n$ or more powers of 2, as these make no contribution to $e^{2\pi i x y / 2^n}$. Hence
$$
\begin{aligned}
\frac{xy}{2^n} &\equiv y_{n-1}(.x_0) + y_{n-2}(.x_1x_0) + y_{n-3}(.x_2x_1x_0) + \dots \\
&\quad + y_1(.x_{n-2}x_{n-3}\dots x_0) + y_0(.x_{n-1}x_{n-2}\dots x_0),
\end{aligned}
$$ {#eq-6.52}
where the factors in parentheses are binary expansions; e.g.,
$$
.x_2x_1x_0 = \frac{x_2}{2} + \frac{x_1}{2^2} + \frac{x_0}{2^3}.
$$ {#eq-6.53}
We can now evaluate
$$
\tilde{f}(x) = \frac{1}{\sqrt{N}}\sum_y e^{2\pi i x y / N} f(y),
$$ {#eq-6.54}
for each of the $N$ values of $x$. But the sum over $y$ factors into $n$ sums over $y_k = 0, 1$, which can be done sequentially in a time of order $n$.

With quantum parallelism, we can do far better. From eq. (6.52) we obtain
$$
\begin{aligned}
\text{QFT} : |x\rangle &\to \frac{1}{\sqrt{N}}\sum_y e^{2\pi i x y / N}|y\rangle \\
&= \frac{1}{\sqrt{2^n}}\left(|0\rangle + e^{2\pi i (.x_0)}|1\rangle\right)\left(|0\rangle + e^{2\pi i (.x_1x_0)}|1\rangle\right)\dots\left(|0\rangle + e^{2\pi i (.x_{n-1}x_{n-2}\dots x_0)}|1\rangle\right).
\end{aligned}
$$ {#eq-6.55}
The QFT takes each computational basis state to an *unentangled* state of $n$ qubits; thus we anticipate that it can be efficiently implemented. Indeed, let's consider the case $n = 3$. We can readily see that the circuit

```
|x₂⟩ ───[ H ]───[ R₁ ]───[ R₂ ]─────────────────────── |y₀⟩
                  │        │
|x₁⟩ ─────────────●────────┼───────[ H ]───[ R₁ ]───── |y₁⟩
                           │                 │
|x₀⟩ ──────────────────────●─────────────────●───[ H ] |y₂⟩
```

does the job (but note that the order of the bits has been reversed in the output). Each Hadamard gate acts as
$$
\boldsymbol{H} : |x_k\rangle \to \frac{1}{\sqrt{2}}\left(|0\rangle + e^{2\pi i (.x_k)}|1\rangle\right).
$$ {#eq-6.56}
The other contributions to the relative phase of $|0\rangle$ and $|1\rangle$ in the $k$th qubit are provided by the two-qubit conditional rotations, where
$$
\boldsymbol{R}_d = \begin{pmatrix} 1 & 0 \\ 0 & e^{i\pi / 2^d} \end{pmatrix},
$$ {#eq-6.57}

<!-- Page 18 -->
and $d = (k - j)$ is the "distance" between the qubits.

In the case $n = 3$, the QFT is constructed from three $\boldsymbol{H}$ gates and three controlled-$\boldsymbol{R}$ gates. For general $n$, the obvious generalization of this circuit requires $n$ $\boldsymbol{H}$ gates and $\binom{n}{2} = \frac{1}{2}n(n-1)$ controlled $\boldsymbol{R}$'s. A two qubit gate is applied to each pair of qubits, again with controlled relative phase $\pi/2^d$, where $d$ is the "distance" between the qubits. Thus the circuit family that implements QFT has a size of order $(\log N)^2$.

We can reduce the circuit complexity to linear in $\log N$ if we are willing to settle for an implementation of fixed accuracy, because the two-qubit gates acting on distantly separated qubits contribute only exponentially small phases. If we drop the gates acting on pairs with distance greater than $m$, than each term in eq. (6.52) is replaced by an approximation to $m$ bits of accuracy; the total error in $xy/2^n$ is certainly no worse than $n 2^{-m}$, so we can achieve accuracy $\varepsilon$ in $xy/2^n$ with $m \ge \log n/\varepsilon$. If we retain only the gates acting on qubit pairs with distance $m$ or less, then the circuit size is $mn \sim n \log n/\varepsilon$.

In fact, if we are going to measure in the computational basis immediately after implementing the QFT (or its inverse), a further simplification is possible – no two-qubit gates are needed at all! We first remark that the controlled-$\boldsymbol{R}_d$ gate acts symmetrically on the two qubits – it acts trivially on $|00\rangle$, $|01\rangle$, and $|10\rangle$, and modifies the phase of $|11\rangle$ by $e^{i\theta_d}$. Thus, we can interchange the "control" and "target" bits without modifying the gate. With this change, our circuit for the 3-qubit QFT can be redrawn as:

```
|x₂⟩ ───[ H ]───●────────●──────────────────────────── |y₀⟩
                │        │
|x₁⟩ ──────────[ R₁ ]───[ H ]──────●────────────────── |y₁⟩
                                   │
|x₀⟩ ───────────────────[ R₂ ]────[ R₁ ]───[ H ]────── |y₂⟩
```

Once we have measured $|y_0\rangle$, we *know* the value of the control bit in the controlled-$\boldsymbol{R}_1$ gate that acted on the first two qubits. Therefore, we will obtain the same probability distribution of measurement outcomes if, instead of applying controlled-$\boldsymbol{R}_1$ and then measuring, we instead measure $y_0$ first, and then apply $(\boldsymbol{R}_1)^{y_0}$ to the next qubit, conditioned on the outcome of the measurement of the first qubit. Similarly, we can replace the controlled-$\boldsymbol{R}_1$ and controlled-$\boldsymbol{R}_2$ gates acting on the third qubit by the single qubit rotation
$$
(\boldsymbol{R}_2)^{y_0}(\boldsymbol{R}_1)^{y_1},
$$ {#eq-6.58}
(that is, a rotation with relative phase $\pi(.y_1y_0)$) *after* the values of $y_1$ and $y_0$ have been measured.

Altogether then, if we are going to measure after performing the QFT, only $n$ Hadamard gates and $n - 1$ single-qubit rotations are needed to implement it. The QFT is remarkably simple!
