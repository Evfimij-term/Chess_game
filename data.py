from classes import The_selected_piece

chess_board = [["." for _ in range(8)] for _ in range(8)]
for i in range(8):
    if i == 0 or i == 7:
        chess_board[0][i] = "Л"
        chess_board[7][i] = "Л"
        chess_board[1][i] = "П"
        chess_board[6][i] = "П"
    elif i == 1 or i == 6:
        chess_board[0][i] = "К"
        chess_board[7][i] = "К"
        chess_board[1][i] = "П"
        chess_board[6][i] = "П"
    elif i == 2 or i == 5:
        chess_board[0][i] = "С"
        chess_board[7][i] = "С"
        chess_board[1][i] = "П"
        chess_board[6][i] = "П"
    elif i == 3:
        chess_board[0][i] = "Ф"
        chess_board[7][i] = "Ф"
        chess_board[1][i] = "П"
        chess_board[6][i] = "П"
    else:
        chess_board[0][i] = "Кр"
        chess_board[7][i] = "Кр"
        chess_board[1][i] = "П"
        chess_board[6][i] = "П"

selected_piece = The_selected_piece()