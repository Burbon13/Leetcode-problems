# https://leetcode.com/problems/serialize-and-deserialize-bst/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return '-'

        return '(' + str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right) + ')'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.__serialize(data, 0, len(data) - 1)

    def __serialize(self, data, left, right):
        if left == right:
            return None

        left += 1
        right -= 1
        index = left
        interior = 0
        comma_list_pos = []
        while index < right:
            if data[index] == '(':
                interior += 1
            elif data[index] == ')':
                interior -= 1
            elif data[index] == ',' and interior == 0:
                comma_list_pos.append(index)
                if len(comma_list_pos) == 2:
                    break
            index += 1

        value = int(data[left:comma_list_pos[0]])
        node = TreeNode(value)
        node.left = self.__serialize(data, comma_list_pos[0] + 1, comma_list_pos[1] - 1)
        node.right = self.__serialize(data, comma_list_pos[1] + 1, right)
        return node


root = TreeNode(1)
left = TreeNode(2)
right = TreeNode(3)
root.left = left
root.right = right

codec = Codec()

print(codec.serialize(root))
codec.deserialize(codec.serialize(root))
