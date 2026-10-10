from fractions import Fraction as F
from itertools import combinations
# Q-A: tetrads with chromatid interference
P0,P1,P2=F(1,2),F(35,100),F(15,100)          # number of crossovers between A and B (0,1,2)
two,three,four=F(1,10),F(7,10),F(2,10)        # second crossover: 2-strand, 3-strand, 4-strand
PD=P0+P2*two; T=P1+P2*three; NPD=P2*four
print('PD',PD,float(PD),' T',T,float(T),' NPD',NPD,float(NPD),' sum',PD+T+NPD)
true_cM=(P1+2*P2)/2*100; perkins=(T+6*NPD)/2*100; RF=(T/2+NPD)*100
print('true map distance cM',float(true_cM),' Perkins estimate',float(perkins),' RF %',float(RF))
# random chromatid choice for comparison
PDr=P0+P2/4; Tr=P1+P2/2; NPDr=P2/4; print('no chromatid interference: PD',float(PDr),'T',float(Tr),'NPD',float(NPDr),' Perkins',float((Tr+6*NPDr)/2*100))
# Q-B: count unrooted binary trees on 6 taxa containing split AB|CDEF but not CD|ABEF
taxa='ABCDEF'
def trees(labels):
    # build all unrooted binary trees by stepwise addition; represent as set of nontrivial splits
    def splits_of(edges,leaves):
        # edges: adjacency dict; compute leaf set on each side of each internal edge
        res=set()
        for u in edges:
            for v in edges[u]:
                if u<v:
                    side=set(); stack=[v]; seen={u,v}
                    while stack:
                        x=stack.pop()
                        if x in leaves: side.add(x)
                        for y in edges[x]:
                            if y not in seen: seen.add(y); stack.append(y)
                    if 1<len(side)<len(leaves)-1:
                        s=frozenset(side); res.add(min(s,frozenset(leaves)-s,key=lambda z:sorted(z)))
        return frozenset(res)
    import copy
    out=set(); nid=[0]
    start={labels[0]:{'i0'},labels[1]:{'i0'},labels[2]:{'i0'},'i0':{labels[0],labels[1],labels[2]}}
    def grow(adj,k):
        if k==len(labels): out.add(splits_of(adj,set(labels))); return
        edges=[(u,v) for u in adj for v in adj[u] if str(u)<str(v)]
        for u,v in edges:
            a=copy.deepcopy(adj); nid[0]+=1; w='n%d'%nid[0]
            a[u].discard(v); a[v].discard(u); a[w]={u,v,labels[k]}; a[u].add(w); a[v].add(w); a[labels[k]]={w}
            grow(a,k+1)
    grow(start,3); return out
T6=trees(list(taxa)); print('total unrooted binary trees on 6 taxa',len(T6))
AB=frozenset('AB'); CD=frozenset('CD')
norm=lambda s:min(s,frozenset(taxa)-s,key=lambda z:sorted(z))
withAB=[t for t in T6 if norm(AB) in t]; both=[t for t in withAB if norm(CD) in t]
print('contain AB|CDEF:',len(withAB),' and also CD|ABEF:',len(both),' AB but not CD:',len(withAB)-len(both))
AC=frozenset('AC'); print('trees containing both AB|CDEF and AC|BDEF:',sum(1 for t in T6 if norm(AB) in t and norm(AC) in t))
