# Section 7.4: Some general properties of QECC's [PDF Pages 18-21]

<!-- ============================================================ -->
<!-- Source: chap7.pdf, Physical Pages: 18-21                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 18 -->
## 7.4 Some general properties of QECC's

We say a quantum code is binary if it can be represented in terms of qubits. In a binary code, a code subspace $\mathcal{H}_{\text{code}}$ of dimension $2^k$ is embedded in a system $\mathcal{H}_S$ of dimension $2^n$, where $k$ and $n > k$ are nonnegative integers. We call $n$ the block size or length of the code, and refer to $k$ as the number of encoded or protected qubits. There is actually no need to require the dimensions of $\mathcal{H}_S$ and $\mathcal{H}_{\text{code}}$ to be powers of two (see the exercises); nevertheless we will mostly confine our attention in this chapter to binary coding, which is the simplest case and the case that typically arises in applications to quantum computing.

A convenient basis for the linear operators acting on an $n$-qubit Hilbert space is provided by the $2^{2n}$ Pauli operators

$$
\{\boldsymbol{I}, \boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z}\}^{\otimes n}.
$$ {#eq-7.43}

Each Pauli operator, a tensor product of $n$ $2\times 2$ Pauli matrices, can be assigned a weight, an integer ranging from 0 to $n$. The weight $w$ is the number of nontrivial Pauli matrices in the tensor product; that is, a weight-$w$ Pauli operator applies the identity $\boldsymbol{I}$ to $n - w$ of the qubits, and applies one of $\{\boldsymbol{X}, \boldsymbol{Y}, \boldsymbol{Z}\}$ to each of the remaining $w$ qubits. Any

<!-- Page 19 -->
$n$-qubit linear operator $\boldsymbol{M}$, even if not a Pauli operator, can also be assigned a weight. Because the Pauli operators are linearly independent, $\boldsymbol{M}$ has a unique expansion as a sum of Pauli operators, and we say $\boldsymbol{M}$ has weight $w$ if a weight-$w$ Pauli operator occurs in that expansion with a nonzero coefficient, while no Pauli operator with weight greater than $w$ occurs in the expansion. Note that if $\boldsymbol{M}_1$ has weight $w_1$ and $\boldsymbol{M}_2$ has weight $w_2$, then the product $\boldsymbol{M}_1\boldsymbol{M}_2$ has weight at most $w_1 + w_2$.

### 7.4.1 Distance

In addition to the length $n$ and the number of encoded qubits $k$, another important parameter characterizing a code is its distance $d$. The distance $d$ is the minimum weight of an operator $\boldsymbol{E}$ such that

$$
\boldsymbol{\Pi}\boldsymbol{E}\boldsymbol{\Pi} \not\propto \boldsymbol{\Pi}.
$$ {#eq-7.44}

Since any operator can be expanded as a linear combination of Pauli operators, we may equivalently say that $d$ is the minimum weight for a Pauli operator $\boldsymbol{E}$ satisfying eq.(7.44). We will describe a quantum code with block size $n$, $k$ encoded qubits, and distance $d$ as an “$[[n, k, d]]$ quantum code.” We use the double-bracket notation for quantum codes, to distinguish from the $[n, k, d]$ notation used for classical codes.

We say that a quantum error-correcting code can “correct $t$ errors” if the span of the set $\mathcal{E}$ of correctable errors includes all operators of weight $t$ or less; equivalently, all Pauli operators of weight $\le t$ are correctable errors. Our definition of distance implies that the criterion for error correction

$$
\boldsymbol{\Pi}\boldsymbol{E}_b^\dagger \boldsymbol{E}_a\boldsymbol{\Pi} = C_{ba}\boldsymbol{\Pi},
$$ {#eq-7.45}

will be satisfied by all operators $\boldsymbol{E}_a, \boldsymbol{E}_b$ of weight $t$ or less, provided that $d \ge 2t+1$, because the operator $\boldsymbol{E}_b^\dagger \boldsymbol{E}_a$ has weight at most $2t$. Therefore, a quantum error-correcting code with distance $d \ge 2t+1$ can correct $t$ errors.

### 7.4.2 Located errors

A distance $d = 2t+1$ code can correct $t$ errors, irrespective of the location of the errors in the code block. But in some cases we may know that particular qubits in the code block are the only ones that have been damaged, in which case we speak of located errors. A given code can protect more errors if the errors occur at known locations rather than unknown locations.

Located errors might arise because we saw a hammer strike $t < n$ of the $n$ qubits in the code block, while the other $n - t$ qubits remained well protected. The erasure errors considered in §7.3.4 may also be regarded as located errors. Perhaps you sent a block of $n$ qubits to me, but $t < n$ of the qubits were lost and never received, while I am confident that the $n - t$ qubits that did arrive were well packaged and were received undamaged. This is an erasure error. If I replace the $t$ missing qubits with $t$ qubits in an arbitrary state, the erasure error becomes a located error because I know which of the $t$ qubits in the block of $n$ are the damaged ones.

A QECC with distance $d = t+1$ can correct $t$ errors at known locations. In this case, the set $\mathcal{E}$ of errors to be corrected is the set of all Pauli operators with support at the $t$ specified locations (each $\boldsymbol{E}_a$ acts trivially on the other $n - t$ qubits). But then, for each $\boldsymbol{E}_a$ and $\boldsymbol{E}_b$ in $\mathcal{E}$, the product $\boldsymbol{E}_b^\dagger \boldsymbol{E}_a$ also has weight at most $t$. Therefore, the error

<!-- Page 20 -->
correction criterion is satisfied for all $\boldsymbol{E}_{a,b} \in \mathcal{E}$, provided the code has distance at least $t+1$. Thus a QECC that corrects $t$ errors at arbitrary locations can correct $2t$ errors at known locations.

### 7.4.3 Error detection

In some cases we may be satisfied to detect whether an error has occurred, even if we are unable to fully diagnose or reverse the error. A measurement designed for error detection has two possible outcomes: “good” and “bad.” If the good outcome occurs, we are assured that the quantum state is undamaged. If the bad outcome occurs, damage has been sustained, and the state should be discarded.

If the error map has its support on the set $\mathcal{E}$ of all Pauli operators of weight up to $t$, and it is possible to make a measurement that correctly diagnoses whether an error has occurred, then it is said that we can detect $t$ errors. Error detection is easier than error correction, so a given code can detect more errors than it can correct. In fact, a QECC with distance $d = t+1$ can detect $t$ errors.

A code with $d = t+1$ has the property

$$
\boldsymbol{\Pi}\boldsymbol{E}_a\boldsymbol{\Pi} = C_a\boldsymbol{\Pi}
$$ {#eq-7.46}

for every Pauli operator $\boldsymbol{E}_a$ of weight $t$ or less (where $\boldsymbol{\Pi}$ is the orthogonal projector onto $\mathcal{H}_{\text{code}}$) or

$$
\boldsymbol{E}_a|\psi\rangle = C_a|\psi\rangle + |\psi_a^\perp\rangle,
$$ {#eq-7.47}

where $|\psi\rangle$ is any vector in $\mathcal{H}_{\text{code}}$ and $|\psi_a^\perp\rangle$ is an (unnormalized) vector orthogonal to the code subspace. Therefore, the general error map in which all errors have weight $t$ or less acts on the code state $|\psi\rangle_S$ according to

$$
|\psi\rangle_S \mapsto \sum_{\boldsymbol{E}_a \in \mathcal{E}} \boldsymbol{E}_a|\psi\rangle_S \otimes |\varphi_a\rangle_E = |\psi\rangle_S \otimes \left( \sum_{\boldsymbol{E}_a \in \mathcal{E}} C_a|\varphi_a\rangle_E \right) + |\text{orthog}\rangle_{SE},
$$ {#eq-7.48}

where $\mathcal{E}$ is the set of all Pauli operators of weight up to $t$, and $|\text{orthog}\rangle$ denotes a vector orthogonal to the code subspace.

Now we can perform an orthogonal measurement on the system $S$, with two possible outcomes: the state is projected onto either the code subspace $\mathcal{H}_{\text{code}}$ or the complementary subspace of $\mathcal{H}_S$. If the first (good) outcome is obtained, the undamaged state $|\psi\rangle$ is recovered. If the second outcome (bad) is found, an error has been detected. We conclude that our QECC with distance $d$ can detect $d-1$ errors. Thus a QECC that corrects $t$ errors can detect $2t$ errors.

### 7.4.4 Quantum codes and entanglement

A QECC protects quantum information from error by encoding it nonlocally, that is, by sharing it among many qubits in a block. Thus a quantum codeword is a highly entangled state.

In fact, a distance $d = t+1$ nondegenerate code has the following property: Choose any state $|\psi\rangle$ in the code subspace and any $t$ qubits in the block. Trace over the remaining $n - t$ qubits to obtain

$$
\boldsymbol{\rho}_{(t)} = \text{tr}_{(n-t)}|\psi\rangle\langle\psi|,
$$ {#eq-7.49}

<!-- Page 21 -->
the density operator of the $t$ qubits. Then this density operator is maximally mixed:

$$
\boldsymbol{\rho}_{(t)} = \frac{1}{2^t}\boldsymbol{I}.
$$ {#eq-7.50}

In any distance-$(t+1)$ code, whether degenerate or not, we cannot acquire any information about the encoded data by observing any $t$ qubits in the block; that is, $\boldsymbol{\rho}_{(t)}$ is a constant, independent of the codeword. But our conclusion that the density operator of any $t$ qubits must be maximally mixed applies only if the code is nondegenerate.

To verify the property eq.(7.50), we note that for a nondegenerate distance-$(t+1)$ code,

$$
\boldsymbol{\Pi}\boldsymbol{E}_a\boldsymbol{\Pi} = 0
$$ {#eq-7.51}

for any $\boldsymbol{E}_a$ of nonzero weight up to $t$, so that

$$
\text{tr}(\boldsymbol{\rho}_{(t)}\boldsymbol{E}_a) = \langle\psi|\boldsymbol{E}_a|\psi\rangle = \langle\psi|\boldsymbol{\Pi}\boldsymbol{E}_a\boldsymbol{\Pi}|\psi\rangle = 0,
$$ {#eq-7.52}

for any $t$-qubit Pauli operator $\boldsymbol{E}_a$ other than the identity. Now $\boldsymbol{\rho}_{(t)}$, like any Hermitian $2^t \times 2^t$ matrix, can be expanded in terms of Pauli operators:

$$
\boldsymbol{\rho}_{(t)} = \left(\frac{1}{2^t}\right)\boldsymbol{I} + \sum_{\boldsymbol{E}_b \ne \boldsymbol{I}} \rho_b \boldsymbol{E}_b.
$$ {#eq-7.53}

Since the Pauli operators satisfy

$$
\left(\frac{1}{2^t}\right)\text{tr}(\boldsymbol{E}_b^\dagger \boldsymbol{E}_a) = \delta_{ba},
$$ {#eq-7.54}

we find that each $\rho_b = 0$, and we conclude that $\boldsymbol{\rho}_{(t)}$ is a multiple of the identity. That is, for any state in the code space, and any set of $t$ qubits in the code block, these qubits are maximally entangled with the complementary set of qubits in the block.
