class Solution:
    def minPathSum(self, grid):
        if grid is None or len(grid) == 0:
            return 0
        if len(grid[0]) == 0:
            return 0

        dp = grid[0]
        for index in range(1, len(dp)):
            dp[index] += dp[index - 1]

        for row in grid[1:]:
            new_dp = [0] * len(dp)
            new_dp[0] = dp[0] + row[0]
            for index, cell in enumerate(row[1:]):
                new_dp[index + 1] = min(new_dp[index], dp[index + 1]) + cell
            dp = new_dp

        return dp[-1]


sol = Solution()

assert sol.minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]) == 7
assert sol.minPathSum([[1, 3, 1]]) == 5
assert sol.minPathSum([
    [1],
    [1],
    [4]
]) == 6
assert sol.minPathSum([]) == 0
assert sol.minPathSum([[], []]) == 0
assert sol.minPathSum([
    [1, 3, 8],
    [1, 5, 8],
    [4, 2, 1]
]) == 9
assert sol.minPathSum([
    [1, 3, 1],
    [19, 5, 99],
    [99, 2, 1]
]) == 12
