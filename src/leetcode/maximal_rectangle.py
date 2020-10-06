class Solution:
    def maximalRectangle(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        height = [0 for _ in range(n)]
        left = [0 for _ in range(n)]
        right = [n for _ in range(n)]
        total_max = 0

        for i in range(m):
            cur_right = n
            cur_left = 0

            # Height calculus
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            # Left calculus
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(cur_left, left[j])
                else:
                    left[j] = 0
                    cur_left = j + 1

            # Right calculus
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(cur_right, right[j])
                else:
                    right[j] = n
                    cur_right = j

            # Max calculus
            for j in range(n):
                total_max = max(total_max, (right[j] - left[j]) * height[j])

        return total_max


sol = Solution()

assert sol.maximalRectangle(
    [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]) == 6
assert sol.maximalRectangle([]) == 0
assert sol.maximalRectangle([["0"]]) == 0
assert sol.maximalRectangle([["1"]]) == 1
assert sol.maximalRectangle([["0", "0"]]) == 0
assert sol.maximalRectangle([["1", "1", "0"]]) == 2
