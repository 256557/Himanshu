# Q42: isolated case of an X-linked lethal with male-biased mutation

## Question
An X-linked recessive disorder is lethal before reproduction in affected males. The population is at mutation-selection equilibrium, and the mutation rate per X chromosome is ten times higher in sperm than in eggs. A boy is the only affected person in his family. His mother has two other sons, both unaffected, and one daughter. What is the probability that the daughter's first son will be affected? Give four decimal places.

## Answer
0.1833 (exactly 11/60)

## Solution

### 1. Equilibrium carrier frequency
Let the mutation rates be u in eggs and 10u in sperm. A daughter receives her maternal X with allele frequency qf + u and her paternal X with frequency 10u, because affected fathers do not reproduce. At equilibrium qf = (qf + u)/2 + 10u/2, so qf = 11u and the carrier frequency is 22u.

### 2. Prior that the mother is a carrier
An affected son arises from a carrier mother with probability 22u x 1/2 = 11u, and from a new mutation in the mother's egg with probability u. The prior is 11u/(11u + u) = 11/12.

### 3. Conditioning on the unaffected brothers
P(carrier) = (11/12 x 1/4)/(11/12 x 1/4 + 1/12) = 11/15.

### 4. The daughter and her son
The daughter is a carrier with probability 11/30, and her son is affected with probability 11/60 = 0.1833.

The equilibrium was confirmed by iterating the two-sex recursion, and the fractions by exact arithmetic (`verify/q42.py`).

## Likely wrong answers
0.0833, from the standard prior of 2/3, which assumes equal mutation rates; 0.2292, from the prior 11/12 without conditioning on the unaffected brothers.
