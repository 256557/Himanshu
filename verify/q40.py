from fractions import Fraction as F
pen=F(4,5); prior=F(1,2)
lc=prior*(1-pen)*(1-pen/2)**2; ln=(1-prior)
post=lc/(lc+ln); print("posterior carrier",post,float(post)," next child affected",post*pen/2,float(post*pen/2))
p2=prior*(1-pen)/(prior*(1-pen)+1-prior); print("ignoring children",float(p2*pen/2)," ignoring all",float(prior*pen/2))
