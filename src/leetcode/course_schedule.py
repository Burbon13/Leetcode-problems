class Graph:
    def __init__(self, numNodes):
        self._numNodes = numNodes
        self._edges = {}

    def addEdge(self, startNode, endNode):
        if startNode not in self._edges:
            self._edges[startNode] = set()
        self._edges[startNode].add(endNode)

    def containsCycle(self):
        nodesVisited = set()
        for node in range(self._numNodes):
            if node not in nodesVisited:
                if not self._recursiveTraversal(node, nodesVisited, set()):
                    print('Node: ' + str(node))
                    return False
        return True

    def _recursiveTraversal(self, currentNode, nodesVisited, currentlyVisitedNodes):
        nodesVisited.add(currentNode)

        if currentNode not in self._edges:
            return True

        currentlyVisitedNodes.add(currentNode)

        returnValue = True
        for neighbour in self._edges[currentNode]:
            if neighbour in currentlyVisitedNodes:
                return False
            if neighbour in nodesVisited:
                continue
            returnValue &= self._recursiveTraversal(neighbour, nodesVisited, currentlyVisitedNodes)

        currentlyVisitedNodes.remove(currentNode)
        return returnValue


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = Graph(numCourses)

        for course1, course2 in prerequisites:
            graph.addEdge(course1, course2)

        return graph.containsCycle()


print(Solution().canFinish(3, [[0,1],[0,2],[1,2]]))