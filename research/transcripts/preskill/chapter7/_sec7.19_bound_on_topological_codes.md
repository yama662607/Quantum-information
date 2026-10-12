# Section 7.19: A Bound on Topological Stabilizer Codes

**Source:** Preskill Lecture Notes, Chapter 7, pp. 60–63 (Physical pages 66–69).

---

We say that a stabilizer code family is local if we may choose all stabilizer generators to be geometrically local in $D$ spatial dimensions, for some finite $D$. If in addition the code distance $d$ increases without bound as the code length $n$ increases, we say that the code is topological. For example, if the qubits are arranged in a $D$-dimensional (hyper)cubic lattice, the code is local if each stabilizer generator has its support on a (hyper)cube with side length $r$, where $r$ is a constant independent of the length $n$ of the code. When a code is local in $D$ dimensions, we may call it a $D$-dimensional code, dropping the word "local" which is understood. We say that $r$ is the range of the code generators. Note that for a topological code family, any set of qubits of constant size is correctable for sufficiently large $n$.

Here we prove a bound on the code parameters $[[n, k, d]]$ for two-dimensional (2D) stabilizer codes:
$$
k d^2 = O(n).
$$

The proof of the bound makes use of three lemmas — the cleaning lemma, the union lemma, and the expansion lemma. The cleaning lemma for stabilizer codes asserts that for any correctable set $M$ and logical Pauli operator $x$, we may choose $x$ to be supported on the complement $M^c$ of $M$. That is, for any logical operator $x$ (commuting with the code stabilizer $S$) there exists $y \in S$ such that $xy$ is supported on $M^c$. A proof of the cleaning lemma is provided in the previous section.

## 7.19.1 The union lemma

We say that two sets of qubits are separated if no stabilizer generator has support on both sets. For a 2D code this is ensured if no $r \times r$ square intersects with both sets.

The union lemma says that if $M_1$ and $M_2$ are separated and both are correctable, then their union $M_1 \cup M_2$ is also correctable. We denote this union as $M_1 M_2$. To prove the union lemma by contradiction, suppose that $M_1 M_2$ is not correctable, in which case there exists a nontrivial logical operator $x$ supported on $M_1 M_2$, of the form
$$
x = (y_1)_{M_1} \otimes (y_2)_{M_2} \otimes I_{(M_1 M_2)^c}.
$$ {#eq-7.244}

Because $x$ is logical, it commutes with all stabilizer generators, and since no generator has support on both $M_1$ and $M_2$, it must be that
$$
x_1 = (y_1)_{M_1} \otimes I_{M_2} \otimes I_{(M_1 M_2)^c} \quad \text{and} \quad x_2 = I_{M_1} \otimes (y_2)_{M_2} \otimes I_{(M_1 M_2)^c}
$$ {#eq-7.245}
also commute with all stabilizer generators, and hence are logical. Furthermore, since $x = x_1 x_2$, and $x$ is nontrivial, either $x_1$ or $x_2$ must be nontrivial. This contradicts our assumption that $M_1$ and $M_2$ are correctable, proving the lemma.

An alternative way to formulate the proof is to note that if $x$ is any logical operator, then we can clean either $M_1$ or $M_2$, because both are correctable. But because $M_1$ and $M_2$ are separated, the stabilizer generators that clean $M_1$ do not act on $M_2$, and the stabilizer generators that clean $M_2$ do not act on $M_1$. Therefore we can clean $M_1$ and $M_2$ simultaneously; i.e., we can clean the union $M_1 M_2$. This means that all logical operators can be supported on $(M_1 M_2)^c$, $g((M_1 M_2)^c) = 2k$, and hence by the cleaning lemma $g(M_1 M_2) = 0$. We conclude that $M_1 M_2$ supports no nontrivial logical operators and is therefore correctable.

## 7.19.2 The expansion lemma

The expansion lemma requires a bit more explanation. Let $M'$ denote the support of all stabilizer generators which act nontrivially on $M$. The external boundary $\partial_+ M$ of $M$ is $M' \cap M^c$, and the internal boundary $\partial_- M$ of $M$ is $(M^c)' \cap M$. For a local code with range $r$, we may visualize $\partial_+ M$ as a thin shell surrounding $M$ (with thickness no greater than $r$), while $\partial_- M$ is a thin shell surrounding $M^c$. The expansion lemma specifies conditions under which we can slightly augment the size of a correctable set while preserving its correctability. It asserts the following: Suppose that $M = NA$ (that is, $M = N \cup A$, where $N$ and $A$ are disjoint). Suppose further that $A$ contains $\partial_- M$, and that $N$, $A$, and $\partial_+ M$ are correctable. Then $M$ is correctable.

To prove the expansion lemma by contradiction, suppose that $M$ is not correctable, in which case there is a nontrivial logical Pauli operator $x$ which is supported on $M$. Furthermore, because $A$ is correctable, there is a stabilizer element $y$, which we may choose to be supported on $M'$, such that $z = xy$ is cleaned on $A$:
$$
z = w_N \otimes I_A \otimes v_{\partial_+ M} \otimes I_{(M')^c}.
$$ {#eq-7.246}

Because $z$ is logical, it commutes with all stabilizer generators, and because $A \supseteq \partial_- M$, no stabilizer generator acts nontrivially on both $N = M \setminus A$ and $\partial_+ M$. Therefore, the restriction $z_1$ of $z$ to $N$ is logical, and the restriction $z_2$ of $z$ to $\partial_+ M$ is also logical. Furthermore, since $z = z_1 z_2$ and $z$ is nontrivial, either $z_1$ or $z_2$ must be nontrivial. This contradicts our assumption that $N$ and $\partial_+ M$ are correctable, proving the lemma.

## 7.19.3 The holographic principle

Next, we use the cleaning lemma and expansion lemma to infer the holographic principle for 2D codes, which asserts that, for some constant $\alpha$, any square on the lattice with side length $\ell = \alpha d$ is a correctable set of qubits. Note that this is not obvious, since the number of qubits contained in the square is $\Omega(d^2)$, and hence, for a topological code family becomes much larger than the code distance $d$ (the size of the smallest noncorrectable set) for sufficiently large $n$.

To prove the holographic principle, consider two concentric squares $N$ and $M$, where $N$ has side length $\ell - 4r$, and $M$ has side length $\ell - 2r$; therefore, $M'$ is contained in a square with side length $\ell$, and $A = M \setminus N$ contains $\partial_- M$. The expansion lemma ensures that $M$ is correctable if $N$, $A$, and $\partial_+ M$ are all correctable. By definition of distance a set is correctable if it contains fewer than $d$ qubits, and therefore $\partial_+ M$ and $A$ are both correctable provided that
$$
|\partial_+ M| \le |M'| - |M| \le \ell^2 - (\ell - 2r)^2 < 4r\ell < d.
$$ {#eq-7.247}

Now imagine starting with a small square, with area less than $d$ so that the square is correctable, and gradually increasing the side length step-by-step, where the length grows by $2r$ in each step. According to eq.(7.247), the square continues to be correctable as long as the side length $\ell$ remains less than $d/4r$. This proves the holographic principle. We call this the holographic principle, somewhat whimsically, because if logical information is encoded in the square, then some of that logical information (though perhaps not all) must be accessible near the square's boundary.

## 7.19.4 Applying the decoupling principle

To prove our bound on $[[n, k, d]]$ we need one more result, which applies to more general binary quantum codes, not just to stabilizer codes. Suppose the code block is divided into three regions $ABC$, where $A$ and $B$ are both correctable. Then the number $k$ of encoded qubits can be no larger than $|C|$, the number of qubits in $C$.

We obtain this result from the decoupling principle. Express the code block as $M M^c$, where $M$ is a correctable set and $M^c$ is its complement. Introduce a reference system $R$, of dimension $2^k$, which is maximally entangled with the code's $k$ logical qubits. Consider the Stinespring dilation of erasure channel applied to $M$. The dilation discards $M$, mapping it to the environment $E$; hence we may consider $M$ itself to be the environment of the channel. The decoupling principle asserts that if the erasure channel is correctable, then the marginal density operator for $RM$ is a product state, whose entropy is additive — the reference system is uncorrelated with the erased subsystem:
$$
H(RM) = H(R) + H(M) \implies k = H(M^c) - H(M),
$$ {#eq-7.248}
where in the second equation we have replaced the entropy $H(R)$ of the maximally mixed reference system by its number of qubits $k$, and have used the feature that the state of $R M M^c$ is pure, hence $H(RM) = H(M^c)$.

Now, recalling that $A$ is correctable we apply eq.(7.248) to $M = A$ and its complement $M^c = BC$, obtaining
$$
k = H(BC) - H(A) \le H(B) + H(C) - H(A).
$$ {#eq-7.249}

Likewise, since $B$ is also correctable, we apply eq.(7.248) to $M = B$ and its complement $M^c = AC$, obtaining
$$
k = H(AC) - H(B) \le H(A) + H(C) - H(B).
$$ {#eq-7.250}

Combining these two inequalities we find
$$
k \le H(C) \le |C|,
$$ {#eq-7.251}
as desired.

## 7.19.5 Proof of the bound

Now we are ready to prove our bound on 2D topological codes. For a 2D stabilizer code, consider partitioning the code block into three sets $ABC$ as shown here:

Each connected component of $A$ is a square with side length less than $d/4r$, with corners clipped off as shown, and same for $B$. Each connected component of $C$ has constant size, but is sufficiently large to separate the components of $A$ by a distance larger than the range $r$ of the stabilizer generators (and same for $B$). By the holographic principle, each component of $A$ is correctable, and because the components are separated, $A$ is correctable by the union lemma. Likewise, $B$ is also correctable. The number of components of $C$ is $O(n/d^2)$, and each component has constant size. We conclude that
$$
k \le |C| = O(n/d^2),
$$ {#eq-7.252}
which proves the bound. Though in the figure we have not indicated any holes punched through the code block, adding holes would not modify the conclusion.

We can also see that the bound is tight — 2D code families exist with $kd^2$ linear in $n$. To show this, consider a planar surface code defined on a rectangle with $k$ holes punched through it, and with boundary conditions such that $e$ anyons can "condense" (i.e., disappear) at any boundary. Nontrivial logical operators are $e$ strings that connect distinct boundaries, and $m$ strings that enclose one or more holes. The code distance (the smallest weight of a nontrivial logical operator) will be at least $d$ if each hole has a perimeter at least $d$, and no two boundaries are closer together than distance $d$. We can easily arrange $k$ square holes, each with side length $d/4$ such that all holes are distance $d$ apart, and also distance $d$ from the outer boundary, on a rectangular lattice $2d$ sites high and $2kd$ sites wide, hence with $4kd^2$ sites; the corresponding surface code has $n = O(kd^2)$ physical qubits.

Our bound shows that a 2D code family cannot be "good" — it cannot have both $k$ and $d$ scaling linearly with $n$. In fact, if $k$ scales linearly with $n$, then the distance $d$ must be a constant. To do better, we need to either allow non-Euclidean geometry, or to allow stabilizer generators that are not geometrically local.
