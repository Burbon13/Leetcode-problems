from copy import deepcopy
from typing import List


class BigNumber:
    def __init__(self, nr=None):
        if nr is None:
            self.nr = {}
        else:
            self.nr = deepcopy(nr)

    def addDigit(self, digit):
        self.nr[digit] = self.nr.get(digit, 0) + 1

    def toString(self) -> str:
        nr_str = ''
        for digit in range(9, -1, -1):
            if digit in self.nr:
                nr_str += str(digit) * self.nr[digit]
        return nr_str if len(nr_str) > 0 else '0'


class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [BigNumber() for _ in range(target + 1)]
        used = [False for _ in range(target + 1)]
        used[0] = True

        for i in range(1, target + 1):
            for new_digit in range(9):
                old_target = i - cost[new_digit]
                if old_target < 0 or not used[old_target]:
                    continue
                new_nr = BigNumber(dp[old_target].nr)
                new_nr.addDigit(new_digit + 1)

                nr1s = new_nr.toString()
                nr2s = dp[i].toString()
                if len(nr1s) > len(nr2s):
                    dp[i] = new_nr
                    used[i] = True
                elif len(nr1s) == len(nr2s) and nr1s > nr2s:
                    dp[i] = new_nr
                    used[i] = True

        # print([dp[x].toString() for x in range(target + 1)])
        return dp[target].toString()


sol = Solution()
assert sol.largestNumber([4, 3, 2, 5, 6, 7, 2, 5, 5], 9) == "7772"
assert sol.largestNumber([7, 6, 5, 5, 5, 6, 8, 7, 8], 12) == "85"
assert sol.largestNumber([2, 4, 6, 2, 4, 6, 4, 4, 4], 5) == "0"
assert sol.largestNumber([6, 10, 15, 40, 40, 40, 40, 40, 40], 47) == "32211"
