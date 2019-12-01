class Solution:
    def findRedundantConnection(self, edges):
        if edges is None:
            return None

        group = [index for index in range(len(edges) + 1)]
        group_dict = {}
        for index in range(len(edges)):
            group_dict[index + 1] = [index + 1]

        print(group)
        print(group_dict)

        for edge in edges:
            node1, node2 = edge

            if group[node1] == group[node2]:
                return edge

            if len(group_dict[group[node1]]) < len(group_dict[group[node2]]):
                node1, node2 = node2, node1

            new_group_value = group[node1]
            old_group = group[node2]
            for node in group_dict[old_group]:
                group_dict[group[node1]].append(node)
                group[node] = new_group_value
            group_dict[old_group] = []
            #
            # print(edge)
            # print(group)
            # print(group_dict)
            # print('==========================')


print(Solution().findRedundantConnection([[3, 4], [1, 2], [2, 4], [3, 5], [2, 5]]))
