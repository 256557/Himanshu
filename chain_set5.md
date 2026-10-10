# Chain set 5: autotetraploid potato with double reduction

Paste the whole block, setup included:

A potato is autotetraploid (four copies of each chromosome). Gene A is far enough from the centromere that 10% of gametes carry two copies of A descended from the same chromosome (double reduction); every other gamete carries one copy from each of two different chromosomes, chosen at random. Allele A is fully dominant over a. Give answers as exact fractions.
Q1. What fraction of gametes from a duplex plant (AAaa) are aa?
Q2. A duplex plant is self-fertilised. What fraction of the offspring are aaaa?
Q3. In the same selfing, what fraction of the offspring are simplex (Aaaa)?
Q4. A simplex plant (Aaaa) is crossed with a nulliplex plant (aaaa). What fraction of the offspring are duplex (AAaa)?
Q5. A triplex plant (AAAa) is self-fertilised. What fraction of the offspring are aaaa?
Q6. Among the offspring of the selfed duplex plant that show the dominant phenotype, what fraction are quadruplex (AAAA)?

## Answer key (exact enumeration, `verify/chain5.py`)
| # | Answer | Working |
|---|---|---|
| Q1 | 1/5 | Duplex gametes: AA = (1 + 2a)/6, Aa = 4(1 - a)/6, aa = (1 + 2a)/6 with a = 0.1, giving 1/5 : 3/5 : 1/5 |
| Q2 | 1/25 | (1/5)^2 |
| Q3 | 6/25 | 2 x (3/5)(1/5) |
| Q4 | 1/40 | Simplex gametes: AA = a/4 = 1/40, Aa = (1 - a)/2, aa = (2 + a)/4. Only AA gametes give AAaa with an aa gamete. |
| Q5 | 1/1600 | Triplex gametes: aa = a/4 = 1/40, so (1/40)^2 |
| Q6 | 1/24 | AAAA = (1/5)^2 = 1/25; dominant = 1 - 1/25 = 24/25; ratio 1/24 |

## Likely wrong answers (ignoring double reduction, a = 0)
Q1 1/6, Q2 1/36, Q3 2/9, Q4 0 (no duplex offspring possible), Q5 0 (no aaaa possible), Q6 1/35.
Other errors: using diploid ratios (Q2 = 1/4), or treating the 10% as a random chromatid choice.

## Model A results (2026-10-10)
All 6 correct: 1/5, 1/25, 6/25, 1/40, 1/1600, 1/24. Its simplex gametes (1/40 : 18/40 : 21/40) match (2 + a)/4 = 21/40. It handles double reduction when the rate is given directly.
