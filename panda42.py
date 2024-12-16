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

# 評価値マトリックス
evaluation_matrix = [
    [10, 5, 5, 5, 5, 10],
    [5, 1, 2, 2, 1, 5],
    [5, 2, 0, 0, 2, 5],
    [5, 2, 0, 0, 2, 5],
    [5, 1, 2, 2, 1, 5],
    [10, 5, 5, 5, 5, 10]
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

def negamax(board, depth, stone, alpha, beta):
    """
    negamax法による探索
    depth: 探索の深さ
    stone: 現在のプレイヤーの石 (1: 黒, 2: 白)
    alpha: アルファ値
    beta: ベータ値
    """
    if depth == 0:
        return evaluate(board, stone)  # 深さが0になったら評価値を返す

    best_score = -math.inf
    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                # 仮に石を置いて次の局面をシミュレート
                board[y][x] = stone
                score = -negamax(board, depth - 1, 3 - stone, -beta, -alpha)  # 相手のターン (stoneを反転)
                # 石を戻す
                board[y][x] = 0

                best_score = max(best_score, score)
                alpha = max(alpha, best_score)
                if alpha >= beta:
                    break  # ベータカット

    return best_score

def best_move(board, stone, depth):
    """
    negamax法を使用して最適な手を選ぶ関数。
    """
    best_score = -math.inf
    best_move = None

    # すべての可能な手を評価
    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                # 仮に石を置いて次の局面を評価
                board[y][x] = stone
                score = -negamax(board, depth - 1, 3 - stone, -math.inf, math.inf)  # 相手のターン
                # 石を戻す
                board[y][x] = 0

                if score > best_score:
                    best_score = score
                    best_move = (x, y)

    return best_move

def evaluate(board, stone):
    """
    局面を評価する関数。
    """
    score = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == stone:
                score += evaluation_matrix[y][x]  # 自分の石がある場所は評価値を加算
            elif board[y][x] == 3 - stone:
                score -= evaluation_matrix[y][x]  # 相手の石がある場所は評価値を減算
    return score

class PandaAI(object):
    def face(self):
        return "🐼"

    def place(self, board, stone):
        x, y = best_move(board, stone, depth=4)  # negamax法で4手先読みを行って最適な手を選ぶ
        return x, y
    
class LionAI4(object):
    def face(self):
        return "🦁"
      
    def place(self, board, stone):
        x, y = best_move(board, stone, depth=4)
        return x, y
