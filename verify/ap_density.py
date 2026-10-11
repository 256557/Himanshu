# Extrinsic mortality under different population regulation.
# (A) density-independent growth: r adjusts -> gradients unchanged.
# (B) regulation by a uniform factor on fecundity (or on survival to first census): r = 0 at equilibrium.
# (C) regulation by an age-independent hazard that falls when mu rises (total hazard fixed): unchanged.
import numpy as np
x=np.arange(0,40); m=np.where(x>=2,1.0,0.0); l=np.exp(-0.15*x)*np.exp(-0.002*x**2)
def rel_fec_gradient(l,m,r):
    g=np.exp(-r*x)*l; return g[20]/g[2]
from scipy.optimize import brentq
def r_of(l,m): return brentq(lambda r: np.sum(np.exp(-r*x)*l*m)-1,-3,3)
mu=0.3; le=l*np.exp(-mu*x)
print("A: ratio g(20)/g(2) mu=0:",rel_fec_gradient(l,m,r_of(l,m)),"mu=0.3:",rel_fec_gradient(le,m,r_of(le,m)))
c0=1/np.sum(l*m); c1=1/np.sum(le*m)
print("B: ratio mu=0:",rel_fec_gradient(l,c0*m,0),"mu=0.3:",rel_fec_gradient(le,c1*m,0))
