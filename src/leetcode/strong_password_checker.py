# https://leetcode.com/problems/strong-password-checker/submissions/

class Solution:
    def strongPasswordChecker(self, s):
        if len(s) < 6:
            padding = 6 - len(s)
            deletion = 0
        elif len(s) > 20:
            deletion = len(s) - 20
            padding = 0
        else:
            deletion = 0
            padding = 0

        contains_requested = 3
        if any(c.islower() for c in s):
            contains_requested -= 1
        if any(c.isupper() for c in s):
            contains_requested -= 1
        if any(c.isdigit() for c in s):
            contains_requested -= 1

        contains_requested = max(0, contains_requested - padding)

        index = 0
        changes = 0
        while index + 2 < len(s):
            if s[index] == s[index + 1] == s[index + 2] and (s[index].isalpha() or s[index].isdigit()):
                changes += 1
                index += 3
            else:
                index += 1

        calc_deletion = deletion - 2
        remove_duplicates = calc_deletion // 3
        if remove_duplicates > 0:
            changes = max(0, changes - remove_duplicates)

        return padding + max(changes, contains_requested) + deletion


solution = Solution()
assert solution.strongPasswordChecker("aaaaaaaaaaaaaaaaaaaaa") == 7
assert solution.strongPasswordChecker("aA123") == 1
assert solution.strongPasswordChecker("1234567890123456Baaaaa") == 3
assert solution.strongPasswordChecker("aaa111") == 2
assert solution.strongPasswordChecker("...") == 3
