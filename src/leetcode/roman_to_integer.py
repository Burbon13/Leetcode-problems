# https://leetcode.com/problems/roman-to-integer


class Solution:
    def __init__(self):
        self.adder_dict = {
            'I': lambda x: (x + 1, 1),
            'V': lambda x: (x + 5, 1),
            'X': lambda x: (x + 10, 1),
            'L': lambda x: (x + 50, 1),
            'C': lambda x: (x + 100, 1),
            'D': lambda x: (x + 500, 1),
            'M': lambda x: (x + 1000, 1),
            ('I', 'V'): lambda x: (x + 4, 2),
            ('I', 'X'): lambda x: (x + 9, 2),
            ('X', 'L'): lambda x: (x + 40, 2),
            ('X', 'C'): lambda x: (x + 90, 2),
            ('C', 'D'): lambda x: (x + 400, 2),
            ('C', 'M'): lambda x: (x + 900, 2),
        }

    def romanToInt(self, s: str) -> int:
        final_number = 0

        index = 0
        s_len = len(s)

        while index < s_len:
            key = None
            if index < s_len - 1 and (s[index], s[index + 1]) in self.adder_dict:
                key = (s[index], s[index + 1])
            else:
                key = s[index]

            final_number, to_add = self.adder_dict[key](final_number)
            index += to_add

        return final_number


print(Solution().romanToInt('I'))
