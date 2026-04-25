import sys

def dfs(guessIndex):
    if guessIndex == len(blanks):
        for i in sudoku:
            print(*i)

        sys.exit()
    else:
        r, c = blanks[guessIndex]
        
        for i in range(1, 10):
            if valid(r, c, i):
                dfs(guessIndex + 1)
                sudoku[r][c] = 0

def valid(r, c, guessNum):
    sudoku[r][c] = guessNum

    for i in range(9):
        if i != c and sudoku[r][i] == guessNum:
            sudoku[r][c] = 0
            return False

    for i in range(9):
        if i != r and sudoku[i][c] == guessNum:
            sudoku[r][c] = 0
            return False

    for i in range(3):
        x = i + r - (r % 3)

        for j in range(3):
            y = j + c - (c % 3)

            if (x, y) != (r, c) and sudoku[x][y] == guessNum:
                sudoku[r][c] = 0
                return False

    return True

sudoku = [list(map(int, input().split())) for i in range(9)]
blanks = [(i, j) for i in range(9) for j in range(9) if sudoku[i][j] == 0]
dfs(0)

# First Try: TLE. Copying sudoku board every time is time consuming.
# during backtrack, change the sudoku board and revert the change
# Second Try: TLE. Using 3 lists in valid and counting them was too time
# consuming.
# Third Try: AC
