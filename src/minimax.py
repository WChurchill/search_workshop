# Minimax Search with alpha-beta pruning

import random
from tictactoe import successors, utility


def minimax(state, maximize=True):
    # check if we're at a leaf node
    if leaf(state):
        return utility(state)
    else:
        return max(children, key=lambda x: x[0])


def utility(state):
    """Evaluates the utility of a game state"""
    return 0
