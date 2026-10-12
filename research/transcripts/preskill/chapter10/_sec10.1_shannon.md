# Section 10.1: Shannon for Dummies [PDF Pages 7-19]

<!-- ============================================================ -->
<!-- Source: chap10.pdf, Physical Pages: 7-19                     -->
<!-- Transcribed: 2026-10-12                                      -->
<!-- ============================================================ -->

<!-- Page 7 -->
# 10 Quantum Shannon Theory

Quantum information science is a synthesis of three great themes of 20th century thought: quantum physics, computer science, and information theory. Up until now, we have given short shrift to the information theory side of this trio, an oversight now to be remedied.

A suitable name for this chapter might have been *Quantum Information Theory*, but I prefer for that term to have a broader meaning, encompassing much that has already been presented in this book. Instead I call it *Quantum Shannon Theory*, to emphasize that we will mostly be occupied with generalizing and applying Claude Shannon's great (classical) contributions to a quantum setting. Quantum Shannon theory has several major thrusts:

1. Compressing quantum information.
2. Transmitting classical and quantum information through noisy quantum channels.
3. Quantifying, characterizing, transforming, and using quantum entanglement.

A recurring theme unites these topics — the properties, interpretation, and applications of von Neumann entropy.

My goal is to introduce some of the main ideas and tools of quantum Shannon theory, but there is a lot we won't cover. For example, we will mostly consider information theory in an *asymptotic setting*, where the same quantum channel or state is used arbitrarily many times, thus focusing on issues of principle rather than more practical questions about devising efficient protocols.

## 10.1 Shannon for Dummies

Before we can understand von Neumann entropy and its relevance to quantum information, we should discuss Shannon entropy and its relevance to classical information.

Claude Shannon established the two core results of classical information theory in his landmark 1948 paper. The two central problems that he solved were:

1. How much can a message be *compressed*; *i.e.*, how redundant is the information? This question is answered by the "source coding theorem," also called the "noiseless coding theorem."
2. At what *rate* can we communicate reliably over a noisy channel; *i.e.*, how much redundancy must be incorporated into a message to protect against errors? This question is answered by the "noisy channel coding theorem."

<!-- Page 8 -->
Both questions concern *redundancy* — how *unexpected* is the next letter of the message, on the average. One of Shannon's key insights was that *entropy* provides a suitable way to quantify redundancy.

I call this section "Shannon for Dummies" because I will try to explain Shannon's ideas quickly, minimizing distracting details. That way, I can compress classical information theory to about 13 pages.

### 10.1.1 Shannon entropy and data compression

A message is a string of letters, where each letter is chosen from an alphabet of $k$ possible letters. We'll consider an idealized setting in which the message is produced by an "information source" which picks each letter by sampling from a probability distribution

$$
X := \{x, p(x)\};
$$ {#eq-10.1}

that is, the letter has the value

$$
x \in \{0, 1, 2, \dots d-1\}
$$ {#eq-10.2}

with probability $p(x)$. If the source emits an $n$-letter message the particular string $x = x_1 x_2 \dots x_n$ occurs with probability

$$
p(x_1 x_2 \dots x_n) = \prod_{i=1}^n p(x_i).
$$ {#eq-10.3}

Since the letters are statistically independent, and each is produced by consulting the same probability distribution $X$, we say that the letters are *independent and identically distributed*, abbreviated *i.i.d.* We'll use $X^n$ to denote the ensemble of $n$-letter messages in which each letter is generated independently by sampling from $X$, and $\vec{x} = (x_1 x_2 \dots x_n)$ to denote a string of letters.

Now consider long $n$-letter messages, $n \gg 1$. We ask: is it possible to compress the message to a shorter string of letters that conveys essentially the same information? The answer is: Yes, it's possible, unless the distribution $X$ is uniformly random.

If the alphabet is binary, then each letter is either 0 with probability $1-p$ or 1 with probability $p$, where $0 \le p \le 1$. For $n$ very large, the law of large numbers tells us that typical strings will contain about $n(1-p)$ 0's and about $np$ 1's. The number of distinct strings of this form is of order the binomial coefficient $\binom{n}{np}$, and from the Stirling approximation $\log n! = n \log n - n + O(\log n)$ we obtain

$$
\begin{aligned}
\log \binom{n}{np} &= \log \left( \frac{n!}{(np)! (n(1-p))!} \right) \\
&\approx n \log n - n - (np \log np - np + n(1-p) \log n(1-p) - n(1-p)) \\
&= n H(p),
\end{aligned}
$$ {#eq-10.4}

where

$$
H(p) = -p \log p - (1-p) \log(1-p)
$$ {#eq-10.5}

is the *entropy function*.

In this derivation we used the Stirling approximation in the appropriate form for natural logarithms. But from now on we will prefer to use logarithms with base 2, which

<!-- Page 9 -->
is more convenient for expressing a quantity of information in bits; thus if no base is indicated, it will be understood that the base is 2 unless otherwise stated. Adopting this convention in the expression for $H(p)$, the number of typical strings is of order $2^{nH(p)}$.

To convey essentially all the information carried by a string of $n$ bits, it suffices to choose a block code that assigns a nonnegative integer to each of the typical strings. This block code needs to distinguish about $2^{nH(p)}$ messages (all occurring with nearly equal *a priori* probability), so we may specify any one of the messages using a binary string with length only slightly longer than $nH(p)$. Since $0 \le H(p) \le 1$ for $0 \le p \le 1$, and $H(p) = 1$ only for $p = \frac{1}{2}$, the block code shortens the message for any $p \ne \frac{1}{2}$ (whenever 0 and 1 are not equally probable). This is Shannon's result. The key idea is that we do not need a codeword for every sequence of letters, only for the *typical* sequences. The probability that the actual message is atypical becomes negligible asymptotically, *i.e.*, in the limit $n \to \infty$.

Similar reasoning applies to the case where $X$ samples from a $d$-letter alphabet. In a string of $n$ letters, $x$ typically occurs about $np(x)$ times, and the number of typical strings is of order

$$
\frac{n!}{\prod_x (np(x))!} \simeq 2^{nH(X)},
$$ {#eq-10.6}

where we have again invoked the Stirling approximation and now

$$
H(X) = -\sum_x p(x) \log_2 p(x) = \mathbb{E}_X \left[ \log_2 \frac{1}{p(x)} \right].
$$ {#eq-10.7}

is the *Shannon entropy* (or simply entropy) of the ensemble $X = \{x, p(x)\}$, and $\mathbb{E}_X [\cdot]$ denotes the expectation value defined by this ensemble. Adopting a block code that assigns integers to the typical sequences, the information in a string of $n$ letters can be compressed to about $nH(X)$ bits. In this sense a letter $x$ chosen from the ensemble carries, on the average, $H(X)$ bits of information.

It is useful to restate this reasoning more carefully using the *strong law of large numbers*, which asserts that a sample average for a random variable almost certainly converges to its expected value in the limit of many trials. If we sample from the distribution $Y = \{y, p(y)\}$ $n$ times, let $y_i, i \in \{1, 2, \dots, n\}$ denote the $i$th sample, and let

$$
\mu[Y] = \mathbb{E}_Y [y] = \sum_y y\, p(y)
$$ {#eq-10.8}

denote the expected value of $y$. Then for any positive $\varepsilon$ and $\delta$ there is a positive integer $N$ such that

$$
\left| \frac{1}{n} \sum_{i=1}^n y_i - \mu[Y] \right| \le \delta
$$ {#eq-10.9}

with probability at least $1-\varepsilon$ for all $n \ge N$. We can apply this statement to the random variable $\log_2 p(x)$. Let us say that a sequence of $n$ letters is *$\delta$-typical* if

$$
H(X) - \delta \le -\frac{1}{n} \log_2 p(x_1 x_2 \dots x_n) \le H(X) + \delta;
$$ {#eq-10.10}

then the strong law of large numbers says that for any $\varepsilon, \delta > 0$ and $n$ sufficiently large, an $n$-letter sequence will be $\delta$-typical with probability $\ge 1-\varepsilon$.

<!-- Page 10 -->
Since each $\delta$-typical $n$-letter sequence $\vec{x}$ occurs with probability $p(\vec{x})$ satisfying

$$
p_{\min} = 2^{-n(H+\delta)} \le p(\vec{x}) \le 2^{-n(H-\delta)} = p_{\max},
$$ {#eq-10.11}

we may infer upper and lower bounds on the *number* $N_{\mathrm{typ}}(\varepsilon, \delta, n)$ of typical sequences:

$$
N_{\mathrm{typ}} p_{\min} \le \sum_{\mathrm{typical\ } x} p(x) \le 1, \quad N_{\mathrm{typ}} p_{\max} \ge \sum_{\mathrm{typical\ } x} p(x) \ge 1 - \varepsilon,
$$ {#eq-10.12}

implies

$$
2^{n(H+\delta)} \ge N_{\mathrm{typ}}(\varepsilon, \delta, n) \ge (1 - \varepsilon) 2^{n(H-\delta)}.
$$ {#eq-10.13}

Therefore, we can encode all typical sequences using a block code with length $n(H + \delta)$ bits. That way, any message emitted by the source can be compressed and decoded successfully as long as the message is typical; the compression procedure achieves a success probability $p_{\mathrm{success}} \ge 1 - \varepsilon$, no matter how the atypical sequences are decoded.

What if we try to compress the message even further, say to $H(X) - \delta'$ bits per letter, where $\delta'$ is a constant independent of the message length $n$? Then we'll run into trouble, because there won't be enough codewords to cover all the typical messages, and we won't be able to decode the compressed message with negligible probability of error. The probability $p_{\mathrm{success}}$ of successfully decoding the message will be bounded above by

$$
p_{\mathrm{success}} \le 2^{n(H-\delta')} 2^{-n(H-\delta)} + \varepsilon = 2^{-n(\delta' - \delta)} + \varepsilon.
$$ {#eq-10.14}

We can correctly decode only $2^{n(H-\delta')}$ typical messages, each occurring with probability no higher than $2^{-n(H-\delta)}$; we add $\varepsilon$, an upper bound on the probability of an atypical message, allowing optimistically for the possibility that we somehow manage to decode the atypical messages correctly. Since we may choose $\varepsilon$ and $\delta$ as small as we please, this success probability becomes small as $n \to \infty$, if $\delta'$ is a positive constant.

The number of bits per letter encoding the compressed message is called the *rate* of the compression code, and we say a rate $R$ is *achievable* asymptotically (as $n \to \infty$) if there is a sequence of codes with rate at least $R$ and error probability approaching zero in the limit of large $n$. To summarize our conclusion, we have found that

$$
\begin{aligned}
\text{Compression Rate} &= H(X) + o(1) \text{ is } \textit{achievable}, \\
\text{Compression Rate} &= H(X) - \Omega(1) \text{ is } \textit{not achievable},
\end{aligned}
$$ {#eq-10.15}

where $o(1)$ denotes a positive quantity which may be chosen as small as we please, and $\Omega(1)$ denotes a positive constant. This is Shannon's source coding theorem.

We have not discussed at all the details of the compression code. We might imagine a huge lookup table which assigns a unique codeword to each message and vice versa, but because such a table has size exponential in $n$ it is quite impractical for compressing and decompressing long messages. It is fascinating to study how to make the coding and decoding efficient while preserving a near optimal rate of compression, and quite important, too, if we really want to compress something. But this practical aspect of classical compression theory is beyond the scope of this book.

### 10.1.2 Joint typicality, conditional entropy, and mutual information

The Shannon entropy quantifies my *ignorance* per letter about the output of an information source. If the source $X$ produces an $n$-letter message, then $n(H(X) + o(1))$ bits suffice to convey the content of the message, while $n(H(X) - \Omega(1))$ bits do not suffice.

<!-- Page 11 -->
Two information sources $X$ and $Y$ can be correlated. Letters drawn from the sources are governed by a joint distribution $XY = \{(x, y), p(x, y)\}$, in which a pair of letters $(x, y)$ appears with probability $p(x, y)$. The sources are independent if $p(x, y) = p(x)p(y)$, but correlated otherwise. If $XY$ is a joint distribution, we use $X$ to denote the marginal distribution, defined as

$$
X = \left\{ x, p(x) = \sum_y p(x, y) \right\},
$$ {#eq-10.16}

and similarly for $Y$. If $X$ and $Y$ are correlated, then by reading a message generated by $Y^n$ I reduce my ignorance about a message generated by $X^n$, which should make it possible to compress the output of $X$ further than if I did not have access to $Y$.

To make this idea more precise, we use the concept of *jointly typical sequences*. Sampling from the distribution $X^n Y^n$, that is, sampling $n$ times from the joint distribution $XY$, produces a message $(\vec{x}, \vec{y}) = (x_1 x_2 \dots x_n, y_1 y_2 \dots y_n)$ with probability

$$
p(\vec{x}, \vec{y}) = p(x_1, y_1) p(x_2, y_2) \dots p(x_n, y_n).
$$ {#eq-10.17}

Let us say that $(\vec{x}, \vec{y})$ drawn from $X^n Y^n$ is *jointly $\delta$-typical* if

$$
\begin{aligned}
2^{-n(H(X)+\delta)} &\le p(\vec{x}) \le 2^{-n(H(X)-\delta)}, \\
2^{-n(H(Y)+\delta)} &\le p(\vec{y}) \le 2^{-n(H(Y)-\delta)}, \\
2^{-n(H(XY)+\delta)} &\le p(\vec{x}, \vec{y}) \le 2^{-n(H(XY)-\delta)}.
\end{aligned}
$$ {#eq-10.18}

Then, applying the strong law of large numbers simultaneously to the three distributions $X^n$, $Y^n$, and $X^n Y^n$, we infer that for $\varepsilon, \delta > 0$ and $n$ sufficiently large, a sequence drawn from $X^n Y^n$ will be jointly $\delta$-typical with probability $\ge 1 - \varepsilon$. Using Bayes' rule, we can then obtain upper and lower bounds on the *conditional* probability $p(\vec{x}|\vec{y})$ for jointly typical sequences:

$$
\begin{aligned}
p(\vec{x}|\vec{y}) &= \frac{p(\vec{x}, \vec{y})}{p(\vec{y})} \ge \frac{2^{-n(H(XY)+\delta)}}{2^{-n(H(Y)-\delta)}} = 2^{-n(H(X|Y)+2\delta)}, \\
p(\vec{x}|\vec{y}) &= \frac{p(\vec{x}, \vec{y})}{p(\vec{y})} \le \frac{2^{-n(H(XY)-\delta)}}{2^{-n(H(Y)+\delta)}} = 2^{-n(H(X|Y)-2\delta)}.
\end{aligned}
$$ {#eq-10.19}

Here we have introduced the quantity

$$
H(X|Y) = H(XY) - H(Y) = \mathbb{E}_{XY}[-\log p(x, y) + \log p(y)] = \mathbb{E}_{XY}[-\log p(x|y)],
$$ {#eq-10.20}

which is called the *conditional entropy* of $X$ given $Y$.

The conditional entropy quantifies my remaining ignorance about $x$ once I know $y$. From eq.(10.19) we see that if $(\vec{x}, \vec{y})$ is jointly typical (as is the case with high probability for $n$ large), then the number of possible values for $\vec{x}$ compatible with the known value of $\vec{y}$ is no more than $2^{n(H(X|Y)+2\delta)}$; hence we can convey $\vec{x}$ with a high success probability using only $H(X|Y) + o(1)$ bits per letter. On the other hand we can't do much better, because if we use only $2^{n(H(X|Y)-\delta')}$ codewords, we are limited to conveying reliably no more than a fraction $2^{-n(\delta'-2\delta)}$ of all the jointly typical messages. To summarize, $H(X|Y)$ is the number of *additional* bits per letter needed to specify both $\vec{x}$ and $\vec{y}$ once $\vec{y}$ is known. Similarly, $H(Y|X)$ is the number of additional bits per letter needed to specify both $\vec{x}$ and $\vec{y}$ when $\vec{x}$ is known.

<!-- Page 12 -->
The information about $X$ that I *gain* when I learn $Y$ is quantified by how much the number of bits per letter needed to specify $X$ is *reduced* when $Y$ is known. This is

$$
\begin{aligned}
I(X; Y) &\equiv H(X) - H(X|Y) \\
&= H(X) + H(Y) - H(XY) \\
&= H(Y) - H(Y|X),
\end{aligned}
$$ {#eq-10.21}

which is called the *mutual information*. The mutual information $I(X; Y)$ quantifies how $X$ and $Y$ are correlated, and is symmetric under interchange of $X$ and $Y$: I find out as much about $X$ by learning $Y$ as about $Y$ by learning $X$. Learning $Y$ never *reduces* my knowledge of $X$, so $I(X; Y)$ is obviously nonnegative, and indeed the inequality $H(X) \ge H(X|Y) \ge 0$ follows easily from the concavity of the $\log$ function.

Of course, if $X$ and $Y$ are completely uncorrelated, we have $p(x, y) = p(x)p(y)$, and

$$
I(X; Y) \equiv \left\langle \log \frac{p(x, y)}{p(x)p(y)} \right\rangle = 0;
$$ {#eq-10.22}

we don't find out anything about $X$ by learning $Y$ if there is no correlation between $X$ and $Y$.

### 10.1.3 Distributed source coding

To sharpen our understanding of the operational meaning of conditional entropy, consider this situation: Suppose that the joint distribution $XY$ is sampled $n$ times, where Alice receives the $n$-letter message $\vec{x}$ and Bob receives the $n$-letter message $\vec{y}$. Now Alice is to send a message to Bob which will enable Bob to determine $\vec{x}$ with high success probability, and Alice wants to send as few bits to Bob as possible. This task is harder than in the scenario considered in §10.1.2, where we assumed that the encoder and the decoder share full knowledge of $\vec{y}$, and can choose their code for compressing $\vec{x}$ accordingly. It turns out, though, that even in this more challenging setting Alice can compress the message she sends to Bob down to $n (H(X|Y) + o(1))$ bits, using a method called *Slepian-Wolf coding*.

Before receiving $(\vec{x}, \vec{y})$, Alice and Bob agree to sort all the possible $n$-letter messages that Alice might receive into $2^{nR}$ possible bins of equal size, where the choice of bins is known to both Alice and Bob. When Alice receives $\vec{x}$, she sends $nR$ bits to Bob, identifying the bin that contains $\vec{x}$. After Bob receives this message, he knows both $\vec{y}$ and the bin containing $\vec{x}$. If there is a unique message in that bin which is jointly typical with $\vec{y}$, Bob decodes accordingly. Otherwise, he decodes arbitrarily. This procedure can fail either because $\vec{x}$ and $\vec{y}$ are not jointly typical, or because there is more than one message in the bin which is jointly typical with $\vec{y}$. Otherwise, Bob is sure to decode correctly.

Since $\vec{x}$ and $\vec{y}$ are jointly typical with high probability, the compression scheme works if it is unlikely for a bin to contain an incorrect message which is jointly typical with $\vec{y}$. If $\vec{y}$ is typical, what can we say about the number $N_{\mathrm{typ}|\vec{y}}$ of messages $\vec{x}$ that are jointly typical with $\vec{y}$? Using eq.(10.19), we have

$$
1 \ge \sum_{\mathrm{typical\ } \vec{x}|\vec{y}} p(\vec{x}|\vec{y}) \ge N_{\mathrm{typ}|\vec{y}}\, 2^{-n(H(X|Y)+2\delta)},
$$ {#eq-10.23}

and thus

$$
N_{\mathrm{typ}|\vec{y}} \le 2^{n(H(X|Y)+2\delta)}.
$$ {#eq-10.24}

<!-- Page 13 -->
Now, to estimate the probability of a decoding error, we need to specify how the bins are chosen. Let's assume the bins are chosen uniformly at random, or equivalently, let's consider averaging uniformly over all codes that divide the length-$n$ strings into $2^{nR}$ bins of equal size. Then the probability that a particular bin contains a message jointly typical with a specified $\vec{y}$ purely by accident is bounded above by

$$
2^{-nR} N_{\mathrm{typ}|\vec{y}} \le 2^{-n(R - H(X|Y) - 2\delta)}.
$$ {#eq-10.25}

We conclude that if Alice sends $R$ bits to Bob per each letter of the message $x$, where

$$
R = H(X|Y) + o(1),
$$ {#eq-10.26}

then the probability of a decoding error vanishes in the limit $n \to \infty$, at least when we average uniformly over all codes. Surely, then, there must exist a particular sequence of codes Alice and Bob can use to achieve the rate $R = H(X|Y) + o(1)$, as we wanted to show.

In this scenario, Alice and Bob jointly know $(x, y)$, but initially neither Alice nor Bob has access to all their shared information. The goal is to merge all the information on Bob's side with minimal communication from Alice to Bob, and we have found that $H(X|Y) + o(1)$ bits of communication per letter suffice for this purpose. Similarly, the information can be merged on Alice's side using $H(Y|X) + o(1)$ bits of communication per letter from Bob to Alice. Note that this argument, based on averaging over codes, is nonconstructive; it establishes the existence of a code that achieves the stated communication rate without exhibiting any such code.

### 10.1.4 Relative entropy and hypothesis testing

Here we briefly introduce another useful entropic quantity, the *relative entropy* (also called the Kullback-Leibler divergence), which arises in the context of hypothesis testing. Suppose we sample $n$ times from the distribution $X = \{x, p(x)\}$, where $n$ is very large, but we mistakenly believe that we are sampling instead from a different distribution $Y = \{x, q(x)\}$. With enough samples, we should be able to rule out this incorrect hypothesis with high probability.

To see how this works with minimal distracting details, suppose that $n$ is so large that the sequence drawn from the distribution is $\delta$-typical with probability $1 - \varepsilon$ where $\delta$ and $\varepsilon$ are negligibly small. That is, assume that when we sample $n$ times from $X$, the letter $x$ is drawn exactly $np(x)$ times. Under our hypothesis, then, in which $x$ occurs with probability $q(x)$, the observed sequence $\vec{x}$ has probability

$$
P(\vec{x}) = \prod_{x=0}^{d-1} q(x)^{np(x)} \implies \log P(\vec{x}) = n \sum_{x=0}^{d-1} p(x) \log q(x) = -n \mathbb{E}_p [-\log q(x)];
$$ {#eq-10.27}

that is,

$$
P(\vec{x}) = 2^{-n \mathbb{E}_p [-\log q(x)]}.
$$ {#eq-10.28}

The quantity $\mathbb{E}_p [-\log q(x)]$ is called the *cross entropy* of $q$ relative to $p$.

This expression $P(\vec{x})$ gives the probability for any particular typical sequence $\vec{x}$, and the total number of typical sequences is $2^{nH(X)}$. Therefore, under our hypothesis, the total probability of the observed frequencies, in which the letter $x$ occurs $np(x)$ times, is

$$
\mathrm{Prob} = 2^{nH(X)} P(\vec{x}) = 2^{-nD(p\|q)},
$$ {#eq-10.29}

<!-- Page 14 -->
where

$$
D(p\|q) = \sum_x p(x) (\log p(x) - \log q(x)) = \mathbb{E}_p \left[ \log \frac{p(x)}{q(x)} \right],
$$ {#eq-10.30}

which is called the *relative entropy* of $p$ with respect to $q$.

We see that the relative entropy governs the confidence with which we can rule out the incorrect hypothesis when $n$ is large; in this sense it is a measure of the distinguishability of the two distributions $p(x)$ and $q(x)$. It is not, however, a metric on probability vectors, because it is asymmetric between $p$ and $q$. This asymmetry occurs because $p$ and $q$ have different roles in the hypothesis testing scenario: $p$ is the true distribution and $q$ is the hypothetical one.

Note that since $\mathrm{Prob} = 2^{-nD(p\|q)}$ is a probability and therefore no larger than 1, it follows that the relative entropy is nonnegative,

$$
D(p\|q) \ge 0.
$$ {#eq-10.31}

### 10.1.5 The noisy channel coding theorem

Suppose Alice wants to send a message to Bob, but the communication channel linking Alice and Bob is noisy. Each time they use the channel, Bob receives the letter $y$ with probability $p(y|x)$ if Alice sends the letter $x$. Using the channel $n \gg 1$ times, Alice hopes to transmit a long message to Bob.

Alice and Bob realize that to communicate reliably despite the noise they should use some kind of code. For example, Alice might try sending the same bit $k$ times, with Bob using a majority vote of the $k$ noisy bits he receives to decode what Alice sent. One wonders: for a given channel, is it possible to ensure perfect transmission asymptotically, *i.e.*, in the limit where the number of channel uses $n \to \infty$? And what can be said about the rate of the code; that is, how many bits must be sent per letter of the transmitted message?

Shannon answered these questions. He showed that any channel can be used for perfectly reliable communication at an asymptotic nonzero rate, as long as there is *some* correlation between the channel's input and its output. Furthermore, he found a useful formula for the optimal rate that can be achieved. These results are the content of the *noisy channel coding theorem*.

*Capacity of the binary symmetric channel.*
To be concrete, suppose we use the binary alphabet $\{0, 1\}$, and the *binary symmetric channel*; this channel acts on each bit independently, flipping its value with probability $p$, and leaving it intact with probability $1-p$. Thus the conditional probabilities characterizing the channel are

$$
\begin{aligned}
p(0|0) &= 1-p, & p(0|1) &= p, \\
p(1|0) &= p, & p(1|1) &= 1-p.
\end{aligned}
$$ {#eq-10.32}

We want to construct a family of codes with increasing block size $n$, such that the probability of a decoding error goes to zero as $n \to \infty$. For each $n$, the code contains $2^k$ codewords among the $2^n$ possible strings of length $n$. The rate $R$ of the code, the number of encoded data bits transmitted per physical bit carried by the channel, is

$$
R = \frac{k}{n}.
$$ {#eq-10.33}

<!-- Page 15 -->
To protect against errors, we should choose the code so that the codewords are as "far apart" as possible. For given values of $n$ and $k$, we want to maximize the number of bits that must be flipped to change one codeword to another, the *Hamming distance* between the two codewords. For any $n$-bit input message, we expect about $np$ of the bits to flip — the input diffuses into one of about $2^{nH(p)}$ typical output strings, occupying an "error sphere" of "Hamming radius" $np$ about the input string. To decode reliably, we want to choose our input codewords so that the error spheres of two different codewords do not overlap substantially. Otherwise, two different inputs will sometimes yield the same output, and decoding errors will inevitably occur. To avoid such decoding ambiguities, the total number of strings contained in all $2^k = 2^{nR}$ error spheres should not exceed the total number $2^n$ of bits in the output message; we therefore require

$$
2^{nH(p)} 2^{nR} \le 2^n
$$ {#eq-10.34}

or

$$
R \le 1 - H(p) := C(p).
$$ {#eq-10.35}

If transmission is highly reliable, we cannot expect the rate of the code to exceed $C(p)$. But is the rate $R = C(p)$ actually *achievable* asymptotically?

In fact transmission with $R = C - o(1)$ and negligible decoding error probability is possible. Perhaps Shannon's most ingenious idea was that this rate can be achieved by an average over "random codes." Though choosing a code at random does not seem like a clever strategy, rather surprisingly it turns out that random coding achieves as high a rate as any other coding scheme in the limit $n \to \infty$. Since $C$ is the optimal rate for reliable transmission of data over the noisy channel it is called the *channel capacity*.

Suppose that $X$ is the uniformly random ensemble for a single bit (either 0 with $p = \frac{1}{2}$ or 1 with $p = \frac{1}{2}$), and that we sample from $X^n$ a total of $2^{nR}$ times to generate $2^{nR}$ "random codewords." The resulting code is known by both Alice and Bob. To send $nR$ bits of information, Alice chooses one of the codewords and sends it to Bob by using the channel $n$ times. To decode the $n$-bit message he receives, Bob draws a "Hamming sphere" with "radius" slightly larger than $np$, containing

$$
2^{n(H(p)+\delta)}
$$ {#eq-10.36}

strings. If this sphere contains a unique codeword, Bob decodes the message accordingly. If the sphere contains more than one codeword, or no codewords, Bob decodes arbitrarily.

How likely is a decoding error? For any positive $\delta$, Bob's decoding sphere is large enough that it is very likely to contain the codeword sent by Alice when $n$ is sufficiently large. Therefore, we need only worry that the sphere might contain another codeword just by accident. Since there are altogether $2^n$ possible strings, Bob's sphere contains a fraction

$$
f = \frac{2^{n(H(p)+\delta)}}{2^n} = 2^{-n(C(p)-\delta)},
$$ {#eq-10.37}

of all the strings. Because the codewords are uniformly random, the probability that Bob's sphere contains any particular codeword aside from the one sent by Alice is $f$, and the probability that the sphere contains any one of the $2^{nR} - 1$ invalid codewords is no more than

$$
2^{nR} f = 2^{-n(C(p)-R-\delta)}.
$$ {#eq-10.38}

<!-- Page 16 -->
Since $\delta$ may be as small as we please, we may choose $R = C(p) - c$ where $c$ is any positive constant, and the decoding error probability will approach zero as $n \to \infty$.

When we speak of codes chosen at random, we really mean that we are averaging over many possible codes. The argument so far has shown that the *average* probability of error is small, where we average over the choice of random code, and for each specified code we also average over all codewords. It follows that there must be a particular sequence of codes such that the average probability of error (when we average over the codewords) vanishes in the limit $n \to \infty$. We would like a stronger result — that the probability of error is small for *every* codeword.

To establish the stronger result, let $p_i$ denote the probability of a decoding error when codeword $i$ is sent. For any positive $\varepsilon$ and sufficiently large $n$, we have demonstrated the existence of a code such that

$$
\frac{1}{2^{nR}} \sum_{i=1}^{2^{nR}} p_i \le \varepsilon.
$$ {#eq-10.39}

Let $N_{2\varepsilon}$ denote the number of codewords with $p_i \ge 2\varepsilon$. Then we infer that

$$
\frac{1}{2^{nR}} (N_{2\varepsilon}) 2\varepsilon \le \varepsilon \text{ or } N_{2\varepsilon} \le 2^{nR-1};
$$ {#eq-10.40}

we see that we can throw away at most half of the codewords, to achieve $p_i \le 2\varepsilon$ for *every* codeword. The new code we have constructed has

$$
\mathrm{Rate} = R - \frac{1}{n},
$$ {#eq-10.41}

which approaches $R$ as $n \to \infty$. We have seen, then, that the rate $R = C(p) - o(1)$ is asymptotically achievable with negligible probability of error, where $C(p) = 1 - H(p)$.

*Mutual information as an achievable rate.*
Now consider how to apply this random coding argument to more general alphabets and channels. The channel is characterized by $p(y|x)$, the conditional probability that the letter $y$ is received when the letter $x$ is sent. We fix an ensemble $X = \{x, p(x)\}$ for the input letters, and generate the codewords for a length-$n$ code with rate $R$ by sampling $2^{nR}$ times from the distribution $X^n$; the code is known by both the sender Alice and the receiver Bob. To convey an encoded $nR$-bit message, one of the $2^{nR}$ $n$-letter codewords is selected and sent by using the channel $n$ times. The channel acts independently on the $n$ letters, governed by the same conditional probability distribution $p(y|x)$ each time it is used. The input ensemble $X$, together with the conditional probability characterizing the channel, determines the joint ensemble $XY$ for each letter sent, and therefore the joint ensemble $X^n Y^n$ for the $n$ uses of the channel.

To define a decoding procedure, we use the notion of joint typicality introduced in §10.1.2. When Bob receives the $n$-letter output message $\vec{y}$, he determines whether there is an $n$-letter input codeword $\vec{x}$ jointly typical with $\vec{y}$. If such $\vec{x}$ exists and is unique, Bob decodes accordingly. If there is no $\vec{x}$ jointly typical with $\vec{y}$, or more than one such $\vec{x}$, Bob decodes arbitrarily.

How likely is a decoding error? For any positive $\varepsilon$ and $\delta$, the $(\vec{x}, \vec{y})$ drawn from $X^n Y^n$ is jointly $\delta$-typical with probability at least $1 - \varepsilon$ if $n$ is sufficiently large. Therefore, we need only worry that there might more than one codeword jointly typical with $\vec{y}$.

Suppose that Alice samples $X^n$ to generate a codeword $\vec{x}$, which she sends to Bob using the channel $n$ times. Then Alice samples $X^n$ a second time, producing another

<!-- Page 17 -->
codeword $\vec{x}'$. With probability close to one, both $\vec{y}$ and $\vec{x}'$ are $\delta$-typical. But what is the probability that $\vec{x}'$ is *jointly* $\delta$-typical with $\vec{y}$?

Because the samples are independent, the probability of drawing these two codewords factorizes as $p(\vec{x}', \vec{x}) = p(\vec{x}')p(\vec{x})$, and likewise the channel output $\vec{y}$ when the first codeword is sent is independent of the second channel input $\vec{x}'$, so $p(\vec{x}', \vec{y}) = p(\vec{x}')p(\vec{y})$. From eq.(10.18) we obtain an upper bound on the number $N_{\mathrm{j.t.}}$ of jointly $\delta$-typical $(\vec{x}, \vec{y})$:

$$
1 \ge \sum_{\mathrm{j.t.\ } (\vec{x}, \vec{y})} p(\vec{x}, \vec{y}) \ge N_{\mathrm{j.t.}}\, 2^{-n(H(XY)+\delta)} \implies N_{\mathrm{j.t.}} \le 2^{n(H(XY)+\delta)}.
$$ {#eq-10.42}

We also know that each $\delta$-typical $\vec{x}'$ occurs with probability $p(\vec{x}') \le 2^{-n(H(X)-\delta)}$ and that each $\delta$-typical $\vec{y}$ occurs with probability $p(\vec{y}) \le 2^{-n(H(Y)-\delta)}$. Therefore, the probability that $\vec{x}'$ and $\vec{y}$ are jointly $\delta$-typical is bounded above by

$$
\begin{aligned}
\sum_{\mathrm{j.t.\ } (\vec{x}', \vec{y})} p(\vec{x}') p(\vec{y}) &\le N_{\mathrm{j.t.}}\, 2^{-n(H(X)-\delta)} 2^{-n(H(Y)-\delta)} \\
&\le 2^{n(H(XY)+\delta)} 2^{-n(H(X)-\delta)} 2^{-n(H(Y)-\delta)} \\
&= 2^{-n(I(X; Y) - 3\delta)}.
\end{aligned}
$$ {#eq-10.43}

If there are $2^{nR}$ codewords, all generated independently by sampling $X^n$, then the probability that *any* other codeword besides $\vec{x}$ is jointly typical with $\vec{y}$ is bounded above by

$$
2^{nR} 2^{-n(I(X; Y) - 3\delta)} = 2^{n(R - I(X; Y) + 3\delta)}.
$$ {#eq-10.44}

Since $\varepsilon$ and $\delta$ are as small as we please, we may choose $R = I(X; Y) - c$, where $c$ is any positive constant, and the decoding error probability will approach zero as $n \to \infty$.

So far we have shown that the error probability is small when we average over codes and over codewords. To complete the argument we use the same reasoning as in our discussion of the capacity of the binary symmetric channel. There must exist a particular sequence of codes with zero error probability in the limit $n \to \infty$, when we average over codewords. And by pruning the codewords, reducing the rate by a negligible amount, we can ensure that the error probability is small for *every* codeword. We conclude that the rate

$$
R = I(X; Y) - o(1)
$$ {#eq-10.45}

is asymptotically achievable with negligible probability of error. This result provides a concrete operational interpretation for the mutual information $I(X; Y)$; it is the information per letter we can transmit over the channel, supporting the heuristic claim that $I(X; Y)$ quantifies the information we gain about $X$ when we have access to $Y$.

The mutual information $I(X; Y)$ depends not only on the channel's conditional probability $p(y|x)$ but also on the *a priori* probability $p(x)$ defining the codeword ensemble $X$. The achievability argument for random coding applies for any choice of $X$, so we have demonstrated that errorless transmission over the noisy channel is possible for any rate $R$ strictly less than

$$
C := \max_X I(X; Y).
$$ {#eq-10.46}

This quantity $C$ is called the *channel capacity*; it depends only on the conditional probabilities $p(y|x)$ that define the channel.

<!-- Page 18 -->
*Upper bound on the capacity.*
We have now shown that any rate $R < C$ is achievable, but can $R$ exceed $C$ with the error probability still approaching 0 for large $n$? To see that a rate for errorless transmission exceeding $C$ is not possible, we reason as follows.

Consider any code with $2^{nR}$ codewords, and consider the uniform ensemble on the codewords, denoted $\tilde{X}^n$, in which each codeword occurs with probability $2^{-nR}$. Evidently, then,

$$
H(\tilde{X}^n) = nR.
$$ {#eq-10.47}

Sending the codewords through $n$ uses of the channel we obtain an ensemble $\tilde{Y}^n$ of output states, and a joint ensemble $\tilde{X}^n \tilde{Y}^n$.

Because the channel acts on each letter independently, the conditional probability for $n$ uses of the channel factorizes:

$$
p(y_1 y_2 \dots y_n | x_1 x_2 \dots x_n) = p(y_1|x_1) p(y_2|x_2) \dots p(y_n|x_n),
$$ {#eq-10.48}

and it follows that the conditional entropy satisfies

$$
\begin{aligned}
H(\tilde{Y}^n | \tilde{X}^n) = \langle -\log p(\vec{y}|\vec{x}) \rangle &= \sum_i \langle -\log p(y_i|x_i) \rangle \\
&= \sum_i H(\tilde{Y}_i | \tilde{X}_i),
\end{aligned}
$$ {#eq-10.49}

where $\tilde{X}_i$ and $\tilde{Y}_i$ are the marginal probability distributions for the $i$th letter determined by our distribution on the codewords. Because Shannon entropy is subadditive, $H(XY) \le H(X) + H(Y)$, we have

$$
H(\tilde{Y}^n) \le \sum_i H(\tilde{Y}_i),
$$ {#eq-10.50}

and therefore

$$
\begin{aligned}
I(\tilde{Y}^n; \tilde{X}^n) &= H(\tilde{Y}^n) - H(\tilde{Y}^n | \tilde{X}^n) \\
&\le \sum_i (H(\tilde{Y}_i) - H(\tilde{Y}_i | \tilde{X}_i)) \\
&= \sum_i I(\tilde{Y}_i; \tilde{X}_i) \le nC.
\end{aligned}
$$ {#eq-10.51}

The mutual information of the messages sent and received is bounded above by the sum of the mutual information per letter, and the mutual information for each letter is bounded above by the capacity, because $C$ is defined as the maximum of $I(X; Y)$ over all input ensembles.

Recalling the symmetry of mutual information, we have

$$
\begin{aligned}
I(\tilde{X}^n; \tilde{Y}^n) &= H(\tilde{X}^n) - H(\tilde{X}^n | \tilde{Y}^n) \\
&= nR - H(\tilde{X}^n | \tilde{Y}^n) \le nC.
\end{aligned}
$$ {#eq-10.52}

Now, if we can decode reliably as $n \to \infty$, this means that the input codeword is completely determined by the signal received, or that the conditional entropy of the input (per letter) must get small

$$
\frac{1}{n} H(\tilde{X}^n | \tilde{Y}^n) \to 0.
$$ {#eq-10.53}

<!-- Page 19 -->
If errorless transmission is possible, then, eq. (10.52) becomes

$$
R \le C + o(1),
$$ {#eq-10.54}

in the limit $n \to \infty$. The asymptotic rate cannot exceed the capacity. In Exercise 10.15, you will sharpen the statement eq.(10.53), showing that

$$
\frac{1}{n} H(\tilde{X}^n | \tilde{Y}^n) \le \frac{1}{n} H_2(p_e) + p_e R,
$$ {#eq-10.55}

where $p_e$ denotes the decoding error probability, and $H_2(p_e) = -p_e \log_2 p_e - (1-p_e) \log_2(1-p_e)$.

We have now seen that the capacity $C$ is the highest achievable rate of communication through the noisy channel, where the probability of error goes to zero as the number of letters in the message goes to infinity. This is Shannon's noisy channel coding theorem. What is particularly remarkable is that, although the capacity is achieved by messages that are many letters in length, we have obtained a *single-letter formula* for the capacity, expressed in terms of the optimal mutual information $I(X; Y)$ for just a single use of the channel.

The method we used to show that $R = C - o(1)$ is achievable, averaging over random codes, is not constructive. Since a random code has no structure or pattern, encoding and decoding are unwieldy, requiring an exponentially large code book. Nevertheless, the theorem is important and useful, because it tells us what is achievable, and not achievable, in principle. Furthermore, since $I(X; Y)$ is a concave function of $X = \{x, p(x)\}$ (with $\{p(y|x)\}$ fixed), it has a unique local maximum, and $C$ can often be computed (at least numerically) for channels of interest. Finding codes which can be efficiently encoded and decoded, and come close to achieving the capacity, is a very interesting pursuit, but beyond the scope of our lightning introduction to Shannon theory.
