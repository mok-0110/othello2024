import math

class EagerAI:
    def face(self):
        return "🐼"

    def place(self, board, stone):
        # ミニマックスアルゴリズムで最適な手を選択
        return self.minimax(board, stone, depth=3, alpha=-math.inf, beta=math.inf, maximizing=True)[1]

    def minimax(self, board, stone, depth, alpha, beta, maximizing):
        opponent = 3 - stone

        # 終了条件: 深さ0または置ける手がない場合
        if depth == 0 or not self.has_valid_moves(board, stone) and not self.has_valid_moves(board, opponent):
            return self.evaluate(board, stone), None

        best_move = None
        if maximizing:
            max_eval = -math.inf
            for move in self.get_valid_moves(board, stone):
                x, y = move
                new_board = [row[:] for row in board]
                self.place_and_flip(new_board, stone, x, y)
                eval_score, _ = self.minimax(new_board, opponent, depth - 1, alpha, beta, False)
                if eval_score > max_eval:
                    max_eval = eval_score
                    best_move = move
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = math.inf
            for move in self.get_valid_moves(board, opponent):
                x, y = move
                new_board = [row[:] for row in board]
                self.place_and_flip(new_board, opponent, x, y)
                eval_score, _ = self.minimax(new_board, stone, depth - 1, alpha, beta, True)
                if eval_score < min_eval:
                    min_eval = eval_score
                    best_move = move
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def evaluate(self, board, stone):
        """
        評価関数: 石の位置、安定性、角、手数などを総合的に評価する。
        """
        opponent = 3 - stone
        score = 0

        # 角の評価
        corners = [(0, 0), (0, len(board) - 1), (len(board[0]) - 1, 0), (len(board[0]) - 1, len(board) - 1)]
        for x, y in corners:
            if board[y][x] == stone:
                score += 100
            elif board[y][x] == opponent:
                score -= 100

        # 角周辺のリスク評価
        corner_adjacents = [
            (0, 1), (1, 0), (1, 1),
            (0, len(board) - 2), (1, len(board) - 1), (1, len(board) - 2),
            (len(board) - 2, 0), (len(board) - 1, 1), (len(board) - 2, 1),
            (len(board) - 2, len(board) - 1), (len(board) - 1, len(board) - 2), (len(board) - 2, len(board) - 2)
        ]
        for x, y in corner_adjacents:
            if board[y][x] == stone:
                score -= 30
            elif board[y][x] == opponent:
                score += 30

        # 安定した石の評価
        score += self.count_stable_stones(board, stone) * 20

        # 手数の評価
        score += len(self.get_valid_moves(board, stone)) * 5
        score -= len(self.get_valid_moves(board, opponent)) * 5

        # 石の数評価（終盤用）
        score += sum(row.count(stone) for row in board) - sum(row.count(opponent) for row in board)

        return score

    def place_and_flip(self, board, stone, x, y):
        """
        石を置き、挟んだ石を裏返す。
        """
        board[y][x] = stone
        opponent = 3 - stone
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            flips = []

            while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
                flips.append((nx, ny))
                nx += dx
                ny += dy

            if 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
                for fx, fy in flips:
                    board[fy][fx] = stone

    def get_valid_moves(self, board, stone):
        """
        石を置ける有効なマスを取得する。
        """
        valid_moves = []
        for y in range(len(board)):
            for x in range(len(board[0])):
                if can_place_x_y(board, stone, x, y):
                    valid_moves.append((x, y))
        return valid_moves

    def has_valid_moves(self, board, stone):
        """
        石を置ける場所があるかを確認する。
        """
        return any(can_place_x_y(board, stone, x, y) for y in range(len(board)) for x in range(len(board[0])))

    def count_stable_stones(self, board, stone):
        """
        安定した石の数をカウントする。
        """
        stable_stones = 0
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == stone and self.is_stable(board, stone, x, y):
                    stable_stones += 1
        return stable_stones

    def is_stable(self, board, stone, x, y):
        """
        石が安定しているかを判定する。
        """
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            while 0 <= nx < len(board[0]) and 0 <= ny < len(board):
                if board[ny][nx] == 0:
                    return False
                nx += dx
                ny += dy
        return True
