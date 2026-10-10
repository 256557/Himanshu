# Q28: SDR 2n eggs (sisters 0,1). A 18 cM, B 22 cM beyond. Fraction homozygous at A, heterozygous at B.
import numpy as np, sys
sys.path.insert(0,'.')
from material_model import run
m1,m2=0.36,0.44
SA=1/3+2/3*np.exp(-1.5*m1); DgS=2/3*(1-np.exp(-1.5*m2))
print('SA',round(SA,6),'D|S',round(DgS,6),'answer',round(SA*DgS,6))
# Model A's earlier wrong method (Q23): independent Poisson(d) per sister, parity; het = 2p(1-p)
p=lambda d:(1-np.exp(-2*d))/2; h=lambda d:2*p(d)*(1-p(d))
print('parity method (wrong)',round((1-h(0.18))*h(0.22),6))
N=8_000_000; A,B=run(N,seg_means=[m1,m2])
j=((A[:,0]==A[:,1])&(B[:,0]!=B[:,1])).mean(); print('sim',round(j,5),'+-',round(2*np.sqrt(j*(1-j)/N),5))
