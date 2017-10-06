import chess
from chess import svg
from ai import get_move

b = chess.Board()
_file = 'chess.svg'

with open(_file, 'w') as f:
    f.write(chess.svg.board(board=b))

user_move = input("enter move: ")

b.push(chess.Move.from_uci(user_move))
with open(_file, 'w') as f:
    f.write(chess.svg.board(board=b))
