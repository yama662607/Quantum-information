# Section 7.21: Reed–Muller Codes

**Source:** Preskill Lecture Notes, Chapter 7, pp. 65–68 (Physical pages 71–74).

---

Another way to construct codes that can correct many errors is to invoke the CSS construction. Recall, in particular, the special case of that construction that applies to a classical code $C$ that is contained in its dual code (we then say that $C$ is "weakly self-dual"). In the CSS construction, there is a codeword associated with each coset of $C$ in $C^\perp$. Thus we obtain an $[[n, k, d]]$ quantum code, where $n$ is the length of $C$, $d$ is (at least) the distance of $C^\perp$, and $k = \dim C^\perp - \dim C$. Therefore, for the construction of CSS codes that correct many errors, we seek weakly self-dual classical codes with a large minimum distance.

One class of weakly self-dual classical codes are the Reed-Muller codes. Though these are not especially efficient, they are very convenient, because they are easy to encode, recovery is simple, and it is not difficult to explain their mathematical structure.[^fn-macwilliams]

[^fn-macwilliams]: See, e.g., MacWilliams and Sloane, Chapter 13.

To prepare for the construction of Reed-Muller codes, consider Boolean functions on $m$ bits,
$$
f : \{0, 1\}^m \to \{0, 1\} .
$$ {#eq-7.258}
There are $2^{2^m}$ such functions forming what we may regard as a binary vector space of dimension $2^m$. It will be useful to have a basis for this space. Recall (§6.1), that any Boolean function has a disjunctive normal form. Since the NOT of a bit $x$ is $1 - x$, and the OR of two bits $x$ and $y$ can be expressed as
$$
x \vee y = x + y - xy ,
$$ {#eq-7.259}
any of the Boolean functions can be expanded as a polynomial in the $m$ binary variables $x_{m-1}, x_{m-2}, \dots, x_1, x_0$. A basis for the vector space of polynomials consists of the $2^m$ functions
$$
1, \; x_i, \; x_i x_j, \; x_i x_j x_k, \; \dots,
$$ {#eq-7.260}
(where, since $x^2 = x$, we may choose the factors of each monomial to be distinct). Each such function $f$ can be represented by a binary string of length $2^m$, whose value in the position labeled by the binary string $x_{m-1}x_{m-2}\dots x_1 x_0$ is $f(x_{m-1}, x_{m-2}, \dots, x_1, x_0)$. For example, for $m = 3$,
$$
\begin{aligned}
1 &= (11111111) \\
x_0 &= (10101010) \\
x_1 &= (11001100) \\
x_2 &= (11110000) \\
x_0 x_1 &= (10001000) \\
x_0 x_2 &= (10100000) \\
x_1 x_2 &= (11000000) \\
x_0 x_1 x_2 &= (10000000) .
\end{aligned}
$$ {#eq-7.261}

A subspace of this vector space is obtained if we restrict the degree of the polynomial to $r$ or less. This subspace is the Reed–Muller (or RM) code, denoted $R(r, m)$. Its length is $n = 2^m$ and its dimension is
$$
k = 1 + \binom{m}{1} + \binom{m}{2} + \dots + \binom{m}{r} .
$$ {#eq-7.262}

Some special cases of interest are:
- $R(0, m)$ is the length-$2^m$ repetition code.
- $R(m-1, m)$ is the dual of the repetition code, the space on all length-$2^m$ even-weight strings.
- $R(1, 3)$ is the $n = 8, k = 4$ code spanned by $1, x_0, x_1, x_2$; it is in fact the $[8, 4, 4]$ extended Hamming code that we have already discussed.
- More generally, $R(m-2, m)$ is a $d = 4$ extended Hamming code for each $m \ge 3$. If we puncture this code (remove the last bit from all codewords) we obtain the $[n = 2^m - 1, k = n - m, d = 3]$ perfect Hamming code.
- $R(1, m)$ has $d = 2^{m-1} = \frac{1}{2}n$ and $k = m + 1$ (the original notes write $k = m$). It is the dual of the extended Hamming code, and is known as a "first-order" Reed–Muller code. It is of considerable practical interest in its own right, both because of its large distance and because it is especially easy to decode.

We can compute the distance of the code $R(r, m)$ by invoking induction on $m$. First we must determine how $R(r, m+1)$ is related to $R(r, m)$. A function of $x_m, \dots, x_0$ can be expressed as
$$
f(x_m, \dots, x_0) = g(x_{m-1}, \dots, x_0) + x_m h(x_{m-1}, \dots, x_0) ,
$$ {#eq-7.263}
and if $f$ has degree $r$, then $g$ must be of degree $r$ and $h$ of degree $r - 1$. Regarding $f$ as a vector of length $2^{m+1}$, we have
$$
f = (g|g) + (h|0)
$$ {#eq-7.264}
where $g, h$ are vectors of length $2^m$. Consider the distance between $f$ and
$$
f' = (g'|g') + (h'|0) .
$$ {#eq-7.265}
For $h = h'$ and $f \ne f'$ this distance is $\mathrm{wt}(f - f') = 2 \cdot \mathrm{wt}(g - g') \ge 2 \cdot \mathrm{dist}(R(r, m))$; for $h \ne h'$ it is at least $\mathrm{wt}(h - h') \ge \mathrm{dist}(R(r - 1, m))$. If $d(r, m)$ denotes the distance of $R(r, m)$, then we see that
$$
d(r, m+1) = \min(2 d(r, m), d(r - 1, m)) .
$$ {#eq-7.266}
Now we can show that $d(r, m) = 2^{m-r}$ by induction on $m$. To start with, we check that $d(r, m=1) = 2^{1-r}$ for $r = 0, 1$; $R(1, 1)$ is the space of all length 2 strings, and $R(0, 1)$ is the length-2 repetition code. Next suppose that $d = 2^{m-r}$ for all $m \le M$ and $0 \le r \le m$. Then we infer that
$$
d(r, m+1) = \min(2^{m-r+1}, 2^{m-r+1}) = 2^{m-r+1} ,
$$ {#eq-7.267}
for each $1 \le r \le m$. It is also clear that $d(m+1, m+1) = 1$, since $R(m+1, m+1)$ is the space of all binary strings of length $2^{m+1}$, and that $d(0, m+1) = 2^{m+1}$, since $R(0, m+1)$ is the length-$2^{m+1}$ repetition code. This completes the inductive step, and proves $d(r, m) = 2^{m-r}$.

It follows, in particular, that $R(m - 1, m)$ has distance 2, and therefore that the dual of $R(r, m)$ is $R(m - r - 1, m)$. First we notice that the binomial coefficients $\binom{m}{j}$ sum to $2^m$, so that $R(m-r-1, m)$ has the right dimension to be $R(r, m)^\perp$. It suffices, then, to show that $R(m - r - 1, m)$ is contained in $R(r, m)^\perp$. But if $f \in R(r, m)$ and $g \in R(m - r - 1, m)$, their product is a polynomial of degree at most $m - 1$, and is therefore in $R(m - 1, m)$. Each vector in $R(m - 1, m)$ has even weight, so the inner product $f \cdot g$ vanishes; hence $g$ is in the dual $R(r, m)^\perp$. This shows that
$$
R(r, m)^\perp = R(m - r - 1, m) .
$$ {#eq-7.268}
It is because of this nice duality property that Reed–Muller codes are well-suited for the CSS construction of quantum codes.

In particular, the Reed–Muller code is weakly self-dual for $r \le m - r - 1$, or $2r \le m - 1$, and self-dual for $2r = m - 1$. In the self-dual case, the distance is
$$
d = 2^{m-r} = 2^{\frac{1}{2}(m+1)} = \sqrt{2n} ,
$$ {#eq-7.269}
and the number of encoded bits is
$$
k = \frac{1}{2}n = 2^{m-1} .
$$ {#eq-7.270}
These self-dual codes, for $m = 3, 5, 7$, have parameters
$$
[8, 4, 4], \quad [32, 16, 8], \quad [128, 64, 16] .
$$ {#eq-7.271}
(The $[8, 4, 4]$ code is the extended Hamming code as we have already noted.) Associated with these self-dual codes are the $k = 0$ quantum codes with parameters
$$
[[8, 0, 4]], \quad [[32, 0, 8]], \quad [[128, 0, 16]] ,
$$ {#eq-7.272}
and so forth.

One way to obtain a $k = 1$ quantum code is to *puncture* the self-dual Reed–Muller code, that is, to delete one of the $n = 2^m$ bits from the code. (It turns out not to matter *which* bit we delete.) The classical punctured code has parameters $n = 2^m - 1$, $d = 2^{\frac{1}{2}(m-1)} - 1 = \sqrt{2(n+1)} - 1$, and $k = \frac{1}{2}(n+1)$. Furthermore, the dual of the punctured code is its even subcode. (The even subcode consists of those RM codewords for which the bit removed by the puncture is zero, and it follows from the self-duality of the RM code that these are orthogonal to all the words (both odd and even weight) of the punctured code.) From these punctured codes, we obtain, via the CSS construction, $k = 1$ quantum codes with parameters
$$
[[7, 1, 3]], \quad [[31, 1, 7]], \quad [[127, 1, 15]] ,
$$ {#eq-7.273}
and so forth. The $[7, 4, 3]$ Hamming code is obtained by puncturing the $[8, 4, 4]$ RM code, and the corresponding $[[7, 1, 3]]$ QECC is of course Steane's code. These QECC's have a distance that increases like the square root of their length.

These $k = 1$ codes are not among the most efficient of the known QECC's. Nevertheless they are of special interest, since their properties are especially conducive to implementing fault-tolerant quantum gates on the encoded data, as we will see in Chapter 8. In particular, one useful property of the self-dual RM codes is that they are "doubly even" — all codewords have a weight that is an integral multiple of four.

Of course, we can also construct quantum codes with $k > 1$ by applying the CSS construction to the RM codes. For example $R(3, 6)$, with parameters
$$
\begin{aligned}
n &= 2^m = 64 \\
d &= 2^{m-r} = 8 \\
k &= 1 + 6 + \binom{6}{2} + \binom{6}{3} = 1 + 6 + 15 + 20 = 42 ,
\end{aligned}
$$ {#eq-7.274}
is dual to $R(2, 6)$, with parameters
$$
\begin{aligned}
n &= 2^m = 64 \\
d &= 2^{m-r} = 16 \\
k &= 1 + 6 + \binom{6}{2} = 1 + 6 + 15 = 22 ,
\end{aligned}
$$ {#eq-7.275}
and so the CSS construction yields a QECC with parameters
$$
[[64, 20, 8]] .
$$ {#eq-7.276}
Many other weakly self-dual codes are known and can likewise be employed.
