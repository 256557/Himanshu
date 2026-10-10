import numpy as np
from scipy.linalg import expm
rng=np.random.default_rng(1)
# states: D0 (c1 hom0,c2 hom1), D1, S0, S1
T=np.array([[.25,.25,.25,.25],[.25,.25,.25,.25],[.5,.5,0,0],[.5,.5,0,0]])
def P(x): m=2*x; return expm(m*(T-np.eye(4)))
D0,D1,S0,S1=range(4)
def two(start,x1,x2,ok):
    p=np.zeros(4);p[start]=1;a=p@P(x1);tot=0
    for i in range(4):
        e=np.zeros(4);e[i]=1;b=e@P(x2)
        for j in range(4):
            if ok(i,j): tot+=a[i]*b[j]
    return tot
S={S0,S1};D={D0,D1}
# simulation: strands 0,1 hom0 (sisters), 2,3 hom1. return homolog label at loci
def sim(n,x1,x2,pair):
    res=np.zeros((n,2,2),int)
    for k in range(n):
        lab=np.array([0,0,1,1])
        for li,x in enumerate((x1,x2)):
            for _ in range(rng.poisson(2*x)):
                a=rng.choice(np.where(lab==0)[0]) if False else None
                # pick one strand of each homolog *by centromere*: strands 0/1 vs 2/3
                i=rng.integers(0,2); j=2+rng.integers(0,2)
                lab[i],lab[j]=lab[j],lab[i]
            res[k,li]=lab[list(pair)]
    return res
qs=[
 ("Q1 central AB/ab",D0,.1,.3,lambda i,j:(i,j) in[(D0,D0),(D1,D1)],0.6171,(0,2),lambda r:(r[:,0,0]!=r[:,0,1])&(r[:,0,0]==r[:,1,0])&(r[:,0,1]==r[:,1,1])),
 ("Q2 central hom both",D0,.2,.25,lambda i,j:i in S and j in S,0.0975,(0,2),lambda r:(r[:,0,0]==r[:,0,1])&(r[:,1,0]==r[:,1,1])),
 ("Q3 terminal homA hetB",S0,.15,.2,lambda i,j:i in S and j in D,0.2281,(0,1),lambda r:(r[:,0,0]==r[:,0,1])&(r[:,1,0]!=r[:,1,1])),
 ("Q4 central Ab/aB",D0,.3,.1,lambda i,j:(i,j) in[(D0,D1),(D1,D0)],0.0381,(0,2),lambda r:(r[:,0,0]!=r[:,0,1])&(r[:,1,0]!=r[:,1,1])&(r[:,0,0]!=r[:,1,0])),
 ("Q5 terminal hom both",S0,.5,.5,lambda i,j:i in S and j in S,0.2324,(0,1),lambda r:(r[:,0,0]==r[:,0,1])&(r[:,1,0]==r[:,1,1])),
 ("Q6 central hom both",D0,.5,.5,lambda i,j:i in S and j in S,0.1248,(0,2),lambda r:(r[:,0,0]==r[:,0,1])&(r[:,1,0]==r[:,1,1])),
 ("Q7 SDR hom both",S0,.3,.2,lambda i,j:i in S and j in S,0.4226,(0,1),lambda r:(r[:,0,0]==r[:,0,1])&(r[:,1,0]==r[:,1,1])),
 ("Q8 attX y f",D0,.1,.56,lambda i,j:i==S0 and j==S0,0.0169,(0,2),lambda r:(r[:,0]==0).all(1)&(r[:,1]==0).all(1)),
 ("Q9 attX y 66cM",D0,.66,0,lambda i,j:i==S0,0.1437,(0,2),lambda r:(r[:,0]==0).all(1)),
 ("Q10 FDR het both",D0,.2,.2,lambda i,j:i in D and j in D,0.7218,(0,2),lambda r:(r[:,0,0]!=r[:,0,1])&(r[:,1,0]!=r[:,1,1])),
 ("Q11 SDR het both",S0,.25,.15,lambda i,j:i in D and j in D,0.3093,(0,1),lambda r:(r[:,0,0]!=r[:,0,1])&(r[:,1,0]!=r[:,1,1])),
 ("Q12 asci SDS both",S0,.1,.2,lambda i,j:i in D and j in D,0.1468,(0,1),lambda r:(r[:,0,0]!=r[:,0,1])&(r[:,1,0]!=r[:,1,1])),
]
N=200000
for name,st,x1,x2,ok,claim,pair,f in qs:
    ex=two(st,x1,x2,ok); r=sim(N,x1,x2,pair); s=f(r).mean()
    print(f"{name:24s} exact={ex:.4f} claimed={claim:.4f} sim={s:.4f}+-{2*np.sqrt(s*(1-s)/N):.4f} {'OK' if round(ex,4)==claim else 'MISMATCH'}")
