# Section 7.7: CSS Codes [PDF Pages 27-29]

<!-- ============================================================ -->
<!-- Source: chap7.pdf, Physical Pages: 27-29                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 27 -->
## 7.7 CSS Codes

Principles from the theory of classical linear codes can be adapted to the construction of quantum error-correcting codes. We will describe here a family of QECC’s, the Calderbank–Shor–Steane (or CSS) codes, that exploit the concept of a dual code.

Let $C_1$ be a classical linear code with $(n - k_1) \times n$ parity check matrix $H_1$, and let $C_2$ be a subcode of $C_1$, with $(n - k_2) \times n$ parity check $H_2$, where $k_2 < k_1$. The first $n - k_1$ rows of $H_2$ coincide with those of $H_1$, but there are $k_1 - k_2$ additional linearly independent rows; thus each word in $C_2$ is contained in $C_1$, but the words in $C_2$ also obey some additional linear constraints.

The subcode $C_2$ defines an equivalence relation in $C_1$; we say that $u, v \in C_1$ are equivalent ($u \equiv v$) if and only if there is a $w$ in $C_2$ such that $u = v + w$. The equivalence classes are the cosets of $C_2$ in $C_1$.

A CSS code is a $k = k_1 - k_2$ quantum code that associates a codeword with each equivalence class. Each element of a basis for the code subspace can be expressed as

$$
|\bar{w}\rangle = \frac{1}{\sqrt{2^{k_2}}} \sum_{v \in C_2} |v + w\rangle,
$$ {#eq-7.89}

an equally weighted superposition of all the words in the coset represented by $w$. There are $2^{k_1 - k_2}$ cosets, and hence $2^{k_1 - k_2}$ linearly independent codewords. The states $|\bar{w}\rangle$ are evidently normalized and mutually orthogonal; that is, $\langle\bar{w}|\bar{w}'\rangle = 0$ if $w$ and $w'$ belong to different cosets.

Now consider what happens to the codeword $|\bar{w}\rangle$ if we apply the bitwise Hadamard transform $\boldsymbol{H}^{(n)}$:

$$
\begin{aligned}
\boldsymbol{H}^{(n)} : |\bar{w}\rangle_F &\equiv \frac{1}{\sqrt{2^{k_2}}} \sum_{v \in C_2} |v + w\rangle \\
&\to |\bar{w}\rangle_P \equiv \frac{1}{\sqrt{2^n}} \sum_u \frac{1}{\sqrt{2^{k_2}}} \sum_{v \in C_2} (-1)^{u \cdot v}(-1)^{u \cdot w}|u\rangle \\
&= \frac{1}{\sqrt{2^{n-k_2}}} \sum_{u \in C_2^\perp} (-1)^{u \cdot w}|u\rangle;
\end{aligned}
$$ {#eq-7.90}

we obtain a coherent superposition, weighted by phases, of words in the dual code $C_2^\perp$ (in the last step we have used the identity eq. (7.85)). It is again manifest in this last expression that the codeword depends only on the $C_2$ coset that $w$ represents — shifting $w$ by an element of $C_2$ has no effect on $(-1)^{u \cdot w}$ if $u$ is in the code dual to $C_2$.

Now suppose that the code $C_1$ has distance $d_1$ and the code $C_2^\perp$ has distance $d_2^\perp$, such that

$$
\begin{aligned}
d_1 &\ge 2t_F + 1, \\
d_2^\perp &\ge 2t_P + 1.
\end{aligned}
$$ {#eq-7.91}

Then we can see that the corresponding CSS code can correct $t_F$ bit flips and $t_P$ phase flips. If $e$ is a binary string of length $n$, let $\boldsymbol{E}_e^{(\text{flip})}$ denote the Pauli operator with an $\boldsymbol{X}$ acting at each location $i$ where $e_i = 1$; it acts on the state $|v\rangle$ according to

$$
\boldsymbol{E}_e^{(\text{flip})} : |v\rangle \to |v + e\rangle.
$$ {#eq-7.92}

And let $\boldsymbol{E}_e^{(\text{phase})}$ denote the Pauli operator with a $\boldsymbol{Z}$ acting where $e_i = 1$; its action is

$$
\boldsymbol{E}_e^{(\text{phase})} : |v\rangle \to (-1)^{v \cdot e}|v\rangle,
$$ {#eq-7.93}

<!-- Page 28 -->
which in the Hadamard rotated basis becomes

$$
\boldsymbol{E}_e^{(\text{phase})} : |u\rangle \to |u + e\rangle.
$$ {#eq-7.94}

Now, in the original basis (the $F$ or “flip” basis), each basis state $|\bar{w}\rangle_F$ of the CSS code is a superposition of words in the code $C_1$. To diagnose bit flip error, we perform on data and ancilla the unitary transformation

$$
|v\rangle \otimes |0\rangle_A \to |v\rangle \otimes |H_1 v\rangle_A,
$$ {#eq-7.95}

and then measure the ancilla. The measurement result $H_1 e_F$ is the bit flip syndrome. If the number of flips is $t_F$ or fewer, we may correctly infer from this syndrome that bit flips have occurred at the locations labeled by $e_F$. We recover by applying $\boldsymbol{X}$ to the qubits at those locations.

To correct phase errors, we first perform the bitwise Hadamard transformation to rotate from the $F$ basis to the $P$ (“phase”) basis. In the $P$ basis, each basis state $|\bar{w}\rangle_P$ of the CSS code is a superposition of words in the code $C_2^\perp$. To diagnose phase errors, we perform a unitary transformation

$$
|v\rangle \otimes |0\rangle_A \to |v\rangle \otimes |G_2 v\rangle_A,
$$ {#eq-7.96}

and measure the ancilla ($G_2$, the generator matrix of $C_2$, is also the parity check matrix of $C_2^\perp$). The measurement result $G_2 e_P$ is the phase error syndrome. If the number of phase errors is $t_P$ or fewer, we may correctly infer from this syndrome that phase errors have occurred at locations labeled by $e_P$. We recover by applying $\boldsymbol{X}$ (in the $P$ basis) to the qubits at those locations. Finally, we apply the bitwise Hadamard transformation once more to rotate the codewords back to the original basis. (Equivalently, we may recover from the phase errors by applying $\boldsymbol{Z}$ to the affected qubits after the rotation back to the $F$ basis.)

If $e_F$ has weight less than $d_1$ and $e_P$ has weight less than $d_2^\perp$, then

$$
\langle\bar{w}|\boldsymbol{E}_{e_P}^{(\text{phase})} \boldsymbol{E}_{e_F}^{(\text{flip})} |\bar{w}'\rangle = 0
$$ {#eq-7.97}

(unless $e_F = e_P = 0$). Any Pauli operator can be expressed as a product of a phase operator and a flip operator — a $\boldsymbol{Y}$ error is merely a bit flip and phase error both afflicting the same qubit. So the distance $d$ of a CSS code satisfies

$$
d \ge \min(d_1, d_2^\perp).
$$ {#eq-7.98}

CSS codes have the special property (not shared by more general QECC’s) that the recovery procedure can be divided into two separate operations, one to correct the bit flips and the other to correct the phase errors.

The unitary transformation eq. (7.95) (or eq. (7.96)) can be implemented by executing a simple quantum circuit. Associated with each of the $n - k_1$ rows of the parity check matrix $H_1$ is a bit of the syndrome to be extracted. To find the $a$th bit of the syndrome, we prepare an ancilla bit in the state $|0\rangle_{A,a}$, and for each value of $\lambda$ with $(H_1)_{a\lambda} = 1$, we execute a controlled-NOT gate with the ancilla bit as the target and qubit $\lambda$ in the data block as the control. When measured, the ancilla qubit reveals the value of the parity check bit $\sum_\lambda (H_1)_{a\lambda} v_\lambda$.

Schematically, the full error correction circuit for a CSS code has the form:

– Figure –  

<!-- Page 29 -->
Separate syndromes are measured to diagnose the bit flip errors and the phase errors. An important special case of the CSS construction arises when a code $C$ contains its dual $C^\perp$. Then we may choose $C_1 = C$ and $C_2 = C^\perp \subseteq C$; the $C$ parity check is computed in both the $F$ basis and the $P$ basis to determine the two syndromes.
