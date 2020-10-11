from typing import List


class Solution:
    def sortItems(self, n: int, m: int, group: List[int], before_items: List[List[int]]) -> List[int]:
        # Step 1 - assign each item to a group (even the ones which do not belong to any)
        groups_set = set()
        nodes_in_group = set()
        self.assignToGroups(n, m, group, groups_set, nodes_in_group)
        print(group, groups_set)

        # Step 2
        graph = {}
        self.generateGraph(n, m, group, before_items, nodes_in_group, graph)

    def assignToGroups(self, n, m, groups, groups_set, nodes_in_group):
        for i in range(n):
            if groups[i] == -1:
                groups[i] = m
                m += 1
            groups_set.add(groups[i])
            if groups[i] not in nodes_in_group:
                nodes_in_group[groups[i]] = set()
            nodes_in_group[groups[i]].add(i)

    def generateGraph(self, n, m, group, before_items, nodes_in_group, graph):
        groups_dependencies = set()
        for element in range(n):
            for must_be_before in before_items[element]:
                group_before = graph[must_be_before]
                group_after = graph[element]
                if must_be_before not in graph:
                    graph[must_be_before] = set()
                graph[must_be_before].add(element)
                if group_before != group_after and (group_before, group_after) not in groups_dependencies:
                    for before_node in nodes_in_group[group_before]:
                        for after_node in nodes_in_group[element]:


sol = Solution()

sol.sortItems(8, 2, [-1, -1, 1, 0, 0, 1, 0, -1], [[], [6], [5], [6], [3, 6], [], [], []])
