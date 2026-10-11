# Counterexample to "equal allele frequency in both sexes is sufficient": equal adult frequencies (p = 0.3,
# same genotype frequencies in each sex) but heterozygous males transmit A to 90% of sperm.
AA,Aa,aa=0.09,0.42,0.49
pm=AA+0.9*Aa; pf=AA+0.5*Aa
off=(pm*pf, pm*(1-pf)+pf*(1-pm), (1-pm)*(1-pf)); p=off[0]+off[1]/2
print("sperm",round(pm,4),"eggs",round(pf,4)," offspring",[round(v,4) for v in off]," HW",[round(p*p,4),round(2*p*(1-p),4),round((1-p)**2,4)])
