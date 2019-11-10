# https://leetcode.com/problems/open-the-lock/

from queue import PriorityQueue


class Solution:
    def increment_digit(self, value, index):
        digits = [int(char) for char in value]
        digits[index] += 1
        if digits[index] == 10:
            digits[index] = 0
        return "".join([str(digit) for digit in digits])

    def decrement_digit(self, value, index):
        digits = [int(char) for char in value]
        digits[index] -= 1
        if digits[index] == -1:
            digits[index] = 9
        return "".join([str(digit) for digit in digits])

    def calculate_diff(self, d1, d2):
        dif_val = abs(d1 - d2)
        if dif_val > 5:
            dif_val = 10 - dif_val
        return dif_val

    def distance_between_neighbours(self, n1, n2):
        difference = 0
        digits1 = [int(char) for char in n1]
        digits2 = [int(char) for char in n2]

        for d1, d2 in zip(digits1, digits2):
            difference += self.calculate_diff(d1, d2)

        return difference

    def get_neighbours(self, value):
        to_return = []
        for index in range(4):
            to_return.append(self.increment_digit(value, index))
            to_return.append(self.decrement_digit(value, index))
        return to_return

    def openLock(self, deadends, target):
        graph = {"0000": 0}
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        my_queue = PriorityQueue()
        my_queue.put((self.distance_between_neighbours("0000", target), "0000"))

        while not my_queue.empty():
            current_value = my_queue.get()[1]
            current_length = graph[current_value]

            neighbours = self.get_neighbours(current_value)

            for neighbour in neighbours:
                if neighbour not in graph and neighbour not in deadends:
                    if neighbour == target:
                        return current_length + 1
                    graph[neighbour] = current_length + 1
                    my_queue.put((self.distance_between_neighbours(neighbour, target), neighbour))

        return -1


assert Solution().openLock(deadends=["0201", "0101", "0102", "1212", "2002"], target="0202") == 6
assert Solution().openLock(deadends=["8888"], target="0009") == 1
assert Solution().openLock(deadends=["8887", "8889", "8878", "8898", "8788", "8988", "7888", "9888"],
                           target="8888") == -1
assert Solution().openLock(deadends=["0000"], target="8888") == -1
