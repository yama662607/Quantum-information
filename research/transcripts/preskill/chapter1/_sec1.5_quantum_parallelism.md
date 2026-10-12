# Section 1.5: Quantum parallelism [PDF Pages 10-13]

<!-- ============================================================ -->
<!-- Source: chap1.pdf, Physical Pages: 10-13                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 10 -->
## 1.5 Quantum parallelism

Feynman’s idea was put in a more concrete form by David Deutsch in 1985. Deutsch emphasized that a quantum computer can best realize its computational potential by invoking what he called “quantum parallelism.” To understand what this means, it is best to consider an example.

Following Deutsch, imagine we have a black box that computes a function that takes a single bit $x$ to a single bit $f(x)$. We don’t know what is happening inside the box, but it must be something complicated, because the computation takes 24 hours. There are four possible functions $f(x)$ (because each of $f(0)$ and $f(1)$ can take either one of two possible values) and we’d like to know what the box is computing. It would take 48 hours to find out both $f(0)$ and $f(1)$.

<!-- Page 11 -->
But we don’t have that much time; we need the answer in 24 hours, not 48. And it turns out that we would be satisfied to know whether $f(x)$ is *constant* ($f(0) = f(1)$) or *balanced* ($f(0) \ne f(1)$). Even so, it takes 48 hours to get the answer.

Now suppose we have a quantum black box that computes $f(x)$. Of course $f(x)$ might not be invertible, while the action of our quantum computer is unitary and must be invertible, so we’ll need a transformation $U_f$ that takes two qubits to two:
$$
U_f : |x\rangle|y\rangle \to |x\rangle|y \oplus f(x)\rangle.
$$ {#eq-1.8}
(This machine flips the second qubit if $f$ acting on the first qubit is 1, and doesn’t do anything if $f$ acting on the first qubit is 0.) We can determine if $f(x)$ is constant or balanced by using the quantum black box twice. But it still takes a day for it to produce one output, so that won’t do. Can we get the answer (in 24 hours) by running the quantum black box *just once*. (This is “Deutsch’s problem.”)

Because the black box is a quantum computer, we can choose the input state to be a *superposition* of $|0\rangle$ and $|1\rangle$. If the second qubit is initially prepared in the state $\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle)$, then
$$
\begin{aligned}
U_f : |x\rangle\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) &\to |x\rangle\frac{1}{\sqrt{2}}(|f(x)\rangle - |1 \oplus f(x)\rangle) \\
&= |x\rangle(-1)^{f(x)}\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle),
\end{aligned}
$$ {#eq-1.9}
so we have isolated the function $f$ in an $x$-dependent phase. Now suppose we prepare the first qubit as $\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)$. Then the black box acts as
$$
\begin{aligned}
U_f : \quad &\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle) \to \\
&\frac{1}{\sqrt{2}}\left[(-1)^{f(0)}|0\rangle + (-1)^{f(1)}|1\rangle\right]\frac{1}{\sqrt{2}}(|0\rangle - |1\rangle).
\end{aligned}
$$ {#eq-1.10}
Finally, we can perform a measurement that projects the first qubit onto the basis
$$
|\pm\rangle = \frac{1}{\sqrt{2}}(|0\rangle \pm |1\rangle).
$$ {#eq-1.11}
Evidently, we will always obtain $|+\rangle$ if the function is constant, and $|-\rangle$ if

<!-- Page 12 -->
the function is balanced.[^2]

So we have solved Deutsch’s problem, and we have found a separation between what a classical computer and a quantum computer can achieve. The classical computer has to run the black box twice to distinguish a balanced function from a constant function, but a quantum computer does the job in one go!

This is possible because the quantum computer is not limited to computing either $f(0)$ or $f(1)$. It can act on a superposition of $|0\rangle$ and $|1\rangle$, and thereby extract “global” information about the function, information that depends on both $f(0)$ and $f(1)$. This is quantum parallelism.

Now suppose we are interested in global properties of a function that acts on $N$ bits, a function with $2^N$ possible arguments. To compute a complete table of values of $f(x)$, we would have to calculate $f$ $2^N$ times, completely infeasible for $N \gg 1$ ($e.g.$, $10^{30}$ times for $N = 100$). But with a quantum computer that acts according to
$$
U_f : |x\rangle|0\rangle \to |x\rangle|f(x)\rangle,
$$ {#eq-1.12}
we could choose the input register to be in a state
$$
\left[\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)\right]^N = \frac{1}{2^{N/2}}\sum_{x=0}^{2^N-1} |x\rangle,
$$ {#eq-1.13}
and by computing $f(x)$ only once, we can generate a state
$$
\frac{1}{2^{N/2}}\sum_{x=0}^{2^N-1} |x\rangle|f(x)\rangle.
$$ {#eq-1.14}
Global properties of $f$ are encoded in this state, and we might be able to extract some of those properties if we can only think of an efficient way to do it.

This quantum computation exhibits “*massive* quantum parallelism;” a simulation of the preparation of this state on a classical computer would

[^2]: In our earlier description of a quantum computation, we stated that the final measurement would project each qubit onto the $\{|0\rangle, |1\rangle\}$ basis, but here we are allowing measurement in a different basis. To describe the procedure in the earlier framework, we would apply an appropriate unitary change of basis to each qubit before performing the final measurement.

<!-- Page 13 -->
require us to compute $f$ an unimaginably large number of times (for $N \gg 1$). Yet we have done it with the quantum computer in only one go. It is just this kind of massive parallelism that Shor invokes in his factoring algorithm.

As noted earlier, a characteristic feature of quantum information is that it can be encoded in nonlocal correlations among different parts of a physical system. Indeed, this is the case in Eq. (1.14); the properties of the function $f$ are stored as correlations between the “input register” and “output register” of our quantum computer. This nonlocal information, however, is not so easy to decipher.

If, for example, I were to measure the input register, I would obtain a result $|x_0\rangle$, where $x_0$ is chosen completely at random from the $2^N$ possible values. This procedure would prepare a state
$$
|x_0\rangle|f(x_0)\rangle.
$$ {#eq-1.15}
We could proceed to measure the output register to find the value of $f(x_0)$. But because Eq. (1.14) has been destroyed by the measurement, the intricate correlations among the registers have been lost, and we get no opportunity to determine $f(y_0)$ for any $y_0 \ne x_0$ by making further measurements. In this case, then, the quantum computation provided no advantage over a classical one.

The lesson of the solution to Deutsch’s problem is that we can sometimes be more clever in exploiting the correlations encoded in Eq. (1.14). Much of the art of designing quantum algorithms involves finding ways to make efficient use of the nonlocal correlations.
