# X-linked isolated-case questions: handoff notes

Model A results: Q41 and Q42 failed (it pooled male and female X chromosomes into one allele frequency). Q43, Q44 and Q45 were solved correctly, so this question type is now usually solved by Model A. Use it only with a new twist.

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
0.1667 (ignoring the unaffected brothers); 0.2500 (assuming the mother is certainly a carrier); 0.0500 (using 1/2 as the prior for the mother).


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


# Set 20: seven isolated-case questions on X-linked disorders

Common method. Let u be the mutation rate per X in eggs, ku in sperm, and f the relative fitness of affected males. Daughters receive a maternal X with allele frequency qf + u and a paternal X with frequency f(qf + u) + ku, so qf = u[(1 + f) + k]/(1 - f). A woman's prior carrier probability is C = 2qf in general, or qf + u + ku if her father is known to be unaffected. Given one affected son, the prior odds that the mother is a carrier are (C/2) : u. 

Each unaffected brother multiplies the odds by 1/2. The risk to the sister's first son is P(mother carrier) x 1/2 x 1/2.

## Q1
An X-linked recessive disorder is lethal before reproduction in affected males; carrier females have normal fitness. The population is at mutation-selection equilibrium with equal mutation rates in eggs and sperm. A boy is the only affected person in his family. His mother has three other sons, all unaffected, and one daughter. What is the probability that the daughter's first son will be affected? Give four decimal places.

Solution. f = 0, k = 1. Equilibrium qf = 2u. Prior carrier probability of the mother C = 4u. Prior odds 2 : 1. After 3 unaffected brothers, odds 1/4 : 1, so P(carrier) = 1/5. Risk = 1/5 x 1/4 = 1/20 = 0.0500.

Answer: 0.0500

## Q2
An X-linked recessive disorder is lethal before reproduction in affected males; carrier females have normal fitness. The population is at mutation-selection equilibrium with a mutation rate per X chromosome 4 times higher in sperm than in eggs. A boy is the only affected person in his family. His mother has two other sons, both unaffected, and one daughter. What is the probability that the daughter's first son will be affected? Give four decimal places.

Solution. f = 0, k = 4. Equilibrium qf = 5u. Prior carrier probability of the mother C = 10u. Prior odds 5 : 1. After 2 unaffected brothers, odds 5/4 : 1, so P(carrier) = 5/9. Risk = 5/9 x 1/4 = 5/36 = 0.1389.

Answer: 0.1389

## Q3
An X-linked recessive disorder reduces the reproductive fitness of affected males to 0.50 relative to unaffected males; carrier females have normal fitness. The population is at mutation-selection equilibrium with equal mutation rates in eggs and sperm. A boy is the only affected person in his family. His maternal grandfather is unaffected. His mother has three other sons, all unaffected, and one daughter. What is the probability that the daughter's first son will be affected? Give four decimal places.

Solution. f = 1/2, k = 1. Equilibrium qf = 5u. Prior carrier probability of the mother C = 7u (father unaffected). Prior odds 7/2 : 1. After 3 unaffected brothers, odds 7/16 : 1, so P(carrier) = 7/23. Risk = 7/23 x 1/4 = 7/92 = 0.0761.

Answer: 0.0761

## Q4
An X-linked recessive disorder reduces the reproductive fitness of affected males to one third relative to unaffected males; carrier females have normal fitness. The population is at mutation-selection equilibrium with equal mutation rates in eggs and sperm. A boy is the only affected person in his family. His maternal grandfather is unaffected. His mother has two other sons, both unaffected, and one daughter. What is the probability that the daughter's first son will be affected? Give four decimal places.

Solution. f = 1/3, k = 1. Equilibrium qf = (7/2)u. Prior carrier probability of the mother C = (11/2)u (father unaffected). Prior odds 11/4 : 1. After 2 unaffected brothers, odds 11/16 : 1, so P(carrier) = 11/27. Risk = 11/27 x 1/4 = 11/108 = 0.1019.

Answer: 0.1019

## Q5
An X-linked recessive disorder reduces the reproductive fitness of affected males to 0.50 relative to unaffected males; carrier females have normal fitness. The population is at mutation-selection equilibrium with a mutation rate per X chromosome 2 times higher in sperm than in eggs. A boy is the only affected person in his family. His mother has one other son, who is unaffected, and one daughter. What is the probability that the daughter's first son will be affected? Give four decimal places.

Solution. f = 1/2, k = 2. Equilibrium qf = 7u. Prior carrier probability of the mother C = 14u. Prior odds 7 : 1. After 1 unaffected brother, odds 7/2 : 1, so P(carrier) = 7/9. Risk = 7/9 x 1/4 = 7/36 = 0.1944.

Answer: 0.1944

## Q6
An X-linked recessive disorder reduces the reproductive fitness of affected males to 0.25 relative to unaffected males; carrier females have normal fitness. The population is at mutation-selection equilibrium with new mutations arising only in eggs. A boy is the only affected person in his family. His maternal grandfather is unaffected. His mother has two other sons, both unaffected, and one daughter. What is the probability that the daughter's first son will be affected? Give four decimal places.

Solution. f = 1/4, k = 0. Equilibrium qf = (5/3)u. Prior carrier probability of the mother C = (8/3)u (father unaffected). Prior odds 4/3 : 1. After 2 unaffected brothers, odds 1/3 : 1, so P(carrier) = 1/4. Risk = 1/4 x 1/4 = 1/16 = 0.0625.

Answer: 0.0625

## Q7
An X-linked recessive disorder is lethal before reproduction in affected males; carrier females have normal fitness. The population is at mutation-selection equilibrium with a mutation rate per X chromosome 2 times higher in eggs than in sperm. A boy is the only affected person in his family. His mother has five other sons, all unaffected, and one daughter. What is the probability that the daughter's first son will be affected? Give four decimal places.

Solution. f = 0, k = 1/2. Equilibrium qf = (3/2)u. Prior carrier probability of the mother C = 3u. Prior odds 3/2 : 1. After 5 unaffected brothers, odds 3/64 : 1, so P(carrier) = 3/67. Risk = 3/67 x 1/4 = 3/268 = 0.0112.

Answer: 0.0112

All values were computed with exact fractions and the equilibrium was checked by iteration (`verify/set20.py`).


# Set 20: step-by-step solutions

## Q1

### 1. Equilibrium allele frequency in females

Let μ be the mutation rate per X chromosome in eggs, μ the rate in sperm, and f = 0 the fitness of affected males. Sons carry the allele at frequency q_f + μ. Affected males do not reproduce, so fathers transmit the allele only through a new mutation in sperm, so the paternal X carries the allele at f(q_f + μ) + μ. A daughter's two X chromosomes give q_f = [(q_f + μ) + f(q_f + μ) + μ]/2, so q_f = μ[(1 + f) + 1]/(1 − f) = 2μ, and the carrier frequency is 4μ.

### 2. Carrier probability of the mother

Nothing is known about the mother's parents, so her prior probability of being a carrier is the population carrier frequency, 4μ.

### 3. Prior given the affected son

An affected son arises from a carrier mother with probability 4μ × 1/2 = 2μ, and from a new mutation in her egg with probability μ. The prior is 2/(2 + 1) = 2/3.

### 4. Conditioning on the three unaffected brothers

A carrier mother has three unaffected sons with probability (1/2)^3 = 1/8, and a non-carrier mother with probability 1.

P(carrier) = (2/3 × 1/8)/(2/3 × 1/8 + 1/3) = 1/5

### 5. The daughter and her son

The daughter is a carrier with probability 1/5 × 1/2 = 1/10, and her son is affected with probability 1/10 × 1/2 = 1/20 = 0.0500.

**Answer: 0.0500**

## Q2

### 1. Equilibrium allele frequency in females

Let μ be the mutation rate per X chromosome in eggs, 4μ the rate in sperm, and f = 0 the fitness of affected males. Sons carry the allele at frequency q_f + μ. Affected males do not reproduce, so fathers transmit the allele only through a new mutation in sperm, so the paternal X carries the allele at f(q_f + μ) + 4μ. A daughter's two X chromosomes give q_f = [(q_f + μ) + f(q_f + μ) + 4μ]/2, so q_f = μ[(1 + f) + 4]/(1 − f) = 5μ, and the carrier frequency is 10μ.

### 2. Carrier probability of the mother

Nothing is known about the mother's parents, so her prior probability of being a carrier is the population carrier frequency, 10μ.

### 3. Prior given the affected son

An affected son arises from a carrier mother with probability 10μ × 1/2 = 5μ, and from a new mutation in her egg with probability μ. The prior is 5/(5 + 1) = 5/6.

### 4. Conditioning on the two unaffected brothers

A carrier mother has two unaffected sons with probability (1/2)^2 = 1/4, and a non-carrier mother with probability 1.

P(carrier) = (5/6 × 1/4)/(5/6 × 1/4 + 1/6) = 5/9

### 5. The daughter and her son

The daughter is a carrier with probability 5/9 × 1/2 = 5/18, and her son is affected with probability 5/18 × 1/2 = 5/36 = 0.1389.

**Answer: 0.1389**

## Q3

### 1. Equilibrium allele frequency in females

Let μ be the mutation rate per X chromosome in eggs, μ the rate in sperm, and f = 1/2 the fitness of affected males. Sons carry the allele at frequency q_f + μ. Fathers transmit it at about f(q_f + μ) plus new sperm mutations, since affected fathers reproduce at 1/2 of the normal rate, so the paternal X carries the allele at f(q_f + μ) + μ. A daughter's two X chromosomes give q_f = [(q_f + μ) + f(q_f + μ) + μ]/2, so q_f = μ[(1 + f) + 1]/(1 − f) = 5μ, and the carrier frequency is 10μ.

### 2. Carrier probability of the mother, given that her father is unaffected

Her maternal X carries the allele with probability q_f + μ = 6μ, and her father is unaffected, so her paternal X carries it only through a new mutation, with probability μ. She is therefore a carrier with prior probability 7μ, not the population value 10μ.

### 3. Prior given the affected son

An affected son arises from a carrier mother with probability 7μ × 1/2 = (7/2)μ, and from a new mutation in her egg with probability μ. The prior is 7/2/(7/2 + 1) = 7/9.

### 4. Conditioning on the three unaffected brothers

A carrier mother has three unaffected sons with probability (1/2)^3 = 1/8, and a non-carrier mother with probability 1.

P(carrier) = (7/9 × 1/8)/(7/9 × 1/8 + 2/9) = 7/23

### 5. The daughter and her son

The daughter is a carrier with probability 7/23 × 1/2 = 7/46, and her son is affected with probability 7/46 × 1/2 = 7/92 = 0.0761.

**Answer: 0.0761**

## Q4

### 1. Equilibrium allele frequency in females

Let μ be the mutation rate per X chromosome in eggs, μ the rate in sperm, and f = 1/3 the fitness of affected males. Sons carry the allele at frequency q_f + μ. Fathers transmit it at about f(q_f + μ) plus new sperm mutations, since affected fathers reproduce at 1/3 of the normal rate, so the paternal X carries the allele at f(q_f + μ) + μ. A daughter's two X chromosomes give q_f = [(q_f + μ) + f(q_f + μ) + μ]/2, so q_f = μ[(1 + f) + 1]/(1 − f) = (7/2)μ, and the carrier frequency is 7μ.

### 2. Carrier probability of the mother, given that her father is unaffected

Her maternal X carries the allele with probability q_f + μ = (9/2)μ, and her father is unaffected, so her paternal X carries it only through a new mutation, with probability μ. She is therefore a carrier with prior probability (11/2)μ, not the population value 7μ.

### 3. Prior given the affected son

An affected son arises from a carrier mother with probability (11/2)μ × 1/2 = (11/4)μ, and from a new mutation in her egg with probability μ. The prior is 11/4/(11/4 + 1) = 11/15.

### 4. Conditioning on the two unaffected brothers

A carrier mother has two unaffected sons with probability (1/2)^2 = 1/4, and a non-carrier mother with probability 1.

P(carrier) = (11/15 × 1/4)/(11/15 × 1/4 + 4/15) = 11/27

### 5. The daughter and her son

The daughter is a carrier with probability 11/27 × 1/2 = 11/54, and her son is affected with probability 11/54 × 1/2 = 11/108 = 0.1019.

**Answer: 0.1019**

## Q5

### 1. Equilibrium allele frequency in females

Let μ be the mutation rate per X chromosome in eggs, 2μ the rate in sperm, and f = 1/2 the fitness of affected males. Sons carry the allele at frequency q_f + μ. Fathers transmit it at about f(q_f + μ) plus new sperm mutations, since affected fathers reproduce at 1/2 of the normal rate, so the paternal X carries the allele at f(q_f + μ) + 2μ. A daughter's two X chromosomes give q_f = [(q_f + μ) + f(q_f + μ) + 2μ]/2, so q_f = μ[(1 + f) + 2]/(1 − f) = 7μ, and the carrier frequency is 14μ.

### 2. Carrier probability of the mother

Nothing is known about the mother's parents, so her prior probability of being a carrier is the population carrier frequency, 14μ.

### 3. Prior given the affected son

An affected son arises from a carrier mother with probability 14μ × 1/2 = 7μ, and from a new mutation in her egg with probability μ. The prior is 7/(7 + 1) = 7/8.

### 4. Conditioning on the one unaffected brother

A carrier mother has one unaffected son with probability (1/2)^1 = 1/2, and a non-carrier mother with probability 1.

P(carrier) = (7/8 × 1/2)/(7/8 × 1/2 + 1/8) = 7/9

### 5. The daughter and her son

The daughter is a carrier with probability 7/9 × 1/2 = 7/18, and her son is affected with probability 7/18 × 1/2 = 7/36 = 0.1944.

**Answer: 0.1944**

## Q6

### 1. Equilibrium allele frequency in females

Let μ be the mutation rate per X chromosome in eggs, 0 the rate in sperm, and f = 1/4 the fitness of affected males. Sons carry the allele at frequency q_f + μ. Fathers transmit it at about f(q_f + μ) plus new sperm mutations, since affected fathers reproduce at 1/4 of the normal rate, so the paternal X carries the allele at f(q_f + μ) + 0. A daughter's two X chromosomes give q_f = [(q_f + μ) + f(q_f + μ) + 0]/2, so q_f = μ[(1 + f) + 0]/(1 − f) = (5/3)μ, and the carrier frequency is (10/3)μ.

### 2. Carrier probability of the mother, given that her father is unaffected

Her maternal X carries the allele with probability q_f + μ = (8/3)μ, and her paternal X is normal, because her father is unaffected and sperm do not mutate. She is therefore a carrier with prior probability (8/3)μ, not the population value (10/3)μ.

### 3. Prior given the affected son

An affected son arises from a carrier mother with probability (8/3)μ × 1/2 = (4/3)μ, and from a new mutation in her egg with probability μ. The prior is 4/3/(4/3 + 1) = 4/7.

### 4. Conditioning on the two unaffected brothers

A carrier mother has two unaffected sons with probability (1/2)^2 = 1/4, and a non-carrier mother with probability 1.

P(carrier) = (4/7 × 1/4)/(4/7 × 1/4 + 3/7) = 1/4

### 5. The daughter and her son

The daughter is a carrier with probability 1/4 × 1/2 = 1/8, and her son is affected with probability 1/8 × 1/2 = 1/16 = 0.0625.

**Answer: 0.0625**

## Q7

### 1. Equilibrium allele frequency in females

Let μ be the mutation rate per X chromosome in eggs, (1/2)μ the rate in sperm, and f = 0 the fitness of affected males. Sons carry the allele at frequency q_f + μ. Affected males do not reproduce, so fathers transmit the allele only through a new mutation in sperm, so the paternal X carries the allele at f(q_f + μ) + (1/2)μ. A daughter's two X chromosomes give q_f = [(q_f + μ) + f(q_f + μ) + (1/2)μ]/2, so q_f = μ[(1 + f) + 1/2]/(1 − f) = (3/2)μ, and the carrier frequency is 3μ.

### 2. Carrier probability of the mother

Nothing is known about the mother's parents, so her prior probability of being a carrier is the population carrier frequency, 3μ.

### 3. Prior given the affected son

An affected son arises from a carrier mother with probability 3μ × 1/2 = (3/2)μ, and from a new mutation in her egg with probability μ. The prior is 3/2/(3/2 + 1) = 3/5.

### 4. Conditioning on the five unaffected brothers

A carrier mother has five unaffected sons with probability (1/2)^5 = 1/32, and a non-carrier mother with probability 1.

P(carrier) = (3/5 × 1/32)/(3/5 × 1/32 + 2/5) = 3/67

### 5. The daughter and her son

The daughter is a carrier with probability 3/67 × 1/2 = 3/134, and her son is affected with probability 3/134 × 1/2 = 3/268 = 0.0112.

**Answer: 0.0112**


