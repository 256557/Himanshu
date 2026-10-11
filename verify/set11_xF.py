# X-linked inbreeding of a daughter of first cousins, four cousin types, by gene dropping.
# Founders: grandparents G (male) and H (female) whose two children are the siblings that link the cousins.
import numpy as np
rng=np.random.default_rng(11); n=2_000_000
def child_X(sex, mother, father):
    """mother: (2,n) labels; father: (1,n). Returns X labels of child."""
    m=mother[rng.integers(0,2,n),np.arange(n)]
    return m[None] if sex=='M' else np.vstack([m,father[0]])
uid=iter(range(100,10**6))
def founder(sex):
    k=1 if sex=='M' else 2
    return np.vstack([np.full(n,next(uid)) for _ in range(k)])
def run(sib1, sib2):
    """sib1 is a parent of the cousin who is the daughter's father; sib2 a parent of her mother."""
    G,H=founder('M'),founder('F')
    s1=child_X(sib1,H,G); s2=child_X(sib2,H,G)
    sp1=founder('F' if sib1=='M' else 'M'); sp2=founder('F' if sib2=='M' else 'M')
    mo1,fa1=(s1,sp1) if sib1=='F' else (sp1,s1)
    mo2,fa2=(s2,sp2) if sib2=='F' else (sp2,s2)
    father=child_X('M',mo1,fa1); mother=child_X('F',mo2,fa2)
    d=child_X('F',mother,father)
    return np.mean(d[0]==d[1])
for name,a,b in [("mothers are sisters",'F','F'),("fathers are brothers",'M','M'),
                 ("father's mother and mother's father are siblings",'F','M'),
                 ("father's father and mother's mother are siblings",'M','F')]:
    print(f"{name}: {run(a,b):.4f}")
print("exact: 3/16 =",3/16,", 0, 1/8 =",1/8,", 0")
