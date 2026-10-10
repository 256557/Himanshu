# X-linked two-locus LD, exact fractions. Recombination r only in females.
# Next gen: sons get one maternal gamete; daughters get a maternal gamete + the father's X.
from fractions import Fraction as F
from itertools import product
H=['11','12','21','22']   # haplotype A_i B_j
def gametes(genos,r):
    """genos: dict {(h1,h2): freq} for females -> gamete haplotype freqs."""
    g={h:F(0) for h in H}
    for (h1,h2),f in genos.items():
        rec1=h1[0]+h2[1]; rec2=h2[0]+h1[1]
        for h,w in ((h1,(1-r)/2),(h2,(1-r)/2),(rec1,r/2),(rec2,r/2)): g[h]+=f*w
    return g
def D(hf):
    t=sum(hf.values()); p={h:hf[h]/t for h in H}
    pA=p['11']+p['12']; pB=p['11']+p['21']
    return p['11']-pA*pB
def step(fem,male,r):
    g=gametes(fem,r)
    newfem={(a,b):g[a]*male[b] for a in H for b in H}   # maternal gamete a, paternal X b
    newmale=g
    return newfem,newmale
def female_haps(fem):
    h={x:F(0) for x in H}
    for (a,b),f in fem.items(): h[a]+=f/2; h[b]+=f/2
    return h
def run(fem,male,r,gens):
    for _ in range(gens): fem,male=step(fem,male,r)
    return fem,male
# user's original question
fem0={('11','22'):F(2,3),('12','21'):F(1,3)}; male0={'11':F(3,4),'12':F(0),'21':F(0),'22':F(1,4)}
f2,m2=run(fem0,male0,F(15,100),2)
print('USER Q: D among female X in gen 2 =',D(female_haps(f2)))
# NEW question: r = 1/5 in females; males 3/5 A1B1, 2/5 A2B2;
# females 1/2 A1B1/A2B2, 1/4 A1B2/A2B1, 1/4 A1B1/A1B1. D across ALL X chromosomes in gen 2.
fem0={('11','22'):F(1,2),('12','21'):F(1,4),('11','11'):F(1,4)}
male0={'11':F(3,5),'12':F(0),'21':F(0),'22':F(2,5)}
f2,m2=run(fem0,male0,F(1,5),2)
fh=female_haps(f2); allX={h:2*fh[h]+m2[h] for h in H}   # each female 2 X, each male 1 X (equal numbers)
Df,Dm,Dall=D(fh),D(m2),D(allX)
print('NEW: D female =',Df,' D male =',Dm,' D all X =',Dall,'=',float(Dall))
print('NEW: naive weighted average (2Df+Dm)/3 =',(2*Df+Dm)/3,'=',float((2*Df+Dm)/3))
pf=fh['11']+fh['12']; pm=m2['11']+m2['12']; qf=fh['11']+fh['21']; qm=m2['11']+m2['21']
print('allele freqs gen2: pA female',pf,' male',pm,' pB female',qf,' male',qm)
