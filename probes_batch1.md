# Probe batch 1: short questions with a hidden trap

Each question is short and gives no hint about the trap. Ask them one at a time and record Model A's answer.

## Questions (type as written)

P1. A woman's parents are paternal half-siblings: they have the same father but different mothers. What is her inbreeding coefficient at an X-linked locus?

P2. In a population at Hardy-Weinberg equilibrium, 8% of males are red-green color-blind. A woman's father has normal color vision. What is the probability that her first son is color-blind? Give four decimal places.

P3. Cystic fibrosis carrier frequency is 1/25. A healthy woman has a brother with cystic fibrosis, and both her parents are healthy. She has one healthy child with a healthy man who has no family history. What is the probability that their next child has cystic fibrosis? Give four decimal places.

P4. In the snail Lymnaea, shell coiling is set by the mother's genotype, and dextral (D) is dominant to sinistral (d). A dd snail is fertilized by a DD snail. The offspring are selfed for two generations. What fraction of the F3 snails coil sinistrally?

P5. In Drosophila, recessive genes a and b lie 20 map units apart on chromosome 2. An A B / a b female is crossed with an A b / a B male. What fraction of the progeny show both recessive phenotypes?

## Answer key (do not show to the model)

| # | Answer | Trap |
|---|---|---|
| P1 | 0 | Her father is the half-brother, and he got his X from his mother, not from the shared father. So no X path runs through the common ancestor. The autosomal answer, 1/8, is wrong here. |
| P2 | 0.0400 | Her paternal X is normal, and her maternal X is a random population X, so P(carrier) = q = 0.08 and P(son affected) = 0.08 x 1/2 = 0.04. Using 2pq / (1 - q^2) = 0.1600 for "a normal woman" ignores the information about her father and gives 0.0800. |
| P3 | 0.0050 (3/596 = 0.005034) | The healthy child is evidence against both parents being carriers. Prior P(both carriers) = 2/3 x 1/25 = 2/75. Posterior = (2/75 x 3/4) / (2/75 x 3/4 + 73/75) = 3/149. Times 1/4 gives 3/596. Skipping the update gives 1/150 = 0.0067. |
| P4 | 1/4 | F1 are Dd but sinistral (mother dd). F2 are 1 DD : 2 Dd : 1 dd, and all are dextral (mother Dd). F3 coiling follows the F2 mother's genotype, so the 1/4 of F2 that are dd have sinistral F3. Common errors are 0 or 1/16. |
| P5 | 0 | Drosophila males do not cross over, so the A b / a B male makes only A b and a B gametes and never a b. No progeny can be a b / a b. The 20 map units only distract. |

Checks: P3 by exact fractions. P1, P2, P4 and P5 by pedigree and gamete reasoning, as shown in the Trap column.
