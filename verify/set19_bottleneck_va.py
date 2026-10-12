# Additive variance at a locus with complete dominance (a = d = 1): VA = 2pq[a + d(q - p)]^2, q = recessive allele freq.
# Before: q = 0.1. Bottleneck: one generation founded by N = 2 individuals (4 gene copies), binomial sampling.
from math import comb
def VA(q): p=1-q; return 2*p*q*(1+(q-p))**2
q0=0.1; n=4
E=sum(comb(n,k)*q0**k*(1-q0)**(n-k)*VA(k/n) for k in range(n+1))
H0=2*q0*(1-q0); EH=sum(comb(n,k)*q0**k*(1-q0)**(n-k)*2*(k/n)*(1-k/n) for k in range(n+1))
print("VA before",VA(q0)," expected VA after",round(E,5)," ratio",round(E/VA(q0),2))
print("heterozygosity before",H0," after",round(EH,4))
