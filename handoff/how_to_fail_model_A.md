# How to make Model A fail: notes for the next chat

## 1. Record so far
- Chromatid tracking (automixis, restitution, attached-X): 17 failures in 19 attempts. This is the most reliable weakness.
- X-linked isolated-case priors: failed Q41 and Q42, passed Q43, Q44 and Q45. Now usually solved.
- Sex-specific meiotic drive with a recessive lethal: failed only when hidden among essay questions; solved when asked alone.
- Standard formula questions (Kimura fixation, mutation load, tetrads, Haldane-Muller): solved.
- Broad essay questions: fails when one subtle exception is buried in a general question, such as the effect of extrinsic mortality on ageing or the "necessary and sufficient" condition for Hardy-Weinberg.

## 2. Errors Model A makes repeatedly
1. Parity method: treats the two retained chromatids as independent and sets each allele by an odd or even count of crossovers.
2. Treats map distance as a recombination fraction and applies Haldane's function, so the crossover mean is wrong.
3. Labels chromatids at the centromere and adds crossover parities over fixed pairs.
4. Pools male and female X chromosomes into one allele frequency (carrier frequency 6u instead of 4u for a lethal).
5. Uses single-pool formulas (q' = q/(1 + q)) when eggs and sperm carry different allele frequencies.
6. States textbook claims as general rules without the conditions they need.

## 3. Twists that make a question harder
1. Ask for a genotype with phase (Ab/aB from an AB/ab parent), not only heterozygosity.
2. Ask for a specific homozygote (ab/ab or AB/AB), which needs both the homozygous state and the phase.
3. Mix two modes of diploid restoration in fixed proportions, and ask about two generations.
4. Use unequal interval lengths and a locus far from the centromere, so the parity method gives a value far from the correct one.
5. Change the reproductive system: first- or second-division restitution, attached-X, ordered asci.
6. For population-genetic priors, combine an unusual mutation bias with reduced fitness and information on an earlier generation.
7. Put the trap inside a broad conceptual question rather than asking about it directly.
8. Give four or five decimal places so that near misses still count as wrong.

## 4. Ready questions that have not yet been sent
- `set18_ten.md`: Q1 to Q5 and Q7 to Q10 (Q6 was solved). Q7 (0.0515), Q8 (0.00505) and Q2 (0.0522) are the strongest.
- `q39_terminal_two_gen.md`: terminal fusion, two generations, answer 0.2170 (parity gives 0.1592).
- `set20_xlinked_seven.md`: seven X-linked variants, now likely to be solved.

## 5. Questions Model A has already failed (can be reused in a new submission)
| Question | Correct | Model A gave |
|---|---|---|
| Q35 terminal fusion, Ab/aB daughters | 0.0270 | 0.0025 |
| Q36 central fusion, Ab/aB daughters | 0.07616 | 0.06883 |
| Q37 SDR eggs, AB/ab from Ab/aB | 0.02628 | 0.00873 |
| Q38 mixed fusion, granddaughters heterozygous | 0.4692 | 0.4706 |
| Q41 isolated DMD case | 0.0833 | 0.1071 |
| Q42 male-biased mutation | 0.1833 | 0.1875 |

## 6. Rules to keep
- Verify every answer by calculation or simulation before using it (scripts in `verify/`).
- State the crossover rule in each chromatid question: "each crossover joins a chromatid of one homolog with a chromatid of the other".
- Write all questions and solutions in plain scientific prose, with no hints toward the method.
