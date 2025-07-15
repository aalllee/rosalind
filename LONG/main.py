

data = ["ATTAGACCTG","CCTGCCGGAA","AGACCTGCCG","GCCGGAATAC"]


def check_overlap(s1,s2):
    min_length = min(len(s1),len(s2))
    res = s1+s2
    max_overlap = 0
    for i in range(min_length,0,-1):
        if s1[-i:] == s2[:i]:
            res = s1 + s2[i:]
            max_overlap = i
            break

    

    for i in range(min_length,0,-1):
        if i <= max_overlap:
            break
        if s1[:i] == s2[-i:]:
            res = s2+s1[i:]
            break

    return res, max_overlap
        


def shortest_superstring(data):
    data = list(data)
    while len(data) > 1:
        max_overlap = 0
        best_match = (0,1)
        res = ""

        for i in range(len(data)):
            for j in range(i+1,len(data)):
                str, overlap = check_overlap(data[i],data[j])
                if overlap > max_overlap:
                    max_overlap = overlap
                    best_match= (i,j)
                    res = str

        updated_data = []
        for i in range(len(data)):
            if i != best_match[0] and i != best_match[1]:
                updated_data.append(data[i])
       
        updated_data.append(res)
        data = updated_data
    
    return data[0]

        



print(shortest_superstring(data))
                