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


def check_victory(board):

    for row in board:
        if len(set(row)) == 1 and row[0] != "":
            return True


    columns = [[], [], []]
    for row in board:
        for i, symbol in enumerate(row):
            columns[i].append(symbol)

    for column in columns:
        if len(set(column)) == 1 and column[0] != "":
            return True


    diagonals = [[], []]
    for i, row in enumerate(board):
        diagonals[0].append(row[i])
    i = 2
    for row in board:
        diagonals[1].append(row[i])
        i -= 1

    for diagonal in diagonals:
        if len(set(diagonal)) == 1 and diagonal[0] != "":
            return True

    return False


if __name__ == "__main__":
    main()
