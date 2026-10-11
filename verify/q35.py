# Q35: terminal fusion, parent AB/ab, A 20 cM from centromere, B 20 cM beyond A.
# Fraction of daughters Ab/aB (repulsion double heterozygote). Daughter keeps strands 0 and 1 (sisters).
import numpy as np
from material_model import run
from math import exp
pD_A=(2/3)*(1-exp(-0.6))
pD_B=2/3+exp(-0.6)/3; d=exp(-0.4)
exact=pD_A*(pD_B-d)/2
tot=0; hits=0
for _ in range(8):
    A,B=run(1_000_000,seg_means=[0.4,0.4])
    a0,a1,b0,b1=A[:,0],A[:,1],B[:,0],B[:,1]
    hits+=np.sum((a0!=a1)&(b0!=b1)&(a0!=b0)); tot+=len(a0)
p=hits/tot
print(f"exact {exact:.6f}  sim {p:.6f} +- {np.sqrt(p*(1-p)/tot):.6f}")
# Parity method (Model A's usual error): each chromatid flips at a Poisson(x) rate, independently.
# Het at A: exactly one chromatid odd in interval 1. Repulsion at B: both chromatids odd in interval 2.
q=(1-exp(-2*0.2))/2
print("parity method", round(2*q*(1-q)*q*q,6))
