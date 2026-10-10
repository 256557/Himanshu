import numpy as np, sys
sys.path.insert(0,'.')
from material_model import run, rng
N=1_000_000
C,Tm=(0,2),(0,1)
def f(pair,x1,x2,test):
    A,B=run(N,seg_means=[2*x1,2*x2])
    a=(A[:,pair[0]],A[:,pair[1]]); b=(B[:,pair[0]],B[:,pair[1]])
    return test(a,b).mean()
hom=lambda g:g[0]==g[1]; het=lambda g:g[0]!=g[1]
rows=[("Q1",C,.1,.3,lambda a,b:het(a)&het(b)&(a[0]==b[0]),0.6171),
("Q2",C,.2,.25,lambda a,b:hom(a)&hom(b),0.0975),
("Q3",Tm,.15,.2,lambda a,b:hom(a)&het(b),0.2281),
("Q4",C,.3,.1,lambda a,b:het(a)&het(b)&(a[0]!=b[0]),0.0381),
("Q5",Tm,.5,.5,lambda a,b:hom(a)&hom(b),0.2324),
("Q6",C,.5,.5,lambda a,b:hom(a)&hom(b),0.1248),
("Q7",Tm,.3,.2,lambda a,b:hom(a)&hom(b),0.4226),
("Q8",C,.1,.56,lambda a,b:(a[0]==0)&(a[1]==0)&(b[0]==0)&(b[1]==0),0.0169),
("Q10",C,.2,.2,lambda a,b:het(a)&het(b),0.7218),
("Q11",Tm,.25,.15,lambda a,b:het(a)&het(b),0.3093),
("Q12",Tm,.1,.2,lambda a,b:het(a)&het(b),0.1468)]
for n,p,x1,x2,t,orig in rows:
    v=f(p,x1,x2,t); print(f"{n:4s} sim={v:.4f}  original bank={orig:.4f}  {'MATCH' if abs(v-orig)<0.002 else 'DIFF'}")
# Q14: FDR, P(hom B | hom A), A 15 cM, B +25 cM
A,B=run(N,seg_means=[0.3,0.5]); hA=A[:,0]==A[:,2]; hB=B[:,0]==B[:,2]
print('Q14 sim',round((hA&hB).sum()/hA.sum(),4),' formula 1/3+2/3e^-0.75 =',round(1/3+2/3*np.exp(-0.75),4))
# Q15: exactly two chiasmata uniform on arm, central fusion, A 0.3, B 0.7
pos=rng.random((N,2)); kA=(pos<0.3).sum(1); kAB=((pos>=0.3)&(pos<0.7)).sum(1)
A,B=run(N,seg_counts=[kA,kAB]); print('Q15 sim',round(((A[:,0]==A[:,2])&(B[:,0]==B[:,2])).mean(),4),' hand 0.1125')
# tetrad types must NOT depend on centromere distance
for c in (0.0,1.0):
    A,B=run(N,seg_means=[c,0.5]); rec=(A!=B).sum(1)
    print('tetrad c=',c,'PD',round((rec==0).mean(),4),'NPD',round((rec==4).mean(),4),'T',round(((rec>0)&(rec<4)).mean(),4))
