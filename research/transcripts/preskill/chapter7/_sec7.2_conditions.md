# Section 7.2: Conditions for quantum error correction [PDF Pages 10-14]

<!-- ============================================================ -->
<!-- Source: chap7.pdf, Physical Pages: 10-14                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 10 -->
## 7.2 Conditions for quantum error correction

In our discussion of error recovery using the nine-qubit code, we have assumed that each qubit undergoes either a bit-flip error or a phase-flip error (or both). This is not a realistic model for the errors, and we must understand how to implement quantum error correction under more general conditions.

Consider a quantum memory, the system $S$ with Hilbert space $\mathcal{H}_S$, which is subjected to noise, described by a TPCP map $\mathcal{N}$. As we discussed in depth in Chapter 3, $\mathcal{N}$ has a dilation, an isometric (inner-product preserving) map $\boldsymbol{U}$ taking $S$ to $SE$, where $E$ is the system's environment. If $\{\boldsymbol{E}_a\}$ is a set of operators which span the space of linear operators taking $S$ to $S$, then $\boldsymbol{U}$ can be expanded as

$$
\boldsymbol{U}_{S\to SE} : |\psi\rangle_S \mapsto \sum_a \boldsymbol{E}_a|\psi\rangle_S \otimes |\varphi_a\rangle_E.
$$ {#eq-7.9}

Here the vectors $\{|\varphi_a\rangle\}$ are *not* assumed to be normalized or mutually orthogonal; hence eq.(7.9) entails no loss of generality. In the case where all the $|\varphi_a\rangle$ are parallel, it describes a *unitary error*, in which a pure state of $S$ remains pure but is subjected to an unknown rotation in Hilbert space. In the case where $\{|\varphi_a\rangle\}$ includes mutually orthogonal vectors, it describes strong decoherence, in which an initially pure state of $S$ becomes mixed due to its entanglement with the environment.

Now we would like to reverse the damage caused by the error by applying a recovery operation $\mathcal{R}$, which is also a TPCP map, and therefore has an isometric dilation $\boldsymbol{V}$ taking $S$ to $SA$, where $A$ is an *ancilla*, an extra system under our control. Unfortunately, successful recovery will not be possible for arbitrary errors of the form eq.(7.9), if we do not know what error occurred, and the environment $E$ is beyond our control. At best we will only be able to reverse errors of a restricted type.

Let's consider a restricted class of noise operations, where the error lies within the

<!-- Page 11 -->
space spanned by a subset $\mathcal{E} \subset \{\boldsymbol{E}_a\}$. We say that the errors in $\mathcal{E}$ are *correctable* if we can recover from any error of the restricted form

$$
\tilde{\boldsymbol{U}}_{S\to SE} : |\psi\rangle_S \mapsto \sum_{\boldsymbol{E}_a \in \mathcal{E}} \boldsymbol{E}_a|\psi\rangle_S \otimes |\varphi_a\rangle_E.
$$ {#eq-7.10}

Our choice of $\mathcal{E}$ will be motivated by the physical properties of the noise. For example, if $S$ is an $n$-qubit system, and the noise is weak and acts nearly independently on the qubits, then we may anticipate that any $\boldsymbol{E}_a$ acting nontrivially on a large portion of the $n$ qubits occurs in the sum eq.(7.9) with only a very small amplitude $\|\varphi_a\| \ll 1$. In that event we might choose $\mathcal{E}$ to contain only operators of low weight (those acting nontrivially on a relatively small number of qubits). If we can correct all the errors in $\mathcal{E}$, then we will be able to nearly reverse the effect of $\boldsymbol{U}$, with the small residual error arising only from $\boldsymbol{E}_a \notin \mathcal{E}$ in eq.(7.9).

But even if we restrict the errors to the correctable set $\mathcal{E}$, we will not be able to protect arbitrary pure states in $\mathcal{H}_S$ from error. At best we will be able to protect only the states lying within a *code subspace* $\mathcal{H}_{\text{code}} \subset \mathcal{H}_S$. If $\mathcal{H}_{\text{code}}$ and $\mathcal{E}$ are appropriately chosen, then we can construct a recovery isometry $\boldsymbol{V}$ (a dilation of the TPCP map $\mathcal{R}$) such that

$$
\boldsymbol{V}_{S\to SA} : \boldsymbol{E}_a|\psi\rangle_S \mapsto |\psi\rangle_S \otimes |\chi_a\rangle_A
$$ {#eq-7.11}

for all $|\psi\rangle_S \in \mathcal{H}_{\text{code}}$ and $\boldsymbol{E}_a \in \mathcal{E}$, and for some set of vectors $\{|\chi_a\rangle_A \in \mathcal{H}_A\}$. It then follows that

$$
|\psi\rangle_S \stackrel{\tilde{\boldsymbol{U}}}{\mapsto} \sum_{\boldsymbol{E}_a\in\mathcal{E}} \boldsymbol{E}_a|\psi\rangle_S \otimes |\varphi_a\rangle_E \stackrel{\boldsymbol{V}}{\mapsto} |\psi\rangle_S \otimes \left( \sum_a |\varphi_a\rangle_E \otimes |\chi_a\rangle_A \right).
$$ {#eq-7.12}

In general, the noise map $\tilde{\boldsymbol{U}}$ generates entanglement between $S$ and $E$. We cannot undo that $E$ became entangled with something, because we do not control $E$. But what we can do, under suitable conditions, is transform entanglement of $E$ with $S$ into entanglement of $E$ with $A$ while purifying $S$ as in eq.(7.12).

For the recovery operation to exist, the code space $\mathcal{H}_{\text{code}}$ and correctable error set $\mathcal{E}$ must obey a necessary condition which just follows from the requirement that $\boldsymbol{V}$ is isometric. For any normalized pure state $|\psi\rangle_S$ in the code space, eq.(7.11) implies that

$$
\langle\psi|\boldsymbol{E}_b^\dagger \boldsymbol{E}_a|\psi\rangle = \langle\psi|\psi\rangle \langle\chi_b|\chi_a\rangle = \langle\chi_b|\chi_a\rangle := C_{ba};
$$ {#eq-7.13}

here $C_{ba}$ is a nonnegative Hermitian matrix, not depending on $|\psi\rangle$. It is sometimes convenient to write this condition differently. If $\{|\bar{i}\rangle\}$ is an orthonormal basis for $\mathcal{H}_{\text{code}}$, and eq.(7.13) holds for any state $|\psi\rangle = \sum_i \psi_i |\bar{i}\rangle$ in the code space, then

$$
\sum_{i,j} \psi_j^* \psi_i \langle\bar{j}|\boldsymbol{E}_b^\dagger \boldsymbol{E}_a|\bar{i}\rangle = C_{ba} \sum_i \psi_i^* \psi_i,
$$ {#eq-7.14}

and hence

$$
\langle\bar{j}|\boldsymbol{E}_b^\dagger \boldsymbol{E}_a|\bar{i}\rangle = \delta_{ji} C_{ba}.
$$ {#eq-7.15}

Expressed in terms of

$$
\boldsymbol{\Pi} = \sum_i |\bar{i}\rangle\langle\bar{i}|,
$$ {#eq-7.16}

<!-- Page 12 -->
the orthogonal projector onto the code space, eq.(7.15) becomes

$$
\boldsymbol{\Pi}\boldsymbol{E}_b^\dagger \boldsymbol{E}_a\boldsymbol{\Pi} = C_{ba}\boldsymbol{\Pi}.
$$ {#eq-7.17}

Eq.(7.17), which must hold for each pair of error operators $\boldsymbol{E}_a$ and $\boldsymbol{E}_b$ in the correctable set $\mathcal{E}$, is called the *quantum error correction condition* or *Knill-Laflamme condition*.

In fact, eq.(7.17) is a sufficient as well as necessary condition for the existence of a recovery operator protecting the code space against the errors in $\mathcal{E}$. Since $C_{ba}$ is Hermitian and nonnegative, we can choose a basis $\tilde{\mathcal{E}} = \{\tilde{\boldsymbol{E}}_a\}$ in which it is diagonal: $\tilde{C}_{ba} = c_a \delta_{ba}$ and $c_a \ge 0$; hence

$$
\tilde{\boldsymbol{U}}_{S\to SE} : |\psi\rangle_S \mapsto \sum_{\tilde{\boldsymbol{E}}_a \in \tilde{\mathcal{E}}} \tilde{\boldsymbol{E}}_a |\psi\rangle_S \otimes |\tilde{\varphi}_a\rangle_E,
$$ {#eq-7.18}

where

$$
\boldsymbol{\Pi}\tilde{\boldsymbol{E}_b}^\dagger \tilde{\boldsymbol{E}}_a\boldsymbol{\Pi} = c_a \delta_{ba}\boldsymbol{\Pi}.
$$ {#eq-7.19}

Since we also have the freedom to rescale the error operators (while performing a compensating rescaling of the vectors $\{|\tilde{\varphi}_a\rangle_E\}$), we may assume that each $c_a$ is either 0 or 1.

Let's first consider the case of a *nondegenerate code* in which $c_a > 0$ for each $a$, and hence (after a suitable rescaling, if necessary)

$$
\boldsymbol{\Pi}\tilde{\boldsymbol{E}_b}^\dagger \tilde{\boldsymbol{E}}_a\boldsymbol{\Pi} = \delta_{ba}\boldsymbol{\Pi}.
$$ {#eq-7.20}

For a nondegenerate code, all of the "error subspaces" $\tilde{\boldsymbol{E}}_a\mathcal{H}_{\text{code}}$ are mutually orthogonal and hence perfectly distinguishable. If a correctable error $\tilde{\boldsymbol{E}}_a \in \mathcal{E}$ acts on the code space, $\tilde{\boldsymbol{E}}_a$ can be unambiguously identified by performing a suitable orthogonal measurement. Furthermore, the error $\tilde{\boldsymbol{E}}_a$ isometrically maps the code space to the corresponding error space. Therefore, once $\tilde{\boldsymbol{E}}_a$ is identified, we can apply a unitary map taking the error space back to the code space, correcting the error.

To be more explicit, the orthogonal projectors

$$
\{\boldsymbol{\Pi}_a = \tilde{\boldsymbol{E}}_a \boldsymbol{\Pi} \tilde{\boldsymbol{E}}_a^\dagger\}
$$ {#eq-7.21}

satisfying

$$
\boldsymbol{\Pi}_a \boldsymbol{\Pi}_b = \delta_{ab}\boldsymbol{\Pi}_a
$$ {#eq-7.22}

project onto the error subspaces. These projectors may not provide a complete partition of $\mathcal{H}_S$, but we can add one additional projector, onto the orthogonal complement of $\oplus_a \tilde{\boldsymbol{E}}_a\mathcal{H}_{\text{code}}$, to define an orthogonal measurement. The measurement outcome $\boldsymbol{\Pi}_a$ provides an *error syndrome* pointing to the error space $\tilde{\boldsymbol{E}}_a\mathcal{H}_{\text{code}}$, where this outcome occurs with probability $\text{prob}(a) = \langle\tilde{\chi}_a|\tilde{\chi}_a\rangle$ if the noise map is given by eq.(7.18) and the error operators obey eq.(7.20); once the outcome $a$ is known, a unitary transformation $\boldsymbol{U}_a$ applied to $\mathcal{H}_S$ corrects the error. The transformation $\boldsymbol{U}_a$ is chosen so that it acts as $\boldsymbol{\Pi}\tilde{\boldsymbol{E}}_a^\dagger$ on the subspace $\tilde{\boldsymbol{E}}_a\mathcal{H}_{\text{code}}$, while its action on the complement of $\tilde{\boldsymbol{E}}_a\mathcal{H}_{\text{code}}$ may be chosen arbitrarily.

This argument shows that recovery from error is possible if eq.(7.17) is satisfied and the code is nondegenerate. But what if the code is degenerate — that is, what if $\tilde{\boldsymbol{E}}_a\boldsymbol{\Pi} = 0$ for some of the error operators? This happens if our basis of correctable errors is overcomplete, so that there are linear combinations of elements of $\mathcal{E}$ which annihilate

<!-- Page 13 -->
the code space. In that case, we may simply eliminate these redundant error operators from our set of correctable errors, replacing our set $\mathcal{E}$ of correctable errors by a smaller set $\tilde{\mathcal{E}} \subset \mathcal{E}$.

We have already encountered an example of a degenerate code — the 9-qubit code, in which phase errors acting on the same cluster of three qubits affect the code subspace in the same way (e.g., $\boldsymbol{Z}_1|\psi\rangle = \boldsymbol{Z}_2|\psi\rangle$, where $|\psi\rangle \in \mathcal{H}_{\text{code}}$). This means that no syndrome measurement can distinguish whether error $\boldsymbol{Z}_1$ or $\boldsymbol{Z}_2$ occurred, and correspondingly, there is an error $\boldsymbol{Z}_1 - \boldsymbol{Z}_2$ which annihilates the code space. As this "error" occurs with zero amplitude, we can eliminate it from the sum over $\tilde{\boldsymbol{E}}_a$ in eq.(7.18) without changing anything. Once all such zero-amplitude errors have been eliminated, we can measure the error syndrome and correct the error just as in the nondegenerate case. Therefore, the error correction condition eq.(7.17) is sufficient as well as necessary for the existence of a recovery map that reverses the error, whether or not the code is degenerate.

We have described this recovery procedure as a two step process, in which the error syndrome is measured in the first step, and an error-correcting unitary operator conditioned on the outcome of the syndrome measurement is performed in the second step. But in order to recover, it is not necessary to perform a measurement that amplifies the error syndrome to the classical world. Instead, we may sum coherently over the possible syndromes, obtaining an isometric recovery map $\boldsymbol{V}$. Acting on the span of $\{\tilde{\boldsymbol{E}}_a\mathcal{H}_{\text{code}}, \tilde{\boldsymbol{E}}_a \in \tilde{\mathcal{E}}\}$, this isometric map is

$$
\boldsymbol{V} : |\varphi\rangle_S \mapsto \sum_b \boldsymbol{\Pi} \tilde{\boldsymbol{E}}_b^\dagger |\varphi\rangle_S \otimes |b\rangle_A
$$ {#eq-7.23}

where $\{|b\rangle_A\}$ is an orthonormal basis for the ancilla (as follows from eq.(7.13) if the error operators obey eq.(7.20)). This recovery map can correct any error of the form eq.(7.18) acting on the code space:

$$
\begin{aligned}
\boldsymbol{V}\tilde{\boldsymbol{U}} : |\psi\rangle_S &\mapsto \sum_{a,b} \boldsymbol{\Pi} \tilde{\boldsymbol{E}}_b^\dagger \tilde{\boldsymbol{E}}_a \boldsymbol{\Pi} |\psi\rangle \otimes |\tilde{\varphi}_a\rangle_E \otimes |b\rangle_A \\
&= |\psi\rangle_S \otimes \left( \sum_a |\tilde{\varphi}_a\rangle_E \otimes |a\rangle_A \right).
\end{aligned}
$$ {#eq-7.24}

Eq.(7.20) ensures that $\boldsymbol{V}$ is an isometry acting on $\text{span}\{\boldsymbol{E}_a\mathcal{H}_{\text{code}}\}$, and it can be extended to an isometry acting on all of $\mathcal{H}_S$. If the ancilla is initialized in a standard pure state $|0\rangle_A$, the isometry $\boldsymbol{V}$ can be realized as a unitary transformation mapping $SA$ to itself. A suitably constructed quantum circuit can execute this recovery transformation; no measurement of the syndrome is required.

– Figure –  
Show $|\psi\rangle$ subjected to noise, and then decoded as ancilla is discarded.

It should be emphasized that the construction of the recovery map $\boldsymbol{V}$ depends only on the code space $\mathcal{H}_{\text{code}}$ and on the correctable error set $\mathcal{E}$. Recovery succeeds for any choice of the vectors $\{|\varphi_a\rangle_E\}$ in eq.(7.10); we don't need to know anything further about the error, only that it lies within the span of the error operators in $\mathcal{E}$. In particular, the

<!-- Page 14 -->
code can be protected against both unitary control errors and decoherence errors, as long as errors outside $\mathcal{E}$ occur with negligible amplitude.

Although an orthogonal measurement of the syndrome is not a necessary part of the recovery procedure, the ancilla is absolutely essential. In effect, the noise "heats up" the quantum memory $S$, and the recovery operation cools it back down. The ancilla $A$ is the cold reservoir where this excess heat is deposited.

If we wish to protect the quantum information stored in a quantum memory for a long time, while the memory is continuously subjected to noise, then we should perform the error recovery map many times in succession. Each recovery step makes use of a fresh ancilla, which may be discarded after use. But if only a limited supply of ancilla qubits are available, then the ancilla should be erased before it is recycled for further error recovery steps; that is, the ancilla must be mapped back to the standard initial state $|0\rangle_A$, in effect cooling it to a very low temperature. This erasure is a dissipative process; work is needed to pump the heat from the ancilla back to the environment. Thus, unless we have an unlimited supply of fresh ancilla qubits, error recovery incurs an unavoidable thermodynamic cost. We cannot perform quantum (or classical) error correction for free.
