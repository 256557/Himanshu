# Grading: five-question set (drive numerical plus four essays), Model A

## Overall fields
Readable: Yes. The final answer section is clear and headed, although the response repeats a draft with "Wait, let me redo" before it.
Accurate: No. Q1 is numerically wrong (0.4 instead of 1/3), and Q3, Q4 and Q5 contain factual errors.
Complete: No. Q3 never separates intergenerational from transgenerational inheritance, and Q4 omits the PABPC1 and miR-128 mechanisms.

## Q1 (wrong: 0.4; correct 1/3 = 0.3333)
The model averaged the egg and sperm frequencies and then formed zygotes from that single pool, so it took the frequency of homozygous lethals as the square of the mean. Drive in one sex makes the two pools differ (eggs x/2, sperm 0.9x, where x is the adult heterozygote frequency), so the lethal class is their product, 0.45x^2. It also reused adult genotype frequencies p/(1 + q) and 2q/(1 + q), which hold only when zygotes are in Hardy-Weinberg proportions with one allele frequency. The correct equilibrium solves x^2 - 2x + 8/9 = 0, giving x = 2/3 and an adult allele frequency of 1/3. Iterating the exact two-pool recursion gives 0.333333 (`verify/q30.py`).

## Q2 (correct, minor omission)
The mechanisms (tRNA abundance, co-translational folding, mRNA structure, error rates) and the condition Ne|s| >> 1 are correct. It omits exonic splicing enhancers, the main synonymous-site fitness effect in mammals, and the dependence of s on expression level.

## Q3 (errors)
1. The Avy and Axin-Fu marks are not carried through the germline. Their methylation is erased in the early embryo and re-established, yet the phenotype is still inherited (Blewitt et al. 2006). Most variably methylated IAPs are likewise reset each generation (Kazachenka et al. 2018).
2. piRNA-guided de novo methylation by MIWI2 and DNMT3A/3C occurs in fetal male germ cells, not in the zygote. Sperm small RNAs alter early embryonic gene expression; re-methylation of the source locus has not been shown.
3. In mouse sperm about 1% of histones remain, not 5-10%; the higher value applies to humans. The claim that retained marks "influence early transcription before the embryonic genome activates" is self-contradictory.
4. It never separates intergenerational effects (F1, F2 exposed as germ cells) from transgenerational inheritance (F3 onward), which the question asks about.

## Q4 (errors and omissions)
1. Alternative polyadenylation that shortens the 3' UTR does not remove exon junctions downstream of the PTC, because the EJC positions are set by splicing. The relevant effect is that a nearby PABPC1 antagonises UPF1, which the response never names.
2. PTBP1 does not block EJC deposition; it binds long 3' UTRs and prevents UPF1 from acting on them.
3. It misses miR-128, which represses UPF1 in neurons and is the standard example of tissue-regulated NMD, and tissue-specific stop-codon readthrough.

## Q5 (mostly correct, one wrong number)
DNMT1 maintenance errors occur at about 10^-3 to 10^-2 per CpG per division, not 1 per 10^5. Self-templating complexes at super-enhancers are speculative and should not be stated as established. It also omits drug-tolerant persister cells (KDM5A-dependent, Sharma et al. 2010), the clearest direct evidence for the question.

## Paste-ready comment
Q1 is wrong. Male-only drive gives eggs and sperm different allele frequencies (x/2 and 0.9x), so the lethal class is their product, not the square of their mean; the correct adult frequency is 1/3, not 0.4. Q3 states that Avy methylation passes through PGC erasure, but it is erased and rebuilt, and it places piRNA-directed methylation in the zygote rather than in fetal germ cells. Q4 explains 3' UTR shortening as removal of downstream EJCs, which splicing, not polyadenylation, determines, and it omits PABPC1 proximity and miR-128. Q5 gives a DNMT1 error rate about 100-fold too low.
