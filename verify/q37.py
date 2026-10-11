# Q37: SDR 2n eggs (sister chromatids), mother Ab/aB, A 15 cM from centromere, B 25 cM beyond. Fraction AB/ab.
import numpy as np
from math import exp
from material_model import run
h=0;n=0
for _ in range(8):
    A,B=run(1_000_000,seg_means=[0.3,0.5])
    h+=((A[:,0]!=A[:,1])&(B[:,0]!=B[:,1])&(A[:,0]!=B[:,0])).sum(); n+=A.shape[0]
ex=(2/3)*(1-exp(-0.45))*((2/3+exp(-0.75)/3)-exp(-0.5))/2
print("sim",h/n,"exact",ex)
