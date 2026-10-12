# Section 5.2: Reversible computation [PDF Pages 13-22]

<!-- ============================================================ -->
<!-- Source: chap5.pdf, Physical Pages: 13-22                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 13 -->
## 5.2 Reversible computation

In devising a model of a quantum computer, we will generalize the circuit model of classical computation. But our quantum logic gates will be unitary transformations, and hence will be invertible, while classical logic gates like the AND gate are not invertible. Before we discuss quantum circuits, it is useful to consider some features of *reversible* classical computation.

### 5.2.1 Landauer's principle

Aside from providing a bridge to quantum computation, classical reversible computing is interesting in its own right, because of *Landauer's principle*. Landauer observed that erasure of information is necessarily a

<!-- Page 14 -->
*dissipative* process. His insight is that erasure always involves the compression of phase space, and so is thermodynamically, as well as logically, irreversible.

For example, I can store one bit of information by placing a single molecule in a box, either on the left side or the right side of a partition that divides the box. Erasure means that we move the molecule to the right side (say) irrespective of whether it started out on the left or right. I can suddenly remove the partition, and then slowly compress the one-molecule "gas" with a piston until the molecule is definitely on the right side. This procedure changes the entropy of the gas by $\Delta S = -k \ln 2$ (where $k$ is Boltzmann's constant) and there is an associated flow of heat from the box to its environment. If the process is quasi-static and isothermal at temperature $T$, then work $W = -kT\Delta S = kT \ln 2$ is performed on the box, work that I have to provide. If I erase information, someone has to pay the power bill.

Landauer also observed that, because irreversible logic elements erase information, they too are necessarily dissipative, and therefore require an unavoidable expenditure of energy. For example, an AND gate maps two input bits to one output bit, with 00, 01, and 10 all mapped to 0, while 11 is mapped to one. If the input is destroyed and we can read only the output, then if the output is 0 we don't know for sure what the input was — there are three possibilities. If the input bits are chosen uniformly at random, than on average the AND gate destroys $\frac{3}{4}\log_2 3 \approx 1.189$ bits of information. Indeed, if the input bits are uniformly random any 2-to-1 gate must "erase" at least one bit on average. According to Landauer's principle, then, we need to do an amount of work at least $W = kT \ln 2$ to operate a 2-to-1 logic gate at temperature $T$.

But if a computer operates reversibly, then in principle there need be no dissipation and no power requirement. We can compute for free! At present this idea is not of great practical importance, because the power consumed in today's integrated circuits exceeds $kT$ per logic gate by at least three orders of magnitude. As the switches on chips continue to get smaller, though, reversible computing might eventually be invoked to reduce dissipation in classical computing hardware.

### 5.2.2 Reversible gates

A reversible computer evaluates an invertible function taking $n$ bits to $n$ bits
$$
f : \{0, 1\}^n \to \{0, 1\}^n.
$$ {#eq-5.26}
An invertible function has a unique input for each output, and we can run the computation backwards to recover the input from the output. We

<!-- Page 15 -->
may regard an invertible function as a permutation of the $2^n$ strings of $n$ bits — there are $(2^n)!$ such functions. If we did not insist on invertibility, there would be $(2^{2^n})^n = (2^n)^{2^n}$ functions taking $n$ bits to $n$ bits (the number of ways to choose $n$ Boolean functions); using the Stirling approximation, $(2^n)! \approx (2^n/e)^{2^n}$, we see that the fraction of all functions which are invertible is quite small, about $e^{-2^n}$.

Any irreversible computation can be "packaged" as an evaluation of an invertible function. For example, for any $f : \{0, 1\}^n \to \{0, 1\}$, we can construct $\tilde{f} : \{0, 1\}^{n+1} \to \{0, 1\}^{n+1}$ such that
$$
\tilde{f}(x, y) = (x, y \oplus f(x)).
$$ {#eq-5.27}
Here $y$ is a bit and $\oplus$ denotes the XOR gate (addition mod 2) — the $n$-bit input $x$ is preserved and the last bit flips iff $f(x) = 1$. Applying $\tilde{f}$ a second time undoes this bit flip; hence $\tilde{f}$ is invertible, and equal to its own inverse. If we set $y = 0$ initially and apply $\tilde{f}$, we can read out the value of $f(x)$ in the last output bit.

Just as for Boolean functions, we can ask whether a complicated reversible computation can be executed by a circuit built from simple components — are there universal reversible gates? It is easy to see that one-bit and two-bit reversible gates do not suffice; we will need three-bit gates for universal reversible computation.

Of the four 1-bit $\to$ 1-bit gates, two are reversible; the trivial gate and the NOT gate. Of the $(2^4)^2 = 256$ possible 2-bit $\to$ 2-bit gates, $4! = 24$ are reversible. One of special interest is the controlled-NOT (CNOT) or reversible XOR gate that we already encountered in Chapter 4:
$$
\text{XOR} : (x, y) \mapsto (x, x \oplus y),
$$ {#eq-5.28}
This gate flips the second bit if the first is 1, and does nothing if the first bit is 0 (hence the name controlled-NOT). Its square is trivial; hence it inverts itself. Anticipating the notation that will be convenient for our discussion of quantum gates, we will sometimes use $\Lambda(\boldsymbol{X})$ to denote the CNOT gate. More generally, by $\Lambda(\boldsymbol{G})$ we mean a gate that applies the operation $\boldsymbol{G}$ to a "target" conditioned on the value of a "control bit;" $\boldsymbol{G}$ is applied if the control bit is 1 and the identity is applied if the control bit is 0. In the case of the CNOT gate, $\boldsymbol{G}$ is the Pauli operator $\boldsymbol{X}$, a bit flip.

<!-- Page 16 -->
The CNOT gate performs a NOT on the second bit if the first bit $x$ is set to 1, and it performs the copy operation if $y$ is initially set to zero:
$$
\text{CNOT} : (x, 0) \mapsto (x, x).
$$ {#eq-5.29}
With the circuit constructed from three XOR's, we can swap two bits:
$$
(x, y) \to (x, x \oplus y) \to (y, x \oplus y) \to (y, x).
$$ {#eq-5.30}
With these swaps we can shuffle bits around in a circuit, bringing them together if we want to act on them with a "local gate" at a fixed location.

To see that the one-bit and two-bit gates are nonuniversal, we observe that all these gates are *linear*. Each reversible two-bit gate has an action of the form
$$
\begin{pmatrix} x \\ y \end{pmatrix} \mapsto \begin{pmatrix} x' \\ y' \end{pmatrix} = M \begin{pmatrix} x \\ y \end{pmatrix} + \begin{pmatrix} a \\ b \end{pmatrix};
$$ {#eq-5.31}
the pair of bits $\begin{pmatrix} a \\ b \end{pmatrix}$ can take any one of four possible values, and the matrix $M$ is one of the six invertible matrices with binary entries
$$
\begin{aligned}
M = &\begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}, \\
&\begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}, \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}, \begin{pmatrix} 1 & 1 \\ 1 & 0 \end{pmatrix}.
\end{aligned}
$$ {#eq-5.32}
(All addition is performed modulo 2.) Combining the six choices for $M$ with the four possible constants, we obtain 24 distinct gates, exhausting all the reversible $2 \to 2$ gates.

Since the linear transformations are closed under composition, any circuit composed from reversible $2 \to 2$ (and $1 \to 1$) gates will compute a linear function
$$
x \mapsto Mx + a.
$$ {#eq-5.33}
But for $n \ge 3$, there are invertible functions on $n$-bits that are nonlinear. An important example is the 3-bit *Toffoli gate* (or controlled-controlled-NOT) $\Lambda^2(\boldsymbol{X})$
$$
\Lambda^2(\boldsymbol{X}) : (x, y, z) \to (x, y, z \oplus xy);
$$ {#eq-5.34}

<!-- Page 17 -->
it flips the third bit if the first two are 1 and does nothing otherwise, thus invoking the (nonlinear) multiplication of the two bits $x$ and $y$. The $\Lambda^2(\cdot)$ notation indicates that the operation acting on the target bit is triggered only if both control bits are set to 1. Like the CNOT gate $\Lambda(\boldsymbol{X})$, $\Lambda^2(\boldsymbol{X})$ is its own inverse.

Unlike the reversible 2-bit gates, the Toffoli gate serves as a universal gate for Boolean logic, if we can provide constant input bits and ignore output bits. If we fix $x = y = 1$, then the Toffoli gate performs NOT acting on the third bit, and if $z$ is set to zero initially, then the Toffoli gate outputs $z = x \wedge y$ in the third bit. Since NOT/AND/OR are a universal gate set, and we can construct OR from NOT and AND ($x \vee y = \neg(\neg x \wedge \neg y)$), this is already enough to establish that the Toffoli gate is universal. Note also that if we fix $x = 1$ the Toffoli gate functions like a CNOT gate acting on $y$ and $z$; we can use it to copy.

The Toffoli gate $\Lambda^2(\boldsymbol{X})$ is also universal in the sense that we can build a circuit to compute any reversible function using Toffoli gates alone (if we can fix input bits and ignore output bits). It will be instructive to show this directly, without relying on our earlier argument that NOT/AND/OR is universal for Boolean functions. Specifically, we can show the following: From the NOT gate and the Toffoli gate $\Lambda^2(\boldsymbol{X})$, we can construct any invertible function on $n$ bits, provided we have one extra bit of scratchpad space available.

The first step is to show that from the three-bit Toffoli-gate $\Lambda^2(\boldsymbol{X})$ we can construct an $n$-bit Toffoli gate $\Lambda^{n-1}(\boldsymbol{X})$ that acts as
$$
(x_1, x_2, \dots, x_{n-1}, y) \to (x_1, x_2, \dots, x_{n-1}, y \oplus x_1 x_2 \dots x_{n-1})
$$ {#eq-5.35}
using one extra bit of scratch space. For example, we construct $\Lambda^3(\boldsymbol{X})$ from $\Lambda^2(\boldsymbol{X})$'s with the circuit:

<!-- Page 18 -->
The purpose of the last $\Lambda^2(\boldsymbol{X})$ gate is to reset the scratch bit back to its original value 0. Actually, with one more gate we can obtain an implementation of $\Lambda^3(\boldsymbol{X})$ that works irrespective of the initial value of the scratch bit:

We can see that the scratch bit really is necessary, because $\Lambda^3(\boldsymbol{X})$ is an odd permutation (in fact a transposition) of the 4-bit strings — it transposes 1111 and 1110. But $\Lambda^2(\boldsymbol{X})$ acting on any three of the four bits is an even permutation; e.g., acting on the last three bits it transposes both 0111 with 0110 and 1111 with 1110. Since a product of even permutations is also even, we cannot obtain $\Lambda^3(\boldsymbol{X})$ as a product of $\Lambda^2(\boldsymbol{X})$'s that act only on the four bits.

This construction of $\Lambda^3(\boldsymbol{X})$ from four $\Lambda^2(\boldsymbol{X})$'s generalizes immediately to the construction of $\Lambda^{n-1}(\boldsymbol{X})$ from two $\Lambda^{n-2}(\boldsymbol{X})$'s and two $\Lambda^2(\boldsymbol{X})$'s (just expand $x_1$ to several control bits in the above diagram). Iterating the construction, we obtain $\Lambda^{n-1}(\boldsymbol{X})$ from a circuit with $2^{n-2} + 2^{n-3} - 2$ $\Lambda^2(\boldsymbol{X})$'s. Furthermore, just one bit of scratch suffices. (With more scratch space, we can build $\Lambda^{n-1}(\boldsymbol{X})$ from $\Lambda^2(\boldsymbol{X})$'s much more efficiently — see Exercise 5.1.)

The next step is to note that, by conjugating $\Lambda^{n-1}(\boldsymbol{X})$ with NOT gates, we can in effect modify the value of the control string that "triggers" the gate. For example, the circuit

<!-- Page 19 -->
flips the value of $y$ if $x_1 x_2 x_3 = 010$, and it acts trivially otherwise. Thus this circuit transposes the two strings 0100 and 0101. In like fashion, with $\Lambda^{n-1}(\boldsymbol{X})$ and NOT gates, we can devise a circuit that transposes any two $n$-bit strings that differ in only one bit. (The location of the bit where they differ is chosen to be the *target* of the $\Lambda^{n-1}(\boldsymbol{X})$ gate.)

But in fact a transposition that exchanges any two $n$-bit strings can be expressed as a product of transpositions that interchange strings that differ in only one bit. If $a_0$ and $a_s$ are two strings that are Hamming distance $s$ apart (differ in $s$ places), then there is a sequence of strings
$$
a_0, a_1, a_2, a_3, \dots, a_s,
$$ {#eq-5.36}
such that each string in the sequence is Hamming distance one from its neighbors. Therefore, each of the transpositions
$$
(a_0 a_1), (a_1 a_2), (a_2 a_3), \dots, (a_{s-1} a_s),
$$ {#eq-5.37}
can be implemented as a $\Lambda^{n-1}(\boldsymbol{X})$ gate conjugated by NOT gates. By composing transpositions we find
$$
\begin{aligned}
(a_0 a_s) = (a_{s-1} a_s)(a_{s-2} a_{s-1}) &\dots (a_2 a_3)(a_1 a_2)(a_0 a_1)(a_1 a_2)(a_2 a_3) \\
&\dots (a_{s-2} a_{s-1})(a_{s-1} a_s);
\end{aligned}
$$ {#eq-5.38}
we can construct the Hamming-distance-$s$ transposition from $2s - 1$ Hamming-distance-one transpositions. It follows that we can construct $(a_0 a_s)$ from $\Lambda^{n-1}(\boldsymbol{X})$'s and NOT gates.

Finally, since every permutation is a product of transpositions, we have shown that every invertible function on $n$-bits (every permutation of the $n$-bit strings) is a product of $\Lambda^{n-1}(\boldsymbol{X})$'s and NOT's, using just one bit of scratch space.

Of course, a NOT can be performed with a $\Lambda^2(\boldsymbol{X})$ gate if we fix two input bits at 1. Thus the Toffoli gate $\Lambda^2(\boldsymbol{X})$ is universal for reversible computation, if we can fix input bits and discard output bits.

<!-- Page 20 -->
### 5.2.3 Saving space: the pebble game

We have seen that with Toffoli and NOT gates we can compute any invertible function using very little scratch space, and also that by fixing constant input bits and ignoring output bits, we can simulate any (irreversible) Boolean circuit using only reversible Toffoli gates. In the latter case, though, we generate two bits of junk every time we simulate an AND gate. Our memory gradually fills with junk, until we reach the stage where we cannot continue with the computation without erasing some bits to clear some space. At that stage, we will finally have to pay the power bill for the computing we have performed, just as Landauer had warned.

Fortunately, there is a general procedure for simulating an irreversible circuit using reversible gates, in which we can erase the junk without using any power. We accumulate and save all the junk output bits as the simulation proceeds, and when we reach the end of the computation we make a copy of the output. The COPY operation, which is logically reversible, can be done with a CNOT or Toffoli gate. Then we run the full computation in reverse, executing the circuit in the opposite order and replacing each gate by its inverse. This procedure cleans up all the junk bits, and returns all registers to their original settings, without any irreversible erasure steps. Yet the result of the computation has been retained, because we copied it before reversing the circuit.

Because we need to run the computation both forward and backward, the reversible simulation uses roughly twice as many gates as the irreversible circuit it simulates. Far worse than that, this simulation method requires a substantial amount of memory, since we need to be able to store about as many bits as the number of gates in the circuit before we finally start to clear the memory by reversing the computation.

It is possible, though, at the cost of modestly increasing the simulation time, to substantially reduce the space required. The trick is to clear space during the course of the simulation by running a part of the computation backward. The resulting tradeoff between time and space is worth discussing, as it illustrates both the value of "uncomputing" and the concept of a recursive simulation.

We imagine dividing the computation into steps of roughly equal size. When we run step $k$ forward, the first thing we do is make a copy of the output from the previous step, then we execute the gates of step $k$, retaining all the junk accumulated by those gates. We cannot run step $k$ forward unless we have previously completed step $k - 1$. Furthermore, we will not be able to run step $k$ backward if we have already run step $k - 1$ backward. The trouble is that we will not be able to reverse the COPY step at the very beginning of step $k$ unless we have retained the output

<!-- Page 21 -->
from step $k - 1$.

To save space in our simulation we want to minimize at all times the number of steps that have already been computed but have not yet been uncomputed. The challenge we face can be likened to a game — the *reversible pebble game*. The steps to be executed form a one-dimension directed graph with sites labeled $1, 2, 3, \dots, T$. Execution of step $k$ is modeled by placing a pebble on the $k$th site of the graph, and executing step $k$ in reverse is modeled as removal of a pebble from site $k$. At the beginning of the game, no sites are covered by pebbles, and in each turn we add or remove a pebble. But we cannot place a pebble at site $k$ (except for $k = 1$) unless site $k - 1$ is already covered by a pebble, and we cannot remove a pebble from site $k$ (except for $k = 1$) unless site $k - 1$ is covered. The object is to cover site $T$ (complete the computation) without using more pebbles than necessary (generating a minimal amount of garbage).

We can construct a recursive procedure that enables us to reach site $t = 2^n$ using $n + 1$ pebbles and leaving only one pebble in play. Let $F_1(k)$ denote placing a pebble at site $k$, and $F_1(k)^{-1}$ denote removing a pebble from site $k$. Then
$$
F_2(1, 2) = F_1(1)F_1(2)F_1(1)^{-1},
$$ {#eq-5.39}
leaves a pebble at site $k = 2$, using a maximum of two pebbles at intermediate stages. Similarly
$$
F_3(1, 4) = F_2(1, 2)F_2(3, 4)F_2(1, 2)^{-1},
$$ {#eq-5.40}
reaches site $k = 4$ using three pebbles, and
$$
F_4(1, 8) = F_3(1, 4)F_3(5, 8)F_3(1, 4)^{-1},
$$ {#eq-5.41}
reaches $k = 8$ using four pebbles. Proceeding this way we construct $F_n(1, 2^n)$ which uses a maximum of $n + 1$ pebbles and leaves a single pebble in play.

Interpreted as a routine for simulating $T_{\text{irr}} = 2^n$ steps of an irreversible computation, this strategy for playing the pebble game represents a reversible simulation requiring space $S_{\text{rev}}$ scaling like
$$
S_{\text{rev}} \approx S_{\text{step}} \log_2(T_{\text{irr}}/T_{\text{step}}),
$$ {#eq-5.42}
where $T_{\text{step}}$ is the number of gates is a single step, and $S_{\text{step}}$ is the amount of memory used in a single step. How long does the simulation take? At each level of the recursive procedure described above, two steps forward are replaced by two steps forward and one step back. Therefore, an irreversible computation with $T_{\text{irr}}/T_{\text{step}} = 2^n$ steps is simulated in $T_{\text{rev}}/T_{\text{step}} = 3^n$ steps, or
$$
T_{\text{rev}} = T_{\text{step}}(T_{\text{irr}}/T_{\text{step}})^{\log 3 / \log 2} = T_{\text{step}}(T_{\text{irr}}/T_{\text{step}})^{1.58},
$$ {#eq-5.43}
a modest power law slowdown.

<!-- Page 22 -->
We can improve this slowdown to
$$
T_{\text{rev}} \sim (T_{\text{irr}})^{1+\varepsilon},
$$ {#eq-5.44}
for any $\varepsilon > 0$. Instead of replacing two steps forward with two forward and one back, we replace $\ell$ forward with $\ell$ forward and $\ell - 1$ back. A recursive procedure with $n$ levels reaches site $\ell^n$ using a maximum of $n(\ell - 1) + 1$ pebbles. Now we have $T_{\text{irr}} \propto \ell^n$ and $T_{\text{rev}} \propto (2\ell - 1)^n$, so that
$$
T_{\text{rev}} = T_{\text{step}}(T_{\text{irr}}/T_{\text{step}})^{\log(2\ell-1)/\log \ell};
$$ {#eq-5.45}
the power characterizing the slowdown is
$$
\frac{\log(2\ell - 1)}{\log \ell} = \frac{\log 2\ell + \log(1 - \frac{1}{2\ell})}{\log \ell} \simeq 1 + \frac{\log 2}{\log \ell} \equiv 1 + \varepsilon,
$$ {#eq-5.46}
and the space requirement scales as
$$
S_{\text{rev}}/S_{\text{step}} \approx \ell n \approx 2^{1/\varepsilon}\log_\ell(T_{\text{irr}}/T_{\text{step}}) \approx \varepsilon 2^{1/\varepsilon}\log_2(T_{\text{irr}}/T_{\text{step}}),
$$ {#eq-5.47}
where $1/\varepsilon = \log_2 \ell$. The required space still scales as $S_{\text{rev}} \sim \log T_{\text{irr}}$, yet the slowdown is no worse than $T_{\text{rev}} \sim (T_{\text{irr}})^{1+\varepsilon}$. By using more than the minimal number of pebbles, we can reach the last step faster.

You might have worried that, because reversible computation is "harder" than irreversible computation, the classification of complexity depends on whether we compute reversibly or irreversibly. But don't worry — we've now seen that a reversible computer can simulate an irreversible computer pretty easily.
