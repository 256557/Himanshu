# Q22: FDR 2n pollen (non-sister pair 0,2). A 15 cM, B 25 cM beyond.
# Among 2n pollen homozygous at B, fraction heterozygous at A.
import numpy as np, sys
sys.path.insert(0,'.')
from material_model import run
m1,m2=0.3,0.5
DA=2/3+np.exp(-1.5*m1)/3; SA=1-DA
DS=(1-np.exp(-1.5*m2))/3; SS=1/3+2/3*np.exp(-1.5*m2)
num=DA*DS; den=num+SA*SS
print('DA',DA,'SA',SA,'DS',DS,'SS',SS,'num',num,'SAxSS',SA*SS,'den',den,'closed',round(num/den,6))
N=6_000_000; A,B=run(N,seg_means=[m1,m2])
hB=B[:,0]==B[:,2]; dA=A[:,0]!=A[:,2]
s=(hB&dA).sum()/hB.sum(); print('sim',round(s,4),'+-',round(2*np.sqrt(s*(1-s)/hB.sum()),4))
p=lambda l:(1-np.exp(-2*l))/2
print('parity method (wrong)',round((1-p(m1))*p(m2)/p(m1+m2),4))
