# Q32: chymotrypsin-like enzyme; pH dependence, DFP adduct mass, active-site titration, mutant contamination.
C,H,O,F,P=12.011,1.008,15.999,18.998,30.974     # average atomic masses
# (a) fraction of maximal kcat at pH 5.8: activity needs His57 neutral (pKa 6.8) and Ile16 amino group protonated (pKa 9.0)
pH,pK1,pK2=5.8,6.8,9.0
fa=1/(1+10**(pK1-pH)+10**(pH-pK2)); print('(a) kcat fraction at pH 5.8 =',round(fa,4))
# (b) mass increase on DFP labelling: Ser-OH + DFP -> Ser-O-P(O)(OiPr)2 + HF
DFP=6*C+14*H+F+3*O+P; HF=H+F; shift=DFP-HF
print('(b) DFP mass',round(DFP,3),' HF',round(HF,3),' mass shift',round(shift,2),'Da')
wrong=(P+O+2*(3*C+7*H))-H; print('    shift with the wrong phosphinyl formula P(O)(iPr)2:',round(wrong,2),'Da')
# (c) active-site titration: 1.00 mg enzyme, Mr 25,000, incorporates 30.0 nmol DIP
nmol=1.00e-3/25000*1e9; print('(c) enzyme nmol',nmol,' active fraction',30.0/nmol)
# (d) S195A prep shows 0.50% of WT specific activity; intrinsic mutant activity 1e-6 of WT
f=(0.005-1e-6)/(1-1e-6); print('(d) WT contamination fraction',f,' percent',round(f*100,4))
