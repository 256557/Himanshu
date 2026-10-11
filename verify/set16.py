import numpy as np
# Q1: LD decay with recombination only in females (cf = 0.2), separate sexes, random mating, no selection.
cf,cm=0.2,0.0
g=np.array([0.5,0,0,0.5])          # gamete freqs AB, Ab, aB, ab in both sexes initially (D = 0.25)
def D(x): return x[0]*x[3]-x[1]*x[2]
def gametes(egg,sperm,c):
    # genotype from union; output gamete freqs with recombination c
    pA_B=np.zeros(4)
    for i in range(4):
        for j in range(4):
            w=egg[i]*sperm[j]
            a=[(0,0),(0,1),(1,0),(1,1)]
            hi,hj=a[i],a[j]
            par=[hi,hj]; rec=[(hi[0],hj[1]),(hj[0],hi[1])]
            for h in par: pA_B[2*h[0]+h[1]]+=w*(1-c)/2
            for h in rec: pA_B[2*h[0]+h[1]]+=w*c/2
    return pA_B
egg,sp=g.copy(),g.copy(); Ds=[]
for t in range(12):
    Ds.append((D(egg)+D(sp))/2)
    egg,sp=gametes(egg,sp,cf),gametes(egg,sp,cm)
r=np.array(Ds)[3:]; print("Q1 per-generation decay factor:",np.round(r[1:]/r[:-1],4)[:4]," (1 - (cf+cm)/2) =",1-(cf+cm)/2)
# Q2: load at mutation-selection balance, mu = 1e-5, for s = 0.1 and 0.01, h = 0.5 and 0.
mu=1e-5
for h in (0.5,0.0):
    for s in (0.1,0.01):
        q=0.0
        for _ in range(2_000_000 if h==0 else 200000):
            q=q+(1-q)*mu
            w=1-2*h*s*q*(1-q)-s*q*q
            q=(q*q*(1-s)+q*(1-q)*(1-h*s))/w
        L=2*h*s*q*(1-q)+s*q*q
        print(f"Q2 h={h} s={s}: q={q:.5f} load={L:.3e}")
# Q3: fixation of a new beneficial mutation (additive, homozygote 1+2s... use Kimura with heterozygote advantage s)
def u(N,Ne,s): p=1/(2*N); return (1-np.exp(-4*Ne*s*p))/(1-np.exp(-4*Ne*s))
for N in (100,1000,10000): print("Q3 N=Ne=",N," u=",round(u(N,N,0.01),5),"  N=10*Ne:",round(u(N,N/10,0.01),5))
