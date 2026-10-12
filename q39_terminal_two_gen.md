# Q39: terminal fusion over two generations

## Question
A parthenogenetic insect is heterozygous Aa at a locus 40 cM (map distance) from the centromere. Crossovers are Poisson, with no chiasma or chromatid interference, and each crossover joins a chromatid of one homolog with a chromatid of the other. Every egg restores diploidy by terminal fusion, so each daughter keeps two sister chromatids. What fraction of her granddaughters are heterozygous at A? Give four decimal places.

## Answer
0.2170

## Solution

### 1. Crossover frequency
Map distance equals half the mean number of crossovers per bivalent, so the centromere-A interval (0.40 M) carries a Poisson number of crossovers with mean m = 0.80.

### 2. State of the retained chromatids
Sister chromatids carry the same homolog at the centromere (state S). Each crossover joins one strand of each homolog's material at that position. From S, every crossover involves exactly one retained chromatid and produces state D. From D, a crossover returns the pair to S with probability 1/2.

### 3. Heterozygosity in one generation
Starting from S, the probability of D after a Poisson number of crossovers with mean m is (2/3)(1 - e^(-3m/2)). With m = 0.80,

P(heterozygous daughter) = (2/3)(1 - e^(-1.2)) = (2/3)(0.698806) = 0.465871.

### 4. Second generation
A homozygous daughter produces only homozygous offspring, and a heterozygous daughter repeats the same process. The fraction of heterozygous granddaughters is 0.465871^2 = 0.217035.

### Check
Simulation of 8 million meioses gave 0.46629 for daughters (`verify/q39.py`).

## Answer
0.2170

## Likely wrong answers
Using m = 0.40 with the formula (1 - e^(-2m))/2 gives 0.0758. Treating the two sister chromatids as independent gives 0.1592. Both differ from the correct value by a wide margin.
