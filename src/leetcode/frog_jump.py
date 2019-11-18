# https://leetcode.com/problems/frog-jump/

from queue import SimpleQueue


class Solution:
    def canCross(self, stones):
        stone_set = set()
        visited_set = set()
        last_stone = stones[-1]

        for stone in stones:
            stone_set.add(stone)
        stone_set.remove(0)

        my_queue = SimpleQueue()
        my_queue.put((0, 0))

        while not my_queue.empty():
            stone, k = my_queue.get()
            for shift in [-1, 0, 1]:
                next_stone = stone + k + shift
                if next_stone in stone_set and (next_stone, k + shift) not in visited_set:
                    if next_stone == last_stone:
                        return True
                    visited_set.add((next_stone, k + shift))
                    my_queue.put((next_stone, k + shift))

        return False


solution = Solution()
print(solution.canCross([0, 1, 3, 5, 6, 8, 12, 17]))
print(solution.canCross([0, 1, 2, 3, 4, 8, 9, 11]))
print(solution.canCross([0, 1, 3, 6, 10, 13, 15, 18]))
