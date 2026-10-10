import numpy as np, sys
sys.path.insert(0,'.')
from twolocus import run
from multiprocessing import Pool
def job(s): return run(400000, 2e-5, seed=2000+s)
with Pool(6) as p: o=np.concatenate(p.map(job,range(12)))
np.save('q27_out.npy',o)
n=len(o); c0=o[:,0]==0; c1=o[:,1]==0
def se(m,k): return 2*np.sqrt(m*(1-m)/k)
q2=(c0&c1).mean()
# symmetric Q3: pool both directions
num=((~c0)&c1).sum()+((~c1)&c0).sum(); den=(~c0).sum()+(~c1).sum(); q3=num/den
q4=((o[:,0]!=0)&(o[:,0]==o[:,1])).mean(); q5=(o[:,0]!=o[:,1]).mean()
print('n',n,' marginal',(c0.mean()+c1.mean())/2)
print('Q2',round(q2,4),'+-',round(se(q2,n),4))
print('Q3',round(q3,4),'+-',round(se(q3,den/2),4))
print('Q4',round(q4,5),'+-',round(se(q4,n),5))
print('Q5',round(q5,4),'+-',round(se(q5,n),4))
print('Q3 via exact marginal',round((0.909776-q2)/(1-0.909776),4))
