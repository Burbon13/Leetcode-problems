class Solution:
    def subarraySum(self, nums, k):
        previous = {}
        previous[0] = 1
        total = 0
        for index, val in enumerate(nums):
            new_sums = {}
            for s in previous:
                new_s = val + s
                new_sums[new_s] = previous[s]
                if new_s == k:
                    total += new_sums[new_s]

            if index > 0:
                if val == k:
                    total += 1
                if val not in new_sums:
                    new_sums[val] = 1
                else:
                    new_sums[val] += 1

            previous = new_sums

        return total


sol = Solution()

assert sol.subarraySum([1, 2, 3], 3) == 2
assert sol.subarraySum([1, 1, 1], 2) == 2
