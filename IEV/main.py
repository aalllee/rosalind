"""
Given: Six nonnegative integers, each of which does not exceed 20,000. The integers correspond to the number of couples in a population possessing each genotype pairing for a given factor. In order, the six given integers represent the number of couples having the following genotypes:

1.AA-AA
2.AA-Aa
3.AA-aa
4.Aa-Aa
5.Aa-aa
6.aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, under the assumption that every couple has exactly two offspring.


"""

import numpy as np

couples = np.array([1,0,0,1,0,1])

def expected_dominant_phenotype_offspring(couples):
    expectation = np.array([1,1,1,0.75,0.5,0])
    return np.sum(2*couples*expectation)


print("number of expected offspring with dominant phenotype: ",  expected_dominant_phenotype_offspring(couples))