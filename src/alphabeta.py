# Minimax Search with alpha-beta pruning

import chess


class SearchNode():
    # reward for winning the game

    # must be less than 'infinity' but still much, much larger than
    # any non-winning board heuristic

    WIN_REWARD = 99999

    def __init__(self, move, board):
        self.move = move  # the move that generated this state
        self.board = board

    def is_leaf(self):
        return self.board.result() != '*'

    def utility(self):
        result = self.board.result()
        # stalemate
        if result == '1/2-1/2':
            return 0
        elif result == '0-1':
            return WIN_REWARD
            # enemy checkmate
        elif result == '1-0':
            return -WIN_REWARD
        else:
            return self.heuristic()
        # heuristic

    def successors(self):
        return [
            SearchNode(m, self.board.copy().push(m))
            for m in self.board.legal_moves
        ]

    def heuristic(self):
        return self.board_score() + self.movable_space * 0.1

    def board_score(self):
        """Compute the points based on the official value of each piece."""
        black_score = 0
        white_score = 0
        for piece in self.board.piece_map():
            if piece.color == chess.WHITE:
                white_score += piece_value(piece.piece_type)
            else:
                black_score += piece_value(piece.piece_type)
        return black_score / white_score  # - 1

    def movable_space(self):
        """Count the number of squares that the player can move to."""
        return 0


def piece_value(piece):
    if piece == chess.PAWN:
        return 1
    elif piece == chess.KNIGHT:
        return 3
    elif piece == chess.BISHOP:
        return 3
    elif piece == chess.ROOK:
        return 5
    elif piece == chess.QUEEN:
        return 9
    elif piece == chess.KING:
        return 0.00001


INFINITY = 9999999999


def get_move(board):
    start_node = SearchNode(None, board)
    best_state = alphabeta(start_node, 1, -INFINITY, INFINITY, maximize=True)
    return best_state.move


def alphabeta(current_node, depth, a, b, maximize=True):
    # check if we're at a leaf node
    if current_node.is_leaf() or depth == 0:
        # the game is over, return the reward
        return SearchNode(current_node.utility(), current_node.board,
                          current_node.move)

    if maximize:
        child_node = SearchNode(-INFINITY, current_node.board)

        # if it's our turn, return the move that maximizes utility
        for state in current_node.successors():
            child_node = max(
                child_node,
                alphabeta(SearchNode(None, state), a, b, not maximize),
                key=lambda node: node.utility)

            # Alpha-Beta pruning
            if child_node.utility >= b:
                return child_node

            a = max(a, child_node.utility)

        return child_node
    else:
        child_node = SearchNode(INFINITY, current_node.board)

        # If opponent's turn, then minimize
        for state in current_node.successors():
            child_node = min(
                child_node,
                alphabeta(SearchNode(None, state), a, b, not maximize),
                key=lambda node: node.utility)

            # Alpha-Beta pruning
            if child_node.utility <= a:
                return child_node

            b = min(b, child_node.utility)

        return child_node
