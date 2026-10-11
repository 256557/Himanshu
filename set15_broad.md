# Set 15: broad questions with a hidden trap

## Questions (paste together)
1. How do demography and variation in offspring number cause the effective size of a population to differ from its census size?
2. Does Fisher's fundamental theorem of natural selection imply that the mean fitness of a population increases whenever selection acts?
3. Under what conditions does a single generation of random mating bring an autosomal locus to Hardy-Weinberg proportions?

## Answers

### Q1
Ne is reduced by fluctuating size (Ne is the harmonic mean over generations), by an unequal sex ratio (Ne = 4NmNf/(Nm + Nf)) and by variance in offspring number above the Poisson value. The trap is the opposite case. With Ne = (4N - 2)/(Vk + 2), a population in which every individual leaves exactly two offspring (Vk = 0) has Ne = 2N - 1, almost twice the census size; equalising family sizes in captive breeding uses this. Simulation with N = 25 and Vk = 0 gave Ne = 49.3 against 2N - 1 = 49 (`verify/set15.py`).
Likely wrong answer: Ne is always smaller than or equal to N.

### Q2
No. The theorem, as clarified by Price (1972), gives the partial change in mean fitness caused by selection, equal to the additive genetic variance in fitness divided by mean fitness, with the environment, including allele frequencies' effects on fitness, held constant. The total change can be negative. Under frequency-dependent selection, a deteriorating environment or gametic selection, mean fitness can fall. For example, a male-limited driver (transmission 0.9) that is lethal in homozygotes spreads while mean viability falls from about 1 to 0.8 (`verify/set15.py`). Mean fitness rises monotonically only in special cases, such as constant viability selection at one locus.
Likely wrong answer: yes, mean fitness always increases at a rate equal to the additive variance in fitness.

### Q3
One generation suffices only if allele frequencies are equal in the two sexes, in addition to the usual conditions of a large population, no selection, mutation or migration, and Mendelian segregation. If they differ, the first generation of offspring has the average allele frequency but an excess of heterozygotes. With p = 0.8 in males and 0.2 in females, offspring are 0.16 AA, 0.68 Aa and 0.16 aa, against 0.25, 0.50 and 0.25 expected; a second generation of random mating gives Hardy-Weinberg proportions. X-linked loci approach equilibrium with damped oscillations, and associations between loci decay by a factor (1 - r) per generation, so neither reaches equilibrium in one generation.
Likely wrong answer: one generation of random mating is always enough for an autosomal locus.
