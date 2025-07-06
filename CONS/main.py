"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

"""

from collections import Counter

dna_strings = []
with open("data.fasta", "r") as f:
    for line in f:
        if line[0] == ">":
            continue
        dna_strings.append(line.strip())


def profile_matrix(dna_strings):
    transposed = list(zip(*dna_strings))
    size = len(dna_strings[0])
    profile = {"A":[0]*size, "C":[0]*size,"G":[0]*size, "T":[0]*size}
    for i in range(len(transposed)):
        for char in transposed[i]:
            profile[char][i]+=1
    return profile


import numpy as np

def consensus(profile):
    out = ""
    for i in range(len(profile["A"])):
        out += max(profile, key= lambda k:profile[k][i])
        
    return out


profile = profile_matrix(dna_strings)
print(profile)
print(consensus(profile))