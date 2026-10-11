# Q34: recessive lethal; heterozygous FEMALES transmit t to 75% of eggs; males Mendelian.
import math
k=0.75; x=0.01                         # x = adult heterozygote frequency
for _ in range(20000):
    qe=k*x; qs=x/2
    tt=qe*qs; Tt=qe*(1-qs)+qs*(1-qe); x=Tt/(1-tt)
print('iterated: het',round(x,6),' adult t freq',round(x/2,6))
print('closed form x = 1 - sqrt((1-k)/k):',1-math.sqrt((1-k)/k),' q =',(1-math.sqrt((1-k)/k))/2)
# Model A's Q30 method: single pool q_z = mean of gamete freqs from HWE-adult assumption, q' = q_z/(1+q_z)
q=0.1
for _ in range(20000):
    qe=k*2*q/(1+q); qs=q/(1+q); qz=(qe+qs)/2; q=qz/(1+qz)
print('single-pool method gives',round(q,6))
