class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[left] <= target <= nums[middle]:
                right = middle - 1
            elif (nums[left] <= target or target < nums[middle]) and nums[middle] < nums[left]:
                right = middle - 1
            else:
                left = middle + 1

        return -1


sol = Solution()

assert sol.search([4, 5, 6, 7, 8, 1, 2, 3], 8) == 4
assert sol.search([4, 5, 6, 7, 0, 1, 2], 0) == 4
assert sol.search([4, 5, 6, 7, 0, 1, 2], 1) == 5
assert sol.search([4, 5, 6, 7, 0, 1, 2], 2) == 6
assert sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
assert sol.search([4, 5, 6, 7, 0, 1, 2], 4) == 0
assert sol.search([4, 5, 6, 7, 0, 1, 2], 5) == 1
assert sol.search([4, 5, 6, 7, 0, 1, 2], 6) == 2
assert sol.search([4, 5, 6, 7, 0, 1, 2], 7) == 3
assert sol.search([4, 5, 6, 7, 0, 1, 2], 7321) == -1
