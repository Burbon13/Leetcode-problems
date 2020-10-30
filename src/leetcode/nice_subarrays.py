from typing import List


class FinishedException(Exception):
    pass


class Position:
    def __init__(self, nums: List[int], k: int):
        self.nums = nums
        self.n = len(nums)

        self.left = 0
        self.in_left = 0

        while self.in_left < self.n and not self.isOdd(nums[self.in_left]):
            self.in_left += 1

        if self.in_left == self.n:
            raise FinishedException("Finished")

        self.in_right = self.in_left
        while k > 0 and self.in_right < self.n:
            if self.isOdd(nums[self.in_right]):
                k -= 1
                if k > 0:
                    self.in_right += 1
            else:
                self.in_right += 1

        if k > 0:
            raise FinishedException("Finished")

        self.right = self.in_right
        while self.right + 1 < self.n and not self.isOdd(nums[self.right + 1]):
            self.right += 1

    def makeStep(self) -> None:
        if self.right == self.n - 1:
            raise FinishedException("Finished")

        self.in_left += 1
        self.left = self.in_left
        while self.in_left < self.n and not self.isOdd(self.nums[self.in_left]):
            self.in_left += 1

        self.right += 1
        self.in_right = self.right
        while self.right + 1 < self.n and not self.isOdd(self.nums[self.right + 1]):
            self.right += 1

    def getSubArrays(self) -> int:
        return (self.in_left - self.left + 1) * (self.right - self.in_right + 1)

    def isOdd(self, nr: int) -> bool:
        return nr % 2 == 1


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total = 0
        try:
            pos = Position(nums, k)
            while True:
                total += pos.getSubArrays()
                pos.makeStep()
        except FinishedException:
            return total


sol = Solution()

assert sol.numberOfSubarrays(nums=[2, 8, 4, 2, 4, 8, 2, 8, 2, 8, 2, 20, 30, 44, 66], k=1) == 0
assert sol.numberOfSubarrays(nums=[2, 8, 4, 2, 4, 8, 2, 8, 2, 8, 2, 20, 30, 44, 66], k=2) == 0
assert sol.numberOfSubarrays(nums=[2, 8, 4, 2, 4, 8, 2, 8, 2, 8, 2, 20, 30, 44, 66], k=3) == 0
assert sol.numberOfSubarrays(nums=[2, 8, 4, 2, 4, 8, 2, 8, 2, 8, 2, 20, 30, 44, 66], k=4) == 0
assert sol.numberOfSubarrays(nums=[2, 8, 4, 2, 4, 8, 2, 8, 2, 8, 2, 20, 30, 44, 66], k=100) == 0
assert sol.numberOfSubarrays(nums=[2, 2, 2, 1, 2, 2, 1, 2, 2, 2], k=2) == 16
assert sol.numberOfSubarrays(nums=[1, 1, 2, 1, 1], k=3) == 2
assert sol.numberOfSubarrays(nums=[2, 4, 6], k=1) == 0
assert sol.numberOfSubarrays(nums=[1, 3, 5, 7, 9], k=1) == 5
assert sol.numberOfSubarrays(nums=[1, 3, 5, 7, 9], k=2) == 4
assert sol.numberOfSubarrays(nums=[1, 3, 5, 7, 9], k=5) == 1
assert sol.numberOfSubarrays(nums=[1, 3, 5, 7, 9, 2], k=5) == 2
assert sol.numberOfSubarrays(nums=[2,1, 3, 5, 7, 9], k=5) == 2
assert sol.numberOfSubarrays(nums=[1, 3, 5, 7, 9], k=6) == 0
