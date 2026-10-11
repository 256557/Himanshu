# Q37 solution: SDR 2n eggs from an Ab/aB plant

## Step 1. Crossover means from map distance
Map distance gives the mean number of crossovers directly. The interval from the centromere to A is 0.15 Morgans, so m1 = 2 x 0.15 = 0.30. The interval from A to B is 0.25 Morgans, so m2 = 2 x 0.25 = 0.50.

## Step 2. What the egg carries
Second-division restitution keeps the two products of one secondary meiocyte, so the egg carries two sister chromatids. At the centromere they carry the same homolog.

## Step 3. The genotype required
The mother carries A with b on one homolog and a with B on the other. An AB/ab egg must be heterozygous at both loci, and the chromatid that carries the A-homolog at A must carry the other homolog at B. The pair must therefore be heterozygous at A and at B with the order of the homologs reversed between the two loci.

## Step 4. States of the chromatid pair and the crossover rule
At any point the two kept chromatids carry the same homolog (S) or different homologs (D). Each crossover joins one strand carrying each homolog's material at that point, with all four pairings equally likely.
1. From S, exactly one kept chromatid is involved, and the pair moves to D.
2. From D, the crossover involves both kept chromatids with probability 1/4, which reverses the order; one of them with probability 1/2, which moves the pair to S; and neither with probability 1/4.

The kept chromatids are therefore not involved independently of each other, and their involvement depends on the state reached so far.

## Step 5. Probabilities over an interval
For a Poisson number of crossovers of mean m:
1. from S, P(D) = (2/3)(1 - e^(-3m/2));
2. from D, P(D) = 2/3 + (1/3)e^(-3m/2), and P(same order) - P(reversed order) = e^(-m).

## Step 6. Centromere to A
The pair starts in S, and m1 = 0.30:

P(D at A) = (2/3)(1 - e^(-0.45)) = (2/3)(0.362372) = 0.241581.

## Step 7. A to B
The pair is in D at A, and m2 = 0.50:

P(D at B) = 2/3 + (1/3)e^(-0.75) = 0.666667 + 0.157455 = 0.824122;
P(same order) - P(reversed order) = e^(-0.5) = 0.606531;
P(D with reversed order) = (0.824122 - 0.606531)/2 = 0.108796.

## Step 8. Result
P(AB/ab) = 0.241581 x 0.108796 = 0.026283, which is 0.02628 to five decimal places.

## Answer
0.02628
