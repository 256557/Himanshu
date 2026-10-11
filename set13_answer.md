# Model answer: epigenetic divergence and antagonistic pleiotropy

## Question 1. Heritable divergence without DNA sequence variation

### Step 1. Requirement
A heritable difference between genetically identical cells needs a state that is self-reinforcing, so that it is copied at division and switches only rarely.

If a state switches with probability k per division, it persists over n divisions when nk is much smaller than 1.

### Step 2. Chromatin-based memory
DNA methylation is copied after replication because UHRF1 recognises hemimethylated CpG sites and recruits DNMT1 to the new strand. Repressive histone marks are propagated by read-write feedback: the EED subunit of PRC2 binds H3K27me3 and stimulates EZH2 to methylate nearby new nucleosomes, and HP1 bound to H3K9me3 recruits SUV39H.

X inactivation is the standard example: one X is silenced at random in the early female embryo, and every descendant cell keeps the same X inactive.

### Step 3. Memory held in regulatory circuits
A gene network with positive feedback can have two stable states. In E. coli, the lac operon shows this: at intermediate inducer levels, induced and uninduced cells coexist, and each state passes to daughter cells because the permease made in an induced cell keeps it induced. Transcription factors that activate their own genes maintain cell identity in the same way.

### Step 4. Memory held in protein conformation or structure
In yeast, the prion [PSI+] is an aggregated form of the Sup35 protein that converts newly made Sup35 into the same form, so the trait is transmitted through division and mating without any sequence change. In ciliates, altered patterns of cortical structures are passed on because existing structures act as templates for new ones.

### Conclusion
Genetically identical cells can maintain heritable phenotypic differences whenever a state is copied faithfully at division by chromatin feedback, regulatory feedback or self-templating proteins.

## Question 2. When antagonistic pleiotropy favours an early-benefit, late-cost allele

### Step 1. Fitness and its age-specific gradients
Fitness is the growth rate r defined by the Euler-Lotka equation, the sum over ages of e^(-rx) l(x) m(x) = 1, where l(x) is survivorship and m(x) fecundity. Hamilton's gradients, each divided by the generation time T, are:
1. for fecundity at age x, e^(-rx) l(x);
2. for the log of survival from age a to a + 1, the sum of e^(-rx) l(x) m(x) over all ages x greater than a.

The survival gradient is constant from birth to the age of first reproduction, then declines, and is zero after the last age of reproduction.

### Step 2. Condition for spread
An allele that raises fecundity at an early age alpha by delta_m and lowers the log survival from age beta by delta_s spreads, for small effects, when

e^(-r alpha) l(alpha) delta_m > delta_s x (sum of e^(-rx) l(x) m(x) over x > beta).

### Step 3. Conditions that favour the allele
1. The cost falls late in the reproductive span, so little reproduction remains after beta; a cost after the last reproduction carries no weight.
2. Reproduction is concentrated early, as in species with early maturity and declining fecundity.
3. The population is growing (r > 0), which discounts late reproduction further.
4. The two effects cannot be separated by recombination or modifier loci, because they come from one gene product.

### Step 4. The role of extrinsic mortality
In a population growing without density regulation, raising an age-independent hazard by mu multiplies l(x) by e^(-mu x), and the Euler-Lotka equation then lowers r by exactly mu. The product e^(-rx) l(x) is unchanged, so both gradients and the condition in Step 2 stay the same. The result changes when density dependence holds the population stationary through fecundity or juvenile survival. Then r stays at 0, the factor e^(-mu x) remains in the gradients, and selection on late ages weakens, so the early-benefit allele is favoured more easily.

Extrinsic mortality therefore matters only when it varies with age or when population regulation acts through fecundity or particular ages rather than through an equal hazard at all ages (`verify/ap_extrinsic.py`, `verify/ap_density.py`).

### Conclusion
An early-benefit, late-cost allele spreads when its fecundity gain, weighted by e^(-r alpha) l(alpha), exceeds its survival cost weighted by the reproduction remaining after the cost begins. This is easiest when the cost falls late in or after the reproductive span, when reproduction is concentrated early and when the population is growing; a constant extrinsic hazard changes the outcome only through the way the population is regulated.
