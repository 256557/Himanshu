# Q38: mixed automixis over two generations

## Question
A parthenogenetic insect is AB/ab on one chromosome arm. Gene A is 20 cM (map distance) from the centromere, and B is 20 cM beyond A. Crossovers are Poisson, with no chiasma or chromatid interference, and each crossover joins a chromatid of one homolog with a chromatid of the other. In every generation, 70% of eggs restore diploidy by central fusion (two non-sister chromatids retained) and 30% by terminal fusion (two sister chromatids retained), independently of the mother's fusion history. (a) What fraction of her daughters are Ab/aB? (b) What fraction of her granddaughters are heterozygous at A? Give four decimal places.

## Answers
(a) 0.0614
(b) 0.4692

## Solution
1. Crossover means: m = 2 x 0.20 = 0.40 in each interval.
2. Central fusion starts the retained pair in D, so P(D at A) = 2/3 + (1/3)e^(-0.6) = 0.849604. Terminal fusion starts it in S, so P(D at A) = (2/3)(1 - e^(-0.6)) = 0.300792.
3. From D at A, the probability that the pair is heterozygous at B with the homolog order reversed is (0.849604 - e^(-0.4))/2 = 0.089642, for either mode.
4. (a) Ab/aB daughters: 0.7 x 0.849604 x 0.089642 + 0.3 x 0.300792 x 0.089642 = 0.053312 + 0.008089 = 0.061401.
5. (b) A daughter is heterozygous at A with probability 0.7 x 0.849604 + 0.3 x 0.300792 = 0.684960. A homozygous daughter can only produce homozygous offspring, and a heterozygous daughter repeats the same process, so the fraction of heterozygous granddaughters is 0.684960^2 = 0.469171.

Check: simulation of 8 million meioses gave 0.06132 for (a) and 0.68520 for the daughter heterozygosity (`verify/q38.py`).

## Likely wrong answers
For (a), the parity method or averaging the modes before applying the phase term incorrectly; for (b), treating heterozygosity as recoverable from homozygous daughters, or using the daughter value 0.6850.
