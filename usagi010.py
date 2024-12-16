import time
import copy

# 評価値表
EVALUATION_TABLE = [
    [120, -20, 10, 5, 5, 10, -20, 120],
    [-20, -40, -5, -5, -5, -5, -40, -20],
    [10, -5, 5, 0, 0, 5, -5, 10],
    [5, -5, 0, 0, 0, 0, -5, 5],
    [5, -5, 0, 0, 0, 0, -5, 5],
    [10, -5, 5, 0, 0, 5, -5, 10],
    [-20, -40, -5, -5, -5, -5, -40, -20],
    [120, -20, 10, 5, 5, 10, -20, 120]
]

# 方向（上下左右・斜め8方向）
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

# ボードの初期化
def initialize_board():
    board = [['・' for _ in range(8)] for _ in range(8)]
    board[3][3], board[3][4] = '○', '●'
    board[4][3], board[4][4] = '●', '○'
    return board

# ボードの表示
def print_board(board):
    print(" " + " ".join(map(str, range(8))))
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))
    print()

# 合法手の探索
def get_valid_moves(board, player):
    opponent = '○' if player == '●' else '●'
    valid_moves = []
    for x in range(8):
        for y in range(8):
            if board[x][y] != '・':
                continue
            if any(can_flip_in_direction(board, x, y, dx, dy, player, opponent) for dx, dy in DIRECTIONS):
                valid_moves.append((x, y))
    return valid_moves

def can_flip_in_direction(board, x, y, dx, dy, player, opponent):
    flips = []
    nx, ny = x + dx, y + dy
    while 0 <= nx < 8 and 0 <= ny < 8:
        if board[nx][ny] == opponent:
            flips.append((nx, ny))
        elif board[nx][ny] == player:
            return flips
        else:
            break
        nx, ny = nx + dx, ny + dy
    return []

# 石を置く
def make_move(board, x, y, player):
    opponent = '○' if player == '●' else '●'
    board[x][y] = player
    for dx, dy in DIRECTIONS:
        flips = can_flip_in_direction(board, x, y, dx, dy, player, opponent)
        for fx, fy in flips:
            board[fx][fy] = player
    return board

# ボードの評価関数
def evaluate_board(board, player):
    opponent = '○' if player == '●' else '●'
    score = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == player:
                score += EVALUATION_TABLE[x][y]
            elif board[x][y] == opponent:
                score -= EVALUATION_TABLE[x][y]
    return score

# ミニマックス探索
def minimax(board, depth, alpha, beta, maximizing, player, opponent):
    if depth == 0 or game_over(board):
        return evaluate_board(board, player)

    valid_moves = get_valid_moves(board, player if maximizing else opponent)
    if not valid_moves:
        return evaluate_board(board, player)

    if maximizing:
        max_eval = float('-inf')
        for x, y in valid_moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, x, y, player)
            eval = minimax(new_board, depth-1, alpha, beta, False, player, opponent)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for x, y in valid_moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, x, y, opponent)
            eval = minimax(new_board, depth-1, alpha, beta, True, player, opponent)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# 最善手を選択
def choose_best_move(board, player, time_limit):
    start_time = time.time()
    best_move = None
    best_score = float('-inf')
    opponent = '○' if player == '●' else '●'

    depth = 1
    while time.time() - start_time < time_limit:
        valid_moves = get_valid_moves(board, player)
        for x, y in valid_moves:
            new_board = copy.deepcopy(board)
            make_move(new_board, x, y, player)
            score = minimax(new_board, depth, float('-inf'), float('inf'), False, player, opponent)
            if score > best_score:
                best_score = score
                best_move = (x, y)
        depth += 1

    return best_move

# ゲーム終了の判定
def game_over(board):
    return not get_valid_moves(board, '●') and not get_valid_moves(board, '○')

# ゲームの進行
def play_game():
    board = initialize_board()
    player = '●'
    time_limit = 3 # 各ターンの時間制限（秒）

    while not game_over(board):
        print_board(board)
        if player == '●': # AIのターン
            move = choose_best_move(board, player, time_limit)
            if move:
                make_move(board, move[0], move[1], player)
        else: # プレイヤーのターン
            print("あなたのターンです！")
            move = input("行と列をスペースで区切って入力してください (例: 3 2): ")
            try:
                x, y = map(int, move.split())
                if (x, y) in get_valid_moves(board, player):
                    make_move(board, x, y, player)
                else:
                    print("その場所には置けません。もう一度入力してください。")
                    continue
            except ValueError:
                print("無効な入力です。もう一度入力してください。")
                continue

        player = '○' if player == '●' else '●'

    print("ゲーム終了！")
    print_board(board)


# ゲームボードの表示形式の変更

def print_board(board):
    # 横列の番号を全角数字に変換
    zenkaku_nums = "０１２３４５６７"
    print(" " + " ".join(zenkaku_nums))
    for i, row in enumerate(board):
        # 縦列の番号も全角数字に変換
        print(f"{zenkaku_nums[i]} " + " ".join(row))
    print()


# 実行
if __name__ == "__main__":
    play_game() 
