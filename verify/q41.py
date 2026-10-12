from fractions import Fraction as F
# Haldane: X-linked recessive lethal, equal mutation rates, mutation-selection equilibrium.
# P(mother carrier | one affected son, no family history) = 2/3 (standard result; derived below).
mu=F(1,10**6); carrier_freq=4*mu
pc=carrier_freq*F(1,2); pn=(1-carrier_freq)*mu   # prob affected son via carrier mother vs new mutation in egg
prior=pc/(pc+pn); print("P(mother carrier | isolated case) ~",float(prior))
prior=F(2,3); post=prior*F(1,4)/(prior*F(1,4)+(1-prior))
print("after two unaffected sons",post," sister carrier",post/2," sister's son affected",post/4,float(post/4))
print("ignoring brothers:",prior/4)
# Iterate the two-sex recursion for an X-linked lethal to get the carrier frequency.
mu=1e-6; qf=0.0
for _ in range(200): qm=qf+mu; qf=qf/2+mu
print("female allele freq",qf/mu,"mu; carrier freq",2*qf/mu,"mu; affected male freq",(qf+mu)/mu,"mu")
