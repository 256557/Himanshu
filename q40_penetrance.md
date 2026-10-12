# Q40: reduced penetrance with Bayesian conditioning

## Question
An autosomal dominant disorder has a penetrance of 80%, and affected status does not depend on age in adults. A man's father is affected and heterozygous; his mother is unaffected and carries no disease allele. The man is unaffected, and so are his two children by an unrelated non-carrier woman. What is the probability that their next child will be affected? Give four decimal places.

## Answer
0.0269 (exactly 9/335)

## Solution

### 1. Prior probability
The man received his father's disease allele with probability 1/2.

### 2. Likelihood of the observations
If he is a carrier, he is unaffected with probability 0.2, and each child is unaffected with probability 1 - (1/2)(0.8) = 0.6. The joint likelihood is 0.2 x 0.6^2 = 0.072. If he is not a carrier, every observation has probability 1.

### 3. Posterior probability
P(carrier) = (0.5 x 0.072)/(0.5 x 0.072 + 0.5 x 1) = 0.036/0.536 = 9/134 = 0.067164.

### 4. Next child
The child is affected if the man is a carrier, transmits the allele and the allele is penetrant: 0.067164 x 0.5 x 0.8 = 0.026866.

Exact fractions are in `verify/q40.py`.

## Likely wrong answers
0.2000 if the man's unaffected status is ignored; 0.0667 if his status is used but the unaffected children are ignored.
