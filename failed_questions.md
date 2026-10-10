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

## Q17 (yeast unordered tetrads, three genes, conditional) [0.0989]
Verified: exact 0.098905; simulation of 4M tetrads 0.0991 +- 0.0005 (`verify/q17.py`).

In yeast, genes A, B and C lie in that order on one chromosome arm. A and B are at a map distance of 20 cM, and B and C at a map distance of 30 cM (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). In a cross A B C x a b c, among unordered tetrads that are tetratype for A and B, what fraction are nonparental ditype for A and C? Give four decimal places.

Solution:
Step 1. At any point, two of the four spores carry parent-1 material and two carry parent-2 material. Each crossover swaps the material beyond it between one parent-1 strand and one parent-2 strand (4 pairs, equally likely).
Step 2. Compare the strand arrangement at two loci. PD: same arrangement. NPD: every strand switched. T: exactly two strands switched, which is the result of one effective swap.
Step 3. Tetratype for A and B means the arrangement at B is one swap away from the arrangement at A. NPD for A and C means the arrangement at C is the full reverse of A. From the B arrangement, the full reverse of A is also exactly one swap away, and it is one specific arrangement out of the 4 reachable by a single swap.
Step 4. Over the B to C interval, the chance of ending one swap away from the start (tetratype for B and C) is (2/3)(1 - e^(-3m/2)). By symmetry it is split equally among the 4 one-swap arrangements, so a specific one has probability (1/6)(1 - e^(-3m/2)).
Step 5. B to C is 0.30 M, and a tetrad has a mean of 2x crossovers, so m = 0.6. P = (1/6)(1 - e^(-0.9)) = (1/6)(0.593430) = 0.098905, about 0.0989.
Step 6. Using the plain NPD formula for B to C (0.0278), or treating the intervals as independent, is wrong. Given that A and B are tetratype, a single effective swap between B and C can already make A and C nonparental ditype.

Model A on Q17 (2026-10-10): CORRECT, 0.0989. It used the same reasoning (a specific one-swap arrangement = P_T(m)/4) and cross-checked P(NPD for A-C) = 0.0571 against the single-interval formula for m = 1.0. Minor wording issues: it calls the tetrad formulas "Haldane", and its permutation notation is loose. Neither affects the answer.

## Q18 (central fusion, repulsion parent, conditional phase) [0.1055]
Verified: closed form 0.105510; simulation of 4M meioses 0.1057 +- 0.0004 (`verify/q18.py`).

A parthenogenetic mite reproduces by central fusion. Genes A and B lie on the same chromosome arm. Gene A is at a map distance of 25 cM from the centromere, and gene B is at a map distance of 20 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). The mother is A b / a B. Among her daughters that are heterozygous at both loci, what fraction are A B / a b? Give four decimal places.

Solution:
Step 1. Central fusion gives the daughter two chromatids, c1 and c2, from different homologs at the centromere. At any point they carry different homologs' material (D) or the same (S).
Step 2. Each crossover joins one strand carrying each homolog's material at that point, all 4 pairs equally likely. From D: exactly one of c1 and c2 is involved with chance 1/2 (giving S); both are involved with chance 1/4 (they swap homologs, staying D); neither with chance 1/4 (no change).
Step 3. With Poisson mean m, starting from D with a known phase: P(D) = 2/3 + (1/3)e^(-3m/2), and P(same phase) - P(swapped phase) = e^(-m).
Step 4. The daughter is heterozygous at A, so she is in D at A. The centromere distance does not matter for this conditional question.
Step 5. She is A B / a b exactly when the phase at B is swapped relative to A (the chromatid with A from the A b homolog carries B from the a B homolog). A to B is 0.2 M, so m = 0.4. P(D at B) = 2/3 + (1/3)e^(-0.6) = 0.849604. P(swapped) = (0.849604 - e^(-0.4))/2 = (0.849604 - 0.670320)/2 = 0.089642.
Step 6. Fraction = 0.089642 / 0.849604 = 0.105510, about 0.1055.
Step 7. Using a recombination fraction (Haldane r = 0.1648, or 0.20) is wrong. The two chromatids come from one meiosis, so a crossover can make the daughter homozygous instead of swapping her phase.

Model A on Q18 (2026-10-10): WRONG, gave 0.0498 (correct 0.1055).
Errors: (1) It used the map length (0.20) as the mean number of crossovers in the A-B interval instead of 2 x 0.20 = 0.40. (2) It modelled each fixed chromatid pair as having an independent Poisson number of crossovers and set alleles by the parity of crossovers touching each chromatid. That ignores that a crossover between two strands carrying the same homolog's material changes nothing. Even with the correct mean of 0.4, its formula gives 0.0987, still wrong.

## Q19 (SDR 2n eggs, reverse conditional) [0.5341]
Verified: closed form 0.534106; simulation of 4M meioses 0.5337 +- 0.0007 (`verify/q19.py`).

A diploid potato clone forms unreduced (2n) eggs by second-division restitution. Genes A and B lie on the same chromosome arm. Gene A is at a map distance of 20 cM from the centromere, and gene B is at a map distance of 30 cM beyond A (map distances are additive, with Poisson crossovers and no chiasma or chromatid interference). The clone is heterozygous at both loci. Among its 2n eggs that are heterozygous at B, what fraction are homozygous at A? Give four decimal places.

Solution:
Step 1. In second-division restitution the 2n egg keeps two sister chromatids, which carry the same homolog's material at the centromere (state S). At any point the state is S (homozygous) or D (heterozygous).
Step 2. Each crossover joins one strand carrying each homolog's material at that point, all 4 pairs equally likely. From S a crossover always gives D. From D it gives S with chance 1/2.
Step 3. With Poisson mean m: from S, P(D) = (2/3)(1 - e^(-3m/2)); from D, P(D) = 2/3 + (1/3)e^(-3m/2). A region of x Morgans has m = 2x.
Step 4. Centromere to A: m1 = 0.4. P(S at A) = 1/3 + (2/3)e^(-0.6) = 0.699208, and P(D at A) = 0.300792.
Step 5. A to B: m2 = 0.6, e^(-0.9) = 0.406570. P(D at B | S at A) = (2/3)(0.593430) = 0.395620. P(D at B | D at A) = 2/3 + 0.406570/3 = 0.802190.
Step 6. Joint probabilities: S at A and D at B = 0.699208 x 0.395620 = 0.276621. D at A and D at B = 0.300792 x 0.802190 = 0.241292. Total heterozygous at B = 0.517913.
Step 7. Fraction = 0.276621 / 0.517913 = 0.534106, about 0.5341.
Step 8. Answering 0.6992 (the plain chance of homozygosity at A) ignores the condition. Being heterozygous at B makes homozygosity at A less likely, because the two loci are linked through the same pair of chromatids.

Model A on Q19 (2026-10-10, reworded short version with "map distance", "additive" and "no chiasma or chromatid interference"): WRONG, gave 0.5857 (correct 0.5341).
It used the right crossover means (0.4, 0.6), but claimed that each crossover "flips exactly one of the two allele states" in the sister pair, so the egg is heterozygous iff the number of crossovers is odd. That holds only from a homozygous state. Once the sisters differ, a crossover involves exactly one of them only half the time (both 1/4, neither 1/4), so heterozygosity is not a parity of the crossover count. Its "intuitive check" (fraction > 0.5) does not test the model.

## Q20 (attached-X, reverse conditional) [0.3253]
Verified: closed form 0.325337; simulation of 8M meioses 0.3249 +- 0.0010 (`verify/q20.py`).

A Drosophila female carries attached-X chromosomes. One arm carries recessive alleles p and d, and the other arm carries their wild-type alleles. Gene p is at a map distance of 15 cM from the centromere, and gene d is 25 cM beyond p (map distances are additive). Crossovers follow a Poisson distribution with no chiasma or chromatid interference. Among her attached-X daughters that are homozygous d/d, what fraction are also homozygous p/p? Give four decimal places.

Solution:
Step 1. An attached-X daughter receives one strand from each arm, so at the centromere her two strands carry different arms' material (state D). States: D (heterozygous), S0 (both carry p d arm material), S1 (both wild-type arm material).
Step 2. Each crossover joins one strand carrying each arm's material at that point. From D: S0 or S1 with 1/4 each, otherwise D. From S0 or S1: always D.
Step 3. With Poisson mean m (m = 2x for x Morgans): from D, P(S0) = (1/6)(1 - e^(-3m/2)). From S0: P(S) = 1/3 + (2/3)e^(-3m/2) and P(S0) - P(S1) = e^(-m).
Step 4. P(d/d) over the whole region, centromere to d: m = 0.8. P = (1/6)(1 - e^(-1.2)) = (1/6)(0.698806) = 0.116468.
Step 5. P(p/p): m1 = 0.3. P(S0 at p) = (1/6)(1 - e^(-0.45)) = 0.060395.
Step 6. From S0 at p, over m2 = 0.5: P(S) = 1/3 + (2/3)e^(-0.75) = 0.648244, and u = e^(-0.5) = 0.606531. P(S0 at d) = (0.648244 + 0.606531)/2 = 0.627388.
Step 7. Joint P(p/p and d/d) = 0.060395 x 0.627388 = 0.037891.
Step 8. Fraction = 0.037891 / 0.116468 = 0.325337, about 0.3253.
Step 9. Treating the loci as independent (answering P(p/p) = 0.0604), or assuming d/d forces p/p, is wrong. Most d/d daughters became homozygous through a crossover between p and d, so they are still heterozygous at p.

## Q21 (terminal fusion, reverse conditional) [0.0740]
Verified: closed form 0.073971; simulation of 6M meioses 0.0739 +- 0.0003 (`verify/q21.py`). The parity ("odd number of crossovers") method gives 0.1066.

A parthenogenetic moth reproduces by terminal fusion: the egg fuses with its sister second polar body. Genes A and B are on the same chromosome arm. A is at a map distance of 10 cM from the centromere, and B is 35 cM beyond A (map distances are additive). Crossovers follow a Poisson distribution with no chiasma or chromatid interference. The female is heterozygous at both loci. Among her daughters that are homozygous at B, what fraction are heterozygous at A? Give four decimal places.

Solution:
Step 1. Terminal fusion joins sister products, so at the centromere the daughter's two chromatids carry the same homolog (state S, homozygous). At any point the state is S or D (heterozygous).
Step 2. Each crossover joins one strand carrying each homolog's material at that point. From S it always gives D. From D it gives S with chance 1/2.
Step 3. With Poisson mean m (m = 2x for x Morgans): from S, P(S) = 1/3 + (2/3)e^(-3m/2); from D, P(S) = (1/3)(1 - e^(-3m/2)).
Step 4. Centromere to A: m1 = 0.2. P(S at A) = 1/3 + (2/3)e^(-0.3) = 0.827212, and P(D at A) = 0.172788.
Step 5. A to B: m2 = 0.7, e^(-1.05) = 0.349938. P(S at B | S at A) = 1/3 + (2/3)(0.349938) = 0.566625. P(S at B | D at A) = (1/3)(1 - 0.349938) = 0.216687.
Step 6. Joint: D at A and S at B = 0.172788 x 0.216687 = 0.037441. S at A and S at B = 0.827212 x 0.566625 = 0.468719. Total homozygous at B = 0.506160.
Step 7. Fraction = 0.037441 / 0.506160 = 0.073971, about 0.0740.
Step 8. Treating homozygosity as "an even number of crossovers" gives 0.1066, which is wrong. From D, half of all crossovers leave the daughter heterozygous.

## Q22 (FDR pollen, reverse conditional) [0.6638]
Verified: closed form 0.663847; simulation of 6M meioses 0.6637 +- 0.0008 (`verify/q22.py`). The parity method gives 0.6134.

A diploid alfalfa clone makes 2n pollen by first-division restitution. Genes A and B are on the same chromosome arm. A is at a map distance of 15 cM from the centromere, and B is 25 cM beyond A (map distances are additive). Crossovers follow a Poisson distribution with no chiasma or chromatid interference. The clone is heterozygous at both loci. Among 2n pollen grains that are homozygous at B, what fraction are heterozygous at A? Give four decimal places.

Solution:
Step 1. First-division restitution keeps one chromatid from each homolog at the centromere, so the pollen starts in state D (heterozygous). At any point the state is D or S (homozygous).
Step 2. Each crossover joins one strand carrying each homolog's material at that point. From D it gives S with chance 1/2. From S it always gives D.
Step 3. With Poisson mean m (m = 2x for x Morgans): from D, P(D) = 2/3 + (1/3)e^(-3m/2) and P(S) = (1/3)(1 - e^(-3m/2)); from S, P(S) = 1/3 + (2/3)e^(-3m/2).
Step 4. Centromere to A: m1 = 0.3. P(D at A) = 2/3 + (1/3)e^(-0.45) = 0.879209, and P(S at A) = 0.120791.
Step 5. A to B: m2 = 0.5, e^(-0.75) = 0.472367. P(S at B | D at A) = (1/3)(0.527633) = 0.175878. P(S at B | S at A) = 1/3 + (2/3)(0.472367) = 0.648244.
Step 6. Joint: D at A and S at B = 0.879209 x 0.175878 = 0.154633. S at A and S at B = 0.120791 x 0.648244 = 0.078302. Total homozygous at B = 0.232935.
Step 7. Fraction = 0.154633 / 0.232935 = 0.663847, about 0.6638.
Step 8. Treating homozygosity as "an odd number of crossovers" gives 0.6134, which is wrong. From S, every crossover changes the state; from D, only half do.

## Q22 short version (simplified wording with an explicit crossover rule) [0.1546]
"A plant makes 2n pollen by first-division restitution, so each pollen grain keeps one chromatid from each homolog. Genes A and B are on the same chromosome arm. A is 15 cM (map distance) from the centromere, and B is 25 cM beyond A. Crossovers are Poisson, with no chiasma or chromatid interference, and each crossover joins a chromatid of one homolog with a chromatid of the other. The plant is heterozygous at A and B. What fraction of the pollen is heterozygous at A but homozygous at B? Give four decimal places."
Answer 0.1546 = (2/3 + e^-0.45/3) x (1 - e^-0.75)/3. Simulation of 8M meioses: 0.15456 +- 0.00026.

Model A (2026-10-10): WRONG, gave 0.1712.
It used the right means (0.3, 0.5) but split crossovers into independent Poisson streams per chromatid and set each allele by the parity of crossovers on that chromatid. It got P(het A) = (1 + e^-0.3)/2 = 0.8704 (correct 0.8792) and P(hom B | het A) = (1 - e^-0.5)/2 = 0.1967 (correct 0.1759). Its parity rule ignores that a crossover changes the pair's state with a probability that depends on the current state (from D only 1/2 of crossovers give S; from S all give D). Its 4-class table summing to 1 is not a real check, because any product of complementary pairs sums to 1.
