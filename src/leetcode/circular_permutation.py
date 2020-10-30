from typing import List, Set


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        used = set()
        used.add(start)
        return self.recursive(n, 2 ** n - 1, [start], used)

    def recursive(self, n, remaining, p, used):
        if remaining == 0:
            if self.differOnlyByOneBit(p[0], p[-1], n):
                return p[:]
            return None

        nexts = self.getDiffNrsByOneBit(p[-1], n)
        for val in nexts:
            if val in used:
                continue
            p.append(val)
            used.add(val)
            solution = self.recursive(n, remaining - 1, p, used)
            p.pop()
            used.remove(val)
            if solution is not None:
                return solution
        return None

    def getDiffNrsByOneBit(self, nr, n) -> Set[int]:
        bit = 1
        nexts = set()
        for _ in range(n):
            if nr & bit > 0:
                nexts.add(nr - bit)
            else:
                nexts.add(nr + bit)
            bit <<= 1
        return nexts

    def differOnlyByOneBit(self, nr1, nr2, n) -> bool:
        bit = 1
        differences = 0
        for _ in range(n):
            if nr1 & bit != nr2 & bit:
                differences += 1
                if differences > 1:
                    return False
            bit <<= 1
        return True


sol = Solution()
print(sol.circularPermutation(2, 3))
print(sol.circularPermutation(3, 2))
