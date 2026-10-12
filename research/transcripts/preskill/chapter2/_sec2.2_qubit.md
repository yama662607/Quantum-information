# Section 2.2: The Qubit [PDF Pages 7-16]

<!-- ============================================================ -->
<!-- Source: chap2.pdf, Physical Pages: 7-16                       -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 7 -->
## 2.2 The Qubit

The indivisible unit of classical information is the *bit*, which takes one of the two possible values $\{0, 1\}$. The corresponding unit of quantum information is called the "quantum bit" or *qubit*. It describes a state in the simplest possible quantum system.

<!-- Page 8 -->
The smallest nontrivial Hilbert space is two-dimensional. We may denote an orthonormal basis for a two-dimensional vector space as $\{|0\rangle, |1\rangle\}$. Then the most general normalized state can be expressed as

$$
a|0\rangle + b|1\rangle,
$$ {#eq-2.15}

where $a, b$ are complex numbers that satisfy $|a|^2 + |b|^2 = 1$, and the overall phase is physically irrelevant. A *qubit* is a quantum system described by a two-dimensional Hilbert space, whose state can take any value of the form eq.(2.15).

We can perform a measurement that projects the qubit onto the basis $\{|0\rangle, |1\rangle\}$. Then we will obtain the outcome $|0\rangle$ with probability $|a|^2$, and the outcome $|1\rangle$ with probability $|b|^2$. Furthermore, *except* in the cases $a=0$ and $b=0$, the measurement irrevocably disturbs the state. If the value of the qubit is initially unknown, then there is no way to determine $a$ and $b$ with that single measurement, or any other conceivable measurement. However, *after* the measurement, the qubit has been prepared in a *known* state -- either $|0\rangle$ or $|1\rangle$ -- that differs (in general) from its previous state.

In this respect, a qubit differs from a classical bit; we can measure a classical bit without disturbing it, and we can decipher all of the information that it encodes. But suppose we have a classical bit that really does have a definite value (either 0 or 1), but where that value is initially unknown to us. Based on the information available to us we can only say that there is a *probability* $p_0$ that the bit has the value 0, and a probability $p_1$ that the bit has the value 1, where $p_0 + p_1 = 1$. When we measure the bit, we acquire additional information; afterwards we know the value with 100% confidence.

An important question is: what is the essential difference between a qubit and a *probabilistic* classical bit? In fact they are *not* the same, for several reasons that we will explore. To summarize the difference in brief: there is only one way to look at a bit, but there is more than one way to look at a qubit.

### 2.2.1 Spin-$\frac{1}{2}$

First of all, the coefficients $a$ and $b$ in eq.(2.15) encode more than just the probabilities of the outcomes of a measurement in the $\{|0\rangle, |1\rangle\}$ basis. In particular, the *relative phase* of $a$ and $b$ also has physical significance.

The properties of a qubit are easier to grasp if we appeal to a geometrical interpretation of its state. For a physicist, it is natural to interpret eq.(2.15) as the spin state of an object with spin-$\frac{1}{2}$ (like an electron). Then $|0\rangle$ and $|1\rangle$ are the spin up ($|\uparrow\rangle$) and spin down ($|\downarrow\rangle$) states along

<!-- Page 9 -->
a particular axis such as the $z$-axis. The two real numbers characterizing the qubit (the complex numbers $a$ and $b$, modulo the normalization and overall phase) describe the *orientation* of the spin in three-dimensional space (the polar angle $\theta$ and the azimuthal angle $\varphi$).

We will not go deeply here into the theory of symmetry in quantum mechanics, but we will briefly recall some elements of the theory that will prove useful to us. A *symmetry* is a transformation that acts on a state of a system, yet leaves all observable properties of the system unchanged. In quantum mechanics, observations are measurements of self-adjoint operators. If $\boldsymbol{A}$ is measured in the state $|\psi\rangle$, then the outcome $|a\rangle$ (an eigenvector of $\boldsymbol{A}$) occurs with probability $|\langle a|\psi\rangle|^2$. A symmetry should leave these probabilities unchanged, when we "rotate" both the system *and* the apparatus.

A symmetry, then, is a mapping of vectors in Hilbert space

$$
|\psi\rangle \mapsto |\psi'\rangle,
$$ {#eq-2.16}

that preserves the absolute values of inner products

$$
|\langle\varphi|\psi\rangle| = |\langle\varphi'|\psi'\rangle|,
$$ {#eq-2.17}

for all $|\varphi\rangle$ and $|\psi\rangle$. According to a famous theorem due to Wigner, a mapping with this property can always be chosen (by adopting suitable phase conventions) to be either unitary or antiunitary. The antiunitary alternative, while important for discrete symmetries, can be excluded for continuous symmetries. Then the symmetry acts as

$$
|\psi\rangle \mapsto |\psi'\rangle = \boldsymbol{U}|\psi\rangle,
$$ {#eq-2.18}

where $\boldsymbol{U}$ is unitary (and in particular, *linear*).

Symmetries form a *group*: a symmetry transformation can be inverted, and the product of two symmetries is a symmetry. For each symmetry operation $R$ acting on our physical system, there is a corresponding unitary transformation $\boldsymbol{U}(R)$. Multiplication of these unitary operators must respect the group multiplication law of the symmetries -- applying $R_1 \circ R_2$ should be equivalent to first applying $R_2$ and subsequently $R_1$. Thus we demand

$$
\boldsymbol{U}(R_1)\boldsymbol{U}(R_2) = \text{Phase}(R_1, R_2) \cdot \boldsymbol{U}(R_1 \circ R_2)
$$ {#eq-2.19}

A phase depending on $R_1$ and $R_2$ is permitted in eq.(2.19) because quantum states are *rays*; we need only demand that $\boldsymbol{U}(R_1 \circ R_2)$ act the same way as $\boldsymbol{U}(R_1)\boldsymbol{U}(R_2)$ on rays, not on vectors. We say that $\boldsymbol{U}(R)$ provides a unitary representation, up to a phase, of the symmetry group.

So far, our concept of symmetry has no connection with dynamics. Usually, we demand of a symmetry that it respect the dynamical evolution of the system. This means that it should not matter whether we

<!-- Page 10 -->
first transform the system and then evolve it, or first evolve it and then transform it. In other words, the diagram

$$
\begin{CD}
\text{Initial} @>\text{dynamics}>> \text{Final} \\
@VV\text{transformation}V @VV\text{transformation}V \\
\text{New Initial} @>\text{dynamics}>> \text{New Final}
\end{CD}
$$

is commutative, and therefore the time evolution operator $e^{-it\boldsymbol{H}}$ commutes with the symmetry transformation $\boldsymbol{U}(R)$:

$$
\boldsymbol{U}(R)e^{-it\boldsymbol{H}} = e^{-it\boldsymbol{H}}\boldsymbol{U}(R);
$$ {#eq-2.20}

expanding to linear order in $t$ we obtain

$$
\boldsymbol{U}(R)\boldsymbol{H} = \boldsymbol{H}\boldsymbol{U}(R).
$$ {#eq-2.21}

For a continuous symmetry, we can choose $R$ infinitesimally close to the identity, $R = I + \epsilon T$, and then $\boldsymbol{U}$ is close to $\boldsymbol{I}$:

$$
\boldsymbol{U} = \boldsymbol{I} - i\epsilon\boldsymbol{Q} + O(\epsilon^2),
$$ {#eq-2.22}

where $\boldsymbol{Q}$ is an operator determined by $T$. From the unitarity of $\boldsymbol{U}$ (to order $\epsilon$) it follows that $\boldsymbol{Q}$ is an observable, $\boldsymbol{Q} = \boldsymbol{Q}^\dagger$. Expanding eq.(2.21) to linear order in $\epsilon$ we find

$$
[\boldsymbol{Q}, \boldsymbol{H}] = 0;
$$ {#eq-2.23}

the observable $\boldsymbol{Q}$ commutes with the Hamiltonian.

Eq.(2.23) is a *conservation law*. It says, for example, that if we prepare an eigenstate of $\boldsymbol{Q}$, then time evolution governed by the Schr\"odinger equation will preserve the eigenstate. Thus we see that symmetries imply conservation laws. Conversely, given a conserved quantity $\boldsymbol{Q}$ satisfying eq.(2.23) we can construct the corresponding symmetry transformations. Finite transformations can be built as a product of many infinitesimal ones:

$$
R = \left(1 + \frac{\theta}{N}T\right)^N \Rightarrow \boldsymbol{U}(R) = \left(\boldsymbol{I} + i\frac{\theta}{N}\boldsymbol{Q}\right)^N \to e^{i\theta\boldsymbol{Q}},
$$ {#eq-2.24}

taking the limit $N \to \infty$. Once we have decided how infinitesimal symmetry transformations are represented by unitary operators, then it is also

<!-- Page 11 -->
determined how finite transformations are represented, for these can be built as a product of infinitesimal transformations. We say that $\boldsymbol{Q}$ is the *generator* of the symmetry.

Let us briefly recall how this general theory applies to spatial rotations and angular momentum. An infinitesimal rotation by $d\theta$ (in the counterclockwise sense) about the axis specified by the unit vector $\hat{n} = (n_1, n_2, n_3)$ can be expressed as

$$
R(\hat{n}, d\theta) = I - i d\theta \hat{n}\cdot \vec{J},
$$ {#eq-2.25}

where $(J_1, J_2, J_3)$ are the components of the angular momentum. A finite rotation is expressed as

$$
R(\hat{n}, \theta) = \exp(-i\theta\hat{n}\cdot\vec{J}).
$$ {#eq-2.26}

Rotations about distinct axes don't commute. From elementary properties of rotations, we find the commutation relations

$$
[J_k, J_\ell] = i\epsilon_{k\ell m}J_m,
$$ {#eq-2.27}

where $\epsilon_{k\ell m}$ is the totally antisymmetric tensor with $\epsilon_{123} = 1$, and repeated indices are summed. To implement rotations on a quantum system, we find self-adjoint operators $\boldsymbol{J}_1, \boldsymbol{J}_2, \boldsymbol{J}_3$ in Hilbert space that satisfy these relations.

The "defining" representation of the rotation group is three dimensional, but the simplest nontrivial irreducible representation is two dimensional, given by

$$
\boldsymbol{J}_k = \frac{1}{2}\boldsymbol{\sigma}_k,
$$ {#eq-2.28}

where

$$
\boldsymbol{\sigma}_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \quad \boldsymbol{\sigma}_2 = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}, \quad \boldsymbol{\sigma}_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},
$$ {#eq-2.29}

are the Pauli matrices. This is the unique two-dimensional irreducible representation, up to a unitary change of basis. Since the eigenvalues of $\boldsymbol{J}_k$ are $\pm\frac{1}{2}$, we call this the spin-$\frac{1}{2}$ representation. (By identifying $\boldsymbol{J}$ as the angular-momentum, we have implicitly chosen units with $\hbar = 1$.)

The Pauli matrices also have the properties of being mutually anticommuting and squaring to the identity,

$$
\boldsymbol{\sigma}_k\boldsymbol{\sigma}_\ell + \boldsymbol{\sigma}_\ell\boldsymbol{\sigma}_k = 2\delta_{k\ell}\boldsymbol{I};
$$ {#eq-2.30}

therefore $(\hat{n}\cdot\vec{\boldsymbol{\sigma}})^2 = n_k n_\ell \boldsymbol{\sigma}_k\boldsymbol{\sigma}_\ell = n_k n_k \boldsymbol{I} = \boldsymbol{I}$ (where repeated indices are summed). By expanding the exponential series, we see that finite rotations are represented as

$$
\boldsymbol{U}(\hat{n}, \theta) = e^{-i\frac{\theta}{2}\hat{n}\cdot\vec{\boldsymbol{\sigma}}} = \boldsymbol{I}\cos\frac{\theta}{2} - i\hat{n}\cdot\vec{\boldsymbol{\sigma}}\sin\frac{\theta}{2}.
$$ {#eq-2.31}

<!-- Page 12 -->
The most general $2 \times 2$ unitary matrix with determinant 1 can be expressed in this form. Thus, we are entitled to think of a qubit as a spin-$\frac{1}{2}$ object, and an arbitrary unitary transformation acting on the qubit's state (aside from a possible physically irrelevant rotation of the overall phase) is a *rotation of the spin*.

A peculiar property of the representation $\boldsymbol{U}(\hat{n}, \theta)$ is that it is *double-valued*. In particular a rotation by $2\pi$ about any axis is represented nontrivially:

$$
\boldsymbol{U}(\hat{n}, \theta=2\pi) = -\boldsymbol{I}.
$$ {#eq-2.32}

Our representation of the rotation group is really a representation "up to a sign"

$$
\boldsymbol{U}(R_1)\boldsymbol{U}(R_2) = \pm\boldsymbol{U}(R_1 \circ R_2).
$$ {#eq-2.33}

But as already noted, this is acceptable, because the group multiplication is respected on *rays*, though not on vectors. These double-valued representations of the rotation group are called *spinor* representations. (The existence of spinors follows from a topological property of the group -- that it is not simply connected.)

While it is true that a rotation by $2\pi$ has no detectable effect on a spin-$\frac{1}{2}$ object, it would be wrong to conclude that the spinor property has no observable consequences. Suppose I have a machine that acts on a pair of spins. If the first spin is up, it does nothing, but if the first spin is down, it rotates the second spin by $2\pi$. Now let the machine act when the first spin is in a *superposition* of up and down. Then

$$
\frac{1}{\sqrt{2}}(|\uparrow\rangle_1 + |\downarrow\rangle_1)|\uparrow\rangle_2 \mapsto \frac{1}{\sqrt{2}}(|\uparrow\rangle_1 - |\downarrow\rangle_1)|\uparrow\rangle_2.
$$ {#eq-2.34}

While there is no detectable effect on the second spin, the state of the first has flipped to an orthogonal state, which is very much observable.

In a rotated frame of reference, a rotation $R(\hat{n}, \theta)$ becomes a rotation through the same angle but about a rotated axis. It follows that the three components of angular momentum transform under rotations as a vector:

$$
\boldsymbol{U}(R)\boldsymbol{J}_k\boldsymbol{U}(R)^\dagger = R_{k\ell}\boldsymbol{J}_\ell.
$$ {#eq-2.35}

Thus, if a state $|m\rangle$ is an eigenstate of $\boldsymbol{J}_3$

$$
\boldsymbol{J}_3|m\rangle = m|m\rangle,
$$ {#eq-2.36}

then $\boldsymbol{U}(R)|m\rangle$ is an eigenstate of $R\boldsymbol{J}_3$ with the same eigenvalue:

$$
\begin{aligned}
R\boldsymbol{J}_3(\boldsymbol{U}(R)|m\rangle) &= \boldsymbol{U}(R)\boldsymbol{J}_3\boldsymbol{U}(R)^\dagger\boldsymbol{U}(R)|m\rangle \\
&= \boldsymbol{U}(R)\boldsymbol{J}_3|m\rangle = m(\boldsymbol{U}(R)|m\rangle).
\end{aligned}
$$ {#eq-2.37}

<!-- Page 13 -->
Therefore, we can construct eigenstates of angular momentum along the axis $\hat{n} = (\sin\theta\cos\varphi, \sin\theta\sin\varphi, \cos\theta)$ by applying a counterclockwise rotation through $\theta$, about the axis $\hat{n}' = (-\sin\varphi, \cos\varphi, 0)$, to a $\boldsymbol{J}_3$ eigenstate. For our spin-$\frac{1}{2}$ representation, this rotation is

$$
\begin{aligned}
\exp\left(-i\frac{\theta}{2}\hat{n}'\cdot\vec{\boldsymbol{\sigma}}\right) &= \exp\left[\frac{\theta}{2}\begin{pmatrix} 0 & -e^{-i\varphi} \\ e^{i\varphi} & 0 \end{pmatrix}\right] \\
&= \begin{pmatrix} \cos\frac{\theta}{2} & -e^{-i\varphi}\sin\frac{\theta}{2} \\ e^{i\varphi}\sin\frac{\theta}{2} & \cos\frac{\theta}{2} \end{pmatrix},
\end{aligned}
$$ {#eq-2.38}

and applying it to $\begin{pmatrix} 1 \\ 0 \end{pmatrix}$, the $\boldsymbol{J}_3$ eigenstate with eigenvalue 1, we obtain

$$
|\psi(\theta, \varphi)\rangle = \begin{pmatrix} e^{-i\varphi/2}\cos\frac{\theta}{2} \\ e^{i\varphi/2}\sin\frac{\theta}{2} \end{pmatrix},
$$ {#eq-2.39}

(up to an overall phase). We can check directly that this is an eigenstate of

$$
\hat{n}\cdot\vec{\boldsymbol{\sigma}} = \begin{pmatrix} \cos\theta & e^{-i\varphi}\sin\theta \\ e^{i\varphi}\sin\theta & -\cos\theta \end{pmatrix},
$$ {#eq-2.40}

with eigenvalue one. We now see that eq.(2.15) with $a = e^{-i\varphi/2}\cos\frac{\theta}{2}$, $b = e^{i\varphi/2}\sin\frac{\theta}{2}$, can be interpreted as a spin pointing in the $(\theta, \varphi)$ direction.

We noted that we cannot determine $a$ and $b$ with a single measurement. Furthermore, even with many identical copies of the state, we cannot completely determine the state by measuring each copy only along the $z$-axis. This would enable us to estimate $|a|$ and $|b|$, but we would learn nothing about the relative phase of $a$ and $b$. Equivalently, we would find the component of the spin along the $z$-axis

$$
\langle\psi(\theta, \varphi)|\boldsymbol{\sigma}_3|\psi(\theta, \varphi)\rangle = \cos^2\frac{\theta}{2} - \sin^2\frac{\theta}{2} = \cos\theta,
$$ {#eq-2.41}

but we would not learn about the component in the $x$-$y$ plane. The problem of determining $|\psi\rangle$ by measuring the spin is equivalent to determining the unit vector $\hat{n}$ by measuring its components along various axes. Altogether, measurements along three different axes are required. E.g., from $\langle\boldsymbol{\sigma}_3\rangle$ and $\langle\boldsymbol{\sigma}_1\rangle$ we can determine $n_3$ and $n_1$, but the sign of $n_2$ remains undetermined. Measuring $\langle\boldsymbol{\sigma}_2\rangle$ would remove this remaining ambiguity.

If we are permitted to rotate the spin, then only measurements along the $z$-axis will suffice. That is, measuring a spin along the $\hat{n}$ axis is equivalent to first applying a rotation that rotates the $\hat{n}$ axis to the axis $\hat{z}$, and then measuring along $\hat{z}$.

In the special case $\theta = \frac{\pi}{2}$ and $\varphi = 0$ (the $\hat{x}$-axis) our spin state is

$$
|\uparrow_x\rangle = \frac{1}{\sqrt{2}}(|\uparrow_z\rangle + |\downarrow_z\rangle)
$$ {#eq-2.42}

<!-- Page 14 -->
("spin-up along the $x$-axis"). The orthogonal state ("spin down along the $x$-axis") is

$$
|\downarrow_x\rangle = \frac{1}{\sqrt{2}}(|\uparrow_z\rangle - |\downarrow_z\rangle).
$$ {#eq-2.43}

For either of these states, if we measure the spin along the $z$-axis, we will obtain $|\uparrow_z\rangle$ with probability $\frac{1}{2}$ and $|\downarrow_z\rangle$ with probability $\frac{1}{2}$.

Now consider the combination

$$
\frac{1}{\sqrt{2}}(|\uparrow_x\rangle + |\downarrow_x\rangle).
$$ {#eq-2.44}

This state has the property that, if we measure the spin along the $x$-axis, we obtain $|\uparrow_x\rangle$ or $|\downarrow_x\rangle$, each with probability $\frac{1}{2}$. Now we may ask, what if we measure the state in eq.(2.44) along the $z$-axis?

If these were probabilistic classical bits, the answer would be obvious. The state in eq.(2.44) is in one of two states, and for *each* of the two, the probability is $\frac{1}{2}$ for pointing up or down along the $z$-axis. So of course we should find up with probability $\frac{1}{2}$ when we measure the state $\frac{1}{\sqrt{2}}(|\uparrow_x\rangle + |\downarrow_x\rangle)$ along the $z$-axis.

But not so for qubits! By adding eq.(2.42) and eq.(2.43), we see that the state in eq.(2.44) is really $|\uparrow_z\rangle$ in disguise. When we measure along the $z$-axis, we always find $|\uparrow_z\rangle$, never $|\downarrow_z\rangle$.

We see that for qubits, as opposed to probabilistic classical bits, probabilities can add in unexpected ways. This is, in its simplest guise, the phenomenon called "quantum interference," an important feature of quantum information.

To summarize the geometrical interpretation of a qubit: we may think of a qubit as a spin-$\frac{1}{2}$ object, and its quantum state is characterized by a unit vector $\hat{n}$ in three dimensions, the spin's direction. A unitary transformation rotates the spin, and a measurement of an observable has two possible outcomes: the spin is either up or down along a specified axis.

It should be emphasized that, while this *formal* equivalence with a spin-$\frac{1}{2}$ object applies to any two-level quantum system, not every two-level system transforms as a spinor under spatial rotations!

### 2.2.2 Photon polarizations

Another important two-state system is provided by a *photon*, which can have two independent polarizations. These photon polarization states also transform under rotations, but photons differ from our spin-$\frac{1}{2}$ objects in two important ways: (1) Photons are massless. (2) Photons have spin-1 (they are not spinors).

<!-- Page 15 -->
We will not present here a detailed discussion of the unitary representations of the Poincare group. Suffice it to say that the *spin* of a particle classifies how it transforms under the *little group*, the subgroup of the Lorentz group that preserves the particle's momentum. For a massive particle, we may always boost to the particle's rest frame, and then the little group is the rotation group.

For massless particles, there is no rest frame. The finite-dimensional unitary representations of the little group turn out to be representations of the rotation group in *two* dimensions, the rotations about the axis determined by the momentum. For a photon, this corresponds to a familiar property of classical light -- the waves are polarized transverse to the direction of propagation.

Under a rotation about the axis of propagation, the two linear polarization states ($|x\rangle$ and $|y\rangle$ for horizontal and vertical polarization) transform as

$$
\begin{aligned}
|x\rangle &\to \cos\theta|x\rangle + \sin\theta|y\rangle \\
|y\rangle &\to -\sin\theta|x\rangle + \cos\theta|y\rangle.
\end{aligned}
$$ {#eq-2.45}

This two-dimensional representation is actually reducible. The matrix

$$
\begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix}
$$ {#eq-2.46}

has the eigenstates

$$
|R\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 \\ i \end{pmatrix}, \quad |L\rangle = \frac{1}{\sqrt{2}}\begin{pmatrix} i \\ 1 \end{pmatrix},
$$ {#eq-2.47}

with eigenvalues $e^{i\theta}$ and $e^{-i\theta}$, the states of right and left circular polarization. That is, these are the eigenstates of the rotation generator

$$
\boldsymbol{J} = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix} = \boldsymbol{\sigma}_2,
$$ {#eq-2.48}

with eigenvalues $\pm 1$. Because the eigenvalues are $\pm 1$ (not $\pm\frac{1}{2}$) we say that the photon has spin-1.

In this context, the quantum interference phenomenon can be described as follows. The polarization states

$$
\begin{aligned}
|+\rangle &= \frac{1}{\sqrt{2}}(|x\rangle + |y\rangle), \\
|-\rangle &= \frac{1}{\sqrt{2}}(-|x\rangle + |y\rangle),
\end{aligned}
$$ {#eq-2.49}

<!-- Page 16 -->
are mutually orthogonal and can be obtained by rotating the states $|x\rangle$ and $|y\rangle$ by $45^\circ$. Suppose that we have a polarization analyzer that allows only one of two orthogonal linear photon polarizations to pass through, absorbing the other. Then an $x$ or $y$ polarized photon has probability $\frac{1}{2}$ of getting through a $45^\circ$ rotated polarizer, and a $45^\circ$ polarized photon has probability $\frac{1}{2}$ of getting through an $x$ or $y$ analyzer. But an $x$ photon never passes through a $y$ analyzer.

Suppose that a photon beam is directed at an $x$ analyzer, with a $y$ analyzer placed further downstream. Then about half of the photons will pass through the first analyzer, but every one of these will be stopped by the second analyzer. But now suppose that we place a $45^\circ$-rotated analyzer between the $x$ and $y$ analyzers. Then about half of the photons pass through each analyzer, and about one in eight will manage to pass all three without being absorbed. Because of this *interference* effect, there is no consistent interpretation in which each photon carries one classical bit of polarization information. Qubits are different than probabilistic classical bits.

A device can be constructed that rotates the linear polarization of a photon, and so applies the transformation Eq. (2.45) to our qubit; it functions by "turning on" a Hamiltonian for which the circular polarization states $|L\rangle$ and $|R\rangle$ are nondegenerate energy eigenstates. This is not the most general possible unitary transformation. But if we also have a device that alters the relative phase of the two orthogonal linear polarization states

$$
\begin{aligned}
|x\rangle &\to e^{-i\varphi/2}|x\rangle, \\
|y\rangle &\to e^{i\varphi/2}|y\rangle
\end{aligned}
$$ {#eq-2.50}

(by turning on a Hamiltonian whose nondegenerate energy eigenstates are the linear polarization states), then the two devices can be employed together to apply an arbitrary $2 \times 2$ unitary transformation (of determinant 1) to the photon polarization state.
