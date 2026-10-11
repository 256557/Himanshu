# Question

An autosomal allele t shows meiotic drive in males: heterozygous males transmit it to 80% of their sperm, and heterozygous females transmit it to 50% of their eggs. Homozygous tt males die before reproduction, tt females survive with probability 0.5, and all other genotypes survive with probability 1. The sex ratio at fertilisation is 1:1, mating is random, the population is very large, and there is no mutation. At the long-term equilibrium, give (a) the frequency of t among adult females, (b) the frequency of t among adult males, and (c) the fraction of zygotes that die. Give four decimal places.

# Solution

## Model

Female and male adults differ in genotype composition, because tt survives only in females. Let F = (F_TT, F_Tt, F_tt) and M = (M_TT, M_Tt, M_tt) be the adult genotype frequencies in each sex.

## Step 1. Gamete frequencies

The frequency of t in eggs is q_e = F_Tt/2 + F_tt. The frequency of t in sperm is q_s = 0.8 M_Tt + M_tt.

## Step 2. Zygotes

Both sexes arise from the same zygote pool: TT = (1 - q_e)(1 - q_s), Tt = q_e(1 - q_s) + q_s(1 - q_e), tt = q_e q_s.

## Step 3. Sex-specific viability

Females keep all TT and Tt zygotes and half of tt; males keep TT and Tt only. Each sex is then normalised to sum to 1.

## Step 4. Why a single allele frequency is insufficient

Egg and sperm frequencies differ because of drive, and adult frequencies differ between sexes because of sex-limited viability. A recursion in one allele frequency with Hardy-Weinberg zygotes therefore misstates both the tt frequency and the composition of each sex, so the two sexes have to be iterated jointly.

## Step 5. Equilibrium

Iterating Steps 1 to 3 converges to the same point from different starting frequencies. At equilibrium, females are TT 0.3579, Tt 0.5440 and tt 0.0980; males are TT 0.3969 and Tt 0.6031. Zygotes are TT 0.3260, Tt 0.4955 and tt 0.1786.

## Step 6. Zygote loss

Half of tt zygotes are male and all of these die; half are female and half of these die. The fraction lost is 0.1786 x (0.5 + 0.25) = 0.1339.

## Result

(a) 0.3700 among adult females, (b) 0.3016 among adult males, (c) 0.1339 of zygotes die.

Verified by deterministic iteration from two starting points (`verify/q31.py`); academic-prose checker: no violations.
