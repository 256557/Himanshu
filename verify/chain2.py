# Chain set 2: two host groups, next-generation matrix K[i][j] = new infections in group i
# caused by one infected individual of group j (column = infector). Children c, adults a.
import numpy as np
from scipy.optimize import brentq
K=np.array([[3.0,0.5],[1.0,0.6]])
ev,V=np.linalg.eig(K); i=np.argmax(ev.real); R0=ev[i].real; v=np.abs(V[:,i].real); v/=v.sum()
print('Q1 R0',round(R0,6),' exact (3.6+sqrt(7.76))/2 =',round((3.6+np.sqrt(7.76))/2,6))
print('Q2 fraction of early infections in children',round(v[0],6))
rho=lambda p: max(abs(np.linalg.eigvals(np.array([[3*(1-p),0.5*(1-p)],[1,0.6]]))))
pc=brentq(lambda p:rho(p)-1,0,1); print('Q3 children-only vaccination threshold',round(pc,6),' exact 1-0.4/1.7 =',round(1-0.4/1.7,6))
T=3+0.5*1/(1-0.6); print('Q4 type-reproduction number for children',T,' 1-1/T =',round(1-1/T,6))
print('Q5 uniform vaccination threshold 1-1/R0 =',round(1-1/R0,6))
print('traps: arithmetic mean of K entries / column sums etc:',K.sum(0),'sqrt of products',np.sqrt(3*0.6))
