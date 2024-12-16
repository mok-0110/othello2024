import pygame
import random
import copy
from IPython.display import display, Image, clear_output
import time

# 定数
BLACK = 1
WHITE = 2
EMPTY = 0
CELL_SIZE = 80
BOARD_SIZE = 8
SCREEN_SIZE = CELL_SIZE * BOARD_SIZE
GREEN = (34, 139, 34)
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
LINE_COLOR = (0, 0, 0)

# 初期ボード作成
def create_board():
    board = [[EMPTY] * BOARD_SIZE for _ in range(BOARD_SIZE)]
    board[3][3] = BLACK
    board[4][4] = BLACK
    board[3][4] = WHITE
    board[4][3] = WHITE
    return board

# 有効な手を取得
def get_valid_moves(board, stone):
    moves = []
    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            if can_place_x_y(board, stone, x, y):
                moves.append((x, y))
    return moves

# 石を置けるか判定
def can_place_x_y(board, stone, x, y):
    if board[y][x] != EMPTY:
        return False
    opponent = 3 - stone
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        found_opponent = False
        while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == opponent:
            nx += dx
            ny += dy
            found_opponent = True
        if found_opponent and 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == stone:
            return True
    return False

# 手を適用
def apply_move(board, stone, x, y):
    opponent = 3 - stone
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    board[y][x] = stone

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        tiles_to_flip = []
        while 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == opponent:
            tiles_to_flip.append((nx, ny))
            nx += dx
            ny += dy
        if 0 <= nx < BOARD_SIZE and 0 <= ny < BOARD_SIZE and board[ny][nx] == stone:
            for flip_x, flip_y in tiles_to_flip:
                board[flip_y][flip_x] = stone

# 盤面を画像として保存
def draw_board_image(board, filename="othello.png", current_turn="Black", current_ai="PANDA"):
    pygame.init()
    screen = pygame.Surface((SCREEN_SIZE, SCREEN_SIZE + 40))
    screen.fill(GREEN)

    for y in range(BOARD_SIZE):
        for x in range(BOARD_SIZE):
            rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE + 40, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, LINE_COLOR, rect, 1)
            if board[y][x] == BLACK:
                pygame.draw.circle(screen, BLACK_COLOR, rect.center, CELL_SIZE // 3)
            elif board[y][x] == WHITE:
                pygame.draw.circle(screen, WHITE_COLOR, rect.center, CELL_SIZE // 3)

    font = pygame.font.Font(None, 36)
    text = font.render(f"Turn: {current_turn} ({current_ai})", True, BLACK_COLOR)
    screen.blit(text, (10, 10))

    pygame.image.save(screen, filename)
    pygame.quit()

# PandaAI（ランダム）
class PandaAI:
    def face(self):
        return "🐼"

    def name(self):
        return "PANDA"

    def place(self, board, stone):
        valid_moves = get_valid_moves(board, stone)
        return random.choice(valid_moves) if valid_moves else (-1, -1)

# MinimaxAI　（ミニマックス法）
class MinimaxAI:
    def face(self):
        return "🤖"

    def name(self):
        return "MINIMAX"

    def place(self, board, stone):
        valid_moves = get_valid_moves(board, stone)
        return valid_moves[0] if valid_moves else (-1, -1)

# DynamicMinimaxAI　（評価法　３段階に分ける）
class DynamicMinimaxAI:
    def face(self):
        return "🎓"

    def name(self):
        return "DYNAMIC"

    def place(self, board, stone):
        valid_moves = get_valid_moves(board, stone)
        return valid_moves[-1] if valid_moves else (-1, -1)

# ゲーム進行
def play_game(ai1, ai2):
    board = create_board()
    current_stone = BLACK
    ai_map = {BLACK: ai1, WHITE: ai2}
    filename = "othello.png"

    while True:
        current_turn = "Black" if current_stone == BLACK else "White"
        current_ai = ai_map[current_stone].name()

        draw_board_image(board, filename, current_turn, current_ai)
        clear_output(wait=True)
        display(Image(filename=filename))
        time.sleep(1)

        if not get_valid_moves(board, current_stone):
            current_stone = 3 - current_stone
            if not get_valid_moves(board, current_stone):
                break

        x, y = ai_map[current_stone].place(board, current_stone)
        if (x, y) != (-1, -1):
            apply_move(board, current_stone, x, y)

        current_stone = 3 - current_stone

    black_score = sum(row.count(BLACK) for row in board)
    white_score = sum(row.count(WHITE) for row in board)
    print("Game Over!")
    print(f"Black: {black_score}, White: {white_score}")
    if black_score > white_score:
        print(f"Black wins! {ai_map[BLACK].face()}")
    elif white_score > black_score:
        print(f"White wins! {ai_map[WHITE].face()}")
    else:
        print("It's a tie!")

# 対戦開始
play_game(DynamicMinimaxAI(), PandaAI())
