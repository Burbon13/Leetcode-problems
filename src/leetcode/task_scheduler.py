class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        counter = {}
        n += 1
        for task in tasks:
            if task not in counter:
                counter[task] = 0
            counter[task] += 1

        sorted_tasks = []
        for task in counter:
            sorted_tasks.append(counter[task])
        sorted_tasks.sort(reverse=True)

        units_of_time = 0
        last_used = {}

        while True:
            found = False
            positive = False

            for i, val in enumerate(sorted_tasks):
                if val > 0:
                    positive = True
                    if i not in last_used or (units_of_time - last_used[i] >= n and (
                            i == len(sorted_tasks) - 1 or sorted_tasks[i] >= sorted_tasks[i + 1])):
                        last_used[i] = units_of_time
                        units_of_time += 1
                        sorted_tasks[i] -= 1
                        found = True
                        # print(f' {i} ')
                        break

            if not positive:
                break

            if not found:
                # print(" IDLE ")
                units_of_time += 1

        return units_of_time


sol = Solution()

assert sol.leastInterval(["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2) == 12
assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 2) == 8
assert sol.leastInterval(["A", "A", "A", "B", "B", "B"], 0) == 6
assert sol.leastInterval(["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2) == 16
