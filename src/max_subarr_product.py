class Solution:
    def maxProduct(self, nums):
        zero_free_lists = []
        has_zero = False

        temp = []
        for val in nums:
            if val == 0:
                has_zero = True
                if len(temp) > 0:
                    zero_free_lists.append(temp)
                    temp = []
            else:
                temp.append(val)
        if len(temp) > 0:
            zero_free_lists.append(temp)

        if len(zero_free_lists) == 0:
            return 0

        result = max([self.gmaxList(x) for x in zero_free_lists])
        if has_zero:
            return max(result, 0)
        return result

    def maxList(self, nums):
        if len(nums) == 1 and nums[0] < 0:
            return nums[0]

        product = 1
        left = 0
        right = 1

        for val in nums:
            product *= val
            if val < 0:
                if left == 0:
                    left = product
                right = 1
            right *= val

        if product < 0:
            product = int(product / max(left, right))

        return product


sol = Solution()

assert sol.maxList([-4, -3, -2]) == 12
assert sol.maxList([2, 3, -2, 4]) == 6
assert sol.maxList([-2, 0, -1]) == 0
