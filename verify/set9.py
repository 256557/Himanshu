# Set 9. Q1: recessive lethal, N = 20 adults, one new copy. Adults are only AA or Aa, so the
# adult allele frequency is at most 1/2 and fixation is impossible; loss is certain.
# Q2: drive in both sexes, kf = 0.6 (eggs), km = 0.9 (sperm), tt lethal.
import numpy as np, math
rng=np.random.default_rng(9)
N=20; reps=200000; maxq=0; lost=0
for _ in range(reps):
    het=1
    while het>0:
        q=het/(2*N)
        # zygotes from random union of gametes of surviving adults; aa die; resample N adults
        z=rng.multinomial(10*N,[(1-q)**2,2*q*(1-q),q*q])
        surv=z[0]+z[1]
        het=rng.hypergeometric(z[1],z[0],N) if surv>=N else z[1]
        maxq=max(maxq,het/(2*N))
    lost+=1
print("Q1: lost",lost,"of",reps,"; highest adult frequency seen",maxq)
kf,km=0.6,0.9; x=0.01
for _ in range(20000):
    e,s=kf*x,km*x; tt=e*s; x=(e*(1-s)+s*(1-e))/(1-tt)
xc=1-math.sqrt(1-(kf+km-1)/(kf*km))
print("Q2: het",round(x,6),"allele",round(x/2,6),"closed",round(xc/2,6))
k=(kf+km)/2; print("trap averaged-k symmetric:",(2*k-1)/(2*k))
