# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, t):
        results = [0] * len(t)
        sorted_temperatures = [[0, 0] for _ in range(len(t))]
        sorted_temperatures[0] = [0, t[0]]
        len_s_t = 1

        for index in range(1, len(t)):
            while len_s_t > 0 and t[index] > sorted_temperatures[len_s_t - 1][1]:
                results[sorted_temperatures[len_s_t - 1][0]] = index - sorted_temperatures[len_s_t - 1][0]
                len_s_t -= 1

            sorted_temperatures[len_s_t][1] = t[index]
            sorted_temperatures[len_s_t][0] = index
            len_s_t += 1

        return results


solution = Solution()
print(solution.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
assert solution.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]

# bs_list = [70, 60, 50, 40]
# assert solution.binary_search(bs_list, 75) == 0
# assert solution.binary_search(bs_list, 70) == 0
# assert solution.binary_search(bs_list, 65) == 1
# assert solution.binary_search(bs_list, 60) == 1
# assert solution.binary_search(bs_list, 55) == 2
# assert solution.binary_search(bs_list, 50) == 2
# assert solution.binary_search(bs_list, 45) == 3
# assert solution.binary_search(bs_list, 40) == 3
# assert solution.binary_search(bs_list, 35) == 4
#
# bs_list = [70, 60, 50, 40, 30]
# assert solution.binary_search(bs_list, 75) == 0
# assert solution.binary_search(bs_list, 70) == 0
# assert solution.binary_search(bs_list, 65) == 1
# assert solution.binary_search(bs_list, 60) == 1
# assert solution.binary_search(bs_list, 55) == 2
# assert solution.binary_search(bs_list, 50) == 2
# assert solution.binary_search(bs_list, 45) == 3
# assert solution.binary_search(bs_list, 40) == 3
# assert solution.binary_search(bs_list, 35) == 4
# assert solution.binary_search(bs_list, 30) == 4
# assert solution.binary_search(bs_list, 25) == 5
#
# bs_list = [(0, 70), (0, 60), (0, 60), (0, 60), (0, 60), (0, 50)]
# print(solution.binary_search(bs_list, 61))
# assert solution.binary_search(bs_list, 61) == 4
# assert solution.binary_search(bs_list, 60) == 1
# assert solution.binary_search(bs_list, 51) == 5
# assert solution.binary_search(bs_list, 42) == 6
# assert solution.binary_search(bs_list, 40) == 6
# assert solution.binary_search(bs_list, 31) == 8
# assert solution.binary_search(bs_list, 30) == 8
# assert solution.binary_search(bs_list, 29) == 10
