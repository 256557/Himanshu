# Q38 solution: heterozygosity at A among granddaughters under mixed automixis

## 1. Crossover frequency in the centromere-A interval
Map distance is additive and equals half the mean number of crossovers per bivalent. The centromere-A interval measures 0.20 M, so the number of crossovers in it is Poisson with mean m = 2 x 0.20 = 0.40. Gene B lies distal to A and does not affect heterozygosity at A.

## 2. State model for the retained chromatid pair
At locus A the two retained chromatids carry either the same parental homolog (state S, homozygous) or different homologs (state D, heterozygous). At any position two strands carry material from each homolog, and each crossover joins one strand of each class, with the four pairings equally likely.
1. In state S, every crossover involves exactly one retained chromatid, and the pair moves to D.
2. In state D, a crossover involves exactly one retained chromatid with probability 1/2, which moves the pair to S; otherwise it involves both or neither, and the pair remains in D.

Because the outcome of each crossover depends on the current state, the two retained chromatids cannot be treated as independent.

## 3. Transition probabilities over the interval
Let PD(k) be the probability of state D after k crossovers. The rules in section 2 give PD(k+1) = 1 - PD(k)/2, whose solution approaches 2/3 geometrically with ratio -1/2. Averaging over a Poisson number of crossovers with mean m gives:
1. from S, P(D) = (2/3)(1 - e^(-3m/2));
2. from D, P(D) = 2/3 + (1/3)e^(-3m/2).

## 4. Central fusion
Central fusion retains two non-sister chromatids, which carry different homologs at the centromere (state D). With m = 0.40,

P(heterozygous at A) = 2/3 + (1/3)e^(-0.6) = 0.666667 + 0.182937 = 0.849604.

## 5. Terminal fusion
Terminal fusion retains two sister chromatids, which carry the same homolog at the centromere (state S). With m = 0.40,

P(heterozygous at A) = (2/3)(1 - e^(-0.6)) = (2/3)(0.451188) = 0.300792.

## 6. Transmission of heterozygosity per generation
Each egg is formed by central fusion with probability 0.7 and by terminal fusion with probability 0.3, so a heterozygous mother produces a heterozygous daughter with probability

f = 0.7 x 0.849604 + 0.3 x 0.300792 = 0.594723 + 0.090238 = 0.684960.

## 7. Recurrence over generations
A mother homozygous at A carries the same allele on all four chromatids, so every daughter she produces is homozygous. A heterozygous daughter produces heterozygous offspring with the same probability f, because the fusion mode is chosen independently in each generation. The fraction heterozygous after n generations is therefore Hn = f^n, starting from H0 = 1.

## 8. Result
H2 = 0.684960^2 = 0.469171, which is 0.4692 to four decimal places.

## Consistency check
The value of f lies between the terminal-fusion and central-fusion values, 0.300792 and 0.849604, as a weighted average must. A simulation of 8 million meioses gave a daughter heterozygosity of 0.68520 (`verify/q38.py`).

## Answer
0.4692
