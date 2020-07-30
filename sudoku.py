import numpy
import random

board = [[0,0,8,0,0,0,0,0,0],
         [4,9,0,1,5,7,0,0,2],
         [0,0,3,0,0,4,1,9,0],
         [1,8,5,0,6,0,0,2,0],
         [0,0,0,0,2,0,0,6,0],
         [9,6,0,4,0,5,3,0,0],
         [0,3,0,0,7,2,0,0,4],
         [0,4,9,0,3,0,0,5,7],
         [8,2,7,0,0,9,0,1,3]]

board = [[8,5,1,7,9,6,2,4,3],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0]]

created_board1 = [[8, 5, 1, 7, 9, 6, 2, 4, 3],
                  [2, 3, 4, 1, 5, 8, 6, 7, 9],
                  [6, 7, 9, 2, 3, 4, 1, 5, 8],
                  [1, 2, 3, 4, 6, 5, 8, 9, 7],
                  [4, 6, 5, 8, 7, 9, 3, 1, 2],
                  [7, 9, 8, 3, 1, 2, 4, 6, 5],
                  [3, 1, 2, 5, 4, 7, 9, 8, 6],
                  [5, 4, 6, 9, 8, 3, 7, 2, 1],
                  [9, 8, 7, 6, 2, 1, 5, 3, 4]]

test_solve = [[0, 0, 0, 7, 9, 6, 0, 4, 0],
              [2, 3, 4, 0, 5, 0, 0, 0, 9],
              [6, 0, 9, 2, 0, 0, 1, 5, 0],
              [1, 2, 0, 4, 6, 5, 0, 9, 0],
              [0, 6, 5, 8, 7, 0, 3, 1, 0],
              [0, 9, 8, 3, 1, 0, 4, 6, 0],
              [0, 1, 2, 5, 0, 0, 0, 0, 6],
              [0, 4, 6, 0, 8, 0, 7, 0, 0],
              [9, 8, 0, 0, 2, 1, 5, 0, 4]]


def possible(y, x, n, sudoku_board):
    for i in range(0, 9):
        if sudoku_board[y][i] is n:
            return False
    for i in range(0, 9):
        if sudoku_board[i][x] is n:
            return False
    x_grid = (x // 3) * 3
    y_grid = (y // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku_board[y_grid + i][x_grid + j] is n:
                return False
    return True

def solve(sudoku_board):
    for y in range(9):
        for x in range(9):
            if sudoku_board[y][x] is 0:
                for n in range(1, 10):
                    if possible(y, x, n, sudoku_board):
                        sudoku_board[y][x] = n
                        solve(sudoku_board)
                        sudoku_board[y][x] = 0
                
                return
    
    print(f"Board\n\n{numpy.matrix(sudoku_board)}")
    input("Board Created!")
solve(test_solve)

def create_game(sudoku_board):
    for y in range(9):
        for x in range(9):
            if sudoku_board[y][x] is 0:
                for n in range(1, 10):
                    if possible(y, x, n, sudoku_board):
                        sudoku_board[y][x] = n
                        create_game(sudoku_board)
                        sudoku_board[y][x] = 0

                return sudoku_board
    print(f"New Sudoku Board Created!\n\n{numpy.matrix(sudoku_board)}")
    input("Merp Merp")

# x = create_game(board)
# print(f"Created a new board! {x}")

def remove_numbers(grid):
    amount = [3, 4, 5]
    for i in range(9):
        remove = random.choice(amount)
        options = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for _ in range(remove):
            choice = random.choice(options)
            options.remove(choice)
            grid[i][choice] = 0

    return grid

# x = remove_numbers(created_board1)
# print(f"Created a new board!\n\n{numpy.matrix(x)}\n\n")
