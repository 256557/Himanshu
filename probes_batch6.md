# Probe batch 6: hard, linked events (the pattern behind the half-tetrad weakness)

## Questions (type as written)

F1. Two loci have a recombination fraction of 0.1. What is the probability that two full siblings share both alleles identical by descent at both loci? Give four decimal places.
F2. Two loci have a recombination fraction of 0.1. What is the probability that two full siblings share at least one allele identical by descent at each of the two loci? Give four decimal places.
F3. An AB/ab F1 plant is selfed by single-seed descent until the lines are fully inbred. The loci have a recombination fraction of 0.1. What fraction of the inbred lines are recombinant (Ab or aB)? Give four decimal places.
F4. The same AB/ab cross is inbred instead by repeated brother-sister mating until fixation. What fraction of the lines are recombinant? Give four decimal places.
F5. In a diploid population of constant size N = 1000, what is the expected time, in generations, back to the most recent common ancestor of three sampled gene copies?

## Answer key (do not show to the model)

| # | Answer | Likely wrong answer | Why |
|---|---|---|---|
| F1 | 0.1681 | 0.0625 (1/16) | Per parent: P(same grandparental copy at both loci) = (1/2)(r^2 + (1-r)^2) = 0.41. Both parents: 0.41^2. Treating the loci as independent gives (1/4)^2. |
| F2 | 0.6681 | 0.5625 (9/16) | Per parent, the sharing indicators at the two loci are correlated (both 0.41, neither 0.41, one only 0.09 each). Treating the loci as independent gives (3/4)^2. |
| F3 | 0.1667 (1/6) | 0.1 or 0.19 | Haldane-Waddington: R = 2r / (1 + 2r). Recombination keeps acting over several generations. |
| F4 | 0.2500 | 0.1667 or 0.1 | Haldane-Waddington for sib mating: R = 4r / (1 + 6r). |
| F5 | about 2667 | 4000 or 2000 | E[T_MRCA] = 4N(1 - 1/n) = 4000 x 2/3. 4000 is the limit for a very large sample, and 2000 is the answer for two copies. |

Verified by simulation (`verify/batch6.py`): F1 0.1673, F2 0.6681, F3 0.1647, F4 0.2485, all within simulation error of the formulas. F2 also computed exactly.
