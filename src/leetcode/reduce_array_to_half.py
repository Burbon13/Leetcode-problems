class Solution:
    def minSetSize(self, arr) -> int:
        counter = {}
        for val in arr:
            if val not in counter:
                counter[val] = 0
            counter[val] += 1
        values = []
        for val in counter:
            values.append(counter[val])
        values.sort(reverse=True)

        total = 0

        nhalf = len(arr) // 2
        new_n = len(arr)
        i = 0
        while new_n > nhalf:
            total += 1
            new_n -= values[i]
            i += 1

        return total


sol = Solution()

assert sol.minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2
assert sol.minSetSize([7, 7, 7, 7, 7, 7]) == 1
assert sol.minSetSize([1, 9]) == 1
assert sol.minSetSize([1000, 1000, 3, 7]) == 1
assert sol.minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5
assert sol.minSetSize([1]) == 1
assert sol.minSetSize([1, 2]) == 1
assert sol.minSetSize([1, 1]) == 1
