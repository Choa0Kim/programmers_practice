def solution(sizes):
    # print(sizes)
    max_i = 0
    max_j = 0
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
            
        if sizes[i][0] >= max_i:
            max_i = sizes[i][0]
        
        if sizes[i][1] >= max_j:
            max_j = sizes[i][1]
    return max_i * max_j
