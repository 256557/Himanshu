# How to make the questions harder

Based on what has worked: Model A passes standard textbook traps, and fails when it must track a hidden state that changes from step to step.

## Core techniques
1. Hidden state: the answer depends on something the question never mentions (Q14: the two chromatids the pollen does not receive).
2. Conditional questions: "given X, what fraction Y". This breaks memorized formulas and independence shortcuts.
3. Chained dependent steps: three loci, or two generations of automixis.
4. Combine two mechanisms: central fusion + recessive lethal; attached-X + X-linked lethal; 2n pollen x normal plant (triploid offspring); automixis + one round of selection.
5. Irrelevant information: give a number that should not be used.
6. Near-miss numbers: choose values where the wrong method lands close to the right one, and ask for 4 decimals.
7. No textbook wording and no method hints.

## More techniques
8. Reverse problems: give the observed frequency and ask for the map distance. The model has to invert the formula instead of plugging numbers into it.
9. Replace the Poisson assumption with an explicit rule, e.g. "every bivalent forms exactly one chiasma, at a uniformly random point on the arm". No ready formula exists, so it must derive from scratch.
10. Sex-specific map lengths, e.g. "female map 30 cM, male map 10 cM", where both parents' meioses matter.
11. Polyploids: autotetraploid segregation with double reduction (a gene far from the centromere). Models often use the wrong gamete ratios.
12. Mixed reproduction: "70% of eggs develop by central fusion, 30% are fertilized by an unrelated male". The model has to weight two pathways.
13. Ask for a quantity other than the usual one: an expected count, a variance, a ratio of two classes, or heterozygosity after two generations.
14. Limit checks: very large distances (the answer should approach a known limit) or zero distance. Wrong methods often give impossible values, such as above 1 or not reaching 2/3.
15. Two-part answers where part 2 needs part 1: "what fraction ... and among those, what fraction ...". One early slip ruins both.
16. Translate the biology: describe the mechanism without naming it, e.g. "the egg fuses with the polar body produced at the first meiotic division" instead of "central fusion". The model must recognise which case it is.

## Writing checklist
- Verify every answer two ways (exact calculation plus simulation). The original bank had 6 wrong answers.
- One reading only: state the crossover model, the interference assumptions and the map-distance convention.
- Under about 80 words, so the model does not time out or skip parts.
- One question per message.
- Vary the organism, mechanism and target class so questions don't look alike.
