class Solution:
    def increasingTriplet(self, nums):
        firstSmall = 99999999999999999999998
        nextSmall = 99999999999999999999999

        for val in nums:
            if val <= firstSmall:
                firstSmall = val
            elif val <= nextSmall:
                nextSmall = val
            else:
                return True
        return False


sol = Solution()

assert sol.increasingTriplet([1,0,1,1,2])
assert sol.increasingTriplet([1, 2, 3, 4, 5])
assert not sol.increasingTriplet([9, 10, 7, 8, 5, 6])
assert sol.increasingTriplet([9, 10, 7, 8, 5, 6, 1, 7])
assert sol.increasingTriplet([1, 2, 3, 4, 5])
assert sol.increasingTriplet([1, 2, 3, 4, 5])
assert sol.increasingTriplet([1, 2, 3, 4, 5])
assert not sol.increasingTriplet([5, 4, 3, 2, 1])
assert not sol.increasingTriplet([])
assert not sol.increasingTriplet([1])
assert not sol.increasingTriplet([1, 2])
assert not sol.increasingTriplet([0, 4, 2, 1, 0, -1, -3])
assert sol.increasingTriplet([1, 2, -10, -8, -7])
