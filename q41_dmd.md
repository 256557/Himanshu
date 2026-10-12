# Q41: isolated case of an X-linked lethal

## Question
Duchenne muscular dystrophy is X-linked recessive, and affected males do not reproduce. Assume the population is at mutation-selection equilibrium with equal mutation rates in eggs and sperm. A boy is the only affected person in his family. His mother has two other sons, both unaffected, and one daughter. What is the probability that the daughter's first son will be affected? Give four decimal places.

## Answer
0.0833 (exactly 1/12)

## Solution

### 1. Prior that the mother is a carrier
At equilibrium, a third of the disease alleles in each generation are new mutations in males, and carriers occur at frequency 4u, where u is the mutation rate. An affected son arises from a carrier mother with probability 4u x 1/2 = 2u, and from a new mutation in the mother's egg with probability u. The probability that the mother of an isolated case is a carrier is therefore 2u/(2u + u) = 2/3.

### 2. Conditioning on the unaffected brothers
A carrier mother has two unaffected sons with probability (1/2)^2 = 1/4. The posterior is (2/3 x 1/4)/(2/3 x 1/4 + 1/3 x 1) = 1/3.

### 3. The daughter
She is a carrier with probability 1/3 x 1/2 = 1/6. If her mother is not a carrier, her own risk equals the population carrier frequency, which is negligible.

### 4. Her son
A carrier transmits the allele to a son with probability 1/2, so the risk is 1/6 x 1/2 = 1/12 = 0.0833.

The exact fractions are checked in `verify/q41.py`.

## Likely wrong answers
0.1667 (ignoring the unaffected brothers); 0.2500 (assuming the mother is certainly a carrier); 0.1250 (using 1/2 as the prior for the mother).
