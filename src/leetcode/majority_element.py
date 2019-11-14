# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums):
        el_maj = nums[0]
        count = 1

        for index in range(1, len(nums)):
            if nums[index] == el_maj:
                count += 1
            else:
                count -= 1
                if count < 0:
                    count = 1
                    el_maj = nums[index]

        return el_maj


solution = Solution()

assert solution.majorityElement([3, 2, 3]) == 3
assert solution.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
assert solution.majorityElement([2, 2, 1, 1, 1, 1, 2]) == 1
