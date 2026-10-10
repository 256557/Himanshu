# Set 8: questions built from Model A's errors on the 10 essay questions

## Q-A (from essay Q3: tetrad probabilities that did not sum to 1)
In a fungus, genes A and B are on the same arm. In each meiosis the interval between them has 0 crossovers with probability 0.50, 1 crossover with probability 0.35, and 2 crossovers with probability 0.15. Each single crossover involves one chromatid of each homolog. When there are two crossovers, the second involves the same two chromatids as the first (a two-strand double) with probability 0.1, the other two chromatids (four-strand) with probability 0.2, and one shared chromatid (three-strand) with probability 0.7. Give (a) the fractions of PD, NPD and T tetrads, (b) the true map distance in cM, and (c) the map distance given by the Perkins formula, (T + 6 NPD)/2. Give exact values.

Answer:
(a) PD = 0.50 + 0.15 x 0.1 = 0.515; T = 0.35 + 0.15 x 0.7 = 0.455; NPD = 0.15 x 0.2 = 0.030 (they sum to 1).
(b) Mean crossovers per meiosis = 0.35 + 2 x 0.15 = 0.65; map distance = 0.65/2 = 0.325 M = 32.5 cM.
(c) Perkins: (0.455 + 6 x 0.030)/2 = 0.3175 = 31.75 cM.
Point: the Perkins formula assumes no chromatid interference. With random chromatid choice (1/4, 1/2, 1/4) it would give exactly 32.5 cM; here negative chromatid interference (too few four-strand doubles) makes it underestimate.
Likely wrong answers: T = 0.5 "fixed"; PD/NPD/T that do not sum to 1; claiming the Perkins value equals the true distance (32.5); recombination frequency 25.75% reported as map distance.

## Q-B (from essay Q10: claiming a single tree can contain incompatible splits)
Consider unrooted, fully resolved (binary) trees on six taxa A, B, C, D, E and F.
(a) How many such trees are there?
(b) How many contain the split AB | CDEF?
(c) How many contain AB | CDEF but not CD | ABEF?
(d) How many contain both AB | CDEF and AC | BDEF?

Answer: (a) 105, (b) 15, (c) 12, (d) 0.
Working: (2n - 5)!! = 7!! = 105. Collapsing A and B into one leaf leaves 5 leaves, giving 15 trees. Also collapsing C and D leaves 4 leaves, giving 3 trees, so 15 - 3 = 12. AB|CDEF and AC|BDEF are incompatible (all four intersections, {A}, {B}, {C}, {DEF}, are non-empty), so no tree contains both.
Likely wrong answers: (d) not 0 (the essay's error); (b) 105/15 = 7 or 3.
Verified by listing all 105 trees (`verify/set8.py`).
