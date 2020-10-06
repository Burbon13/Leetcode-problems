from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k: int):
        dq = deque()
        maximums = []

        for i, val in enumerate(nums):
            while len(dq) > 0 and i - dq[0][0] >= k:
                dq.popleft()
            while len(dq) > 0 and i - dq[-1][0] >= k:
                dq.pop()

            if len(dq) == 0:
                dq.append((i, val))
            elif dq[0][1] >= val:
                dq.appendleft((i, val))
            elif dq[-1][1] <= val:
                dq.append((i, val))

            if i >= k - 1:
                maximums.append(dq[-1][1])

        return maximums


sol = Solution()

assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
