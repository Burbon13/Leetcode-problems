# https://leetcode.com/problems/top-k-frequent-elements/submissions/

from queue import PriorityQueue


class Solution:
    def topKFrequent(self, nums, k: int):
        nr_app = {}
        for value in nums:
            if value not in nr_app:
                nr_app[value] = 0
            nr_app[value] += 1

        pq = PriorityQueue()
        added = 0
        for key in nr_app:
            pq.put((nr_app[key], key))
            if added < k:
                added += 1
            else:
                pq.get()

        return [pq.get()[1] for _ in range(k)][::-1]


solution = Solution()

print(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2))
