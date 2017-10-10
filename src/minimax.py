# Minimax Search with alpha-beta pruning

import chess
import minimax
import random


def get_move(board):
    """Return a legal chess move that maximizes chances of winning"""
    print(len(board.legal_moves))
    moves = [m for m in board.legal_moves]
    return random.choice(moves)


def utility(board):
    """Approximates the utility of a certain board configuration"""
    return 0
