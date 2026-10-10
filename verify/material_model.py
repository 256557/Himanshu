# Correct physics: sister chromatids are defined LOCALLY. At any point, two strands carry
# homolog-1 material (one homolog's axis) and two carry homolog-2 material. Each crossover
# joins one local homolog-1 strand with one local homolog-2 strand (4 pairs, equally likely).
import numpy as np
rng=np.random.default_rng(7)
def run(N, seg_means=None, seg_counts=None):
    """Return list of label arrays (N x 4) at the end of each segment."""
    lab=np.tile(np.array([0,0,1,1],np.int8),(N,1)); r=np.arange(N); out=[]
    for s in range(len(seg_means) if seg_means is not None else len(seg_counts)):
        k=rng.poisson(seg_means[s],N) if seg_means is not None else seg_counts[s]
        for c in range(int(k.max()) if k.size else 0):
            m=k>c
            z=np.argsort(lab+rng.random((N,4)),1)      # columns 0,1 = strands with label 0; 2,3 = label 1
            i=z[r,rng.integers(0,2,N)]; j=z[r,2+rng.integers(0,2,N)]
            li,lj=lab[r,i].copy(),lab[r,j].copy()
            lab[r[m],i[m]]=lj[m]; lab[r[m],j[m]]=li[m]
        out.append(lab.copy())
    return out
