class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        total = 0
        changed = False

        x = 1 << 31

        for _ in range(32):
            low_bit = m & x
            high_bit = n & x

            if low_bit == 0 and high_bit == 0:
                x >>= 1
                continue

            if low_bit == 0 or high_bit == 0:
                x >>= 1
                changed = True
                continue

            if changed:
                x >>= 1
                continue

            total += x
            x >>= 1

        return total


sol = Solution()

assert sol.rangeBitwiseAnd(5, 7) == 4
assert sol.rangeBitwiseAnd(0, 1) == 0