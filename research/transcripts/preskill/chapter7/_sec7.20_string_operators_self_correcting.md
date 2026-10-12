# Section 7.20: String Operators and Self-Correcting Codes

**Source:** Preskill Lecture Notes, Chapter 7, pp. 63–65 (Physical pages 69–71).

---

## 7.20.1 2D stabilizer codes have stringlike logical operators

Using the cleaning lemma and the union lemma we can see that any 2D stabilizer code has a nontrivial logical operator supported on a strip of constant width. A similar argument shows that a stabilizer code in $D$ dimensions has a nontrivial logical operator supported on a $(D-1)$-dimensional slab of constant thickness. (Note that the argument does not show that each logical operator is supported on a slab — only that at least one nontrivial logical operator has this structure.)

For qubits arranged on a square, we may argue as follows. Cover the code block with vertical strips, where each strip has constant thickness greater than $r$, the range of the stabilizer generators. Counting from the left edge, color the odd-numbered strips black and the even-numbered strips white. We claim that at least one of these strips supports a nontrivial logical operator. To prove the claim by contradiction, suppose that no nontrivial logical operator is supported on any of the black strips. Thus each black strip is correctable, and because the strips are separated by distance greater than $r$, the union of all black strips is also correctable and therefore cleanable. Consider a nontrivial logical operator; after cleaning this logical operator on the black strips, we obtain a nontrivial logical operator $x$ supported on the union of all white strips. Thus $x$ commutes with all stabilizer generators. Because the white strips are separated by distance greater than $r$, no stabilizer generator has support on more than one strip. It follows that all stabilizer generators commute with the restriction of $x$ to a single strip; that is, $x$ is a product of strip operators, each supported on a vertical strip of constant width, and each of which is logical (commutes with the stabilizer). Because $x$ is a nontrivial logical operator, at least one of these strip operators must be both logical and nontrivial. This contradicts our assumption that no strip supports a nontrivial logical operator, hence proving, as desired, that there is a nontrivial logical operator supported on a single vertical strip with constant thickness.

Of course, we did not need to choose the strips to be vertical. The same argument applies to any way of dividing the code block into regions that can be colored white and black, such that distinct black strips are separated by distance greater than $r$ and distinct white strips are separated by distance greater than $r$. In particular, it follows that there is a nontrivial logical operator supported on a horizontal strip of constant thickness as well.

## 7.20.2 2D local stabilizer codes are not self correcting

Results that specify the geometry of a region that supports a logical operator have implications for the physical robustness of quantum memories.

Consider a stabilizer code with geometrically local generators $\{S_a\}$, where the qubits reside at the sites of a $D$-dimensional hypercubic lattice with linear size $L$. The generating set $\{S_a\}$ might be overcomplete, but we assume that the number of local generators acting nontrivially on each qubit is a constant independent of $L$. The local Hamiltonian
$$
H = -\sum_a \frac{1}{2} (S_a - I),
$$ {#eq-7.253}
has a $2^k$-fold degenerate ground state with energy $E = 0$, where $k$ is the number of protected qubits — each ground state is a simultaneous eigenstate with eigenvalue one of all elements of $\{S_a\}$. If a quantum memory governed by this Hamiltonian is subjected to thermal noise, how well protected is the $2^k$-dimensional code space?

If $|\psi\rangle$ is a zero-energy eigenstate of $H$ and $x$ is a Pauli operator, then $x|\psi\rangle$ is an eigenstate of $H$ with eigenvalue $E(x)$, where $E(x)$ is the number of elements of $\{S_a\}$ that anticommute with $x$. Thermal fluctuations may excite the memory, but excitations with energy cost $E$ are suppressed by the Boltzmann factor $e^{-E/\tau}$ where $\tau$ is the temperature (and Boltzmann's constant $k_B$ has been set to one). We suppose that the environment applies a sequence of weight-one Pauli operators to the system, so that the error history after $t$ steps can be described as a walk on the Pauli group, starting at the identity:
$$
\{x_i \in \mathcal{P}, i = 0, 1, 2, 3, \dots, t\},
$$ {#eq-7.254}
where $x_0 = I$, and $x_{i+1}x_i^{-1}$ has weight one. Let $\mathcal{P}(z)$ denote the set of all such walks, with any number of steps, that start at $I$ and terminate at $z \in \mathcal{P}$. We define
$$
\Delta(z) \equiv \min_{\gamma \in \mathcal{P}(z)} \max_{x \in \gamma} E(x),
$$ {#eq-7.255}
the minimum energy barrier that must be surmounted by any walk that reaches Pauli operator $z$. Thus such walks occur with a probability per unit time suppressed by the Boltzmann factor $e^{-\Delta(z)/\tau}$. We also define
$$
\Delta_{\min} \equiv \min_{x \in S^\perp \setminus S} \Delta(x).
$$ {#eq-7.256}
[^note-eq-7.257]
[^note-eq-7.257]: In the original text, the equation number tag `(7.257)` appears on an empty line following eq.(7.256).

Here $\Delta_{\min}$ is the lowest energy barrier protecting any nontrivial logical operator (representing a nontrivial coset of $S^\perp / S$).

We say that a quantum memory is *self correcting* if $\Delta_{\min}$ grows faster than logarithmically with $L$. In that case *all* nontrivial logical operators are suppressed by a Boltzmann factor whose reciprocal grows super-polynomially with $L$. Though the Pauli walk may not be a particularly accurate description of noise in realistic systems, it allows us to define the notion of barrier height precisely, and to state the criteria for self correction simply. Furthermore, we expect the Boltzmann factor $e^{-\Delta/\tau}$ suppressing the Pauli walk to provide a reasonable (though crude) estimate of the logical error rate for more realistic noise models, assuming that the system attains thermal equilibrium.

Our finding that 2D stabilizer codes always admit strip logical operators has implications regarding the self correction properties of these codes. For any logical operator $x$ supported on a vertical strip of constant width, we may build a Pauli walk that starts at $I$ and ends at $x$ by starting at the bottom of the strip, and then building the vertical string operator row by row. At each stage of this walk, any "excited" local stabilizer generator $S_a$ such that $S_a = -1$ acts only on qubits which are within distance $r$ of the boundary of the walk, where $r$ is the range of the stabilizer generators. The number of such qubits is $O(1)$ and the total number of stabilizer generators acting on these qubits is $O(1)$. Therefore, the energy cost of the partially completed walk, and hence $\Delta_{\min}$, are $O(1)$. We conclude the 2D stabilizer codes are not self correcting.
