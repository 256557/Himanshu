# Q17: yeast unordered tetrads, genes A-B-C on one arm, A-B 20 cM, B-C 30 cM (Poisson,
# no interference). Among tetrads that are tetratype (T) for A and B, fraction that are NPD for A and C.
import numpy as np, itertools, sys
from scipy.linalg import expm
sys.path.insert(0,'.')
from material_model import run
# exact: 6 states (which 2 strands carry homolog-1 material); one crossover = swap one 0 and one 1
S=[s for s in itertools.product((0,1),repeat=4) if sum(s)==2]; ix={s:k for k,s in enumerate(S)}
T=np.zeros((6,6))
for s in S:
    for i in range(4):
        for j in range(4):
            if s[i]==0 and s[j]==1:
                t=list(s); t[i],t[j]=1,0; T[ix[s],ix[tuple(t)]]+=.25
P=lambda m: expm(m*(T-np.eye(6)))
a=np.eye(6)[ix[(0,0,1,1)]]
A=a; B=a@P(0.4); num=den=0
for sb in S:
    diffAB=sum(x!=y for x,y in zip((0,0,1,1),sb))
    if diffAB!=2: continue                     # tetratype for A-B
    den+=B[ix[sb]]
    C=np.eye(6)[ix[sb]]@P(0.6)
    num+=B[ix[sb]]*C[ix[(1,1,0,0)]]             # NPD for A-C: every strand recombinant
print('exact',round(num/den,6),' closed (1/6)(1-e^-0.9) =',round((1-np.exp(-0.9))/6,6))
N=4_000_000
LA,LB,LC=run(N,seg_means=[0.0,0.4,0.6])
recAB=(LA!=LB).sum(1); recAC=(LA!=LC).sum(1)
t=(recAB==2); s=((recAC==4)&t).sum()/t.sum()
print('sim',round(s,4),'+-',round(2*np.sqrt(s*(1-s)/t.sum()),4))
m=0.6; print('plain B-C NPD formula (wrong answer)',round(1/6-np.exp(-m)/2+np.exp(-1.5*m)/3,4))
