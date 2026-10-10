# Chain set 2: disease spread with two host groups (send together, in order)

Setup:
A new infection spreads in a fully susceptible population of children and adults. Early in the outbreak, one infected child causes on average 3 new infections in children and 1 in adults. One infected adult causes on average 0.5 new infections in children and 0.6 in adults. A vaccine gives complete protection, and vaccinated people cannot be infected. Give each answer to four decimal places unless stated.

Q1. What is the basic reproduction number R0?
Q2. Early in the outbreak, while cases grow steadily, what fraction of new infections are in children?
Q3. If only children are vaccinated, what minimum fraction of children must be vaccinated to prevent an outbreak?
Q4. What is the expected number of child infections caused, directly or through chains of adults, by one infected child? (This is the type-reproduction number for children.)
Q5. If instead the same fraction of everyone is vaccinated, what minimum fraction is needed?

## Answer key (checked numerically, `verify/chain2.py`)
| # | Answer | Working |
|---|---|---|
| Q1 | 3.1928 | Largest eigenvalue of K = [[3, 0.5], [1, 0.6]] (columns = infector): (3.6 + sqrt(7.76))/2 |
| Q2 | 0.7217 | Leading eigenvector: v_adult = 2(R0 - 3) v_child = 0.3857 v_child, so 1/1.3857 |
| Q3 | 0.7647 | Vaccinating fraction p of children scales the child row by (1 - p): need (1 - 3s)(0.4) - 0.5s = 0 with s = 1 - p, so s = 0.4/1.7 |
| Q4 | 4.25 | T = 3 + (0.5 x 1)/(1 - 0.6) |
| Q5 | 0.6868 | 1 - 1/R0 |

## Consistency checks
- Q3 must equal 1 - 1/Q4 = 1 - 1/4.25 = 0.7647. If not, the model used two different ideas.
- Q3 is larger than Q5 here. Using 1 - 1/R0 for children-only vaccination (0.6868) is a common error: it ignores the adult-to-adult chains.

## Likely wrong answers
- Q1: 4 (column sum for children), 2.05 (average of column sums), 1.34 (sqrt(3 x 0.6)), or using rows as infectors.
- Q2: 3/4.5 = 0.6667 (share of all secondary infections from all sources), 0.75 (children's share of the child-infector column).
- Q3: 0.6868 (1 - 1/R0), or 0.6667 (1 - 1/3, children only, ignoring adults).
- Q4: 3 (direct only) or 3.5.
