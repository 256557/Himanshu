import numpy as np, itertools
from scipy.linalg import expm
# strands 0,1 share centromere (homolog-0 sisters), 2,3 share the other centromere.
# state = tuple of distal material (0/1) on each strand; always two 0s and two 1s.
states=[s for s in itertools.product((0,1),repeat=4) if sum(s)==2]
idx={s:k for k,s in enumerate(states)}
T=np.zeros((6,6))
for s in states:
    for i in (0,1):
        for j in (2,3):   # crossover between non-sister chromatids, all 4 pairs equally likely
            t=list(s); t[i],t[j]=t[j],t[i]; T[idx[s],idx[tuple(t)]]+=.25
P=lambda x: expm(2*x*(T-np.eye(6)))
start=np.zeros(6); start[idx[(0,0,1,1)]]=1
def q(x1,x2,pair,ok):
    a=start@P(x1); tot=0
    for s in states:
        e=np.zeros(6); e[idx[s]]=1; b=e@P(x2)
        for t in states:
            tot+=a[idx[s]]*b[idx[t]]*ok((s[pair[0]],s[pair[1]]),(t[pair[0]],t[pair[1]]))
    return tot
hom=lambda g:g[0]==g[1]; het=lambda g:g[0]!=g[1]
C,Tm=(0,2),(0,1)   # central/FDR/attached-X pair; terminal/SDR/asci sister pair
rows=[("Q1",.1,.3,C,lambda a,b:het(a) and a==b,0.6171),
("Q2",.2,.25,C,lambda a,b:hom(a) and hom(b),0.0975),
("Q3",.15,.2,Tm,lambda a,b:hom(a) and het(b),0.2281),
("Q4",.3,.1,C,lambda a,b:het(a) and het(b) and a!=b,0.0381),
("Q5",.5,.5,Tm,lambda a,b:hom(a) and hom(b),0.2324),
("Q6",.5,.5,C,lambda a,b:hom(a) and hom(b),0.1248),
("Q7",.3,.2,Tm,lambda a,b:hom(a) and hom(b),0.4226),
("Q8",.1,.56,C,lambda a,b:a==(0,0) and b==(0,0),0.0169),
("Q9",.66,0,C,lambda a,b:a==(0,0),0.1437),
("Q10",.2,.2,C,lambda a,b:het(a) and het(b),0.7218),
("Q11",.25,.15,Tm,lambda a,b:het(a) and het(b),0.3093),
("Q12",.1,.2,Tm,lambda a,b:het(a) and het(b),0.1468)]
for n,x1,x2,p,ok,c in rows:
    v=q(x1,x2,p,ok); print(f"{n:4s} full-tetrad exact={v:.4f}  bank={c:.4f}  {'OK' if round(v,4)==c else 'WRONG'}")
