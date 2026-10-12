# 2.4 Schmidt decomposition [📄 chap2.pdf](/assets/pdf/preskill/chap2.pdf#page=23)

A bipartite pure state can be expressed in a standard form (the Schmidt decomposition) that is often very useful.

To arrive at this form, note that an arbitrary vector in $\mathcal{H}_A \otimes \mathcal{H}_B$ can be expanded as
$$
|\psi\rangle_{AB} = \sum_{i,\mu} \psi_{i\mu} |i\rangle_A \otimes |\mu\rangle_B \equiv \sum_i |i\rangle_A \otimes |\tilde{i}\rangle_B. \tag{2.79}
$$
Here $\{|i\rangle_A\}$ and $\{|\mu\rangle_B\}$ are orthonormal basis for $\mathcal{H}_A$ and $\mathcal{H}_B$ respectively, but to obtain the second equality in eq.(2.79) we have defined
$$
|\tilde{i}\rangle_B \equiv \sum_\mu \psi_{i\mu} |\mu\rangle_B. \tag{2.80}
$$
Note that the $|\tilde{i}\rangle_B$'s need not be mutually orthogonal or normalized.

Now let's suppose that the $\{|i\rangle_A\}$ basis is chosen to be the basis in which $\boldsymbol{\rho}_A$ is diagonal,
$$
\boldsymbol{\rho}_A = \sum_i p_i |i\rangle\langle i|. \tag{2.81}
$$
We can also compute $\boldsymbol{\rho}_A$ by performing a partial trace,
$$
\begin{aligned}
\boldsymbol{\rho}_A &= \mathrm{tr}_B(|\psi\rangle\langle\psi|) \\
&= \mathrm{tr}_B\left(\sum_{i,j} |i\rangle\langle j| \otimes |\tilde{i}\rangle\langle\tilde{j}|\right) = \sum_{i,j} \langle\tilde{j}|\tilde{i}\rangle (|i\rangle\langle j|). \tag{2.82}
\end{aligned}
$$
We obtained the last equality in eq.(2.82) by noting that
$$
\mathrm{tr}_B\left(|\tilde{i}\rangle\langle\tilde{j}|\right) = \sum_k \langle k|\tilde{i}\rangle\langle\tilde{j}|k\rangle = \sum_k \langle\tilde{j}|k\rangle\langle k|\tilde{i}\rangle = \langle\tilde{j}|\tilde{i}\rangle, \tag{2.83}
$$
where $\{|k\rangle\}$ is a complete orthonormal basis for $\mathcal{H}_B$. By comparing eq.(2.81) and eq.(2.82), we see that
$$
{}_B\langle\tilde{j}|\tilde{i}\rangle_B = p_i \delta_{ij}. \tag{2.84}
$$
Hence, it turns out that the $\{|\tilde{i}\rangle_B\}$ are orthogonal after all. We obtain orthonormal vectors by rescaling,
$$
|i'\rangle_B = p_i^{-1/2} |\tilde{i}\rangle_B \tag{2.85}
$$
(we may assume $p_i \ne 0$, because we will need eq.(2.85) only for $i$ appearing in the sum eq.(2.81)), and therefore obtain the expansion
$$
|\psi\rangle_{AB} = \sum_i \sqrt{p_i} |i\rangle_A \otimes |i'\rangle_B, \tag{2.86}
$$
in terms of a particular orthonormal basis of $\mathcal{H}_A$ and $\mathcal{H}_B$.

Eq.(2.86) is the Schmidt decomposition of the bipartite pure state $|\psi\rangle_{AB}$. Any bipartite pure state can be expressed in this form, but the bases used depend on the pure state that is being expanded. In general, we can't simultaneously expand both $|\psi\rangle_{AB}$ and $|\phi\rangle_{AB} \in \mathcal{H}_A \otimes \mathcal{H}_B$ in the form eq.(2.86) using the same orthonormal bases for $\mathcal{H}_A$ and $\mathcal{H}_B$.

It is instructive to compare the Schmidt decomposition of the bipartite pure state $|\psi\rangle_{AB}$ with its expansion in a generic orthonormal basis
$$
|\psi\rangle_{AB} = \sum_{a,\mu} \psi_{a\mu} |a\rangle_A \otimes |\mu\rangle_B. \tag{2.87}
$$
The orthonormal bases $\{|a\rangle_A\}$ and $\{|\mu\rangle_B\}$ are related to the Schmidt bases $\{|i\rangle_A\}$ and $\{|i'\rangle_B\}$ by unitary transformations $\boldsymbol{U}_A$ and $\boldsymbol{U}_B$, hence
$$
|i\rangle_A = \sum_a |a\rangle_A (\boldsymbol{U}_A)_{ai}, \quad |i'\rangle_B = \sum_\mu |\mu\rangle_B (\boldsymbol{U}_B)_{\mu i'}. \tag{2.88}
$$
By equating the expressions for $|\psi\rangle_{AB}$ in eq.(2.86) and eq.(2.87), we find
$$
\psi_{a\mu} = \sum_i (\boldsymbol{U}_A)_{ai} \sqrt{p_i} (\boldsymbol{U}_B^T)_{i\mu}. \tag{2.89}
$$
We see that by applying unitary transformations on the left and right, any matrix $\psi$ can be transformed to a matrix which is diagonal and nonnegative. (The "diagonal" matrix will be rectangular rather than square if the Hilbert spaces $\mathcal{H}_A$ and $\mathcal{H}_B$ have different dimensions.) Eq.(2.89) is said to be the singular value decomposition of $\psi$, and the weights $\{\sqrt{p_i}\}$ in the Schmidt decomposition are $\psi$'s singular values.

Using eq.(2.86), we can also evaluate the partial trace over $\mathcal{H}_A$ to obtain
$$
\boldsymbol{\rho}_B = \mathrm{tr}_A(|\psi\rangle\langle\psi|) = \sum_i p_i |i'\rangle\langle i'|. \tag{2.90}
$$
We see that $\boldsymbol{\rho}_A$ and $\boldsymbol{\rho}_B$ have the same nonzero eigenvalues. If $\mathcal{H}_A$ and $\mathcal{H}_B$ do not have the same dimension, the number of zero eigenvalues of $\boldsymbol{\rho}_A$ and $\boldsymbol{\rho}_B$ will differ.

If $\boldsymbol{\rho}_A$ (and hence $\boldsymbol{\rho}_B$) have no degenerate eigenvalues other than zero, then the Schmidt decomposition of $|\psi\rangle_{AB}$ is essentially uniquely determined by $\boldsymbol{\rho}_A$ and $\boldsymbol{\rho}_B$. We can diagonalize $\boldsymbol{\rho}_A$ and $\boldsymbol{\rho}_B$ to find the $|i\rangle_A$'s and $|i'\rangle_B$'s, and then we pair up the eigenstates of $\boldsymbol{\rho}_A$ and $\boldsymbol{\rho}_B$ with the same eigenvalue to obtain eq.(2.86). We have chosen the phases of our basis states so that no phases appear in the coefficients in the sum; the only remaining freedom is to redefine $|i\rangle_A$ and $|i'\rangle_B$ by multiplying by opposite phases (which leaves the expression eq.(2.86) unchanged).

But if $\boldsymbol{\rho}_A$ has degenerate nonzero eigenvalues, then we need more information than that provided by $\boldsymbol{\rho}_A$ and $\boldsymbol{\rho}_B$ to determine the Schmidt decomposition; we need to know which $|i'\rangle_B$ gets paired with each $|i\rangle_A$. For example, if both $\mathcal{H}_A$ and $\mathcal{H}_B$ are $d$-dimensional and $U_{ij}$ is any $d \times d$ unitary matrix, then
$$
|\psi\rangle_{AB} = \frac{1}{\sqrt{d}} \sum_{i,j=1}^d |i\rangle_A U_{ij} \otimes |j'\rangle_B, \tag{2.91}
$$
will yield $\boldsymbol{\rho}_A = \boldsymbol{\rho}_B = \frac{1}{d}\boldsymbol{I}$ when we take partial traces. Furthermore, we are free to apply simultaneous unitary transformations in $\mathcal{H}_A$ and $\mathcal{H}_B$; writing
$$
|i\rangle_A = \sum_a |a\rangle_A V_{ai}, \quad |i'\rangle_B = \sum_b |b'\rangle_B V_{bi}^*, \tag{2.92}
$$
where $V$ is a unitary matrix, we have
$$
\begin{aligned}
|\psi\rangle_{AB} = \frac{1}{\sqrt{d}} \sum_i |i\rangle_A \otimes |i'\rangle_B &= \frac{1}{\sqrt{d}} \sum_{i,a,b} |a\rangle_A V_{ai} \otimes |b'\rangle_B V_{ib}^\dagger \\
&= \frac{1}{\sqrt{d}} \sum_a |a\rangle_A \otimes |a'\rangle_B. \tag{2.93}
\end{aligned}
$$
This simultaneous rotation preserves the state $|\psi\rangle_{AB}$, illustrating that there is an ambiguity in the basis used when we express $|\psi\rangle_{AB}$ in the Schmidt form.

## 2.4.1 Entanglement [📄 chap2.pdf](/assets/pdf/preskill/chap2.pdf#page=25)

With any bipartite pure state $|\psi\rangle_{AB}$ we may associate a positive integer, the Schmidt number, which is the number of nonzero eigenvalues in $\boldsymbol{\rho}_A$ (or $\boldsymbol{\rho}_B$) and hence the number of terms in the Schmidt decomposition of $|\psi\rangle_{AB}$. In terms of this quantity, we can define what it means for a bipartite pure state to be entangled: $|\psi\rangle_{AB}$ is entangled (or nonseparable) if its Schmidt number is greater than one; otherwise, it is separable (or unentangled). Thus, a separable bipartite pure state is a direct product of pure states in $\mathcal{H}_A$ and $\mathcal{H}_B$,
$$
|\psi\rangle_{AB} = |\phi\rangle_A \otimes |\chi\rangle_B; \tag{2.94}
$$
then the reduced density matrices $\boldsymbol{\rho}_A = |\phi\rangle\langle\phi|$ and $\boldsymbol{\rho}_B = |\chi\rangle\langle\chi|$ are pure. Any state that cannot be expressed as such a direct product is entangled; then $\boldsymbol{\rho}_A$ and $\boldsymbol{\rho}_B$ are mixed states.

When $|\psi\rangle_{AB}$ is entangled we say that $A$ and $B$ have quantum correlations. It is not strictly correct to say that subsystems $A$ and $B$ are uncorrelated if $|\psi\rangle_{AB}$ is separable; after all, the two spins in the separable state
$$
|\!\uparrow\rangle_A |\!\uparrow\rangle_B, \tag{2.95}
$$
are surely correlated -- they are both pointing in the same direction. But the correlations between $A$ and $B$ in an entangled state have a different character than those in a separable state. One crucial difference is that entanglement cannot be created locally. The only way to entangle $A$ and $B$ is for the two subsystems to directly interact with one another.

We can prepare the state eq.(2.95) without allowing spins $A$ and $B$ to ever come into contact with one another. We need only send a (classical!) message to two preparers (Alice and Bob) telling both of them to prepare a spin pointing along the $z$-axis. But the only way to turn the state eq.(2.95) into an entangled state like
$$
\frac{1}{\sqrt{2}} (|\!\uparrow\rangle_A |\!\uparrow\rangle_B + |\!\downarrow\rangle_A |\!\downarrow\rangle_B), \tag{2.96}
$$
is to apply a collective unitary transformation to the state. Local unitary transformations of the form $\boldsymbol{U}_A \otimes \boldsymbol{U}_B$, and local measurements performed by Alice or Bob, cannot increase the Schmidt number of the two-qubit state, no matter how much Alice and Bob discuss what they do. To entangle two qubits, we must bring them together and allow them to interact.

As we will discuss in Chapters 4 and 10, it is also possible to make the distinction between entangled and separable bipartite mixed states. We will also discuss various ways in which local operations can modify the form of entanglement, and some ways that entanglement can be put to use.
