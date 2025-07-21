"""
Given: Two DNA strings s and t (each of length at most 1 kbp) in FASTA format.

Return: One collection of indices of s in which the symbols of t appear as a subsequence of s. If multiple solutions exist, you may return any one.
"""


def spliced_motif(s,t):
    i = 0
    indices = []
    for j in range(len(s)):
        if s[j] == t[i]:
            indices.append(j+1)
            i+=1
        
        if i == len(t):
            break
    return indices

    
s = "ACGTACGTGACG"
t = "GTA"
print(spliced_motif(s,t))
        
