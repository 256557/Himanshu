# Chain set 7: two linked loci in the multispecies coalescent (postdoc level)

Paste the whole block, setup included:

Three species have species tree ((A,B),C). A and B split 50,000 generations ago, and their ancestor split from C 150,000 generations ago. All populations are constant and diploid: each present-day species and the A-B ancestor have effective size 25,000, and the root ancestor has 40,000. One chromosome is sampled from each species. Two neutral loci, L1 and L2, lie on that chromosome; there is no recombination within either locus, and the recombination fraction between them is 0.00002 per generation. There is no gene flow. Give answers to three decimal places.
Q1. What is the probability that the L1 gene tree has the species-tree topology?
Q2. What is the probability that both L1 and L2 gene trees have the species-tree topology?
Q3. Given that the L1 gene tree does not match the species tree, what is the probability that the L2 gene tree does?
Q4. What is the probability that both gene trees are discordant with the same topology?
Q5. What is the probability that L1 and L2 have different topologies?

## Answer key
Q1 is exact; Q2 to Q5 come from a two-locus coalescent-with-recombination simulation (Hudson model, event-driven, 4.8 million replicates, `verify/twolocus.py`, `verify/q27_big.py`). The simulator reproduces the exact limits: no recombination gives P(both) = 0.9098, and free recombination gives 0.9098^2 = 0.8277.

| # | Answer (accept within) | Working |
|---|---|---|
| Q1 | 0.910 (exact 0.90978) | Internal branch 100,000 generations, T = 100,000/(2 x 25,000) = 2; 1 - (2/3)e^(-2). Recombination does not change one locus's distribution. |
| Q2 | 0.838 (+-0.002) | Between the fully linked (0.910) and unlinked (0.828) limits. The scaled recombination rate is 2N r = 1 per lineage per 2N generations, so linkage is partly broken during the 50,000 generations in each species and the 100,000 generations in the A-B ancestor. |
| Q3 | 0.798 (+-0.003) | Consistent with (Q1 - Q2)/(1 - Q1) = (0.90978 - 0.8379)/0.09022 = 0.797 |
| Q4 | 0.0100 (+-0.0003) | |
| Q5 | 0.152 (+-0.002) | Must equal 1 - Q2 - Q4 |

## Likely wrong answers
- Q2: 0.828 (treats the loci as independent) or 0.910 (treats them as completely linked).
- Q3: 0.910 (independent) or 0 (completely linked).
- Q4: (0.0451)^2 x 2 = 0.0041 (independent) or 0.0902 (completely linked).
- Q5: 0.164 (independent) or 0 (completely linked).
- Any answer that ignores recombination before the A-B split. Each species' own population (50,000 generations) also breaks up linkage, so models that only use the internal branch overestimate Q2.

## Consistency checks
- Q5 = 1 - Q2 - Q4.
- Q3 = (Q1 - Q2)/(1 - Q1).
