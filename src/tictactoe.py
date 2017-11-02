import copy
import minimax


def display(board):
    # display column numbers
    print("  ", end="")
    for col in range(len(board[0])):
        print(col, end=" ")

    # print the first row of the board
    print("\n0", end=" ")
    for cell in board[0][:-1]:
        print("{}|".format(cell), end="")
    # print the last cell of the first row
    print("{}".format(board[0][-1]))

    # print each remaining row and a line separator
    for row_id in range(len(board[1:])):
        print("  ", end="")  # print space for row labels
        for _ in range(len(board[row_id]) - 1):
            print("-+", end="")  # print line separators
        print("-")
        print("{} ".format(row_id + 1), end="")
        for cell in board[row_id][:-1]:
            print("{}|".format(cell), end="")
        print("{}".format(board[row_id][-1]))


def make_board(width):
    assert (width % 2 != 0)
    return [[' ' for col in range(width)] for row in range(width)]


def utility(board):
    # check all rows
    cat = True
    for row in board:
        if ' ' not in row:
            if 'O' not in row:
                return 1
            if 'X' not in row:
                return -1
        else:
            cat = False
    if cat:
        return 0
    # check columns
    width = len(board)
    for column_idx in range(width):
        column = [row[column_idx] for row in board]
        if ' ' not in column:
            if 'O' not in column:
                return 1
            if 'X' not in column:
                return -1
    # check diagonals
    diag1 = [board[x][x] for x in range(width)]
    diag2 = [board[x][width - 1 - x] for x in range(width)]
    for diag in [diag1, diag2]:
        if ' ' not in diag:
            if 'O' not in diag:
                return 1
            if 'X' not in diag:
                return -1
    return None


def successors(board, turn):
    width = len(board)
    result = []
    for row_idx in range(width):
        for column_idx in range(width):
            if board[row_idx][column_idx] == ' ':
                new_board = copy.deepcopy(board)
                new_board[row_idx][column_idx] = turn
                result.append(new_board)
    return result


def test_board():
    b = make_board(3)
    b[0][0] = 'O'
    b[1][0] = 'O'
    b[0][1] = 'X'
    b[1][1] = 'X'
    b[0][2] = 'O'
    b[1][2] = 'X'
    b[2][2] = 'O'
    return b


def valid_move(input, board):
    width = len(board)
    row = input[0]
    col = input[1]
    return (row < width) and (col < width) and (board[row][col] == ' ')


def prompt_move():
    s = input("Enter move: <row> <column> ")
    tokens = s.split()
    return int(tokens[0]), int(tokens[1])


def game_loop():
    WIDTH = 3
    b = make_board(WIDTH)

    while utility(b) is None:
        ### Human moves
        # sanitize user input

        user_move = prompt_move()
        while not valid_move(user_move, b):
            user_move = prompt_move()

        # process move
        b[user_move[0]][user_move[1]] = 'O'

        ### AI moves
        current_node = minimax.SearchNode(None, b)
        next_node = minimax.minimax(current_node, maximize=True)
        b = next_node.board


if __name__ == '__main__':
    display(test_board())
