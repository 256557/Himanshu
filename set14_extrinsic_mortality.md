# Set 14: extrinsic mortality and the evolution of ageing

## Questions
1. A population grows exponentially without density regulation. If an age-independent extrinsic death rate is added, does selection against a deleterious effect expressed late in life become weaker relative to selection on early-life traits?
2. Does the answer change if the population is held stationary by density-dependent reduction of fecundity?

## Answer

### Step 1. Hamilton's gradients
With the Euler-Lotka equation, the sum of e^(-rx) l(x) m(x) over ages equal to 1, the selection gradient on fecundity at age x is proportional to e^(-rx) l(x), and the gradient on log survival from age a is proportional to the sum of e^(-rx) l(x) m(x) over ages after a.

### Step 2. Density-independent growth
An added hazard mu multiplies l(x) by e^(-mu x), and r falls by exactly mu. The product e^(-rx) l(x) is unchanged, so every age-specific gradient keeps the same value and late-acting effects are selected exactly as before. The answer to question 1 is no.

### Step 3. Regulation through fecundity
When density dependence scales fecundity so that the population is stationary, r stays at 0. The factor e^(-mu x) then remains in l(x), and the gradients decline faster with age. Selection against late-acting effects therefore becomes weaker, and the answer to question 2 is yes. In an example life table, the ratio of the fecundity gradient at age 20 to that at age 2 fell from 0.030 to 0.00014 when mu = 0.3 was added, whereas under density-independent growth it did not change (`verify/ap_density.py`).

### Conclusion
Age-independent extrinsic mortality affects the evolution of ageing only through the way the population is regulated; it has no effect under density-independent growth or when regulation acts as an equal hazard at all ages.

## Likely wrong answer
Yes to both, from Williams' verbal argument that high extrinsic mortality always weakens selection at late ages.
