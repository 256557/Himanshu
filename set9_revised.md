# Set 9: revised questions

## Q1
An autosomal allele a is lethal in homozygotes before reproduction and has no effect in heterozygotes. A single new copy of a arises in a randomly mating population of 20 diploid adults of constant size, with no further mutation or migration. What is the probability that a eventually becomes fixed among adults?

Answer: 0. Loss is certain.

Every adult is AA or Aa, so the adult frequency of a can never exceed 1/2. A population fixed for a would consist only of aa zygotes, and all of them die. In 200,000 simulated populations a was always lost, and its highest adult frequency was 0.475 (`verify/set9.py`).
Likely wrong answers: 1/40 = 0.025 (neutral fixation probability) or a Kimura diffusion value.

## Q2
An autosomal allele t is lethal when homozygous and has no effect in heterozygotes. Heterozygous females transmit t to 60% of their eggs, and heterozygous males transmit it to 90% of their sperm. Mating is random, the population is very large, and there is no mutation. What is the long-term frequency of t among adults? Give four decimal places.

Answer: 0.3639. With x the adult heterozygote frequency, eggs carry t at 0.6x and sperm at 0.9x, so tt = 0.54x^2 and x' = (1.5x - 1.08x^2)/(1 - 0.54x^2). Equilibrium: 0.54x^2 - 1.08x + 0.5 = 0, so x = 1 - sqrt(1 - 0.5/0.54) = 0.7278, and the allele frequency is x/2 = 0.3639. A polymorphism exists whenever the two transmission rates sum to more than 1.
Likely wrong answer: 0.3333, from averaging the rates.

## Q3
A pregnant mouse is exposed to an endocrine disruptor, and an altered phenotype is later seen in her descendants. From which generation can the phenotype be attributed to transgenerational epigenetic inheritance rather than direct exposure, and how does this change if an adult male is exposed before mating instead? Can such inheritance produce adaptation without any change in DNA sequence?

Answer outline:
1. Maternal exposure during gestation reaches the F0 mother, the F1 embryo and the F1 embryo's germ cells, which form the F2. The F3 is the first unexposed generation.
2. Exposure of an adult male reaches his germ cells, which form the F1, so the F2 is the first unexposed generation.
3. Adaptation requires a heritable state that persists long enough for selection to act on it. Most reported mammalian effects fade within a few generations, so evidence for adaptation in mammals is weak. Longer-lasting transmission of small-RNA-dependent silencing is documented in C. elegans, and stable epialleles are documented in plants.
