# https://leetcode.com/problems/rotate-function/

class Solution:
    def maxRotateFunction(self, the_list):
        if len(the_list) == 0:
            return 0
        current_f_value = self.__f_value(the_list)
        maximum_value = current_f_value
        list_sum = sum(the_list)
        n = len(the_list)
        last_pos = n - 1
        for index in range(n - 1):
            current_f_value += list_sum
            current_f_value -= the_list[last_pos] * n
            last_pos -= 1
            maximum_value = max(maximum_value, current_f_value)

        return maximum_value

    def __f_value(self, the_list):
        return sum([index * val for index, val in enumerate(the_list)])


print(Solution().maxRotateFunction([1, 1, 1, 9, 1, 1, 1, 8, 8, 8, 8, -2, 8, 8, -8, -8, -2]))
