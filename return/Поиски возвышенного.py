def find_mountain(matrix):
    out = (0, (0, 0))
    for row in range(len(matrix)):
        for cell in range(len(matrix[row])):
            if matrix[row][cell] > out[0]:
                out = (matrix[row][cell], (row, cell))
    return out[1]
