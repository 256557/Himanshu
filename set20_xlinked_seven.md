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
