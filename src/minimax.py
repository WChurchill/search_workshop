# Minimax Search with alpha-beta pruning

from tictactoe import successors, utility, display


class SearchNode():
    def __init__(self, utility, board):
        self.utility = utility
        self.board = board


def minimax(current_node, a, b, maximize=True):
    # check if we're at a leaf node
    util = utility(current_node.board)
    if util is not None:
        # the game is over, return the reward
        display(current_node.board)
        return SearchNode(util, current_node.board)

    if maximize:
        child_node = SearchNode(-9999999999, current_node.board)

        # if it's our turn, return the move that maximizes utility
        for state in successors(current_node.board, 'X'):
            child_node = max(child_node, minimax(SearchNode(None, state), a, b, not maximize),
                             key=lambda node: node.utility)

            # Alpha-Beta pruning
            if child_node.utility >= b:
                return child_node

            a = max(a, child_node.utility)

        return child_node
    else:
        child_node = SearchNode(9999999999, current_node.board)

        # If opponent's turn, return the move that minimizes utility
        for state in successors(current_node.board, 'O'):
            child_node = min(child_node, minimax(SearchNode(None, state), a, b, not maximize),
                             key=lambda node: node.utility)

            # Alpha-Beta pruning
            if child_node.utility <= a:
                return child_node

            b = min(b, child_node.utility)

        return child_node
