import sympy as sp, itertools
m=sp.symbols('m',positive=True)
states=[s for s in itertools.product((0,1),repeat=4) if sum(s)==2]
idx={s:k for k,s in enumerate(states)}
T=sp.zeros(6)
for s in states:
    for i in (0,1):
        for j in (2,3):
            t=list(s); t[i],t[j]=t[j],t[i]; T[idx[s],idx[tuple(t)]]+=sp.Rational(1,4)
E=((T-sp.eye(6))*m).exp()
for s in states:
  print(s,[sp.simplify(E[idx[s],idx[t]]) for t in states])
