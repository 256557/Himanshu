# Q39: terminal fusion, locus A 40 cM from centromere (m = 0.8). Heterozygosity in daughters and granddaughters.
from math import exp
from material_model import run
h=0;n=0
for _ in range(8):
    (A,)=run(1_000_000,seg_means=[0.8]); h+=(A[:,0]!=A[:,1]).sum(); n+=A.shape[0]
p=(2/3)*(1-exp(-1.2))
print("daughters sim",h/n,"exact",p,"granddaughters",p*p)
q=(1-exp(-0.8))/2; print("wrong: model formula m=0.4",((1-exp(-0.8))/2)**2," parity",(2*q*(1-q))**2)
