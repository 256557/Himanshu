# Q35 solution: terminal fusion, AB/ab mother, Ab/aB daughters

## Step 1. Crossover means from map distance
Map distance is additive and equals half the mean number of crossovers per meiosis. Each interval is 20 cM, or 0.20 Morgans, so the number of crossovers in the four-strand bundle is Poisson with mean m = 2 x 0.20 = 0.40 in each interval. No mapping-function conversion is needed, because the distance is given as map distance rather than as a recombination fraction.

## Step 2. What the daughter carries
Terminal fusion joins the egg nucleus with its sister product of the second division. The daughter therefore keeps two sister chromatids, which carry the same homolog at the centromere.

## Step 3. States of the chromatid pair
At any point along the arm, the two kept chromatids carry either the same homolog (state S, homozygous) or different homologs (state D, heterozygous). For a double heterozygote, D has two phases: the chromatid carrying the A-homolog at A also carries the B-homolog at B (coupling, AB/ab), or it carries the b-homolog at B (repulsion, Ab/aB).

## Step 4. Effect of one crossover
At any point two strands carry material of one homolog and two carry material of the other, and each crossover joins one strand of each kind, with all four pairings equally likely.
1. From S, the two kept chromatids carry the same material, so exactly one of them is involved in every crossover. The pair always moves to D.
2. From D, the crossover involves both kept chromatids with probability 1/4, which swaps their material and reverses the phase. It involves one of them with probability 1/2, which moves the pair to S. It involves neither with probability 1/4, which leaves the pair unchanged.

The two chromatids therefore cannot be treated as independent, and counting crossovers on each one separately gives the wrong answer.

## Step 5. Probabilities over an interval
With a Poisson number of crossovers of mean m:
1. from S, P(D) = (2/3)(1 - e^(-3m/2));
2. from D, P(D) = 2/3 + (1/3)e^(-3m/2);
3. starting from D in a given phase, P(same phase) - P(reversed phase) = e^(-m).

## Step 6. Centromere to A
The pair starts in S, and m = 0.40:
P(D at A) = (2/3)(1 - e^(-0.6)) = (2/3)(0.451188) = 0.300792.

## Step 7. A to B
The pair starts in D at A, and m = 0.40:
P(D at B) = 2/3 + (1/3)e^(-0.6) = 0.666667 + 0.182937 = 0.849604;
P(same phase) - P(reversed phase) = e^(-0.4) = 0.670320.
The probability of D with reversed phase is (0.849604 - 0.670320)/2 = 0.089642.

## Step 8. Result
P(Ab/aB) = 0.300792 x 0.089642 = 0.026964, which is 0.0270 to four decimal places.

## Check
A simulation of 8 million meioses, applying the crossover rule of Step 4 to each strand pair directly, gave 0.02693 (`verify/q36.py`). Counting crossovers on each chromatid independently gives 0.0075 even with the correct mean.

## Answer
0.0270
