import numpy as np
rng=np.random.default_rng(3); r=0.1; N=400000
# F1/F2: full sibs, two loci r=0.1. Per parent: does each sib get the same grandparental copy at L1, L2?
def parent_share(n):
    a1=rng.integers(0,2,(n,2)); flip=rng.random((n,2))<r
    a2=a1^flip
    return a1[:,0]==a1[:,1], a2[:,0]==a2[:,1]
p1,p2=parent_share(N); m1,m2=parent_share(N)
print('F1 IBD2 at both loci', np.mean(p1&p2&m1&m2), 'formula', (0.5*(r**2+(1-r)**2))**2)
print('F2 share >=1 IBD at both', np.mean((p1|m1)&(p2|m2)))
# F3: RIL by selfing from AB/ab F1, many generations; fraction recombinant (Ab or aB lines)
def ril(selfing, gens=25, n=100000):
    # individuals: two haplotypes, each (A?,B?) as 0/1 parental origin; start AB/ab
    h=np.zeros((n,2,2),int); h[:,1,:]=1
    for _ in range(gens):
        def gamete(h):
            pick=rng.integers(0,2,n); rec=rng.random(n)<r
            g1=h[np.arange(n),pick,0]; g2=h[np.arange(n),np.where(rec,1-pick,pick),1]
            return np.stack([g1,g2],1)
        if selfing: h=np.stack([gamete(h),gamete(h)],1)
        else:
            # sib mating within lines: keep two sibs per line
            raise
    return np.mean(h[:,0,0]!=h[:,0,1])
print('F3 RIL selfing recombinant', ril(True), 'formula', 2*r/(1+2*r))
# F4 sib-mating RIL
def ril_sib(gens=40,n=60000):
    H=np.zeros((n,2,2,2),int); H[:,:,1,:]=1   # two sibs, both AB/ab
    idx=np.arange(n)
    def gam(h):
        pick=rng.integers(0,2,n); rec=rng.random(n)<r
        return np.stack([h[idx,pick,0],h[idx,np.where(rec,1-pick,pick),1]],1)
    for _ in range(gens):
        kids=[np.stack([gam(H[:,0]),gam(H[:,1])],1) for _ in range(2)]
        H=np.stack(kids,1)
    return np.mean(H[:,0,0,0]!=H[:,0,0,1])
print('F4 RIL sib recombinant', ril_sib(), 'formula', 4*r/(1+6*r))
print('F5 E[TMRCA] n=3, N=1000 diploid', 4*1000*(1-1/3))
