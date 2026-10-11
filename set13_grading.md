# Grading: epigenetic divergence and antagonistic pleiotropy (Model A)

## Fields
Readable: Yes.
Accurate: No.
Complete: No.

## Q1 errors
1. The stability condition mixes units. The response defines k_switch as a switching rate per cell division and then requires k_switch << 1/tau. A per-division rate must itself be much smaller than 1, and over n divisions the requirement is n k_switch << 1.
2. EZH2 is not stimulated by H3K27me3 directly. The EED subunit of PRC2 binds H3K27me3 and allosterically activates EZH2.
3. The claim that hepatocytes and neurons keep their identity solely through chromatin marks omits self-sustaining transcription-factor feedback, which can maintain a state without any chromatin mark.

## Q1 omissions
The question concerns genetically identical cells in general, but the response covers only chromatin. It omits bistable gene-regulatory circuits (for example, lac operon induction in E. coli), self-templating protein conformations such as the yeast prion [PSI+], and structural inheritance of cortical patterns in ciliates.

## Q2 errors
1. The survival gradient is written as the integral from x of e^(-ru) m(u) du. Hamilton's expression includes survivorship, the integral of e^(-ru) l(u) m(u) du. The cost term of the inequality then applies an extra e^(-r beta) factor and still omits l(u), so the inequality is wrong.
2. High age-independent extrinsic mortality is called the most critical condition, which is a known error. In the Euler-Lotka framework the response itself uses, a constant extra hazard mu multiplies l(x) by e^(-mu x) and lowers r by exactly mu, so e^(-rx) l(x) and both selection gradients are unchanged. A numerical check gives identical gradients to machine precision (`verify/ap_extrinsic.py`). Extrinsic mortality changes the age pattern of selection only if it is age-dependent or if density dependence acts on particular ages.
3. Both diagrams draw the survival gradient falling from birth. Hamilton's survival gradient is constant from birth to the age of first reproduction and declines only afterwards.
4. The second diagram, placed under the condition that costs after the last reproduction are invisible to selection, still shows a positive survival gradient at beta. After the last age of reproduction the survival gradient is zero.

## Paste-ready comment
Question 1 is broadly correct on chromatin mechanisms, but its stability condition mixes a per-division rate with a per-time threshold, it attributes H3K27me3 recognition to EZH2 rather than EED, and it omits non-chromatin mechanisms such as bistable regulatory circuits and prion-like proteins. Question 2 contains three errors. The survival selection gradient omits survivorship l(u), and the cost term in the spreading condition carries an extra e^(-r beta), so the inequality is incorrect. The response presents high age-independent extrinsic mortality as the most critical condition, yet in its own Euler-Lotka framework a constant added hazard reduces r by the same amount and leaves both selection gradients unchanged; extrinsic mortality matters only if it is age-dependent or interacts with density dependence. The diagrams draw the survival gradient declining from birth, although it is flat until first reproduction, and show a positive gradient at a post-reproductive age that the text calls selectively invisible.
