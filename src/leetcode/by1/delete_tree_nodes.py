class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        tree_dict = {}
        for index, par_index in enumerate(parent):
            node1, node2 = index, par_index
            if node2 == -1:
                continue
            if node2 in tree_dict:
                tree_dict[node2].append(node1)
            else:
                tree_dict[node2] = [node1]

        print(tree_dict)
        return nodes - self.__recursive(0, tree_dict, value)[0]

    def __recursive(self, node, tree_dict, values):
        """ Returns (scoase/ramase subtree/sum) """

        total_out = 0
        current_sum = values[node]
        current_nodes = 1
        if node in tree_dict:
            for next_node in tree_dict[node]:
                put_out, remain, the_sum = self.__recursive(next_node, tree_dict, values)
                total_out += put_out
                current_sum += the_sum
                current_nodes += remain

        if current_sum == 0:
            (total_out + current_nodes, 0, 0)

        return (total_out, current_nodes, current_sum)


print(Solution().deleteTreeNodes(7, [-1,0,0,1,2,2,2], ))