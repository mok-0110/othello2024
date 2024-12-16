WEIGHT_MATRIX = [
    [100, -20, 10, 10, -20, 100],
    [-20, -50,  1,  1, -50, -20],
    [10,   1,   5,  5,   1,  10],
    [10,   1,   5,  5,   1,  10],
    [-20, -50,  1,  1, -50, -20],
    [100, -20, 10, 10, -20, 100],
]

class nekoAI(object):

    def face(self):
        return "🐱"

    def count_flips(self, board, stone, x, y):
        if board[y][x] != 0:
            return 0

        opponent = 3 - stone
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        total_flips = 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            flips = 0
            while 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == opponent:
                flips += 1
                nx += dx
                ny += dy
            if flips > 0 and 0 <= nx < len(board[0]) and 0 <= ny < len(board) and board[ny][nx] == stone:
                total_flips += flips

        return total_flips

    def evaluate_moves(self, board, stone):
        moves = []
        for y in range(len(board)):
            for x in range(len(board[0])):
                if can_place_x_y(board, stone, x, y):
                    flips = self.count_flips(board, stone, x, y)
                    weight = WEIGHT_MATRIX[y][x]  # マスの重み
                    score = flips + weight
                    moves.append((score, x, y))
        return moves

    def place(self, board, stone):
        moves = self.evaluate_moves(board, stone)
        if moves:
            moves.sort(reverse=True)
            _, x, y = moves[0]
            return x, y
        else:
            return random_place(board, stone)
