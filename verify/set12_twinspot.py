# Mitotic crossover in a y + / + sn female (y distal, sn proximal). One G2 crossover per cell:
# 80% between centromere and sn, 20% between sn and y. It joins one chromatid of each homolog,
# and at anaphase each daughter receives one chromatid from each centromere at random.
import numpy as np
rng=np.random.default_rng(12); n=1_000_000
out={'twin':0,'yellow':0,'singed':0,'none':0}
for _ in range(1):
    prox=rng.random(n)<0.8
    i=rng.integers(0,2,n); j=2+rng.integers(0,2,n)        # chromatids 0,1 on homolog 1; 2,3 on homolog 2
    Y=np.tile([1,1,0,0],(n,1)); S=np.tile([0,0,1,1],(n,1)) # 1 = mutant allele
    r=np.arange(n)
    yi,yj=Y[r,i].copy(),Y[r,j].copy(); Y[r,i]=yj; Y[r,j]=yi        # y is distal to either crossover
    si,sj=S[r,i].copy(),S[r,j].copy(); S[r[prox],i[prox]]=sj[prox]; S[r[prox],j[prox]]=si[prox]
    pick=rng.integers(0,2,n)                                       # pairing at segregation
    d1=(np.zeros(n,int),2+pick); d2=(np.ones(n,int),3-pick)   # chromatid 0 joins 2 or 3
    def pheno(d):
        y=(Y[r,d[0]]+Y[r,d[1]])==2; s=(S[r,d[0]]+S[r,d[1]])==2
        return y,s
    y1,s1=pheno(d1); y2,s2=pheno(d2)
    twin=(y1&s2&~s1&~y2)|(y2&s1&~s2&~y1)
    yel=~twin&((y1&~s1)|(y2&~s2)); sng=~twin&((s1&~y1)|(s2&~y2))
    print("twin",twin.mean(),"yellow single",yel.mean(),"singed single",sng.mean(),"no spot",(~twin&~yel&~sng).mean())
