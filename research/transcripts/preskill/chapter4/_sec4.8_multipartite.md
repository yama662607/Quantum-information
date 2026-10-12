# Section 4.8: Multipartite entanglement (Transcript)

Source: `quarto/assets/pdf/preskill/chap4.pdf`, pages 48–59

## 4.8 Multipartite entanglement [p.48]

Up until now, we have mostly limited our attention to quantum states shared by two parties. We will conclude this chapter with some observations about the properties of entanglement shared by three or more parties: *multipartite entanglement*.

Consider for example the case of a pure state $|\psi\rangle_{A_1, A_2, \dots A_n}$ shared by $n$ parties $A_1, A_2, \dots A_n$, and suppose that there is no way to divide the parties into two smaller camps, where each camp shares a pure state.

<!-- Page 49 -->
Thus the state is entangled, and furthermore, it can't be expressed as a product of states each involving fewer than $n$ parties. Hence we might say that the state exhibits $n$-party entanglement. If the parties start out with an $n$-fold product state $|\psi_1\rangle_{A_1} \otimes |\psi_2\rangle_{A_2} \otimes \dots |\psi_n\rangle_{A_n}$, then there is no way for them to assemble the state $|\psi\rangle_{A_1, A_2, \dots A_n}$ using LOCC alone — quantum communication is required. Indeed, no matter how we divide the $n$ parties into two subsystems $A$ and $B$, quantum communication between $A$ and $B$ is needed.

What if we disallow quantum communication, but we do equip the parties with *pairwise* entanglement that has been established in advance? Then for the purpose of constructing the state $|\psi\rangle_{A_1, A_2, \dots A_n}$, it clearly suffices for the first party $A_1$ to share bipartite entanglement with each of the other $n-1$ parties. Party $A_1$ can build the state $|\psi\rangle_{A_1, A_2, \dots A_n}$ in her own laboratory, and then teleport the corresponding share of the state to each of the $n-1$ other parties. In this sense, then, bipartite entanglement and LOCC is as powerful a resource as multiparty entanglement.

Nonetheless, multipartite entangled states exhibit some qualitatively new phenomena that we don't encounter in the study of bipartite entanglement, such as nonprobabilistic tests of Einstein locality, and entanglement-enhanced multiparty communication.

### 4.8.1 Three quantum boxes [p.49]

In the wake of the wildly successful experiment with the three coins on the table, Alice and Bob are now world famous. They are both tenured professors, Alice at Caltech, and Bob at Chicago. They are much too important to spend much time in the lab, but they have many graduate students and remain scientifically active.

Their best student, Charlie, who did all the hard work on the coin experiment, has graduated and is now an assistant professor at Princeton. Alice and Bob would like to nurture Charlie's career, and help him earn tenure. One day, Alice and Bob are chatting on the phone:

**Alice:** You know, Bob, we really ought to help Charlie. Can you think of a neat experiment that the three of us can do together?

**Bob:** Well, I dunno, Alice. There are a lot of experiments I'd like to do with our entangled pairs of qubits. But in each experiment, there's one qubit for me and one for you. It looks like Charlie's the odd man out.

**Alice:** [Long pause] Bob . . .. Have you ever thought of doing an experiment with *three* qubits?

<!-- Page 50 -->
Bob's jaw drops and his pulse races. In a sudden epiphany, his whole future career seems mapped out before him. Truth be told, Bob was beginning to wonder if pairs of qubits were getting to be old hat. Now he knows that for the next five years, he will devote himself slavishly to performing the definitive three-qubit experiment. By that time, he, Alice, and Charlie will have trained another brilliant student, and will be ready for a crack at four qubits. Then another student, and another qubit. And so on to retirement.

Here is the sort of three-qubit experiment that Alice and Bob decide to try: Alice instructs her technician in her lab at Caltech to prepare carefully a state of three quantum boxes. (But Alice doesn't know exactly how the technician does it.) She keeps one box for herself, and she ships the other two by quantum express, one to Bob and one to Charlie. Each box has a ball inside that can be either black or white, but the box is sealed tight shut. The only way to find out what is inside is to open the box, but there are two different ways to open it — the box has two doors, clearly marked $X$ and $Y$. When either door opens, a ball pops out whose color can be observed. It isn't possible to open both doors at once.

Alice, Bob, and Charlie decide to study how the boxes are correlated. They conduct many carefully controlled trials. Each time, one of the three, chosen randomly, opens door $X$, while the other two open door $Y$. Lucky as ever, Alice, Bob, and Charlie make an astonishing discovery. They find that every single time they open the boxes this way, the number of black balls they find is *always odd*.

That is, Alice, Bob and Charlie find that when they open door $X$ on one box and door $Y$ on the other two, the colors of the balls in the boxes are guaranteed to be one of
$$
0_A 0_B 1_C, \quad 0_A 1_B 0_C, \quad 1_A 0_B 0_C, \quad 1_A 1_B 1_C,
$$ (4.132)
(0 for white, 1 for black); They *never* see any of
$$
1_A 1_B 0_C, \quad 1_A 0_B 1_C, \quad 0_A 1_B 1_C, \quad 0_A 0_B 0_C.
$$ (4.133)
It makes no difference which of the three boxes is opened through door $X$.

After a while, Alice, Bob, and Charlie catch on that after opening two of the boxes, they can always predict what will happen before they open the third box. If the first two balls are the same color, the last ball is sure to be black, and if the first two are different colors, the last ball is sure to be white. They've tried it a zillion times, and it always works!

<!-- Page 51 -->
Even after all the acclaim showered upon the three-coin experiment, Alice, Bob, and Charlie have never quite shaken their attachment to Einstein locality. One day they are having a three-way conference call:

**Alice:** You know, guys, sometimes I just can't decide whether to open door $X$ or door $Y$ of my box. I know I have to choose carefully . . . If I open door $X$, that's sure to disturb the box; so I'll never know what would have happened if I had opened door $Y$ instead. And if I open door $Y$, I'll never know what I would have found if I had opened door $X$. It's frustrating!

**Bob:** Alice, you're so wrong! Our experiment shows that you can have it both ways. Don't you see? Let's say that you want to know what will happen when you open door $X$. Then just ask Charlie and me to open door $Y$ of our boxes and to tell you what we find. You'll know absolutely for sure, without a doubt, what's going to happen when you open door $X$. We've tested that over and over again, and it always works. So why bother to open door $X$? You can go ahead and open door $Y$ instead, and see what you find. That way, you really do know the result of opening *both* doors!

**Charlie:** But how can you be sure? If Alice opens door $Y$, she passes up the opportunity to open door $X$. She can't really ever have it both ways. After she opens door $Y$, we can never check whether opening door $X$ would have given the result we expected.

**Bob:** Oh come on, how can it be otherwise? Look, you don't really believe that what you do to your box in Princeton and I do to mine in Chicago can exert any *influence* on what Alice finds when she opens her box in Pasadena, do you? When we open our boxes, we can't be changing anything in Alice's box; we're just finding the information we need to predict with certainty what Alice is going to find.

**Charlie:** Well, maybe we should do some more experiments to find out if you're right about that.

Indeed, the discovery of the three-box correlation has made Alice and Bob even more famous than before, but Charlie hasn't gotten the credit he deserves — he still doesn't have tenure. No wonder he wants to do more experiments! He continues:

**Charlie:** Here's something we can try. In all the experiments we've done up to now, we have always opened door $Y$ on two boxes and door $X$ on the other box. Maybe we should try something different.

<!-- Page 52 -->
Like, maybe we should see what happens if we open the same door on all three boxes. We could try opening three $X$ doors.

**Bob:** Oh, come on! I'm tired of three boxes. We already know all about three boxes. It's time to move on, and I think Diane is ready to help out. Let's do four boxes!

**Alice:** No, I think Charlie's right. We can't really say that we know everything there is to know about three boxes until we've experimented with other ways of opening the doors.

**Bob:** Forget it. They'll never fund us! After we've put all that effort into opening two $Y$'s and an $X$, now we're going to say we want to open three $X$'s? They'll say we've done whiffnium and now we're proposing whaffnium . . . We'll sound ridiculous!

**Alice:** Bob has a point. I think that the only way we can get funding to do this experiment is if we can make a prediction about what will happen. Then we can say that we're doing the experiment to test the prediction. Now, I've heard about some theorists named Greenberger, Horne, Zeilinger, and Mermin (GHZM). They've been thinking a lot about our three-box experiments; maybe they'll be able to suggest something.

**Bob:** Well, these boxes are my life, and they're just a bunch of theorists. I doubt that they'll have anything interesting or useful to say. But I suppose it doesn't really matter whether their theory makes any sense . . . If we can test it, then even I will accept that we have a reason for doing another three-box experiment.

And so it happens that Alice, Bob, and Charlie make the pilgrimage to see GHZM. And despite Bob's deep skepticism, GHZM make a very interesting suggestion indeed:

**GHZM:** Bob says that opening a box in Princeton and a box in Chicago can't possibly have any influence on what will happen when Alice opens a box in Pasadena. Well, let's suppose that he's right. Now you guys are going to do an experiment in which you all open your $X$ doors. No one can say what's going to happen, but we can reason this way: Let's just assume that if you had opened three $Y$ doors, you would have found three white balls. Then we can use Bob's argument to see that if you open three $X$ doors instead, you will have to find three black balls. It goes like this: if Alice opens $X$, Bob opens $Y$, and Charlie opens $Y$, then you know for certain that the number of black balls has to be odd. So, if we know that Bob

<!-- Page 53 -->
and Charlie both would find white when they open door $Y$, then Alice has to find black when she opens door $X$. Similarly, if Alice and Charlie both would find white when they open $Y$, then Bob has to find black when he opens $X$, and if Alice and Bob both would find white when they open $Y$, then Charlie must find black when he opens $X$. So we see that§
$$
Y_A Y_B Y_C = 000 \longrightarrow X_A X_B X_C = 111 .
$$ (4.134)
Don't you agree?

**Bob:** Well, maybe that's logical enough, but what good is it? We don't know what we're going to find inside a box until we open it. You've assumed that we know $Y_A Y_B Y_C = 000$, but we never know that ahead of time.

**GHZM:** Sure, but wait. Yes, you're right that we can't know ahead of time what we would find if we opened door $Y$ on each box. But there are only eight possibilities for three boxes, and we can easily list them all. And for each of those eight possibilities for $Y_A Y_B Y_C$ we can use the same reasoning as before to infer the value of $X_A X_B X_C$. We obtain a table, like this:
$$
\begin{aligned}
Y_A Y_B Y_C = 000 &\longrightarrow X_A X_B X_C = 111 \\
Y_A Y_B Y_C = 001 &\longrightarrow X_A X_B X_C = 001 \\
Y_A Y_B Y_C = 010 &\longrightarrow X_A X_B X_C = 010 \\
Y_A Y_B Y_C = 100 &\longrightarrow X_A X_B X_C = 100 \\
Y_A Y_B Y_C = 011 &\longrightarrow X_A X_B X_C = 100 \\
Y_A Y_B Y_C = 101 &\longrightarrow X_A X_B X_C = 010 \\
Y_A Y_B Y_C = 110 &\longrightarrow X_A X_B X_C = 001 \\
Y_A Y_B Y_C = 111 &\longrightarrow X_A X_B X_C = 111
\end{aligned}
$$ (4.135)

**Bob:** Okay, but so what?

**GHZM:** There's something interesting about the table, Bob! Look at the values for $X_A X_B X_C$ . . . Every single entry has an odd number of 1's. That's our prediction: when you all open door $X$ on your boxes, you'll always find an odd number of black balls! Could be one, or could be three, but always odd.

Naturally, Alice, Bob, and Charlie are delighted by this insight from GHZM. They proceed to propose the experiment, which is approved and

§ Here 0 stands for white and 1 stands for black; $Y_A$ is what Alice finds when she opens door $Y$ on her box, and so on.

<!-- Page 54 -->
generously funded. Finally the long awaited day arrives when they are to carry out the experiment for the first time. And when Alice, Bob, and Charlie each open door $X$ on their boxes, can you guess what they find? Three white balls. Whaaaa??!!

Suspecting an error, Alice and Bob and Charlie repeat the experiment, very carefully, over and over and over again. And in every trial, every single time, they find an even number of black balls when they open door $X$ on all three boxes. Sometimes none, sometimes two, but never one and never three. What they find, every single time, is just the opposite of what GHZM had predicted would follow from the principle of Einstein locality!

Desperation once again drives Alice, Bob, and Charlie into the library, seeking enlightenment. After some study of a quantum mechanics textbook, and a thorough interrogation of Alice's lab technician, they realize that their three boxes had been prepared in a GHZM quantum state
$$
|\psi\rangle_{ABC} = \frac{1}{\sqrt{2}} (|000\rangle_{ABC} + |111\rangle_{ABC}) ,
$$ (4.136)
a simultaneous eigenstate with eigenvalue one of the three observables
$$
\boldsymbol{Z}_A \otimes \boldsymbol{Z}_B \otimes \boldsymbol{I}_C, \quad \boldsymbol{I}_A \otimes \boldsymbol{Z}_B \otimes \boldsymbol{Z}_C, \quad \boldsymbol{X}_A \otimes \boldsymbol{X}_B \otimes \boldsymbol{X}_C .
$$ (4.137)
And since $\boldsymbol{Z}\boldsymbol{X} = i\boldsymbol{Y}$, they realize that this state has the properties
$$
\begin{aligned}
\boldsymbol{Y}_A \otimes \boldsymbol{Y}_B \otimes \boldsymbol{X}_C &= -1 \\
\boldsymbol{X}_A \otimes \boldsymbol{Y}_B \otimes \boldsymbol{Y}_C &= -1 \\
\boldsymbol{Y}_A \otimes \boldsymbol{X}_B \otimes \boldsymbol{Y}_C &= -1 \\
\boldsymbol{X}_A \otimes \boldsymbol{X}_B \otimes \boldsymbol{X}_C &= 1 .
\end{aligned}
$$ (4.138)

In opening the box through door $X$ or door $Y$, Alice, Bob, and Charlie are measuring the observable $\boldsymbol{X}$ or $\boldsymbol{Y}$, where the outcome 1 signifies a white ball, and the outcome $-1$ a black ball. Thus if the three qubit state eq. (4.136) is prepared, eq. (4.138) says that an odd number of black balls will be found if door $Y$ is opened on two boxes and door $X$ on the third, while an even number of black balls will be found if door $X$ is opened on all three boxes. This behavior, unambiguously predicted by quantum mechanics, is just what had seemed so baffling to Alice, Bob, and Charlie, and to their fellow die-hard advocates of Einstein locality.

After much further study of the quantum mechanics textbook, Alice, Bob, and Charlie gradually come to recognize the flaw in their reasoning. They learn of Bohr's principle of complementarity, of the irreconcilable incompatibility of noncommuting observables. And they recognized that

<!-- Page 55 -->
to arrive at their prediction, they had *postulated* an outcome for the measurement of $YYY$, and then proceeded to infer the consequences for a measurement of $XXX$. By failing to heed the insistent admonitions of Niels Bohr, they had fallen prey to the most pernicious of fallacies.

As they had hoped, the experiment of the three boxes brings even further acclaim to Alice and Bob, and tenure to Charlie. Of course, the three-coin experiment had already convincingly struck down Einstein locality; even so, the three-box experiment had a different character. In the coin experiment, Alice and Bob could uncover any two of the three coins, finding any one of four possible configurations: $HH, HT, TH, TT$. Only by carrying out many trials could they amass a convincing statistical case for the violation of the Bell inequality. In contrast, in the three-box experiment, Alice, Bob, and Charlie had found a result inconsistent with Einstein locality in *every single trial* in which they opened door $X$ on all three boxes!

### 4.8.2 Cat states [p.55]

The GHZM state studied by Alice, Bob, and Charlie is a natural three-qubit generalization of the maximally entangled Bell pair. A Bell pair can be characterized as the simultaneous eigenstate of the two commuting operators $ZZ$, whose eigenvalue is the "parity bit" of the pair, and $XX$, whose eigenvalue is the phase bit. (Here we use a compressed notation in which the tensor product symbol $\otimes$ is suppressed — *e.g.*, $XX$ denotes the operator that simultaneously applies $X$ to both Alice's qubit and Bob's.) The GHZM state is the simultaneous eigenstate of $ZZI, IZZ$, and $XXX$.

An $n$-qubit generalization of the GHZM state can be defined, which is the simultaneous eigenstate of the $n$ commuting operators
$$
\begin{aligned}
ZZIII\dots I , \\
IZZII\dots I , \\
IIZZI\dots I , \\
\dots \\
III\dots IZZ , \\
XX\dots XX .
\end{aligned}
$$ (4.139)
Each such simultaneous eigenstate has the form
$$
\frac{1}{\sqrt{2}} (|x\rangle \pm |\neg x\rangle) ,
$$ (4.140)
where $\neg x$ denotes the complement of the binary string $x$. Since for large $n$ this state is a coherent superposition of two "macroscopically distinguishable"

<!-- Page 56 -->
states, it is called an $n$-qubit *cat state*, in homage to Schrödinger's cat. The $n$-qubit cat state has $n-1$ parity bits, and just one phase bit.

Some noteworthy properties of cat states are:
- Each qubit is maximally entangled with the rest. That is, if we trace over the other $n-1$ qubits, the qubit's density operator is $\boldsymbol{\rho} = \frac{1}{2}\boldsymbol{I}$. For this reason, it is sometimes said that a cat state is a maximally entangled state of $n$ qubits.
- But this is a rather misleading locution. Because its parity and phase bits are treated quite asymmetrically, the cat is not so profoundly entangled as some other multiqubit states that we will encounter in Chapter 7. For example, for the cat state with $x = 000\dots 0$, if we trace over $n-2$ qubits, the density operator of the remaining two is
$$
\boldsymbol{\rho}_{\text{2-qubit}} = \frac{1}{2} (|00\rangle\langle 00| + |11\rangle\langle 11|) ,
$$ (4.141)
which has rank two rather than four. Correspondingly, we can acquire a bit of information about a cat state (one of its parity bits) by observing only two of the qubits in the state. Other multiqubit states, which might be regarded as more highly entangled than cat states, have the property that the density operator of two (or more) qubits is proportional to the identity, if we trace over the rest.
- Suppose that Charlie prepares one of the $2^n$ possible cat states and distributes it to $n$ parties. Using LOCC, the parties can determine all $n-1$ parity bits of the state — each party measures $Z$ and all broadcast their results. But by measuring $Z$ they destroy the phase bit. Alternatively, they can all measure $X$ to determine the phase bit, but at the cost of destroying all the parity bits.
- Each party, by applying one of $\{I, X, Y, Z\}$ can transform a given cat state to any one of four other cat states; that is, the party can modify the phase bit and one of the $n-1$ parity bits. All $n$ parties, working together, can transform one cat state to any one of the $2^n$ mutually orthogonal cat states; for example, one party can manipulate the phase bit while each of the the other $n-1$ parties controls a parity bit.
- If the parties unite, the phase bit and all parity bits can be simultaneously measured.

If the parties start out with a product state, the three-qubit cat state (for example) can be prepared by executing the quantum circuit:

<!-- Page 57 -->
```
phase bit (0, 1)  --|H|--*-----*-----
                         |     |
parity bits \tilde{x}  --+-----|-----  --> (1/\sqrt{2}) (|0, \tilde{x}> \pm |1, \tilde{x}>)
                               |
                       --------+-----
```

For the $n$-party case, a similar circuit with $n-1$ CNOT gates does the job. Thus, to prepare the state, it suffices for the first party to visit each of the other $n-1$ parties. By running the circuit in reverse, a cat state can be transformed to a product state that can be measured locally.

### 4.8.3 Entanglement-enhanced communication [p.57]

An intriguing property of the $n$-qubit cat state is that its phase bit can be manipulated by each one of the $n$ parties that share the state. One wonders how this shared resource might be exploited.

We will describe a setting in which possession of a cat state reduces the amount of communication that is required to accomplish a distributed information processing task. Suppose that each one of $n$ parties labeled by index $i = 1, 2, 3, \dots, n$ resides on a separate planet, and that party $i$ possesses some data (a string of bits $x_i$) known only to that party. The goal of the parties is to compute a function $f$ (with a one-bit output) that depends on all the data:
$$
f(x_1, x_2, x_3, \dots, x_n) \in \{0, 1\} .
$$ (4.142)
In this universe, computation is cheap, and communication is expensive. Each party has unlimited computational power at her disposal, but since no party knows the full input of the function $f$, no one can compute $f$ unless the parties communicate. For this purpose, they are equipped with a broadcast channel — if any party speaks, all the others can hear her. However, use of the broadcast channel is very expensive, so that the parties wish to compute $f$ while making minimal use of the channel.

With this motivation, we define the *classical communication complexity* $CCC[f]$ of the function $f$:
$$
CCC[f] = \text{the minimum of bits that must be broadcast (in the worst case) for all the parties to know the value of } f(x_1, x_2, x_3, \dots, x_n).
$$
Here "in the worst case" means that we maximize the number of bits of communication required over all possible values for the input strings $x_1, x_2, x_3, \dots, x_n$.

<!-- Page 58 -->
We are interested in whether using quantum information can reduce the amount of communication required to compute a function. Hence we contrast the function's classical communication complexity with its quantum communication complexity. There are actually several different natural ways to generalize a classical communication setting to a quantum setting. In one, to which we return in Chapter 6, the parties are allowed to exchange qubits instead of classical bits. Here, we consider a scenario in which all communication is via the classical broadcast channel, but the parties are allowed to share entangled states that have been prepared in advance, and to manipulate their shared entanglement locally. Thus we define the *quantum communication complexity* $QCC[f]$ as
$$
QCC[f] = \text{the minimum of bits that must be broadcast (in the worst case) for all the parties to know the value of } f(x_1, x_2, x_3, \dots, x_n),
$$
where the parties are permitted to share prior quantum entanglement.

One way to argue that multipartite entanglement can be a useful resource is to establish that there are functions $f$ such that
$$
QCC[f] < CCC[f] .
$$ (4.143)

Here is an example of such a function: Each party holds an $m$-bit string, and they are to compute
$$
\sum_{i=1}^n x_i \pmod{2^m} .
$$ (4.144)
Except that they have been promised that the answer is either $0$ or $2^{m-1}$; therefore, their function has just a one-bit output.

First consider what strategy the parties should play if they share no entanglement. Suppose that parties 2 through $n$ broadcast their data, and that the first party computes $f$ and broadcasts the result. But note that it is not necessary for the parties to broadcast all of their bits, since some of the bits cannot affect the answer. Indeed, the $k$ least significant bits are irrelevant as long as
$$
(n - 1)(2^k - 1) < 2^{m-1} ,
$$ (4.145)
which is satisfied provided that
$$
(n - 1)2^k \le 2^{m-1} .
$$ (4.146)
It suffices then, for parties 2 through $n$ to broadcast their $m-k$ most significant bits, where
$$
m - k \ge \log_2(n - 1) + 1 ;
$$ (4.147)

<!-- Page 59 -->
including one more bit for the first party to broadcast the answer, we conclude that
$$
CCC[f] \le (n - 1)(\log_2(n - 1) + 1) + 1 .
$$ (4.148)
In fact, this protocol is close to optimal — it can be proved that
$$
CCC[f] > n \log_2 n - n .
$$ (4.149)

But the amount of communication required can be reduced if the parties share an $n$-qubit cat state, for they can imprint the answer on their shared phase bit! Each applies to her qubit the transformation
$$
\begin{aligned}
|0\rangle &\to |0\rangle , \\
|1\rangle &\to e^{2\pi i (x_i / 2^m)} |1\rangle .
\end{aligned}
$$ (4.150)
Thus the cat state
$$
|\text{cat}\rangle = \frac{1}{\sqrt{2}} (|000\dots 0\rangle + |111\dots 1\rangle)
$$ (4.151)
is transformed to
$$
|\text{cat}'\rangle = \frac{1}{\sqrt{2}} (|000\dots 0\rangle + \eta |111\dots 1\rangle) ,
$$ (4.152)
where the phase $\eta$ is
$$
\eta = \exp\left(2\pi i \left(\sum_{i=1}^n x_i\right) / 2^m\right) = (-1)^{f(x_1, x_2, \dots, x_n)} .
$$ (4.153)
Thus the fu
