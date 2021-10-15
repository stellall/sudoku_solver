from pprint import pprint

def find_next_space(puzzles):
    for r in range(9):
        for c in range(9): 
            if puzzles[r][c] == -1:
                return r, c
    return None, None  

def is_valid(puzzles, guess, row, column):
    row_values = puzzles[row]
    if guess in row_values:
        return False 
    col_values = [puzzles[i][column] for i in range(9)]
    if guess in col_values:
        return False
    row_start = (row // 3) * 3 
    column_start = (column // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(column_start, column_start + 3):
            if puzzles[r][c] == guess:
                return False
    return True

def sudoku_slover(puzzles):
    row, column = find_next_space(puzzles)
    if row is None:  
        return True 
    
    for guess in range(1, 10): 
        if is_valid(puzzles, guess, row, column):
            puzzles[row][column] = guess
            if sudoku_slover(puzzles):
                return True
        puzzles[row][column] = -1
    return False

if __name__ == '__main__':
    board = [
        [-1, -1, 6, 8, 5, 1, -1, -1, -1],
        [3, 4, -1, 9, -1, 6, 8, -1, -1],
        [-1, -1, -1, 4, 7, 3, 2, 5, 6],
        [4, -1, 9, 6, -1, -1, -1, 3, -1],
        [-1, -1, -1, -1, -1, -1, 5, 9, 8],
        [-1, -1, 8, 2, 1, -1, -1, 6, -1],
        [-1, 1, -1, 5, 6, 8, 4, -1, -1],
        [-1, -1, -1, 3, 4, -1, -1, -1, -1],
        [-1, -1, -1, 1, 9, 7, 6, -1, 3]
    ]
    print(sudoku_slover(board))
    pprint(board)
