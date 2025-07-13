

"""
Given: A collection of at most 10 symbols defining an ordered alphabet, and a positive integer n (n≤10).

Return: All strings of length n that can be formed from the alphabet, ordered lexicographically (use the standard order of symbols in the English alphabet).
"""


#take the cartesian prduct of the alphabet with itself n times

from itertools import product

def all_strings(alphabet, n):
    alphabet = sorted(alphabet)
    return [''.join(p) for p in product(alphabet, repeat=n)]


print(all_strings(["A","C","G","T"],2))