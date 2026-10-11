# Set 16: broad questions with a hidden trap

## Questions (paste together)
1. How does linkage disequilibrium between two linked loci decay under random mating, and what determines its rate in a species such as Drosophila melanogaster?
2. How does the strength of selection against a deleterious mutation affect the genetic load it imposes on a population at mutation-selection balance?
3. How does population size affect the probability that a single new beneficial mutation becomes fixed, and the rate at which beneficial substitutions accumulate?

## Solution

### Q1. Decay of linkage disequilibrium

Step 1. Under random mating in a large population, only recombinant gametes break up an association, so D falls by a factor (1 - c) each generation: D_t = D_0 (1 - c)^t.

Step 2. The rate c is the recombination fraction averaged over the two sexes, because each offspring receives one gamete from each parent.

Step 3. Drosophila males do not undergo meiotic crossing over. With a female recombination fraction cf, the average is cf/2, so D decays by (1 - cf/2) per generation. For cf = 0.2 the factor is 0.9, not 0.8; a two-sex recursion gives 0.9 exactly (`verify/set16.py`).

Step 4. In a finite population drift creates new disequilibrium, so the expected r^2 approaches a value near 1/(1 + 4Ne c) rather than zero.

Answer: D decays geometrically at a rate set by the sex-averaged recombination fraction, which in Drosophila is half the female value.

Likely wrong answer: D_t = D_0 (1 - c)^t with c taken from the female map distance.

### Q2. Genetic load and the strength of selection

Step 1. At equilibrium, mutation adds deleterious alleles at rate mu per gamete, and selection removes them at the same rate.

Step 2. For a partially dominant allele, q is approximately mu/(hs) and the load is approximately 2mu. For a fully recessive allele, q is approximately the square root of mu/s and the load is approximately mu.

Step 3. The strength of selection cancels: weaker selection raises the equilibrium frequency by the same factor that it lowers the fitness cost per copy. With mu = 10^-5 and h = 0.5, the load was 1.90 x 10^-5 for s = 0.1 and 1.99 x 10^-5 for s = 0.01; with h = 0 it was 1.00 x 10^-5 for both (`verify/set16.py`).

Step 4. Dominance does matter, as do inbreeding (which exposes recessive alleles) and the total genomic mutation rate, which sums the loads over loci.

Answer: the load is nearly independent of s and is set by the mutation rate (Haldane-Muller principle); s determines how common the allele is, not how much fitness it costs the population.

Likely wrong answer: stronger selection imposes a larger load.

### Q3. Population size and beneficial mutations

Step 1. For a new mutation with heterozygous advantage s in a population with Ne = N, the fixation probability is (1 - e^(-2s))/(1 - e^(-4Ns)), which approaches 2s once 4Ns is large.

Step 2. The fixation probability of a single mutation therefore does not depend on N. With s = 0.01, it is 0.0202 for N = 100 and 0.0198 for N = 1000 and 10000 (`verify/set16.py`).

Step 3. When Ne differs from N, the probability is approximately 2s Ne/N. With N = 10 Ne it falls to 0.0020.

Step 4. The rate of substitution is the number of new mutations, 2N mu, times the fixation probability, giving about 4N mu s, which does rise with N.

Answer: larger populations do not fix a given beneficial mutation more often; they accumulate beneficial substitutions faster because more mutations arise.

Likely wrong answer: the fixation probability of each beneficial mutation increases with population size.
