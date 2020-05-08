moves = (
    (1, 0),
    (-1, 0),
    (0, 1),
    (0, -1)
)


class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        values = []

        for i, row in enumerate(matrix):
            for j, val in enumerate(row):
                values.append((val, i, j))

        values.sort(reverse=True)

        max_val = 0
        dp = [[1 for _ in range(m)] for _ in range(n)]
        for val, i, j in values:
            for next_move in moves:
                next_i = i + next_move[0]
                next_j = j + next_move[1]
                if 0 <= next_i < n and 0 <= next_j < m:
                    if matrix[next_i][next_j] < matrix[i][j]:
                        dp[next_i][next_j] = max(dp[next_i][next_j], dp[i][j] + 1)
                        max_val = max(max_val, dp[next_i][next_j])

        return max_val


sol = Solution()

assert sol.longestIncreasingPath([
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
]) == 4

assert sol.longestIncreasingPath([
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]) == 4

assert sol.longestIncreasingPath([]) == 0

assert sol.longestIncreasingPath([[], []]) == 0
