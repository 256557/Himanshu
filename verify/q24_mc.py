import numpy as np
rng=np.random.default_rng(24)
def sim(fem_types,fem_p,male_types,male_p,r,gens,N=3_000_000):
    # haplotype as (a,b) bits: 0 = allele 1, 1 = allele 2
    fi=rng.choice(len(fem_types),N,p=fem_p); F_=np.array(fem_types)[fi]       # N x 2 x 2
    mi=rng.choice(len(male_types),N,p=male_p); M_=np.array(male_types)[mi]    # N x 2
    for _ in range(gens):
        def gam(n):
            mom=F_[rng.integers(0,N,n)]
            k=rng.integers(0,2,n); rec=rng.random(n)<r
            a=mom[np.arange(n),k,0]; b=mom[np.arange(n),np.where(rec,1-k,k),1]
            return np.stack([a,b],1)
        dad=M_[rng.integers(0,N,N)]
        daughters_mat=gam(N); sons=gam(N)
        F_=np.stack([daughters_mat,dad],1); M_=sons
    return F_,M_
def D(h):
    pA=(h[:,0]==0).mean(); pB=(h[:,1]==0).mean(); return ((h[:,0]==0)&(h[:,1]==0)).mean()-pA*pB
h11,h12,h21,h22=[0,0],[0,1],[1,0],[1,1]
F_,M_=sim([[h11,h22],[h12,h21],[h11,h11]],[.5,.25,.25],[h11,h22],[.6,.4],0.2,2)
allX=np.concatenate([F_[:,0],F_[:,1],M_])
print('MC new Q: D all X',round(D(allX),4),' exact 0.1147')
F_,M_=sim([[h11,h22],[h12,h21]],[2/3,1/3],[h11,h22],[.75,.25],0.15,2)
print('MC user Q: D female X',round(D(np.concatenate([F_[:,0],F_[:,1]])),4),' exact',round(581/6400,4))
