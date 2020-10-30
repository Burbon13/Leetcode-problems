from collections import deque


class HashableSequence:
    def __init__(self, limit):
        self.limit = limit
        self.index = 1
        self.current_hash = 0
        self.linear_sum = 0
        self.nr_queue = deque()
        self.primes = [67, 257, 71, 607, 89, 379, 107, 11, 113, 127, 131, 137, 139, 149, 157, 167, 179, 181, 191, 197,
                       199,
                       211, 227, 233, 239, 251]

    def hash(self) -> int:
        return self.current_hash

    def addChar(self, c):
        if self.index == self.limit + 1:
            self.current_hash -= self.linear_sum
            self.linear_sum -= self.nr_queue.popleft()
            self.index -= 1

        self.current_hash += self.index * self.primes[self.charValue(c)]
        self.linear_sum += self.primes[self.charValue(c)]
        self.nr_queue.append(self.primes[self.charValue(c)])
        self.index += 1

    def charValue(self, char):
        return ord(char) - 97


class Solution:
    def longestDupSubstring(self, s: str) -> str:
        left = 1
        right = len(s) - 1
        result = ""

        while left <= right:
            middle = (left + right) // 2

            duplicate = self.hasDuplicates(s, middle)
            if duplicate != "":
                result = duplicate
                left = middle + 1
            else:
                right = middle - 1

        print(result)
        return result

    def hasDuplicates(self, S, middle) -> str:
        strs = set()
        hsq = HashableSequence(middle)
        for i in range(middle):
            hsq.addChar(S[i])
        strs.add(hsq.hash())
        print(hsq.hash(), S[:middle])
        for i in range(middle, len(S)):
            hsq.addChar(S[i])
            val = hsq.hash()
            print(hsq.hash(), S[i - middle + 1: i + 1])
            if val in strs:
                return S[i - middle + 1: i + 1]
            strs.add(val)

        return ""


sol = Solution()

assert sol.longestDupSubstring(
    "ababbcbabcbabcabcbabcbababbcabcbaabbaabcabcbabcabcbabcabcbabcabcbababbacbacacaaaaa") == "abcabcbabcabcbabcabcbab"
assert sol.longestDupSubstring("abcacbacacaaaaa") == "aaaa"
assert sol.longestDupSubstring("abcbabcabcbabcabcbabcabcbababbacbacacaaaaa") == "abcbabcabcbabcabcbab"
assert sol.longestDupSubstring("ana") == "a"
assert sol.longestDupSubstring("banana") == "ana"
assert sol.longestDupSubstring("abcd") == ""
assert sol.longestDupSubstring("aaaa") == "aaa"
assert sol.longestDupSubstring("aa") == "a"
