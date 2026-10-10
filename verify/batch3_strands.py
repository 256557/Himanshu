# Strand-level replication: every new strand stays paired with its own template.
# PCR strand types: O original (no primer end), H half-long (5' primer end only),
# S exact length (both ends set by primers). Copy of O -> H, copy of H or S -> S.
from collections import Counter
def pcr(strands, cycles):
    for _ in range(cycles):
        duplexes=[(t,{'O':'H','H':'S','S':'S'}[t]) for t in strands]
        strands=[s for d in duplexes for s in d]
    return Counter(tuple(sorted(d)) for d in duplexes)
print("C1 ds start, 4 cycles:", pcr(['O','O'],4))
print("C2 single strand start, 3 cycles:", pcr(['O'],3))
# Meselson-Stahl: strands 'N15' or 'N14'; each round, new strand from medium.
def ms(media):
    strands=['15','15']
    for m in media:
        duplexes=[(s,m) for s in strands]; strands=[x for d in duplexes for x in d]
    return Counter(tuple(sorted(d)) for d in duplexes)
print("C3 14,14,15:", ms(['14','14','15']))
# Taylor: label one round in 3H, then cold rounds; chromatid = one duplex.
def taylor(media):
    strands=['c','c']   # one chromosome's two strands, unlabeled
    for m in media:
        duplexes=[(s,m) for s in strands]; strands=[x for d in duplexes for x in d]
    lab=sum('h' in d for d in duplexes); return lab,len(duplexes)
print("C4 hot,cold,cold labeled chromatids:", taylor(['h','c','c']))
