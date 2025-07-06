"""
Given: Three positive integers k, m, and n, representing a population containing k+m+n 
organisms: k individuals are homozygous dominant for a factor,
m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

"""

from math import comb

def prob_dominant(k,m,n):
    num_pairs = comb(k+n+m,2)
    kk = comb(k,2)
    km = k*m
    kn = k*n
    mn = m*n*0.5
    mm = comb(m,2)*0.75
    return (kk+km+kn+mn+mm)/num_pairs

print(prob_dominant(2,2,2))