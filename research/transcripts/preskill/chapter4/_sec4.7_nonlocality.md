# Section 4.7: Nonlocality without entanglement (Transcript)

Source: `quarto/assets/pdf/preskill/chap4.pdf`, pages 45–48

## 4.7 Nonlocality without entanglement [p.45]

Quantum entanglement typifies the principle that there are bipartite quantum operations that cannot be implemented using only local operations and classical communication (LOCC). For example, if Alice and Bob share no prior entanglement, they cannot perform Bell measurement or prepare the entangled state $|\phi^+\rangle_{AB}$ unless they get together. Now we will encounter an interesting surprise: some things that Alice and Bob are unable to do with LOCC do *not* involve quantum entanglement, at least not directly.

Consider a game played by Alice, Bob, and Charlie. Charlie prepares a state $|\psi_i\rangle_{AB}$ selected from an ensemble of mutually orthogonal bipartite states, and distributes $|\psi_i\rangle_{AB}$ to Alice and Bob. To win the game, Alice and Bob must identify the state that Charlie prepared. Of course, if Alice and Bob were permitted to unite, they could perform an orthogonal measurement that would identify the state with certainty, and they would be able to win every time. But the rules of the game require Alice and Bob to stay separated, and they are forbidden to exchange quantum information — only LOCC is allowed. Thus, if Charlie's ensemble includes entangled states, Alice and Bob won't be able to win in general.

To make things easier for Alice and Bob, let's impose a new rule: Charlie is required to prepare a product state
$$
|\psi\rangle_{AB} = |\alpha_i\rangle_A \otimes |\beta_i\rangle_B .
$$ (4.128)

Now, since Alice has a pure state, and so does Bob, we might expect them to be able to devise a winning strategy. But on further reflection, this is not so obvious. Though the states $\{|\psi_i\rangle_{AB}\}$ in Charlie's ensemble are mutually orthogonal, the states $\{|\alpha_i\rangle_A\}$ that Alice could receive need not be mutually orthogonal, and the same is true of the states $\{|\beta_i\rangle_B\}$ that Bob could receive.

Indeed, even under the new rules, there is no winning strategy for Alice and Bob in general. Though Charlie sends a pure state to Alice and a pure state to Bob, there is no way for Alice and Bob, using LOCC, to fully decipher the message that Charlie has sent to them. This phenomenon is called *nonlocality without entanglement*.

The best way to understand nonlocality without entanglement is to consider an example. Suppose that Alice and Bob share a pair of qutrits (3-level quantum systems), and denote the three elements of an orthonormal basis for the qutrit by $\{|0\rangle, |1\rangle, |2\rangle\}$. In a streamlined notation, Charlie's ensemble of nine mutually orthogonal states is
$$
\begin{aligned}
|\psi\rangle_{1,2} &= |0, 0 \pm 1\rangle, \\
|\psi\rangle_{3,4} &= |0 \pm 1, 2\rangle, \\
|\psi\rangle_{5,6} &= |2, 1 \pm 2\rangle, \\
|\psi\rangle_{7,8} &= |1 \pm 2, 0\rangle, \\
|\psi\rangle_9 &= |1, 1\rangle.
\end{aligned}
$$ (4.129)

<!-- Page 47 -->
(Here, $|0, 0 \pm 1\rangle$ denotes $|0\rangle_A \otimes \frac{1}{\sqrt{2}}(|0\rangle_B \pm |1\rangle_B)$, etc.) For ease of visualization, it is very convenient to represent this basis pictorially, as a tiling of a square by rectangles:

```
          Bob
       0    1    2
    +---------+----+
  0 | |ψ_1,2> |    |
    +----+----+    |
A 1 |    | |9>| |34|
l   | |78|----+    |
i 2 |    | |ψ_5,6> |
c   +----+---------+
e
```

In the picture, the mutual orthogonality of the elements of Charlie's basis is reflected in the property that the rectangles are nonoverlapping.

When Charlie prepares one of these 9 states and distributes it, Alice receives one of the states
$$
|0\rangle, |1\rangle, |2\rangle, |0 \pm 1\rangle, |1 \pm 2\rangle,
$$ (4.130)
and similarly for Bob. These states are *not* mutually orthogonal, and so cannot be perfectly distinguished by the recipient.

For example, Alice might perform an incomplete orthogonal measurement that distinguishes the state $|2\rangle$ from its orthogonal complement. Pictorially, this measurement "cuts" the square into two nonoverlapping parts. If Charlie prepared one of $|\psi_{5,6}\rangle, |\psi_{7,8}\rangle$, then Alice's outcome could be $|2\rangle\langle 2|$; in that case the state prepared by her measurement can be represented as:

```
          Bob
       0    1    2
    +----+---------+
A 2 | |78| |ψ_5,6> |
l   +----+---------+
```

After learning Alice's measurement outcome, Bob can perform an orthogonal measurement that projects on the basis
$$
\{|0\rangle, |1+2\rangle, |1-2\rangle\}.
$$ (4.131)

<!-- Page 48 -->
If his outcome is $|1+2\rangle$ or $|1-2\rangle$, then Alice and Bob have successfully identified Charlie's state as $|\psi_5\rangle$ or $|\psi_6\rangle$. But if Bob's outcome is $|0\rangle$, then Alice and Bob remain uncertain whether Charlie prepared $|\psi_7\rangle$ of $|\psi_8\rangle$ [note: typo in original, "of" means "or"]. On the other hand, if Charlie prepared one of $|\psi_{1,2}\rangle, |\psi_{3,4}\rangle, |\psi_{7,8}\rangle, |\psi_9\rangle$, then Alice's outcome could be $|0\rangle\langle 0| + |1\rangle\langle 1|$; in that case the state prepared by her measurement can be represented as:

```
          Bob
       0    1    2
    +---------+----+
  0 | |ψ_1,2> |    |
    +----+----+ |34|
A 1 | |78| |9>|    |
l   +----+----+----+
```

Once again, Alice and Bob have lost any hope of distinguishing $|\psi_7\rangle$ from $|\psi_8\rangle$, but in a few more rounds of LOCC, they can successfully identify any of the other five states. Bob projects onto $|2\rangle$ or its complement; if he finds $|2\rangle\langle 2|$, then Alice projects onto $|0 \pm 1\rangle$ to complete the protocol. If Bob's outcome is $|0\rangle\langle 0| + |1\rangle\langle 1|$, then Alice projects onto $\{|0\rangle, |1\rangle\}$; finally Bob measures in either the $|0 \pm 1\rangle$ basis (if Alice found $|0\rangle$) or the $\{|0\rangle, |1\rangle\}$ basis (if Alice found $|1\rangle$).

By choosing one of nine mutually orthogonal product states, Charlie has sent two trits of classical information to Alice and Bob. But their LOCC protocol, which fails to distinguish $|\psi_7\rangle$ from $|\psi_8\rangle$, has not been able to recover all of the information in Charlie's message. Of course, this is just one possible protocol, but one can prove (we won't here) that no LOCC protocol can extract two trits of classical information. The trouble is that with LOCC, Alice and Bob cannot fully "dissect" the square into nonoverlapping rectangles. This is nonlocality without entanglement.
