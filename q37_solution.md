# Q37 solution: allelic composition of SDR 2n eggs from an Ab/aB parent

## 1. Crossover frequencies from map distance
Map distance is additive and equals half the mean number of crossovers per bivalent. Under a Poisson model, the crossover number in the centromere-A interval (0.15 M) has mean m1 = 0.30, and that in the A-B interval (0.25 M) has mean m2 = 0.50. Because the distances are map distances, no mapping function is applied.

## 2. Chromatid composition of SDR eggs
Second-division restitution retains both products of a single secondary meiocyte. Each 2n egg therefore contains two sister chromatids, which carry the same parental homolog at the centromere.

## 3. Definition of the target genotype
The parent carries the haplotypes Ab and aB. An AB/ab egg is heterozygous at both loci, and the chromatid that carries the Ab homolog at A carries the aB homolog at B. The two retained chromatids must therefore differ at A and at B, with the homolog order reversed between the loci.

## 4. State model for the retained chromatid pair
At each position along the arm the retained pair is either homozygous for parental origin (state S) or heterozygous (state D). At any position two strands carry material from each homolog, and a crossover joins one strand of each class, with the four possible pairings equally likely.
1. In state S, every crossover involves exactly one retained chromatid and converts the pair to D.
2. In state D, a crossover involves both retained chromatids with probability 1/4, which reverses the homolog order; one of them with probability 1/2, which converts the pair to S; and neither with probability 1/4.

Involvement of the two chromatids is therefore dependent on the current state, and the chromatids cannot be treated as independent.

## 5. Transition probabilities over an interval
For a Poisson number of crossovers with mean m, the model in section 4 gives:
1. from S, P(D) = (2/3)(1 - e^(-3m/2));
2. from D, P(D) = 2/3 + (1/3)e^(-3m/2), and the difference between the probabilities of retained and reversed homolog order is e^(-m).

## 6. Interval from the centromere to A
The pair enters the interval in state S. With m1 = 0.30,

P(D at A) = (2/3)(1 - e^(-0.45)) = 0.241581.

## 7. Interval from A to B
The pair enters the interval in state D. With m2 = 0.50, P(D at B) = 2/3 + (1/3)e^(-0.75) = 0.824122 and the order difference is e^(-0.5) = 0.606531. The probability that the pair remains heterozygous with reversed order is (0.824122 - 0.606531)/2 = 0.108796.

## 8. Result
The frequency of AB/ab eggs is 0.241581 x 0.108796 = 0.026283, or 0.02628 to five decimal places.

## Answer
0.02628
