import numpy as np
rng=np.random.default_rng(2026); a,b=0.30,0.50
hits=homs=0
for chunk in range(40):
    N=1_000_000; lab=np.tile(np.array([0,0,1,1],np.int8),(N,1)); r=np.arange(N); res=[]
    for m_ in (a,b):
        k=rng.poisson(m_,N)
        for c in range(k.max()):
            m=k>c; i=rng.integers(0,2,N); j=2+rng.integers(0,2,N)
            li,lj=lab[r,i].copy(),lab[r,j].copy()
            lab[r[m],i[m]]=lj[m]; lab[r[m],j[m]]=li[m]
        res.append(lab[:,0]==lab[:,2])
    homs+=res[0].sum(); hits+=(res[0]&res[1]).sum()
s=hits/homs; print('40M meioses: P(hom B | hom A) =',round(s,5),'+-',round(2*np.sqrt(s*(1-s)/homs),5),' n_homA',homs)
print('mine 0.80146   Model A 0.80327')
