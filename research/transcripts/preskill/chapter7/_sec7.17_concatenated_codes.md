# Section 7.17: Concatenated Codes

**Source:** Preskill Lecture Notes, Chapter 7, pp. 48–51 (Physical pages 54–57).

---

Up until now, all of the QECC's that we have explicitly constructed have $d = 3$ (or $d = 2$), and so can correct one error (at best). Now we will describe some examples of codes that have higher distance.

A particularly simple way to construct codes that can correct more errors is to concatenate codes that can correct one error. A concatenated code is a code within a code. Suppose we have two $k = 1$ QECC's, an $[[n_1, 1, d_1]]$ code $C_1$ and an $[[n_2, 1, d_2]]$ code $C_2$. Imagine constructing a length $n_2$ codeword of $C_2$, and expanding the codeword as a coherent superposition of product states, in which each qubit is in one of the states $|0\rangle$ or $|1\rangle$. Now replace each qubit by a length-$n_1$ encoded state using the code $C_1$; that is replace $|0\rangle$ by $|\bar{0}\rangle$ and $|1\rangle$ by $|\bar{1}\rangle$ of $C_1$. The result is a code with length $n = n_1 n_2$, $k = 1$, and distance no less than $d = d_1 d_2$. We will call $C_2$ the "outer" code and $C_1$ the "inner" code.

In fact, we have already discussed one example of this construction: Shor's 9-qubit code. In that case, the inner code is the three-qubit repetition code with stabilizer generators
$$
\begin{aligned}
&\boldsymbol{Z}\boldsymbol{Z}\boldsymbol{I}, \\
&\boldsymbol{I}\boldsymbol{Z}\boldsymbol{Z},
\end{aligned}
$$ {#eq-7.213}
and the outer code is the three-qubit "phase code" with stabilizer generators
$$
\begin{aligned}
&\boldsymbol{X}\boldsymbol{X}\boldsymbol{I}, \\
&\boldsymbol{I}\boldsymbol{X}\boldsymbol{X},
\end{aligned}
$$ {#eq-7.214}
(the Hadamard rotated repetition code). We construct the stabilizer of the concatenated code as follows: Acting on each of the three qubits contained in the block of the outer code, we include the two generators $\boldsymbol{Z}_1\boldsymbol{Z}_2, \boldsymbol{Z}_2\boldsymbol{Z}_3$ of the inner code (six generators altogether). Then we add the two generators of the outer code, but with $\boldsymbol{X}, \boldsymbol{Z}$ replaced by the *encoded* operations of the inner code; in this case, these are the two generators
$$
\begin{aligned}
&\bar{\boldsymbol{X}}\bar{\boldsymbol{X}}\bar{\boldsymbol{I}}, \\
&\bar{\boldsymbol{I}}\bar{\boldsymbol{X}}\bar{\boldsymbol{X}},
\end{aligned}
$$ {#eq-7.215}
where $\bar{\boldsymbol{I}} = \boldsymbol{I}\boldsymbol{I}\boldsymbol{I}$ and $\bar{\boldsymbol{X}} = \boldsymbol{X}\boldsymbol{X}\boldsymbol{X}$. You will recognize these as the eight stabilizer generators of Shor's code that we have described earlier. In this case, the inner and outer codes both have distance 1 (e.g., $\boldsymbol{Z}\boldsymbol{I}\boldsymbol{I}$ commutes with the stabilizer of the inner code), yet the concatenated code has distance $3 > d_1 d_2 = 1$. This happens because the code has been cleverly constructed so that the weight 1 and 2 encoded operations of the inner code do not commute with the stabilizer of the outer code. (It would have been different if we had concatenated the repetition code with itself rather than with the phase code!)

We can obtain a distance 9 code (capable of correcting four errors) by concatenating the $[[5, 1, 3]]$ code with itself. The length $n = 25$ is the smallest for any known code with $k = 1$ and $d = 9$. (An $[[n, 1, 9]]$ code with $n = 23, 24$ would be consistent with the Rains bound, but it is unknown whether such a code really exists.)

The stabilizer of the $[[25, 1, 9]]$ concatenated code has 24 generators. Of these, 20 are obtained as the four generators $\boldsymbol{M}_{1,2,3,4}$ acting on each of the five subblocks of the outer code, and the remaining four are the *encoded* operators $\bar{\boldsymbol{M}}_{1,2,3,4}$ of the outer code. Notice that the stabilizer contains elements of weight 4 (the stabilizer elements acting on each of the five inner codes); therefore, the code is degenerate. This is typical of concatenated codes.

There is no need to stop at two levels of concatenation; from $L$ QECC's with parameters $[[n_1, 1, d_1]], \dots, [[n_L, 1, d_L]]$, we can construct a hierarchical code with altogether $L$ levels of codes within codes; it has length
$$
n = n_1 n_2 \dots n_L,
$$ {#eq-7.216}
and distance
$$
d \ge d_1 d_2 \dots d_L.
$$ {#eq-7.217}
In particular, by concatenating the $[[5, 1, 3]]$ code $L$ times, we may construct a code with parameters
$$
[[5^L, 1, 3^L]].
$$ {#eq-7.218}
Strictly speaking, this family of codes cannot protect against a number of errors that scales linearly with the length. Rather the ratio of the number $t$ of errors that can be corrected to the length $n$ is
$$
\frac{t}{n} \sim \frac{1}{2}\left(\frac{3}{5}\right)^L,
$$ {#eq-7.219}
which tends to zero for large $L$. But the distance $d$ may be a deceptive measure of how well the code performs — it is all right if recovery fails for *some* ways of choosing $t \ll pn$ errors, so long as recovery will be successful for the *typical* ways of choosing $pn$ faulty qubits. In fact, concatenated codes *can* correct $pn$ typical errors, for $n$ large and $p > 0$.

Actually, the way concatenated codes are usually used does not fully exploit their power to correct errors. To be concrete, consider the $[[5, 1, 3]]$ code in the case where each of the five qubits is independently subjected to the depolarizing channel with error probability $p$ (that is $\boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z}$ errors each occur with probability $p/3$). Recovery is sure to succeed if fewer than two errors occur in the block. Therefore, as in §7.5.2, we can bound the failure probability by
$$
p_{\mathrm{fail}} \equiv p^{(1)} \le \binom{5}{2} p^2 = 10 p^2.
$$ {#eq-7.220}
Now consider the performance of the concatenated $[[25, 1, 9]]$ code. To keep life easy, we will perform recovery in a simple (but nonoptimal) way: First we perform recovery on each of the five subblocks, measuring $\boldsymbol{M}_{1,2,3,4}$ to obtain an error syndrome for each subblock. After correcting the subblocks, we then measure the stabilizer generators $\bar{\boldsymbol{M}}_{1,2,3,4}$ of the outer code, to obtains its syndrome, and apply an encoded $\bar{\boldsymbol{X}}, \bar{\boldsymbol{Y}}$, or $\bar{\boldsymbol{Z}}$ to one of the subblocks if the syndrome reveals an error.

For the outer code, recovery will succeed if at most one of the subblocks is damaged, and the probability $p^{(1)}$ of damage to a subblock is bounded as in eq. (7.220); we conclude that the probability of a botched recovery for the $[[25, 1, 9]]$ code is bounded above by
$$
p^{(2)} \le 10(p^{(1)})^2 \le 10(10p^2)^2 = 1000 p^4.
$$ {#eq-7.221}
Our recovery procedure is clearly not the best possible, because four errors can induce failure if there are two each in two different subblocks. Since the code has distance nine, there is a better procedure that would always recover successfully from four errors, so that $p^{(2)}$ would be of order $p^5$ rather than $p^4$. Still, the suboptimal procedure has the advantage that it is very easily generalized, (and analyzed) if there are many levels of concatenation.

Indeed, if there are $L$ levels of concatenation, we begin recovery at the innermost level and work our way up. Solving the recursion
$$
p^{(\ell)} \le C [p^{(\ell-1)}]^2,
$$ {#eq-7.222}
starting with $p^{(0)} = p$, we conclude that
$$
p^{(L)} \le \frac{1}{C}(Cp)^{2^L},
$$ {#eq-7.223}
(where here $C = 10$). We see that as long as $p < 1/10$, we can make the failure probability as small as we please by adding enough levels to the code.

We may write
$$
p^{(L)} \le p_0 \left(\frac{p}{p_0}\right)^{2^L},
$$ {#eq-7.224}
where $p_0 = \frac{1}{10}$ is an estimate of the threshold error probability that can be tolerated (we will obtain better codes and better estimates of this threshold below). Note that to obtain
$$
p^{(L)} < \epsilon,
$$ {#eq-7.225}
we may choose the block size $n = 5^L$ so that
$$
n \le \left[\frac{\log(p_0/\epsilon)}{\log(p_0/p)}\right]^{\log_2 5}.
$$ {#eq-7.226}
In principle, the concatenated code at a high level could fail with many fewer than $n/10$ errors, but these would have to be distributed in a highly conspiratorial fashion that is quite unlikely for $n$ large.

The concatenated encoding of an unknown quantum state can be carried out level by level. For example to encode $a|0\rangle + b|1\rangle$ in the $[[25, 1, 9]]$ block, we could first prepare the state $a|\bar{0}\rangle + b|\bar{1}\rangle$ in the five qubit block, using the encoding circuit described earlier, and also prepare four five-qubit blocks in the state $|\bar{0}\rangle$. The $a|\bar{0}\rangle + b|\bar{1}\rangle$ can be encoded at the next level by executing the encoded circuit yet again, but this time with all gates replaced by encoded gates acting on five-qubit blocks. We will see in the next chapter how these encoded gates are constructed.
