


"""
Given: Two positive integers k(k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.

"""

import math

def binomial_pmf(n, p, x):
    binom_coeff = math.comb(n, x)
    return binom_coeff * (p ** x) * ((1 - p) ** (n - x))

def binomial_cdf(n, p, k):
    cdf = 0
    for x in range(k):
        cdf += binomial_pmf(n, p, x)
    return cdf


k = 2
n = 2**k
N = 1
p = 0.25


#P(X>=N)
print(1-binomial_cdf(n,p,N))

