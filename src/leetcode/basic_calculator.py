ops_1 = [
    ('+', (lambda val1, val2: val1 + val2)),
    ('-', (lambda val1, val2: val1 - val2))
]
ops_2 = [
    ('*', (lambda val1, val2: val1 * val2)),
    ('/', (lambda val1, val2: int(val1 / val2)))
]


class Solution:
    def calculate(self, s):
        return self.recursive_calc(s.replace(' ', ''))

    def recursive_calc(self, s):
        pos1 = s.rfind(ops_1[0][0])
        pos2 = s.rfind(ops_1[1][0])

        if pos1 > pos2:
            return ops_1[0][1](self.calculate(s[:pos1]), self.calculate(s[pos1 + 1:]))
        elif pos2 > pos1:
            return ops_1[1][1](self.calculate(s[:pos2]), self.calculate(s[pos2 + 1:]))

        pos1 = s.rfind(ops_2[0][0])
        pos2 = s.rfind(ops_2[1][0])

        if pos1 > pos2:
            return ops_2[0][1](self.calculate(s[:pos1]), self.calculate(s[pos1 + 1:]))
        elif pos2 > pos1:
            return ops_2[1][1](self.calculate(s[:pos2]), self.calculate(s[pos2 + 1:]))

        return int(s)


sol = Solution()
assert sol.calculate("1+2*5/3+6/4*2") == 6
assert sol.calculate("3+2*2") == 7
assert sol.calculate(" 3/2 ") == 1
assert sol.calculate(" 3+5 / 2 ") == 5
