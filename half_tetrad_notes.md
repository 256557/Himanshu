# Half-tetrad, two linked loci: question bank (verified)

## Correction notice (2026-10-10)
An earlier version of this file claimed that Q1, Q2, Q4, Q6, Q8 and Q10 had wrong answers. **That claim was wrong, and the original answers are correct.** The "correction" paired strands for crossing over by centromere. Physically, sister chromatids are defined locally: beyond a crossover, the two arms on one homolog's axis are still sisters. So every crossover joins one strand carrying homolog-1 material and one carrying homolog-2 material at that point. That is the original D/S0/S1 method. A check: under the correct rule, PD/NPD/T tetrad frequencies do not depend on centromere distance, as standard tetrad theory requires; under the wrong rule they did.

Re-verified with the correct rule (`verify/material_model.py`, `verify/recheck_all.py`, 1M simulated meioses per question): all bank answers match.

## The weakness (Model A)
It fails when an individual carries two chromatids from the same meiosis and two linked loci must be tracked: automixis (central or terminal fusion), unreduced 2n gametes (FDR/SDR), attached-X, and ordered asci.

Typical errors:
1. It treats the two chromatids as crossing over independently.
2. It treats the two intervals as independent, or treats homozygosity as a bit that every crossover flips with chance 1/2 regardless of state.
3. It sometimes uses x instead of 2x as the crossover mean.
4. On single-locus questions it sometimes swaps central and terminal fusion.

## Core method (correct)
- Follow the two chromatids c1 and c2 the individual receives.
  - Central fusion, FDR or attached-X: start in D (different homologs).
  - Terminal fusion or SDR: start in S (same homolog).
- One crossover joins one local homolog-1 strand with one local homolog-2 strand (4 pairs, equally likely).
  - From D: P(goes to S) = 1/2 (S0 or S1, 1/4 each); P(D0 swaps to D1) = 1/4.
  - From S: always goes to D (D0 or D1, 1/2 each).
- Poisson crossovers with mean m = 2x for x Morgans:
  - P(D) = 2/3 + (P0 - 2/3)e^(-3m/2)
  - d = P(D0) - P(D1) = d0 e^(-m)
  - u = P(S0) - P(S1) = u0 e^(-m)
- Chain the intervals: centromere to A, then A to B, starting interval 2 from the state at A.

## Question bank

| # | Set-up | Asked | Correct | Model A gave |
|---|---|---|---|---|
| 1 | Central fusion, AB/ab; A 10 cM, B +30 cM | AB/ab daughters | 0.6171 | 0.0687 |
| 2 | Central fusion; A 20, B +25 | homozygous at both | 0.0975 | 0.0806 |
| 3 | Terminal fusion; A 15, B +20 | hom A, het B | 0.2281 | 0.2132 |
| 4 | Central fusion, AB/ab; A 30, B +10 | Ab/aB daughters | 0.0381 | 0.0351 |
| 5 | Terminal fusion; A 50, B +50 | homozygous at both | 0.2324 | 0.4678 |
| 6 | Central fusion; A 50, B +50 | homozygous at both | 0.1248 | 0.1580 |
| 7 | SDR 2n eggs; A 30, B +20 | homozygous at both | 0.4226 | untested |
| 8 | Attached-X y f; f 10, y +56 | yellow and forked | 0.0169 | timed out |
| 9 | Attached-X; y 66 cM | yellow | 0.1437 | timed out |
| 10 | FDR 2n pollen; A 20, B +20 | het at both | 0.7218 | untested |
| 11 | SDR 2n eggs; A 25, B +15 | het at both | 0.3093 | untested |
| 12 | Neurospora asci; A 10, B +20 | SDS for both | 0.1468 | 0.1501 |
| 13 | Terminal fusion, A b/a B; A 20, B +30 | AA BB | 0.0097 | untested |
| 14 | FDR pollen; A 15, B +25 | hom B given hom A | 0.6482 | 0.8033 |
| 15 | Central fusion, exactly 2 chiasmata; A 30%, B 70% of arm | hom at both | 0.1125 | untested |
| 16 | 1 chiasma, 60% central fusion / 40% fertilized | aa bb | 0.2050 | 0.2050 (correct) |

Exact forms:
- Q1: (2/3 + e^-0.3/3)(1/3 + e^-0.9/6 + e^-0.6/2)
- Q2: (1 - e^-0.6)(1 + 2e^-0.75)/9
- Q3: (1/3 + 2e^-0.45/3)(2/3)(1 - e^-0.6)
- Q4: (2/3 + e^-0.9/3)(1/3 + e^-0.3/6 - e^-0.2/2)
- Q5: (1/3 + 2e^-1.5/3)^2
- Q6: (1/3)(1 - e^-1.5)(1/3 + 2e^-1.5/3)
- Q7: (1/3 + 2e^-0.9/3)(1/3 + 2e^-0.6/3)
- Q8: (1/6)(1 - e^-0.3) x (1/3 + 2e^-1.68/3 + e^-1.12)/2
- Q10: (2/3 + e^-0.6/3)^2
- Q11: (2/3)(1 - e^-0.75) x (2/3 + e^-0.45/3)
- Q14: 1/3 + (2/3)e^-0.75

Full question texts and solutions are in `failed_questions.md`.
