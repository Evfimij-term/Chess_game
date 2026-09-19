def print_board(chess_board):
    for i in range(8):
        line = ""
        for j in range(8):
            line += chess_board[i][j] + " "
        print(line)