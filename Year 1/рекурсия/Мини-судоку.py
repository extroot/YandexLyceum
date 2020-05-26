def solve_sudoku(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                st = matrix[:]
                for x in get_nums(matrix, i, j):
                    st[i][j] = x
                    out = solve_sudoku(st)
                    if out:
                        for h in out:
                            print(*h)
                        break



solve_sudoku([
    [0, 0, 0, 0],
    [0, 0, 2, 0],
    [0, 1, 0, 0],
    [3, 0, 0, 4]])
