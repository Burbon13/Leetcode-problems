class Solution(object):
    def maxPoints(self, points):
        points.reverse()
        unique_points = self.__get_unique_points(points)

        line_dict = {}
        for index1 in range(1, len(unique_points)):
            the_set = set()
            for index2 in range(0, index1):
                point1 = unique_points[index1][0]
                point2 = unique_points[index2][0]
                amount_of_points = unique_points[index1][1]

                line_value = self.__get_line_value(point1, point2)
                print(point1, point2, line_value)
                if line_value in the_set:
                    continue
                the_set.add(line_value)

                if line_value in line_dict:
                    line_dict[line_value] += amount_of_points
                else:
                    line_dict[line_value] = amount_of_points

        print(line_dict)

        return max([line_dict[key] for key in line_dict]) + 1

    def __get_unique_points(self, points):
        points_dict = {}
        for point in points:
            if (point[0], point[1]) in points_dict:
                points_dict[(point[0], point[1])] += 1
            else:
                points_dict[(point[0], point[1])] = 1
        return [(key, points_dict[key]) for key in points_dict]

    def __get_line_value(self, point1, point2):
        dif_x = point1[0] - point2[0]
        dif_y = point1[1] - point2[1]

        if dif_x == 0:
            return 'y_' + str(point1[0])

        if dif_y == 0:
            return 'x_' + str(point1[1])

        y_value = (point2[1] - point1[1]) * (- point1[0] / (point2[0] - point1[0])) + point1[1]

        panta = '%.8f' % (dif_x / dif_y) + '*' + '%.8f' % (y_value)
        return panta


print(Solution().maxPoints([[1,1],[2,2],[3,3]]))
