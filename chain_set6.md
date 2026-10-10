# Chain set 6: gene trees in a species tree (multispecies coalescent)

Paste the whole block, setup included:

Three species have species tree ((A,B),C). A and B split 1.0 million years ago, and their common ancestor split from C 3.0 million years ago. The generation time is 20 years. The effective population size (diploid, equal sex ratio, constant) is 25,000 in the A-B ancestral population and 40,000 in the root ancestral population. Sample one gene copy per species. Loci are neutral, with no gene flow and no recombination within a locus; the mutation rate is 1e-8 per site per generation. Give answers to four significant figures.
Q1. What is the probability that an autosomal gene tree has the same topology as the species tree?
Q2. What is the probability that an autosomal gene tree groups B with C?
Q3. Same as Q1, for an X-linked locus.
Q4. Same as Q1, for a mitochondrial locus.
Q5. What is the expected autosomal sequence divergence (per site) between A and B?
Q6. Among autosomal loci whose gene tree groups A with B, what is the expected time (in generations) back to the A-B common ancestor?

## Answer key (formulas plus coalescent simulation of 1,000,000 loci, `verify/chain6.py`)
| # | Answer | Working |
|---|---|---|
| Q1 | 0.9098 | Internal branch = 2 Myr = 100,000 generations; T = 100,000 / (2 x 25,000) = 2; P = 1 - (2/3)e^(-2) |
| Q2 | 0.04511 | (1/3)e^(-2) |
| Q3 | 0.9537 | X-linked: coalescence rate 1/(1.5 N), T = 100,000/37,500 = 2.667; 1 - (2/3)e^(-2.667) |
| Q4 | 0.9998 | mtDNA: haploid, maternal; N_f = 12,500, T = 100,000/12,500 = 8; 1 - (2/3)e^(-8) = 0.99978 |
| Q5 | 0.002081 | E[T_AB] = t1 + 2N_AB(1 - e^(-T)) + e^(-T) x 2N_root = 50,000 + 43,233 + 10,827 = 104,060; d = 2 mu E[T_AB] |
| Q6 | 88,930 (88,926) | Concordant either by coalescing in the A-B ancestor (prob 0.864665, mean time t1 + E[X given X < t] = 50,000 + 34,348) or by A and B coalescing first in the root (prob e^(-2)/3 = 0.045112, mean t2 + 2N_root/3 = 176,667). Weighted mean / 0.909776 = 88,926 |

Simulation: Q1 0.9100, Q2 0.04493, Q5 0.002081, Q6 88,963.

## Likely wrong answers
- Q1: using T = t/N (0.9887) or t/(4N) (0.7547), or forgetting to convert years to generations.
- Q3: treating X like autosomes (0.9098) or using 3/4 in the wrong direction (T = 1.5, 0.8512).
- Q4: using N/4 on the wrong side (T = 0.5, 0.5957).
- Q5: 2mu(t1 + 2N_AB) = 0.002000 (ignores the root population), or 2mu t1 = 0.001000 (ignores ancestral polymorphism).
- Q6: the unconditional mean, 104,060 (ignores the condition), or t1 + 2N_AB = 100,000.
