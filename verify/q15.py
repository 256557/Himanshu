# Q15: central fusion; every arm has EXACTLY TWO chiasmata, each at an independent uniform
# position along the arm; each chiasma involves a random non-sister pair (no chromatid
# interference). A at 30% of the arm length, B at 70%. Fraction of daughters homozygous at both.
import numpy as np, itertools
from fractions import Fraction as F
from math import factorial
states=[s for s in itertools.product((0,1),repeat=4) if sum(s)==2]
idx={s:k for k,s in enumerate(states)}
T=[[F(0)]*6 for _ in range(6)]
for s in states:
    for i in (0,1):
        for j in (2,3):
            t=list(s); t[i],t[j]=t[j],t[i]; T[idx[s]][idx[tuple(t)]]+=F(1,4)
def mpow(k):
    R=[[F(int(i==j)) for j in range(6)] for i in range(6)]
    for _ in range(k): R=[[sum(R[i][l]*T[l][j] for l in range(6)) for j in range(6)] for i in range(6)]
    return R
pA,pAB=F(3,10),F(4,10); pR=1-pA-pAB
start=idx[(0,0,1,1)]; hom=lambda s:s[0]==s[2]   # daughter keeps strands 0 and 2 (non-sisters)
tot=F(0)
for k1 in range(3):
    for k2 in range(3-k1):
        k3=2-k1-k2
        w=F(factorial(2),factorial(k1)*factorial(k2)*factorial(k3))*pA**k1*pAB**k2*pR**k3
        M1,M2=mpow(k1),mpow(k2)
        tot+=w*sum(M1[start][idx[s]]*M2[idx[s]][idx[t]] for s in states if hom(s) for t in states if hom(t))
print('exact',tot,float(tot))
rng=np.random.default_rng(99); hits=0; n=0
for chunk in range(10):
    N=2_000_000; r=np.arange(N)
    pos=np.sort(rng.random((N,2)),1); I=rng.integers(0,2,(N,2)); J=2+rng.integers(0,2,(N,2))
    def state_at(x):
        L=np.tile(np.array([0,0,1,1],np.int8),(N,1))
        for c in range(2):
            m=pos[:,c]<x; i,j=I[:,c],J[:,c]
            li,lj=L[r,i].copy(),L[r,j].copy()
            L[r[m],i[m]]=lj[m]; L[r[m],j[m]]=li[m]
        return L
    SA,SB=state_at(0.3),state_at(0.7)
    hits+=((SA[:,0]==SA[:,2])&(SB[:,0]==SB[:,2])).sum(); n+=N
h=hits/n; print('sim 20M',round(h,5),'+-',round(2*np.sqrt(h*(1-h)/n),5))
a,b=0.6,0.8   # arm = 100 cM if treated as Poisson: A at 30 cM, B 40 cM beyond
print('Poisson-model (wrong here)',round((1-np.exp(-1.5*a))*(2+3*np.exp(-b/2)+np.exp(-1.5*b))/18,4))
