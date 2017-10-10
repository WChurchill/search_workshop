import chess
from chess import svg
import minimax

b = chess.Board()
_file = 'chess.svg'

with open(_file, 'w') as f:
    f.write(chess.svg.board(board=b))

while not b.is_game_over():
    # Human moves
    user_move = chess.Move.from_uci(input("enter move: "))
    while user_move not in b.legal_moves:
        user_move = chess.Move.from_uci(input("enter move: "))
    b.push(user_move)
    with open(_file, 'w') as f:
        f.write(chess.svg.board(board=b))

    # AI moves
    b.push(minimax.get_move(b))
    with open(_file, 'w') as f:
        f.write(chess.svg.board(board=b))
