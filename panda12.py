import math
import random

BLACK = 1
WHITE = 2

board = [
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 2, 0, 0],
        [0, 0, 2, 1, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
]

def can_place_x_y(board, stone, x, y):
    if board[y][x] != 0:
        return False  # 既に石がある場合は置けない

    opponent = 3 - stone  # 相手の石 (1なら2、2なら1)
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        found_opponent = False

        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
            nx += dx
            ny += dy
            found_opponent = True

        if found_opponent and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
            return True

    return False

def count_flippable_stones(board, stone, x, y):
    """
    指定された位置 (x, y) に石を置いた場合にひっくり返せる石の数を数える関数。
    """
    if board[y][x] != 0:
        return 0

    opponent = 3 - stone
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    total_flippable = 0

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        flippable = 0

        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
            nx += dx
            ny += dy
            flippable += 1

        if flippable > 0 and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
            total_flippable += flippable

    return total_flippable

def best_place(board, stone):
    """
    ひっくり返せる石の数が最大になる位置を探して返す関数。
    """
    best_score = -1
    best_move = None

    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                score = count_flippable_stones(board, stone, x, y)
                if score > best_score:
                    best_score = score
                    best_move = (x, y)

    return best_move

class PandaAI(object):

    def face(self):
        return "🐼"

    def place(self, board, stone):
        # 最適な場所を探す
        move = best_place(board, stone)
        return move
