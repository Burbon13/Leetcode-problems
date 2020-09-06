class Solution:
    def findUnsortedSubarray(self, nums):
        n = len(nums)
        maxs = [0 for _ in range(n)]
        maxs[0] = nums[0]

        for i in range(1, n):
            maxs[i] = max(maxs[i - 1], nums[i])

        left = 0
        while left < n and nums[left] == maxs[left]:
            left += 1

        right = n - 1
        while right >= 0 and nums[right] == maxs[right]:
            right -= 1

        if right == -1:
            return 0

        while left > 0 and maxs[left] == maxs[left - 1]:
            left -= 1

        return right - left + 1


sol = Solution()

assert sol.findUnsortedSubarray([1, 2, 4, 5, 3]) == 3
assert sol.findUnsortedSubarray([1, 3, 2, 3, 3]) == 2
assert sol.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]) == 5
assert sol.findUnsortedSubarray([1, 2, 3, 4, 5, 6, 7, 8]) == 0
assert sol.findUnsortedSubarray([1, 2, 3, 4, 4, 7, 7, 7]) == 0
