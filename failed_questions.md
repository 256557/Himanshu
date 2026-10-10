# Questions to (re-)ask Model A

All answers re-verified on 2026-10-10 with the correct crossover rule: each crossover joins one strand carrying homolog-1 material and one carrying homolog-2 material at that point (`verify/material_model.py`, `verify/recheck_all.py`). An earlier version of this file gave wrong "corrected" answers for R1, R2, R4, R6, Q14 and Q15; those are fixed below.

## Re-ask list (questions Model A failed)

R1 (Q1). A parthenogenetic insect reproduces by central fusion. She is A B / a b. Gene A is at a map distance of 10 cM from the centromere, and gene B is at a map distance of 30 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). What fraction of her daughters are A B / a b? Give four decimal places. [0.6171]

R2 (Q2). A parthenogenetic lizard reproduces by central fusion. Genes A and B lie on the same chromosome arm. Gene A is at a map distance of 20 cM from the centromere, and gene B is at a map distance of 25 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). For a female heterozygous at both loci, what fraction of her daughters are homozygous at both loci? Give four decimal places. [0.0975]

R3 (Q3). A parthenogenetic moth reproduces by terminal fusion: the egg fuses with its sister second polar body. Genes A and B lie on the same chromosome arm. Gene A is at a map distance of 15 cM from the centromere, and gene B is at a map distance of 20 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). For a female heterozygous at both loci, what fraction of her daughters are homozygous at A but heterozygous at B? Give four decimal places. [0.2281]

R4 (Q4). An ant queen produces daughters by central fusion. She is A B / a b. Gene A is at a map distance of 30 cM from the centromere, and gene B is at a map distance of 10 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). What fraction of her daughters are A b / a B? Give four decimal places. [0.0381]

R5 (Q5). A stick insect reproduces by terminal fusion. Genes A and B lie on the same chromosome arm. Gene A is at a map distance of 50 cM from the centromere, and gene B is at a map distance of 50 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). For a female heterozygous at both loci, what fraction of her daughters are homozygous at both loci? Give four decimal places. [0.2324]

R6 (Q6). Cape honeybee workers produce female offspring by central fusion. Genes A and B lie on the same chromosome arm. Gene A is at a map distance of 50 cM from the centromere, and gene B is at a map distance of 50 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). For a worker heterozygous at both loci, what fraction of her female offspring are homozygous at both loci? Give four decimal places. [0.1248]

R7 (Q12). In Neurospora crassa, genes A and B lie on the same chromosome arm. Gene A is at a map distance of 10 cM from the centromere, and gene B is at a map distance of 20 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). In a cross A B x a b, what fraction of ordered asci show second-division segregation for both genes? Give four decimal places. [0.1468]

| # | Model A gave | Correct |
|---|---|---|
| R1 | 0.0687 | 0.6171 |
| R2 | 0.0806 | 0.0975 |
| R3 | 0.2132 | 0.2281 |
| R4 | 0.0351 | 0.0381 |
| R5 | 0.4678 | 0.2324 |
| R6 | 0.1580 | 0.1248 |
| R7 | 0.1501 | 0.1468 |

## Q13 (terminal fusion, repulsion) [0.0097]

In a parthenogenetic snail, genes A and B lie on the same chromosome arm. Gene A is at a map distance of 20 cM from the centromere, and gene B is at a map distance of 30 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). A female of genotype A b / a B reproduces by terminal fusion, in which the egg fuses with its sister second polar body. What fraction of her daughters are A A B B? Give four decimal places.

Solution: The egg and second polar body are sisters, so at the centromere they carry the same homolog (A b or a B, 1/2 each). States: S0 (both A b material), S1 (both a B material), D (different). From S a crossover always gives D; from D it gives S0 or S1 with 1/4 each. With Poisson mean m from S: P(S) = 1/3 + (2/3)e^(-3m/2) and u = e^(-m). m1 = 0.4: P(S0 at A) = (1/2)(1/3 + (2/3)e^(-0.6)) = 0.349604. m2 = 0.6, from S0: P(S1 at B) = (1/3 + (2/3)e^(-0.9) - e^(-0.6))/2 = 0.027784. Answer 0.349604 x 0.027784 = 0.009713, about 0.0097.

## Q14 (FDR pollen, conditional) [0.6482]

A diploid alfalfa clone forms unreduced (2n) pollen by first-division restitution. Genes A and B lie on the same chromosome arm. Gene A is at a map distance of 15 cM from the centromere, and gene B is at a map distance of 25 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). The clone is heterozygous at both loci. Among its 2n pollen grains that are homozygous at A, what fraction are also homozygous at B? Give four decimal places.

Solution:
Step 1. FDR pollen gets one chromatid from each homolog at the centromere, c1 and c2.
Step 2. At any point c1 and c2 carry the same homolog's material (S, homozygous) or different material (D).
Step 3. Each crossover joins one strand carrying each homolog's material at that point, all 4 pairs equally likely. From S, both of the pollen's strands carry the same material, so the crossover always involves exactly one of them, and the state becomes D. From D, it involves exactly one of them with chance 1/2, giving S.
Step 4. With Poisson mean m, starting from S: P(S) = 1/3 + (2/3)e^(-3m/2).
Step 5. Homozygous at A means state S at A, so the centromere distance does not matter. A to B is 0.25 M, so m = 0.5.
Step 6. P = 1/3 + (2/3)e^(-0.75) = 0.333333 + 0.314911 = 0.648244, about 0.6482.

Model A gave 0.8033: WRONG. It treated homozygosity as a bit that every crossover flips with chance 1/2. From S, every crossover changes the state, not half of them.

## Q15 (exactly two chiasmata, central fusion) [0.1125]

A parthenogenetic weevil reproduces by central fusion. Genes A and B lie on one chromosome arm, A at 30% and B at 70% of the arm's length from the centromere. In every meiosis this arm forms exactly two chiasmata, each at an independent, uniformly random position along the arm, and each involving a random pair of non-sister chromatids. For a female heterozygous at both loci, what fraction of her daughters are homozygous at both loci? Give four decimal places.

Solution:
Step 1. Central fusion gives the daughter one chromatid from each homolog at the centromere (state D).
Step 2. One chiasma: from D, S with chance 1/2 (it involves exactly one of her two chromatids); from S, always D.
Step 3. Each chiasma lies before A with probability 0.3, between A and B with 0.4, and beyond B with 0.3. At least one must lie before A.
Step 4. Both before A (0.09): S after two steps needs D, then D, then S: (1/2)(1/2) = 1/4. Contribution 0.0225.
Step 5. One before A, one beyond B (0.18): P(S at A) = 1/2, unchanged at B. Contribution 0.09.
Step 6. One before A, one between A and B (0.24): S at A, then the second chiasma always gives D at B. Contribution 0.
Step 7. Total = 0.0225 + 0.09 = 0.1125.
Check: simulation 0.1126.

## Q16 (one chiasma, mixed reproduction, unnamed central fusion) [0.2050]

A female insect is A B / a b, with A at 30% and B at 70% of one chromosome arm's length from the centromere. This arm always forms exactly one chiasma, at a uniformly random position, between a random pair of non-sister chromatids. 60% of her eggs develop unfertilized: the egg nucleus fuses with a nucleus from the division of the first polar body. The other 40% are fertilized by an a b / a b male. What fraction of all her offspring are a a b b? Give four decimal places.

Solution: Unfertilized: the chiasma must lie before A (0.3) and involve exactly one of the two fused chromatids (1/2), and they must carry a b material (1/2): 0.075. Fertilized: P(egg = a b) = (1 - 0.4 x 1/2)/2 = 0.4. Total = 0.6 x 0.075 + 0.4 x 0.4 = 0.2050.

Model A gave 0.2050: CORRECT (it enumerated the four chromatids for each chiasma position; one chiasma is easy to enumerate).
