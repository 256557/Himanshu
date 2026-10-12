# Check Model A's bottleneck formula E[VA'] = VA(1-F) + 2F VD (claimed exact at p = 1/2) by exact binomial expectation.
from math import comb
def VA(p,a,d): q=1-p; return 2*p*q*(a+d*(q-p))**2
def VD(p,d): q=1-p; return (2*p*q*d)**2
for p,Nb in ((0.5,2),(0.5,10),(0.1,2),(0.9,2)):
    n=2*Nb; F=1/n; a=d=1
    ex=sum(comb(n,k)*p**k*(1-p)**(n-k)*VA(k/n,a,d) for k in range(n+1))
    claim=VA(p,a,d)*(1-F)+2*F*VD(p,d)
    print(f"p={p} Nb={Nb}: exact {ex:.5f}  formula {claim:.5f}  VA before {VA(p,a,d):.5f}")
