class Solution:
    def firstMissingPositive(self, nums):
        for i in range(len(nums)):
            if nums[i] == 'x':
                continue
            if nums[i] <= 0 or nums[i] > len(nums):
                continue
            self.cyclic(nums[i], nums)

        i = 1
        while i <= len(nums) and nums[i - 1] == 'x':
            i += 1
        return i

    def cyclic(self, val, nums):
        while 0 < val <= len(nums) and nums[val - 1] != 'x':
            next_val = nums[val - 1]
            nums[val - 1] = 'x'
            val = next_val


sol = Solution()

assert sol.firstMissingPositive([]) == 1
assert sol.firstMissingPositive([1]) == 2
assert sol.firstMissingPositive([2]) == 1
assert sol.firstMissingPositive([3, 4, -1, 1]) == 2
assert sol.firstMissingPositive([1, 2, 0]) == 3
assert sol.firstMissingPositive([7, 8, 9, 11, 12]) == 1
assert sol.firstMissingPositive([7, 8, 9, 11, 12, 2, 3, 4]) == 1
assert sol.firstMissingPositive([7, 8, 9, 11, 12, 2, 3, 4, 1, 2, 3, 4, 8]) == 5
