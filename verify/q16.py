# Q16: female A B / a b. One arm, EXACTLY ONE chiasma per meiosis, uniform position, random
# non-sister pair. A at 30% of arm, B at 70%. 60% of eggs: egg nucleus fuses with a nucleus
# from the first polar body's division (central fusion: non-sister chromatids).
# 40% of eggs: fertilized by an a b / a b male. Fraction of all offspring that are aa bb.
import numpy as np
rng=np.random.default_rng(16); N=10_000_000; r=np.arange(N)
pos=rng.random(N); i=rng.integers(0,2,N); j=2+rng.integers(0,2,N)
def state_at(x):
    L=np.tile(np.array([0,0,1,1],np.int8),(N,1))      # 0 = A B homolog, 1 = a b homolog
    m=pos<x; li,lj=L[r,i].copy(),L[r,j].copy()
    L[r[m],i[m]]=lj[m]; L[r[m],j[m]]=li[m]; return L
SA,SB=state_at(0.3),state_at(0.7)
parth=rng.random(N)<0.6
# egg chromatid: random one of 4; central fusion partner: a non-sister (other centromere), random
e=rng.integers(0,4,N); p=np.where(e<2,2+rng.integers(0,2,N),rng.integers(0,2,N))
aa_bb_cf=(SA[r,e]==1)&(SA[r,p]==1)&(SB[r,e]==1)&(SB[r,p]==1)
aa_bb_sex=(SA[r,e]==1)&(SB[r,e]==1)                 # sperm always a b
h=np.where(parth,aa_bb_cf,aa_bb_sex).mean()
print('sim',round(h,5),'+-',round(2*np.sqrt(h*(1-h)/N),5))
print('exact', 0.6*0.3*0.25 + 0.4*(1-0.4*0.5)/2, ' terminal-fusion misread', 0.6*0.3*0.5 + 0.16, ' ignores homolog identity', 0.6*0.3*0.5+0.16)
