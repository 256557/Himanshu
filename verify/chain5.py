# Chain set 5: autotetraploid genetics with double reduction (alpha = 0.1).
# Gamete model: with probability alpha the gamete gets two sister chromatids of ONE random
# chromosome (double reduction); otherwise it gets one chromatid from each of two different
# random chromosomes (random pair of the 4 chromosomes).
from fractions import Fraction as F
from itertools import combinations
a=F(1,10)
def gametes(nA):
    chroms=['A']*nA+['a']*(4-nA); g={0:F(0),1:F(0),2:F(0)}    # key = number of A alleles
    for c in chroms: g[2 if c=='A' else 0]+=a/4
    pairs=list(combinations(range(4),2))
    for i,j in pairs: g[(chroms[i]=='A')+(chroms[j]=='A')]+=(1-a)/len(pairs)
    return g
def cross(g1,g2):
    o={k:F(0) for k in range(5)}
    for x,p in g1.items():
        for y,q in g2.items(): o[x+y]+=p*q
    return o
dup,sim,tri,nul=gametes(2),gametes(1),gametes(3),gametes(0)
print('duplex gametes AA,Aa,aa:',dup[2],dup[1],dup[0])
print('Q1 duplex aa gametes',dup[0])
s=cross(dup,dup); print('Q2 duplex selfed aaaa',s[0]); print('Q3 duplex selfed Aaaa (simplex)',s[1])
t=cross(sim,nul); print('Q4 simplex x nulliplex: duplex offspring',t[2])
u=cross(tri,tri); print('Q5 triplex selfed aaaa',u[0], float(u[0]))
print('Q6 duplex selfed: AAAA among dominant phenotype',s[4]/(1-s[0]), float(s[4]/(1-s[0])))
# alpha=0 comparison (chromosome segregation) for traps
a=F(0); d0=gametes(2); s0=cross(d0,d0)
print('alpha=0: Q1',d0[0],' Q2',s0[0],' Q3',s0[1],' Q4',cross(gametes(1),gametes(0))[2],' Q5',cross(gametes(3),gametes(3))[0],' Q6',s0[4]/(1-s0[0]))
