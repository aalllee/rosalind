"""
An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

Given a DNA string t
 corresponding to a coding strand, its transcribed RNA string u
 is formed by replacing all occurrences of 'T' in t
 with 'U' in u
.

Given: A DNA string t
 having length at most 1000 nt.

Return: The transcribed RNA string of t
.
"""

sample_data = "GATGGAACTTGACTACGTAAATT"

output_data = ""
for char in sample_data:
    if char == "T":
        output_data += "U"
    else:
        output_data += char

print(output_data)
