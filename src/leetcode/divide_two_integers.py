# https://leetcode.com/problems/divide-two-integers/submissions/

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        negatives = 0
        if dividend < 0:
            dividend = -dividend
            negatives += 1
        if divisor < 0:
            divisor = -divisor
            negatives += 1

        left = 0
        right = 2 ** 31 - 1

        while left <= right:
            middle = (left + right) // 2
            int_div = middle * divisor

            if int_div <= dividend < int_div + divisor:
                return middle * (1 if negatives % 2 == 0 else -1)

            if int_div > dividend:
                left = middle + 1
            else:
                right = middle - 1


solution = Solution()
print(solution.divide(-2147483648, -1))
