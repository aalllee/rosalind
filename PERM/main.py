
"""
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
"""


def heaps_permutation(arr, n=None):
    if n is None:
        n = len(arr)
    result = []

    if n == 1:
        result.append(arr.copy())
    else:
        for i in range(n):
            result += heaps_permutation(arr, n - 1)
            if n % 2 == 0:
                arr[i], arr[n - 1] = arr[n - 1], arr[i]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]

    return result


def print_permutations(x):
    arr = list(range(1,x+1))
    res =heaps_permutation(arr)
    print(len(res))
    for perm in res:
        print("".join(str(s) for s in perm))

print_permutations(3)

