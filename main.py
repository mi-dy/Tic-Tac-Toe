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

        x_input = int(input("Place X at row: ")) -1
        y_input = int(input("Place X at calumn: ")) -1
        
        board[x_input][y_input] = "X"

        if check_victory(board):
            for row in board:
                print(f"|{row[0]}|{row[1]}|{row[2]}|")

            print("Victory royal!")
            return

        enemy_x, enemy_y = enemy_function(board, in_a_row)
        board[enemy_x][enemy_y] = "O"

        if check_victory(board):
            for row in board:
                print(f"|{row[0]}|{row[1]}|{row[2]}|")

            print("Looser!")
            return


# Make turn functions work no matter how big is the board
def turn_to_column(board):
    columns = [[], [], []]
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
    for symbol in ["O", "X"]:
        for x, row in enumerate(board):
            for y in range(len(row)-in_a_row + 1):
                check = row[y : y + in_a_row]
                if check.count(symbol) == in_a_row -1 and check.count("") == 1:
                    empty_index = check.index("")
                    return x, y + empty_index

                    
if __name__ == "__main__":
    main()
