# Recessive deleterious allele (h = 0), mu = 1e-5 per gamete, s = 0.1 and 0.01.
# (A) random mating equilibrium load; (B) load in first generation of complete selfing;
# (C) equilibrium load under complete selfing (genotype-frequency recursion).
import numpy as np
mu=1e-5
for s in (0.1,0.01):
    q=0.0
    for _ in range(3_000_000):
        q=q+(1-q)*mu; w=1-s*q*q; q=(q*q*(1-s)+q*(1-q))/w
    LA=s*q*q
    # first generation of selfing from HW adults (genotypes before selection, after mutation)
    AA,Aa,aa=(1-q)**2,2*q*(1-q),q*q
    aa1=aa+Aa/4; LB=s*aa1
    # complete selfing equilibrium: track genotype freqs; mutation in gametes, then selfing segregation
    x=np.array([1.0,0.0,0.0])          # AA, Aa, aa adults
    for _ in range(200000):
        AA,Aa,aa=x
        # selfed offspring with mutation A->a in each gamete independently
        def gam(g):  # prob gamete carries a
            return {0:0,1:0.5,2:1}[g]
        new=np.zeros(3)
        for g,f in ((0,AA),(1,Aa),(2,aa)):
            pa=gam(g); pa=pa+(1-pa)*mu
            # two gametes from the same parent are independent draws
            new+=f*np.array([(1-pa)**2,2*pa*(1-pa),pa*pa])
        L=s*new[2]; new[2]*=1-s; x=new/new.sum()
    print(f"s={s}: q_rm={q:.4f}  load random mating={LA:.2e}  first selfed generation={LB:.2e}  selfing equilibrium={L:.2e}")
