# Set 10: two concept questions

## Q1
In a honeybee colony headed by a queen that mated with a single drone, what is the coefficient of relatedness of a worker to her brother, and of a drone to his sister?

Answer: worker to brother 1/4; drone to sister 1/2.

A worker carries one maternal and one paternal genome, and her brothers carry only a maternal genome. A gene drawn from the worker is maternal with probability 1/2 and is then shared with a given brother with probability 1/2, giving 1/4. A drone's only genome is maternal, and each of its genes is present in a given sister with probability 1/2. Simulation of 1M draws gives 0.250 and 0.500 (`verify/set10_bee.py`).
Likely wrong answers: one symmetric value for both directions (1/4 or 1/2), or 3/4, which is the worker-to-sister value.

## Q2
A female kangaroo is heterozygous for two electrophoretic variants of the X-linked enzyme phosphoglycerate kinase (PGK1). She received variant A from her mother and variant B from her father. Which variants are expected in her red blood cells?

Answer: almost only variant A.

In marsupials X inactivation is imprinted: the paternal X is inactivated in every cell rather than at random. Her somatic cells therefore express the maternal variant, A. Silencing of the paternal X is incomplete for some genes and tissues, so weak B activity can appear in some tissues, but no 50:50 mosaic is expected. Kangaroo PGK1 variants were among the first evidence for this paternal inactivation (Cooper and colleagues, early 1970s).
Likely wrong answer: a mosaic of A and B cells in roughly equal proportions, as in eutherian random X inactivation.
