import copy


def display(board):
    for cell in board[0][:-1]:
        print("{}|".format(cell), end="")
    print("{}".format(board[0][-1]))
    for row in board[1:]:
        for _ in range(len(row) - 1):
            print("-+", end="")
        print("-")
        for cell in row[:-1]:
            print("{}|".format(cell), end="")
        print("{}".format(row[-1]))


def make_board(width):
    assert (width % 2 != 0)
    return [[' '] * width] * width


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


def successors(board):
    width = len(board)
    result = []
    for row_idx in range(width):
        for column_idx in range(width):
            if board[row_idx][column_idx] == ' ':
                board1 = copy.deepcopy(board)
                board2 = copy.deepcopy(board)

                board1[row_idx][column_idx] = 'X'
                board2[row_idx][column_idx] = 'O'
                result += [board1, board2]
    return result


if __name__ == '__main__':
    b = make_board(3)
    b[0][0] = 'X'
    display(b)
