from fractions import Fraction as F
uf=1e-6; um=10*uf; qf=0.0
for _ in range(300): qf=(qf+uf)/2+um/2
print("female allele freq/uf",qf/uf," carrier freq/uf",2*qf/uf)
uf=F(1); um=F(10); car=2*(uf+um)
prior=car/2/(car/2+uf); post=prior*F(1,4)/(prior*F(1,4)+1-prior)
print("prior",prior,"post",post,"sister",post/2,"son",post/4,float(post/4))
