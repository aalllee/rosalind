"""
Given: Two DNA strings s1 and s2 of equal length (at most 1 kbp).

Return: The transition/transversion ratio R(s1,s2).

"""

def tt_ratio(s1,s2):
    A_G_sum = ord('A') + ord('G')  
    C_T_sum = ord('C') + ord('T') 
    A_C_sum = ord('A')+ord('C')
    A_T_sum = ord('A')+ord('T')
    G_C_sum = ord('G')+ord('C')
    G_T_sum = ord('G')+ord('T')

    transitions = 0
    transversions = 0
    for i in range(len(s1)):
        sum = ord(s1[i])+ord(s2[i])
        if sum == A_G_sum or sum == C_T_sum:
            transitions+=1
        elif sum == A_C_sum or sum == A_T_sum or sum == G_C_sum or sum == G_T_sum:
            transversions+=1
    
    return transitions/transversions


s1 = "GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT"
s2 = "TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT"
print(tt_ratio(s1,s2))

