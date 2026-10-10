# Q26: central fusion (non-sisters 0,2), mother A B / a b (homolog 0 = A B, homolog 1 = a b).
# A 20 cM, B 20 cM beyond. Fraction of daughters a b / a b.
import numpy as np, itertools, sys
sys.path.insert(0,'.')
from material_model import run
from scipy.linalg import expm
m1,m2=0.4,0.4
S1A=(1-np.exp(-1.5*m1))/6
PS=1/3+2/3*np.exp(-1.5*m2); u=np.exp(-m2)
ans=S1A*(PS+u)/2
print('correct (local-material rule)',round(ans,6),'  S1 at A',round(S1A,6),' P(S1 at B|S1 at A)',round((PS+u)/2,6))
# wrong 1: centromere-paired 6-state chain
S=[s for s in itertools.product((0,1),repeat=4) if sum(s)==2]; ix={s:k for k,s in enumerate(S)}
T=np.zeros((6,6))
for s in S:
    for i in (0,1):
        for k in (2,3):
            t=list(s); t[i],t[k]=t[k],t[i]; T[ix[s],ix[tuple(t)]]+=.25
P=lambda m: expm(m*(T-np.eye(6)))
a=np.eye(6)[ix[(0,0,1,1)]]@P(m1); tot=0
for s in S:
    if not (s[0]==1 and s[2]==1): continue
    b=np.eye(6)[ix[s]]@P(m2); tot+=a[ix[s]]*sum(b[ix[t]] for t in S if t[0]==1 and t[2]==1)
print('wrong: centromere-paired chain',round(tot,6))
# wrong 2: independent parity per chromatid; each chromatid flips with Poisson(m/2) count
q=lambda m:(1-np.exp(-m))/2   # P(odd) for Poisson(m/2)
# chromatid 0 starts hom0 (A B), chromatid 2 starts hom1 (a b); need both carry 'a b' at A and at B
# chromatid0: odd in I, even in II ; chromatid2: even in I, even in II
print('wrong: independent parity',round(q(m1)*(1-q(m2))*(1-q(m1))*(1-q(m2)),6))
print('wrong: loci independent',round(S1A*(1-np.exp(-1.5*(m1+m2)))/6,6))
N=8_000_000; A,B=run(N,seg_means=[m1,m2])
j=((A[:,0]==1)&(A[:,2]==1)&(B[:,0]==1)&(B[:,2]==1)).mean()
print('sim',round(j,5),'+-',round(2*np.sqrt(j*(1-j)/N),5))
