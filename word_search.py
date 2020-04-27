# Improvement ideas: if been there with same pos, go back

directions = [
    [1, 0],
    [-1, 0],
    [0, 1],
    [0, -1]
]


class Solution:
    def exist(self, board, word):
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if self.backtracking(i, j, board, word, 0, set()):
                    return True
        return False

    def backtracking(self, i, j, board, word, index, traversed):
        if (i, j) in traversed:
            return False

        if board[i][j] != word[index]:
            return False

        if index == len(word) - 1:
            return True

        traversed.add((i, j))

        for x_pad, y_pad in directions:
            new_x = i + x_pad
            new_y = j + y_pad
            if 0 <= new_x < len(board) and 0 <= new_y < len(board[0]) and self.backtracking(new_x, new_y, board, word,
                                                                                            index + 1, traversed):
                return True

        traversed.remove((i, j))

        return False


sol = Solution()
mat1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

assert sol.exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "ABCESEEEFS")
assert sol.exist(mat1, "ABCCED")
assert sol.exist(mat1, "SEE")
assert sol.exist(mat1, "SEE")
assert sol.exist(mat1, "SFCS")
assert sol.exist(mat1, "ABCESCFSADEE")
assert not sol.exist(mat1, "ABCESCFSADEA")
assert not sol.exist(mat1, "ABCB")
