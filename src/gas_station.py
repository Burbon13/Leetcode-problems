class Solution:
    def canCompleteCircuit(self, gas, cost):
        n = len(gas)
        gas = [*gas, *gas]
        cost = [*cost, *cost]
        prev_index = 0
        index = 0
        total = 0
        total_cost = 0
        for quantity, current_cost in zip(gas, cost):
            total_cost += quantity - current_cost
            total += 1
            while total_cost < 0:
                total_cost -= gas[prev_index] - cost[prev_index]
                total -= 1
                prev_index += 1
            if total == n:
                return (index + 1) % n
            index += 1
            if index >= n:
                index -= n

        return -1


sol = Solution()

assert sol.canCompleteCircuit([5, 1, 2, 3, 4], [2, 3, 4, 5, 1]) == 4
assert sol.canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]) == 3
assert sol.canCompleteCircuit([2, 3, 4], [3, 4, 3]) == -1
