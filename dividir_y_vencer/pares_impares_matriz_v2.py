def count(matrix, start_row=None, end_row=None, start_column=None, end_column=None):
    if start_row is None:
        start_row = 0
        end_row = len(matrix)-1
        start_column = 0
        end_column = len(matrix)-1
    if start_row == end_row and start_column == end_column:
        num = matrix[start_row][start_column]
        if num % 2 == 0:
            return (num, 1, 0)
        else:
            return (num, 0, 1)
    mid_row = (start_row + end_row) // 2
    mid_column = (start_column + end_column) // 2
    p1 = count(matrix, start_row, mid_row, start_column, mid_column)
    p2 = count(matrix, start_row, mid_row, mid_column+1, end_column)
    p3 = count(matrix, mid_row+1, end_row, start_column, mid_column)
    p4 = count(matrix, mid_row+1, end_row, mid_column+1, end_column)
    sum = p1[0] + p2[0] + p3[0] + p4[0]
    even = p1[1] + p2[1] + p3[1] + p4[1]
    odd = p1[2] + p2[2] + p3[2] + p4[2]
    return (sum, even, odd)

print(count([[1,2,3,4],  # -> (136,8,8)
             [5,6,7,8],
             [9,10,11,12],
             [13,14,15,16]]))