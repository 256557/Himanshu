import numpy as np, itertools
from scipy.linalg import expm
# Terminal fusion: egg + second polar body = sister chromatids (strands 0,1).
# Parent Ab/aB: homolog 0 carries A b, homolog 1 carries a B. Target AABB:
# homolog-0 material on both at A, homolog-1 material on both at B.
states=[s for s in itertools.product((0,1),repeat=4) if sum(s)==2]
idx={s:k for k,s in enumerate(states)}
T=np.zeros((6,6))
for s in states:
    for i in (0,1):
        for j in (2,3):
            t=list(s); t[i],t[j]=t[j],t[i]; T[idx[s],idx[tuple(t)]]+=.25
P=lambda x: expm(2*x*(T-np.eye(6)))
x1,x2=0.2,0.3
tot=0
for start in [(0,0,1,1),(1,1,0,0)]:          # which homolog the sisters carry: 1/2 each
    a=np.eye(6)[idx[start]]@P(x1)
    for s in states:
        if (s[0],s[1])!=(0,0): continue
        b=np.eye(6)[idx[s]]@P(x2)
        tot+=0.5*a[idx[s]]*sum(b[idx[t]] for t in states if (t[0],t[1])==(1,1))
print("exact",round(tot,6))
# closed form via sister 3-state chain
m1,m2=2*x1,2*x2
pS0=0.5*(1/3+2*np.exp(-1.5*m1)/3)              # S0 at A, averaged over start
pswitch=(1/3+2*np.exp(-1.5*m2)/3-np.exp(-m2))/2 # S0 at A -> S1 at B
print("closed",round(pS0*pswitch,6))
rng=np.random.default_rng(7);N=400000;hit=0
for _ in range(N):
    lab=np.array([0,0,1,1]) if rng.random()<.5 else np.array([1,1,0,0]); g=[]
    for x in (x1,x2):
        for _ in range(rng.poisson(2*x)):
            i=rng.integers(0,2); j=2+rng.integers(0,2); lab[i],lab[j]=lab[j],lab[i]
        g.append((lab[0],lab[1]))
    hit+= g[0]==(0,0) and g[1]==(1,1)
s=hit/N; print("sim",round(s,4),"+-",round(2*np.sqrt(s*(1-s)/N),4))
