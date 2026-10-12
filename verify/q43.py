from fractions import Fraction as F
ue=1e-6; us=0.1*ue; qf=0.0
for _ in range(300): qf=(qf+ue)/2+us/2
print("carrier freq / ue",2*qf/ue)
def risk(car_over_ue, n=4):
    odds=F(car_over_ue)/2          # carrier route weight / new-mutation weight (ue)
    post=odds*F(1,2**n)/(odds*F(1,2**n)+1)
    return post, post/4
c=risk(F(22,10)); p=risk(F(42,10)); s=risk(4)
print("correct",c,float(c[1])," pooled",float(p[1])," standard 2/3 prior",float(s[1]))
