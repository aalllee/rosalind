#Counting nucleotides

with open('rosalind_dna.txt', 'r') as file:
    content = file.read()


count = [0,0,0,0]
for nucleotide in content:
    if nucleotide == "A":
        count[0] += 1
    if nucleotide == "C":
        count[1] += 1
    if nucleotide == "T":
        count[2] += 1
    if nucleotide == "G":
        count[3] += 1

print(count)