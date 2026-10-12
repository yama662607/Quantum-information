# Section 4.2: The Bell inequality [PDF Pages 10-17]

<!-- ============================================================ -->
<!-- Source: chap4.pdf, Physical Pages: 10-17                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 10 -->
## 4.2 The Bell inequality

### 4.2.1 Three quantum coins

Is a local hidden-variable theory merely a reformulation of quantum mechanics, or is it a testable hypothesis? John Bell's fruitful idea was to test Einstein locality by considering the quantitative properties of the correlations between measurement outcomes obtained by two parties, Alice and Bob, who share an entangled state. Let us consider an example of the sort of correlations that Alice and Bob would like to explain.

The system that Alice and Bob are studying might be described this way: Alice, in Pasadena, has in her possession three coins laid out on a table, labeled 1, 2, 3. Each coin has either its heads ($H$) or tails ($T$) side facing up, but it is hidden under an opaque cover, so that Alice is not able to tell whether it is an $H$ or a $T$. Alice can uncover any one of the three coins, and so learn its value ($H$ or $T$). However, as soon as that one coin is uncovered, the other two covered coins instantly disappear in a puff of smoke, and Alice never gets an opportunity to uncover the other coins. She has many copies of the three-coin set, and eventually she learns that, no matter which coin she exposes, she is just as likely to find an $H$ as a $T$. Bob, in Chicago, has a similar set of coins, also labeled 1, 2, 3. He too finds that each one of his coins, when revealed, is as likely to be an $H$ as a $T$.

In fact, Alice and Bob have many identical copies of their shared set of coins, so they conduct an extensive series of experiments to investigate how their coin sets are correlated with one another. They quickly make a remarkable discovery: Whenever Alice and Bob uncover coins with the *same* label (whether 1, 2, or 3), they *always* find coins with the same value --- either both are $H$ or both are $T$. They conduct a million trials, just to be sure, and it works every single time! Their coin sets are perfectly correlated.

Alice and Bob suspect that they have discovered something important, and they frequently talk on the phone to brainstorm about the implications of their results. One day, Alice is in an especially reflective mood:

**Alice:** You know, Bob, sometimes it's hard for me to decide which of the three coins to uncover. I know that if I uncover coin 1, say, then coins 2 and 3 will disappear, and I'll never have a chance to find out the values of those coins. Once, just once, I'd love to be able to uncover two of the three coins, and find out whether each is an $H$ or a $T$. But I've tried and it just isn't possible --- there's no way to look at one coin and prevent the other from going poof!

**Bob:** [*Long pause*] Hey . . . wait a minute Alice, I've got an idea . . . Look, I think there *is* a way for you to find the value of two of your

<!-- Page 11 -->
coins, after all! Let's say you would like to uncover coin 1 and coin 2. Well, I'll uncover *my* coin 2 here in Chicago, and I'll call you to tell you what I found, let's say its an $H$. We know, then, that you are certain to find an $H$ if you uncover your coin 2 also. There's absolutely no doubt about that, because we've checked it a million times. Right?

**Alice:** Right . . .

**Bob:** But now there's no reason for you to uncover your coin 2; you know what you'll find anyway. You can uncover coin 1 instead. And then you'll know the value of both coins.

**Alice:** Hmmm . . . yeah, maybe. But we won't be sure, will we? I mean, yes, it always worked when we uncovered the same coin before, but this time you uncovered your coin 2, and your coins 1 and 3 disappeared, and I uncovered my coin 1, and my coins 2 and 3 disappeared. There's no way we'll ever be able to check anymore what would have happened if we had both uncovered coin 2.

**Bob:** We don't have to check that anymore, Alice; we've already checked it a million times. Look, your coins are in Pasadena and mine are in Chicago. Clearly, there's just no way that my decision to uncover my coin 2 can have any *influence* on what you'll find when you uncover your coin 2. That's not what's happening. It's just that when I uncover my coin 2 we're collecting the information we need to predict with certainty what will happen when you uncover your coin 2. Since we're already certain about it, why bother to do it!

**Alice:** Okay, Bob, I see what you mean. Why don't we do an experiment to see what really happens when you and I uncover different coins?

**Bob:** I don't know, Alice. We're not likely to get any funding to do such a dopey experiment. I mean, does anybody really care what happens when I uncover coin 2 and you uncover coin 1?

**Alice:** I'm not sure, Bob. But I've heard about a theorist named Bell. They say that he has some interesting ideas about the coins. He might have a theory that makes a prediction about what we'll find. Maybe we should talk to him.

**Bob:** Good idea! And it doesn't really matter whether his theory makes any sense or not. We can still propose an experiment to test his prediction, and they'll probably fund us.

So Alice and Bob travel to CERN to have a chat with Bell. They tell Bell about the experiment they propose to do. Bell listens closely, but for

<!-- Page 12 -->
a long time he remains silent, with a faraway look in his eyes. Alice and Bob are not bothered by his silence, as they rarely understand anything that theorists say anyway. But finally Bell speaks.

**Bell:** I think I have an idea . . .. When Bob uncovers his coin in Chicago, that can't exert any *influence* on Alice's coin in Pasadena. Instead, what Bob finds out by uncovering his coin reveals some *information* about what will happen when Alice uncovers her coin.

**Bob:** Well, that's what I've been saying . . .

**Bell:** Right. Sounds reasonable. So let's assume that Bob is right about that. Now Bob can uncover any one of his coins, and know for sure what Alice will find when she uncovers the corresponding coin. He isn't *disturbing* her coin in any way; he's just finding out about it. We're forced to conclude that there must be some *hidden variables* that specify the condition of Alice's coins. And if those variables are completely known, then the value of each of Alice's coins can be unambiguously predicted.

**Bob:** [*Impatient with all this abstract stuff*] Yeah, but so what?

**Bell:** When your correlated coin sets are prepared, the values of the hidden variables are not completely specified; that's why any one coin is as likely to be an $H$ as a $T$. But there must be some probability distribution $P(x, y, z)$ (with $x, y, z \in \{H, T\}$) that characterizes the preparation and governs Alice's three coins. These probabilities must be nonnegative, and they sum to one:

$$
\sum_{x,y,z\in\{H,T\}} P(x, y, z) = 1.
$$ {#eq-4.15}

Alice can't uncover all three of her coins, so she can't measure $P(x, y, z)$ directly. But with Bob's help, she can in effect uncover any two coins of her choice. Let's denote with $P_{\text{same}}(i, j)$, the probability that coins $i$ and $j$ ($i, j = 1, 2, 3$) have the same value, either both $H$ or both $T$. Then we see that

$$
\begin{aligned}
P_{\text{same}}(1, 2) &= P(HHH) + P(HHT) + P(TTH) + P(TTT), \\
P_{\text{same}}(2, 3) &= P(HHH) + P(THH) + P(HTT) + P(TTT), \\
P_{\text{same}}(1, 3) &= P(HHH) + P(HTH) + P(THT) + P(TTT),
\end{aligned}
$$ {#eq-4.16}

and it immediately follows from eq. (4.15) that

$$
\begin{aligned}
&P_{\text{same}}(1, 2) + P_{\text{same}}(2, 3) + P_{\text{same}}(1, 3) \\
&= 1 + 2 P(HHH) + 2 P(TTT) \ge 1.
\end{aligned}
$$ {#eq-4.17}

<!-- Page 13 -->
So that's my prediction: $P_{\text{same}}$ should obey the inequality

$$
P_{\text{same}}(1, 2) + P_{\text{same}}(2, 3) + P_{\text{same}}(1, 3) \ge 1.
$$ {#eq-4.18}

You can test it my doing your experiment that "uncovers" two coins at a time.

**Bob:** Well, I guess the math looks right. But I don't really get it. Why does it work?

**Alice:** I think I see . . .. Bell is saying that if there are three coins on a table, and each one is either an $H$ or a $T$, then at least two of the three have to be the *same*, either both $H$ or both $T$. Isn't that it, Bell?

Bell stares at Alice, a surprised look on his face. His eyes glaze, and for a long time he is speechless. Finally, he speaks:

**Bell:** Yes

So Alice and Bob are amazed and delighted to find that Bell is that rarest of beasts --- a theorist who makes sense. With Bell's help, their proposal is approved and they do the experiment, only to obtain a shocking result. After many careful trials, they conclude, to very good statistical accuracy that

$$
P_{\text{same}}(1, 2) \simeq P_{\text{same}}(2, 3) \simeq P_{\text{same}}(1, 3) \simeq \frac{1}{4},
$$ {#eq-4.19}

and hence

$$
P_{\text{same}}(1, 2) + P_{\text{same}}(2, 3) + P_{\text{same}}(1, 3) \simeq 3 \cdot \frac{1}{4} = \frac{3}{4} < 1.
$$ {#eq-4.20}

The correlations found by Alice and Bob flagrantly violate Bell's inequality!

Alice and Bob are good experimenters, but dare not publish so disturbing a result unless they can find a plausible theoretical interpretation. Finally, they become so desperate that they visit the library to see if quantum mechanics can offer any solace . . .

### 4.2.2 Quantum entanglement vs. Einstein locality

What Alice and Bob read about is quantum entanglement. Eventually, they learn that their magical coins are governed by a maximally entangled state of two qubits. What Alice and Bob really share are many copies of the state $|\psi^-\rangle$. When Alice uncovers a coin, she is measuring her qubit

<!-- Page 14 -->
along one of three possible axes, no two of which are orthogonal. Since the measurements don't commute, Alice can uncover only one of her three coins. Similarly, when Bob uncovers his coin, he measures his member of the entangled pair along any one of three axes, so he too is limited to uncovering just one of his three coins. But since Alice's measurements commute with Bob's, they can uncover one coin each, and study how Alice's coins are correlated with Bob's coins.

To help Alice and Bob interpret their experiment, let's see what quantum mechanics predicts about these correlations. The state $|\psi^-\rangle$ has the convenient property that it remains invariant if Alice and Bob each apply the same unitary transformation,

$$
\boldsymbol{U} \otimes \boldsymbol{U}|\psi^-\rangle = |\psi^-\rangle.
$$ {#eq-4.21}

For infinitesimal unitaries, this becomes the property

$$
\left(\vec{\boldsymbol{\sigma}}^{(A)} + \vec{\boldsymbol{\sigma}}^{(B)}\right) |\psi^-\rangle = 0
$$ {#eq-4.22}

(the state has vanishing total angular momentum, as you can easily check by an explicit computation). Now consider the expectation value

$$
\langle\psi^-|\left(\vec{\boldsymbol{\sigma}}^{(A)} \cdot \hat{a}\right) \left(\vec{\boldsymbol{\sigma}}^{(B)} \cdot \hat{b}\right) |\psi^-\rangle,
$$ {#eq-4.23}

where $\hat{a}$ and $\hat{b}$ are unit 3-vectors. Acting on $|\psi^-\rangle$, we can replace $\vec{\boldsymbol{\sigma}}^{(B)}$ by $-\vec{\boldsymbol{\sigma}}^{(A)}$; therefore, the expectation value can be expressed as a property of Alice's system, which has density operator $\boldsymbol{\rho}_A = \frac{1}{2}\boldsymbol{I}$:

$$
\begin{aligned}
&-\langle\psi^-|\left(\vec{\boldsymbol{\sigma}}^{(A)} \cdot \hat{a}\right) \left(\vec{\boldsymbol{\sigma}}^{(A)} \cdot \hat{b}\right) |\psi^-\rangle \\
&= -a_i b_j \mathrm{tr}\left(\boldsymbol{\rho}_A \boldsymbol{\sigma}_i^{(A)} \boldsymbol{\sigma}_j^{(A)}\right) = -a_i b_j \delta_{ij} = -\hat{a} \cdot \hat{b} = -\cos\theta,
\end{aligned}
$$ {#eq-4.24}

where $\theta$ is the angle between the axes $\hat{a}$ and $\hat{b}$. Thus we find that the measurement outcomes are always perfectly anticorrelated when we measure both spins along the same axis $\hat{a}$, and we have also obtained a more general result that applies when the two axes are different.

The projection operator onto the spin up (spin down) states along $\hat{n}$ is

<!-- Page 15 -->
$\boldsymbol{E}(\hat{n}, \pm) = \frac{1}{2}(\boldsymbol{I} \pm \hat{n} \cdot \vec{\boldsymbol{\sigma}})$; we therefore obtain

$$
\begin{aligned}
P(++) &= \langle\psi^-|\boldsymbol{E}^{(A)}(\hat{a}, +)\boldsymbol{E}^{(B)}(\hat{b}, +)|\psi^-\rangle = \frac{1}{4}(1 - \cos\theta), \\
P(--) &= \langle\psi^-|\boldsymbol{E}^{(A)}(\hat{a}, -)\boldsymbol{E}^{(B)}(\hat{b}, -)|\psi^-\rangle = \frac{1}{4}(1 - \cos\theta), \\
P(+-) &= \langle\psi^-|\boldsymbol{E}^{(A)}(\hat{a}, +)\boldsymbol{E}^{(B)}(\hat{b}, -)|\psi^-\rangle = \frac{1}{4}(1 + \cos\theta), \\
P(-+) &= \langle\psi^-|\boldsymbol{E}^{(A)}(\hat{a}, -)\boldsymbol{E}^{(B)}(\hat{b}, +)|\psi^-\rangle = \frac{1}{4}(1 + \cos\theta);
\end{aligned}
$$ {#eq-4.25}

here $P(++)$ is the probability that Alice and Bob both obtain the spin-up outcome when Alice measures along $\hat{a}$ and Bob measures along $\hat{b}$, etc. The probability that their outcomes are the same is

$$
P_{\text{same}} = P(++) + P(--) = \frac{1}{2}(1 - \cos\theta),
$$ {#eq-4.26}

and the probability that their outcomes are opposite is

$$
P_{\text{opposite}} = P(+-) + P(-+) = \frac{1}{2}(1 + \cos\theta).
$$ {#eq-4.27}

Now suppose that Alice measures her spin along one of the three symmetrically distributed axes in the $x-z$ plane,

$$
\begin{aligned}
\hat{a}_1 &= (0, 0, 1), \\
\hat{a}_2 &= \left(\frac{\sqrt{3}}{2}, 0, -\frac{1}{2}\right), \\
\hat{a}_3 &= \left(-\frac{\sqrt{3}}{2}, 0, -\frac{1}{2}\right),
\end{aligned}
$$ {#eq-4.28}

so that

$$
\hat{a}_1 \cdot \hat{a}_2 = \hat{a}_2 \cdot \hat{a}_3 = \hat{a}_3 \cdot \hat{a}_1 = -\frac{1}{2}.
$$ {#eq-4.29}

And suppose that Bob measures along one of three axes that are diametrically opposed to Alice's:

$$
\begin{aligned}
\hat{b}_1 &= -\hat{a}_1, \\
\hat{b}_2 &= -\hat{a}_2, \\
\hat{b}_3 &= -\hat{a}_3.
\end{aligned}
$$ {#eq-4.30}

When Alice and Bob choose opposite axes, then $\theta = 180^\circ$ and $P_{\text{same}} = 1$. But otherwise $\theta = \pm 60^\circ$ so that $\cos\theta = 1/2$ and $P_{\text{same}} = 1/4$. This is just the behavior that Alice and Bob found in their experiment, in violation of Bell's prediction.

<!-- Page 16 -->
Bell's logic seemed compelling but something went wrong, so we are forced to reconsider his tacit assumptions. First, Bell assumed that there is a joint probability distribution that governs the possible outcomes of all measurements that Alice and Bob might perform. This is the hidden-variable hypothesis. He imagines that if the values of the hidden variables are exactly known, then the outcome of any measurement can be predicted with certainty --- measurement outcomes are described probabilistically because the values of the hidden variables are drawn from an ensemble of possible values. Second, Bell assumed that Bob's decision about what to measure in Chicago has no effect on the hidden variables that govern Alice's measurement in Pasadena. This is the assumption that the hidden variables are *local*. If we accept these two assumptions, there is no escaping Bell's conclusion. We have found that the correlations predicted by quantum theory are incompatible with theses assumptions.

What are the implications? Perhaps the moral of the story is that it can be dangerous to reason about what *might* have happened, but didn't actually happen --- what are sometimes called *counterfactuals*. Of course, we do this all the time in our everyday lives, and we usually get away with it; reasoning about counterfactuals seems to be acceptable in the classical world, but sometimes it gets us into trouble in the quantum world. We claimed that Alice knew what would happen when she measured along $\hat{a}_1$, because Bob measured along $-\hat{a}_1$, and every time we have ever checked, their measurement outcomes are always perfectly correlated. But Alice did *not* measure along $\hat{a}_1$; she measured along $\hat{a}_2$ instead. We got into trouble by trying to assign probabilities to the outcomes of measurements along $\hat{a}_1$, $\hat{a}_2$, and $\hat{a}_3$, even though Alice can perform just one of those measurements. In quantum theory, assuming that there is a probability distribution that governs the outcomes of all three measurements that Alice might have made, even though she was able to carry out only one of these measurements, leads to mathematical inconsistencies, so we had better not do it. We have affirmed Bohr's principle of *complementary* --- we are forbidden to consider simultaneously the possible outcomes of two mutually exclusive experiments.

One who rejects the complementarity principle may prefer to say that violations of the Bell inequalities (confirmed experimentally) have exposed an essential *nonlocality* built into the quantum description of Nature. If we do insist that it is legitimate to talk about outcomes of mutually exclusive experiments then we are forced to conclude that Bob's choice of measurement actually exerted a subtle *influence* on the outcome of Alice's measurement. Thus advocates of this viewpoint speak of "quantum nonlocality."

By ruling out local hidden variables, Bell demolished Einstein's dream that the indeterminacy of quantum theory could be eradicated by adopt-

<!-- Page 17 -->
ing a more complete, yet still local, description of Nature. If we accept locality as an inviolable principle, then we are forced to accept randomness as an unavoidable and intrinsic feature of quantum measurement, rather than a consequence of incomplete knowledge.

To some, the peculiar correlations unmasked by Bell's inequality call out for a deeper explanation than quantum mechanics seems to provide. They see the EPR phenomenon as a harbinger of new physics awaiting discovery. But they may be wrong. We have been waiting over 65 years since EPR, and so far no new physics.

The human mind seems to be poorly equipped to grasp the correlations exhibited by entangled quantum states, and so we speak of the weirdness of quantum theory. But whatever your attitude, experiment forces you to accept the existence of the weird correlations among the measurement outcomes. There is no big mystery about how the correlations were established --- we saw that it was necessary for Alice and Bob to get together at some point to create entanglement among their qubits. The novelty is that, even when $A$ and $B$ are distantly separated, we cannot accurately regard $A$ and $B$ as two separate qubits, and use classical information to characterize how they are correlated. They are more than just correlated, they are a single *inseparable* entity. They are *entangled*.
