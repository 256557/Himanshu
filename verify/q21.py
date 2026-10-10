# Q21: terminal fusion (sisters 0,1). A 10 cM, B 35 cM beyond. Among daughters homozygous at B,
# fraction heterozygous at A.
import numpy as np, sys
sys.path.insert(0,'.')
from material_model import run
m1,m2=0.2,0.7
SA=1/3+2/3*np.exp(-1.5*m1); DA=1-SA
SS=1/3+2/3*np.exp(-1.5*m2); DS=(1-np.exp(-1.5*m2))/3
print('SA',SA,'SS',SS,'DS',DS,'num',DA*DS,'den',SA*SS+DA*DS,'closed',round(DA*DS/(SA*SS+DA*DS),6))
N=6_000_000; A,B=run(N,seg_means=[m1,m2])
hB=B[:,0]==B[:,1]; dA=A[:,0]!=A[:,1]
s=(hB&dA).sum()/hB.sum(); print('sim',round(s,4),'+-',round(2*np.sqrt(s*(1-s)/hB.sum()),4))
