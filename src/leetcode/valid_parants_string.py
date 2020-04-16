from queue import SimpleQueue


class Solution:
    def checkValidString(self, s: str) -> bool:
        open_parant_count = 0
        star_queue = SimpleQueue()
        for index, c in enumerate(s):
            if c == '*':
                star_queue.put(index)
            elif c == '(':
                open_parant_count += 1
            elif open_parant_count > 0:
                open_parant_count -= 1
            elif not star_queue.empty():
                pos = star_queue.get()
                s = s[:pos] + '(' + s[pos + 1:]
            else:
                return False

        open_parant_count = 0
        star_queue = SimpleQueue()
        for index, c in enumerate(s[::-1]):
            if c == '*':
                star_queue.put(index)
            elif c == ')':
                open_parant_count += 1
            elif open_parant_count > 0:
                open_parant_count -= 1
            elif not star_queue.empty():
                pos = star_queue.get()
                s = s[:pos] + '(' + s[pos + 1:]
            else:
                return False

        return True


solution = Solution()
assert not solution.checkValidString("(*)(")
assert solution.checkValidString("(*()")
assert solution.checkValidString("()")
assert solution.checkValidString("(*)")
assert solution.checkValidString("(*))")
assert solution.checkValidString("((*)")
assert not solution.checkValidString("(())((())()()(*)(*()(())())())()()((()())((()))(*")
