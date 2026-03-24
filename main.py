import random
import re

from tkinter import *
from tkinter import ttk

def main():
    in_a_row = 3
    board = [["","",""],["","",""],["","",""]]
    for _ in range(5):

        for row in board:
            print(f"|{row[0]}|{row[1]}|{row[2]}|")

        y_input = int(input("Place X at row: ")) -1
        x_input = int(input("Place X at calumn: ")) -1
        
        board[y_input][x_input] = "X"

        if check_victory(board):
            for row in board:
                print(f"|{row[0]}|{row[1]}|{row[2]}|")

            print("Victory royal!")
            return

        enemy_y, enemy_x = enemy_function(board, in_a_row)
        board[enemy_y][enemy_x] = "O"

        if check_victory(board):
            for row in board:
                print(f"|{row[0]}|{row[1]}|{row[2]}|")

            print("Looser!")
            return


def turn_to_column(board):
    columns = []
    for row in board:
        columns.append([])
    for row in board:
        for i, symbol in enumerate(row):
            columns[i].append(symbol)
    return columns

def turn_to_diagonal(board):
    diagonals = [[], []]
    for i, row in enumerate(board):
        diagonals[0].append(row[i])
    i = 2
    for row in board:
        diagonals[1].append(row[i])
        i -= 1
    return diagonals

#Change victory cond check to be viable in bigger scale boards
def check_victory(board):

    for row in board:
        if len(set(row)) == 1 and row[0] != "":
            return True

    for column in turn_to_column(board):
        if len(set(column)) == 1 and column[0] != "":
            return True


    for diagonal in turn_to_diagonal(board):
        if len(set(diagonal)) == 1 and diagonal[0] != "":
            return True

    return False


def enemy_function(board, in_a_row):
    best_moves = []
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for symbol in ["O", "X"]:

        for y in range(len(board)):
            for x in range(len(board[0])):
                for dy, dx in directions:
                    end_y = y + (in_a_row - 1) * dy
                    end_x = x + (in_a_row - 1) * dx
                    if 0 <= end_y < len(board) and 0 <= end_x < len(board[0]):
                        segment = [board[y + i*dy][x + i*dx] for i in range(in_a_row)]
                        if segment.count(symbol) == in_a_row -1 and segment.count("") >= 1:
                            empty_square_index = segment.index("")
                            return y + empty_square_index*dy, x + empty_square_index*dx
                        elif segment.count(symbol) > 0 and segment.count("") > 0 and len(set(segment)) == 2:
                            symbol_value = 0
                            if symbol == "O":
                                symbol_value = 1
                            empty_square_index = segment.index("")
                            best_moves.append((segment.count(symbol), symbol_value, y + empty_square_index*dy, x + empty_square_index*dx))

    if len(best_moves) >= 1:
        best_move = max(best_moves)
        return best_move[2], best_move[3]

    center = len(board)//2
    if len(board)%2 == 1:
        if board[center][center] == "":
            return center, center
    else:
        corners = [(0,0), (0, len(board)-1), (len(board)-1, 0), (len(board)-1, len(board)-1)]
        for y, x in corners:
            if board[y][x] == "":
                return y, x

 
if __name__ == "__main__":
    main()
