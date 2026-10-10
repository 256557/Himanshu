# Chained set: SDR 2n eggs (sister pair 0,1). A 15 cM, B 20 cM beyond A, C 25 cM beyond B.
import numpy as np, sys
sys.path.insert(0,'.')
from material_model import run
m1,m2,m3=0.3,0.4,0.5
E=lambda m: np.exp(-1.5*m)
S_from_S=lambda m:1/3+2/3*E(m); D_from_S=lambda m:2/3*(1-E(m))
S_from_D=lambda m:(1-E(m))/3;   D_from_D=lambda m:2/3+E(m)/3
q1=S_from_S(m1)
q2=S_from_S(m1+m2)
q3=q1*S_from_S(m2)
q4=q3/q2
q5=D_from_S(m1)*S_from_D(m2)*D_from_S(m3)
for k,v in zip(['Q1 hom A','Q2 hom B','Q3 hom A & hom B','Q4 hom A | hom B','Q5 het A, hom B, het C'],[q1,q2,q3,q4,q5]):
    print(f'{k:24s} {v:.6f}')
N=8_000_000; A,B,C=run(N,seg_means=[m1,m2,m3])
hA=A[:,0]==A[:,1]; hB=B[:,0]==B[:,1]; hC=C[:,0]==C[:,1]
sims=[hA.mean(),hB.mean(),(hA&hB).mean(),(hA&hB).sum()/hB.sum(),(~hA&hB&~hC).mean()]
print('sim:',[round(x,4) for x in sims])
p=lambda m:(1-np.exp(-m))/2   # P(odd) per chromatid stream with mean m/2... parity method values
