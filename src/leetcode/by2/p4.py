class Solution:
    def minFallingPathSum(self, arr) -> int:
        if len(arr) == 1:
            return arr[0][0]

        dp = [[-999999 for _ in range(len(arr))] for _ in range(len(arr))]
        dp[0] = arr[0]

        vals = sorted(arr[0])
        minimum = vals[0]
        next_minimum = vals[1]

        for row in range(1, len(arr)):
            min1 = 9999999
            next_min1 = 99999999
            for col in range(len(arr)):
                if minimum == dp[row - 1][col]:
                    dp[row][col] = arr[row][col] + next_minimum
                else:
                    dp[row][col] = arr[row][col] + minimum

                cur_val = dp[row][col]
                if cur_val < min1:
                    next_min1 = min1
                    min1 = cur_val
                elif cur_val < next_min1:
                    next_min1 = cur_val

            minimum, next_minimum = min1, next_min1

        return min(dp[-1])


solution = Solution()
print(solution.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]))