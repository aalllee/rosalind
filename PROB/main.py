
import math
dna = "ACGATACAA"

A = [0.129 ,0.287, 0.423, 0.476, 0.641, 0.742, 0.783]


def p_random_string(dna, A):
    for gc in A:
        p_gc = gc/2
        p_at = (1-gc)/2
        p = 1
        for base in dna:
            if base in "CG":
                p*=p_gc
            else:
                p*=p_at
        
        print(math.log10(p))


    

p_random_string(dna,A)      


