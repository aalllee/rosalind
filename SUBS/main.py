
"""
Given: Two DNA strings s and t (each of length at most 1 kbp).
Return: All locations of t as a substring of s.
"""



s ="GATATATGCATATACTT"
t = "ATAT"

def find_substrings(s,t):
    len_t, len_s = len(t), len(s)
    out = []
    for i in range(len_s-len_t+1):
        if s[i:len_t+i] == t: 
            out.append(i)
    return out

print(find_substrings(s,t))