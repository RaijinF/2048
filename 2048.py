import random

#-------------------------------board

def init_board(board, size):
    for i in range(size):
        row = []
        for j in range(size):
            row.append("")
        board.append(row)
        
def print_board(board):
    for row in board:
        for elem in row:
            print(f"[{elem : ^4}]", end="")
        print()


#-----------------------------num gen

def gen_cor(size):
    x_cor = random.randint(0, size-1)
    y_cor = random.randint(0, size-1)
    return x_cor, y_cor
    
def is_cor_free(board, x_cor, y_cor):
    return board[x_cor][y_cor] == ""

def gen_num():
    next_num=[2,2,2,4,2,2,4,2,2,2]
    random_index = random.randint(0, 9)
    return next_num[random_index]     

def next_num(size, board):
    num = gen_num()
    x, y = gen_cor(size)
    while not is_cor_free(board, x, y): # while not "true" jump 38, while not "false" jump 39
        x, y = gen_cor(size)
    board[x][y] = num
    
def init_num(board, size):
    x1, y1 = gen_cor(size)
    board[x1][y1] = 2
    x2, y2 = gen_cor(size)
    while not is_cor_free(board, x2, y2):
        x2, y2 = gen_cor(size)
    board[x2][y2] = 2
       
#------------------------------------------- Move    

def move_up(board,size):
    for i in range(1, size):
        for j in range(0, size):
            if board[i][j] != "" and board[i][j] == board[i-1][j]:
                board[i-1][j] = board[i-1][j] + board[i][j]
                board[i][j] = ""
            elif board[i][j] != "" and board[i-1][j] == "":
                board[i-1][j] = board[i][j]
                board[i][j] = ""

def move_down(board, size):
    for i in reversed(range(0, size-1)):
        for j in range(0, size):
            if board[i][j] != "" and board[i][j] == board[i+1][j]:
                board[i+1][j] = board[i+1][j] + board[i][j]
                board[i][j] = ""
            elif board[i][j] != "" and board[i+1][j] == "":
                board[i+1][j] = board[i][j]
                board[i][j] = ""

def move_left(board, size):
    for i in range(0, size):
        for j in range(1, size):
            if board[i][j] != "" and board[i][j] == board[i][j-1]:
                board[i][j-1] = board[i][j-1] + board[i][j]
                board[i][j] = ""
            elif board[i][j] != "" and board[i][j-1] == "":
                board[i][j-1] = board[i][j]
                board[i][j] = ""

def move_right(board, size):
    for i in range(0, size):
        for j in reversed(range(0, size-1)):
            if board[i][j] != "" and board[i][j] == board[i][j+1]:
                board[i][j+1] = board[i][j+1] + board[i][j]
                board[i][j] = ""
            elif board[i][j] != "" and board[i][j+1] == "":
                board[i][j+1] = board[i][j]
                board[i][j] = ""
                

def move_cont(board, size, dir):
    if dir.lower() == "w":
        move_up(board, size)
    if dir.lower() == "s":
        move_down(board, size)
    if dir.lower() == "a":
        move_left(board, size)
    if dir.lower() == "d":
        move_right(board, size)
    
    
            
def main():
    size = 4
    board = []
    init_board(board, size)
    init_num(board, size)
    print_board(board)
    move_cont(board, size, input())
    
    print_board(board)
    
if __name__ == "__main__":
    main()