# baseline minimax search

from tictactoe import successors, utility, display


class SearchNode():
    def __init__(self, utility, board):
        self.utility = utility
        self.board = board


def minimax(current_node, maximize=True):
    # check if we're at a leaf node
    util = utility(current_node.board)
    if util is not None:
        # the game is over, return the reward
        display(current_node.board)
        return SearchNode(util, current_node.board)
    elif maximize:
        # if it's our turn, return the move that maximizes utility
        child_nodes = [
            minimax(SearchNode(None, state), not maximize)
            for state in successors(current_node.board, 'X')
        ]
        return max(child_nodes, key=lambda node: node.utility)
    else:
        child_nodes = [
            minimax(SearchNode(None, state), not maximize)
            for state in successors(current_node.board, 'X')
        ]
        return min(child_nodes, key=lambda node: node.utility)
