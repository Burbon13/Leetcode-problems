class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        i, j = 0, 0
        action = 'down'
        new_s_arr = []
        for c in s:
            new_s_arr.append(((i, j), c))
            i, j, action = self.next(action, i, j, numRows)
        new_s_arr.sort()
        new_s = ''
        for value in new_s_arr:
            new_s += value[1]
        return new_s

    def next(self, action, i, j, numRows):
        if i == numRows - 1:
            action = 'up'
            i -= 1
            j += 1
        elif i == 0:
            action = 'down'
            i += 1
        elif action == 'down':
            i += 1
        else:
            i -= 1
            j += 1
        return i, j, action


sol = Solution()

assert sol.convert('PAYPALISHIRING', 1) == 'PAYPALISHIRING'
assert sol.convert('PAYPALISHIRING', 3) == 'PAHNAPLSIIGYIR'
assert sol.convert('PAYPALISHIRING', 4) == 'PINALSIGYAHRPI'
