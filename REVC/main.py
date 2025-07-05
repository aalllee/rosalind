"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s
 is the string sc
 formed by reversing the symbols of s
, then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s
 of length at most 1000 bp.

Return: The reverse complement sc
 of s
.
"""

def modify_char(char):
    if char == 'A':
        return 'T'
    elif char == 'C':
        return 'G'
    elif char == 'T':
        return 'A'
    elif char == 'G':
        return 'C'
    else:
        return char

def reverse_complement(s):
    reverse = s[::-1]
    reverse_complement = "".join([modify_char(char) for char in reverse])
    return reverse_complement


print(reverse_complement("AAAACCCGGT"))

