# Chain set 4: major-outbreak probabilities in a two-type branching process.
# Column = infector. Child: means 3 (children), 1 (adults). Adult: 0.5 (children), 0.6 (adults).
import numpy as np
from scipy.optimize import fsolve
M=np.array([[3.0,0.5],[1.0,0.6]])
# (a) independent Poisson offspring counts
def gp(q):
    qc,qa=q
    return [np.exp(-M[0,0]*(1-qc)-M[1,0]*(1-qa))-qc, np.exp(-M[0,1]*(1-qc)-M[1,1]*(1-qa))-qa]
qc,qa=fsolve(gp,[0.05,0.3])
print('Poisson: P(major | 1 child) =',round(1-qc,6),' P(major | 1 adult) =',round(1-qa,6),' P(major | 1 child + 1 adult) =',round(1-qc*qa,6))
# (b) exponential infectious period (mean 1): counts are Poisson given the duration, shared across targets
def ge(q):
    qc,qa=q
    return [1/(1+M[0,0]*(1-qc)+M[1,0]*(1-qa))-qc, 1/(1+M[0,1]*(1-qc)+M[1,1]*(1-qa))-qa]
ec,ea=fsolve(ge,[0.2,0.6])
print('Exponential period: P(major | 1 child) =',round(1-ec,6),' P(major | 1 adult) =',round(1-ea,6))
R0=max(abs(np.linalg.eigvals(M))); print('R0',round(R0,6),' 1-1/R0 =',round(1-1/R0,6))
# (c) wrong: exponential period but treating child and adult counts as independent geometrics
def gw(q):
    qc,qa=q
    return [1/(1+M[0,0]*(1-qc))/(1+M[1,0]*(1-qa))-qc, 1/(1+M[0,1]*(1-qc))/(1+M[1,1]*(1-qa))-qa]
wc,wa=fsolve(gw,[0.2,0.6]); print('wrong (independent geometrics): P(major | 1 child) =',round(1-wc,6))
# simulation check
rng=np.random.default_rng(4)
def sim(start, expo, n=200000, cap=2000):
    big=0
    for _ in range(n):
        c,a=start; total=0
        while c+a>0 and total<cap:
            if expo:
                tc=rng.exponential(1,c); ta=rng.exponential(1,a)
                nc=rng.poisson(3*tc).sum()+rng.poisson(0.5*ta).sum(); na=rng.poisson(1*tc).sum()+rng.poisson(0.6*ta).sum()
            else:
                nc=rng.poisson(3*c+0.5*a); na=rng.poisson(1*c+0.6*a)
            c,a=nc,na; total+=c+a
        big+= total>=cap
    return big/n
for lab,st,ex in [('Poisson child',(1,0),False),('Poisson adult',(0,1),False),('Expo child',(1,0),True)]:
    s=sim(st,ex); print('sim',lab,round(s,4),'+-',round(2*np.sqrt(s*(1-s)/200000),4))
