# Chain set 3: two host groups + leaky vaccine. Column = infector, row = infected.
import numpy as np
from scipy.optimize import brentq
K=np.array([[2.4,0.8],[0.9,0.7]])        # children, adults
es,ei=0.7,0.5                            # vaccine: -70% susceptibility, -50% infectiousness if infected
def ngm(p):
    # types: unvaccinated children (cu), vaccinated children (cv), adults (a)
    sus=np.array([1-p, p*(1-es), 1.0])           # share of each child type's susceptible mass, adults 1
    inf=np.array([1.0, 1-ei, 1.0])               # infectiousness of each type
    base=np.array([[K[0,0],K[0,0],K[0,1]],
                   [K[0,0],K[0,0],K[0,1]],
                   [K[1,0],K[1,0],K[1,1]]])      # child->child, child->adult etc by group
    return sus[:,None]*base*inf[None,:]
rho=lambda M: max(abs(np.linalg.eigvals(M)))
R0=rho(K); print('Q1 R0',round(R0,6))
M=ngm(0.8); R=rho(M); print('Q2 R with 80% of children vaccinated',round(R,6))
ev,V=np.linalg.eig(M); i=np.argmax(abs(ev)); v=np.abs(V[:,i].real); v/=v.sum()
print('Q3 share of early cases: unvacc child, vacc child, adult',np.round(v,6))
print('Q4 R with 100% of children vaccinated',round(rho(ngm(1.0)),6))
try: print('   threshold',brentq(lambda p:rho(ngm(p))-1,0,1))
except Exception as e: print('   no threshold in [0,1]')
# wrong shortcut: scale child row by (1 - p*es), ignore infectiousness
W=lambda p: rho(np.array([[K[0,0]*(1-p*es),K[0,1]*(1-p*es)],[K[1,0],K[1,1]]]))
print('wrong (susceptibility only) Q2',round(W(0.8),6),' Q4',round(W(1.0),6))
print('wrong (both effects applied to whole child row)',round(rho(np.array([[K[0,0]*(1-p) if False else K[0,0]*(1-0.8*es)*(1-0.8*ei),K[0,1]*(1-0.8*es)],[K[1,0]*(1-0.8*ei),K[1,1]]])),6))
# Q5: uniform coverage of everyone needed (leaky vaccine, homogeneous effect on both groups)
def ngm_all(p):
    base=np.zeros((4,4)); groups=[0,0,1,1]
    sus=np.array([1-p,p*(1-es),1-p,p*(1-es)]); inf=np.array([1,1-ei,1,1-ei])
    for r in range(4):
        for c in range(4): base[r,c]=K[groups[r],groups[c]]
    return sus[:,None]*base*inf[None,:]
pc=brentq(lambda p:rho(ngm_all(p))-1,0,1); print('Q5 uniform coverage threshold',round(pc,6))
print('   formula: R0*(1 - p*(1-(1-es)(1-ei))) = 1 ->',round((1-1/R0)/(1-(1-es)*(1-ei)),6))
