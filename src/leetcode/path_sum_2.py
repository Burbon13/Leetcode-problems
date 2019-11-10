# https://leetcode.com/problems/path-sum-ii

from copy import deepcopy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int):
        to_return = []
        self.__get_all_leafs_paths_of_sum(root, sum, to_return, [])
        return to_return

    def __get_all_leafs_paths_of_sum(self, root: TreeNode, sum: int, to_return, current_path):
        if root is None:
            return

        sum -= root.val
        current_path.append(root.val)

        if root.left is None and root.right is None:
            if sum == 0:
                to_return.append(deepcopy(current_path))
        else:
            if root.left:
                self.__get_all_leafs_paths_of_sum(root.left, sum, to_return, current_path)
            if root.right:
                self.__get_all_leafs_paths_of_sum(root.right, sum, to_return, current_path)

        current_path.pop()
