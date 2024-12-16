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


import random
import math

BLACK = 1
WHITE = 2

# オセロのボード
board = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 2, 0, 0],
    [0, 0, 2, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

# Q-learningのパラメータ
ALPHA = 0.1  # 学習率
GAMMA = 0.9  # 割引率
EPSILON = 0.2  # 探索率（ランダムに動く確率）
Q_TABLE = {}  # Qテーブル (状態 -> 行動のQ値)

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

def can_place(board, stone):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if can_place_x_y(board, stone, x, y):
                return True
    return False

def random_place(board, stone):
    while True:
        x = random.randint(0, len(board[0]) - 1)
        y = random.randint(0, len(board) - 1)
        if can_place_x_y(board, stone, x, y):
            return x, y

def get_state(board):
    """ボードの状態をタプルに変換して返す"""
    return tuple(tuple(row) for row in board)

def update_q_table(state, action, reward, next_state):
    """Qテーブルを更新する"""
    if state not in Q_TABLE:
        Q_TABLE[state] = {}
    if action not in Q_TABLE[state]:
        Q_TABLE[state][action] = 0

    # 次の状態の最大Q値
    next_max_q = max(Q_TABLE.get(next_state, {}).values(), default=0)

    # Q値の更新
    Q_TABLE[state][action] += ALPHA * (reward + GAMMA * next_max_q - Q_TABLE[state][action])

def choose_action(board, stone):
    """行動を選択する"""
    state = get_state(board)

    # 探索と活用のバランス
    if random.random() < EPSILON:
        # ランダムに行動
        return random_place(board, stone)
    else:
        # Qテーブルに基づく最適行動
        if state not in Q_TABLE:
            Q_TABLE[state] = {}

        best_action = None
        best_q_value = -math.inf

        for y in range(len(board)):
            for x in range(len(board[0])):
                if can_place_x_y(board, stone, x, y):
                    if (x, y) not in Q_TABLE[state]:
                        Q_TABLE[state][(x, y)] = 0  # 初期化
                    q_value = Q_TABLE[state][(x, y)]
                    if q_value > best_q_value:
                        best_q_value = q_value
                        best_action = (x, y)

        return best_action

class PandaAI(object):
    def face(self):
        return "🐼"

    def place(self, board, stone):
        # 最適な手を選ぶ
        return choose_action(board, stone)

def play_game():
    """ゲームを1回実行して学習する"""
    board_copy = [row[:] for row in board]  # ボードのコピー
    turn = BLACK  # 最初は黒が先手
    while can_place(board_copy, turn):
        x, y = PandaAI().place(board_copy, turn)
        board_copy[y][x] = turn
        turn = 3 - turn  # 黒と白を交互に

    # ゲーム終了後に報酬を更新
    return board_copy

# ゲームの実行例（数回繰り返す）
for _ in range(1000):  # 1000回対戦
    final_board = play_game()
    winner = 1  # ここでは簡単に黒の勝ちとする
    if winner == 1:
        reward = 1  # 黒が勝った場合
    else:
        reward = -1  # 白が勝った場合

    # ゲームの状態と報酬に基づいてQテーブルを更新
    state = get_state(final_board)
    for action in Q_TABLE.get(state, {}):
        update_q_table(state, action, reward, state)

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

play_othello(NonAI()) # ここを自分の作ったAIに変える
