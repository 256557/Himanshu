# Q35/Q36 pair: AB/ab mother, A 20 cM from centromere, B 20 cM beyond A. Fraction of daughters Ab/aB.
# Terminal fusion keeps sister strands (0,1); central fusion keeps non-sister strands (0,2).
import numpy as np
from math import exp
from material_model import run
tot=0; tf=0; cf=0
for _ in range(8):
    A,B=run(1_000_000,seg_means=[0.4,0.4])
    for keep,acc in (((0,1),'t'),((0,2),'c')):
        i,j=keep
        rep=(A[:,i]!=A[:,j])&(B[:,i]!=B[:,j])&(A[:,i]!=B[:,i])
        if acc=='t': tf+=rep.sum()
        else: cf+=rep.sum()
    tot+=A.shape[0]
P=2/3+exp(-0.6)/3; d=exp(-0.4); rev=(P-d)/2
print("terminal: sim",tf/tot," exact",(2/3)*(1-exp(-0.6))*rev)
print("central : sim",cf/tot," exact",P*rev)
# parity method for central fusion: each strand flips by Poisson(0.2) per interval, independent
q=(1-exp(-0.4))/2
print("parity central:",(q*q+(1-q)**2)*q*q)
