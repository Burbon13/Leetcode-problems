class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i1 = 0
        i2 = 0
        last_char = None
        while i2 < len(typed):
            if i1 < len(name) and name[i1] == typed[i2]:
                last_char = name[i1]
                i1 += 1
                i2 += 1
            elif typed[i2] == last_char:
                i2 += 1
            else:
                return False

        return i1 == len(name)


sol = Solution()

assert sol.isLongPressedName("alex", "aaleex")
assert not sol.isLongPressedName("saeed", "ssaaedd")
assert sol.isLongPressedName("leelee", "lleeelee")
assert sol.isLongPressedName("laiden", "laiden")
assert not sol.isLongPressedName("abcdef", "abcdee")
assert sol.isLongPressedName("abcde", "abcdeeeeee")
