class Solution:
    def findJudge(self, N, trust):
        if N == 1:
            return len(trust) == 0

        is_trusted = {}
        trusts = {}
        for a, b in trust:
            if b not in is_trusted:
                is_trusted[b] = 0
            if a not in trusts:
                trusts[a] = 0
            trusts[1] += 1
            is_trusted[b] += 1

        total = []
        for person in is_trusted:
            if is_trusted[person] == N - 1:
                total.append(person)

        if len(total) == 1 and total[0] not in trusts:
            return total[0]
        return -1


sol = Solution()

assert sol.findJudge(2, [[1, 2]]) == 2
assert sol.findJudge(3, [[1, 3], [2, 3]]) == 3
assert sol.findJudge(3, [[1, 3], [2, 3], [3, 1]]) == -1
assert sol.findJudge(3, [[1, 2], [2, 3]]) == -1
assert sol.findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
