# Q45: isolated case of an X-linked disorder with reduced male fitness

## Question
An X-linked recessive disorder reduces the reproductive fitness of affected males to 0.5 relative to unaffected males; carrier females have normal fitness. The population is at mutation-selection equilibrium with equal mutation rates in eggs and sperm. A boy is the only affected person in his family, and his maternal grandfather is unaffected. His mother has two other sons, both unaffected, and one daughter. What is the probability that the daughter's first son will be affected? Give four decimal places.

## Answer
0.1167 (exactly 7/60)

## Solution

### 1. Equilibrium allele frequency in females
Let u be the mutation rate per X chromosome and f = 0.5 the fitness of affected males. Sons carry the allele at frequency qf + u. Fathers transmit it at about f(qf + u) + u, since affected fathers reproduce at half the normal rate. A daughter's two X chromosomes give qf = [(qf + u) + f(qf + u) + u]/2, so qf = u(2 + f)/(1 - f) = 5u, and the carrier frequency is 10u.

### 2. Carrier probability of the mother, given that her father is unaffected
Her maternal X carries the allele with probability qf + u = 6u. Her father is unaffected, so her paternal X carries it only through a new mutation, with probability u. She is therefore a carrier with prior probability 7u, not the population value 10u.

### 3. Prior given the affected son
An affected son arises from a carrier mother with probability 7u x 1/2 = 3.5u, and from a new mutation in her egg with probability u. The prior is 3.5/4.5 = 7/9.

### 4. Conditioning on the two unaffected brothers
P(carrier) = (7/9 x 1/4)/(7/9 x 1/4 + 2/9) = 7/15.

### 5. The daughter and her son
The daughter is a carrier with probability 7/30, and her son is affected with probability 7/60 = 0.1167.

The equilibrium was checked by iterating the two-sex recursion, and the fractions by exact arithmetic (`verify/q45.py`).

## Likely wrong answers
0.0833, from the textbook prior of 2/3 for a lethal disorder; 0.1389, from using the population carrier frequency 10u without allowing for the unaffected grandfather.
