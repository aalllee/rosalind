"""
Given: A positive integer n≤10000 followed by a permutation π of length n.

Return: A longest increasing subsequence of π, followed by a longest decreasing subsequence of π.

"""

def longest_increasing(n,seq):
    longest = [1]*n
    prev = [-1]*n

    

    for i in range(n):
        for j in range(i):
            if seq[j]<seq[i] and longest[j]+1 > longest[i]:
                longest[i] = longest[j]+1
                prev[i] = j
    
    max_index = max(range(n), key = lambda i:longest[i])

    res = []
    while max_index != -1:
        res.append(seq[max_index])
        max_index = prev[max_index]


    return res[::-1]



def longest_decreasing(n,seq):
    longest = [1]*n
    prev = [-1]*n

    

    for i in range(n):
        for j in range(i):
            if seq[j]>seq[i] and longest[j]+1 > longest[i]:
                longest[i] = longest[j]+1
                prev[i] = j
    
    max_index = max(range(n), key = lambda i:longest[i])

    res = []
    while max_index != -1:
        res.append(seq[max_index])
        max_index = prev[max_index]


    return res[::-1]


print(longest_increasing(5,[5, 1, 4, 2, 3]))
print(longest_decreasing(5,[5, 1, 4, 2, 3]))
    

    