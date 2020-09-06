class Solution:
    def solve(self, board) -> None:
        if board is None or len(board) == 0 or len(board[0]) == 0:
            return

        self.transformNonSurroundedToY(board)
        self.transform(board, 'O', 'X')
        self.transform(board, 'Y', 'O')

    def transformNonSurroundedToY(self, board):
        n, m = len(board), len(board[0])
        self.checkNonSurrounded([0, 0], (0, 1), m, board)
        self.checkNonSurrounded([0, 0], (1, 0), n, board)
        self.checkNonSurrounded([n - 1, m - 1], (0, -1), m, board)
        self.checkNonSurrounded([n - 1, m - 1], (-1, 0), n, board)

    def checkNonSurrounded(self, pos, move, steps, board):
        while steps > 0:
            if board[pos[0]][pos[1]] == 'O':
                self.fill(pos, board)
            steps -= 1
            pos[0] += move[0]
            pos[1] += move[1]

    def fill(self, pos, board):
        board[pos[0]][pos[1]] = 'Y'
        v1 = [0, 0, 1, -1]
        v2 = [1, -1, 0, 0]
        for p in range(4):
            i = pos[0] + v1[p]
            j = pos[1] + v2[p]
            try:
                if board[i][j] == 'O':
                    self.fill((i, j), board)
            except:
                pass

    def transform(self, board, from_value, to_value):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == from_value:
                    board[i][j] = to_value


sol = Solution()

input = [["X","X","X","X"],["X","O","O","X"],["X","O","O","X"],["X","O","X","X"]]
sol.solve(input)

print(input)
