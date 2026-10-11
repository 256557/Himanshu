# Q30: recessive lethal driver, drive only in heterozygous males (k = 0.9), Mendelian in females.
# Autosomal, random mating, large population, no mutation. x = heterozygote frequency among adults
# (same in both sexes, since survival does not depend on sex).
from fractions import Fraction as F
import math
k=0.9; x=0.01
for _ in range(5000):
    qf=x/2; qm=k*x                      # egg and sperm frequencies of the driver
    aa=qf*qm; Aa=qf*(1-qm)+qm*(1-qf)
    x=Aa/(1-aa)
print('iterated: adult heterozygotes',round(x,6),' adult allele freq',round(x/2,6),
      ' zygote allele freq',round((x/2+k*x)/2,6),' zygotes dying',round(k*x*x/2,6))
print('closed form: x = 1 - sqrt((1-k)/k) =',1-math.sqrt((1-k)/k))
# traps
print('symmetric-drive formula: het',(2*k-1)/k,' allele',(2*k-1)/(2*k))
