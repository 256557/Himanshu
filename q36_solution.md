# Q36 solution: central fusion, AB/ab mother, Ab/aB daughters

## Step 1. Crossover means from map distance
Map distance is additive and equals half the mean number of crossovers per meiosis. Each interval is 20 cM, or 0.20 Morgans, so the number of crossovers in each interval is Poisson with mean m = 2 x 0.20 = 0.40. The distances are map distances, so no mapping-function conversion is needed.

## Step 2. What the daughter carries
Central fusion joins two nuclei that separated at the first meiotic division. The daughter therefore keeps two non-sister chromatids, which carry different homologs at the centromere.

## Step 3. States of the chromatid pair
At any point along the arm, the two kept chromatids carry either the same homolog (state S, homozygous) or different homologs (state D, heterozygous). For a double heterozygote, D has two phases. In coupling, the chromatid carrying the A-homolog at A also carries the B-homolog at B (AB/ab). In repulsion, it carries the b-homolog at B (Ab/aB).

## Step 4. Effect of one crossover
At any point two strands carry material of one homolog and two carry material of the other. Each crossover joins one strand of each kind, with all four pairings equally likely. Starting from D:
1. with probability 1/4 the crossover joins the two kept chromatids, which exchanges their distal material and reverses the phase;
2. with probability 1/2 it involves one kept chromatid, which then carries the same material as the other, so the pair moves to S;
3. with probability 1/4 it involves neither, and the pair is unchanged.

From S, exactly one kept chromatid is involved in every crossover, so the pair always returns to D.

Because the outcome of each crossover depends on the current state of the pair, the two chromatids cannot be followed separately, and crossover counts on fixed chromatid pairs cannot be added by parity.

## Step 5. Probabilities over an interval
Combining Step 4 with a Poisson number of crossovers of mean m gives, for a pair that starts in D:
1. P(D) = 2/3 + (1/3)e^(-3m/2);
2. P(same phase) - P(reversed phase) = e^(-m).

The probability of D with reversed phase is therefore (P(D) - e^(-m))/2.

## Step 6. Centromere to A
The pair starts in D, and m = 0.40:

P(D at A) = 2/3 + (1/3)e^(-0.6) = 0.666667 + 0.182937 = 0.849604.

## Step 7. A to B
The pair is in D at A, and m = 0.40:

P(D at B) = 2/3 + (1/3)e^(-0.6) = 0.849604;
P(same phase) - P(reversed phase) = e^(-0.4) = 0.670320;
P(D with reversed phase) = (0.849604 - 0.670320)/2 = 0.089642.

## Step 8. Result
P(Ab/aB) = 0.849604 x 0.089642 = 0.076160, which is 0.07616 to five decimal places.

## Consistency check
The reversed-phase term behaves correctly at the two limits. When the A-B distance shrinks to zero, P(D at B) and the phase difference both equal 1, so the reversed-phase probability is 0. When the distance becomes very large, P(D at B) approaches 2/3 and the phase difference approaches 0, so the reversed-phase probability approaches 1/3. The value 0.089642 lies between these limits.

## Answer
0.07616
