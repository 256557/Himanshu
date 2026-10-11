# Set 11: X-linked inbreeding

## Question
A woman's parents are first cousins. Give her inbreeding coefficient at an X-linked locus when (a) her father's mother and her mother's mother are sisters, (b) her father's father and her mother's father are brothers, and (c) her father's mother and her mother's father are sister and brother. Assume the grandparents' generation is not inbred.

## Answer
(a) 3/16, (b) 0, (c) 1/8. The autosomal value is 1/16 in all three cases.

## Solution

### Step 1. The paternal X
A daughter's paternal X is her father's only X, which he received from his mother. Every path of identity must therefore pass through the father's mother.

### Step 2. Case (b)
The father's mother is not one of the related siblings, so his X carries no copy from the shared grandparents. The coefficient is 0.

### Step 3. Identity between two sisters' transmitted X chromosomes
Two sisters carry the same paternal X, and their maternal X chromosomes are identical by descent with probability 1/2. Each sister transmits either X with probability 1/2, so the transmitted chromosomes are identical with probability (1/4)(1) + (1/4)(1/2) = 3/8.

### Step 4. Case (a)
The father carries his mother's transmitted X. The woman receives from her mother the X that came from the maternal grandmother with probability 1/2. The coefficient is (1/2)(3/8) = 3/16.

### Step 5. Case (c)
The brother has only his mother's X, and he passes it to his daughter, who passes it on with probability 1/2. The sister passes her maternal X with probability 1/2, and that X is identical to her brother's with probability 1/2. The coefficient is (1/2)(1/2)(1/2) = 1/8.

### Check
Gene dropping with 2 million replicates per case gave 0.1877, 0.0000 and 0.1248 (`verify/set11_xF.py`).

## Likely wrong answers
1/16 for every case, from the autosomal path-counting rule; or the X-linked rule applied without noting that male-to-male links break every path.
