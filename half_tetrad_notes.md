# Half-tetrad, two linked loci: corrected question bank

Checked 2026-10-10 by an exact 6-state four-strand Markov chain (`verify/full_tetrad_exact.py`) and by direct Monte Carlo simulation of the tetrad, 200,000 meioses per question (`verify/old_3state_vs_sim.py`). The two methods agree.

## What was wrong

The old "core method" tracked only the individual's two chromatids, using states D, S0 and S1. It is exact only when the two chromatids are **sisters**: terminal fusion, SDR, and SDS in ordered asci.

It is **wrong for non-sister pairs**: central fusion, FDR and attached-X. A crossover is between two non-sister chromatids, chosen by centromere, and all 4 pairs are equally likely. A crossover is not "one strand carrying each homolog's material". When the two chromatids are non-sisters, whether a crossover changes their state depends on the material carried by the other two strands, which this individual does not receive. So the three-state chain is not Markov. Single-locus answers still come out right (Q9 is correct), but two-locus joint answers do not.

Example: an attached-X daughter is homozygous y f at forked. Her strands Y1 and W1 both carry y f material, so the other strands Y2 and W2 both carry + material. A Y1-W1 crossover swaps y f with y f, and a Y2-W2 crossover swaps + with +. Neither changes anything, so this state is lost at rate m/2, not at rate m.

## Corrected table

| # | Set-up | Pair type | Old "correct" | Verified correct | Model A gave | A still wrong? |
|---|---|---|---|---|---|---|
| 1 | Central fusion, AB/ab daughters; A 10 cM, B +30 cM | non-sister | 0.6171 | **0.6327** | 0.0687 | yes |
| 2 | Central fusion, homozygous at both; 20 / +25 | non-sister | 0.0975 | **0.1205** | 0.0806 | yes |
| 3 | Terminal fusion, hom A het B; 15 / +20 | sister | 0.2281 | 0.2281 | 0.2132 | yes |
| 4 | Central fusion, Ab/aB daughters; 30 / +10 | non-sister | 0.0381 | **0.0376** | 0.0351 | yes |
| 5 | Terminal fusion, homozygous at both; 50 / +50 | sister | 0.2324 | 0.2324 | 0.4678 | yes |
| 6 | Central fusion, homozygous at both; 50 / +50 | non-sister | 0.1248 | **0.1745** | 0.1580 | yes |
| 7 | SDR 2n eggs, homozygous at both; 30 / +20 | sister | 0.4226 | 0.4226 | untested | - |
| 8 | Attached-X, y f daughters; f 10, y +56 | non-sister | 0.0169 | **0.0264** | timed out | - |
| 9 | Attached-X, yellow only; y 66 cM | non-sister (single locus) | 0.1437 | 0.1437 | timed out | - |
| 10 | FDR 2n pollen, het at both; 20 / +20 | non-sister | 0.7218 | **0.7421** | untested | - |
| 11 | SDR 2n eggs, het at both; 25 / +15 | sister | 0.3093 | 0.3093 | untested | - |
| 12 | Neurospora SDS at both; 10 / +20 | sister | 0.1468 | 0.1468 | 0.1501 | yes |

All six questions Model A actually answered are still failures, so the weakness finding stands. But Q1, Q2, Q4 and Q6 must be re-graded against the corrected values. Q8 and Q10 need new answer keys and solutions before they are used.

## Correct method

Mean crossovers per tetrad: m = 2x for x Morgans (map distance, additive, Poisson). Each crossover picks one of the 4 non-sister pairs, chosen by centromere, and swaps the distal material.

**Sister pair** (terminal fusion, SDR, ascus SDS). The old 3-state chain is exact:
- P(D) = 2/3 + (P0 - 2/3)e^(-3m/2), with start S (P0 = 0).
- From S0: P(stay S0) = (P(S) + u)/2, with P(S) = 1/3 + (2/3)e^(-3m/2) and u = e^(-m).

**Non-sister pair** (central fusion, FDR, attached-X). Track all four strands. Y1 and Y2 share homolog-1's centromere, W1 and W2 share homolog-2's, and the individual receives Y1 and W1. Write a state as the material (1 or 2) on (Y1, Y2, W1, W2). There are 6 states:

- P = (1,1,2,2), parental: individual het, coupling. The start state.
- R = (2,2,1,1): individual het, swapped.
- M1 = (1,2,1,2): individual homozygous for homolog-1 material.
- M2 = (2,1,2,1): individual homozygous for homolog-2 material.
- N1 = (1,2,2,1): individual het, coupling (hidden partner of P).
- N2 = (2,1,1,2): individual het, swapped (hidden partner of R).

Transition probabilities over a region with mean m (let E1 = e^(-m/2), E2 = e^(-m), E3 = e^(-3m/2)):
- P to P: 1/6 + E2/2 + E3/3. P to R: 1/6 - E2/2 + E3/3. P to each of M1, M2, N1, N2: (1 - E3)/6.
- M1 to M1: 1/6 + 3E1/4 + E3/12. M1 to each of M2, N1, N2: 1/6 - E1/4 + E3/12. M1 to P or R: (1 - E3)/6.
- The rows for R, M2, N1 and N2 follow by symmetry (`verify/transition_matrix_closed_form.py`).

Closed forms for the non-sister two-locus questions, with a = m1 and b = m2:
- Hom at both: (1/18)(1 - e^(-3a/2))(2 + 3e^(-b/2) + e^(-3b/2)). This gives Q2 = 0.1205 and Q6 = 0.1745.
- One specific homozygote at both (Q8): (1/72)(1 - e^(-3a/2))(2 + 9e^(-b/2) + e^(-3b/2)) = 0.0264.
- Het at both (Q10): 4/9 + e^(-b/2)/6 + e^(-3b/2)/18 + 2e^(-3a/2)/9 - e^(-3a/2)e^(-b/2)/6 + 5e^(-3a/2)e^(-3b/2)/18 = 0.7421.

## Corrected Q8 solution (plain text, ready to type)

Step 1. An attached-X daughter receives one compound X chromatid: one strand of the y f arm and one strand of the wild-type arm, joined at one centromere. Call the y f arm strands Y1 and Y2, and the wild-type arm strands W1 and W2. The daughter receives Y1 and W1. Crossovers occur between a Y strand and a W strand, all 4 pairs equally likely, and each one swaps the material distal to it.

Step 2. Both of the daughter's strands must be followed, and so must the two strands she does not receive. Whether a crossover changes her genotype depends on what those other strands carry.

Step 3. A region of x Morgans has a mean of 2x crossovers. Centromere to forked is 0.1 M, so m1 = 0.2. She is f/f only if Y1 and W1 both carry y f material at forked, so Y2 and W2 both carry + material. Starting from the parental arrangement, the chance of this arrangement is (1/6)(1 - e^(-3m1/2)) = (1/6)(1 - e^(-0.3)) = 0.043197.

Step 4. From that arrangement, a Y1-W1 crossover swaps y f material with y f material, and a Y2-W2 crossover swaps + with +. Neither changes anything. Only Y1-W2 and Y2-W1 crossovers move the state. Over a region with mean m, the chance of being back in the same arrangement is 1/6 + (3/4)e^(-m/2) + (1/12)e^(-3m/2).

Step 5. Forked to yellow is 0.56 M, so m2 = 1.12. This gives 1/6 + 0.75 x e^(-0.56) + e^(-1.68)/12 = 0.166667 + 0.428407 + 0.015531 = 0.610605.

Step 6. A daughter is yellow and forked only if she is homozygous y f at both loci: 0.043197 x 0.610605 = 0.026376, about 0.0264.

Step 7. Following only the daughter's two strands gives a wrong answer of 0.0169. That method assumes every crossover changes a homozygous state, which is true only when the two strands are sisters.
