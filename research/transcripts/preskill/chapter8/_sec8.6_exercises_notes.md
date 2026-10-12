# Section 8.6: Epilogue, Chern-Simons Theory, S-Matrix, Edge Excitations, and Bibliographical Notes [PDF Pages 63-68]

<!-- ============================================================ -->
<!-- Source: chap8.pdf, Physical Pages: 63-68                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 63 -->
## 9.18 Epilogue

That is as far as I got in class. I will mention briefly here a few other topics that I might have covered if I had not run out of time.

### 9.18.1 Chern-Simons theory

We have discussed how anyon models can be constructed through a brute-force solution to the polynomial equations. This method is foolproof, but in practice models are often constructed using other, more efficient methods. Indeed, most of the known anyon models have been found as instances of Chern-Simons theory.

The fusion rules of a Chern-Simons theory are a truncated version of the fusion rules for irreducible representations of a Lie group. For example, associated with the group $\text{SU}(2)$ there is a tower of Chern-Simons theories indexed by a positive integer $k$. For $\text{SU}(2)$, the irreducible representations carry labels $j = 0, \frac{1}{2}, 1, \frac{3}{2}, 2, \frac{5}{2}, \dots$, and the fusion rules have the form

$$
j_1 \times j_2 = \sum_{j = |j_2 - j_1|}^{j_1 + j_2} j.
$$ {#eq-8.128}

In the Chern-Simons theory denoted $\text{SU}(2)_k$, the half-integer labels are limited to $j \le k/2$, and the label $j$ is contained in $j_1 \times j_2$ only if $j_1 + j_2 + j \le k$.

For example, the $\text{SU}(2)_1$ model is abelian, and the nontrivial fusion rules of the $\text{SU}(2)_2$ model are

$$
\begin{aligned}
\frac{1}{2} \times \frac{1}{2} &= 0 + 1, \\
\frac{1}{2} \times 1 &= \frac{1}{2}, \\
1 \times 1 &= 0.
\end{aligned}
$$ {#eq-8.129}

Therefore, the label $\frac{1}{2}$ has quantum dimension $d_{1/2} = \sqrt{2}$, and the topological Hilbert space of $2m$ such anyons with total charge 0 has dimension

$$
N_{(\frac{1}{2})^{2m}}^0 = 2^{m-1}.
$$ {#eq-8.130}

The polynomial equations for these fusion rules have multiple solutions (only one of which describes the braiding properties of the $\text{SU}(2)_2$ model), but none of the resulting models have computationally universal braiding rules. The space $V_{\frac{1}{2}\frac{1}{2}\frac{1}{2}\frac{1}{2}}^0$ is two-dimensional, and the $2 \times 2$ matrices $F \equiv F_{\frac{1}{2}\frac{1}{2}\frac{1}{2}\frac{1}{2}}$ and $R \equiv R_{\frac{1}{2}\frac{1}{2}}$ are, up to overall phases and complex conjugation,

$$
F = H = \frac{1}{\sqrt{2}} \begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}, \quad R = P = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}.
$$ {#eq-8.131}

<!-- Page 64 -->
These are Clifford-group quantum gates, inadequate for universality.

However, the $\text{SU}(2)_k$ models for $k \ge 3$ *are* computationally universal. The nontrivial fusion rules of $\text{SU}(2)_3$ are

$$
\begin{aligned}
\frac{1}{2} \times \frac{1}{2} &= 0 + 1, \\
\frac{1}{2} \times 1 &= \frac{1}{2} + \frac{3}{2}, \\
\frac{1}{2} \times \frac{3}{2} &= 1, \\
1 \times 1 &= 0 + 1, \\
1 \times \frac{3}{2} &= \frac{1}{2}, \\
\frac{3}{2} \times \frac{3}{2} &= 0.
\end{aligned}
$$ {#eq-8.132}

The Fibonacci (Yang-Lee) model that we have studied is obtained by truncating $\text{SU}(2)_3$, further, eliminating the noninteger labels $\frac{1}{2}$ and $\frac{3}{2}$ (i.e., this is the Chern-Simons theory $\text{SO}(3)_3$); then the only remaining nontrivial fusion rule is $1 \times 1 = 0 + 1$.

Wang (unpublished) has recently constructed all anyon models with no more than four labels, and has found that all of the models are closely related to the models that are found in Chern-Simons theory.

### 9.18.2 S-matrix

The *modular S-matrix* of an anyon model can be defined in terms of two anyon world lines that form a *Hopf link*:

– Figure: Boxed formula for S-matrix: $S_a^b = \frac{1}{\mathcal{D}}$ times Hopf link of loop $a$ (red) and loop $b$ (blue) –

Here $\mathcal{D}$ is the total quantum dimension of the model, and we have used the normalization where unlinked loops would have the value $d_a d_b$; then the matrix $S_a^b$ is symmetric and unitary. In abelian anyon models, the Hopf link arose in our discussion of topological degeneracy, where we characterized how the vacuum state of an anyon model on the torus is affected when an anyon is transported around one of the cycles of the torus. The $S$-matrix has a similar interpretation in the nonabelian case.

By elementary reasoning, $S$ can be related to the fusion rules:

$$
(N_a)_b^c = \sum_d S_b^d \left(\frac{S_a^d}{S_1^d}\right) (S^{-1})_d^c;
$$ {#eq-8.133}

<!-- Page 65 -->
that is, the $S$-matrix simultaneously *diagonalizes* all the matrices $\{N_a\}$ (the *Verlinde relation*). Note that it follows from the definition that $S_1^a = d_a / \mathcal{D}$.

### 9.18.3 Edge excitations

In our formulation of anyon models, we have discussed the fusing and braiding of particles in the two-dimensional *bulk*. But there is another aspect of the physics of two-dimensional media that we have not yet discussed, the properties of the one-dimensional *edge* of the sample. Typically, if a two-dimensional system supports anyons in the bulk, there are also *chiral massless excitations* that propagate along the one-dimensional edge. At nonzero temperature $T$, there is an energy flux along the edge given by the expression

$$
J = \frac{\pi}{12} c_- T^2;
$$ {#eq-8.134}

here the constant $c_-$, called the *chiral central charge* of the edge, is a universal property that is unaffected by small changes in the underlying Hamiltonian of the system.

While this chiral central charge is an intrinsic property of the two-dimensional medium, the properties of the anyons in the bulk do not determine it completely; rather we have

$$
\frac{1}{\mathcal{D}} \sum_a d_a^2 e^{2\pi i J_a} = e^{(2\pi i/8) c_-},
$$ {#eq-8.135}

where the sum is over the complete label set of the anyon model, and $e^{2\pi i J_a} = R_{a\bar{a}}^1$ is the topological spin of the label $a$. This expression relates the quantity $c_-$, characteristic of the edge theory, to the quantum dimensions and topological spins of the bulk theory, but determines $c_-$ only modulo 8. Therefore, at least in principle, there can be multiple edge theories corresponding to a single theory of anyons in the bulk.

## 9.19 Bibliographical notes

Some of the pioneering papers on the theory of anyons are reprinted in [1].

What I have called the "nonabelian superconductor" model is often referred to in the literature as the "quantum double," and is studied using the representation theory of Hopf algebras. For a review see [2].

That nonabelian anyons can be used for fault-tolerant quantum computing was first suggested in [3]. This paper also discusses the toric code, and related lattice models that have nonabelian phases. A particular realization of universal quantum computation in a nonabelian superconductor

<!-- Page 66 -->
was discussed in [4, 5]. My discussion of the universal gate set is based on [6], where more general models are also discussed. Other schemes, that make more extensive use of electric charges and that are universal for smaller groups (like $S_3$) are described in [7].

Diagrammatic methods, like those I used in the discussion of the quantum dimension, are extensively applied to derive properties of anyons in [8]. The role of the polynomial equations (pentagon and hexagon equations) in (1+1)-dimensional conformal field theory is discussed in [9].

Simulation of anyons using a quantum circuit is discussed in [10]. Simulation of a universal quantum computer using the anyons of the $\text{SU}(2)_{k=3}$ Chern-Simons theory is discussed in [11]. That the Yang-Lee model is also universal was pointed out in [12].

I did not discuss physical implementations in my lectures, but I list a few relevant references here anyway: Ideas about realizing abelian and nonabelian anyons using superconducting Josephson-junction arrays are discussed in [13]. A spin model with nearest-neighbor interactions that has nonabelian anyons (though not ones that are computationally universal) is proposed and solved in [14], and a proposal for realizing this model using cold atoms trapped in an optical lattice is described in [15]. Some ideas about realizing the (computationally universal) $\text{SU}(2)_{k=3}$ model in a system of interacting electrons are discussed in [16].

Much of my understanding of the theory of computing with nonabelian anyons was derived from many helpful discussions with Alexei Kitaev.

<!-- Page 67 -->
## References

[1] F. Wilczek, *Fractional statistics and anyon superconductivity* (World Scientific, Singapore, 1990).

[2] M. de Wild Propitius and F. A. Bais, "Discrete gauge theories," arXiv: hep-th/9511201 (1995).

[3] A. Yu. Kitaev, "Fault-tolerant quantum computation by anyons," *Annals Phys.* **303**, 2-30 (2003), arXiv: quant-ph/9707021.

[4] R. W. Ogburn and H. Preskill, "Topological quantum computation," *Lect. Notes in Comp. Sci.* **1509**, 341-356 (1999).

[5] J. Preskill, "Fault-tolerant quantum computation," arXiv: quant-ph/9712048 (1997).

[6] C. Mochon, "Anyons from non-solvable finite groups are sufficient for universal quantum computation," *Phys. Rev. A* **67**, 022315 (2003), quant-ph/0206128.

[7] C. Mochon, "Anyon computers with smaller groups," *Phys. Rev. A* **69**, 032306 (2004), arXiv: quant-ph/0306063.

[8] J. Fröhlich and F. Gabbiani, "Braid statistics in local quantum theory," *Rev. Math. Phys.* **2**:3, 251–353 (1990).

[9] G. Moore and N. Seiberg, "Classical and quantum conformal field theory," *Comm. Math. Phys.* **123**, 171–254 (1989).

[10] M. H. Freedman, A. Kitaev, and Z. Wang, "Simulation of topological field theories by quantum computers," *Comm. Math. Phys.* **227**, 587-603 (2002), arXiv: quant-ph/0001071.

[11] M. H. Freedman, M. Larsen, and Z. Wang, "A modular functor which is universal for quantum computation," arXiv: quant-ph/0001108 (2000).

[12] G. Kuperberg, unpublished.

[13] B. Doucot, L. B. Ioffe, and J. Vidal, "Discrete non-Abelian gauge theories in two-dimensional lattices and their realizations in Josephson-junction arrays," *Phys. Rev. B* **69**, 214501 (2004), arXiv: cond-mat/0302104.

<!-- Page 68 -->
[14] A. Kitaev, "Anyons in a spin model on the honeycomb lattice," unpublished.

[15] L.-M. Duan, E. Demler, and M. D. Lukin, "Controlling spin exchange interactions of ultracold atoms in optical lattices," *Phys. Rev. Lett.* **91**, 090402 (2003), arXiv: cond-mat/0210564.

[16] M. Freedman, C. Nayak, K. Shtengel, K. Walker, and Zhenghan Wang, "A class of $P, T$-invariant topological phases of interacting electrons," cond-mat/0307511 (2003).
