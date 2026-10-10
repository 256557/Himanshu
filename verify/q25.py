# Q25: SDR 2n eggs (sisters 0,1). A 10 cM, B 15 cM beyond A, C 20 cM beyond B.
# Fraction homozygous at A, heterozygous at B, homozygous at C.
import numpy as np, sys
sys.path.insert(0,'.')
from material_model import run
m1,m2,m3=0.2,0.3,0.4
SA=1/3+2/3*np.exp(-1.5*m1); DB=2/3*(1-np.exp(-1.5*m2)); SC=(1-np.exp(-1.5*m3))/3
print('SA',round(SA,6),'D|S',round(DB,6),'S|D',round(SC,6),'closed',round(SA*DB*SC,6))
p=lambda l:(1-np.exp(-2*l))/2
print('parity method (wrong)',round((1-p(m1))*p(m2)*p(m3),6))
N=8_000_000; A,B,C=run(N,seg_means=[m1,m2,m3])
j=((A[:,0]==A[:,1])&(B[:,0]!=B[:,1])&(C[:,0]==C[:,1])).mean()
print('sim',round(j,5),'+-',round(2*np.sqrt(j*(1-j)/N),5))
