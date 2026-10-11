# Question

An autosomal allele t is lethal when homozygous and has no effect in heterozygotes. Heterozygous females transmit t to 75% of their eggs; heterozygous males transmit it normally. Mating is random, the population is very large, and there is no mutation. What is the long-term frequency of t among adults? Give four decimal places.

# Solution

## Step 1. Gamete frequencies

Let x be the frequency of heterozygotes among adults; because tt dies, the adult frequency of t is x/2. Eggs carry t at 0.75x and sperm at x/2.

## Step 2. Zygotes and selection

The frequency of tt zygotes is the product of the two gametic frequencies, (0.75x)(x/2) = 0.375x^2, not the square of a single allele frequency. Heterozygous zygotes occur at 1.25x - 0.75x^2, and removing tt gives x' = (1.25x - 0.75x^2)/(1 - 0.375x^2).

## Step 3. Equilibrium

Setting x' = x gives x^2 - 2x + 2/3 = 0, so x = 1 - sqrt(1/3) = 0.4226; the other root exceeds 1. The adult frequency of t is x/2 = 0.2113. The slope of the recursion is 1.25 at x = 0, so a rare allele increases, and the equilibrium is reached from any starting frequency tested.

## Remark

The recursion q' = q/(1 + q) assumes that eggs and sperm carry t at the same frequency. Female-limited transmission bias violates this, and applying the single-pool recursion gives 0.1111.

# Answer

0.2113
