# Set 20: isolated X-linked cases. f = fitness of affected males, k = sperm/egg mutation ratio,
# n = unaffected brothers of the proband, gf = maternal grandfather stated unaffected.
from fractions import Fraction as F
def solve(f,k,n,gf):
    f=F(f); k=F(k); ue=F(1); us=k
    qf=(ue*(1+f)+us)/(1-f)
    C=qf+ue+us if gf else 2*qf
    odds=C/2/ue
    post=odds/2**n/(odds/2**n+1)
    return qf,C,odds,post,post/4
cases=[(0,1,3,False),(0,4,2,False),(F(1,2),1,3,True),(F(1,3),1,2,True),(F(1,2),2,1,False),(F(1,4),0,2,True),(0,F(1,2),5,False)]
for i,c in enumerate(cases,1):
    qf,C,o,p,r=solve(*c)
    print(i,c,"qf",qf,"C",C,"odds",o,"post",p,"risk",r,round(float(r),4))
# numeric check of the equilibrium for case 3 by iteration
u=1e-7; f=0.5; q=0.0
for _ in range(3000): qm=q+u; q=((q+u)+(f*qm/(1-qm*(1-f))+u))/2
print("iter qf/u",q/u)
