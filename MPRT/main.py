
import re
import requests

def fetch_fasta(accession):
    url = f'https://www.uniprot.org/uniprot/{accession}.fasta'
    r = requests.get(url)
    lines = r.text.splitlines()
    seq = ''.join([line.strip() for line in lines if not line.startswith('>')])
    return seq


uniProtIDs = ["A2Z669","B5ZC00","P07204","P20840"]

protein_motif_expression = r'N[^P][ST][^P]'

def find_motif_positions(proteinIDs, motif_expression):
    
    pattern = re.compile(protein_motif_expression)

    protein = ""
    for id in proteinIDs:
        protein = fetch_fasta(id)
        matches = list(pattern.finditer(protein))
        if len(matches)==0:
            continue

        print(id, ":")
        for match in matches:
            print(match.start() + 1, end=" ")

        print("")

find_motif_positions(uniProtIDs, protein_motif_expression)

