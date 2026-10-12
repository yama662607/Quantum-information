# Section 6.9: Classical simulation of slightly entangling quantum computations

## Transcript (English Original)

### 6.9 Classical simulation of slightly entangling quantum computations [chap6.pdf#page=48]

How hard is it to simulate a quantum computer using a classical computer? Clearly, we would like to understand more deeply the classical and quantum complexity of solving the time-dependent and time-independent Schroedinger equations. In particular, we wish to identify cases for which the problem seems to be hard classically and easy quantumly, for these are cases where quantum computers will find a useful niche.

More broadly, why do we believe that quantum computers are more powerful than classical ones, and what is the source of the quantum computer's power? Roughly speaking, it seems to be hard to simulate a quantum system with a classical computer because the Hilbert space of the quantum computer is exponentially large in the number of qubits $n$, and that exponentially large Hilbert space is needed to accommodate and describe the quantum correlations among the qubits in a many-body quantum system. From this perspective, it seems legitimate to claim that quantum entanglement is the source of the quantum computer's power. On the other hand, that claim may be too simplistic, because: 1) Some quantum computations that generate highly entangled quantum states are easy to simulate classically. We'll see an example next term when we discuss (in connection with quantum error correction) quantum computation using the Clifford group. 2) For *mixed* states, simulating a quantum computation classically might be hard even if the state remains separable (that is, unentangled) at all times during the computation — even if the correlations among the parts of the quantum computer are "classical" they could still be hard to simulate. You examined an example in a homework problem: estimating the trace of an exponentially large unitary matrix using just "one clean qubit."

So let's ask the question this way: for quantum computation with pure states, if the qubits in the computer never become highly entangled during the course of the computation, can we simulate the quantum computer efficiently with a classical computer? As we'll see, the answer is yes.

Imagine that $n$ qudits ($d$-dimensional systems) are arranged in a line, and consider cutting the system into two parts anywhere along the line: there are $m$ qudits to the left of the cut and $n-m$ qubits to the right of the cut. Suppose that for any way of choosing where we cut the chain, the entanglement between the two parts is bounded above by a constant (independent of the system size $n$). We could quantify the entanglement in various ways, and the conclusion would be the same, but to keep the discussion simple [chap6.pdf#page=49] let us use the Schmidt number. Recall that the Schmidt number is the number of terms in the Schmidt expansion of a bipartite pure state — equivalently it is the rank of the density operator for either part.

While in principle the Schmidt number could be as large as $d^{n/2}$ when the system is cut into two subsystems of equal size, let us assume that
$$
\text{Schmidt number} \le D = \text{constant}.
$$ (6.219)

We claim that under this assumption:
1. There is a succinct classical description of the pure state of $n$ qudits.
2. A computation in which the $n$ qudits have bounded Schmidt number at all times can be efficiently simulated on a classical computer.

First, let's construct the succinct description. The $n$-qudit state $|\psi\rangle$ can be expanded in the standard basis as
$$
|\psi\rangle = \sum c^{i_1 i_2 \dots i_n} |i_1 i_2 \dots i_n\rangle
$$ (6.220)
in terms of the $d^n$ complex numbers $\{c^{i_1 i_2 \dots i_n}\}$. This is not succinct in general, but if the Schmidt rank is bounded then each $c^{i_1 i_2 \dots i_n}$ can be expressed as a contraction of tensors, where each tensor has 3 indices, and each index has a constant number of values:

-figure-

Here each $(P_k)^{i_k}_{\alpha_{k-1} \alpha_k}$ has $dD^2$ entries (except for the sites at the ends of the chain, which have $dD$ entries). Therefore, the state is described by $ndD^2$ complex parameters, a number that is linear rather than exponential in $n$. (In the case of a product state, this becomes $nd$ parameters.)

To obtain this compressed description of the $n$-site state $|\psi\rangle$ we perform the Schmidt decomposition repeatedly ($n - 1$ times in succession). In the first step we divide the system between qudits 1 and 2:
$$
|\psi\rangle = \sum_{\alpha_1} \lambda_{1\alpha_1} |\psi_{1\alpha_1}\rangle |\phi_{2\alpha_1}\rangle.
$$ (6.221)
Here the $\{\lambda_{1\alpha_1}\}$ are Schmidt coefficients, the $\{|\psi_{1\alpha_1}\rangle\}$ are elements of an orthonormal basis for the first qudit, and $\{|\phi_{2\alpha_1}\rangle\}$ are elements of an orthonormal basis for qudits $2, 3, \dots n$. We can expand $|\psi_{1\alpha_1}\rangle$ in the standard basis, obtaining
$$
|\psi\rangle = \sum_{\alpha_1} \sum_{i_1} \lambda_{1\alpha_1} \psi_{1\alpha_1}^{i_1} |i_1\rangle |\phi_{2\alpha_1}\rangle = \sum_{\alpha_1} \sum_{i_1} (P_1^{i_1})_{\alpha_1} |i_1\rangle |\phi_{2\alpha_1}\rangle,
$$ (6.222)
where $(P_1^{i_1})_{\alpha_1} = \lambda_{1\alpha_1} \psi_{1\alpha_1}^{i_1}$. Now we Schmidt decompose $|\phi_{2\alpha_1}\rangle$ across the cut between qudits 2 and 3, finding
$$
|\phi_{2\alpha_1}\rangle = \sum_{\alpha_2} \sum_{i_2} (P_2^{i_2})_{\alpha_1\alpha_2} |i_2\rangle |\phi_{3\alpha_2}\rangle.
$$ (6.223)
Note that there is no $\alpha_1$ label on the states $\{|\phi_{3\alpha_2}\rangle\}$. That is because these are the states occurring in the Schmidt decomposition across the 2-3 cut that describe the right side of [chap6.pdf#page=50] the cut. These states have nothing to do with $\alpha_1$, which labels the states in the Schmidt decomposition across the 1-2 cut.

Repeating the Schmidt decomposition $n - 1$ times we find
$$
|\psi\rangle = \sum_{\alpha_1 \dots \alpha_{n-1}} \sum_{i_1, \dots i_n} (P_1^{i_1})_{\alpha_1} (P_2^{i_2})_{\alpha_1\alpha_2} (P_3^{i_3})_{\alpha_2\alpha_3} \dots (P_n^{i_n})_{\alpha_{n-1}} |i_1 i_2 \dots i_n\rangle.
$$ (6.224)
This is the decomposition in terms of contracted tensors that we sought. It is called the *matrix product state* (MPS) decomposition of $|\psi\rangle$. It exists for any $|\psi\rangle$, but for generic $|\psi\rangle$, the matrices in the middle of the chain of $n$ qudits become exponentially large in $n$. Under the assumption of bounded Schmidt rank, however, $(P_1)^{i_1}$ and $(P_n)^{i_n}$ are $D$-component vectors and $(P_k)^{i_k}$ for $k = 2, 3, \dots n-1$ are $D \times D$ matrices.

Therefore, we have expressed $|\psi\rangle = \sum_{i_1, \dots i_n} P_1^{i_1} P_2^{i_2} \dots P_n^{i_n} |i_1 i_2 \dots i_n\rangle$ where the coefficient is a product of matrices. If we don't want the endpoints to be special we can replace $P_1^{i_1}$ and $P_n^{i_n}$ by $D \times D$ matrices contracted with one another; then
$$
|\psi\rangle = \sum_{i_1, \dots i_n} \mathrm{tr}\left(P_1^{i_1} P_2^{i_2} \dots P_n^{i_n}\right) |i_1 i_2 \dots i_n\rangle.
$$ (6.225)
This description looks like the MPS locally, but with the ends of the chain now glued together.

Suppose that the qudits are arranged in a one-dimensional chain, and that a circuit of geometrically local quantum gates acts on the state, such that each gate acts on a pair of neighboring qudits. We want to see that the MPS description can be efficiently updated as this circuit is executed. If a unitary transformation $U$ acts on a pair of neighboring qudits on the chain as in

-figure-

this unitary affects only two neighboring matrices:
$$
\sum_\beta (P^i)_{\alpha\beta} (Q^j)_{\beta\gamma} \mapsto \sum_\beta \sum_{i'j'} U^{ij}_{i'j'} (P^{i'})_{\alpha\beta} (Q^{j'})_{\beta\gamma} \equiv M^{ij}_{\alpha\gamma}.
$$ (6.226)
Now we need to update the Schmidt decomposition across the $P-Q$ cut:

-figure-

We regard $M^{ij}_{\alpha\gamma}$ as a $dD \times dD$ matrix, and we perform its *singular value decomposition* (SVD). Recall that for any matrix $M$, there are unitary matrices $V_L$ and $V_R$ such that $M = V_L^\dagger \Delta V_R$, where $\Delta$ is diagonal. This Schmidt decomposes the state
$$
\sum_{ac} M_{ac} |ac\rangle = \sum_b \Delta_b |\psi_{Lb}\rangle \otimes |\psi_{Rb}\rangle
$$ (6.227)
where $|\psi_{Lb}\rangle = \sum_a |a\rangle V^\dagger_{Lab}$ and $|\psi_{Rb}\rangle = \sum_c |c\rangle V^\dagger_{Rbc}$. Here $|ac\rangle$ is shorthand for $|\alpha i, \gamma j\rangle$, where $|\alpha\rangle$ labels the states in the Schmidt decomposition across the cut just to the left of [chap6.pdf#page=51] the two neighboring sites where $U$ acts, and $\gamma$ labels states in the Schmidt decomposition across the cut just to the right.

The SVD of an $N \times N$ matrix can be computed in time $O(N^3)$ on a classical computer. In the case of $M^{ij}_{\alpha\gamma}$, for which $N = dD$, this is time $O(d^3 D^3)$. In general, the middle index $b$ would be summed over $N (= dD)$ values. But if the Schmidt rank stays bounded by $D$, the matrix $\Delta$ has at most $D$ nonzero eigenvalues. We may identify $(P'^i)_{\alpha\beta} = (V_L^\dagger \sqrt{\Delta})^i_{\alpha\beta}$ and $(Q'^j)_{\beta\gamma} = (\sqrt{\Delta} V_R)^j_{\beta\gamma}$, where $\beta$ is summed over $D$ values, completing the update of the MPS. The point is that when $U$ acts on neighboring sites labeled $a, a + 1$, we need not update the Schmidt states to the left of site $a$ or to the right of site $a + 1$.

Acting on a product state, any 2-qudit state acting across a given cut can produce a state with Schmidt number at most $d^2$ across that cut.

-figure-

This can be achieved by a SWAP gate acting on two maximally entangled pairs, one on each side of the cut. Likewise, acting on a state with Schmidt number $D$, the two-qudit gate can increase the Schmidt number to at most $d^2 D$. This means that, starting with a product state, a circuit in which no more than $G$ gates act across any particular cut creates a state with Schmidt number at most $D = (d^2)^G$ across that cut. (We can simulate a 2-qudit gate $U$ acting across the cut by swapping the qubits until they are at adjacent sites on either side of the cut, applying $U$, and then swapping back. Only $U$, not the swaps, increases the Schmidt number, and it increases it by at most the factor $d^2$.) The quantum state admits an efficient MPS classical description provided that the Schmidt number $D$ is bounded above by $\mathrm{poly}(n)$ across every cut, and furthermore this description can be efficiently updated each time a quantum gate is applied. It follows that a quantum computation acting on $n$ qubits can be simulated efficiently by a classical computer if the initial state of the quantum computer is a product state, and the number of gates that act across each cut (for some ordering of the qubits) is $O(\log n)$, since in that case we have $D \le (d^2)^{O(\log n)} = n^{O(\log d^2)}$.

We should also note that, for an MPS, local measurements of the qudits in the chain are easy to simulate. First let's impose the proper normalization condition on the state $|\psi\rangle$:
$$
\begin{aligned}
|\psi\rangle &= \sum_{i_1, \dots i_n} \mathrm{tr}\left(P_1^{i_1} P_2^{i_2} \dots P_n^{i_n}\right) |i_1 i_2 \dots i_n\rangle \\
\implies \langle\psi|\psi\rangle &= \sum_{i_1, \dots i_n} \left|\mathrm{tr}\left(P_1^{i_1} P_2^{i_2} \dots P_n^{i_n}\right)\right|^2,
\end{aligned}
$$ (6.228)
which is conveniently written as
$$
\sum_{i_1, \dots i_n} \mathrm{tr}\left(\left(P_1^{i_1} \otimes P_1^{i_1*}\right)\left(P_2^{i_2} \otimes P_2^{i_2*}\right) \dots \left(P_n^{i_n} \otimes P_n^{i_n*}\right)\right) = \mathrm{tr}(E_1 E_2 \dots E_n),
$$ (6.229)
where $E_k = \sum_{i_k} P_k^{i_k} \otimes P_k^{i_k*}$ is a $D^2 \times D^2$ matrix. The expectation value of a product [chap6.pdf#page=52] observable can be expressed as:
$$
\begin{aligned}
\langle\psi|\mathcal{O}_1 \otimes \mathcal{O}_2 \otimes \dots \otimes \mathcal{O}_n|\psi\rangle &= \sum_{j_1 \dots j_n} \sum_{i_1 \dots i_n} \mathrm{tr}\left(P_1^{j_1*} \dots P_n^{j_n*}\right) \langle j_1|\mathcal{O}_1|i_1\rangle \dots \langle j_n|\mathcal{O}_n|i_n\rangle \times \mathrm{tr}\left(P_1^{i_1} \dots P_n^{i_n}\right) \\
&= \mathrm{tr}\left(E_1(\mathcal{O}_1) E_2(\mathcal{O}_2) \dots E_n(\mathcal{O}_n)\right)
\end{aligned}
$$ (6.230)
where $E_k(\mathcal{O}_k) = \sum_{i_k, j_k} \left(P_k^{i_k} \otimes P_k^{j_k*}\right) \langle j_k|\mathcal{O}_k|i_k\rangle$ is also a $D^2 \times D^2$ matrix. We can evaluate the trace of a product of $n$ constant-size matrices in time $O(n)$. This completes the proof that slightly entangled quantum computations can be classically simulated in polynomial time.

Finally, let's return to the problem of finding the energy of the ground state of a local Hamiltonian. In many one-dimensional systems studied in physics, the ground state and low-lying excited states can be well approximated by an MPS with a reasonable matrix size. That is, there is a good approximation to e.g. the ground state with maximal Schmidt number across any cut
$$
D = \mathrm{poly}(n).
$$ (6.231)
However there are local Hamiltonians (even translation-invariant ones) for which finding the ground state energy seems to be hard not only for classical computers but also for quantum computers! In these cases, either an accurate MPS representation requires matrices super-polynomial in size, or, if there is a good MPS approximation with $D = \mathrm{poly}(n)$, it must be a hard computational task to find that approximation.
