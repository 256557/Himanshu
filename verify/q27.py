import numpy as np, sys
sys.path.insert(0,'.')
from twolocus import run
from multiprocessing import Pool
def job(s): return run(300000, 2e-5, seed=100+s)
with Pool(6) as p: o=np.concatenate(p.map(job,range(6)))
n=len(o); c0=o[:,0]==0; c1=o[:,1]==0
def show(lab,x,base=None):
    x=np.asarray(x); m=x.mean(); print(f'{lab:55s} {m:.4f} +- {2*np.sqrt(m*(1-m)/len(x)):.4f}')
show('Q1 P(locus X concordant)',c0)
show('Q2 P(both concordant)',c0&c1)
d=~c0; show('Q3 P(Y concordant | X discordant)',c1[d])
show('Q4 P(both discordant, same topology)',(o[:,0]!=0)&(o[:,0]==o[:,1]))
show('Q5 P(X and Y have different topologies)',o[:,0]!=o[:,1])
print('limits: unlinked Q2',round(0.9097765**2,4),' fully linked Q2',0.9098,' unlinked Q3',0.9098,' linked Q3 0')
