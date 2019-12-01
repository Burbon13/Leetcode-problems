# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/

class Solution:
    def pathInZigZagTree(self, label: int):
        to_return = []

        pow_2 = 1
        while pow_2 <= label:
            pow_2 <<= 1
        pow_2 >>= 1

        while label > 0:
            to_return.append(label)

            right = (pow_2 << 1) - 1
            label = right - (label - pow_2)

            label >>= 1
            pow_2 >>= 1

        to_return.reverse()
        return to_return


print(Solution().pathInZigZagTree(14))