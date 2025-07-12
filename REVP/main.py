
"""
Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

"""


data = "TCAATGCATGCGGGTCTATATGCAT"

complement = str.maketrans('ACGT', 'TGCA')
def reverse_palindrome(dna,min,max):
    for l in range(min,max):
        for i in range(0,len(dna)-l):
            substr = dna[i:i+l] 
            if substr == substr.translate(complement)[::-1]:
                print(i+1, " ", l)


reverse_palindrome(data,4,12)