# Section 7.12: Quantum secret sharing

**Source:** Preskill Lecture Notes, Chapter 7, pp. 38–40 (Physical pages 44–46).

---

The $[[5, 1, 3]]$ code provides a nice illustration of a possible application of QECC's.[^7-2]

Suppose that some top secret information is to be entrusted to $n$ parties. Because none is entirely trusted, the secret is divided into $n$ shares, so that each party, with access to his share alone, can learn nothing at all about the secret. But if enough parties get together and pool their shares, they can decipher the secret or some part of it.

In particular, an $(m, n)$ threshold scheme has the property that $m$ shares are sufficient to reconstruct all of the secret information. But from $m - 1$ shares, no information at all can be extracted. (This is called a threshold scheme because as shares $1, 2, 3 \dots, m - 1$ are collected one by one, nothing is learned, but the next share crosses the threshold and reveals everything.)

We should distinguish two kinds of secrets: a classical secret is an a priori unknown bit string, while a quantum secret is an a priori unknown quantum state. Either type of secret can be shared. In particular, we can distribute a classical secret among several parties by selecting one from an ensemble of mutually orthogonal (entangled) quantum states, and dividing the state among the parties.

We can see, for example, that the $[[5, 1, 3]]$ code may be employed in a $(3, 5)$ threshold scheme, where the shared information is classical. One classical bit is encoded by preparing one of the two orthogonal states $|\bar{0}\rangle$ or $|\bar{1}\rangle$ and then the five qubits are distributed to five parties. We have seen that (since the code is nondegenerate) if any two parties get together, then the density matrix $\rho$ of their two qubits is
$$
\rho^{(2)} = \frac{1}{4}\mathbf{1} .
$$ {#eq-7.165}
Hence, they learn nothing about the quantum state from any measurement of their two qubits. But we have also seen that the code can correct two located errors or two erasures. When any three parties get together, they may correct the two errors (the two missing qubits) and perfectly reconstruct the encoded state $|\bar{0}\rangle$ or $|\bar{1}\rangle$.

It is also clear that by a similar procedure a single qubit of quantum information can be shared — the $[[5, 1, 3]]$ code is also the basis of a $((3, 5))$ quantum threshold scheme (we use the $((m, n))$ notation if the shared information is quantum information, and the $(m, n)$ notation if the shared information is classical). How does this quantum-secret-sharing scenario generalize to more qubits? Suppose we prepare a pure state $|\psi\rangle$ of $n$ qubits — can it be employed in an $((m, n))$ threshold scheme?

We know that $m$ qubits must be sufficient to reconstruct the state; hence $n - m$ erasures can be corrected. It follows from our general error correction criterion that the expectation value of any weight-$(n - m)$ observable must be independent of the state $|\psi\rangle$
$$
\langle\psi| E |\psi\rangle \text{ independent of } |\psi\rangle, \quad \text{wt}(E) \le n - m .
$$ {#eq-7.166}
Thus, if $m$ parties have all the information, the other $n - m$ parties have no information at all. That makes sense, since quantum information cannot be cloned.

On the other hand, we know that $m - 1$ shares reveal nothing, or that
$$
\langle\psi| E |\psi\rangle \text{ independent of } |\psi\rangle, \quad \text{wt}(E) \le m - 1 .
$$ {#eq-7.167}
It then follows that $m - 1$ erasures can be corrected, or that the other $n - m + 1$ parties have all the information.

From these two observations we obtain the two inequalities
$$
\begin{aligned}
n - m < m &\implies n < 2m , \\
m - 1 < n - m + 1 &\implies n > 2m - 2 .
\end{aligned}
$$ {#eq-7.168}
It follows that
$$
n = 2m - 1 ,
$$ {#eq-7.169}
in an $((m, n))$ pure state quantum threshold scheme, where each party has a single qubit. In other words, the threshold is reached as the number of qubits in hand crosses over from the minority to the majority of all $n$ qubits.

We see that if each share is a qubit, a quantum pure state threshold scheme is a $[[2m - 1, k, m]]$ quantum code with $k \ge 1$. But in fact the $[[3, 1, 2]]$ and $[[7, 1, 4]]$ codes do not exist, and it follows from the Rains bound that the $m > 3$ codes do not exist. In a sense, then, the $[[5, 1, 3]]$ code is the unique quantum threshold scheme.

There are a number of caveats — the restriction $n = 2m - 1$ continues to apply if each share is a $q$-dimensional system rather than a qubit, but various
$$
[[2m - 1, 1, k]]_q
$$ {#eq-7.170}
codes can be constructed for $q > 2$. (See the exercises for an example.)

Also, we might allow the shared information to be a mixed state (that encodes a pure state). For example, if we discard one qubit of the five qubit block, we have a $((3, 4))$ scheme. Again, once we have three qubits, we can correct two erasures, one arising because the fourth share is in the hands of another party, the other arising because a qubit has been thrown away.

Finally, we have assumed that the shared information is quantum information. But if we are only sharing classical information instead, then the conditions for correcting erasures are less stringent. For example, a Bell pair may be regarded as a kind of $(2, 2)$ threshold scheme for two bits of classical information, where the classical information is encoded by choosing one of the four mutually orthogonal states $|\phi^\pm\rangle, |\psi^\pm\rangle$. A party in possession of one of the two qubits is unable to access any of this classical information. But this is not a scheme for sharing a quantum secret, since linear combinations of these Bell states do not have the property that $\rho = \frac{1}{2}\mathbf{1}$ if we trace out one of the two qubits.

---

[^7-2]: R. Cleve, D. Gottesman, and H.-K. Lo, "How to Share a Quantum Secret," quant-ph/9901025.
