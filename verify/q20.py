# Q20: attached-X (non-sister pair 0,2). Arm 1 carries p d, arm 2 carries + +.
# p at 15 cM from centromere, d 25 cM beyond. Among daughters homozygous d/d, fraction also p/p.
import numpy as np, sys
sys.path.insert(0,'.')
from material_model import run
m1,m2=0.3,0.5
joint=(1-np.exp(-1.5*m1))/6*((1/3+2/3*np.exp(-1.5*m2))+np.exp(-m2))/2
pB=(1-np.exp(-1.5*(m1+m2)))/6
print('closed',round(joint/pB,6),'joint',round(joint,6),'P(dd)',round(pB,6))
N=8_000_000; A,B=run(N,seg_means=[m1,m2])
dd=(B[:,0]==0)&(B[:,2]==0); pp=(A[:,0]==0)&(A[:,2]==0)
s=(dd&pp).sum()/dd.sum(); print('sim',round(s,4),'+-',round(2*np.sqrt(s*(1-s)/dd.sum()),4))
