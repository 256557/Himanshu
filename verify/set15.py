# Set 15 checks.
import numpy as np
rng=np.random.default_rng(15)
# (1) Ne when every individual leaves exactly two gametes (Vk = 0): Ne = (4N-2)/(Vk+2) = 2N-1.
N=25; reps=20000; T=60
genes=np.tile(np.arange(2*N),(reps,1))            # all founder copies distinct
Hs=[]
for t in range(T):
    # each individual i contributes exactly 2 gametes, one random allele copy each (Mendelian)
    idx=np.repeat(np.arange(N),2)                       # parents of the 2N gametes
    pick=rng.integers(0,2,(reps,2*N))
    gam=genes[np.arange(reps)[:,None], 2*idx[None,:]+pick]
    perm=np.argsort(rng.random((reps,2*N)),1)           # random pairing into zygotes
    genes=gam[np.arange(reps)[:,None],perm]
    a,b=genes[:,0::2],genes[:,1::2]
    Hs.append(np.mean(a!=b))                            # prob. two genes in an individual not IBD
H=np.array(Hs); rate=1-np.exp(np.polyfit(np.arange(20,T),np.log(H[20:]),1)[0])
print("Vk=0: per-generation loss",round(rate,5)," Ne =",round(1/(2*rate),1)," 2N-1 =",2*N-1," N =",N)
# (2) Mean fitness can fall under selection: male-limited drive k=0.9 with a recessive lethal.
k=0.9; x=0.01; wbar=[]
for _ in range(200):
    e,s=x/2,k*x; tt=e*s; wbar.append(1-tt); x=(e*(1-s)+s*(1-e))/(1-tt)
print("mean viability: start",round(wbar[0],5)," equilibrium",round(wbar[-1],5))
# (3) Autosomal locus, allele frequency 0.8 in males and 0.2 in females, random mating.
pm,pf=0.8,0.2
g1=(pm*pf, pm*(1-pf)+pf*(1-pm), (1-pm)*(1-pf)); p1=g1[0]+g1[1]/2
print("after 1 generation: AA,Aa,aa =",[round(v,4) for v in g1]," HW would be",[round(p1*p1,4),round(2*p1*(1-p1),4),round((1-p1)**2,4)])
