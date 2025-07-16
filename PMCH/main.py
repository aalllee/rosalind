"""
Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.
"""
import math

def perfect_matchings(s):
    ct_a = s.count("A")
    ct_g = s.count("G")

    return math.factorial(ct_a)*math.factorial(ct_g)


data = "AGCUAGUCAU"
print(perfect_matchings(data))

