class Solution:
    def decodeString(self, s: str) -> str:
        return self.recursive(s, 0, len(s) - 1)

    def recursive(self, s, left, right):
        if left > right:
            return ""

        if left == right:
            return s[left]

        result = ""

        i = left
        while i <= right:
            if s[i].isalpha():
                result += s[i]
                i += 1
            else:
                nr, left_parant = self.read_nr(s, i)
                right_parant = self.find_right_parant(s, left_parant)
                result += self.recursive(s, left_parant + 1, right_parant - 1) * nr
                i = right_parant + 1

        return result

    def read_nr(self, s, i):
        nr = 0
        while s[i].isdigit():
            nr = nr * 10 + int(s[i])
            i += 1
        return nr, i

    def find_right_parant(self, s, i):
        open_parant = 1
        i += 1
        while open_parant > 0:
            if s[i] == "[":
                open_parant += 1
            elif s[i] == "]":
                open_parant -= 1
            i += 1
        return i - 1


sol = Solution()

assert sol.decodeString("3[a]2[bc]") == "aaabcbc"
assert sol.decodeString("3[3[a]]") == "aaaaaaaaa"
assert sol.decodeString("") == ""
assert sol.decodeString("sfsafasfasfa") == "sfsafasfasfa"
assert sol.decodeString("3[a2[c]]") == "accaccacc"
assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
assert sol.decodeString("abc3[cd]xyz") == "abccdcdcdxyz"
