# Chain set 1: same plant, five linked questions (send together, in order)

Setup (send first, then the five questions):
A potato clone makes 2n eggs by second-division restitution, so each egg keeps two sister chromatids. Genes A, B and C are on the same chromosome arm in that order. A is 15 cM (map distance) from the centromere, B is 20 cM beyond A, and C is 25 cM beyond B. Crossovers are Poisson, with no chiasma or chromatid interference, and each crossover joins a chromatid of one homolog with a chromatid of the other. The clone is heterozygous for all three genes. Give each answer to four decimal places.

Q1. What fraction of the 2n eggs are homozygous at A?
Q2. What fraction are homozygous at B?
Q3. What fraction are homozygous at both A and B?
Q4. Among eggs homozygous at B, what fraction are homozygous at A?
Q5. What fraction are heterozygous at A, homozygous at B, and heterozygous at C?

## Answer key (verified: exact formulas plus a simulation of 8M meioses, `verify/chain1.py`)
| # | Answer | Formula |
|---|---|---|
| Q1 | 0.7584 | 1/3 + (2/3)e^(-0.45) |
| Q2 | 0.5666 | 1/3 + (2/3)e^(-1.05) |
| Q3 | 0.5303 | Q1 x [1/3 + (2/3)e^(-0.6)] |
| Q4 | 0.9359 | Q3 / Q2 |
| Q5 | 0.0128 | (2/3)(1 - e^(-0.45)) x (1/3)(1 - e^(-0.6)) x (2/3)(1 - e^(-0.75)) |

Simulation: 0.7585, 0.5668, 0.5304, 0.9358, 0.0128.

## Consistency checks (catch the model even when single answers look plausible)
- Q4 must equal Q3 / Q2. If not, the model switched methods between questions.
- Q3 must be at most min(Q1, Q2).
- Q2 uses the whole centromere-to-B distance (35 cM, m = 0.7). Splitting it into two intervals must give the same Q2:
  Q1 x P(S to S over 20 cM) + (1 - Q1) x P(D to S over 20 cM) = 0.7584 x 0.6992 + 0.2416 x 0.1504 = 0.5666.
- Q1 and Q2 are single-locus results. The model usually gets these right, so a wrong Q3, Q4 or Q5 isolates the two-locus weakness.

## Step values for grading
- e^(-0.45) = 0.637628; e^(-0.6) = 0.548812; e^(-0.75) = 0.472367; e^(-1.05) = 0.349938
- P(S at B | S at A) = 0.699208
- Q5 factors: 0.241581 x 0.150396 x 0.351755
