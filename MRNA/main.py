

"""
Given: A protein string of length at most 1000 aa.

Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000. (Don't neglect the importance of the stop codon in protein translation.)
"""


codon_table = {
    'F': 2, 'L': 6, 'S': 6, 'Y': 2, 'C': 2, 'W': 1, 'P': 4,
    'H': 2, 'Q': 2, 'R': 6, 'I': 3, 'M': 1, 'T': 4, 'N': 2,
    'K': 2, 'V': 4, 'A': 4, 'D': 2, 'E': 2, 'G': 4
}

protein = "MA"

RNA_string_count = 1
for aa in protein:
    RNA_string_count*=codon_table[aa]

#times 3 for 3 different stop codons per RNA
res = (RNA_string_count*3)%1000000
print(res)