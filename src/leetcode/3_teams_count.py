from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        return self.oneCaseCalculate(rating) + self.oneCaseCalculate(rating[::-1])

    def oneCaseCalculate(self, rating):
        smaller = self.calculate(rating, lambda x, y: x < y)
        bigger = self.calculate(rating[::-1], lambda x, y: x > y)[::-1]

        total = 0
        for small, big in zip(smaller, bigger):
            total += small * big
        return total

    def calculate(self, rating, comparator):
        result = [0 for _ in rating]
        for i, val in enumerate(rating):
            for j in range(i):
                if comparator(rating[j], val):
                    result[i] += 1
        return result


sol = Solution()
assert sol.numTeams([2, 5, 3, 4, 1]) == 3
assert sol.numTeams([2, 1, 3]) == 0
assert sol.numTeams([1, 2, 3, 4]) == 4
