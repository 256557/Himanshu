# Probe batch 3: strand pairing (follow-up to B2)

Model A missed B2: it counted the strand types correctly but paired the new strands with each other instead of with their templates. Every question here depends on the same rule: a new strand stays paired with the strand it was copied from.

## Questions (type as written)

C1. A PCR starts with one double-stranded DNA molecule. After 4 cycles, how many double-stranded molecules have exactly the target length?
C2. A PCR starts with a single strand of DNA, not a duplex. After 3 cycles, how many double-stranded molecules have exactly the target length?
C3. E. coli fully labeled with 15N grows for two generations in 14N medium, then one generation back in 15N medium. What fraction of the DNA molecules have hybrid density?
C4. Root-tip cells replicate once in 3H-thymidine, then go through two more replications in unlabeled medium. At the third metaphase, what fraction of chromatids are labeled?
C5. A PCR starts with one double-stranded DNA molecule. After 5 cycles, what fraction of all double-stranded molecules have exactly the target length?

## Answer key (do not show to the model)

| # | Answer | Trap |
|---|---|---|
| C1 | 8 | 2^4 - 2x4 = 8. Pairing all 22 short strands with each other gives 11, and counting 2^4 - 2 gives 14. Duplexes: 8 S/S, 6 H/S, 2 O/H. |
| C2 | 1 | 2^(n-1) - n = 1. Duplexes: 1 S/S, 2 H/S, 1 O/H. Common errors are 2 (the double-stranded formula) or 3. |
| C3 | 3/4 | After 2 generations in 14N: 2 hybrid and 2 light. In 15N, all 8 strands get a new heavy partner: 2 heavy (15/15) and 6 hybrid (14/15). The light class disappears. |
| C4 | 1/4 | Only the original 2 labeled strands remain, spread over 8 chromatids per chromosome lineage. Common error: 1/2. |
| C5 | 11/16 (0.6875) | (32 - 10) / 32. Common errors: 30/32 or 0.75. |

Verified by strand-level simulation: `verify/batch3_strands.py`.

## Model A results (2026-10-10)

All 5 correct: C1 = 8, C2 = 1, C3 = 3/4, C4 = 1/4, C5 = 11/16.
- This time it explicitly paired each new strand with its own template, so the B2 error did not repeat. B2 looks like a one-off slip, not a stable weakness.
- Its working contains self-corrections ("wait, let me redo") and one wrong intermediate formula (T strands = 2^n - 2n - 2), which it fixed later. The final answer section is clean and correct (T strands = 2^(n+1) - 2n - 2; T-T duplexes = 2^n - 2n).
