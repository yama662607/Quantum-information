# Section 6.1: Some Quantum Algorithms [PDF Pages 7-12]

<!-- ============================================================ -->
<!-- Source: chap6.pdf, Physical Pages: 7-12                       -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 7 -->
# 6 Quantum Algorithms

## 6.1 Some Quantum Algorithms

While we are not yet able to show that $BPP \neq BQP$, there are three approaches that we can pursue to study the differences between the capabilities of classical and quantum computers:

(1) **Nonexponential speedup.** We can find quantum algorithms that are demonstrably faster than the best classical algorithm, but not *exponentially* faster. These algorithms shed no light on the conventional classification of complexity. But they do demonstrate a type of separation between tasks that classical and quantum computers can perform. Example: Grover's quantum speedup of the search of an unsorted data base.

(2) **"Relativized" exponential speedup.** We can consider the problem of analyzing the contents of a "quantum black box." The box performs an (*a priori* unknown) unitary transformation. We can prepare an input for the box, and we can measure its output; our task is to find out what the box does. It is possible to prove that quantum black boxes (computer scientists call them oracles[^1]) exist with this property: By feeding quantum superpositions to the box, we can learn what is inside with an *exponential* speedup, compared to how long it would take if we were only allowed classical inputs. A computer scientist would say that $BPP \neq BQP$ "relative to the oracle." Example: Simon's exponential quantum speedup for finding the period of a 2 to 1 function.

(3) **Exponential speedup for "apparently" hard problems.** We can exhibit a quantum algorithm that solves a problem in polynomial time, where the problem appears to be hard classically, so that it is strongly suspected (though not proved) that the problem is not in $BPP$. Example: Shor's factoring algorithm.

**Deutsch's problem.** We will discuss examples from all three approaches. But first, we'll warm up by recalling an example of a simple quantum algorithm that was previously discussed in §1.5: Deutsch's algorithm for distinguishing between constant and balanced functions $f : \{0, 1\} \to \{0, 1\}$. We are presented with a quantum black box that computes $f(x)$; that is, it enacts the two-qubit unitary transformation
$$
U_f : |x\rangle|y\rangle \to |x\rangle|y \oplus f(x)\rangle,
$$ {#eq-6.1}
which flips the second qubit iff $f(\text{first qubit}) = 1$. Our assignment is to determine

[^1]: The term "oracle" signifies that the box responds to a query *immediately*; that is, the time it takes the box to operate is not included in the complexity analysis.

<!-- Page 8 -->
whether $f(0) = f(1)$. If we are restricted to the "classical" inputs $|0\rangle$ and $|1\rangle$, we need to access the box twice ($x = 0$ and $x = 1$) to get the answer. But if we are allowed to input a coherent superposition of these "classical" states, then once is enough.

The quantum circuit that solves the problem (discussed in §1.5) is:

```
|0⟩ ──────[ H ]──────●──────[ H ]────── Measure
                     │
|1⟩ ──────[ H ]───[ U_f ]────────────────
```

Here $H$ denotes the Hadamard transform
$$
H : |x\rangle \to \frac{1}{\sqrt{2}} \sum_y (-1)^{xy}|y\rangle,
$$ {#eq-6.2}
or
$$
\begin{aligned}
H : |0\rangle &\to \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \\
|1\rangle &\to \frac{1}{\sqrt{2}}(|0\rangle - |1\rangle);
\end{aligned}
$$ {#eq-6.3}
that is, $H$ is the $2 \times 2$ matrix
$$
H : \begin{pmatrix} \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} \end{pmatrix}.
$$ {#eq-6.4}

The circuit takes the input $|0\rangle|1\rangle$ to
$$
\begin{aligned}
|0\rangle|1\rangle &\to \frac{1}{2}(|0\rangle + |1\rangle)(|0\rangle - |1\rangle) \\
&\to \frac{1}{2}\left((-1)^{f(0)}|0\rangle + (-1)^{f(1)}|1\rangle\right)(|0\rangle - |1\rangle) \\
&\to \frac{1}{2}\left[\left((-1)^{f(0)} + (-1)^{f(1)}\right)|0\rangle + \left((-1)^{f(0)} - (-1)^{f(1)}\right)|1\rangle\right]\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle).
\end{aligned}
$$ {#eq-6.5}

Then when we measure the first qubit, we find the outcome $|0\rangle$ with probability one if $f(0) = f(1)$ (constant function) and the outcome $|1\rangle$ with probability one if $f(0) \neq f(1)$ (balanced function).

A quantum computer enjoys an advantage over a classical computer because it can invoke *quantum parallelism*. Because we input a superposition of $|0\rangle$ and $|1\rangle$, the output is sensitive to both the values of $f(0)$ and $f(1)$, even though we ran the box just once.

**Deutsch–Jozsa problem.** Now we'll consider some generalizations of Deutsch's problem. We will continue to assume that we are to analyze a quantum black box ("quantum oracle"). But in the hope of learning something about complexity, we will imagine that we have a family of black boxes, with variable input size. We are interested in how the time needed to find out what is inside the box scales with the size of the input (where "time" is measured by how many times we query the box).

<!-- Page 9 -->
In the *Deutsch–Jozsa problem*, we are presented with a quantum black box that computes a function taking $n$ bits to 1,
$$
f : \{0, 1\}^n \to \{0, 1\},
$$ {#eq-6.6}
and we have it on good authority that $f$ is either constant ($f(x) = c$ for all $x$) or balanced ($f(x) = 0$ for exactly $\frac{1}{2}$ of the possible input values). We are to solve the decision problem: Is $f$ constant or balanced?

In fact, we can solve this problem, too, accessing the box only once, using the same circuit as for Deutsch's problem (but with $x$ expanded from one bit to $n$ bits). We note that if we apply $n$ Hadamard gates in parallel to $n$-qubits,
$$
H^{(n)} = H \otimes H \otimes \dots \otimes H,
$$ {#eq-6.7}
then the $n$-qubit state transforms as
$$
H^{(n)} : |x\rangle \to \prod_{i=1}^n \left(\frac{1}{\sqrt{2}} \sum_{y_i \in \{0, 1\}} (-1)^{x_i y_i}|y_i\rangle\right) \equiv \frac{1}{2^{n/2}} \sum_{y=0}^{2^n-1} (-1)^{x \cdot y}|y\rangle,
$$ {#eq-6.8}
where $x, y$ represent $n$-bit strings, and $x \cdot y$ denotes the *bitwise* AND (or mod 2 scalar product)
$$
x \cdot y = (x_1 \wedge y_1) \oplus (x_2 \wedge y_2) \oplus \dots \oplus (x_n \wedge y_n).
$$ {#eq-6.9}

Acting on the input $(|0\rangle)^n|1\rangle$, the action of the circuit is
$$
\begin{aligned}
(|0\rangle)^n|1\rangle &\to \left(\frac{1}{2^{n/2}}\sum_{x=0}^{2^n-1}|x\rangle\right)\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) \\
&\to \left(\frac{1}{2^{n/2}}\sum_{x=0}^{2^n-1}(-1)^{f(x)}|x\rangle\right)\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) \\
&\to \left(\frac{1}{2^n}\sum_{x=0}^{2^n-1}\sum_{y=0}^{2^n-1}(-1)^{f(x)}(-1)^{x \cdot y}|y\rangle\right)\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)
\end{aligned}
$$ {#eq-6.10}

Now let us evaluate the sum
$$
\frac{1}{2^n}\sum_{x=0}^{2^n-1}(-1)^{f(x)}(-1)^{x \cdot y}.
$$ {#eq-6.11}

If $f$ is a constant function, the sum is
$$
(-1)^{f(x)}\left(\frac{1}{2^n}\sum_{x=0}^{2^n-1}(-1)^{x \cdot y}\right) = (-1)^{f(x)}\delta_{y,0};
$$ {#eq-6.12}
it vanishes unless $y = 0$. Hence, when we measure the $n$-bit register, we obtain the result $|y = 0\rangle \equiv (|0\rangle)^n$ with probability one. But if the function is balanced, then for $y = 0$, the sum becomes
$$
\frac{1}{2^n}\sum_{x=0}^{2^n-1}(-1)^{f(x)} = 0,
$$ {#eq-6.13}
(because half of the terms are $(+1)$ and half are $(-1)$). Therefore, the probability of obtaining the measurement outcome $|y = 0\rangle$ is zero.

<!-- Page 10 -->
We conclude that one query of the quantum oracle suffices to distinguish constant and balanced function with 100% confidence. The measurement result $y = 0$ means constant, any other result means balanced.

So quantum computation solves this problem neatly, but is the problem really hard classically? If we are restricted to classical input states $|x\rangle$, we can query the oracle repeatedly, choosing the input $x$ at random (without replacement) each time. Once we obtain distinct outputs for two different queries, we have determined that the function is balanced (not constant). But if the function is in fact constant, we will not be certain it is constant until we have submitted $2^{n-1} + 1$ queries and have obtained the same response every time. In contrast, the quantum computation gives a definite response in only one go. So in this sense (if we demand absolute certainty) the classical calculation requires a number of queries exponential in $n$, while the quantum computation does not, and we might therefore claim an exponential quantum speedup.

But perhaps it is not reasonable to demand absolute certainty of the classical computation (particularly since any real quantum computer will be susceptible to errors, so that the quantum computer will also be unable to attain absolute certainty.) Suppose we are satisfied to guess balanced or constant, with a probability of success
$$
P(\text{success}) > 1 - \varepsilon.
$$ {#eq-6.14}

If the function is actually balanced, then if we make $k$ queries, the probability of getting the same response every time is $p = 2^{-(k-1)}$. If after receiving the same response $k$ consecutive times we guess that the function is balanced, then a quick Bayesian analysis shows that the probability that our guess is wrong is $\frac{1}{2^{k-1}+1}$ (assuming that balanced and constant are *a priori* equally probable). So if we guess after $k$ queries, the probability of a wrong guess is
$$
1 - P(\text{success}) = \frac{1}{2^{k-1}(2^{k-1} + 1)}.
$$ {#eq-6.15}

Therefore, we can achieve success probability $1 - \varepsilon$ for $\varepsilon^{-1} = 2^{k-1}(2^{k-1} + 1)$ or $k \sim \frac{1}{2} \log\left(\frac{1}{\varepsilon}\right)$. Since we can reach an exponentially good success probability with a polynomial number of trials, it is not really fair to say that the problem is hard.

**Bernstein–Vazirani problem.** Exactly the same circuit can be used to solve another variation on the Deutsch–Jozsa problem. Let's suppose that our quantum black box computes one of the functions $f_a$, where
$$
f_a(x) = a \cdot x,
$$ {#eq-6.16}
and $a$ is an $n$-bit string. Our job is to determine $a$.

The quantum algorithm can solve this problem with certainty, given just one ($n$-qubit) quantum query. For this particular function, the quantum state in eq. (6.10) becomes
$$
\frac{1}{2^n}\sum_{x=0}^{2^n-1}\sum_{y=0}^{2^n-1}(-1)^{a \cdot x}(-1)^{x \cdot y}|y\rangle.
$$ {#eq-6.17}

But in fact
$$
\frac{1}{2^n}\sum_{x=0}^{2^n-1}(-1)^{a \cdot x}(-1)^{x \cdot y} = \delta_{a,y},
$$ {#eq-6.18}
so this state is $|a\rangle$. We can execute the circuit once and measure the $n$-qubit register, finding the $n$-bit string $a$ with probability one.

<!-- Page 11 -->
If only classical queries are allowed, we acquire only one bit of information from each query, and it takes $n$ queries to determine the value of $a$. Therefore, we have a clear separation between the quantum and classical difficulty of the problem. Even so, this example does not probe the relation of $BPP$ to $BQP$, because the classical problem is not hard. The number of queries required classically is only linear in the input size, not exponential.

**Simon's problem.** Bernstein and Vazirani managed to formulate a variation on the above problem that *is* hard classically, and so establish for the first time a "relativized" separation between quantum and classical complexity. We will find it more instructive to consider a simpler example proposed somewhat later by Daniel Simon.

Once again we are presented with a quantum black box, and this time we are assured that the box computes a function
$$
f : \{0, 1\}^n \to \{0, 1\}^n,
$$ {#eq-6.19}
that is 2-to-1. Furthermore, the function has a "period" given by the $n$-bit string $a$; that is
$$
f(x) = f(y) \quad \text{iff} \quad y = x \oplus a,
$$ {#eq-6.20}
where here $\oplus$ denotes the bitwise XOR operation. (So $a$ is the period if we regard $x$ as taking values in $(Z_2)^n$ rather than $Z_{2^n}$.) This is all we know about $f$. Our job is to determine the value of $a$.

Classically this problem is *hard*. We need to query the oracle an exponentially large number of times to have any reasonable probability of finding $a$. We don't learn anything until we are fortunate enough to choose two queries $x$ and $y$ that happen to satisfy $x \oplus y = a$. Suppose, for example, that we choose $2^{n/4}$ queries. The number of pairs of queries is less than $(2^{n/4})^2$, and for each pair $\{x, y\}$, the probability that $x \oplus y = a$ is $2^{-n}$. Therefore, the probability of successfully finding $a$ is less than
$$
2^{-n}(2^{n/4})^2 = 2^{-n/2};
$$ {#eq-6.21}
even with exponentially many queries, the success probability is exponentially small.

If we wish, we can frame the question as a decision problem: Either $f$ is a 1-1 function, or it is 2-to-1 with some randomly chosen period $a$, each occurring with an *a priori* probability $\frac{1}{2}$. We are to determine whether the function is 1-to-1 or 2-to-1. Then, after $2^{n/4}$ classical queries, our probability of making a correct guess is
$$
P(\text{success}) < \frac{1}{2} + \frac{1}{2^{n/2}},
$$ {#eq-6.22}
which does not remain bounded away from $\frac{1}{2}$ as $n$ gets large.

But with quantum queries the problem is easy! The circuit we use is essentially the same as above, but now *both* registers are expanded to $n$ qubits. We prepare the equally weighted superposition of all $n$-bit strings (by acting on $|0\rangle$ with $\boldsymbol{H}^{(n)}$), and then we query the oracle:
$$
U_f : \left(\sum_{x=0}^{2^n-1}|x\rangle\right)|0\rangle \to \sum_{x=0}^{2^n-1}|x\rangle|f(x)\rangle.
$$ {#eq-6.23}

Now we measure the second register. (This step is not actually necessary, but I include it here for the sake of pedagogical clarity.) The measurement outcome is selected at random from the $2^{n-1}$ possible values of $f(x)$, each occurring equiprobably. Suppose the

<!-- Page 12 -->
outcome is $f(x_0)$. Then because both $x_0$ and $x_0 \oplus a$, and only these values, are mapped by $f$ to $f(x_0)$, we have prepared the state
$$
\frac{1}{\sqrt{2}}(|x_0\rangle + |x_0 \oplus a\rangle)
$$ {#eq-6.24}
in the first register.

Now we want to extract some information about $a$. Clearly it would do us no good to measure the register (in the computational basis) at this point. We would obtain either the outcome $x_0$ or $x_0 \oplus a$, each occurring with probability $\frac{1}{2}$, but neither outcome would reveal anything about the value of $a$.

But suppose we apply the Hadamard transform $\boldsymbol{H}^{(n)}$ to the register before we measure:
$$
\begin{aligned}
\boldsymbol{H}^{(n)} : \frac{1}{\sqrt{2}}(|x_0\rangle + |x_0 \oplus a\rangle) &\to \frac{1}{2^{(n+1)/2}}\sum_{y=0}^{2^n-1}\left[(-1)^{x_0 \cdot y} + (-1)^{(x_0 \oplus a) \cdot y}\right]|y\rangle \\
&= \frac{1}{2^{(n-1)/2}}\sum_{a \cdot y = 0}(-1)^{x_0 \cdot y}|y\rangle.
\end{aligned}
$$ {#eq-6.25}

If $a \cdot y = 1$, then the terms in the coefficient of $|y\rangle$ interfere destructively. Hence only states $|y\rangle$ with $a \cdot y = 0$ survive in the sum over $y$. The measurement outcome, then, is selected at random from all possible values of $y$ such that $a \cdot y = 0$, each occurring with probability $2^{-(n-1)}$.

We run this algorithm repeatedly, each time obtaining another value of $y$ satisfying $y \cdot a = 0$. Once we have found $n$ such linearly independent values $\{y_1, y_2, y_3 \dots y_n\}$ (that is, linearly independent over $(Z_2)^n$), we can solve the equations
$$
\begin{aligned}
y_1 \cdot a &= 0 \\
y_2 \cdot a &= 0 \\
&\ \vdots \\
y_n \cdot a &= 0,
\end{aligned}
$$ {#eq-6.26}
to determine a unique value of $a$, and our problem is solved. It is easy to see that with $O(n)$ repetitions, we can attain a success probability that is exponentially close to 1.

So we finally have found an example where, given a particular type of quantum oracle, we can solve a problem in polynomial time by exploiting quantum superpositions, while exponential time is required if we are limited to classical queries. As a computer scientist might put it:

There exists an oracle relative to which $BQP \neq BPP$.

Note that whenever we compare classical and quantum complexity relative to an oracle, we are considering a quantum oracle (queries and replies are states in Hilbert space), but with a preferred orthonormal basis. If we submit a classical query (an element of the preferred basis) we always receive a classical response (another basis element). The issue is whether we can achieve a significant speedup by choosing more general quantum queries.
