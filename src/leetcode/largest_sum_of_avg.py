# https://leetcode.com/problems/largest-sum-of-averages/

class Solution:
    def largestSumOfAverages(self, a, k):
        return self.solution_1(a, k)

    # Time complexity: O(k * n * n)
    def solution_1(self, a, k):
        dp = [
            [0 for _ in range(len(a))],
            [0 for _ in range(len(a))]
        ]

        array_sum = 0
        for index, val in enumerate(a):
            array_sum += val
            dp[1][index] = array_sum / (index + 1)

        for current_k in range(2, k + 1):
            for index in range(current_k - 1, len(a)):
                dp[current_k % 2][index] = a[index] + dp[(current_k + 1) % 2][index - 1]

                array_sum = a[index]
                count = 1
                for lower_index in range(index - 1, current_k - 2, -1):
                    array_sum += a[lower_index]
                    count += 1
                    dp[current_k % 2][index] = max(
                        dp[current_k % 2][index],
                        dp[(current_k + 1) % 2][lower_index - 1] + (array_sum / count)
                    )

        return dp[k % 2][-1]


assert Solution().solution_1([9, 1, 2, 3, 9], 3) == 20.0
assert Solution().solution_1([2], 1) == 2.0
assert Solution().solution_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == 55.0
assert Solution().solution_1([1, 2, 8, 2, 3, 8, 1, 2], 5) == 21.5
