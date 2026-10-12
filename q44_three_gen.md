# Q44: isolated X-linked lethal case with information on two generations

## Question
An X-linked recessive disorder is lethal before reproduction in affected males, and the population is at mutation-selection equilibrium with equal mutation rates in eggs and sperm. A boy is the only affected person in his family. His mother has three other sons, all unaffected, and one daughter. The mother's own mother has two sons, both unaffected. What is the probability that the daughter's first son will be affected? Give four decimal places.

## Answer
0.0338 (exactly 5/148)

## Solution

### 1. Population priors
At equilibrium the carrier frequency among women is 4u, where u is the mutation rate per X chromosome. A woman can also be a carrier through a new mutation in either parental gamete, with total probability 2u.

### 2. Weights of the possible histories, to first order in u
1. Grandmother carrier (prior 4u), her two sons unaffected (1/4), mother inherits the allele (1/2), mother has one affected and three unaffected sons (1/16): weight 4u x 1/4 x 1/2 x 1/16 = u/32.
2. Grandmother not a carrier, mother a carrier through a new mutation (2u), mother's sons as observed (1/16): weight u/8.
3. Neither a carrier, proband affected through a new mutation in the mother's egg: weight u.

Histories that need two independent mutations are of order u^2 and are ignored.

### 3. Posterior for the mother
P(mother carrier) = (u/32 + u/8)/(u/32 + u/8 + u) = (1 + 4)/(1 + 4 + 32) = 5/37.

### 4. The daughter and her son
The daughter is a carrier with probability 5/74, and her son is affected with probability 5/148 = 0.033784.

The enumeration was checked with exact fractions at u = 10^-7 (`verify/q44.py`).

## Likely wrong answers
0.0500, from ignoring the grandmother's unaffected sons and using the standard prior of 2/3; a larger value from using the pooled carrier frequency 6u in place of 4u.
