class Solution:
    def removeBoxes(self, boxes):
        k = len(boxes)
        dp = [[0 for _ in range(k)] for _ in range(k)]
        result = self.recursiveDP(boxes, 0, k - 1, dp)
        # print(dp)
        return result

    def recursiveDP(self, boxes, left, right, dp):
        if left > right:
            return 0

        if dp[left][right] > 0:
            return dp[left][right]

        if left == right:
            dp[left][right] = 1
            return 1

        # Left expansion
        current_sum = 0
        dp[left][right] = 1 + self.recursiveDP(boxes, left + 1, right, dp)
        index = left + 1
        total = 1
        last_left = left
        while index <= right:
            if boxes[index] == boxes[left]:
                total += 1
                current_sum += self.recursiveDP(boxes, last_left + 1, index - 1, dp)
                dp[left][right] = max(dp[left][right],
                                      current_sum + total ** 2 + self.recursiveDP(boxes, index + 1, right, dp))
                last_left = index
            index += 1

        # Right expansion
        current_sum = 0
        dp[left][right] = max(dp[left][right], 1 + self.recursiveDP(boxes, left, right - 1, dp))
        index = right - 1
        total = 1
        last_right = right
        while index >= left:
            if boxes[index] == boxes[right]:
                total += 1
                current_sum += self.recursiveDP(boxes, index + 1, last_right - 1, dp)
                dp[left][right] = max(dp[left][right],
                                      current_sum + total ** 2 + self.recursiveDP(boxes, left, index - 1, dp))
                last_right = index
            index -= 1

        return dp[left][right]


sol = Solution()

assert sol.removeBoxes([5, 3, 5, 3, 3, 3, 3, 5]) == 30
assert sol.removeBoxes([3, 5, 3, 3, 3, 3]) == 26
assert sol.removeBoxes([8, 8, 5, 5]) == 8
assert sol.removeBoxes([9, 3, 6, 8, 8, 1, 2, 5, 5, 6]) == 16
assert sol.removeBoxes([1, 2, 3, 1, 2, 3]) == 8
assert sol.removeBoxes([1, 2, 1, 1, 1, 1, 1, 1, 2, 1, 1, 2]) == 84
assert sol.removeBoxes([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 15
assert sol.removeBoxes([1, 1]) == 4
assert sol.removeBoxes([1, 1, 1]) == 9
assert sol.removeBoxes([1, 2, 1, 1]) == 10
assert sol.removeBoxes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
assert sol.removeBoxes([1, 2]) == 2
assert sol.removeBoxes([]) == 0
assert sol.removeBoxes([1]) == 1
assert sol.removeBoxes([10]) == 1
assert sol.removeBoxes([200]) == 1
assert sol.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23
# assert sol.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23
# assert sol.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23
# assert sol.removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23
