# https://leetcode.com/problems/number-of-islands/


class Solution:
    def numIslands(self, grid):
        total_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    total_count += 1
                    self.__eliminate(i, j, grid)

        return total_count

    def __eliminate(self, i, j, grid):
        grid[i][j] = '0'
        for p1, p2 in zip([-1, 1, 0, 0], [0, 0, 1, -1]):
            new_i = i + p1
            new_j = j + p2
            if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] == '1':
                self.__eliminate(new_i, new_j, grid)


print(Solution().numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
))
