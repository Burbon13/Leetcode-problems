class Solution:
    def maximumSwap(self, num: int) -> int:
        binary_cover = 1
        maximum_digit = 0
        maximum_digit_binary_cover = -1
        maximum_value_after_swap = num

        while binary_cover <= num:
            digit = (num // binary_cover) % 10

            if maximum_digit > 0 and maximum_digit > digit:
                new_val_1 = ((num // (binary_cover * 10)) * 10 + maximum_digit) * binary_cover + (num % binary_cover)
                new_val_2 = ((new_val_1 // (
                        maximum_digit_binary_cover * 10)) * 10 + digit) * maximum_digit_binary_cover + (
                                    new_val_1 % maximum_digit_binary_cover)
                if new_val_2 > maximum_value_after_swap:
                    maximum_value_after_swap = new_val_2

            if digit > maximum_digit:
                maximum_digit = digit
                maximum_digit_binary_cover = binary_cover

            binary_cover *= 10

        return maximum_value_after_swap


sol = Solution()

assert sol.maximumSwap(4227220) == 7224220
assert sol.maximumSwap(1234) == 4231
assert sol.maximumSwap(0) == 0
assert sol.maximumSwap(1) == 1
assert sol.maximumSwap(1111) == 1111
assert sol.maximumSwap(1001) == 1100
assert sol.maximumSwap(2034) == 4032
assert sol.maximumSwap(2736) == 7236
