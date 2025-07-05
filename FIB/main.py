"""
Given: Positive integers n≤40 and k≤5.

Return: The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k
 rabbit pairs (instead of only 1 pair).


n: Number of months (positive integer ≤ 40).

k: The number of rabbit pairs produced by each reproduction-age pair (positive integer ≤ 5).

We start with 1 pair of rabbits.

In each subsequent month, every pair of rabbits that is at least two months old produces k new pairs.
"""


def reproduction_count(n,k):
    month_count = [0] * n

    month_count[0] = 1
    month_count[1] = 1

    for i in range(2,n):
        month_count[i] = month_count[i-1] + month_count[i-2] * k

    return month_count[n-1]

print(reproduction_count(5,3))
