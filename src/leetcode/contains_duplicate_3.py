class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        buckets = {}

        j = - k - 1
        i = 0

        while i < len(nums):
            if j >= 0:
                bucket_index = nums[j] // (t + 1)
                del buckets[bucket_index]

            bucket_index = nums[i] // (t + 1)

            if bucket_index in buckets:
                return True

            if bucket_index - 1 in buckets and nums[i] - buckets[bucket_index - 1] <= t:
                return True

            if bucket_index + 1 in buckets and buckets[bucket_index + 1] - nums[i] <= t:
                return True

            buckets[bucket_index] = nums[i]

            i += 1
            j += 1

        return False


sol = Solution()

assert not sol.containsNearbyAlmostDuplicate([1, 5, 9, 1, 5, 9], 2, 3)
assert not sol.containsNearbyAlmostDuplicate([1, 1, 1, 1, 1], 0, 0)
assert not sol.containsNearbyAlmostDuplicate([], 2, 3)
assert not sol.containsNearbyAlmostDuplicate([1], 2, 3)
assert sol.containsNearbyAlmostDuplicate([1, 0, 1, 1], 1, 2)
assert sol.containsNearbyAlmostDuplicate([1, 2, 3, 1], 3, 0)
