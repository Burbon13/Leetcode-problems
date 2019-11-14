# https://leetcode.com/problems/n-queens/

from copy import copy


class Solution:
    def __init__(self):
        self.__total = []
        self.__strings = []

    def totalNQueens(self, n):
        self.__total = []
        self.__strings = []
        for i in range(n):
            strstr = ''
            for x in range(n):
                if x == i:
                    strstr += 'Q'
                else:
                    strstr += '.'
            self.__strings.append(strstr)

        self.__backtracking(0, n, set(), set(), set(), [])
        return self.__total

    def __backtracking(self, pos, n, cols, diag1, diag2, current_progress):
        if pos == n:
            self.__total.append(copy(current_progress))
            return

        for index in range(n):
            diag1_val = index + pos
            diag2_val = index - pos
            if index not in cols and diag1_val not in diag1 and diag2_val not in diag2:
                cols.add(index)
                diag1.add(diag1_val)
                diag2.add(diag2_val)
                current_progress.append(self.__strings[index])
                self.__backtracking(pos + 1, n, cols, diag1, diag2, current_progress)
                current_progress.pop(-1)
                cols.remove(index)
                diag1.remove(diag1_val)
                diag2.remove(diag2_val)


solution = Solution()

print(solution.totalNQueens(4))