class Solution:
    def threeSum(self, nums):
        results = set()
        prev = set()

        prev.add(nums[0])

        for index, val in enumerate(nums[1:]):
            index += 1

            for next_val in range(index + 1, len(nums)):
                v1 = val
                v2 = nums[next_val]
                if -v1 - v2 in prev:
                    results.add(tuple(sorted([v1, v2, -v1 - v2])))

            prev.add(val)

        return results


sol = Solution()

print(sol.threeSum([-1,0,1,2,-1,-4]))
