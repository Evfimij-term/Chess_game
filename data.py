from classes import The_selected_piece
from classes import Piece

chess_board = [[Piece() for _ in range(8)] for _ in range(8)]
for i in range(8):
    if i == 0 or i == 7:
        chess_board[0][i].type, chess_board[0][i].color = "Л", "black"
        chess_board[7][i].type, chess_board[0][i].color = "Л", "white"
        chess_board[1][i].type, chess_board[1][i].color = "П", "black"
        chess_board[6][i].type, chess_board[6][i].color = "П", "white"
    elif i == 1 or i == 6:
        chess_board[0][i].type, chess_board[0][i].color = "К", "black"
        chess_board[7][i].type, chess_board[7][i].color = "К", "white"
        chess_board[1][i].type, chess_board[1][i].color = "П", "black"
        chess_board[6][i].type, chess_board[6][i].color = "П", "white"
    elif i == 2 or i == 5:
        chess_board[0][i].type, chess_board[0][i].color = "С", "black"
        chess_board[7][i].type, chess_board[7][i].color = "С", "white"
        chess_board[1][i].type, chess_board[1][i].color = "П", "black"
        chess_board[6][i].type, chess_board[6][i].color = "П", "white"
    elif i == 3:
        chess_board[0][i].type, chess_board[0][i].color = "Ф", "black"
        chess_board[7][i].type, chess_board[7][i].color = "Ф", "white"
        chess_board[1][i].type, chess_board[1][i].color = "П", "black"
        chess_board[6][i].type, chess_board[6][i].color = "П", "white"
    else:
        chess_board[0][i].type, chess_board[0][i].color = "Кр", "black"
        chess_board[7][i].type, chess_board[7][i].color = "Кр", "white"
        chess_board[1][i].type, chess_board[1][i].color = "П", "black"
        chess_board[6][i].type, chess_board[6][i].color = "П", "white"

selected_piece = The_selected_piece()