class Solution:
    def findTargetSumWays(self, nums, S):
        if abs(S) > 1000:
            return 0

        dp = [[0 for _ in range(2002)] for _ in range(2)]
        dp[0][1000] = 1

        for val in nums:
            for i in range(-1000, 1000):
                if dp[0][i + 1000] == 0:
                    continue
                if i + val <= 1000:
                    dp[1][i + val + 1000] += dp[0][i + 1000]
                if i - val >= -1000:
                    dp[1][i - val + 1000] += dp[0][i + 1000]

            for i in range(-1000, 1001):
                dp[0][i + 1000] = dp[1][i + 1000]
                dp[1][i + 1000] = 0

            # print(dp[0][995:1005])

        return dp[0][S + 1000]


sol = Solution()

assert sol.findTargetSumWays([1000], 1000) == 1
assert sol.findTargetSumWays([1], 1) == 1
assert sol.findTargetSumWays([1, 1, 1, 1, 1], 3) == 5
