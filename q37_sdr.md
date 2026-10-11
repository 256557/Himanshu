# Q37: SDR 2n eggs, repulsion mother

## Question
A plant heterozygous Ab/aB produces unreduced (2n) eggs by second-division restitution, so each egg keeps two sister chromatids. Gene A is 15 cM (map distance) from the centromere, and B is 25 cM beyond A on the same arm. Crossovers are Poisson, with no chiasma or chromatid interference, and each crossover joins a chromatid of one homolog with a chromatid of the other. What fraction of the 2n eggs are AB/ab? Give five decimal places.

## Answer
0.02628

## Solution
1. Crossover means: m1 = 2 x 0.15 = 0.30 (centromere to A) and m2 = 2 x 0.25 = 0.50 (A to B).
2. Sister chromatids start on the same homolog (state S). An AB/ab egg is heterozygous at both loci with the homolog order reversed between A and B, because the mother carries A with b and a with B.
3. Centromere to A: P(D at A) = (2/3)(1 - e^(-0.45)) = 0.241581.
4. A to B, starting from D: P(D) = 2/3 + (1/3)e^(-0.75) = 0.824122, and P(same order) - P(reversed order) = e^(-0.5) = 0.606531, so P(D, reversed) = (0.824122 - 0.606531)/2 = 0.108796.
5. Result: 0.241581 x 0.108796 = 0.026283, or 0.02628.

Check: simulation of 8 million meioses gave 0.02636 (`verify/q37.py`).

## Likely wrong answers
Treating AB/ab as the parental (coupling) arrangement and using the same-order term, (0.824122 + 0.606531)/2 x 0.241581 = 0.17281; or counting crossovers on each chromatid independently.
