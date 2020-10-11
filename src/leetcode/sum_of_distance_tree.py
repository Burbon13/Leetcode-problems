from typing import List


class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        graph = {}
        for node1, node2 in edges:
            if node1 not in graph:
                graph[node1] = []
            graph[node1].append(node2)

            if node2 not in graph:
                graph[node2] = []
            graph[node2].append(node1)

        const_sums = {}
        self.recursiveSums(0, -1, graph, const_sums)
        results = [0 for _ in range(N)]
        self.recursiveCalc(0, -1, 0, 0, graph, const_sums, results)
        return results

    def recursiveSums(self, node, parent, graph, const_sums):
        total = 0
        nodes = 1

        for son in graph[node]:
            if son != parent:
                self.recursiveSums(son, node, graph, const_sums)
                total += const_sums[son][0] + 1 * const_sums[son][1]
                nodes += const_sums[son][1]

        const_sums[node] = (total, nodes)

    def recursiveCalc(self, node, parent, parentSum, parentNodes, graph, const_sums, results):
        total = parentSum + 1 * parentNodes
        totalNodes = parentNodes

        for son in graph[node]:
            if son != parent:
                total += const_sums[son][0] + 1 * const_sums[son][1]
                totalNodes += const_sums[son][1]

        results[node] = total

        for son in graph[node]:
            if son != parent:
                newTotal = total - const_sums[son][0] - 1 * const_sums[son][1]
                newTotalNodes = totalNodes - const_sums[son][1] + 1
                self.recursiveCalc(son, node, newTotal, newTotalNodes, graph, const_sums, results)


sol = Solution()

assert sol.sumOfDistancesInTree(6, [[0, 1], [0, 2], [2, 3], [2, 4], [2, 5]]) == [8, 12, 6, 10, 10, 10]
