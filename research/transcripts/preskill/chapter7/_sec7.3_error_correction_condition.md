# Section 7.3: More about the error correction condition [PDF Pages 14-18]

<!-- ============================================================ -->
<!-- Source: chap7.pdf, Physical Pages: 14-18                      -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 14 -->
## 7.3 More about the error correction condition

The condition eq.(7.17) is the foundation of the theory of quantum error correction. In this section we will explore further the interpretation and implications of this error correction condition; considering it from complementary vantage points deepens our appreciation of how and why quantum error correction works.

### 7.3.1 Distinguishability of orthogonal code states

We can protect encoded quantum information against noise only if the noise preserves the perfect distinguishability of orthogonal vectors in the code space. Thus if $\boldsymbol{E}_a, \boldsymbol{E}_b$ are any two errors in the correctable set $\mathcal{E}$, and $|\varphi\rangle, |\psi\rangle$ are any two orthogonal pure states in $\mathcal{H}_{\text{code}}$, then $\boldsymbol{E}_a|\varphi\rangle$ and $\boldsymbol{E}_b|\psi\rangle$ must also be orthogonal. Otherwise, the recovery isometry cannot possibly map $\boldsymbol{E}_a|\varphi\rangle$ and $\boldsymbol{E}_b|\psi\rangle$ to the orthogonal states $|\varphi\rangle$ and $|\psi\rangle$.

To be concrete, suppose the code space is two-dimensional and let $\{|\bar{0}\rangle, |\bar{1}\rangle\}$ denote an orthonormal basis for $\mathcal{H}_{\text{code}}$. For distinguishability of the basis vectors to be preserved by the correctable errors, we require that $\boldsymbol{E}_a|\bar{0}\rangle \perp \boldsymbol{E}_b|\bar{1}\rangle$ for $\boldsymbol{E}_a, \boldsymbol{E}_b \in \mathcal{E}$, or

$$
\langle\bar{1}|\boldsymbol{E}_b^\dagger \boldsymbol{E}_a|\bar{0}\rangle = 0 = \langle\bar{0}|\boldsymbol{E}_b^\dagger \boldsymbol{E}_a|\bar{1}\rangle.
$$ {#eq-7.25}

Distinguishability must also be preserved for the conjugate basis states $\{\frac{1}{\sqrt{2}}(|\bar{0}\rangle \pm |\bar{1}\rangle)\}$; therefore

$$
0 = (\langle\bar{0}| + \langle\bar{1}|) \boldsymbol{E}_b^\dagger \boldsymbol{E}_a (|\bar{0}\rangle - |\bar{1}\rangle) = \langle\bar{0}|\boldsymbol{E}_b^\dagger \boldsymbol{E}_a|\bar{0}\rangle - \langle\bar{1}|\boldsymbol{E}_b^\dagger \boldsymbol{E}_a|\bar{1}\rangle.
$$ {#eq-7.26}

Putting together eq.(7.25) and (7.26) we see that the error correction condition

$$
\langle\bar{j}|\boldsymbol{E}_b^\dagger \boldsymbol{E}_a|\bar{i}\rangle = \delta_{ji} C_{ba}
$$ {#eq-7.27}

is satisfied for $\boldsymbol{E}_a, \boldsymbol{E}_b \in \mathcal{E}$; thus survival of perfect distinguishability for both the basis states $|\bar{0}\rangle, |\bar{1}\rangle$ and the conjugate basis states suffices to ensure that quantum information in the code space can be perfectly protected against the noise.

<!-- Page 15 -->
The noise might deform the code states $|\bar{0}\rangle$ and $|\bar{1}\rangle$ substantially, but that won't necessarily mean that encoded quantum information is irrevocably lost. As long as orthogonal code vectors are mapped to distinguishable (mixed) states of the system, recovery from error is possible.

### 7.3.2 Leakage of information to the environment

In typical laboratory settings, information stored in a quantum memory is fragile because the memory cannot be perfectly isolated from the outside world, and leakage of information to the environment induces irreversible decoherence. A quantum error-correcting code can prevent this leakage, protecting the encoded state.

If the system $S$ is subjected to an error of the form eq.(7.10), then if the initial state $|\psi\rangle_S$ is in the code space $\mathcal{H}_{\text{code}}$ we find by tracing out $S$ that the state of the environment becomes

$$
\begin{aligned}
\boldsymbol{\rho}_E &= \text{tr}_S\left(\sum_{\boldsymbol{E}_a, \boldsymbol{E}_b \in \mathcal{E}} \boldsymbol{E}_a|\psi\rangle\langle\psi|\boldsymbol{E}_b^\dagger \otimes |\varphi_a\rangle\langle\varphi_b|\right) \\
&= \sum_{\boldsymbol{E}_a, \boldsymbol{E}_b \in \mathcal{E}} \langle\psi|\boldsymbol{E}_b^\dagger \boldsymbol{E}_a|\psi\rangle |\varphi_a\rangle\langle\varphi_b| = \sum_{a,b} C_{ba}|\varphi_a\rangle\langle\varphi_b|,
\end{aligned}
$$ {#eq-7.28}

where in the last equality we have used the error correction condition eq.(7.13). When the error correction condition is satisfied, then, the state of the environment is independent of the encoded quantum state. The converse is also true — if $\boldsymbol{\rho}_E$ does not depend on the code state $|\psi\rangle$, then the error correction conditions are satisfied, and the noise is correctable.

### 7.3.3 Decoupling a reference system

We can recast the error correction condition in another useful form by applying the relative state method described in Chapter 3. Let $\{|\bar{i}\rangle_S\}$ denote an orthonormal basis for the code space $\mathcal{H}_{\text{code}} \subset \mathcal{H}_S$. We introduce a reference system $R$, where the dimension $d_R$ of $\mathcal{H}_R$ is the same as the dimension of $\mathcal{H}_{\text{code}}$, and consider the state

$$
|\Phi\rangle_{RS} = \frac{1}{\sqrt{d_R}} \sum_i |i\rangle_R \otimes |\bar{i}\rangle_S,
$$ {#eq-7.29}

in which $R$ is maximally entangled with the code space.

Under the noise isometry $\tilde{\boldsymbol{U}}$ in eq.(7.10), this state is mapped to

$$
|\Phi'\rangle_{RSE} = \frac{1}{\sqrt{d_R}} \sum_i \sum_{\boldsymbol{E}_a \in \mathcal{E}} |i\rangle_R \otimes \boldsymbol{E}_a|\bar{i}\rangle_S \otimes |\varphi_a\rangle_E.
$$ {#eq-7.30}

A successful recovery isometry $\boldsymbol{V}_{S\to SA}$ maps this state according to

$$
|\Phi'\rangle_{RSE} \stackrel{\boldsymbol{V}}{\mapsto} |\Phi\rangle_{RS} \otimes |\chi\rangle_{EA}
$$ {#eq-7.31}

restoring the maximal entanglement of $R$ and the code space.

The error correction condition eq.(7.15) provides a characterization of the marginal

<!-- Page 16 -->
state of $RE$ after the noise acts. Tracing out the system $S$ yields

$$
\begin{aligned}
\boldsymbol{\rho}_{RE} &= \text{tr}_S |\Phi'\rangle\langle\Phi'| = \frac{1}{d_R}\sum_{i,j}\sum_{\boldsymbol{E}_a, \boldsymbol{E}_b \in \mathcal{E}} \langle\bar{j}|\boldsymbol{E}_b^\dagger \boldsymbol{E}_a|\bar{i}\rangle \otimes |i\rangle\langle j| \otimes |\varphi_a\rangle\langle\varphi_b| \\
&= \frac{1}{d_R}\sum_{i,j,a,b} C_{ba}\delta_{ji} \otimes |i\rangle\langle j| \otimes |\varphi_a\rangle\langle\varphi_b| = \frac{1}{d_R}\boldsymbol{I}_R \otimes \boldsymbol{\rho}_E.
\end{aligned}
$$ {#eq-7.32}

We conclude that for error correction to be possible, the reference system must remain uncorrelated with the environment, in which case we say that the reference system *decouples* from the environment. This statement $\boldsymbol{\rho}_{RE} = \boldsymbol{\rho}_R \otimes \boldsymbol{\rho}_E$ is another way to formulate the requirement that no leakage of information to the environment is allowed.

The decoupling condition eq.(7.32) is equivalent to the Knill-Laflamme error correction eq.(7.17), and provides an alternative perspective on why this condition suffices to ensure that the noise is correctable. Note that the state $|\Phi'\rangle_{RSE}$ provides a purification of the maximally mixed state $\boldsymbol{\rho}_R$. If $R$ is uncorrelated with $E$, then $R$ must be maximally entangled with some subsystem of $S$. Therefore a recovery operator acting on $S$ exists which maps this subsystem back to the code space, restoring $|\Phi\rangle_{RS}$. (For a more explicit construction, see the discussion of erasure correction in §7.3.4, and see also Chapter 10.)

To prevent misunderstanding, we emphasize that in general the recovery map depends on the noise channel. So, for example, if recovery map $\mathcal{R}_1$ corrects noise channel $\mathcal{N}_1$ and recovery map $\mathcal{R}_2$ corrects noise channel $\mathcal{N}_2$, that's not enough to guarantee correctability if the channel could be either one of $\mathcal{N}_1$ or $\mathcal{N}_2$, and we don't know which. For example, if the noise channel is a unitary transformation acting on $S$, then no channel environment is needed and decoupling is trivially satisfied, even if we take the “code space” to be all of $S$. Indeed, if the noise is the unitary $U_1$ we can recover with $U_1^\dagger$, and if the noise is the unitary $U_2$ we can recover with $U_2^\dagger$. But that does not mean we can correct a channel in which both of $U_1$ and $U_2$ are possible errors. If, say, those two unitary errors occur with respective probabilities $p_1$ and $p_2$, then the dilation of the noise channel would associate distinct states of the environment with those two possible unitaries, and the decoupling condition could easily fail.

The decoupling condition is quite useful, because it provides a powerful approach to *approximate* quantum error correction. If $\boldsymbol{\rho}_{RE}$ is close to a product state, then a recovery map exists that nearly reverses the error. We'll make heavy use of that idea in Chapter 10.

### 7.3.4 Correcting erasure errors

When we say that a quantum system has been *erased*, we mean that the system has escaped beyond our reach and can no longer be accessed. Furthermore, we *know* that the system has been lost. Mathematically, we can describe erasure by the TPCP map

$$
\boldsymbol{\rho}_S \mapsto |e\rangle\langle e|;
$$ {#eq-7.33}

here $|e\rangle$, called the *erasure symbol*, is a vector orthogonal to the system's Hilbert space $\mathcal{H}_S$. The idea is that we can perform a two-outcome orthogonal measurement which detects whether erasure occurs — the outcome $|e\rangle\langle e|$ confirms erasure while the outcome $I - |e\rangle\langle e| = \boldsymbol{\Pi}_S$ (the projector onto $\mathcal{H}_S$), confirms that $S$ is still available. An isometric

<!-- Page 17 -->
dilation of this erasure map acts according to

$$
|\psi\rangle_S \mapsto |e\rangle \otimes |\psi\rangle_E;
$$ {#eq-7.34}

the system is replaced by the erasure symbol while its initial state is recorded in the environment.

Recovery from erasure is of particular interest. Of course, we can't possibly recover if $S$ is completely erased. But suppose instead that $S = BC$ has a decomposition into subsystems, $\mathcal{H}_S = \mathcal{H}_B \otimes \mathcal{H}_C$, where $B$ is erased but $C$ is unharmed. We might anticipate that if the erased subsystem $B$ is not too large, and the code is suitably chosen, then we can recover the (redundantly encoded) protected quantum information using a recovery map that acts on $C$ alone. In effect, if we disregard the superfluous erasure symbol in eq.(7.34), erasure of $B$ maps the state of $S = BC$ to the corresponding state of $C$ and the environment $E$, according to

$$
|\psi\rangle_{BC} \mapsto |\psi\rangle_{EC},
$$ {#eq-7.35}

after which $E$ is traced out. Equivalently, erasure of $B$ is a noise channel mapping $S$ to $C$ defined by tracing out $B$, so that we may just as well regard $B$ as the environment for the dilation of this noise channel.

If a reference system $R$ is maximally entangled with $\mathcal{H}_{\text{code}}$ as in eq.(7.29), then the decoupling condition eq.(7.32) for quantum error correction becomes, for the case of erasure,

$$
\boldsymbol{\rho}_{RB} = \frac{1}{d_R}\boldsymbol{I}_R \otimes \boldsymbol{\rho}_B,
$$ {#eq-7.36}

where $B$ is the erased subsystem. We know on general grounds that this decoupling condition suffices to ensure that the erasure of $B$ is correctable. But it will be instructive to construct an explicit recovery map, from which we can extract some additional insights.

The condition eq.(7.36) has interesting implications regarding the structure of the code space. If $\boldsymbol{\rho}_B = \sum_b \lambda_b |b\rangle\langle b|$, where $\{|b\rangle\}$ is an orthonormal basis for $B$, then eq.(7.36) implies that the pure state of $RBC$ has the Schmidt decomposition (across the RB-C cut)

$$
|\Phi\rangle_{RBC} = \frac{1}{\sqrt{d_R}}\sum_{i,b}\sqrt{\lambda_b} |i\rangle_R \otimes |b\rangle_B \otimes |\psi_{bi}\rangle_C,
$$ {#eq-7.37}

where $\{|\psi_{bi}\rangle\}$ is an orthonormal basis for a subspace of $C$ which has dimension $d_B d_R$; here $d_B$ is the rank of $\boldsymbol{\rho}_B$ (its number of nonvanishing eigenvalues) and $d_R$ is the dimension of $R$. This subspace has a decomposition into subsystems $C_1 C_2$, where $C_1$ has dimension $d_B$ and $C_2$ has dimension $d_R$, such that

$$
|\psi_{bi}\rangle_C = \boldsymbol{U}_C(|b\rangle_{C_1} \otimes |i\rangle_{C_2})
$$ {#eq-7.38}

for some unitary transformation $\boldsymbol{U}_C$ acting on $C$, and therefore the orthonormal basis states for the code space can be expressed as

$$
\begin{aligned}
|\bar{i}\rangle_{BC} &= (\boldsymbol{I}_B \otimes \boldsymbol{U}_C)\left(\sum_b \sqrt{\lambda_b} |b\rangle_B \otimes |b\rangle_{C_1}\right) \otimes |i\rangle_{C_2} \\
&:= (\boldsymbol{I}_B \otimes \boldsymbol{U}_C)|\chi\rangle_{BC_1} \otimes |i\rangle_{C_2}.
\end{aligned}
$$ {#eq-7.39}

<!-- Page 18 -->
– Figure –  
Depict the encoding circuit for the code which protects against erasure of $B$, corresponding to eq.(7.39).

Eq.(7.39) clarifies how erasure correction can be achieved. The unitary transformation $\boldsymbol{I}_B \otimes \boldsymbol{U}_C^\dagger$, supported only on $C$, can be applied to the code space even if the subsystem $B$ is inaccessible. This transformation maps the code state $|\psi\rangle_S = \sum_i \psi_i |\bar{i}\rangle_S$ to the corresponding state $|\psi\rangle_{C_2} = \sum_i \psi_i |i\rangle_{C_2}$ of $C_2$, tensored with the fixed state $|\chi\rangle_{BC_1}$ of $BC_1$ which does not depend on $|\psi\rangle$. Thus if $B$ is erased, we can apply $\boldsymbol{U}_C^\dagger$, replace the state of $BC_1$ by $|\chi\rangle$, and then apply $\boldsymbol{U}_C$ to recover the undamaged code state.

This observation has a further implication. We say that an operator $\boldsymbol{M}$ acting on $S$ is a *logical operator* if it maps $\mathcal{H}_{\text{code}}$ to $\mathcal{H}_{\text{code}}$. Hence if $\boldsymbol{M}$ is logical it acts on the code's orthonormal basis states as

$$
\boldsymbol{M}_S : |\bar{i}\rangle_S \mapsto \sum_j |\bar{j}\rangle_S M_{ji}.
$$ {#eq-7.40}

From eq.(7.39) we see that if erasure of $B$ is correctable, then the logical operator $\boldsymbol{M}_S$ can be realized as an operator supported on $C$ alone:

$$
\boldsymbol{M}_S = (\boldsymbol{I}_B \otimes \boldsymbol{U}_C)(\boldsymbol{I}_{BC_1} \otimes \boldsymbol{M}_{C_2})(\boldsymbol{I}_B \otimes \boldsymbol{U}_C^\dagger),
$$ {#eq-7.41}

where

$$
\boldsymbol{M}_{C_2} : |i\rangle_{C_2} \mapsto \sum_j |j\rangle_{C_2} M_{ji}.
$$ {#eq-7.42}

We conclude that, if erasure of $B$ can be corrected, then we can apply an arbitrary logical operator to the code space without ever touching the subsystem $B$. This is sometimes called the *cleaning lemma*, because it's possible to “clean” the operator $\boldsymbol{M}$ on the correctable subsystem without altering its action on the code space.
