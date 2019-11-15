# https://leetcode.com/problems/grid-illumination/

class Solution:
    def gridIllumination(self, n, lamps, queries):
        row_dict = {}
        col_dict = {}
        diag1_dict = {}
        diag2_dict = {}
        lamps_set = set()
        to_return = []

        for lamp in lamps:
            row, col, diag1, diag2 = self.__get_axes(lamp)
            self.__increment_dict(row_dict, row)
            self.__increment_dict(col_dict, col)
            self.__increment_dict(diag1_dict, diag1)
            self.__increment_dict(diag2_dict, diag2)
            lamps_set.add((lamp[0], lamp[1]))

        for query in queries:
            # Verifying if the position has light
            row, col, diag1, diag2 = self.__get_axes(query)
            if self.__dict_has_positive_value(row_dict, row) \
                    or self.__dict_has_positive_value(col_dict, col) \
                    or self.__dict_has_positive_value(diag1_dict, diag1) \
                    or self.__dict_has_positive_value(diag2_dict, diag2):
                to_return.append(1)
            else:
                to_return.append(0)
            # Shutting down lamps from the 3X3 matrix
            for row_shift in range(-1, 2):
                for col_shift in range(-1, 2):
                    row, col, diag1, diag2 = self.__get_axes([query[0] + row_shift, query[1] + col_shift])
                    if (row, col) in lamps_set:
                        lamps_set.remove((row, col))
                        self.__decrement_dict(row_dict, row)
                        self.__decrement_dict(col_dict, col)
                        self.__decrement_dict(diag1_dict, diag1)
                        self.__decrement_dict(diag2_dict, diag2)

        return to_return

    def __get_axes(self, lamp):
        return lamp[0], lamp[1], lamp[0] + lamp[1], lamp[1] - lamp[0]

    def __increment_dict(self, dictionary, key):
        if key not in dictionary:
            dictionary[key] = 1
        else:
            dictionary[key] += 1

    def __decrement_dict(self, dictionary, key):
        if key in dictionary and dictionary[key] > 0:
            dictionary[key] -= 1

    def __dict_has_positive_value(self, dictionary, key):
        return key in dictionary and dictionary[key] > 0


N = 5
queries = [[0, 4], [0, 1], [1, 4]]
lamps = [[0, 0], [0, 4]]

solution = Solution()

print(solution.gridIllumination(N, lamps, queries))
