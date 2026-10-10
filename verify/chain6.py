# Chain set 6: three-species coalescent (species tree ((A,B),C)).
import numpy as np
g=20; t1=1.0e6/g; t2=3.0e6/g; t=t2-t1          # generations: A-B split, root split, internal branch
NAB,NR,mu=25000,40000,1e-8
T=t/(2*NAB)
q1=1-2/3*np.exp(-T); q2=np.exp(-T)/3
TX=t/(1.5*NAB); q3=1-2/3*np.exp(-TX)
Tmt=t/(NAB/2); q4=1-2/3*np.exp(-Tmt)          # mtDNA: coalescence rate 1/N_females, N_f = N/2
ETab=t1+2*NAB*(1-np.exp(-T))+np.exp(-T)*2*NR
q5=2*mu*ETab
# conditional on concordant topology
EXlt=2*NAB-t*np.exp(-T)/(1-np.exp(-T))       # E[X | X < t], X ~ Exp(mean 2N)
num=(1-np.exp(-T))*(t1+EXlt)+(np.exp(-T)/3)*(t1+t+2*NR/3)
q6=num/q1
print(f'T={T} TX={TX:.4f} Tmt={Tmt}')
for k,v in zip(['Q1','Q2','Q3','Q4','Q5','Q6'],[q1,q2,q3,q4,q5,q6]): print(k,v)
print('traps: Q5 using t1+2N_AB:',2*mu*(t1+2*NAB),' Q5 using t1 only:',2*mu*t1,' Q6 unconditional E[T_AB]:',ETab)
# simulation (generations, continuous-time coalescent)
rng=np.random.default_rng(6); n=1_000_000
x=rng.exponential(2*NAB,n)                       # A-B coalescence in AB ancestor (after t1)
inAB=x<t
# lineages entering root: if coalesced, 2 lineages (AB, C); else 3 (A, B, C)
first=rng.exponential(2*NR/3,n); pick=rng.integers(0,3,n)   # pick 0 = AB pair first
conc=inAB|(pick==0)
tab=np.where(inAB,t1+x,np.where(pick==0,t2+first,t2+first+rng.exponential(2*NR,n)))
bc=(~inAB)&(pick==1)
print('sim Q1',conc.mean(),' Q2',bc.mean(),' Q5',2*mu*tab.mean(),' Q6',tab[conc].mean())
