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
