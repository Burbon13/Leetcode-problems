# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution:
    def removeDuplicates(self, nums):
        len_new_list = len(nums)

        head_index = 1
        current_index = 2

        while current_index < len(nums):
            if nums[current_index] != nums[head_index] or nums[current_index] != nums[head_index - 1]:
                nums[head_index + 1] = nums[current_index]
                head_index += 1
            else:
                len_new_list -= 1
            current_index += 1

        return len_new_list


solution = Solution()

array1 = [1,1,1,2,2,3]
resu