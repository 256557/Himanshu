# Questions Model A failed (ready to re-ask)

Answers use the verified full-tetrad values (see half_tetrad_notes.md). Q1, Q2, Q4 and Q6 use the corrected answers, not the old bank values.

R1 (Q1). A parthenogenetic insect reproduces by central fusion: the egg nucleus fuses with the first polar body's product from the other homolog. She is A B / a b. Gene A is at a map distance of 10 cM from the centromere, and gene B is at a map distance of 30 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). What fraction of her daughters are A B / a b? Give four decimal places. [0.6327]

R2 (Q2). A parthenogenetic lizard reproduces by central fusion. Genes A and B lie on the same chromosome arm. Gene A is at a map distance of 20 cM from the centromere, and gene B is at a map distance of 25 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). For a female heterozygous at both loci, what fraction of her daughters are homozygous at both loci? Give four decimal places. [0.1205]

R3 (Q3). A parthenogenetic moth reproduces by terminal fusion: the egg fuses with its sister second polar body. Genes A and B lie on the same chromosome arm. Gene A is at a map distance of 15 cM from the centromere, and gene B is at a map distance of 20 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). For a female heterozygous at both loci, what fraction of her daughters are homozygous at A but heterozygous at B? Give four decimal places. [0.2281]

R4 (Q4). An ant queen produces daughters by central fusion. She is A B / a b. Gene A is at a map distance of 30 cM from the centromere, and gene B is at a map distance of 10 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). What fraction of her daughters are A b / a B? Give four decimal places. [0.0376]

R5 (Q5). A stick insect reproduces by terminal fusion. Genes A and B lie on the same chromosome arm. Gene A is at a map distance of 50 cM from the centromere, and gene B is at a map distance of 50 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). For a female heterozygous at both loci, what fraction of her daughters are homozygous at both loci? Give four decimal places. [0.2324]

R6 (Q6). Cape honeybee workers produce female offspring by central fusion. Genes A and B lie on the same chromosome arm. Gene A is at a map distance of 50 cM from the centromere, and gene B is at a map distance of 50 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). For a worker heterozygous at both loci, what fraction of her female offspring are homozygous at both loci? Give four decimal places. [0.1745]

R7 (Q12). In Neurospora crassa, genes A and B lie on the same chromosome arm. Gene A is at a map distance of 10 cM from the centromere, and gene B is at a map distance of 20 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). In a cross A B x a b, what fraction of ordered asci show second-division segregation for both genes? Give four decimal places. [0.1468]

## What Model A gave before

| # | Model A | Correct |
|---|---|---|
| R1 | 0.0687 | 0.6327 |
| R2 | 0.0806 | 0.1205 |
| R3 | 0.2132 | 0.2281 |
| R4 | 0.0351 | 0.0376 |
| R5 | 0.4678 | 0.2324 |
| R6 | 0.1580 | 0.1745 |
| R7 | 0.1501 | 0.1468 |

## New question Q14 (verified: closed form 0.801461, simulation 0.8011 +- 0.0023; script `verify/q14.py`)

Question (type as written):
A diploid alfalfa clone forms unreduced (2n) pollen by first-division restitution. Genes A and B lie on the same chromosome arm. Gene A is at a map distance of 15 cM from the centromere, and gene B is at a map distance of 25 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). The clone is heterozygous at both loci. Among its 2n pollen grains that are homozygous at A, what fraction are also homozygous at B? Give four decimal places. [0.8015]

Solution (plain text):
Step 1. In first-division restitution the 2n pollen keeps one chromatid from each homolog at the centromere. Call them c1 (homolog 1) and c2 (homolog 2), and call their sisters c1' and c2'. Crossovers occur between non-sister chromatids (one of c1, c1' with one of c2, c2'), all 4 pairs equally likely, and each swaps the material distal to it.
Step 2. Classify the four strands at a point into three classes. M: c1 and c2 carry the same homolog's material (the pollen is homozygous). Then c1' and c2' both carry the other homolog's material. PR: c1 and c2 differ, and each matches its own sister (c1 = c1', c2 = c2'; parental or fully reversed). N: c1 and c2 differ, and each differs from its own sister.
Step 3. One crossover moves between the classes as follows. From M: a c1-c2 or c1'-c2' crossover swaps identical material and changes nothing; the other two pairs give PR. So M goes to M 1/2, PR 1/2. From PR: two pairs give M and two give N, so 1/2 each. From N: two pairs leave N unchanged and two give PR, so N 1/2, PR 1/2.
Step 4. This one-crossover matrix has eigenvalues 1, 1/2 and -1/2. With a Poisson number of crossovers of mean m, starting in M: P(M) = 1/3 + (1/2)e^(-m/2) + (1/6)e^(-3m/2). A region of x Morgans has mean m = 2x.
Step 5. A to B is 0.25 M, so m = 0.5. Given that the pollen is homozygous at A, the strands are in class M at A, so P(homozygous at B) = 1/3 + (1/2)e^(-0.25) + (1/6)e^(-0.75) = 0.333333 + 0.389400 + 0.078728 = 0.801461, about 0.8015.
Step 6. The centromere distance does not matter for this conditional question, because being homozygous at A already fixes class M at A. Following only the pollen's two chromatids, as if every crossover changed a homozygous state, gives 1/3 + (2/3)e^(-0.75) = 0.6482, which is wrong. Half of the crossovers from class M swap identical material and change nothing.

### Model A on Q14 (2026-10-10): WRONG, gave 0.8033

Check with 40 million simulated meioses (`verify/q14_big.py`): 0.80169 +- 0.00036. Correct 0.8015 is inside this range; 0.8033 is about 9 standard errors away.

Its error: it treated homozygosity as a parity bit that each crossover flips with chance 1/2, independently of the current state, and so got P = (1 + e^(-0.5))/2 = 1 - r(Haldane). That is wrong because the flip chance depends on the hidden configuration of the two strands the pollen does not receive. From class N (pollen heterozygous, each chromatid differing from its sister), no single crossover can make the pollen homozygous. It also claimed the two intervals are independent without justification.

## New question Q15: explicit chiasma rule, no Poisson (verified: exact 69/400 = 0.1725, simulation of 20M meioses 0.17258 +- 0.00017; script `verify/q15.py`)

Question (type as written):
A parthenogenetic weevil reproduces by central fusion. Genes A and B lie on one chromosome arm, A at 30% and B at 70% of the arm's length from the centromere. In every meiosis this arm forms exactly two chiasmata, each at an independent, uniformly random position along the arm, and each involving a random pair of non-sister chromatids. For a female heterozygous at both loci, what fraction of her daughters are homozygous at both loci? Give four decimal places. [0.1725]

Solution (plain text):
Step 1. Central fusion gives each daughter two non-sister chromatids, c1 and c2, one from each homolog at the centromere. Their sisters are c1' and c2'. Each chiasma swaps the material beyond it between one homolog-1 chromatid and one homolog-2 chromatid, all 4 pairs equally likely.
Step 2. Track all four chromatids in three classes. M: c1 = c2 (the daughter is homozygous). PR: c1 = c1' and c2 = c2'. N: c1 differs from c1' and c2 differs from c2'. At the centromere the class is PR.
Step 3. One chiasma moves: PR to M 1/2, N 1/2. M to M 1/2, PR 1/2. N to N 1/2, PR 1/2.
Step 4. The daughter must be homozygous at A, so at least one chiasma must lie before A. Each chiasma falls before A with probability 0.3, between A and B with 0.4, and beyond B with 0.3.
Step 5. Case 1: both chiasmata before A (0.3 x 0.3 = 0.09). After two steps from PR, P(M) = (1/2)(1/2) = 1/4. Nothing changes between A and B. Contribution: 0.09 x 1/4 = 0.0225.
Step 6. Case 2: one chiasma before A and one beyond B (2 x 0.3 x 0.3 = 0.18). P(M at A) = 1/2, and B keeps that class. Contribution: 0.18 x 1/2 = 0.09.
Step 7. Case 3: one chiasma before A and one between A and B (2 x 0.3 x 0.4 = 0.24). P(M at A) = 1/2, then the second chiasma keeps M with probability 1/2. Contribution: 0.24 x 1/4 = 0.06.
Step 8. Total = 0.0225 + 0.09 + 0.06 = 0.1725.
Step 9. Converting to map distances and using a Poisson model (A at 30 cM, B 40 cM beyond) gives 0.1422, which is wrong. The number of chiasmata is fixed at two, not Poisson.
