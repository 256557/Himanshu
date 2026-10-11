# Set 17: two linked questions on genetic load

## Questions (paste together)
1. A large, randomly mating population carries a fully recessive deleterious allele at mutation-selection balance. How does the strength of selection against homozygotes affect the genetic load this allele imposes?
2. If the same population switches permanently to self-fertilisation, how does the load from this allele change in the first selfed generation and at the new equilibrium?

## Solution

### Question 1

Step 1. At equilibrium, new mutations enter at rate mu per gamete and selection removes the same number of alleles, almost all of them in aa homozygotes.

Step 2. The equilibrium frequency is q = sqrt(mu/s), so the load, s q^2, equals mu. The selection coefficient cancels.

Step 3. With mu = 10^-5, the load was 1.00 x 10^-5 for both s = 0.1 (q = 0.0100) and s = 0.01 (q = 0.0316) (`verify/set17.py`).

Answer: the load is set by the mutation rate and does not depend on s. Weaker selection allows the allele to become more common by exactly the factor that offsets its smaller cost.

### Question 2

Step 1. In the first selfed generation, a quarter of the offspring of each heterozygote are homozygous, so the frequency of aa rises from q^2 to q^2 + q(1 - q)/2.

Step 2. The load therefore rises sharply. It was 5.04 x 10^-4 for s = 0.1 and 1.63 x 10^-4 for s = 0.01, which are about 50 and 16 times the outcrossing value. This is inbreeding depression, and it is larger when selection is weaker because more recessive alleles were hidden in heterozygotes.

Step 3. Under continued selfing, nearly every copy is soon exposed in a homozygote, and the allele is purged until it is rare enough that removal again balances mutation. Iterating genotype frequencies gave an equilibrium load of 1.00 x 10^-5 for both values of s.

Answer: selfing raises the load transiently through inbreeding depression, but the equilibrium load returns to about mu, the same as under outcrossing. What changes permanently is the frequency of the allele, which falls from sqrt(mu/s) to about mu/s.

## Likely wrong answers
For Question 1, that stronger selection imposes a larger load. For Question 2, that a selfing population carries a permanently higher load, or that its load falls below the outcrossing value because purging removes the allele.
