# Chain set 3: two host groups + leaky vaccine (send together, in order)

Setup:
An infection spreads in a fully susceptible population of children and adults. Early on, one infected child causes on average 2.4 new child infections and 0.9 adult infections. One infected adult causes 0.8 child infections and 0.7 adult infections. A vaccine cuts a person's chance of infection by 70%, and vaccinated people who still get infected are only half as infectious as unvaccinated ones. Give answers to four decimal places.

Q1. What is R0 with no vaccination?
Q2. If 80% of children (and no adults) are vaccinated, what is the reproduction number?
Q3. In that case, while cases grow steadily, what fraction of new infections are in vaccinated children?
Q4. What minimum fraction of children must be vaccinated (adults unvaccinated) to stop the outbreak?
Q5. What minimum fraction of everyone, vaccinated equally in both groups, stops the outbreak?

## Answer key (checked numerically, `verify/chain3.py`)
| # | Answer | Working |
|---|---|---|
| Q1 | 2.7510 | Largest eigenvalue of [[2.4, 0.8], [0.9, 0.7]] (columns = infector) |
| Q2 | 1.2152 | Three types: unvaccinated children, vaccinated children, adults. Equivalent 2x2: child susceptibility s = 1 - 0.7p = 0.44, child "infectious mass" a = (1 - p) + p(0.3)(0.5) = 0.32, giving [[2.4a, 0.8s], [0.9a/s ... ]] -> largest eigenvalue 1.2152 |
| Q3 | 0.2402 | Leading eigenvector of the 3-type matrix: shares 0.2002 (unvaccinated children), 0.2402 (vaccinated children), 0.5596 (adults) |
| Q4 | 0.9314 (= 95/102) | Threshold: (1 - 2.4a)(1 - 0.7) - 0.8 x 0.9 x a = 0 gives a = 0.3/1.44, and a = 1 - 0.85p |
| Q5 | 0.7488 | Vaccine cuts transmission per vaccinated person by 1 - 0.3 x 0.5 = 0.85, so p = (1 - 1/R0)/0.85 |

Check values: with 100% of children vaccinated, R = 0.9 exactly.

## Likely wrong answers
- Q2: 1.4683 (uses only the 70% susceptibility cut and ignores reduced infectiousness).
- Q4: "impossible" (with the susceptibility-only shortcut, R stays at 1.1749 even at 100% coverage), or 1 - 1/R0 based answers.
- Q5: 0.6365 (1 - 1/R0, perfect vaccine) or 0.9090 ((1 - 1/R0)/0.7, susceptibility only).
- Q3: answering the share of vaccinated children in the population (0.8 of children) instead of among cases.
