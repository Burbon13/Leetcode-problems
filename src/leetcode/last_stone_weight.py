from queue import PriorityQueue


class Solution:
    def lastStoneWeight(self, stones) -> int:
        if stones is None or len(stones) == 0:
            return None

        if len(stones) == 1:
            return stones[0]

        prq = PriorityQueue()
        for stone in stones:
            prq.put(-stone)

        while True:
            vmare = -prq.get()
            if prq.empty():
                return vmare
            vmaricel = -prq.get()

            print(vmare, vmaricel)

            if prq.empty():
                return vmare - vmaricel

            if vmare != vmaricel:
                prq.put(vmaricel - vmare)



print(Solution().lastStoneWeight([2,7,4,1,8,1]))