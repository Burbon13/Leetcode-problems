# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __repr__(self):
        return f'Val {self.val} next {self.next.val if self.next is not None else None}'


class Solution:
    def __init__(self):
        self.__node_dict = None

    def connect(self, root):
        if root is None:
            return None

        self.__node_dict = {}
        self.__traverse(root, 0)
        return root

    def __traverse(self, node, row):
        if row in self.__node_dict:
            self.__node_dict[row].next = node
        self.__node_dict[row] = node

        if node.left is not None:
            self.__traverse(node.left, row + 1)
        if node.right is not None:
            self.__traverse(node.right, row + 1)


node7 = Node(7, None, None, None)
node6 = Node(6, None, None, None)
node5 = Node(5, None, None, None)
node4 = Node(4, None, None, None)
node3 = Node(3, None, node7, None)
node2 = Node(2, node4, node5, None)
node1 = Node(1, node2, node3, None)

solution = Solution()
solution.connect(node1)

print(node1)
print(node2)
print(node3)
print(node4)
print(node5)
print(node6)
print(node7)
