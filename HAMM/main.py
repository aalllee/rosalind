"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t), is the number of corresponding symbols that differ in s and t

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t)

"""


s1 = "GAGCCTACTAACGGGAT"
s2 = "CATCGTAATGACGGCCT"

def hamming_distance(s1,s2):
    return sum(c1!=c2 for c1,c2 in zip(s1,s2))

print(hamming_distance(s1,s2))