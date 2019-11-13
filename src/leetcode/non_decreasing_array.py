# https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums):
        nums.insert(0, -99999999999)
        nums.append(9999999999)

        index = 1
        lives = 1
        while index < len(nums) - 1:
            if nums[index + 1] < nums[index - 1]:
                if lives > 0:
                    nums[index + 1] = nums[index]
                    lives -= 1
                else:
                    return False
            elif nums[index + 1] < nums[index]:
                if lives > 0:
                    nums[index] = nums[index + 1]
                    lives -= 1
                else:
                    return False
            index += 1

        return True


solution = Solution()

assert solution.checkPossibility([4, 2, 3]) is True
assert solution.checkPossibility([4, 2, 1]) is False
assert solution.checkPossibility([1, 2, 3]) is True
assert solution.checkPossibility([1, 1, 1, 1]) is True
assert solution.checkPossibility([3, 4, 2, 3]) is False
