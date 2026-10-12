# Q38: AB/ab mother, A 20 cM, B +20 cM. 70% of eggs central fusion (strands 0,2), 30% terminal (0,1).
import numpy as np
from math import exp
from material_model import run
rng=np.random.default_rng(38); hit=0; hetA=0; n=0
for _ in range(8):
    A,B=run(1_000_000,seg_means=[0.4,0.4]); N=A.shape[0]
    j=np.where(rng.random(N)<0.7,2,1)
    r=np.arange(N); a0,a1,b0,b1=A[:,0],A[r,j],B[:,0],B[r,j]
    hit+=((a0!=a1)&(b0!=b1)&(a0!=b0)).sum(); hetA+=(a0!=a1).sum(); n+=N
P=2/3+exp(-0.6)/3; T=(2/3)*(1-exp(-0.6)); rev=(P-exp(-0.4))/2
pa=0.7*P+0.3*T
print("a sim",hit/n,"exact",0.7*P*rev+0.3*T*rev)
print("het A daughters sim",hetA/n,"exact",pa," granddaughters",pa**2)
