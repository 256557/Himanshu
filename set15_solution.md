# Set 15: model solution

## Question 1. Effective size and census size

### Step 1. Definition

The effective size Ne is the size of an ideal Wright-Fisher population (constant size, equal sex ratio, random union of gametes, Poisson offspring numbers) that loses heterozygosity by drift at the same rate as the real population.

Any departure from these assumptions changes Ne relative to the census size N.

### Step 2. Fluctuating size

Heterozygosity is lost at rate 1/(2Ni) in generation i, so Ne over t generations is the harmonic mean of the Ni. Sizes of 1000, 10 and 1000 give Ne of about 29.

### Step 3. Unequal sex ratio

Each sex supplies half the genes, so Ne = 4NmNf/(Nm + Nf), twice the harmonic mean of the numbers of breeding males and females. With 10 males and 90 females, Ne = 36.

### Step 4. Variance in offspring number

For a diploid population of constant size, Ne = (4N - 2)/(Vk + 2), where Vk is the variance in lifetime offspring number. Poisson variation (Vk = 2) gives Ne close to N, and a few individuals dominating reproduction gives Ne far below N. If every individual leaves exactly two offspring, Vk = 0 and Ne = 2N - 1, almost twice the census size. Simulation with N = 25 gave Ne = 49.3 (`verify/set15.py`).

### Step 5. Other demographic factors

Self-fertilisation lowers Ne to about N/(1 + F), where F is the inbreeding coefficient.

Overlapping generations and subdivision with limited migration also alter Ne, and subdivision can raise the effective size of the whole population above the summed census size of its demes when migration is low.

## Question 2. Fisher's fundamental theorem

### Step 1. What the theorem states

The change in mean fitness w can be split into two parts. The first is the change produced by selection acting on allele frequencies with the average effects of alleles held constant; it equals the additive genetic variance in fitness divided by mean fitness, VA(w)/w, and cannot be negative. The second is the change in the fitness values themselves.

Fisher's theorem concerns the first part only.

### Step 2. Why the total change can be negative

The second part has no fixed sign. It changes when fitness depends on genotype frequencies, when the environment deteriorates, when recombination breaks favourable gene combinations, and when transmission is not Mendelian. In each of these cases the fitness of a genotype is different in the next generation from its value in the current one, so the gain from selection can be outweighed by the loss in fitness values. Under negative frequency-dependent selection, for example, a genotype that becomes common loses fitness as it spreads, and mean fitness can fall while selection continues to change allele frequencies. Recurrent mutation adds a further, separate change through allele frequencies.

### Step 3. A worked example

A homozygous-lethal allele that heterozygous males transmit to 90% of their sperm spreads until one fifth of zygotes die, so mean viability falls from about 1 to 0.8 (`verify/set15.py`).

### Step 4. When mean fitness does rise

With constant viabilities at one autosomal locus and random mating, mean fitness never decreases, and the allele frequencies move up the fitness surface. This is a special case.

### Answer

No. The theorem guarantees an increase only in the selective part of the change; the total mean fitness can fall.

## Question 3. Hardy-Weinberg proportions after one generation

### Step 1. Random union of gametes

With A at frequency ps in sperm and pe in eggs, random union gives AA = ps pe, Aa = ps(1 - pe) + pe(1 - ps) and aa = (1 - ps)(1 - pe).

### Step 2. The condition

The offspring allele frequency is (ps + pe)/2, and AA equals its square only when (ps - pe)^2 = 0. Hardy-Weinberg proportions follow in one generation only if sperm and eggs carry the allele equally often.

### Step 3. Sexes that differ in allele frequency

With 0.8 in males and 0.2 in females, the offspring are 0.16 AA, 0.68 Aa and 0.16 aa, against Hardy-Weinberg values of 0.25, 0.50 and 0.25.

Their allele frequency is 0.5 in both sexes, so a second generation of random mating gives Hardy-Weinberg proportions.

### Step 4. Gametes that differ from their parents

The condition concerns gametes, not adults. If adults of both sexes carry A at 0.3 but heterozygous males transmit A to 90% of their sperm, sperm carry 0.468 and eggs 0.3, and the offspring have 0.1404 AA instead of the Hardy-Weinberg value 0.1475 (`verify/set15_hw_drive.py`). Mendelian segregation and the absence of gametic selection are therefore part of the requirement.

### Step 5. Remaining conditions

The population must be large enough that sampling of zygotes adds negligible error, and mating must be random with respect to genotype.

X-linked loci with unequal frequencies in the sexes approach equilibrium with damped oscillations, and associations between loci decay by a factor (1 - r) per generation, so neither case reaches equilibrium in one generation.

### Answer

One generation suffices when the male and female gamete pools carry the allele at the same frequency, which requires equal adult frequencies in the two sexes, Mendelian segregation, no gametic selection, random mating and a large population.
