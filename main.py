sudoku = [
    [8, 0, 0, 0, 0, 0, 0, 0, 4],
    [0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

def print_sudoku(sudoku):
    for row in sudoku:
        row = [str(value) for value in row]
        print('| ' + ' | '.join(row) + ' |')

def is_solved(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True


def is_valid(sudoku, row_pos, column_pos, value):
    row = sudoku[row_pos]
    if value in row:
        return False
    column = [sudoku[i][column_pos] for i in range(9)]
    if value in column:
        return False
    
    row_init = row_pos // 3 * 3
    column_init = column_pos // 3 * 3
    row_end = row_init + 2
    column_end = column_init + 2
    grid = [sudoku[i][j] for j in range(column_init, column_end + 1) for i in range(row_init, row_end + 1)]
    if value in grid:
        return False

    return True

def find_first_pos(sudoku):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return i, j
    return -1, -1

def solve(sudoku):
    if is_solved(sudoku):
        return sudoku
    row, col = find_first_pos(sudoku)
    for num in range(1, 10):
        if is_valid(sudoku, row, col, num):
            sudoku[row][col] = num
            result = solve(sudoku)
            if result is not None:
                return result
            sudoku[row][col] = 0
    return None

print_sudoku(solve(sudoku))