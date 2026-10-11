# Does age-independent extrinsic mortality change Hamilton's age-specific selection gradients?
# Euler-Lotka: sum_x e^{-rx} l(x) m(x) = 1. Add hazard mu: l'(x) = l(x) e^{-mu x}. Then r' = r - mu.
import numpy as np
from scipy.optimize import brentq
x=np.arange(0,40); m=np.where(x>=2,1.0,0.0); l=np.exp(-0.15*x)*np.exp(-0.002*x**2)
def grads(l):
    r=brentq(lambda r: np.sum(np.exp(-r*x)*l*m)-1,-2,2)
    T=np.sum(x*np.exp(-r*x)*l*m)
    gm=np.exp(-r*x)*l/T                                     # dr/dm(x)
    gs=np.array([np.sum((np.exp(-r*x)*l*m)[x>a]) for a in x])/T   # dr/dln p(a), survival a -> a+1
    return r,gm,gs
r0,gm0,gs0=grads(l); r1,gm1,gs1=grads(l*np.exp(-0.3*x))
print("r without / with extra hazard 0.3:",round(r0,4),round(r1,4))
print("max change in fecundity gradient:",np.abs(gm0-gm1).max(), " survival gradient:",np.abs(gs0-gs1).max())
