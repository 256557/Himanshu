# Two-locus coalescent with recombination inside species tree ((A,B),C). Event-driven (Hudson model).
# Lineage = [pop, mat0, mat1]; mat = frozenset of samples carried at that locus, or None.
import numpy as np, sys
def run(nrep, r, NA=25000, NB=25000, NC=25000, NAB=25000, NR=40000, t1=50000, t2=150000, seed=1):
    rng=np.random.default_rng(seed)
    size={'A':NA,'B':NB,'C':NC,'AB':NAB,'R':NR}
    out=np.zeros((nrep,2),int)      # per locus: 0 = (A,B) first, 1 = (A,C) first, 2 = (B,C) first
    code={frozenset('AB'):0,frozenset('AC'):1,frozenset('BC'):2}
    for k in range(nrep):
        L=[[s,frozenset(s),frozenset(s)] for s in 'ABC']
        first=[None,None]; t=0.0
        while first[0] is None or first[1] is None:
            # rates
            pops={}
            for i,l in enumerate(L): pops.setdefault(l[0],[]).append(i)
            ev=[]; rates=[]
            for p,idx in pops.items():
                n=len(idx)
                if n>=2: ev.append(('c',p)); rates.append(n*(n-1)/2/(2*size[p]))
            for i,l in enumerate(L):
                if l[1] is not None and l[2] is not None: ev.append(('r',i)); rates.append(r)
            tot=sum(rates)
            nxt= t1 if t<t1 else (t2 if t<t2 else np.inf)
            dt=rng.exponential(1/tot) if tot>0 else np.inf
            if t+dt>=nxt:
                t=nxt
                for l in L:
                    if t==t1 and l[0] in ('A','B'): l[0]='AB'
                    if t==t2 and l[0] in ('AB','C'): l[0]='R'
                continue
            t+=dt
            e=ev[rng.choice(len(ev),p=np.array(rates)/tot)]
            if e[0]=='r':
                l=L[e[1]]; L.append([l[0],None,l[2]]); l[2]=None
            else:
                idx=pops[e[1]]; i,j=rng.choice(idx,2,replace=False)
                a,b=L[i],L[j]; new=[a[0],None,None]
                for loc in (1,2):
                    if a[loc] is not None and b[loc] is not None:
                        if first[loc-1] is None and len(a[loc])==1 and len(b[loc])==1:
                            first[loc-1]=code[a[loc]|b[loc]]
                        m=a[loc]|b[loc]; new[loc]=None if len(m)==3 else m
                    else: new[loc]=a[loc] if a[loc] is not None else b[loc]
                    if new[loc] is not None and len(new[loc])==3: new[loc]=None
                    # a locus whose first pair already merged elsewhere: first stays
                for x in sorted([i,j],reverse=True): L.pop(x)
                if new[1] is not None or new[2] is not None: L.append(new)
            # a single lineage whose first coalescence at a locus already happened and is the last two:
            for loc in (0,1):
                if first[loc] is None:
                    holders=[l for l in L if l[loc+1] is not None]
                    sizes=sorted(len(l[loc+1]) for l in holders)
                    if sizes==[1,2]:    # first merge happened: identify pair from the size-2 set
                        pair=[l[loc+1] for l in holders if len(l[loc+1])==2][0]; first[loc]=code[pair]
        out[k]=first
    return out
if __name__=='__main__':
    for r in (0.0, 1.0):
        o=run(20000,r,seed=3)
        print('r=',r,' P(locus1 concordant)',(o[:,0]==0).mean(),' P(both)',((o[:,0]==0)&(o[:,1]==0)).mean())
