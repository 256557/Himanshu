# X-linked recessive, affected males have fitness 0.5, equal mutation rate u in eggs and sperm.
from fractions import Fraction as F
u=1e-7; f=0.5; qf=0.0
for _ in range(2000):
    qm=qf+u                                   # sons: maternal X with egg mutation
    pat=f*qm/(1-qm*(1-f))                     # X transmitted by reproducing fathers
    qf=((qf+u)+(pat+u))/2                     # daughters: maternal X + paternal X (with sperm mutation)
print("female allele freq / u",qf/u," carrier/u",2*qf/u)
# Mother of the proband: her father is unaffected, so her paternal X is mutant only by new sperm mutation (u).
car=F(5)+1+1                                   # maternal X freq (qf+u = 6u) + paternal new mutation (u) = 7u
prior=car/2/(car/2+1); post=prior/4/(prior/4+1-prior)
print("prior",prior,"post",post,"son",post/4,float(post/4))
