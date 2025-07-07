

"""
Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
"""

def mortal_fibonacci_rabits(n,m):

    mem = [0]*n

    mem[0] = 1
    mem[1] = 1

    born= [0]*n
    born[0] =1

    for i in range(2,n):
        born[i] = mem[i-1]-born[i-1]
        dead = 0
        if i >= m:
            dead = born[i-m]

        mem[i] = mem[i-1] - dead + (mem[i-1]-born[i-1]) 

    return mem

print(mortal_fibonacci_rabits(13,5))

