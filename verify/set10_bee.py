# Honeybee, singly mated queen: relatedness = P(a random gene in the actor is IBD in the recipient).
# Worker = one queen gene + the drone father's genome; brother = one queen gene (haploid).
import numpy as np
rng=np.random.default_rng(10); n=1_000_000
w_q=rng.integers(0,2,n); b=rng.integers(0,2,n)          # which queen copy each got
# worker -> brother: pick a worker gene: maternal (1/2) or paternal (1/2)
pick_maternal=rng.random(n)<0.5
print("worker->brother", np.mean(pick_maternal & (w_q==b)))
# brother -> sister: his only gene; sister's maternal copy matches with 1/2 (paternal copy is the drone father's, not IBD)
print("brother->sister", np.mean(w_q==b))
