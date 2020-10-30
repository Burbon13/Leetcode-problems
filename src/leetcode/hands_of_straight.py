from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        n = len(hand)
        if n % W != 0:
            return False

        counter = {}
        values = set()
        for val in hand:
            counter[val] = counter.get(val, 0) + 1
            values.add(val)

        for group in range(n // W):
            first_val = min(values)
            counter[first_val] -= 1
            if counter[first_val] == 0:
                del counter[first_val]
                values.remove(first_val)
            next_val = first_val + 1
            for step in range(1, W):
                if next_val not in values:
                    return False
                counter[next_val] -= 1
                if counter[next_val] == 0:
                    del counter[next_val]
                    values.remove(next_val)
                next_val += 1

        return True


sol = Solution()
assert sol.isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3)
assert not sol.isNStraightHand([1, 2, 3, 4, 5], 4)
