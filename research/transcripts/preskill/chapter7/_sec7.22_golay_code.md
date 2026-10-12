# Section 7.22: The Golay Code

**Source:** Preskill Lecture Notes, Chapter 7, pp. 68–70 (Physical pages 74–76).

---

From the perspective of pure mathematics, the most important error-correcting code (classical or quantum) ever discovered is also one of the first ever described in a published article — the Golay code. Here we will briefly describe the Golay code, as it too can be transformed into a nice QECC via the CSS construction. (Perhaps this QECC is not really important enough to deserve a section of this chapter; still, I have included it just for fun.)

The (extended) Golay code is a self-dual $[24, 12, 8]$ classical code. If we puncture it (remove any one of its 24 bits), we obtain the $[23, 12, 7]$ Golay code, which can correct three errors. This code is actually perfect, as it saturates the sphere-packing bound:
$$
1 + \binom{23}{1} + \binom{23}{2} + \binom{23}{3} = 2^{11} = 2^{23-12} .
$$ {#eq-7.277}
In fact, perfect codes that correct more than one error are extremely rare. It can be shown[^fn-golay-perfect] that the *only* perfect codes (linear or nonlinear) over *any* finite field that can correct more than one error are the $[23, 12, 7]$ code and one other code discovered by Golay, with parameters $[11, 6, 5]$ (which is a ternary code over $\mathbb{F}_3$).

[^fn-golay-perfect]: MacWilliams and Sloane §6.10.

The $[24, 12, 8]$ Golay code has a very intricate symmetry. The symmetry is characterized by its automorphism group — the group of permutations of the 24 bits that take codewords to codewords. This is the Mathieu group $M_{24}$, a sporadic simple group of order 244,823,040 that was discovered in the 19th century.

The $2^{12} = 4096$ codewords have the weight distribution (in an obvious notation)
$$
0^1 8^{759} 12^{2576} 16^{759} 24^1 .
$$ {#eq-7.278}
Note in particular that each weight is a multiple of 4 (the code is doubly even). What is the significance of the number $759 (= 3 \cdot 11 \cdot 23)$? In fact it is
$$
\binom{24}{5} \Big/ \binom{8}{5} = 759 ,
$$ {#eq-7.279}
and it arises for this combination reason: with each weight-8 codeword we associate the eight-element set ("octad") where the codeword has its support. Each 5-element subset of the 24 bits is contained in exactly one octad (a reflection of the code's large symmetry).

What makes the Golay code important in mathematics? Its discovery in 1949 set in motion a sequence of events that led, by around 1980, to a complete classification of the finite simple groups. This classification is one of the greatest achievements of 20th century mathematics.

(A group is simple if it contains no nontrivial normal subgroup. The finite simple groups may be regarded as the building blocks of all finite groups in the sense that for any finite group $G$ there is a unique decomposition of the form
$$
G \equiv G_0 \supseteq G_1 \supseteq G_2 \supseteq \dots \supseteq G_n ,
$$ {#eq-7.280}
where each $G_{j+1}$ is a normal subgroup of $G_j$, and each quotient group $G_j/G_{j+1}$ is simple. The finite simple groups can be classified into various infinite families, plus 26 additional "sporadic" simple groups that resist classification.)

The Golay code led Leech, in 1964, to discover an extraordinarily close packing of spheres in 24 dimensions, known as the *Leech Lattice* $\Lambda$. The lattice points (the centers of the spheres) are 24-component integer-valued vectors with these properties: to determine if $\vec{x} = (x_1, x_2, \dots, x_{24})$ is contained in $\Lambda$, write each component $x_j$ in binary notation,
$$
x_j = \dots x_{j3} x_{j2} x_{j1} x_{j0} .
$$ {#eq-7.281}
Then $\vec{x} \in \Lambda$ if
(i) The $x_{j0}$'s are either all 0's or all 1's.
(ii) The $x_{j2}$'s are an even parity 24-bit string if the $x_{j0}$'s are 0, and an odd parity 24-bit string if the $x_{j0}$'s are 1.
(iii) The $x_{j1}$'s are a 24-bit string contained in the Golay code.

When these rules are applied, a negative number is represented by its binary complement, e.g.
$$
\begin{aligned}
-1 &= \dots 11111 , \\
-2 &= \dots 11110 , \\
-3 &= \dots 11101 , \\
&\quad \text{etc.}
\end{aligned}
$$ {#eq-7.282}

We can easily check that $\Lambda$ is a lattice; that is, it is closed under addition. (Bits other than the last three in the binary expansion of the $x_j$'s are unrestricted).

We can now count the number of nearest neighbors to the origin (or the number of spheres that touch any given sphere). These points are all $(\text{distance})^2 = 32$ away from the origin:
$$
\begin{aligned}
(\pm 2)^8 &: 2^7 \cdot 759 \\
(\pm 3)(\mp 1)^{23} &: 2^{12} \cdot 24 \\
(\pm 4)^2 &: 2^2 \cdot \binom{24}{2} .
\end{aligned}
$$ {#eq-7.283}
That is, there are $759 \cdot 2^7$ neighbors that have eight components with the values $\pm 2$ — their support is on one of the 759 weight-8 Golay codewords, and the number of $-$ signs must be even. There are $2^{12} \cdot 24$ neighbors that have one component with value $\pm 3$ (this component can be chosen in 24 ways) and the remaining 23 components have the value $(\mp 1)$. If, say, $+3$ is chosen, then the position of the $+3$, together with the position of the $-1$'s, can be any of the $2^{11}$ Golay codewords with value 1 at the position of the $+3$. There are $2^2 \cdot \binom{24}{2}$ neighbors with two components each taking the value $\pm 4$ (the signs are unrestricted). Altogether, the coordination number of the lattice is $196,560$.

The Leech lattice has an extraordinary automorphism group discovered by Conway in 1968. This is the finite subgroup of the 24-dimensional rotation group $SO(24)$ that preserves the lattice. The order of this finite group (known as $\cdot 0$, or "dot oh") is
$$
2^{22} \cdot 3^9 \cdot 5^4 \cdot 7^2 \cdot 11 \cdot 13 \cdot 23 = 8,315,553,613,086,720,000 \simeq 8.3 \times 10^{18} .
$$ {#eq-7.284}
If its two element center is modded out, the sporadic simple group $\cdot 1$ is obtained. At the time of its discovery, $\cdot 1$ was the largest of the sporadic simple groups that had been constructed.

The Leech lattice and its automorphism group eventually (by a route that won't be explained here) led Griess in 1982 to the construction of the most amazing sporadic simple group of all (whose existence had been inferred earlier by Fischer and Griess). It is a finite subgroup of the rotation group in 196,883 dimensions, whose order is approximately $8.08 \times 10^{53}$. This behemoth known as $F_1$ has earned the nickname "the monster" (though Griess prefers to call it "the friendly giant".) It is the largest of the sporadic simple groups, and the last to be discovered.

Thus the classification of the finite simple groups owes much to (classical) coding theory, and to the Golay code in particular. Perhaps the theory of QECC's can also bequeath to mathematics something of value and broad interest!

Anyway, since the (extended) $[24, 12, 8]$ Golay code is self-dual, the $[23, 12, 7]$ code obtained by puncturing it is weakly self-dual; its $[23, 11, 8]$ dual is its even subcode. From it, a $[[23, 1, 7]]$ QECC can be constructed by the CSS method. This code is not the most efficient quantum code that can correct three errors (there is a $[[17, 1, 7]]$ code that saturates the Rains bound), but it has especially nice properties that are conducive to fault-tolerant quantum computation, as we will see in Chapter 8.

