# https://leetcode.com/problems/median-of-two-sorted-arrays/
from statistics import mean, median


class Solution:
    def get_before_cut(self, nums1, nums2, cut_1, cut_2):
        val1 = None if cut_1 <= 0 else nums1[cut_1 - 1]
        val2 = None if cut_2 <= 0 else nums2[cut_2 - 1]
        return [val1, val2]

    def get_after_cut(self, nums1, nums2, cut_1, cut_2):
        val1 = None if cut_1 >= len(nums1) else nums1[cut_1]
        val2 = None if cut_2 >= len(nums2) else nums2[cut_2]
        return [val1, val2]

    def my_max(self, val1, val2):
        if val1 is None:
            return val2
        if val2 is None:
            return val1
        return max(val1, val2)

    def my_min(self, val1, val2):
        if val1 is None:
            return val2
        if val2 is None:
            return val1
        return min(val1, val2)

    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) == 0:
            return median(nums2)
        if len(nums2) == 0:
            return median(nums1)

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left_1, right_1 = 0, len(nums1)
        is_even = (len(nums1) + len(nums2)) % 2 == 0

        while left_1 <= right_1:
            cut_1 = (left_1 + right_1) // 2
            cut_2 = ((len(nums1) + len(nums2) + 1) // 2) - cut_1

            before_cut = self.get_before_cut(nums1, nums2, cut_1, cut_2)
            after_cut = self.get_after_cut(nums1, nums2, cut_1, cut_2)

            if self.my_max(*before_cut) <= self.my_min(*after_cut):
                if is_even:
                    return mean([
                        self.my_max(*before_cut),
                        self.my_min(*after_cut)
                    ])
                return self.my_max(*before_cut)

            if before_cut[0] and after_cut[1] and before_cut[0] > after_cut[1]:
                right_1 = cut_1 - 1
            else:
                left_1 = cut_1 + 1


assert Solution().findMedianSortedArrays([3, 4], [1, 2]) == 2.5
assert Solution().findMedianSortedArrays([3], [1, 2]) == 2
assert Solution().findMedianSortedArrays([4], [1, 2]) == 2
assert Solution().findMedianSortedArrays([0], [1, 2]) == 1
assert Solution().findMedianSortedArrays([3], [-2, -1]) == -1
assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
