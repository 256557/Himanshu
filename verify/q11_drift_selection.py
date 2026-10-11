# Q11: fixation of a deleterious allele, s = -0.02 (homozygote fitness 1+s, heterozygote 1+hs).
# Diffusion (Kimura): u(p) = int_0^p G / int_0^1 G,  G(x) = exp(-2 Ne s (2 h x + (1-2h) x^2)).
# Checked against Wright-Fisher simulation (Ne = N = 50, new mutant p = 1/(2N)).
import numpy as np
from scipy.integrate import quad
s=-0.02
def u(N,Ne,h,p=None):
    p=1/(2*N) if p is None else p
    G=lambda x: np.exp(-2*Ne*s*(2*h*x+(1-2*h)*x*x))
    return quad(G,0,p)[0]/quad(G,0,1)[0]
print("neutral 1/(2N) and u for h = 0, 0.5, 1 (Ne = N):")
for N in [10,25,50,100,250,500,1000]:
    print(N, f"{1/(2*N):.3e}", *[f"{u(N,N,h):.3e}" for h in (0,0.5,1)])
print("N = 1000, Ne = 100 (census larger than Ne), h = 0.5:", f"{u(1000,100,0.5):.3e}")
rng=np.random.default_rng(11)
def wf(N,h,reps):
    fix=0
    for _ in range(reps//200000):
        n=np.ones(200000,np.int64)
        alive=np.ones(200000,bool)
        while alive.any():
            x=n[alive]/(2*N)
            w11,w12=1+s,1+h*s
            num=x*x*w11+x*(1-x)*w12
            den=num+x*(1-x)*w12+(1-x)**2
            n[alive]=rng.binomial(2*N,num/den)
            fix+=np.sum(n[alive]==2*N)
            alive&=(n>0)&(n<2*N)
    return fix/reps
reps=4_000_000
for h in (0,0.5,1):
    p=wf(50,h,reps); print(f"WF N=50 h={h}: sim {p:.3e} +- {np.sqrt(p/reps):.1e}   diffusion {u(50,50,h):.3e}")
