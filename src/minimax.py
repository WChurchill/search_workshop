# baseline minimax search

import tictactoe as ttt


class SearchNode():
    def __init__(self, parent, utility, board):
        self.utility = utility
        self.board = board
        self.parent = parent


def minimax(current_node, a, b, maximize=True):
    # check if we're at a leaf node
    util = ttt.utility(current_node.board)
    if util is not None:
        # the game is over, return the reward
        # ttt.display(current_node.board)
        return SearchNode(current_node, util, current_node.board)

    if maximize:
        child_node = SearchNode(current_node, -9999999999, current_node.board)

        # if it's our turn, return the move that maximizes utility
        for state in ttt.successors(current_node.board, 'X'):
            child_node = max(
                child_node,
                minimax(
                    SearchNode(current_node, None, state), a, b, not maximize),
                key=lambda node: node.utility)

            # Alpha-Beta pruning
            if child_node.utility >= b:
                return child_node

            a = max(a, child_node.utility)

        return child_node
    else:
        child_node = SearchNode(current_node, 9999999999, current_node.board)

        # If opponent's turn, return the move that minimizes utility
        for state in ttt.successors(current_node.board, 'O'):
            child_node = min(
                child_node,
                minimax(
                    SearchNode(current_node, None, state), a, b, not maximize),
                key=lambda node: node.utility)

            # Alpha-Beta pruning
            if child_node.utility <= a:
                return child_node

            b = min(b, child_node.utility)

        return child_node


def game_loop():
    WIDTH = 3
    b = ttt.make_board(WIDTH)

    while ttt.utility(b) is None:
        ttt.display(b)

        ### Human moves
        # sanitize user input

        user_move = ttt.prompt_move()
        while not ttt.valid_move(user_move, b):
            user_move = ttt.prompt_move()
        # process move
        b[user_move[0]][user_move[1]] = 'O'

        # end game if human plays winning move
        ttt.display(b)
        if ttt.utility(b) is None:
            ### AI moves
            current_node = SearchNode(None, None, b)
            best_node = minimax(
                current_node, -9999999999, 9999999999, maximize=True)
            b = best_node.board


if __name__ == '__main__':
    game_loop()
