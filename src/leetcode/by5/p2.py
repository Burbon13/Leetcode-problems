class Solution:
    def findMinFibonacciNumbers(self, k):
        mps = []

        f1 = 1
        f2 = 1

        while f1 <= k:
            aux = f2
            f2 += f1
            f1 = aux
            mps.append(f1)

        total = 0

        index = len(mps) - 1
        while k > 0:
            while mps[index] <= k:
                total += int(k / mps[index])
                k -= int(k / mps[index]) * mps[index]
            index -= 1

        return total


sol = Solution()

assert sol.findMinFibonacciNumbers(7) == 2
assert sol.findMinFibonacciNumbers(10) == 2
assert sol.findMinFibonacciNumbers(19) == 3
