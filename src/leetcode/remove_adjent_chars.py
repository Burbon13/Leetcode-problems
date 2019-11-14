# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

class Solution:
    def removeDuplicates(self, string):
        final_string_stack = []
        for char in string:
            if len(final_string_stack) == 0:
                final_string_stack.append(char)
            elif final_string_stack[-1] == char:
                final_string_stack.pop(-1)
            else:
                final_string_stack.append(char)
        final_string = ''
        for val in final_string_stack:
            final_string += val
        return final_string


solution = Solution()

print(solution.removeDuplicates("abccttbth"))
# assert solution.removeDuplicates("xabccccccbbbaattyyuuuyyttty") == 'ca'
