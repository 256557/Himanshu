# Q43: isolated X-linked lethal with egg-biased mutation and four unaffected brothers

## Question
An X-linked recessive disorder is lethal before reproduction in affected males. The population is at mutation-selection equilibrium, and the mutation rate per X chromosome is ten times higher in eggs than in sperm. A boy is the only affected person in his family. His mother has four other sons, all unaffected, and one daughter. What is the probability that the daughter's first son will be affected? Give four decimal places.

## Answer
0.0161 (exactly 11/684)

## Solution

### 1. Equilibrium allele frequency in females
Let the mutation rates be u in eggs and 0.1u in sperm. A daughter receives her maternal X at allele frequency qf + u and her paternal X at frequency 0.1u, because affected fathers do not reproduce. At equilibrium qf = (qf + u + 0.1u)/2, so qf = 1.1u and the carrier frequency among women is 2.2u.

### 2. Prior odds that the mother is a carrier
An affected son arises from a carrier mother with probability 2.2u x 1/2 = 1.1u, and from a new mutation in the egg with probability u. The prior odds are 1.1 : 1.

### 3. Conditioning on four unaffected brothers
A carrier mother has four unaffected sons with probability (1/2)^4 = 1/16. The posterior odds are 1.1/16 : 1, so P(carrier) = (1.1/16)/(1.1/16 + 1) = 11/171 = 0.064327.

### 4. The daughter and her son
The daughter is a carrier with probability 11/342, and her son is affected with probability 11/684 = 0.016082.

The equilibrium was confirmed by iterating the two-sex recursion, and the fractions by exact arithmetic (`verify/q43.py`).

## Likely wrong answers
0.0290, from pooling male and female X chromosomes into one allele frequency (carrier frequency 4.2u); 0.0278, from the textbook prior of 2/3 for equal mutation rates. Both are about 1.7 to 1.8 times the correct value.
