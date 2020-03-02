from copy import deepcopy


class Solution:
    def trapRainWater(self, heightMap):
        left_to_right = deepcopy(heightMap)
        right_to_left = deepcopy(heightMap)
        up_to_bottom = deepcopy(heightMap)
        bottom_to_up = deepcopy(heightMap)

        for line in left_to_right:
            for index in range(1, len(line)):
                line[index] = max(line[index - 1], line[index])

        for line in right_to_left:
            for index in range(len(line) - 2, -1, -1):
                line[index] = max(line[index + 1], line[index])

        for column in range(0, len(up_to_bottom[0])):
            for row in range(1, len(up_to_bottom)):
                up_to_bottom[row][column] = max(up_to_bottom[row - 1][column], up_to_bottom[row][column])

        for column in range(0, len(bottom_to_up[0])):
            for row in range(len(bottom_to_up) - 2, -1, -1):
                bottom_to_up[row][column] = max(bottom_to_up[row + 1][column], bottom_to_up[row][column])

        total = 0

        for row in range(1, len(heightMap) - 1):
            for column in range(1, len(heightMap[0]) - 1):
                difference = min(
                    left_to_right[row][column],
                    right_to_left[row][column],
                    up_to_bottom[row][column],
                    bottom_to_up[row][column]
                ) - heightMap[row][column]
                difference = max(0, difference)
                print(difference, end=' ')
                total += difference
            print('')

        return total


solution = Solution()
print(solution.trapRainWater([[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]))
