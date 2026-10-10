# Q23: terminal fusion (sisters 0,1). A 12 cM, B 18 cM beyond. Fraction het at A, hom at B.
import numpy as np, sys
sys.path.insert(0,'.')
from material_model import run
m1,m2=0.24,0.36
DA=2/3*(1-np.exp(-1.5*m1)); SgD=(1-np.exp(-1.5*m2))/3
print('DA',round(DA,6),'S|D',round(SgD,6),'closed',round(DA*SgD,6))
p=lambda l:(1-np.exp(-2*l))/2
print('parity method (wrong)',round(p(m1)*p(m2),6))
N=8_000_000; A,B=run(N,seg_means=[m1,m2])
j=((A[:,0]!=A[:,1])&(B[:,0]==B[:,1])).mean(); print('sim',round(j,5),'+-',round(2*np.sqrt(j*(1-j)/N),5))
