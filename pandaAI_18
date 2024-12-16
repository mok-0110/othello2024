BLACK=1
WHITE=2

board = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,2,0,0],
        [0,0,2,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
]


class AI(object):

    def face(self):
        return "🐼"

    def place(self, board, stone):
        return x, y
import math
import random

BLACK=1
WHITE=2

board = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,2,0,0],
        [0,0,2,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
]

def can_place_x_y(board, stone, x, y):
    """
    石を置けるかどうかを調べる関数。
    board: 2次元配列のオセロボード
    x, y: 石を置きたい座標 (0-indexed)
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    return: 置けるなら True, 置けないなら False
    """
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
            return True  # 石を置ける条件を満たす

    return False

def can_place(board, stone):
    """
    石を置ける場所を調べる関数。
    board: 2次元配列のオセロボード
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    """
    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                return True
    return False

def random_place(board, stone):
    """
    石をランダムに置く関数。
    board: 2次元配列のオセロボード
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    """
    while True:
        x = random.randint(0, len(board[0]) - 1)
        y = random.randint(0, len(board) - 1)
        if can_place_x_y(board, stone, x, y):
            return x, y

class PandaAI(object):

    def face(self):
        return "🐼"

    def place(self, board, stone):
        x, y = random_place(board, stone)
        return x, y


!pip install -U kogi-canvas

from kogi_canvas import play_othello, PandaAI

BLACK=1
WHITE=2

board = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,2,0,0],
        [0,0,2,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
]

play_othello(PandaAI()) # ここを自分の作ったAIに変える
from kogi_canvas import Canvas
import math
import random

BLACK=1
WHITE=2

board = [
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
        [0,0,1,2,0,0],
        [0,0,2,1,0,0],
        [0,0,0,0,0,0],
        [0,0,0,0,0,0],
]

def can_place_x_y(board, stone, x, y):
    """
    石を置けるかどうかを調べる関数。
    board: 2次元配列のオセロボード
    x, y: 石を置きたい座標 (0-indexed)
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    return: 置けるなら True, 置けないなら False
    """
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
            return True  # 石を置ける条件を満たす

    return False

def can_place(board, stone):
    """
    石を置ける場所を調べる関数。
    board: 2次元配列のオセロボード
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    """
    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                return True
    return False

def random_place(board, stone):
    """
    石をランダムに置く関数。
    board: 2次元配列のオセロボード
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    """
    while True:
        x = random.randint(0, len(board[0]) - 1)
        y = random.randint(0, len(board) - 1)
        if can_place_x_y(board, stone, x, y):
            return x, y

class PandaAI(object):

    def face(self):
        return "🐼"

    def place(self, board, stone):
        x, y = random_place(board, stone)
        return x, y

play_othello(PandaAI())
class SmartAI(object):

    def face(self):
        return "🐼"

    def __init__(self, depth=3):
        self.depth = depth  # 探索の深さ

    def evaluate_board(self, board, stone):
        """
        ボードの評価関数。
        - 石数の差に加え、隅の価値を高める。
        """
        opponent = 3 - stone
        score = 0

        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == stone:
                    score += 1
                    if (x == 0 or x == len(board[0]) - 1) and (y == 0 or y == len(board) - 1):
                        score += 5  # 隅の価値を高める
                elif board[y][x] == opponent:
                    score -= 1
        return score

    def get_valid_moves(self, board, stone):
        """
        有効な手を全て取得する関数。
        """
        moves = []
        for y in range(len(board)):
            for x in range(len(board[0])):
                if can_place_x_y(board, stone, x, y):
                    moves.append((x, y))
        return moves

    def make_move(self, board, stone, x, y):
        """
        ボードに石を置き、変化後のボードを返す。
        """
        new_board = [row[:] for row in board]  # ボードのコピー
        opponent = 3 - stone
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        new_board[y][x] = stone

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            stones_to_flip = []

            while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and new_board[ny][nx] == opponent:
                stones_to_flip.append((nx, ny))
                nx += dx
                ny += dy

            if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and new_board[ny][nx] == stone:
                for flip_x, flip_y in stones_to_flip:
                    new_board[flip_y][flip_x] = stone

        return new_board

    def alphabeta(self, board, stone, depth, alpha, beta, maximizing_player):
        """
        アルファベータ探索を実装。
        """
        if depth == 0 or not can_place(board, stone):
            return self.evaluate_board(board, stone), None

        best_move = None
        valid_moves = self.get_valid_moves(board, stone)

        if maximizing_player:
            max_eval = -math.inf
            for move in valid_moves:
                new_board = self.make_move(board, stone, move[0], move[1])
                eval, _ = self.alphabeta(new_board, 3 - stone, depth - 1, alpha, beta, False)
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = math.inf
            for move in valid_moves:
                new_board = self.make_move(board, stone, move[0], move[1])
                eval, _ = self.alphabeta(new_board, 3 - stone, depth - 1, alpha, beta, True)
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def place(self, board, stone):
        """
        アルファベータ探索で最適な一手を選択。
        """
        _, best_move = self.alphabeta(board, stone, self.depth, -math.inf, math.inf, True)
        return best_move
CORNERS = [(0, 0), (0, 5), (5, 0), (5, 5)]
DANGEROUS_MOVES = {
    (0, 0): [(0, 1), (1, 0), (1, 1)],
    (0, 5): [(0, 4), (1, 5), (1, 4)],
    (5, 0): [(4, 0), (5, 1), (4, 1)],
    (5, 5): [(4, 5), (5, 4), (4, 4)],
}
  def prioritize_corners_first(valid_moves):
    """
    隅を最優先で選択する。
    """
    for move in valid_moves:
        if move in CORNERS:
            return move
    return None


def avoid_dangerous_moves(valid_moves, board, stone):
    """
    隅に近い危険な手を避ける。
    """
    safe_moves = []
    for move in valid_moves:
        is_dangerous = False
        for corner, danger_moves in DANGEROUS_MOVES.items():
            if move in danger_moves and board[corner[1]][corner[0]] == 0:  # 隅が空なら危険
                is_dangerous = True
                break
        if not is_dangerous:
            safe_moves.append(move)

    return safe_moves or valid_moves  # 全て危険なら仕方なく選択


def evaluate_with_corners(board, stone):
    """
    隅を強く評価し、危険な手を避ける評価関数。
    """
    score = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == stone:
                if (x, y) in CORNERS:
                    score += 1000  # 隅を非常に高く評価
                else:
                    score += 1  # 他の位置も軽く評価
            elif board[y][x] == 3 - stone:
                if (x, y) in CORNERS:
                    score -= 1000  # 相手の隅も強く評価
                else:
                    score -= 1
    return score
class CornerPriorityAI(SmartAI):
    def place(self, board, stone):
        valid_moves = self.get_valid_moves(board, stone)

        # 隅を優先
        corner_move = prioritize_corners_first(valid_moves)
        if corner_move:
            return corner_move

        # 危険な手を避ける
        safe_moves = avoid_dangerous_moves(valid_moves, board, stone)

        # 最良の手を選択（評価関数を用いる）
        best_score = -float("inf")
        best_move = None
        for move in safe_moves:
            temp_board = self.make_move(board, stone, move[0], move[1])
            score = evaluate_with_corners(temp_board, stone)
            if score > best_score:
                best_score = score
                best_move = move

        return best_move
play_othello(CornerPriorityAI())
      
