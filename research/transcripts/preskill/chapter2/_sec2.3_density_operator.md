# 2.3 The density operator [📄 chap2.pdf](/assets/pdf/preskill/chap2.pdf#page=16)

## 2.3.1 The bipartite quantum system [📄 chap2.pdf](/assets/pdf/preskill/chap2.pdf#page=16)

Having understood everything about a single qubit, we are ready to address systems with two qubits. Stepping up from one qubit to two is a bigger leap than you might expect. Much that is weird and wonderful about quantum mechanics can be appreciated by considering the properties of the quantum states of two qubits.

The axioms of §2.1 provide a perfectly acceptable general formulation of the quantum theory. Yet under many circumstances, we find that the axioms appear to be violated. The trouble is that our axioms are intended to characterize the quantum behavior of a closed system that does not interact with its surroundings. In practice, closed quantum systems do not exist; the observations we make are always limited to a small part of a much larger quantum system.

When we study open systems, that is, when we limit our attention to just part of a larger system, then (contrary to the axioms):

1. States are not rays.
2. Measurements are not orthogonal projections.
3. Evolution is not unitary.

To arrive at the laws obeyed by open quantum systems, we must recall our fifth axiom, which relates the description of a composite quantum system to the description of its component parts. As a first step toward understanding the quantum description of an open system, consider a two-qubit world in which we observe only one of the qubits. Qubit $A$ is here in the room with us, and we are free to observe or manipulate it any way we please. But qubit $B$ is locked in a vault where we can't get access to it. The full system $AB$ obeys the axioms of §2.1. But we would like to find a compact way to characterize the observations that can be made on qubit $A$ alone.

We'll use $\{|0\rangle_A, |1\rangle_A\}$ and $\{|0\rangle_B, |1\rangle_B\}$ to denote orthonormal bases for qubits $A$ and $B$ respectively. Consider a quantum state of the two-qubit world of the form
$$
|\psi\rangle_{AB} = a|0\rangle_A \otimes |0\rangle_B + b|1\rangle_A \otimes |1\rangle_B. \tag{2.51}
$$
In this state, qubits $A$ and $B$ are correlated. Suppose we measure qubit $A$ by projecting onto the $\{|0\rangle_A, |1\rangle_A\}$ basis. Then with probability $|a|^2$ we obtain the result $|0\rangle_A$, and the measurement prepares the state
$$
|0\rangle_A \otimes |0\rangle_B; \tag{2.52}
$$
with probability $|b|^2$, we obtain the result $|1\rangle_A$ and prepare the state
$$
|1\rangle_A \otimes |1\rangle_B. \tag{2.53}
$$
In either case, a definite state of qubit $B$ is picked out by the measurement. If we subsequently measure qubit $B$, then we are guaranteed (with probability one) to find $|0\rangle_B$ if we had found $|0\rangle_A$, and we are guaranteed to find $|1\rangle_B$ if we had found $|1\rangle_A$. In this sense, the outcomes of the $\{|0\rangle_A, |1\rangle_A\}$ and $\{|0\rangle_B, |1\rangle_B\}$ measurements are perfectly correlated in the state $|\psi\rangle_{AB}$.

But now we would like to consider more general observables acting on qubit $A$, and we would like to characterize the measurement outcomes for $A$ alone (irrespective of the outcomes of any measurements of the inaccessible qubit $B$). An observable acting on qubit $A$ only can be expressed as
$$
\boldsymbol{M}_A \otimes \boldsymbol{I}_B, \tag{2.54}
$$
where $\boldsymbol{M}_A$ is a self-adjoint operator acting on $A$, and $\boldsymbol{I}_B$ is the identity operator acting on $B$. The expectation value of the observable in the state $|\psi\rangle$ is:
$$
\begin{aligned}
\langle \boldsymbol{M}_A \rangle &= \langle\psi| \boldsymbol{M}_A \otimes \boldsymbol{I}_B |\psi\rangle \\
&= (a^* \langle 00| + b^* \langle 11|) (\boldsymbol{M}_A \otimes \boldsymbol{I}_B) (a|00\rangle + b|11\rangle) \\
&= |a|^2 \langle 0| \boldsymbol{M}_A |0\rangle + |b|^2 \langle 1| \boldsymbol{M}_A |1\rangle \tag{2.55}
\end{aligned}
$$
(where we have used the orthogonality of $|0\rangle_B$ and $|1\rangle_B$). This expression can be rewritten in the form
$$
\langle \boldsymbol{M}_A \rangle = \mathrm{tr}(\boldsymbol{M}_A \boldsymbol{\rho}_A), \quad \boldsymbol{\rho}_A = |a|^2 |0\rangle\langle 0| + |b|^2 |1\rangle\langle 1| \tag{2.56}
$$
and $\mathrm{tr}(\cdot)$ denotes the trace. The operator $\boldsymbol{\rho}_A$ is called the density operator (or density matrix) for qubit $A$. It is self-adjoint, positive (its eigenvalues are nonnegative) and it has unit trace (because $|\psi\rangle$ is a normalized state.)

Because $\langle \boldsymbol{M}_A \rangle$ has the form eq.(2.56) for any observable $\boldsymbol{M}_A$ acting on qubit $A$, it is consistent to interpret $\boldsymbol{\rho}_A$ as representing an ensemble of possible quantum states, each occurring with a specified probability. That is, we would obtain precisely the same result for $\langle \boldsymbol{M}_A \rangle$ if we stipulated that qubit $A$ is in one of two quantum states. With probability $p_0 = |a|^2$ it is in the quantum state $|0\rangle$, and with probability $p_1 = |b|^2$ it is in the state $|1\rangle$. To describe the measurement of an observable which acts on qubit $A$, we can consider $\boldsymbol{M}_A$ to be the projection $\boldsymbol{E}_A(a_n)$ onto the corresponding eigenstate of that observable. Then
$$
\mathrm{Prob}(a_n) = p_0 \langle 0| \boldsymbol{E}_A(a_n) |0\rangle + p_1 \langle 1| \boldsymbol{E}_A(a_n) |1\rangle, \tag{2.57}
$$
which is the probability of outcome $a_n$ summed over the ensemble, and weighted by the probability of each state in the ensemble.

We have emphasized previously that there is an essential difference between a coherent superposition of the states $|0\rangle$ and $|1\rangle$, and a probabilistic ensemble, in which $|0\rangle$ and $|1\rangle$ can each occur with specified probabilities. For example, for a spin-$1/2$ object we have seen that if we measure $\sigma_1$ in the state $\frac{1}{\sqrt{2}}(|\!\uparrow_z\rangle + |\!\downarrow_z\rangle)$, we will obtain the result $|\!\uparrow_x\rangle$ with probability one. But the ensemble in which $|\!\uparrow_z\rangle$ and $|\!\downarrow_z\rangle$ each occur with probability $1/2$ is represented by the density operator
$$
\boldsymbol{\rho} = \frac{1}{2}(|\!\uparrow_z\rangle\langle\uparrow_z\!| + |\!\downarrow_z\rangle\langle\downarrow_z\!|) = \frac{1}{2}\boldsymbol{I}, \tag{2.58}
$$
and the projection onto $|\!\uparrow_x\rangle$ then has the expectation value
$$
\mathrm{tr}(|\!\uparrow_x\rangle\langle\uparrow_x\!| \boldsymbol{\rho}) = \langle\uparrow_x\!| \boldsymbol{\rho} |\!\uparrow_x\rangle = \frac{1}{2}. \tag{2.59}
$$
Similarly, if we measure the spin along any axis labeled by polar angles $\theta$ and $\phi$, the probability of obtaining the result "spin up" is
$$
\begin{aligned}
\langle |\psi(\theta, \phi)\rangle\langle\psi(\theta, \phi)| \rangle &= \mathrm{tr}(|\psi(\theta, \phi)\rangle\langle\psi(\theta, \phi)| \boldsymbol{\rho}) \\
&= \langle\psi(\theta, \phi)| \frac{1}{2}\boldsymbol{I} |\psi(\theta, \phi)\rangle = \frac{1}{2}. \tag{2.60}
\end{aligned}
$$
Therefore, if in the two-qubit world an equally weighted coherent superposition of $|00\rangle$ and $|11\rangle$ is prepared, the state of qubit $A$ behaves incoherently -- along any axis it is an equiprobable mixture of spin up and spin down.

This discussion of the correlated two-qubit state $|\psi\rangle_{AB}$ is easily generalized to an arbitrary state of any bipartite quantum system (a system divided into two parts). The Hilbert space of a bipartite system is $\mathcal{H}_A \otimes \mathcal{H}_B$ where $\mathcal{H}_{A,B}$ are the Hilbert spaces of the two parts. This means that if $\{|i\rangle_A\}$ is an orthonormal basis for $\mathcal{H}_A$ and $\{|\mu\rangle_B\}$ is an orthonormal basis for $\mathcal{H}_B$, then $\{|i\rangle_A \otimes |\mu\rangle_B\}$ is an orthonormal basis for $\mathcal{H}_A \otimes \mathcal{H}_B$. Thus an arbitrary pure state of $\mathcal{H}_A \otimes \mathcal{H}_B$ can be expanded as
$$
|\psi\rangle_{AB} = \sum_{i,\mu} a_{i\mu} |i\rangle_A \otimes |\mu\rangle_B, \tag{2.61}
$$
where $\sum_{i,\mu} |a_{i\mu}|^2 = 1$. The expectation value of an observable $\boldsymbol{M}_A \otimes \boldsymbol{I}_B$ that acts only on subsystem $A$ is
$$
\begin{aligned}
\langle \boldsymbol{M}_A \rangle &= {}_{AB}\langle\psi| \boldsymbol{M}_A \otimes \boldsymbol{I}_B |\psi\rangle_{AB} \\
&= \sum_{j,\nu} a_{j\nu}^* ({}_A\langle j| \otimes {}_B\langle\nu|) (\boldsymbol{M}_A \otimes \boldsymbol{I}_B) \sum_{i,\mu} a_{i\mu} (|i\rangle_A \otimes |\mu\rangle_B) \\
&= \sum_{i,j,\mu} a_{j\mu}^* a_{i\mu} \langle j| \boldsymbol{M}_A |i\rangle = \mathrm{tr}(\boldsymbol{M}_A \boldsymbol{\rho}_A), \tag{2.62}
\end{aligned}
$$
where
$$
\boldsymbol{\rho}_A = \mathrm{tr}_B(|\psi\rangle\langle\psi|) \equiv \sum_{i,j,\mu} a_{i\mu} a_{j\mu}^* |i\rangle\langle j| \tag{2.63}
$$
is the density operator of subsystem $A$.

We may say that the density operator $\boldsymbol{\rho}_A$ for subsystem $A$ is obtained by performing a partial trace over subsystem $B$ of the density operator (in this case a pure state) for the combined system $AB$. We may regard a dual vector (or bra) ${}_B\langle\mu|$ as a linear map that takes vectors in $\mathcal{H}_A \otimes \mathcal{H}_B$ to vectors of $\mathcal{H}_A$, defined through its action on a basis:
$$
{}_B\langle\mu| i\nu\rangle_{AB} = \delta_{\mu\nu} |i\rangle_A; \tag{2.64}
$$
similarly, the ket $|\mu\rangle_B$ defines a map from the $\mathcal{H}_A \otimes \mathcal{H}_B$ dual basis to the $\mathcal{H}_A$ dual basis, via
$$
{}_{AB}\langle i\nu|\mu\rangle_B = \delta_{\mu\nu} {}_A\langle i|. \tag{2.65}
$$
The partial trace operation is a linear map that takes an operator $\boldsymbol{M}_{AB}$ on $\mathcal{H}_A \otimes \mathcal{H}_B$ to an operator on $\mathcal{H}_A$ defined as
$$
\mathrm{tr}_B \boldsymbol{M}_{AB} = \sum_\mu {}_B\langle\mu| \boldsymbol{M}_{AB} |\mu\rangle_B. \tag{2.66}
$$
We see that the density operator acting on $A$ is the partial trace
$$
\boldsymbol{\rho}_A = \mathrm{tr}_B(|\psi\rangle\langle\psi|). \tag{2.67}
$$
From the definition eq.(2.63), we can immediately infer that $\boldsymbol{\rho}_A$ has the following properties:

1. $\boldsymbol{\rho}_A$ is self-adjoint: $\boldsymbol{\rho}_A = \boldsymbol{\rho}_A^\dagger$.
2. $\boldsymbol{\rho}_A$ is positive: For any $|\phi\rangle$, $\langle\phi|\boldsymbol{\rho}_A|\phi\rangle = \sum_\mu |\sum_i a_{i\mu} \langle\phi|i\rangle|^2 \ge 0$.
3. $\mathrm{tr}(\boldsymbol{\rho}_A) = 1$: We have $\mathrm{tr}(\boldsymbol{\rho}_A) = \sum_{i,\mu} |a_{i\mu}|^2 = 1$, since $|\psi\rangle_{AB}$ is normalized.

It follows that $\boldsymbol{\rho}_A$ can be diagonalized in an orthonormal basis, that the eigenvalues are all real and nonnegative, and that the eigenvalues sum to one.

If we are looking at a subsystem of a larger quantum system, then, even if the state of the larger system is a ray, the state of the subsystem need not be; in general, the state is represented by a density operator. In the case where the state of the subsystem is a ray, we say that the state is pure. Otherwise the state is mixed. If the state is a pure state $|\psi\rangle_A$, then the density matrix $\boldsymbol{\rho}_A = |\psi\rangle\langle\psi|$ is the projection onto the one-dimensional space spanned by $|\psi\rangle_A$. Hence a pure density matrix has the property $\boldsymbol{\rho}^2 = \boldsymbol{\rho}$. A general density matrix, expressed in the basis $\{|a\rangle\}$ in which it is diagonal, has the form
$$
\boldsymbol{\rho}_A = \sum_a p_a |a\rangle\langle a|, \tag{2.68}
$$
where $0 < p_a \le 1$ and $\sum_a p_a = 1$. If the state is not pure, there are two or more terms in this sum, and $\boldsymbol{\rho}^2 \ne \boldsymbol{\rho}$; in fact, $\mathrm{tr}\boldsymbol{\rho}^2 = \sum p_a^2 < \sum p_a = 1$.

We say that $\boldsymbol{\rho}$ is an incoherent mixture of the states $\{|a\rangle\}$; "incoherent" means that the relative phases of the $|a\rangle$'s are experimentally inaccessible. Since the expectation value of any observable $\boldsymbol{M}$ acting on the subsystem can be expressed as
$$
\langle \boldsymbol{M} \rangle = \mathrm{tr}\boldsymbol{M}\boldsymbol{\rho} = \sum_a p_a \langle a|\boldsymbol{M}|a\rangle, \tag{2.69}
$$
we see as before that we may interpret $\boldsymbol{\rho}$ as describing an ensemble of pure quantum states, in which the state $|a\rangle$ occurs with probability $p_a$. We have, therefore, come a long part of the way to understanding how probabilities arise in quantum mechanics when a quantum system $A$ interacts with another system $B$. $A$ and $B$ become entangled, that is, correlated. The entanglement destroys the coherence of a superposition of states of $A$, so that some of the phases in the superposition become inaccessible if we look at $A$ alone. We may describe this situation by saying that the state of system $A$ collapses -- it is in one of a set of alternative states, each of which can be assigned a probability.

## 2.3.2 Bloch sphere [📄 chap2.pdf](/assets/pdf/preskill/chap2.pdf#page=21)

Let's return to the case in which system $A$ is a single qubit, and consider the form of the general density matrix. The most general self-adjoint $2 \times 2$ matrix has four real parameters, and can be expanded in the basis $\{\boldsymbol{I}, \boldsymbol{\sigma}_1, \boldsymbol{\sigma}_2, \boldsymbol{\sigma}_3\}$. Since each $\boldsymbol{\sigma}_i$ is traceless, the coefficient of $\boldsymbol{I}$ in the expansion of a density matrix $\boldsymbol{\rho}$ must be $1/2$ (so that $\mathrm{tr}(\boldsymbol{\rho}) = 1$), and $\boldsymbol{\rho}$ may be expressed as
$$
\begin{aligned}
\boldsymbol{\rho}(\vec{P}) &= \frac{1}{2}(\boldsymbol{I} + \vec{P} \cdot \vec{\boldsymbol{\sigma}}) \\
&\equiv \frac{1}{2}(\boldsymbol{I} + P_1 \boldsymbol{\sigma}_1 + P_2 \boldsymbol{\sigma}_2 + P_3 \boldsymbol{\sigma}_3) \\
&= \frac{1}{2} \begin{pmatrix} 1 + P_3 & P_1 - iP_2 \\ P_1 + iP_2 & 1 - P_3 \end{pmatrix}, \tag{2.70}
\end{aligned}
$$
where $P_1, P_2, P_3$ are real numbers. We can compute $\det \boldsymbol{\rho} = \frac{1}{4}(1 - \vec{P}^2)$. Therefore, a necessary condition for $\boldsymbol{\rho}$ to have nonnegative eigenvalues is $\det \boldsymbol{\rho} \ge 0$ or $\vec{P}^2 \le 1$. This condition is also sufficient; since $\mathrm{tr}\boldsymbol{\rho} = 1$, it is not possible for $\boldsymbol{\rho}$ to have two negative eigenvalues. Thus, there is a $1-1$ correspondence between the possible density matrices of a single qubit and the points on the unit 3-ball $0 \le |\vec{P}| \le 1$. This ball is usually called the Bloch sphere (although it is really a ball, not a sphere).

The boundary
$$
|\vec{P}| = 1
$$
of the ball (which really is a sphere) contains the density matrices with vanishing determinant. Since $\mathrm{tr}\boldsymbol{\rho} = 1$, these density matrices must have the eigenvalues $0$ and $1$ -- they are one-dimensional projectors, and hence pure states. We have already seen that any pure state of a single qubit is of the form $|\psi(\theta, \phi)\rangle$ and can be envisioned as a spin pointing in the $(\theta, \phi)$ direction. Indeed using the property
$$
(\hat{n} \cdot \vec{\boldsymbol{\sigma}})^2 = \boldsymbol{I}, \tag{2.71}
$$
where $\hat{n}$ is a unit vector, we can easily verify that the pure-state density matrix
$$
\boldsymbol{\rho}(\hat{n}) = \frac{1}{2}(\boldsymbol{I} + \hat{n} \cdot \vec{\boldsymbol{\sigma}}) \tag{2.72}
$$
satisfies the property
$$
(\hat{n} \cdot \vec{\boldsymbol{\sigma}})\boldsymbol{\rho}(\hat{n}) = \boldsymbol{\rho}(\hat{n})(\hat{n} \cdot \vec{\boldsymbol{\sigma}}) = \boldsymbol{\rho}(\hat{n}), \tag{2.73}
$$
and, therefore is the projector
$$
\boldsymbol{\rho}(\hat{n}) = |\psi(\hat{n})\rangle\langle\psi(\hat{n})|; \tag{2.74}
$$
that is, $\hat{n}$ is the direction along which the spin is pointing up. Alternatively, from the expression
$$
|\psi(\theta, \varphi)\rangle = \begin{pmatrix} e^{-i\varphi/2} \cos(\theta/2) \\ e^{i\varphi/2} \sin(\theta/2) \end{pmatrix}, \tag{2.75}
$$
we may compute directly that
$$
\begin{aligned}
\boldsymbol{\rho}(\theta, \varphi) &= |\psi(\theta, \varphi)\rangle\langle\psi(\theta, \varphi)| \\
&= \begin{pmatrix} \cos^2(\theta/2) & \cos(\theta/2)\sin(\theta/2)e^{-i\varphi} \\ \cos(\theta/2)\sin(\theta/2)e^{i\varphi} & \sin^2(\theta/2) \end{pmatrix} \\
&= \frac{1}{2}\boldsymbol{I} + \frac{1}{2}\begin{pmatrix} \cos\theta & \sin\theta e^{-i\varphi} \\ \sin\theta e^{i\varphi} & -\cos\theta \end{pmatrix} \\
&= \frac{1}{2}(\boldsymbol{I} + \hat{n} \cdot \vec{\boldsymbol{\sigma}}) \tag{2.76}
\end{aligned}
$$
where $\hat{n} = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$. One nice property of the Bloch parametrization of the pure states is that while $|\psi(\theta, \varphi)\rangle$ has an arbitrary overall phase that has no physical significance, there is no phase ambiguity in the density matrix $\boldsymbol{\rho}(\theta, \varphi) = |\psi(\theta, \varphi)\rangle\langle\psi(\theta, \varphi)|$; all the parameters in $\boldsymbol{\rho}$ have a physical meaning.

From the property
$$
\frac{1}{2} \mathrm{tr}\,\boldsymbol{\sigma}_i \boldsymbol{\sigma}_j = \delta_{ij} \tag{2.77}
$$
we see that
$$
\langle \hat{n} \cdot \vec{\boldsymbol{\sigma}} \rangle_{\vec{P}} = \mathrm{tr}\left((\hat{n} \cdot \vec{\boldsymbol{\sigma}})\boldsymbol{\rho}(\vec{P})\right) = \hat{n} \cdot \vec{P}. \tag{2.78}
$$
We say that the vector $\vec{P}$ in Eq. (2.70) parametrizes the polarization of the spin. If there are many identically prepared systems at our disposal, we can determine $\vec{P}$ (and hence the complete density matrix $\boldsymbol{\rho}(\vec{P})$) by measuring $\langle \hat{n} \cdot \vec{\boldsymbol{\sigma}} \rangle$ along each of three linearly independent axes.
