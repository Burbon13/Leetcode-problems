MOD = 10 ** 9 + 7


class Solution:
    def numberOfArrays(self, s, k):
        if s is None or len(s) == 0:
            return 0
        if s[0] == '0':
            return 0
        if int(s[0]) > k:
            return 0

        dp = [0] * len(s)
        dp[0] = 1

        for index, val in enumerate(s[1:]):
            actual_index = index + 1

            nr = int(s[actual_index])
            power = 1

            if nr > k:
                return 0

            if nr > 0:
                dp[actual_index] = dp[actual_index - 1]

            i = actual_index - 1
            while nr <= k and i >= 0:
                power *= 10
                nr += power * int(s[i])
                if k >= nr and nr > 0 and s[i] != '0':
                    dp[actual_index] += dp[i - 1] if i > 0 else 1
                    dp[actual_index] %= MOD
                i -= 1

            if dp[actual_index] == 0:
                return 0

        return dp[-1]


sol = Solution()

assert sol.numberOfArrays("2020", 30) == 1
assert sol.numberOfArrays("1000", 10000) == 1
assert sol.numberOfArrays("1000", 10) == 0
assert sol.numberOfArrays("1317", 2000) == 8
assert sol.numberOfArrays("1234567890", 90) == 34
