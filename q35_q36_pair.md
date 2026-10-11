# Q35 and Q36: linked pair on automixis and phase

## Questions (paste together)
A parthenogenetic insect is AB/ab on one chromosome arm. Gene A is 20 cM (map distance) from the centromere, and B is 20 cM beyond A. Crossovers are Poisson, with no chiasma or chromatid interference, and each crossover joins a chromatid of one homolog with a chromatid of the other. Give answers to four decimal places.
1. If each egg restores diploidy by terminal fusion, so that a daughter keeps two sister chromatids, what fraction of daughters are Ab/aB?
2. If instead each egg restores diploidy by central fusion, so that a daughter keeps two non-sister chromatids, what fraction of daughters are Ab/aB?

## Answers
1. 0.0270
2. 0.0762

## Solution

### Step 1. States
Follow the two chromatids a daughter keeps. At any point they carry the same homolog (S) or different homologs (D). In D, the pair carries the homologs either in the same order as at A or in the reverse order.

### Step 2. Transition rule
With Poisson mean m = 2x for x Morgans:
1. from S, P(D) = (2/3)(1 - e^(-3m/2));
2. from D, P(D) = 2/3 + (1/3)e^(-3m/2);
3. the difference between the probabilities of keeping and reversing the order is e^(-m).

From D, the probability of being in D with reversed order after the interval is therefore (P(D) - e^(-m))/2.

### Step 3. The interval from A to B
Here m = 0.4, so P(D) = 2/3 + e^(-0.6)/3 = 0.849604 and e^(-0.4) = 0.670320. A daughter that is A/a at A becomes Ab/aB with probability (0.849604 - 0.670320)/2 = 0.089642. This factor is the same for both modes of fusion, because the process depends only on the state at A.

### Step 4. Terminal fusion
The pair starts in S at the centromere. With m = 0.4, P(D at A) = (2/3)(1 - e^(-0.6)) = 0.300792. The answer is 0.300792 x 0.089642 = 0.026964.

### Step 5. Central fusion
The pair starts in D. With m = 0.4, P(D at A) = 0.849604. The answer is 0.849604 x 0.089642 = 0.076160.

### Check
Simulation of 8 million meioses gave 0.02693 and 0.07616 (`verify/q36.py`).

## Likely wrong answers
Counting crossovers on each chromatid independently (the parity method) gives 0.0075 and 0.0197. Treating the phase at B as unrelated to the phase at A gives half of all double heterozygotes, 0.1278 and 0.3610.
