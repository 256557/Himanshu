# Question

A parthenogenetic insect reproduces by terminal fusion, so each daughter keeps two sister chromatids. Genes A and B are on the same chromosome arm. A is 20 cM (map distance) from the centromere, and B is 20 cM beyond A. Crossovers are Poisson, with no chiasma or chromatid interference, and each crossover joins a chromatid of one homolog with a chromatid of the other. The mother is AB/ab. What fraction of her daughters are Ab/aB? Give four decimal places.

# Solution

## Step 1. States
Follow the two sister chromatids the daughter keeps. At any point they carry the same homolog (S) or different homologs (D). D has two phases: the chromatids carry homologs in the same order as at A (D0) or in the reverse order (D1).

## Step 2. Transition rule
A crossover from S always gives D. From D it gives S with probability 1/2 and reverses the phase with probability 1/4. With Poisson mean m = 2x for x Morgans, the phase difference P(D0) - P(D1) decays as e^(-m).

## Step 3. Centromere to A
The chromatids start in S, and m1 = 0.4. The probability of D at A is (2/3)(1 - e^(-0.6)) = 0.300792. This D state is the heterozygote A/a.

## Step 4. A to B
Starting from D at A, m2 = 0.4. The probability of D at B is 2/3 + e^(-0.6)/3 = 0.849604, and the phase difference is e^(-0.4) = 0.670320. The daughter is Ab/aB only if the phase is reversed, with probability (0.849604 - 0.670320)/2 = 0.089642.

## Step 5. Result
The fraction is 0.300792 x 0.089642 = 0.026964, or 0.0270.

## Remark
The phase at B remembers the phase at A, so repulsion daughters are much rarer than coupling daughters (0.2286). Independent parity counts for each chromatid give 0.0075, because they ignore that the state, not each chromatid, controls which crossovers change the genotype.

# Answer

0.0270
