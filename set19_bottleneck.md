# Set 19: bottlenecks and additive genetic variance

## Question
A large population passes through a severe bottleneck and then recovers in size. How does the bottleneck change the additive genetic variance of a quantitative trait, and does the answer depend on the genetic architecture of the trait?

## Solution

### 1. Purely additive traits
When alleles act additively within and between loci, additive variance is proportional to heterozygosity. A bottleneck of effective size N lowers heterozygosity by a factor (1 - 1/(2N)) per generation, so the expected additive variance falls by the same factor, and the loss is permanent until mutation restores it.

### 2. Dominance
With dominance, additive variance at a locus is VA = 2pq[a + d(q - p)]^2 and depends on allele frequency as well as on heterozygosity. A rare recessive allele contributes little additive variance, because most of its copies sit in heterozygotes with no phenotypic effect. Drift that raises its frequency converts dominance variance into additive variance.

### 3. A worked example
Take complete dominance (a = d = 1) and a recessive allele at q = 0.1, so VA = 8pq^3 = 0.0072. After one generation founded by two individuals (four gene copies), expected heterozygosity falls from 0.180 to 0.135, but expected additive variance rises to 0.0547, about 7.6 times the original value (`verify/set19_bottleneck_va.py`).

### 4. Epistasis
With epistasis, the average effect of an allele depends on the frequencies at other loci. Drift that changes those frequencies converts part of the epistatic variance into additive variance, and the expected additive variance can rise after a bottleneck.

### 5. Limits
The increase is an expectation over replicate populations. Individual bottlenecked populations vary widely, many lose the variant altogether, and the total genetic variance and mean fitness usually fall through inbreeding depression.

## Answer
For a purely additive trait, a bottleneck reduces additive variance in proportion to the loss of heterozygosity. When dominance or epistasis contributes to the trait, drift can convert non-additive variance into additive variance, and the expected additive variance can rise even though heterozygosity falls.

## Likely wrong answer
A bottleneck always reduces additive genetic variance because it reduces heterozygosity.
