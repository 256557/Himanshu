# Q19: SDR 2n eggs (sister chromatids 0,1). A 20 cM from centromere, B 30 cM beyond A.
# Among 2n eggs heterozygous at B, fraction homozygous at A.
import numpy as np, sys
sys.path.insert(0,'.')
from material_model import run
a,b=0.4,0.6
SA=1/3+2/3*np.exp(-1.5*a); DA=1-SA
S_to_D=2/3*(1-np.exp(-1.5*b)); D_to_D=2/3+np.exp(-1.5*b)/3
ans=SA*S_to_D/(SA*S_to_D+DA*D_to_D)
print('closed',round(ans,6),' P(S at A)',round(SA,4),'(naive answer ignoring the condition)')
N=4_000_000
A,B=run(N,seg_means=[a,b])
hetB=B[:,0]!=B[:,1]; homA=A[:,0]==A[:,1]
s=(hetB&homA).sum()/hetB.sum()
print('sim',round(s,4),'+-',round(2*np.sqrt(s*(1-s)/hetB.sum()),4))
