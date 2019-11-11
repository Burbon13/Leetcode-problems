# https://leetcode.com/problems/subsets/


from copy import deepcopy


class Solution:
    def subsets(self, nums):
        solutions = []
        self.__bckt_generation(0, nums, [], solutions)
        return solutions

    def __bckt_generation(self, index, nums, current_sol, solutions):
        if index == len(nums):
            solutions.append(deepcopy(current_sol))
            return

        self.__bckt_generation(index + 1, nums, current_sol, solutions)
        current_sol.append(nums[index])
        self.__bckt_generation(index + 1, nums, current_sol, solutions)
        current_sol.pop()


print(Solution().subsets([1, 2, 3]))
