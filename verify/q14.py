# Q14: FDR 2n pollen (non-sister chromatids: one from each homolog at the centromere).
# A at 15 cM, B 25 cM beyond. Among 2n pollen homozygous at A, fraction also homozygous at B.
import numpy as np
a,b=2*0.15,2*0.25            # crossover means per interval (2x Morgans)
closed=(2+3*np.exp(-b/2)+np.exp(-1.5*b))/6
old3=1/3+2*np.exp(-1.5*b)/3  # sister-type chain (wrong here)
print('closed',round(closed,6),'old 3-state',round(old3,6))
rng=np.random.default_rng(5); N=1000000
lab=np.tile([0,0,1,1],(N,1)); r=np.arange(N); res=[]
for m_ in (a,b):
    k=rng.poisson(m_,N)
    for c in range(k.max()):
        m=k>c; i=rng.integers(0,2,N); j=2+rng.integers(0,2,N)
        li,lj=lab[r,i].copy(),lab[r,j].copy()
        lab[r[m],i[m]]=lj[m]; lab[r[m],j[m]]=li[m]
    res.append(lab[:,0]==lab[:,2])
homA=res[0]; s=(res[0]&res[1]).sum()/homA.sum()
print('sim',round(s,4),'+-',round(2*np.sqrt(s*(1-s)/homA.sum()),4),'P(hom A)',round(homA.mean(),5),'exact',round((1-np.exp(-1.5*a))/3,5))
