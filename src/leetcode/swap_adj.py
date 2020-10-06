class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False

        R_count = 0
        L_count = 0

        i = 0
        n = len(start)
        while i < n:
            if start[i] == 'R':
                R_count += 1
            if end[i] == 'L':
                L_count -= 1

            if R_count > 0 and L_count < 0:
                return False

            if start[i] == 'L':
                L_count += 1
            if end[i] == 'R':
                R_count -= 1

            if L_count > 0:
                return False
            if R_count < 0:
                return False

            i += 1

        return L_count == 0 and R_count == 0


sol = Solution()
assert not sol.canTransform("XXRXL", "LXRXX")
assert not sol.canTransform("LR", "RL")
assert sol.canTransform("RXXLRXRXL", "XRLXXRRLX")
assert not sol.canTransform("LLR", "RRL")
assert not sol.canTransform("XLLR", "LXLX")
assert not sol.canTransform("RLX", "XLR")
