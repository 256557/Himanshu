# Question

A new mutation arises as a single copy in a diploid, randomly mating population of constant size N = 50 (Ne = N). Homozygotes for the mutant allele have relative fitness 1 + s and heterozygotes 1 + hs, with s = -0.02. There is no further mutation or migration.

(a) Can the mutant allele reach fixation? Give its fixation probability for h = 0.5, to three significant figures.
(b) How does this probability change when Ne rises from 50 to 100, and when Ne = 100 but the census size is N = 1000?
(c) Give the fixation probability for h = 0 and for h = 1, and explain why dominance changes it.

# Answer

(a) Yes. With h = 0.5, u = (1 - e^(-2 Ne s p))/(1 - e^(-2 Ne s)) with p = 1/(2N), which gives 3.16 x 10^-3, against 1.00 x 10^-2 for a neutral allele.
(b) At Ne = N = 100 the value falls to 3.77 x 10^-4; it declines roughly as e^(-2 Ne |s|) once 2 Ne |s| exceeds 1. With Ne = 100 and N = 1000 the starting frequency is 1/2000, and u = 3.74 x 10^-5.
(c) For h = 0, u = 4.23 x 10^-3; for h = 1, u = 2.31 x 10^-3. A rare allele occurs almost only in heterozygotes, so a recessive deleterious allele is nearly invisible to selection while rare and drifts almost neutrally, whereas a dominant one is selected against from the first generation.

Diffusion values from Kimura's integral; Wright-Fisher simulation (4M runs per h) gave 4.24, 3.16 and 2.26 x 10^-3 (`verify/q11_drift_selection.py`).
