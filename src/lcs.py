class Solution:
    def longestConsecutive(self, nums):
        forest = Forest()

        for val in nums:
            left = val - 1
            right = val + 1

            left_group = forest.get_group(left)
            right_group = forest.get_group(right)
            forest.unite_groups(left_group, right_group, val)

        return forest.get_max_size()


class Forest:
    def __init__(self):
        self._groups = {}
        self._organization = {}
        self._size = 0

    def get_group(self, group_id):
        return -1 if group_id not in self._groups else self._groups[group_id]

    def get_max_size(self):
        return max([len(self._organization[x]) for x in self._organization]) if self._size > 0 else 0

    def unite_groups(self, group1, group2, new_val):
        if new_val in self._groups:
            return
        new_group_val = self._unite(group1, group2)
        self._add(new_group_val, new_val)

    def _unite(self, group1, group2):
        if group1 == -1 and group2 == -1:
            return -1
        if group1 == -1:
            return group2
        if group2 == -1:
            return group1

        for x in self._organization[group2]:
            self._groups[x] = group1

        self._organization[group1] = [*self._organization[group1], *self._organization[group2]]

        del self._organization[group2]

        return group1

    def _add(self, group, new_val):
        if group == -1:
            self._size += 1
            self._groups[new_val] = self._size
            self._organization[self._size] = [new_val]
        else:
            self._groups[new_val] = group
            self._organization[group].append(new_val)


solution = Solution()

print(solution.longestConsecutive([]))
