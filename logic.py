from data import chess_board
from data import selected_piece

def print_board(chess_board):
    for i in range(8):
        line = ""
        for j in range(8):
            line += chess_board[i][j].type + " "
        print(line)

def click_handling_on_board(x, y):
    if selected_piece.is_selected == True and x != selected_piece.where_selected[0] and y != selected_piece.where_selected[1]:
        check_piece(x, y)
    elif selected_piece.is_selected == False and chess_board[y][x].type != ".":
        selected_piece.is_selected = True
        selected_piece.what_selected = chess_board[y][x]
        selected_piece.where_selected[0] = x
        selected_piece.where_selected[1] = y

def check_piece(x, y):
    check_L(x, y)

def check_L(x, y):
    if selected_piece.what_selected == "Л":
        x0 = selected_piece.where_selected[0]
        y0 = selected_piece.where_selected[1]
        if x0 == x:
            row = chess_board[y]
            left, right = min(x0, x), max(x0, x)
            sub_row = row[left + 1:right]
            if len(sub_row) == 0 and chess_board[y][x].type == ".":
                chess_board[y][x], chess_board[y0][x0] = chess_board[y0][x0], chess_board[y][x]
            elif len(sub_row) == 0 and chess_board[y][x].type != "." and chess_board[y][x].color != chess_board[y0][x0].color:
                chess_board[y][x].type = chess_board[y0][x0].type
                chess_board[y][x].color = chess_board[y0][x0].color
                chess_board[y0][x0].type = "."
                chess_board[y0][x0].color = "nothing"
            elif all(x.type == "." for x in sub_row) and (chess_board[y][x].type == "." or chess_board[y][x].color != chess_board[y0][x0].color):
                chess_board[y][x].type = chess_board[y0][x0].type
                chess_board[y][x].color = chess_board[y0][x0].color
                chess_board[y0][x0].type = "."
                chess_board[y0][x0].color = "nothing"