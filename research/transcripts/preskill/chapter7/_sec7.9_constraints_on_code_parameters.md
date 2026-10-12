# Section 7.9: Some Constraints on Code Parameters [PDF Pages 31-33]

<!-- ============================================================ -->
<!-- Source: chap7.pdf, Physical Pages: 31-33                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 31 -->
## 7.9 Some Constraints on Code Parameters

Shor’s code protects one encoded qubit from an error in any single one of nine qubits in a block, and Steane’s code reduces the block size from nine to seven. Can we do better still?

### 7.9.1 The Quantum Hamming bound

To understand how much better we might do, let’s see if we can derive any bounds on the distance $d = 2t + 1$ of an $[[n, k, d]]$ quantum code, for given $n$ and $k$. At first, suppose we limit our attention to *nondegenerate* codes, which assign a distinct syndrome to each possible error. On a given qubit, there are three possible linearly independent errors $\boldsymbol{X}$, $\boldsymbol{Y}$, or $\boldsymbol{Z}$. In a block of $n$ qubits, there are $\binom{n}{j}$ ways to choose $j$ qubits that are affected by errors, and three possible errors for each of these qubits; therefore the total number of possible errors of weight up to $t$ is

$$
N(t) = \sum_{j=0}^t 3^j \binom{n}{j}.
$$ {#eq-7.108}

If there are $k$ encoded qubits, then there are $2^k$ linearly independent codewords. If all $\boldsymbol{E}_a |\bar{j}\rangle$’s are linearly independent, where $\boldsymbol{E}_a$ is any error of weight up to $t$ and $|\bar{i}\rangle$ is any element of a basis for the codewords, then the dimension $2^n$ of the Hilbert space of $n$ qubits must be large enough to accommodate $N(t) \cdot 2^k$ independent vectors; hence

$$
N(t) = \sum_{j=0}^t 3^j \binom{n}{j} \le 2^{n-k}.
$$ {#eq-7.109}

This result is called the *quantum Hamming bound*. An analogous bound applies to classical block codes, but without the factor of $3^j$, since there is only one type of error (a flip) that can affect a classical bit. We also emphasize that the quantum Hamming bound applies only in the case of nondegenerate coding, while the classical Hamming bound applies in general. However, no degenerate quantum codes that violate the quantum Hamming code have yet been constructed (as of January, 1999).

In the special case of a code with one encoded qubit ($k = 1$) that corrects one error ($t = 1$), the quantum Hamming bound becomes

$$
1 + 3n \le 2^{n-1},
$$ {#eq-7.110}

which is satisfied for $n \ge 5$. In fact, the case $n = 5$ saturates the inequality ($1 + 15 = 16$). A nondegenerate $[[5, 1, 3]]$ quantum code, if it exists, is *perfect*: The entire 32-dimensional Hilbert space of the five qubits is needed to accommodate all possible one-qubit errors acting on all codewords — there is no wasted space.

### 7.9.2 The no-cloning bound

We could still wonder, though, if there is a *degenerate* $n = 4$ code that can correct one error. In fact, it is easy to see that no such code can exist. We already know that a code that corrects $t$ errors at arbitrary locations can also be used to correct $2t$ errors at known locations. Suppose that we have a $[[4, 1, 3]]$ quantum code. Then we could

<!-- Page 32 -->

encode a single qubit in the four-qubit block, and split the block into two sub-blocks, each containing two qubits.

– Figure –

If we append $|00\rangle$ to each of those two sub-blocks, then the original block has spawned two offspring, each with two located errors. If we were able to correct the two located errors in each of the offspring, we would obtain two identical copies of the parent block — we would have cloned an unknown quantum state, which is impossible. Therefore, no $[[4, 1, 3]]$ quantum code can exist. We conclude that $n = 5$ is the minimal block size of a quantum code that corrects one error, whether the code is degenerate or not.

The same reasoning shows that an $[[n, k \ge 1, d]]$ code can exist only for

$$
n > 2(d - 1).
$$ {#eq-7.111}

### 7.9.3 The quantum Singleton bound

This result eq. (7.111) can be strengthened to

$$
n - k \ge 2(d - 1).
$$ {#eq-7.112}

Eq. (7.112) resembles the Singleton bound on classical code parameters,

$$
n - k \ge d - 1,
$$ {#eq-7.113}

and so has been called the “quantum Singleton bound.” For a classical *linear* code, the Singleton bound is a near triviality: the code can have distance $d$ only if any $d - 1$ columns of the parity check matrix are linearly independent. Since the columns have length $n - k$, at most $n - k$ columns can be linearly independent; therefore $d - 1$ cannot exceed $n - k$. The Singleton bound also applies to nonlinear codes.

The quantum Singleton bound shows that $n = 5$ is the minimal code length for an $[[n, 1, 3]]$ quantum code, and that $n = 4$ is the minimal length for an $[[n, 2, 2]]$ code; we’ll soon see that $[[5, 1, 3]]$ and $[[4, 2, 2]]$ codes can be constructed. The bound does not exclude the existence of a $[[3, 1, 2]]$ code, although no such code exists for qubits. However, the bound also applies to codes constructed from higher dimensional objects, and in fact there is a $[[3, 1, 2]]$ code in which the fundamental particles are qutrits rather than qubits, as you will show in Exercise ??.

An elegant proof of the quantum Singleton bound can be found based on information theory ideas which we will develop in Chapter 10. In Exercise ?? we prove the following statement: Suppose that the code block can be divided into three parts $ABC$ such that erasure of $A$ can be corrected and erasure of $B$ can also be corrected. Then the number of encoded qubits satisfies $k \le |C|$, where $|C|$ denotes the number of qubits in $C$. To derive the quantum Singleton bound, choose $A$ and $B$ to be disjoint sets each containing $d - 1$ qubits; hence $A$ and $B$ are both correctable. (This is possible because the no-cloning bound ensures that $n > 2(d - 1)$ for $k \ge 1$.). Choose $C$ to be the complement of $AB$ in the code block. Then we have

$$
k \le |C| = n - |A| - |B| = n - 2(d - 1).
$$ {#eq-7.114}

<!-- Page 33 -->

The quantum Singleton bound then follows.

For most values of $n$ and $k$ the quantum Singleton bound is not tight. Rains has obtained the stronger result that an $[[n, k, 2t + 1]]$ code with $k \ge 1$ must satisfy

$$
t \le \left\lfloor \frac{n + 1}{6} \right\rfloor,
$$ {#eq-7.115}

where $\lfloor x \rfloor$ “floor $x$” is the greatest integer greater than or equal to $x$. Thus, the minimal length of a $k = 1$ code that can correct $t = 1, 2, 3, 4, 5$ errors is $n = 5, 11, 17, 23, 29$ respectively. Codes with all of these parameters have actually been constructed, except for the $[[23, 1, 9]]$ code.
