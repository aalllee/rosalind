
"""
Given: A positive integer n≤6.

Return: The total number of signed permutations of length n, followed by a list of all such permutations (you may list the signed permutations in any order).

"""


from itertools import permutations

def signed_permutations(n):
    result = []
    base = list(range(1, n + 1))
    for perm in permutations(base):
        for signs in range(2 ** n):
            signed_perm =[]
            for i in range(n):
                if (signs >> i) & 1:
                    signed_perm.append(-perm[i])
                else:
                    signed_perm.append(perm[i])
            result.append(signed_perm)
    return result


data = 2
res = signed_permutations(data)
print(len(res))
for p in res:
    print(p)
