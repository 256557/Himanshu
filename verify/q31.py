# Q31: autosomal driver t. Heterozygous males transmit t to 80% of sperm; females Mendelian.
# Viability: tt females 0.5, tt males 0 (lethal); TT and Tt viability 1 in both sexes.
# 1:1 sex ratio at fertilisation, random mating, large population, no mutation.
# Female and male adults are tracked separately (genotype frequencies TT, Tt, tt).
import numpy as np
k=0.8; vf=np.array([1,1,0.5]); vm=np.array([1,1,0.0])
def step(F,M):
    qe=F[1]/2+F[2]; qs=k*M[1]+M[2]          # t frequency in eggs and in sperm
    z=np.array([(1-qe)*(1-qs), qe*(1-qs)+qs*(1-qe), qe*qs])
    f=z*vf; m=z*vm
    return f/f.sum(), m/m.sum(), z
F=np.array([0.98,0.02,0.0]); M=F.copy()
for _ in range(50000): F,M,z=step(F,M)
qf=F[1]/2+F[2]; qm=M[1]/2+M[2]
print('adult females TT,Tt,tt',np.round(F,6),' t freq',round(qf,6))
print('adult males   TT,Tt,tt',np.round(M,6),' t freq',round(qm,6))
print('zygotes TT,Tt,tt',np.round(z,6),' fraction of zygotes dying',round(z[2]*0.5*0.5+z[2]*0.5*1,6))
F2,M2,_=step(F,M); print('fixed-point check',np.abs(F2-F).max(),np.abs(M2-M).max())
