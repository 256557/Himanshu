# Q18: central fusion, mother A b / a B (homolog 0 = A b, homolog 1 = a B).
# A 25 cM from centromere, B 20 cM beyond A (Poisson, no interference).
# Among daughters heterozygous at both loci, fraction that are A B / a b (coupling).
import numpy as np, sys
sys.path.insert(0,'.')
from material_model import run
m2=0.4
PD=2/3+np.exp(-1.5*m2)/3
print('closed',round((PD-np.exp(-m2))/(2*PD),6))
N=4_000_000
A,B=run(N,seg_means=[0.5,0.4])
c1A,c2A,c1B,c2B=A[:,0],A[:,2],B[:,0],B[:,2]      # central fusion: non-sisters 0 and 2
het=(c1A!=c2A)&(c1B!=c2B)
coup=het&(c1A!=c1B)                              # chromatid carrying A (hom 0) carries B (hom 1)
s=coup.sum()/het.sum()
print('sim',round(s,4),'+-',round(2*np.sqrt(s*(1-s)/het.sum()),4))
print('Haldane r (wrong)',round((1-np.exp(-0.4))/2,4))
