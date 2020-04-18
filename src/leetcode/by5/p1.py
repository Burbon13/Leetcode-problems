class Solution:
    def minStartValue(self, nums):
        min_neg = 0
        suma = 0
        for val in nums:
            suma += val
            min_neg = min(suma, min_neg)
        return 1 - min_neg


sol = Solution()

assert sol.minStartValue([1, 2]) == 1
assert sol.minStartValue([1, -2, -3]) == 5
assert sol.minStartValue([-3, 2, -3, 4, 2]) == 5
