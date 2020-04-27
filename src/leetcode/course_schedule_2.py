class Solution:
    def findOrder(self, numCourses, prerequisites):
        graph = {}
        nr_before = {}
        for second, first in prerequisites:
            if first not in graph:
                graph[first] = []
            if second not in nr_before:
                nr_before[second] = 0
            graph[first].append(second)
            nr_before[second] += 1

        order = []
        added = set()
        for course in range(numCourses):
            if course not in added and (course not in nr_before or nr_before[course] == 0):
                self.recursive(course, graph, nr_before, order, added)

        return order if len(order) == numCourses else []

    def recursive(self, course, graph, nr_before, order, added):
        order.append(course)
        added.add(course)
        if course in graph:
            for next_course in graph[course]:
                nr_before[next_course] -= 1
                if nr_before[next_course] == 0:
                    self.recursive(next_course, graph, nr_before, order, added)


sol = Solution()

assert sol.findOrder(2, [[1, 0]]) == [0, 1]
assert sol.findOrder(2, [[1, 0], [0,1]]) == []
assert sol.findOrder(3, [[1, 0], [0,1]]) == []
assert sol.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 1, 2, 3] or sol.findOrder(4, [[1, 0], [2, 0], [3, 1],
                                                                                               [3, 2]]) == [0, 2, 1, 3]
