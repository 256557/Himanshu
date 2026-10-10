# Probe batch 5: harder biology, 5 questions

## Questions (type as written)

E1. Genes a, b and c lie in that order; a-b is 10 map units and b-c is 20 map units, with a coefficient of coincidence of 0.5. In a testcross of the triple heterozygote, what percentage of progeny are recombinant between a and c?
E2. For an X-linked allele, the frequency is 0.6 in females and 0.2 in males. With random mating, what is its frequency in females after two generations, and at equilibrium?
E3. In mice, yellow (A^Y) is dominant and lethal when homozygous, and bb mice are albino regardless of the A locus. Two A^Y a Bb mice are crossed. What fraction of the living offspring are yellow?
E4. A recessive lethal allele has frequency 0.1. With no new mutation, what is its frequency after 10 generations?
E5. Of the 9 possible single-nucleotide substitutions in the codon UAU, how many are synonymous, missense and nonsense?

## Answer key (do not show to the model)

| # | Answer | Trap |
|---|---|---|
| E1 | 28% | DCO = 0.1 x 0.2 x 0.5 = 0.01. a-c recombinants = 0.10 + 0.20 - 2(0.01) = 0.28. Double crossovers restore the parental a-c combination. Common errors: 30% or 29%. |
| E2 | 0.5 after two generations; 7/15 (about 0.467) at equilibrium | Females take the average of both parents and males take the mother's value: gen 1 F 0.4, M 0.6; gen 2 F 0.5. Equilibrium = (2 x 0.6 + 0.2) / 3. Common error: a simple average of 0.4. |
| E3 | 1/2 | Among survivors, A^Y a is 2/3 and B_ is 3/4, so 2/3 x 3/4 = 1/2. Common errors: 2/3 (ignores albino epistasis) or 9/16. |
| E4 | 0.05 | For a recessive lethal, q_t = q0 / (1 + t q0) = 0.1 / 2. Common errors come from geometric decay (0.1 x 0.99^10 and similar). |
| E5 | 1 synonymous (UAC), 6 missense, 2 nonsense (UAA, UAG) | Check every position: the first two positions are all missense, and the third gives UAC (Tyr), UAA (stop), UAG (stop). |

All answers computed exactly by script (fractions, enumeration and the standard codon table).
