# Set 12: mitotic recombination and twin spots

## Question
A Drosophila female is y + / + sn on the X chromosome, where y (yellow) lies distal to sn (singed) and both are recessive. In a population of wing cells, each cell undergoes exactly one mitotic crossover in G2: 80% of crossovers fall between the centromere and sn, and 20% between sn and y. Each crossover joins a chromatid of one homolog with a chromatid of the other, and at anaphase each daughter cell receives one chromatid of each homolog at random. What fractions of these cells give rise to (a) a twin spot of yellow beside singed tissue, (b) a single yellow spot, and (c) a single singed spot?

## Answer
(a) 0.40, (b) 0.10, (c) 0. The remaining 0.50 give no spot.

## Solution

### Step 1. Crossover between the centromere and sn
The exchange moves both markers, so one centromere carries chromatids y + and + sn, and so does the other. If the two y + chromatids go to one daughter, that daughter is yellow and the other is singed, which is a twin spot. The alternative segregation gives two heterozygous daughters. Each outcome has probability 1/2, so this class gives 0.8 x 1/2 = 0.40 twin spots.

### Step 2. Crossover between sn and y
Only y is exchanged. One centromere carries y + and + +, and the other carries y sn and + sn. With probability 1/2 the y + and y sn chromatids go together, giving a yellow cell beside a wild-type cell; otherwise both daughters are heterozygous. This class gives 0.2 x 1/2 = 0.10 single yellow spots.

### Step 3. Single singed spots
A cell homozygous for sn but not y requires sn to be exchanged without y, which needs two crossovers. With exactly one crossover the fraction is 0.

### Check
Simulation of 1 million cells gave 0.4001, 0.1001 and 0 (`verify/set12_twinspot.py`).

## Likely wrong answers
(a) 0.80 and (b) 0.20, from ignoring that half of all segregations restore heterozygosity; or a non-zero value for (c), from treating the two markers symmetrically.
