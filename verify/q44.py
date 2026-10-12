# Q44: X-linked lethal, equal mutation rate u in eggs and sperm, carrier frequency 4u.
# Grandmother G has 2 unaffected sons; mother M has 1 affected son (proband) and 3 unaffected sons.
from fractions import Fraction as F
u=F(1,10**7)
car=4*u
tot=0; mc=0
for g in (1,0):
    pg=car if g else 1-car
    pG_sons=F(1,4) if g else 1
    pm_car=(F(1,2)+ (1-F(1,2))*0 if g else 0)   # transmission from carrier G
    pm_car=(F(1,2) if g else 0) + (1-(F(1,2) if g else 0))*(1-(1-u)*(1-u))  # plus new mutation in G's egg or G's husband's sperm
    for m in (1,0):
        pm=pm_car if m else 1-pm_car
        lik=F(1,2)*F(1,8) if m else u*1   # proband affected, three unaffected sons
        w=pg*pG_sons*pm*lik; tot+=w; mc+=w*m
post=mc/tot
print("P(M carrier)",float(post)," daughter's son",float(post/4))
print("exact limit 5/37 =",5/37," son 5/148 =",5/148)
