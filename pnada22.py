from kogi_canvas import Canvas
import math

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
        return False

    opponent = 3 - stone
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

def get_valid_moves(board, stone):
    return [(x, y) for y in range(len(board)) for x in range(len(board[0])) if can_place_x_y(board, stone, x, y)]

def apply_move(board, stone, x, y):
    new_board = [row[:] for row in board]
    new_board[y][x] = stone
    opponent = 3 - stone
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        cells_to_flip = []

        while 0 <= nx < len(new_board[0]) and 0 <= ny < len(new_board) and new_board[ny][nx] == opponent:
            cells_to_flip.append((nx, ny))
            nx += dx
            ny += dy

        if 0 <= nx < len(new_board[0]) and 0 <= ny < len(new_board) and new_board[ny][nx] == stone:
            for flip_x, flip_y in cells_to_flip:
                new_board[flip_y][flip_x] = stone

    return new_board

def evaluate_board(board, stone):
    opponent = 3 - stone
    stable_bonus = 20
    edge_bonus = 10
    center_penalty = -1
    mobility_bonus = 2

    score = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == stone:
                if (x == 0 or x == len(board[0]) - 1) and (y == 0 or y == len(board) - 1):
                    score += 100  # 角は最重要
                elif x == 0 or x == len(board[0]) - 1 or y == 0 or y == len(board) - 1:
                    score += edge_bonus
                else:
                    score += center_penalty
            elif board[y][x] == opponent:
                score -= 1

    valid_moves = len(get_valid_moves(board, stone))
    opponent_moves = len(get_valid_moves(board, opponent))
    score += mobility_bonus * (valid_moves - opponent_moves)
    return score

def minimax(board, stone, depth, alpha, beta, maximizing, adaptive_depth=False):
    if depth == 0 or not get_valid_moves(board, stone):
        return evaluate_board(board, stone)

    if adaptive_depth:
        total_stones = sum(row.count(stone) + row.count(3 - stone) for row in board)
        depth = 4 if total_stones > 40 else 3

    if maximizing:
        max_eval = -math.inf
        for x, y in get_valid_moves(board, stone):
            new_board = apply_move(board, stone, x, y)
            eval = minimax(new_board, 3 - stone, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for x, y in get_valid_moves(board, stone):
            new_board = apply_move(board, stone, x, y)
            eval = minimax(new_board, 3 - stone, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

class PandaAI(object):
    def face(self):
        return "🐼"

    def place(self, board, stone):
        best_score = -math.inf
        best_move = None
        adaptive_depth = True  # ゲーム状況に応じた深さ調整
        for x, y in get_valid_moves(board, stone):
            new_board = apply_move(board, stone, x, y)
            score = minimax(new_board, 3 - stone, 4, -math.inf, math.inf, False, adaptive_depth)
            if score > best_score:
                best_score = score
                best_move = (x, y)
        return best_move

play_othello(PandaAI())

