# https://leetcode.com/problems/n-queens-ii/

class Solution:
    def __init__(self):
        self.__total = 0

    def totalNQueens(self, n):
        self.__total = 0
        self.__backtracking(0, n, set(), set(), set())
        return self.__total

    def __backtracking(self, pos, n, cols, diag1, diag2):
        if pos == n:
            self.__total += 1
            return

        for index in range(n):
            diag1_val = index + pos
            diag2_val = index - pos
            if index not in cols and diag1_val not in diag1 and diag2_val not in diag2:
                cols.add(index)
                diag1.add(diag1_val)
                diag2.add(diag2_val)
                self.__backtracking(pos + 1, n, cols, diag1, diag2)
                cols.remove(index)
                diag1.remove(diag1_val)
                diag2.remove(diag2_val)


solution = Solution()

assert solution.totalNQueens(4) == 2
