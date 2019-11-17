# https://leetcode.com/problems/number-of-squareful-arrays/

class Solution:
    def numSquarefulPerms(self, nums):
        index = 0
        limit = 10 ** 9
        squares_set = set()
        while index * index <= limit:
            squares_set.add(index * index)
            index += 1

        rank_dict = {}
        new_nums = []
        for number in nums:
            if number not in rank_dict:
                rank_dict[number] = 1
            else:
                rank_dict[number] += 1
            new_nums.append((number, rank_dict[number]))

        for key in rank_dict:
            rank_dict[key] = 0
        to_return = []
        current = [0 for _ in range(len(nums))]
        return self.__recursive(new_nums, 0, current, rank_dict, squares_set)

    def __recursive(self, nums, pos, current, rank_dict, squares_set):
        if pos == len(nums):
            return 1

        total_count = 0
        for value in nums:
            if rank_dict[value[0]] == value[1] - 1 and (pos == 0 or (value[0] + current[pos - 1]) in squares_set):
                rank_dict[value[0]] += 1
                current[pos] = value[0]
                total_count += self.__recursive(nums, pos + 1, current, rank_dict, squares_set)
                rank_dict[value[0]] -= 1

        return total_count


print(Solution().numSquarefulPerms([1, 17, 8]))
