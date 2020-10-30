from typing import List


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1, y1 = points[0]
        x2, y2 = points[1]
        x3, y3 = points[2]

        if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
            return False

        angle_1 = (x1 - x2) / (y1 - y2) if y1 - y2 != 0 else 'horizontal'
        angle_2 = (x1 - x3) / (y1 - y3) if y1 - y3 != 0 else 'horizontal'

        return angle_1 != angle_2


sol = Solution()

assert sol.isBoomerang([[0, 0], [0, 100000], [0, 200000]])
assert not sol.isBoomerang([[0, 0], [0, 100000], [1, 200000]])
assert sol.isBoomerang([[0, 1], [2, 2], [2, 0]])
assert sol.isBoomerang([[0, 0], [0, 2], [2, 1]])
assert sol.isBoomerang([[1, 1], [2, 3], [3, 2]])
assert not sol.isBoomerang([[1, 1], [2, 2], [3, 3]])
