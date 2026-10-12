# 2.7 Summary [📄 chap2.pdf](/assets/pdf/preskill/chap2.pdf#page=41)

**Axioms.** The arena of quantum mechanics is a Hilbert space $\mathcal{H}$. The fundamental assumptions are:

(1) A state is a ray in $\mathcal{H}$.
(2) An observable is a self-adjoint operator on $\mathcal{H}$.
(3) A measurement is an orthogonal projection.
(4) Time evolution is unitary.
(5) A composite system $AB$ is described by the tensor product $\mathcal{H}_A \otimes \mathcal{H}_B$.

**Density operator.** But if we confine our attention to only a portion of a larger quantum system, assumptions (1)-(4) need not be satisfied. In particular, a quantum state is described not by a ray, but by a density operator $\boldsymbol{\rho}$, a nonnegative operator with unit trace. The density operator is pure (and the state can be described by a ray) if $\boldsymbol{\rho}^2 = \boldsymbol{\rho}$; otherwise, the state is mixed. An observable $\boldsymbol{M}$ has expectation value $\mathrm{tr}(\boldsymbol{M}\boldsymbol{\rho})$ in this state.

**Qubit.** A quantum system with a two-dimensional Hilbert space is called a qubit. The general density matrix of a qubit is
$$
\boldsymbol{\rho}(\vec{P}) = \frac{1}{2}(\boldsymbol{I} + \vec{P} \cdot \vec{\boldsymbol{\sigma}}) \tag{2.162}
$$
where $\vec{P}$ is a three-component vector of length $|\vec{P}| \le 1$. Pure states have $|\vec{P}| = 1$.

**Schmidt decomposition.** For any pure state $|\psi\rangle_{AB}$ of a bipartite system, there are orthonormal bases $\{|i\rangle_A\}$ for $\mathcal{H}_A$ and $\{|i'\rangle_B\}$ for $\mathcal{H}_B$ such that
$$
|\psi\rangle_{AB} = \sum_i \sqrt{p_i} |i\rangle_A \otimes |i'\rangle_B; \tag{2.163}
$$
Eq.(2.163) is called the Schmidt decomposition of $|\psi\rangle_{AB}$. In a bipartite pure state, subsystems $A$ and $B$ separately are described by density operators $\boldsymbol{\rho}_A$ and $\boldsymbol{\rho}_B$; it follows from eq.(2.163) that $\boldsymbol{\rho}_A$ and $\boldsymbol{\rho}_B$ have the same nonvanishing eigenvalues (the $p_i$'s). The number of nonvanishing eigenvalues is called the Schmidt number of $|\psi\rangle_{AB}$. A bipartite pure state is said to be entangled if its Schmidt number is greater than one.

**Ensembles.** The density operators on a Hilbert space form a convex set, and the pure states are the extremal points of the set. A mixed state of a system $A$ can be prepared as an ensemble of pure states in many different ways, all of which are experimentally indistinguishable if we observe system $A$ alone. Given any mixed state $\boldsymbol{\rho}_A$ of system $A$, any preparation of $\boldsymbol{\rho}_A$ as an ensemble of pure states can be realized in principle by performing a measurement in another system $B$ with which $A$ is entangled. In fact given many such preparations of $\boldsymbol{\rho}_A$, there is a single entangled state of $A$ and $B$ such that any one of these preparations can be realized by measuring a suitable observable in $B$ (the HJW theorem). By measuring in system $B$ and reporting the measurement outcome to system $A$, we can extract from the mixture a pure state chosen from one of the ensembles.

**Fidelity.** The fidelity $F(\boldsymbol{\rho}, \boldsymbol{\sigma}) = \|\boldsymbol{\sigma}^{1/2} \boldsymbol{\rho}^{1/2}\|_1^2$, quantifies the distinguishability of two density operators -- it is the maximum overlap achieved by their purifications (Uhlmann's theorem). The fidelity $F(\boldsymbol{\rho}, \boldsymbol{\sigma})$ is close to one if and only if the $L^1$ distance $\|\boldsymbol{\rho} - \boldsymbol{\sigma}\|_1$ is small.

Further important ideas are developed in the Exercises.
