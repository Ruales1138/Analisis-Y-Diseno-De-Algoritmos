def is_valid(matrix, sum_r, sum_c):
    for i, row in enumerate(matrix):
        if sum(row) > sum_r[i]:
            return False
    for i in range(len(matrix)):
        sum_c_2 = 0
        for j in range(len(matrix)):
            sum_c_2 += matrix[j][i]
        if sum_c_2 > sum_c[i]:
            return False
    return True

def kakudem(sum_r=None, sum_c=None, n=None, matrix = None, i = 0, j = 0, used_num = set()):
    if n is None:
        n = len(sum_r)
    if matrix is None:
        matrix = [[0]*n for _ in range(n)]
    if i == n:
        print(matrix)
        return True
    if j == n:
        return kakudem(sum_r, sum_c, n, matrix, i+1, 0, used_num)
    for option in range(1, (n**2)+1):
        if option in used_num:
            continue
        matrix[i][j] = option
        used_num.add(option)
        if is_valid(matrix, sum_r, sum_c):
            if kakudem(sum_r, sum_c, n, matrix, i, j+1, used_num):
                return True
        matrix[i][j] = 0
        used_num.remove(option)
    return False

print(kakudem([14,15,16], [18,13,14]))   # [[1, 6, 7], 
                                            #  [9, 2, 4], 
                                            #  [8, 5, 3]]
print(kakudem([16,12,17], [12,15,18], n=None, matrix=None, i=0, used_num=set()))   