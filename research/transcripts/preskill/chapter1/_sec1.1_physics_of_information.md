# Section 1.1: Physics of information [PDF Pages 1-4]

<!-- ============================================================ -->
<!-- Source: chap1.pdf, Physical Pages: 1-4                       -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 1 -->
# Chapter 1

# Introduction and Overview

The course has a website at
```
http://www.theory.caltech.edu/~preskill/ph229
```
General information can be found there, including a course outline and links to relevant references.

Our topic can be approached from a variety of points of view, but these lectures will adopt the perspective of a theoretical physicist (that is, it’s my perspective and I’m a theoretical physicist). Because of the interdisciplinary character of the subject, I realize that the students will have a broad spectrum of backgrounds, and I will try to allow for that in the lectures. Please give me feedback if I am assuming things that you don’t know.

## 1.1 Physics of information

Why is a physicist teaching a course about information? In fact, the *physics of information and computation* has been a recognized discipline for at least several decades. This is natural. Information, after all, is something that is encoded in the state of a physical system; a computation is something that can be carried out on an actual physically realizable device. So the study of information and computation should be linked to the study of the underlying physical processes. Certainly, from an engineering perspective, mastery of principles of physics and materials science is needed to develop state-of-the-art computing hardware. (Carver Mead calls his Caltech research group, dedicated to advancing the art of chip design, the “Physics of Computation” (Physcmp) group).

<!-- Page 2 -->
From a more abstract theoretical perspective, there have been noteworthy milestones in our understanding of how physics constrains our ability to use and manipulate information. For example:

- **Landauer’s principle.** Rolf Landauer pointed out in 1961 that erasure of information is necessarily a *dissipative* process. His insight is that erasure always involves the compression of phase space, and so is irreversible.

  For example, I can store one bit of information by placing a single molecule in a box, either on the left side or the right side of a partition that divides the box. Erasure means that we move the molecule to the left side (say) irrespective of whether it started out on the left or right. I can suddenly remove the partition, and then slowly compress the one-molecule “gas” with a piston until the molecule is definitely on the left side. This procedure reduces the entropy of the gas by $\Delta S = k \ln 2$ and there is an associated flow of heat from the box to the environment. If the process is isothermal at temperature $T$, then work $W = kT \ln 2$ is performed on the box, work that I have to provide. If I am to erase information, someone will have to pay the power bill.

- **Reversible computation.** The logic gates used to perform computation are typically *irreversible*, e.g., the NAND gate
$$
(a, b) \to \neg(a \land b)
$$ {#eq-1.1}
has two input bits and one output bit, and we can’t recover a unique input from the output bit. According to Landauer’s principle, since about one bit is erased by the gate (averaged over its possible inputs), at least work $W = kT \ln 2$ is needed to operate the gate. If we have a finite supply of batteries, there appears to be a theoretical limit to how long a computation we can perform.

  But Charles Bennett found in 1973 that any computation can be performed using only reversible steps, and so in principle requires no dissipation and no power expenditure. We can actually construct a reversible version of the NAND gate that preserves all the information about the input: For example, the (Toffoli) gate
$$
(a, b, c) \to (a, b, c \oplus a \land b)
$$ {#eq-1.2}
is a reversible 3-bit gate that flips the third bit if the first two both take the value 1 and does nothing otherwise. The third output bit becomes the NAND of $a$ and $b$ if $c = 1$. We can transform an irreversible computation

<!-- Page 3 -->
to a reversible one by replacing the NAND gates by Toffoli gates. This computation could in principle be done with negligible dissipation.

  However, in the process we generate a lot of extra junk, and one wonders whether we have only postponed the energy cost; we’ll have to pay when we need to erase all the junk. Bennett addressed this issue by pointing out that a reversible computer can run forward to the end of a computation, print out a copy of the answer (a logically reversible operation) and then *reverse* all of its steps to return to its initial configuration. This procedure removes the junk without any energy cost.

  In principle, then, we need not pay any power bill to compute. In practice, the (irreversible) computers in use today dissipate orders of magnitude more than $kT \ln 2$ per gate, anyway, so Landauer’s limit is not an important engineering consideration. But as computing hardware continues to shrink in size, it may become important to beat Landauer’s limit to prevent the components from melting, and then reversible computation may be the only option.

- **Maxwell’s demon.** The insights of Landauer and Bennett led Bennett in 1982 to the reconciliation of Maxwell’s demon with the second law of thermodynamics. Maxwell had envisioned a gas in a box, divided by a partition into two parts $A$ and $B$. The partition contains a shutter operated by the demon. The demon observes the molecules in the box as they approach the shutter, allowing fast ones to pass from $A$ to $B$, and slow ones from $B$ to $A$. Hence, $A$ cools and $B$ heats up, with a negligible expenditure of work. Heat flows from a cold place to a hot place at no cost, in apparent violation of the second law.

  The resolution is that the demon must collect and store information about the molecules. If the demon has a finite memory capacity, he cannot continue to cool the gas indefinitely; eventually, information must be erased. At that point, we finally pay the power bill for the cooling we achieved. (If the demon does not erase his record, or if we want to do the thermodynamic accounting before the erasure, then we should associate some entropy with the recorded information.)

  These insights were largely anticipated by Leo Szilard in 1929; he was truly a pioneer of the physics of information. Szilard, in *his* analysis of the Maxwell demon, invented the concept of a *bit* of information, (the name “bit” was introduced later, by Tukey) and associated the entropy $\Delta S = k \ln 2$ with the acquisition of one bit (though Szilard does not seem to have fully grasped Landauer’s principle, that it is the *erasure* of the bit that carries an inevitable

<!-- Page 4 -->
cost).

These examples illustrate that work at the interface of physics and information has generated noteworthy results of interest to both physicists and computer scientists.
