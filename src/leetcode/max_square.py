class Solution:
    def maximalSquare(self, matrix) -> int:
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        result = 0

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    result = max(result, dp[i][j])

        return result * result


sol = Solution()

assert sol.maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]) == 4

assert sol.maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "0", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "0", "0", "1", "0"]]) == 4

assert sol.maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "0", "1"],
     ["1", "1", "1", "0", "1"],
     ["1", "0", "0", "1", "0"]]) == 1

assert sol.maximalSquare(
    [["1", "0", "1", "0", "0"],
     ["1", "0", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "1", "1", "1", "1"]]) == 9

assert sol.maximalSquare(
    [["1", "1", "1", "1", "0"],
     ["1", "1", "1", "1", "1"],
     ["1", "1", "1", "1", "1"],
     ["1", "1", "1", "1", "0"]]) == 16
