def init_board(board, size):
    for i in range(size):
        row = []
        for j in range(size):
            row.append("0")
        board.append(row)
        
def print_board(board, size):
    for i in range(size):
        for j in range(size):
            print(f"[ {board[i][j]} ]", end="")
        print()
    
def main():
    size = 4
    board = []
    init_board(board, size)
    print_board(board, size)
    
if __name__ == "__main__":
    main()