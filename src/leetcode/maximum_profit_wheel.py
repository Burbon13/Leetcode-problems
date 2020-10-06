class Solution:
    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        maximum_profit = 0
        maximum_rotations = -1
        current_profit = 0
        clients_waiting = 0

        for i, nr_clients in enumerate(customers):
            clients_waiting += nr_clients
            current_profit += min(clients_waiting, 4) * boardingCost
            clients_waiting -= min(clients_waiting, 4)
            current_profit -= runningCost

            if current_profit > maximum_profit:
                maximum_profit = current_profit
                maximum_rotations = i + 1

        i = len(customers)
        while clients_waiting > 0:
            current_profit += min(clients_waiting, 4) * boardingCost
            clients_waiting -= min(clients_waiting, 4)
            current_profit -= runningCost

            if current_profit > maximum_profit:
                maximum_profit = current_profit
                maximum_rotations = i + 1
            i += 1

        return maximum_rotations


sol = Solution()

assert sol.minOperationsMaxProfit([10, 10, 6, 4, 7], 3, 8) == 9
assert sol.minOperationsMaxProfit([10, 9, 6], 6, 4) == 7
assert sol.minOperationsMaxProfit([3, 4, 0, 5, 1], 1, 92) == -1
assert sol.minOperationsMaxProfit([8, 3], 5, 6) == 3
