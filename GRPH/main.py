
"""
For a collection of strings and a positive integer k the overlap graph for the strings is a directed graph Ok
in which each string is represented by a node, and string s is connected to string t with a directed edge when there is a length k
suffix of s that matches a length k prefix of t, as long as s≠t; we demand s≠t
to prevent directed loops in the overlap graph (although directed cycles may be present).

Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.

"""


sequences = {}

key = ""


with open("data.fasta","r") as f:
    for line in f:
        line = line.strip()
        if line[0]  == ">":
            key = line[1:]
        else:
            sequences[key] = line


adjacency_list = []
for key, value in sequences.items():
    for key2, value2 in sequences.items():
        #print(value, " ", value2)
        if value == value2: 
            continue
        if value[-3:] == value2[:3]:
            adjacency_list.append([key,key2])
            #adjacency_list[key] = key2

print(adjacency_list)