class Solution:
    def findMin(self, nums):
        return self.recursiveBS(nums, 0, len(nums) - 1, nums[-1])

    def recursiveBS(self, nums, left, right, leftmost):
        if left == right:
            return nums[left]
        if left + 1 == right:
            return min(nums[left], nums[right])

        middle = (left + right) // 2

        if nums[middle] < leftmost:
            return min(nums[middle], self.recursiveBS(nums, left, middle - 1, leftmost))
        if nums[middle] == leftmost:
            return min(
                nums[middle],
                self.recursiveBS(nums, left, middle - 1, leftmost),
                self.recursiveBS(nums, middle + 1, right, leftmost)
            )
        return min(nums[middle], self.recursiveBS(nums, middle + 1, right, leftmost))


sol = Solution()
assert sol.findMin([3, 3, 1, 3]) == 1
assert sol.findMin([3, 3, 3, 3, 3, 3, 3, 3, 3, 1, 3]) == 1
assert sol.findMin([1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 1
assert sol.findMin([3, 3, 1, 3, 3, 3, 3, 3, 3, 3, 3]) == 1
assert sol.findMin([1, 3, 5]) == 1
assert sol.findMin([69]) == 69
assert sol.findMin([2, 2, 2, 0, 1]) == 0
assert sol.findMin([3, 1, 3]) == 1
assert sol.findMin([3, 3, 3]) == 3
assert sol.findMin([8, 8, 8, 8, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6]) == 2
assert sol.findMin([8, 8, 8, 8, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 8, 8, 8]) == 2
assert sol.findMin([2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 8, 8, 8]) == 2
