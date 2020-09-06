class Solution:
    def largestTimeFromDigits(self, A) -> str:
        solution = {
            "value": ""
        }
        used = [0 for _ in range(10)]
        for x in A:
            used[x] += 1
        self.recursiveApproach("", used, solution)
        return solution["value"]

    def recursiveApproach(self, tempSol, used, solution):
        if len(tempSol) == 4:
            if int(tempSol[:2]) <= 24 and tempSol > solution["value"]:
                solution["value"] = tempSol
            return

        for x in range(10):
            if used[x] > 0:
                used[x] -= 1
                self.recursiveApproach(tempSol + str(x), used, solution)
                used[x] += 1


sol = Solution()
print(sol.largestTimeFromDigits([1, 2, 3, 4]))
