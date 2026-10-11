# Question

Consider a large, randomly mating population with an equal sex ratio at fertilisation and no mutation. At an autosomal locus, heterozygous males transmit allele t to 80% of their sperm, and heterozygous females transmit it to 50% of their eggs. Males of genotype tt die before reproduction, females of genotype tt survive to reproduce with probability 0.5, and all other genotypes have equal viability. What is the equilibrium frequency of t among reproducing females? Give the answer to four decimal places.

# Solution

## Model

The allele is transmitted at different rates by the two sexes, and tt viability differs between them. Adult females and males therefore differ in genotype composition. Let F_TT, F_Tt and F_tt denote genotype frequencies among adult females, and M_TT, M_Tt and M_tt those among adult males.

## Step 1. Gamete frequencies

The frequency of t is q_e = F_Tt/2 + F_tt in eggs and q_s = 0.8 M_Tt + M_tt in sperm.

## Step 2. Zygote frequencies

Under random union of gametes, zygotes occur as TT = (1 - q_e)(1 - q_s), Tt = q_e(1 - q_s) + q_s(1 - q_e) and tt = q_e q_s. Both sexes arise from this zygote pool in equal numbers.

## Step 3. Viability selection

Females retain all TT and Tt zygotes and half of tt zygotes. Males retain TT and Tt zygotes only. Genotype frequencies within each sex are then renormalised.

## Step 4. Equilibrium

Steps 1 to 3 define a recursion for the two sets of adult frequencies. Iterated from different initial values, it converges to adult females with TT 0.3579, Tt 0.5440 and tt 0.0980, and adult males with TT 0.3969 and Tt 0.6031. Zygotes at equilibrium are TT 0.3260, Tt 0.4955 and tt 0.1786.

## Step 5. Allele frequency in females

The frequency of t among reproducing females is F_Tt/2 + F_tt = 0.5440/2 + 0.0980 = 0.3700. The corresponding frequency in males is 0.6031/2 = 0.3016.

## Remark

The standard recursion for a recessive lethal, q' = q/(1 + q), assumes a single gamete pool in Hardy-Weinberg proportions and identical genotype composition in the two sexes. Neither assumption holds here, and the recursion does not give the equilibrium.

# Answer

0.3700
