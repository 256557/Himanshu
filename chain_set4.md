# Chain set 4: chance of a major outbreak (two host groups, branching process)

Paste the whole block, setup included:

An infection enters a large, fully susceptible population of children and adults. Each infected child infects on average 3 children and 1 adult; each infected adult infects on average 0.5 children and 0.6 adults. Different infected people act independently. Give answers to four decimal places.
Part 1: assume each infected person's numbers of child and adult infections are independent Poisson counts.
Q1. What is the probability that one infected child starts a major outbreak (does not die out)?
Q2. What is the probability that one infected adult starts a major outbreak?
Q3. What is the probability that one infected child plus one infected adult, introduced together, start a major outbreak?
Part 2: now assume instead that each infected person is infectious for an exponentially distributed time (mean 1), and infects children and adults at constant rates during that time (giving the same averages as above).
Q4. What is the probability that one infected child starts a major outbreak?
Q5. What is the probability that one infected adult starts a major outbreak?

## Answer key (verified: fixed-point solution plus branching-process simulation, `verify/chain4.py`)
| # | Answer | Working |
|---|---|---|
| Q1 | 0.9688 | Extinction probabilities solve qc = exp(-3(1-qc) - 1(1-qa)), qa = exp(-0.5(1-qc) - 0.6(1-qa)): qc = 0.031245, qa = 0.440361. Answer 1 - qc. |
| Q2 | 0.5596 | 1 - qa |
| Q3 | 0.9862 | 1 - qc x qa (independent lineages) |
| Q4 | 0.7152 | With an exponential period T, counts are Poisson given T, so they are correlated. Generating function E[exp(-T(...))] = 1/(1 + ...): qc = 1/(1 + 3(1-qc) + (1-qa)), qa = 1/(1 + 0.5(1-qc) + 0.6(1-qa)): qc = 0.284765, qa = 0.634037. Answer 1 - qc. |
| Q5 | 0.3660 | 1 - qa |

Simulation (200,000 introductions each): Q1 0.9685, Q2 0.5612, Q4 0.7142.

## Likely wrong answers
- Any question: 1 - 1/R0 = 0.6868. That shortcut ignores which group starts the outbreak and the offspring distribution.
- Q3: 1 - (1 - Q1)(1 - Q2) is correct here, but adding probabilities (Q1 + Q2) is wrong.
- Q4: 0.7933, from treating the child and adult counts as independent geometric variables. In Part 2 they are positively correlated, because both depend on the same infectious period.
- Q4 vs Q1: a model that ignores the change in distribution will repeat 0.9688. R0 is the same in both parts, but the outbreak probability is not.
