class Solution:
    def checkStraightLine(self, coordinates):
        if len(coordinates) < 3:
            return True

        coordinates.sort()

        diffx = coordinates[0][0] - coordinates[1][0]
        diffy = coordinates[0][1] - coordinates[1][1]

        for index in range(2, len(coordinates)):
            cur_dif_x = coordinates[index - 1][0] - coordinates[index][0]
            cur_dif_y = coordinates[index - 1][1] - coordinates[index][1]
            if diffx * cur_dif_y != diffy * cur_dif_x:
                return False

        return True


sol = Solution()

assert sol.checkStraightLine([[-3, -2], [-1, -2], [2, -2], [-2, -2], [0, -2]])
assert sol.checkStraightLine([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
assert not sol.checkStraightLine([[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]])
