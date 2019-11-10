class Solution:
    def jump(self, nums):
        num_of_nums = len(nums)
        # where_from[i] is a list of all indexes from where you can jump to i
        where_from = [[] for _ in range(num_of_nums)]
        dp = [num_of_nums + 1 for _ in range(num_of_nums)]
        farthest_jump = -1

        for index, value in enumerate(nums):
            how_far_now = min(num_of_nums, index + value)

            if how_far_now <= farthest_jump:
                continue

            jump = max(how_far_now - index, 1)

            farthest_jump = how_far_now

            while jump <= value and jump + index < len(nums):
                where_from[index + jump].append(index)
                jump += 1

        dp[0] = 0

        for index in range(num_of_nums):
            for previous_index in where_from[index]:
                dp[index] = min(dp[index], dp[previous_index] + 1)

        return dp[-1]


assert Solution().jump([2, 3, 1, 1, 4]) == 2
