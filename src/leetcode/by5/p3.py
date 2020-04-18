class Solution:
    def total(self, n):
        if n <= 0:
            return 1
        return 3 * (2 ** (n - 1))

    def psbchars(self, last_char):
        if last_char is None:
            return ['a', 'b', 'c']
        if last_char == 'a':
            return ['b', 'c']
        if last_char == 'b':
            return ['a', 'c']
        return ['a', 'b']

    def getHappyString(self, n, k):
        total = self.total(n)
        if total < k:
            return ""

        to_return = ""
        index = 0
        last_char = None

        while index < n:
            next_total = self.total(n - index - 1) * 2 // 3
            next_total = max(next_total, 1)
            possible_chars = self.psbchars(last_char)
            i = 0
            while k > next_total:
                k -= next_total
                i += 1
            to_return += possible_chars[i]
            last_char = possible_chars[i]
            index += 1

        print(to_return)
        return to_return


sol = Solution()

assert sol.getHappyString(3, 9) == "cab"
assert sol.getHappyString(3, 1) == "aba"
assert sol.getHappyString(1, 3) == "c"
assert sol.getHappyString(1, 4) == ""
assert sol.getHappyString(2, 7) == ""
assert sol.getHappyString(10, 100) == "abacbabacb"
