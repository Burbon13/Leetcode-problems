import he

class Solution:
    def minTime(self, n: int, edges, hasApple) -> int:
        if n == 1:
            return 0

        graph = {}
        for edge in edges:
            vertex0, vertex1 = edge
            if vertex0 not in graph:
                graph[vertex0] = set()
            graph[vertex0].add(vertex1)
            if vertex1 not in graph:
                graph[vertex1] = set()
            graph[vertex1].add(vertex0)

        return self.recursive(0, graph, set(), hasApple)

    def recursive(self, node, graph, visited, hasApple):
        visited.add(node)

        total = 0

        for next_node in graph[node]:
            if next_node not in visited:
                steps = self.recursive(next_node, graph, visited, hasApple)
                if steps > 0 or hasApple[next_node]:
                    total += 2 + steps

        return total


sol = Solution()
assert sol.minTime(7,
                   [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                   [False, False, True, False, True, True, False]) == 8
assert sol.minTime(7,
                   [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                   [False, False, True, False, False, True, False]) == 6
assert sol.minTime(1, [], [True]) == 0
assert sol.minTime(1, [], [False]) == 0
assert sol.minTime(2, [[0, 1]], [False, False]) == 0
assert sol.minTime(2, [[0, 1]], [False, True]) == 2
