class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign_result = 1

        if dividend < 0 and divisor > 0:
            sign_result = -1
            dividend = -dividend
        elif dividend >= 0 and divisor < 0:
            sign_result = -1
            divisor = - divisor
        elif dividend < 0 and divisor < 0:
            divisor = -divisor
            dividend = -dividend

        result = 0

        while dividend >= divisor:
            temp, to_add = divisor, 1
            while temp << 1 <= dividend:
                temp <<= 1
                to_add <<= 1
            result += to_add
            dividend -= temp

        return result if sign_result == 1 else - result


solution = Solution()
print(solution.divide(-2147483648, -1))