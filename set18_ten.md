# Set 18: ten chromatid-tracking questions

All questions share one rule, stated in each: crossovers are Poisson, with no chiasma or chromatid interference, and each crossover joins a chromatid of one homolog with a chromatid of the other. Map distance x (Morgans) gives a crossover mean m = 2x per interval.

Common results used in the solutions. Let S mean that the two retained chromatids carry the same homolog at a point and D that they carry different homologs. Over an interval with crossover mean m:
- from S: P(D) = (2/3)(1 - e^(-3m/2)), P(S) = 1/3 + (2/3)e^(-3m/2);
- from D: P(D) = 2/3 + (1/3)e^(-3m/2), P(S) = (1/3)(1 - e^(-3m/2));
- from S or D, the excess of the original homolog order over the reversed order is e^(-m).

Sister chromatids (terminal fusion, second-division restitution, first-division segregation in asci) start in S. Non-sister chromatids (central fusion, first-division restitution, attached-X) start in D.

## Q1
A parthenogenetic weevil reproduces by central fusion, so each daughter keeps two non-sister chromatids. A founder is heterozygous at a locus 35 cM (map distance) from the centromere. [Common rule.] What fraction of her great-granddaughters (three generations later) are heterozygous at this locus? Give four decimal places.

Solution: m = 0.70. Per generation, P(D) from D = 2/3 + (1/3)e^(-1.05) = 0.783298. Homozygotes produce only homozygotes, so the answer is 0.783298^3 = 0.4806.

## Q2
A plant AB/ab produces 2n pollen by first-division restitution, so each grain keeps two non-sister chromatids. A is 10 cM (map distance) from the centromere and B is 30 cM beyond A. [Common rule.] What fraction of 2n pollen grains are homozygous at both loci? Give four decimal places.

Solution: m1 = 0.20, m2 = 0.60. P(S at A) from D = (1/3)(1 - e^(-0.3)) = 0.086394. From S, P(S at B) = 1/3 + (2/3)e^(-0.9) = 0.604374. Answer 0.086394 x 0.604374 = 0.0522.

## Q3
A plant AB/ab forms 2n eggs by second-division restitution, so each egg keeps two sister chromatids. A is 15 cM from the centromere and B is 20 cM beyond A. [Common rule.] What fraction of 2n eggs are heterozygous at A but homozygous at B? Give four decimal places.

Solution: m1 = 0.30, m2 = 0.40. P(D at A) from S = (2/3)(1 - e^(-0.45)) = 0.241581. From D, P(S at B) = (1/3)(1 - e^(-0.6)) = 0.150396. Answer 0.0363.

## Q4
A Drosophila female carries an attached-X chromosome heterozygous for yellow (y) and its wild-type allele, with y 50 cM (map distance) from the centromere. Attached-X daughters receive two non-sister chromatids joined at a common centromere. [Common rule.] What fraction of her attached-X daughters are yellow? Give four decimal places.

Solution: m = 1.0. From D, P(S) = (1/3)(1 - e^(-1.5)) = 0.258957, and half of these carry y on both arms. Answer 0.1295.

## Q5
In Neurospora crassa a gene lies 30 cM (map distance) from its centromere. [Common rule.] What fraction of ordered asci show second-division segregation for this gene? Give four decimal places.

Solution: second-division segregation occurs when the two sister chromatids of one centromere differ at the gene, that is, state D starting from S. With m = 0.60, (2/3)(1 - e^(-0.9)) = 0.3956. The value 2 x 0.30 = 0.60 is the answer only when there is at most one crossover.

## Q6
In yeast, genes A and B lie 30 cM (map distance) apart on the same arm. [Common rule.] What fraction of unordered tetrads from AB x ab are non-parental ditypes? Give four decimal places.

Solution: a non-parental ditype requires all four strands to be recombinant. With m = 0.60, NPD = 1/6 - (1/2)e^(-m) + (1/3)e^(-3m/2) = 0.166667 - 0.274406 + 0.135523 = 0.0278.

## Q7
A parthenogenetic insect AB/ab reproduces by central fusion. A is 20 cM from the centromere and B is 20 cM beyond A. [Common rule.] What fraction of daughters are ab/ab? Give four decimal places.

Solution: m = 0.40 per interval. From D, P(S at A) = (1/3)(1 - e^(-0.6)) = 0.150396, and half of these are aa: 0.075198. From S at A, the pair keeps the same homolog at B with probability (P(S) + e^(-m))/2 = (0.699208 + 0.670320)/2 = 0.684764. Answer 0.075198 x 0.684764 = 0.0515.

## Q8
A parthenogenetic insect Ab/aB reproduces by terminal fusion. A is 20 cM from the centromere and B is 20 cM beyond A. [Common rule.] What fraction of daughters are AB/AB? Give five decimal places.

Solution: m = 0.40 per interval. The retained dyad carries either homolog with probability 1/2, so P(both chromatids carry the Ab homolog at A) = P(S at A)/2 = 0.699208/2 = 0.349604. From S at A, the pair must switch to the other homolog at B while staying homozygous: (P(S) - e^(-m))/2 = (0.699208 - 0.670320)/2 = 0.014444. Answer 0.349604 x 0.014444 = 0.00505.

## Q9
A plant AB/ab produces 2n pollen by first-division restitution. A is 15 cM from the centromere and B is 25 cM beyond A. [Common rule.] Among 2n pollen grains heterozygous at A, what fraction are homozygous at B? Give four decimal places.

Solution: the pair is in D at A, so with m2 = 0.50, P(S at B) = (1/3)(1 - e^(-0.75)) = 0.1759. The centromere distance does not enter.

## Q10
A parthenogenetic insect AB/ab reproduces by central fusion. A is 25 cM from the centromere and B is 25 cM beyond A. [Common rule.] What fraction of daughters are heterozygous at both loci? Give four decimal places.

Solution: m = 0.50 per interval. From D, P(D) = 2/3 + (1/3)e^(-0.75) = 0.824122 for each interval. Answer 0.824122^2 = 0.6792.

## Verification
Each value was compared with a simulation of 2 million meioses under the same crossover rule (`verify/set18.py`); all agree within sampling error. For Q8 the script fixes the retained dyad on one homolog, and the stated answer averages over the two dyads.
