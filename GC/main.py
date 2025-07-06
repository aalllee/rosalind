"""
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used method of string labeling is called FASTA format. In this format, the string is introduced by a line that begins with '>', followed by some labeling information. Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 
"""

from collections import Counter

seq_id = ""
gc_content = 0

def gc_percentage(s):
    freq = Counter(s)
    count = freq['G'] + freq["C"]
    ratio  =  count / len(s) 
    return ratio


temp_id = ""

with open("sample_data.fasta", "r") as file:
    for line in file:
        line = line.strip()
        
        if line[0] == ">":
            temp_id = line[1:]
            continue


        new_gc_content = gc_percentage(line)

        if new_gc_content > gc_content:
            gc_content = new_gc_content
            seq_id = temp_id

        print(line)
    

print(seq_id, "has the highest GC content of", gc_content*100, "percent")


