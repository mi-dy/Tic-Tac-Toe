import random

from tkinter import *
from tkinter import ttk

def main():
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

        enemy_turn(board)

        if check_victory(board):
            for row in board:
                print(f"|{row[0]}|{row[1]}|{row[2]}|")

            print("Looser!")
            return


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

def enemy_turn(board):

    for i, row in enumerate(board):
        if "" in row and row.count("O") == 2:
            x = 0
            for element in row:
                if element == "":
                    break
                x += 1

            board[i][x] = "O"
            return board

        if "" in row and row.count("X") == 2:
            x = 0
            for element in row:
                if element == "":
                    break
                x += 1

            board[i][x] = "O"
            return board
            

   
if __name__ == "__main__":
    main()
