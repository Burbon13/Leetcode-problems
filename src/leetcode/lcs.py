class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text1) + 1), [0] * (len(text1) + 1)]

        for i, c2 in enumerate(text2):
            for j, c1 in enumerate(text1):
                j = j + 1
                if c1 == c2:
                    dp[i % 2][j] = dp[(i + 1) % 2][j - 1] + 1
                else:
                    dp[i % 2][j] = max(dp[(i + 1) % 2][j], dp[i % 2][j - 1])

        return dp[(len(text2) + 1) % 2][len(text1)]


sol = Solution()
assert sol.longestCommonSubsequence("abcde", "ace") == 3
assert sol.longestCommonSubsequence("abc", "abc") == 3
assert sol.longestCommonSubsequence("abc", "def") == 0
assert sol.longestCommonSubsequence("", "") == 0
assert sol.longestCommonSubsequence("", "asdasdasda") == 0
