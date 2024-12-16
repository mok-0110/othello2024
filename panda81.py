!pip install -U kogi-canvas
from kogi_canvas import play_othello, PandaAI

import random

BLACK = 1
WHITE = 2
CORNER_POSITIONS = [(0, 0), (0, 5), (5, 0), (5, 5)]  # ボードのコーナー
ADJACENT_POSITIONS = [
    (0, 1), (1, 0), (1, 1),  # 角(0, 0)の隣接位置
    (0, 4), (1, 5), (1, 4),  # 角(0, 5)の隣接位置
    (4, 0), (5, 1), (4, 5),  # 角(5, 0)の隣接位置
    (5, 4), (4, 1)  # 角(5, 5)の隣接位置
]

def can_place_x_y(board, stone, x, y):
    """
    指定された座標に石を置けるかどうかを判定する関数。
    """
    if board[y][x] != 0:
        return False  # すでに石がある場合は置けない

    opponent = 3 - stone  # 相手の石
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        found_opponent = False

        while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
            nx += dx
            ny += dy
            found_opponent = True

        if found_opponent and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
            return True  # 有効な手が見つかった

    return False

def random_place(board, stone):
    """
    ランダムな位置に石を置く関数。
    """
    while True:
        x = random.randint(0, len(board[0]) - 1)
        y = random.randint(0, len(board) - 1)
        if can_place_x_y(board, stone, x, y):
            return x, y

def evaluate_board(board, stone):
    """
    ボードを評価し、スコアを返す関数。
    高いスコアほど有利。
    """
    opponent = 3 - stone
    score = 0

    # コーナーを重視する
    for x, y in CORNER_POSITIONS:
        if board[y][x] == stone:
            score += 10  # コーナーは非常に価値が高い
        elif board[y][x] == opponent:
            score -= 10

    # コーナー隣接位置の評価（少しだけ低評価に調整）
    for x, y in ADJACENT_POSITIONS:
        if board[y][x] == stone:
            score -= 3  # 隣接位置は避けるべきなので低評価
        elif board[y][x] == opponent:
            score += 3  # 相手が隣接位置に置いた場合は逆に有利

    # 石の数の評価 (積極的に石を増やす)
    for y in range(6):
        for x in range(6):
            if board[y][x] == stone:
                score += 1
            elif board[y][x] == opponent:
                score -= 1

    # ボードが埋まっている場合、相手の手を制限する
    empty_count = sum(row.count(0) for row in board)
    if empty_count <= 10:
        score += 5  # ゲームが終盤の場合は積極的に進める

    return score

def minimax(board, depth, stone, alpha, beta):
    """
    ミニマックスアルゴリズムを用いて、最適な手を探索する関数。
    """
    # 基本的な終了条件
    if depth == 0:
        return evaluate_board(board, stone), None

    best_score = -float('inf') if stone == BLACK else float('inf')
    best_move = None

    # すべての有効な手を評価
    for y in range(6):
        for x in range(6):
            if can_place_x_y(board, stone, x, y):
                # 新しいボードを作成してその手をシミュレート
                new_board = [row[:] for row in board]
                new_board[y][x] = stone
                # 再帰的に探索
                score, _ = minimax(new_board, depth - 1, 3 - stone, alpha, beta)

                if stone == BLACK:
                    if score > best_score:
                        best_score = score
                        best_move = (x, y)
                    alpha = max(alpha, score)
                else:
                    if score < best_score:
                        best_score = score
                        best_move = (x, y)
                    beta = min(beta, score)

                if beta <= alpha:
                    break  # アルファ・ベータ剪定

    return best_score, best_move

class EagerAI(object):
    def face(self):
        return "🐼"  # EagerAIパンダ

    def place(self, board, stone):
        # ミニマックスアルゴリズムを使って最適な手を選ぶ
        _, best_move = minimax(board, 3, stone, -float('inf'), float('inf'))
        if best_move is None:
            return random_place(board, stone)  # 手が無ければランダム

        return best_move
play_othello(EagerAI())
