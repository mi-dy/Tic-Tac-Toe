import sys

def main():
    in_a_row = 3
    board_size = int(input("Size of the board: "))
    board = []

    for i in range(board_size):
        board.append([])
        for _ in range(board_size):
            board[i].append("")

    if len(board) > 5:
        in_a_row = len(board) - 3

    while True:

        print_board(board)

        y_input = int(input("Place X at row: ")) -1
        x_input = int(input("Place X at column: ")) -1
        
        if board[y_input][x_input] == "":
            board[y_input][x_input] = "X"
        else:
            continue

        if check_victory(board, in_a_row):
            print_board(board)

            print("Victory royal!")
            return

        enemy_y, enemy_x = enemy_function(board, in_a_row)
        board[enemy_y][enemy_x] = "O"

        if check_victory(board, in_a_row):
            print_board(board)

            print("Looser!")
            return


def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")

def check_victory(board, in_a_row):

    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    for y in range(len(board)):
        for x in range(len(board[0])):
            for dy, dx in directions:
                end_y = y + (in_a_row - 1) * dy
                end_x = x + (in_a_row - 1) * dx
                if 0 <= end_y < len(board) and 0 <= end_x < len(board[0]):
                    segment = [board[y + i*dy][x + i*dx] for i in range(in_a_row)]
                    if len(set(segment)) == 1 and segment[0] != "":
                        return True
    
    full_row_count = 0
    for row in board:
        if "" not in row:
            full_row_count += 1

    if full_row_count == len(board):
        sys.exit("Tie!")
 
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
                        elif segment.count(symbol) > 1 and segment.count("") > 0 and len(set(segment)) == 2:
                            symbol_value = 0
                            if symbol == "O":
                                symbol_value = 1
                            empty_square_index = segment.index("")
                            best_moves.append((segment.count(symbol), symbol_value, y + empty_square_index*dy, x + empty_square_index*dx))
                        elif segment.count("O") > 0 and segment.count("") > 0 and len(set(segment)) == 2:
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
    corners = [(0,0), (0, len(board)-1), (len(board)-1, 0), (len(board)-1, len(board)-1)]
    for y, x in corners:
        if board[y][x] == "":
            return y, x

 
if __name__ == "__main__":
    main()
