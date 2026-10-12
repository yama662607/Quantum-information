# Section 6.3: Factoring [PDF Pages 18-24]

<!-- ============================================================ -->
<!-- Source: chap6.pdf, Physical Pages: 18-24                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 18 -->
## 6.3 Factoring

### 6.3.1 Factoring as period finding

What does the factoring problem (finding the prime factors of a large composite positive integer) have to do with periodicity? There is a well-known (randomized) reduction of

<!-- Page 19 -->
factoring to determining the period of a function. Although this reduction is not directly related to quantum computing, we will discuss it here for completeness, and because the prospect of using a quantum computer as a factoring engine has generated so much excitement.

Suppose we want to find a factor of the $n$-bit number $N$. Select pseudo-randomly $a < N$, and compute the greatest common divisor $\text{GCD}(a, N)$, which can be done efficiently (in a time of order $(\log N)^3$) using the Euclidean algorithm. If $\text{GCD}(a, N) \neq 1$ then the GCD is a nontrivial factor of $N$, and we are done. So suppose $\text{GCD}(a, N) = 1$.

[Aside: The Euclidean algorithm. To compute $\text{GCD}(N_1, N_2)$ (for $N_1 > N_2$) first divide $N_1$ by $N_2$ obtaining remainder $R_1$. Then divide $N_2$ by $R_1$, obtaining remainder $R_2$. Divide $R_1$ by $R_2$, *etc.* until the remainder is 0. The last nonzero remainder is $R = \text{GCD}(N_1, N_2)$. To see that the algorithm works, just note that (1) $R$ divides all previous remainders and hence also $N_1$ and $N_2$, and (2) *any* number that divides $N_1$ and $N_2$ will also divide all remainders, including $R$. A number that divides both $N_1$ and $N_2$, and also is divided by any number that divides both $N_1$ and $N_2$ must be $\text{GCD}(N_1, N_2)$. To see how long the Euclidean algorithm takes, note that
$$
R_j = q R_{j+1} + R_{j+2},
$$ {#eq-6.59}
where $q \ge 1$ and $R_{j+2} < R_{j+1}$; therefore $R_{j+2} < \frac{1}{2} R_j$. Two divisions reduce the remainder by at least a factor of 2, so no more than $2\log N_1$ divisions are required, with each division using $O((\log N)^2)$ elementary operations; the total number of operations is $O((\log N)^3)$.]

The numbers $a < N$ coprime to $N$ (having no common factor with $N$) form a finite group under multiplication mod $N$. [Why? We need to establish that each element $a$ has an inverse. But for given $a < N$ coprime to $N$, each $ab \pmod N$ is distinct, as $b$ ranges over all $b < N$ coprime to $N$. (If $N$ divides $ab - ab'$, it must divide $b - b'$.) Therefore, for some $b$, we must have $ab \equiv 1 \pmod N$; hence the inverse of $a$ exists.] Each element $a$ of this finite group has a finite *order* $r$, the smallest positive integer such that
$$
a^r \equiv 1 \pmod N.
$$ {#eq-6.60}
The order of $a \bmod N$ is the period of the function
$$
f_{N, a}(x) = a^x \pmod N.
$$ {#eq-6.61}
We know there is an efficient quantum algorithm that can find the period of a function; therefore, if we can compute $f_{N, a}$ efficiently, we can find the order of $a$ efficiently.

Computing $f_{N, a}$ may look difficult at first, since the exponent $x$ can be very large. But if $x < 2^m$ and we express $x$ as a binary expansion
$$
x = x_{m-1}\cdot 2^{m-1} + x_{m-2}\cdot 2^{m-2} + \dots + x_0,
$$ {#eq-6.62}
we have
$$
a^x \pmod N = (a^{2^{m-1}})^{x_{m-1}} (a^{2^{m-2}})^{x_{m-2}} \dots (a)^{x_0} \pmod N.
$$ {#eq-6.63}
Each $a^{2^j}$ has a large exponent, but can be computed efficiently by a *classical* computer, using repeated squaring
$$
a^{2^j} \pmod N = (a^{2^{j-1}})^2 \pmod N.
$$ {#eq-6.64}

<!-- Page 20 -->
So only $m - 1$ (classical) $\bmod N$ multiplications are needed to assemble a table of all $a^{2^j}$'s.

The computation of $a^x \pmod N$ is carried out by executing a routine:

```text
INPUT 1
For j = 0 to m - 1, if x_j = 1, MULTIPLY a^{2^j}.
```

This routine requires at most $m \bmod N$ multiplications, each requiring of order $(\log N)^2$ elementary operations. (Using tricks for performing efficient multiplication of very large numbers, the number of elementary operations can be reduced to $O(\log N \log\log N \log\log\log N)$; thus, asymptotically for large $N$, a circuit family with size $O(\log^2 N \log\log N \log\log\log N)$ can compute $f_{N, a}$.) Since $r < N$, we will have a reasonable chance of success at extracting the period if we choose $m \sim 2\log N$. Hence, the computation of $f_{N, a}$ can be carried out by a circuit family of size $O((\log N)^3)$. Schematically, the circuit has the structure:

```
|x₂⟩ ───────────────●─────────────────────────
                    │
|x₁⟩ ───────●───────┼─────────────────────────
            │       │
|x₀⟩ ───●───┼───────┼─────────────────────────
        │   │       │
|1⟩  ══[ a ]=[ a² ]=[ a⁴ ]════════════════════
```

Multiplication by $a^{2^j}$ is performed if the control qubit $x_j$ has the value 1.

Suppose we have found the period $r$ of $a \bmod N$. Then *if* $r$ is even, we have
$$
N \text{ divides } \left(a^{\frac{r}{2}} + 1\right)\left(a^{\frac{r}{2}} - 1\right).
$$ {#eq-6.65}
We know that $N$ does not divide $a^{r/2} - 1$; if it did, the order of $a$ would be $\le r/2$. Thus, *if it is also the case* that $N$ does not divide $a^{r/2} + 1$, or
$$
a^{r/2} \not\equiv -1 \pmod N,
$$ {#eq-6.66}
*then* $N$ must have a nontrivial common factor with each of $a^{r/2} \pm 1$. Therefore, $\text{GCD}(N, a^{r/2} + 1) \neq 1$ is a factor (that we can find efficiently by a classical computation), and we are done.

We see that, once we have found $r$, we succeed in factoring $N$ *unless* either (1) $r$ is odd or (2) $r$ is even and $a^{r/2} \equiv -1 \pmod N$. How likely is success?

Let's suppose that $N$ is a product of two prime factors $p_1 \neq p_2$,
$$
N = p_1 p_2
$$ {#eq-6.67}
(this is actually the least favorable case). For each $a < p_1 p_2$, there exist unique $a_1 < p_1$ and $a_2 < p_2$ such that
$$
\begin{aligned}
a &\equiv a_1 \pmod{p_1} \\
a &\equiv a_2 \pmod{p_2}.
\end{aligned}
$$ {#eq-6.68}
Choosing a random $a < N$ is, therefore, equivalent to choosing random $a_1 < p_1$ and $a_2 < p_2$.

<!-- Page 21 -->
[Aside: We're using the **Chinese Remainder Theorem**. The $a$ solving eq. (6.68) is unique because if $a$ and $b$ are both solutions, then both $p_1$ and $p_2$ must divide $a - b$. The solution exists because every $a < p_1 p_2$ solves eq. (6.68) for *some* $a_1$ and $a_2$. Since there are exactly $p_1 p_2$ ways to choose $a_1$ and $a_2$, and exactly $p_1 p_2$ ways to choose $a$, uniqueness implies that there is an $a$ corresponding to each pair $a_1, a_2$.]

Now let $r_1$ denote the order of $a_1 \bmod p_1$ and $r_2$ denote the order of $a_2 \bmod p_2$. The Chinese remainder theorem tells us that $a^r \equiv 1 \pmod{p_1 p_2}$ is equivalent to
$$
\begin{aligned}
a_1^r &\equiv 1 \pmod{p_1} \\
a_2^r &\equiv 1 \pmod{p_2}.
\end{aligned}
$$ {#eq-6.69}
Therefore $r = \text{LCM}(r_1, r_2)$. If $r_1$ and $r_2$ are both odd, then so is $r$, and we lose.
But if *either* $r_1$ or $r_2$ is even, then so is $r$, and we are still in the game. If
$$
\begin{aligned}
a^{r/2} &\equiv -1 \pmod{p_1} \\
a^{r/2} &\equiv -1 \pmod{p_2}.
\end{aligned}
$$ {#eq-6.70}
Then we have $a^{r/2} \equiv -1 \pmod{p_1 p_2}$ and we still lose. But if either
$$
\begin{aligned}
a^{r/2} &\equiv -1 \pmod{p_1} \\
a^{r/2} &\equiv 1 \pmod{p_2},
\end{aligned}
$$ {#eq-6.71}
or
$$
\begin{aligned}
a^{r/2} &\equiv 1 \pmod{p_1} \\
a^{r/2} &\equiv -1 \pmod{p_2},
\end{aligned}
$$ {#eq-6.72}
then $a^{r/2} \not\equiv -1 \pmod{p_1 p_2}$ and we win. (Of course, $a^{r/2} \equiv 1 \pmod{p_1}$ and $a^{r/2} \equiv 1 \pmod{p_2}$ is not possible, for that would imply $a^{r/2} \equiv 1 \pmod{p_1 p_2}$, and $r$ could not be the order of $a$.)

Suppose that
$$
\begin{aligned}
r_1 &= 2^{c_1}\cdot \text{odd} \\
r_2 &= 2^{c_2}\cdot \text{odd},
\end{aligned}
$$ {#eq-6.73}
where $c_1 > c_2$. Then $r = \text{LCM}(r_1, r_2) = 2r_2 \cdot \text{integer}$, so that $a^{r/2} \equiv 1 \pmod{p_2}$ and eq. (6.71) is satisfied — we win! Similarly $c_2 > c_1$ implies eq. (6.72) — again we win. But for $c_1 = c_2$, $r = r_1 \cdot (\text{odd}) = r_2 \cdot (\text{odd}')$ so that eq. (6.70) is satisfied — in that case we lose.

Okay — it comes down to: for $c_1 = c_2$ we lose, for $c_1 \neq c_2$ we win. How likely is $c_1 \neq c_2$?

It helps to know that the multiplicative group mod $p$ is cyclic — it contains a primitive element of order $p - 1$, so that all elements are powers of the primitive element. [Why? The integers mod $p$ are a finite *field*. If the group were not cyclic, the maximum order of the elements would be $q < p - 1$, so that $x^q \equiv 1 \pmod p$ would have $p - 1$ solutions. But that can't be: in a finite field there are no more than $q$ $q$th roots of unity.]

Suppose that $p - 1 = 2^k \cdot s$, where $s$ is odd, and consider the orders of all the elements of the cyclic group of order $p - 1$. For brevity, we'll discuss only the case $k = 1$, which is the least favorable case for us. Then if $b$ is a primitive (order $2s$) element, the even powers of $b$ have odd order, and the odd powers of $b$ have order $2\cdot(\text{odd})$. In this case,

<!-- Page 22 -->
then, $r = 2^c \cdot (\text{odd})$ where $c \in \{0, 1\}$, each occuring equiprobably. Therefore, if $p_1$ and $p_2$ are both of this (unfavorable) type, and $a_1, a_2$ are chosen randomly, the probability that $c_1 \neq c_2$ is $\frac{1}{2}$. Hence, once we have found $r$, our probability of successfully finding a factor is at least $\frac{1}{2}$, if $N$ is a product of two distinct primes. If $N$ has more than two distinct prime factors, our odds are even better. The method fails if $N$ is a prime power, $N = p^\alpha$, but prime powers can be efficiently factored by other methods.

### 6.3.2 RSA

Does anyone care whether factoring is easy or hard? Well, yes, some people do.

The presumed difficulty of factoring is the basis of the security of the widely used RSA (for Rivest, Shamir, and Adleman) scheme for public key cryptography, which you may have used yourself if you have ever sent your credit card number over the internet.

The idea behind public key cryptography is to avoid the need to exchange a secret key (which might be intercepted and copied) between the parties that want to communicate. The enciphering key is public knowledge. But using the enciphering key to infer the deciphering key involves a prohibitively difficult computation. Therefore, Bob can send the enciphering key to Alice and everyone else, but only Bob will be able to decode the message that Alice (or anyone else) encodes using the key. Encoding is a "one-way function" that is easy to compute but very hard to invert.

(Of course, Alice and Bob could have avoided the need to exchange the public key if they had decided on a private key in their previous clandestine meeting. For example, they could have agreed to use a long random string as a one-time pad for encoding and decoding. But perhaps Alice and Bob never anticipated that they would someday need to communicate privately. Or perhaps they did agree in advance to use a one-time pad, but they have now used up their private key, and they are loath to reuse it for fear that an eavesdropper might then be able to break their code. Now they are too far apart to safely exchange a new private key; public key cryptography appears to be their most secure option.)

To construct the public key Bob chooses two large prime numbers $p$ and $q$. But he does not publicly reveal their values. Instead he computes the product
$$
N = pq.
$$ {#eq-6.74}
Since Bob knows the prime factorization of $N$, he also knows the value of the Euler function $\varphi(N)$ — the number of number less than $N$ that are coprime with $N$. In the case of a product of two primes it is
$$
\varphi(N) = N - p - q + 1 = (p - 1)(q - 1),
$$ {#eq-6.75}
(only multiples of $p$ and $q$ share a factor with $N$). It is easy to find $\varphi(N)$ if you know the prime factorization of $N$, but it is hard if you know only $N$.

Bob then pseudo-randomly selects $e < \varphi(N)$ that is coprime with $\varphi(N)$. He reveals to Alice (and anyone else who is listening) the value of $N$ and $e$, but nothing else.

Alice converts her message to ASCII, a number $a < N$. She encodes the message by computing
$$
b = f(a) = a^e \pmod N,
$$ {#eq-6.76}
which she can do quickly by repeated squaring. How does Bob decode the message?

<!-- Page 23 -->
Suppose that $a$ is coprime to $N$ (which is overwhelmingly likely if $p$ and $q$ are very large — anyway Alice can check before she encodes). Then
$$
a^{\varphi(N)} \equiv 1 \pmod N
$$ {#eq-6.77}
(Euler's theorem). This is so because the numbers less than $N$ and coprime to $N$ form a group (of order $\varphi(N)$) under mod $N$ multiplication. The order of any group element must divide the order of the group (the powers of $a$ form a subgroup). Since $\text{GCD}(e, \varphi(N)) = 1$, we know that $e$ has a multiplicative inverse $d = e^{-1} \bmod \varphi(N)$:
$$
ed \equiv 1 \pmod{\varphi(N)}.
$$ {#eq-6.78}
The value of $d$ is Bob's closely guarded secret; he uses it to decode by computing:
$$
\begin{aligned}
f^{-1}(b) &= b^d \pmod N \\
&= a^{ed} \pmod N \\
&= a \cdot (a^{\varphi(N)})^{\text{integer}} \pmod N \\
&= a \pmod N.
\end{aligned}
$$ {#eq-6.79}

[Aside: How does Bob compute $d = e^{-1}$? The multiplicative inverse is a byproduct of carrying out the Euclidean algorithm to compute $\text{GCD}(e, \varphi(N)) = 1$. Tracing the chain of remainders from the bottom up, starting with $R_n = 1$:
$$
\begin{aligned}
1 = R_n &= R_{n-2} - q_{n-1} R_{n-1} \\
R_{n-1} &= R_{n-3} - q_{n-2} R_{n-2} \\
R_{n-2} &= R_{n-4} - q_{n-3} R_{n-3} \\
\text{etc.} \dots
\end{aligned}
$$ {#eq-6.80}
(where the $q_j$'s are the quotients), so that
$$
\begin{aligned}
1 &= (1 + q_{n-1} q_{n-2}) R_{n-2} - q_{n-1} R_{n-3} \\
1 &= (-q_{n-1} - q_{n-3}(1 + q_{n-1} q_{n-2})) R_{n-3} + (1 + q_{n-1} q_{n-2}) R_{n-4}, \\
\text{etc.} \dots
\end{aligned}
$$ {#eq-6.81}
Continuing, we can express 1 as a linear combination of any two successive remainders; eventually we work our way up to
$$
1 = d \cdot e + q \cdot \varphi(N),
$$ {#eq-6.82}
and identify $d$ as $e^{-1} \pmod{\varphi(N)}$.]

Of course, if Eve has a superfast factoring engine, the RSA scheme is insecure. She factors $N$, finds $\varphi(N)$, and quickly computes $d$. In fact, she does not really need to factor $N$; it is sufficient to compute the order modulo $N$ of the encoded message $a^e \pmod N$. Since $e$ is coprime with $\varphi(N)$, the order of $a^e \pmod N$ is the same as the order of $a$ (both elements generate the same orbit, or cyclic subgroup). Once the order $\text{Ord}(a)$ is known, Eve computes $\tilde{d}$ such that
$$
\tilde{d} e \equiv 1 \pmod{\text{Ord}(a)}
$$ {#eq-6.83}
so that
$$
(a^e)^{\tilde{d}} \equiv a \cdot (a^{\text{Ord}(a)})^{\text{integer}} \pmod N \equiv a \pmod N,
$$ {#eq-6.84}

<!-- Page 24 -->
and Eve can decipher the message. If our only concern is to defeat RSA, we run the Shor algorithm to find $r = \text{Ord}(a^e)$, and we needn't worry about whether we can use $r$ to extract a factor of $N$ or not.

How important are such prospective cryptographic applications of quantum computing? When fast quantum computers are readily available, concerned parties can stop using RSA, or can use longer keys to stay a step ahead of contemporary technology. However, people with secrets sometimes want their messages to remain confidential for a while (30 years?). They may not be satisfied by longer keys if they are not confident about the pace of future technological advances.

And if they shun RSA, what will they use instead? Not so many suitable one-way functions are known, and others besides RSA are (or may be) vulnerable to a quantum attack. So there really is a lot at stake. If fast large scale quantum computers become available, the cryptographic implications may be far reaching.

But while quantum theory taketh away, quantum theory also giveth; quantum computers may compromise public key schemes, but also offer an alternative: secure quantum key distribution, as discussed in Chapter 4.
