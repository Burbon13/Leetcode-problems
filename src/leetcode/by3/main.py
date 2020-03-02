class Solution:
    def findBestValue(self, arr, target: int) -> int:

        left = 0
        right = target
        t_sum = sum(arr)

        max_appr = 9999999999999999999
        value = 9999999999999999999
        while left <= right:
            middle = (left + right) // 2
            if left == right:
                a = 3
            cur_sum = 0
            for v in arr:
                cur_sum += min(v, middle)

            if abs(cur_sum - target) < max_appr or (abs(cur_sum - target) == max_appr and middle < value):
                max_appr = abs(cur_sum - target)
                value = middle

            if cur_sum >= target:
                right = middle - 1
            else:
                left = middle + 1

        return value


print(Solution().findBestValue([4, 9, 3], 10))
print(Solution().findBestValue([2, 3, 5], 10))
print(Solution().findBestValue([60864, 25176, 27249, 21296, 20204], 56803))
print(Solution().findBestValue([60864], 56803))
