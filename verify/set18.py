# Set 18: ten chromatid-tracking questions, exact formulas checked against the local-material simulation.
import numpy as np
from math import exp
from material_model import run
N=2_000_000
PD_S=lambda m:(2/3)*(1-exp(-1.5*m)); PD_D=lambda m:2/3+exp(-1.5*m)/3
PS_S=lambda m:1/3+(2/3)*exp(-1.5*m); PS_D=lambda m:(1/3)*(1-exp(-1.5*m))
def sim(means,f):
    L=run(N,seg_means=means); return f(L).mean()
res=[]
# 1 central fusion, 35 cM, het after 3 generations
ex=PD_D(0.7)**3; s=sim([0.7],lambda L:L[0][:,0]!=L[0][:,2])**3; res.append((1,ex,s))
# 2 FDR pollen, A 10, B +30, homozygous at both
ex=PS_D(0.2)*PS_S(0.6); s=sim([0.2,0.6],lambda L:(L[0][:,0]==L[0][:,2])&(L[1][:,0]==L[1][:,2])); res.append((2,ex,s))
# 3 SDR eggs, A 15, B +20, het A hom B
ex=PD_S(0.3)*PS_D(0.4); s=sim([0.3,0.4],lambda L:(L[0][:,0]!=L[0][:,1])&(L[1][:,0]==L[1][:,1])); res.append((3,ex,s))
# 4 attached-X, y 50 cM, yellow daughters (homozygous y)
ex=PS_D(1.0)/2; s=sim([1.0],lambda L:(L[0][:,0]==L[0][:,2])&(L[0][:,0]==1)); res.append((4,ex,s))
# 5 Neurospora, gene 30 cM, SDS asci
ex=PD_S(0.6); s=sim([0.6],lambda L:L[0][:,0]!=L[0][:,1]); res.append((5,ex,s))
# 6 tetrads, genes 30 cM apart on same arm near centromere, NPD
ex=1/6-exp(-0.6)/2+exp(-0.9)/3
s=sim([1e-9,0.6],lambda L:(L[0]!=L[1]).all(1)); res.append((6,ex,s))
# 7 central fusion AB/ab, A 20, B +20, ab/ab daughters
ex=PS_D(0.4)/2*(PS_S(0.4)+exp(-0.4))/2
s=sim([0.4,0.4],lambda L:(L[0][:,0]==1)&(L[0][:,2]==1)&(L[1][:,0]==1)&(L[1][:,2]==1)); res.append((7,ex,s))
# 8 terminal fusion Ab/aB, A 20, B +20, AB/AB daughters (A on homolog 0, B on homolog 1)
ex=PS_S(0.4)/2*(PS_S(0.4)-exp(-0.4))/2
s=sim([0.4,0.4],lambda L:(L[0][:,0]==0)&(L[0][:,1]==0)&(L[1][:,0]==1)&(L[1][:,1]==1)); res.append((8,ex,s))
# 9 FDR pollen, A 15, B +25, P(hom B | het A)
L=run(N,seg_means=[0.3,0.5]); hA=L[0][:,0]!=L[0][:,2]
ex=PS_D(0.5); s=(hA&(L[1][:,0]==L[1][:,2])).sum()/hA.sum(); res.append((9,ex,s))
# 10 central fusion, A 25, B +25, het at both
ex=PD_D(0.5)**2; s=sim([0.5,0.5],lambda L:(L[0][:,0]!=L[0][:,2])&(L[1][:,0]!=L[1][:,2])); res.append((10,ex,s))
for q,e,s in res: print(q,round(e,6),round(s,6))
