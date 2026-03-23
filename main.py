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

    for symbol in ["O", "X"]:

        for y in range(len(board)):
            for x in range(len(board[0])-in_a_row + 1):
                check_segment = board[y][x : x + in_a_row]
                if check_segment.count(symbol) == in_a_row -1 and check_segment.count("") >= 1:
                    empty_square_index = check_segment.index("")
                    return y, x + empty_square_index
        
        for y in range(len(board) - in_a_row + 1):
            for x in range(len(board[0])):
                check_segment = []
                for i in range(in_a_row):
                    check_segment.append(board[y+i][x])
                if check_segment.count(symbol) == in_a_row -1 and check_segment.count("") >= 1:
                    empty_square_index = check_segment.index("")
                    return y + empty_square_index, x

 
if __name__ == "__main__":
    main()
