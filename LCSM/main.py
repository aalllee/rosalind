
"""
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.

Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

"""
sequences = []
with open("data.fasta", "r") as f:
    for line in f:
        if line[0] == ">":
            continue
        else:
            sequences.append(line.strip())

print(sequences)


def has_common_substring(strings, length):
    substrings = set()
    first = strings[0]
    
    for i in range(len(first) - length + 1):
        substrings.add(first[i:i+length])
    
    for s in strings[1:]:
        current_subs = set()
        for i in range(len(s) - length + 1):
            sub = s[i:i+length]
            if sub in substrings:
                current_subs.add(sub)
        substrings = current_subs
        if not substrings:
            return ""
    
    return sorted(substrings)[0] if substrings else ""

def longest_common_substring(strings):
    low, high = 0, len(strings[0])
    result = ""
    
    while low <= high:
        mid = (low + high) // 2
        candidate = has_common_substring(strings, mid)
        if candidate:
            result = candidate
            low = mid + 1 
        else:
            high = mid - 1
            
    return result


print(longest_common_substring(sequences))
