# Section 3.3 Transcript: Channel-state duality and the dilation of a channel

**Source**: `quarto/assets/pdf/preskill/chap3.pdf` (Pages 20–23)  
**Status**: Complete, faithful transcript including all mathematical expressions and formatting.

---

## 3.3 Channel-state duality and the dilation of a channel (p. 20)

We have now seen that a quantum channel acting on $A$, which arises from a unitary map on an extension of $A$, is a completely positive linear map of density operators to density operators. We have also argued that linearity and complete positivity are properties that should hold for any reasonable evolution law on quantum states. It is therefore satisfying to note that any trace-preserving completely positive linear map is a quantum channel — it has an operator sum representation and a unitary realization. When considering the (in general nonunitary) evolution of $A$, we are entitled to imagine that $A$ is part of an extended system which evolves unitarily.

### 3.3.1 Channel-state duality (p. 20)

To prove this statement we will use a trick which is interesting in its own right and also has other applications. For the purpose of studying the properties of a map $\mathcal{E}$ taking $A$ to $A'$, we introduce an auxiliary system $R$ with the same dimension as $A$, which we call the *reference system*. If $\mathcal{E}$ is completely positive, it maps a maximally entangled state on $RA$ to a nonnegative operator on $RA'$. Conversely, we may associate with any nonnegative operator on $RA'$ a corresponding CP map taking $A$ to $A'$. This correspondence between maps and states, called the *Choi-Jamiołkowski isomorphism* or *channel-state duality*, is a very useful tool.

To see how it works, consider how $I \otimes \mathcal{E}$ acts on the maximally entangled state
$$
|\tilde{\Phi}\rangle_{RA} = \sum_{i=0}^{d-1} |i\rangle_R \otimes |i\rangle_A.
\tag{3.70}
$$
where $A$ and $R$ both have dimension $d$. This vector has norm $\sqrt{d}$ instead of norm $1$; we choose this unconventional normalization, highlighted by the tilde over $\Phi$, to avoid annoying factors of $d$ in the formulas that follow.

If $\mathcal{E}_{A \to A'}$ is completely positive, then $I \otimes \mathcal{E}$ maps $|\tilde{\Phi}\rangle\langle\tilde{\Phi}|$ (up to normalization) to a density operator on $RA'$, which like any density operator can be realized by an ensemble of pure states; hence
$$
(I \otimes \mathcal{E})\left( \big(|\tilde{\Phi}\rangle\langle\tilde{\Phi}|\big)_{RA} \right) = \sum_a \big(|\tilde{\Psi}_a\rangle\langle\tilde{\Psi}_a|\big)_{RA'}.
\tag{3.71}
$$
Here the normalization of $|\tilde{\Psi}_a\rangle$ may depend on $a$; in order to make the equation look less cluttered, we've absorbed the probability of each pure state occurring in the ensemble into that state's normalization.

Now we notice that
$$
|\varphi\rangle_A = \sum_i \varphi_i |i\rangle_A = \sum_i \varphi_i \left({}_R\langle i|\tilde{\Phi}\rangle_{RA}\right) = {}_R\langle\varphi^*|\tilde{\Phi}\rangle_{RA};
\tag{3.72}
$$
using the linearity of $\mathcal{E}$, eq.(3.71) then implies
$$
\mathcal{E}\left( (|\varphi\rangle\langle\varphi|)_A \right) = \sum_a \left(\langle\varphi^*|\tilde{\Psi}_a\rangle\langle\tilde{\Psi}_a|\varphi^*\rangle\right)_{A'}.
\tag{3.73}
$$
(This scheme for extracting the action on $|\varphi\rangle_A$ using the dual vector ${}_R\langle\varphi^*|$ is called the *relative-state method*.) Given a vector $|\tilde{\Phi}\rangle_{RA'}$ [Note: in context of eq.(3.74), $|\tilde{\Psi}_a\rangle_{RA'}$], where $R$ is $d$ dimensional, we may define an operator $\boldsymbol{M}_a$ mapping $\mathcal{H}_A$ to $\mathcal{H}_{A'}$ (where $A$ is $d$ dimensional) by
$$
\boldsymbol{M}_a |\varphi\rangle_A = {}_R\langle\varphi^*|\tilde{\Psi}_a\rangle_{RA'};
\tag{3.74}
$$
it is easy to check that $\boldsymbol{M}_a$ is linear. Thus eq.(3.73) provides an operator-sum representation of $\mathcal{E}$ acting on the pure state $(|\varphi\rangle\langle\varphi|)_A$ (and hence by linearity acting on any density operator):
$$
\mathcal{E}(\boldsymbol{\rho}) = \sum_a \boldsymbol{M}_a \boldsymbol{\rho} \boldsymbol{M}_a^\dagger.
\tag{3.75}
$$
We have now established the desired isomorphism between states and CP maps: Eq.(3.71) tells us how to obtain a state on $RA'$ from the channel $\mathcal{E}_{A \to A'}$, while eq.(3.74) and eq.(3.75) tells us how to recover the CP map from the state. Furthermore, the $\{\boldsymbol{M}_a\}$ must obey the completeness relation $\sum_a \boldsymbol{M}_a^\dagger \boldsymbol{M}_a = \boldsymbol{I}$ if $\mathcal{E}$ is trace-preserving.

Put succinctly, the argument went as follows. Because $\mathcal{E}_{A \to A'}$ is completely positive, $I \otimes \mathcal{E}$ takes a maximally entangled state on $RA$ to a density operator on $RA'$, up to normalization. This density operator can be expressed as an ensemble of pure states, and each of these pure states is associated with a Kraus operator in the operator-sum representation of $\mathcal{E}$.

From this viewpoint, we see that the freedom to choose the Kraus operators representing a channel in many different ways is really the same thing as the freedom to choose the ensemble of pure states representing a density operator in many different ways. According to the HJW theorem, two different ensemble realizations of the same density operator,
$$
(I \otimes \mathcal{E})\left( \big(|\tilde{\Phi}\rangle\langle\tilde{\Phi}|\big)_{RA} \right) = \sum_a \big(|\tilde{\Psi}_a\rangle\langle\tilde{\Psi}_a|\big)_{RA'} = \sum_\mu (|\tilde{\gamma}_\mu\rangle\langle\tilde{\gamma}_\mu|)_{RA'},
\tag{3.76}
$$
are related by a unitary change of basis,
$$
|\tilde{\gamma}_\mu\rangle = \sum_a V_{\mu a} |\tilde{\Psi}_a\rangle.
\tag{3.77}
$$
Correspondingly, two different sets of Kraus operators $\{\boldsymbol{M}_a\}$ and $\{\boldsymbol{N}_\mu\}$ representing the same channel are related by
$$
\boldsymbol{N}_\mu = \sum_a V_{\mu a} \boldsymbol{M}_a
\tag{3.78}
$$
where $V_{\mu a}$ is a unitary matrix.

Channel-state duality also makes clear how many Kraus operators are needed to describe a channel. A channel $\mathcal{E}$ mapping $A$ to $A'$, where $A$ has dimension $d$ and $A'$ has dimension $d'$, is equivalent to a density operator on $RA'$, where $R$ has dimension $d$, and the minimal number of Kraus operators needed to represent the channel is the same as the minimal number of pure states needed in an ensemble representation of the density operator. This is the density operator's rank (number of nonzero eigenvalues), which is no larger than $dd'$. Of course, there may be operator-sum representations of $\mathcal{E}$ which use many more than this minimal number of Kraus operators, just as an ensemble representation of a density operator might use many more than the minimal number of pure states.

The number of free parameters needed to specify a channel mapping $A$ to $A'$ is the number $(dd')^2$ needed to specify a density operator on $RA'$, except that there are $d^2$ constraints because the map is trace preserving for each of $d^2$ linearly independent inputs. Therefore the number of real free parameters is
$$
d^2 (d'^2 - 1).
\tag{3.79}
$$
This is 12 parameters for a general channel taking qubits to qubits. In contrast, a unitary map on qubits has only 3 parameters, aside from the physically irrelevant overall phase.

### 3.3.2 Stinespring dilation (p. 22)

Once we have an operator-sum representation of the channel $\mathcal{E}_{A \to A'}$, it is easy to see how $\mathcal{E}$ can be realized by a unitary map acting on an extended system. We introduce an extra system $E$, the channel's *environment*, which has dimension equal to the number of Kraus operators and orthonormal basis $\{|a\rangle\}$. Then we define an inner-product preserving map (an *isometry*) which takes $A$ to $A'E$ according to
$$
\boldsymbol{U}_{A \to A'E} : |\psi\rangle \mapsto \sum_a \boldsymbol{M}_a |\psi\rangle \otimes |a\rangle.
\tag{3.80}
$$
The completeness relation satisfied by the $\{\boldsymbol{M}_a\}$ implies $\boldsymbol{U}^\dagger \boldsymbol{U} = \boldsymbol{I}_A$. Though $\boldsymbol{U}$ may not actually be unitary, it might as well be, because we can easily extend an isometry to a unitary transformation by expanding the input Hilbert space. This isometry, which yields $\mathcal{E}_{A \to A'}$ when we trace out the environment, is called the *Stinespring dilation* of the channel.

Another way to think about the construction of the Stinespring dilation is that we have used $E$ to construct a *purification* of the density operator arising from channel-state duality:
$$
|\bar{\Psi}\rangle_{RA'E} = \sum_a |\tilde{\Psi}_a\rangle_{RA'} \otimes |a\rangle_E.
\tag{3.81}
$$
Apart from a normalization factor of $\sqrt{d}$, this is the pure state of $RA'E$ that results when the dilation acts on the maximally entangled state $|\tilde{\Phi}\rangle_{RA}$; we may recover the dilation from $|\bar{\Psi}\rangle$ using
$$
\boldsymbol{U}_{A \to A'E}|\psi\rangle_A = {}_R\langle\psi^*|\bar{\Psi}\rangle_{RA'E}.
\tag{3.82}
$$
This succinct way to characterize a channel using a pure state is sometimes quite convenient, and we'll make heavy use of it when studying quantum channels in Chapter 10.

### 3.3.3 Axioms revisited (p. 23)

In Chapter 2 we stated the axioms of quantum mechanics in a form appropriate for closed systems. With the theory of open systems now in hand, we can give an alternative formulation with revised notions of how states, measurements, and evolution are described.

**States.** A state is a *density operator*, a nonnegative Hermitian operator in Hilbert space with unit trace.

**Measurement.** A measurement is a *positive operator-valued measure* (*POVM*), a partition of unity by nonnegative operators. When the measurement $\{\boldsymbol{E}_a\}$ is performed on the state $\boldsymbol{\rho}$, the outcome $a$ occurs with probability $\mathrm{tr}(\boldsymbol{E}_a \boldsymbol{\rho})$.

**Dynamics.** Time evolution is described by a *trace-preserving completely positive map* (*TPCP map*).

One could regard either the open-system or closed-system version as the fundamental formulation of the theory; it's really a matter of taste. We have already seen how the open-system axioms are obtained starting from the closed-system axioms. Alternatively, starting with the open-system axioms, pure states arise as the extremal points in the space of density operators, or from the observation that every density operator has a purification in an extended system. Similarly, orthogonal measurements and unitary evolution arise naturally because every POVM can be realized by an orthogonal measurement in an extended system, and every trace-preserving completely positive map has an isometric Stinespring dilation. The notion that an open system may always be regarded as part of a larger closed system is fondly known as the *church of the larger Hilbert space*.
