#Sudoku program to work on backtracking

grid = [
    [0,0,6,0,9,0,2,0,0],
    [9,0,0,3,0,0,8,0,0],
    [0,0,0,0,0,0,0,0,4],
    [0,0,2,0,0,0,4,8,7],
    [7,0,4,0,0,6,0,0,0],
    [0,0,0,0,0,2,0,0,0],
    [1,0,0,0,3,0,0,0,0],
    [6,3,0,0,0,0,0,5,0],
    [0,5,8,0,0,0,0,7,2]
]

#so in sudoku you can't have the same number in the same row or column or in the 3x3 square
#x is the row aka the y coord 
#y is the column aka the x coord
def solve(board):
    emptySpace = findEmpty(board)
    #if there is no empty space it is solved
    if not emptySpace:
        return True
    row = emptySpace[0]
    col = emptySpace[1]
    
    #recursion and backtracking
    for i in range(1,10):
        if assignPossible(row, col, i, board):
            board[row][col] = i

            if solve(board):
                return True
            #if there is non valid solution in the recursion stack we make that space 0 and go back
            board[row][col] = 0
    return False

def assignPossible(row, column, num, board):
    #so we check the row first
    for i in range(9):
        if board[row][i] == num and column != i:
            return False
    #check column
    for i in range(9):
        if board[i][column] == num and row != i:
            return False
    #check box


    for i in range(row, row):
        for j in range(column, column):
            if board[i][j] == num and row != i and column != j:
                return False
    return True 
    

def findEmpty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j) #row then column
    return None

#function to check if the number is in row
def notInRow(row, column, num, board):
    for i in range(9):
        if board[row][i] == num and column != i:
            return False
    return True

#function to check if number is in column
def notInCol(row, column, num, board):
    for i in range(9):
        if grid[i][column] == num and row != i:
            return False
    return True

def notInBox(row, column, num, board):
    for i in range(3):
        for j in range(3):
            if(board[row + i][column + j] == num):
                return False
    return True

#function to check if the space is empty
def findEmpty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j) #row then column
    return None

#to print the board 
def printGrid(board):
    for i in range(9):
        if i%3 == 0 and i != 0:
            print('')   
        for j in range(9):
            if j%3 == 0 and i >= 0:
                print(' ', end='')
            if j == 8:
                print(str(board[i][j]) +' ')
            else:
                print(str(board[i][j]) + ' ', end='')


printGrid(grid)
solve(grid)
print("\n")
print("Solution: \n")
printGrid(grid)
