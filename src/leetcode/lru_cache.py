# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Node for LinkedList
class Node:
    def __init__(self, value, key):
        self.value = value
        self.key = key
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.start = None
        self.end = None
        self.size = 0

    def append(self, value: int, key: int) -> Node:
        new_node = Node(value, key)
        if self.size == 0:
            self.start = new_node
            self.end = new_node
        else:
            new_node.previous = self.end
            self.end.next = new_node
            self.end = self.end.next
        self.size += 1
        return new_node

    def move_to_end(self, node: Node) -> None:
        if node == self.end:
            return

        if self.size <= 1:
            return

        if node == self.start:
            self.start = self.start.next
            self.start.previous = None
        else:
            node.previous.next = node.next
            node.next.previous = node.previous

        node.next = None
        node.previous = self.end
        self.end.next = node
        self.end = node

    def pretty_print(self):
        str_to_print = '['

        pointer = self.start

        while pointer is not None:
            str_to_print += f'({pointer.key} {pointer.value}) ,'
            pointer = pointer.next

        str_to_print += ']'
        print(str_to_print)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_list = LinkedList()
        self.hash_map = {}

    def get(self, key: int) -> int:
        if key in self.hash_map:
            node = self.hash_map[key]
            self.linked_list.move_to_end(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            self.linked_list.move_to_end(node)
            node.value = value
            return

        if self.linked_list.size < self.capacity:
            new_node = self.linked_list.append(value, key)
            self.hash_map[key] = new_node
        else:
            first_node = self.linked_list.start
            del self.hash_map[first_node.key]
            self.hash_map[key] = first_node
            first_node.key = key
            first_node.value = value
            self.linked_list.move_to_end(first_node)


instr = ["LRUCache", "put", "put", "put", "put", "put", "get", "put", "get", "get", "put", "get", "put", "put", "put",
         "get", "put", "get", "get", "get", "get", "put", "put", "get", "get", "get", "put", "put", "get", "put", "get",
         "put", "get", "get", "get", "put", "put", "put", "get", "put", "get", "get", "put", "put", "get", "put", "put",
         "put", "put", "get", "put", "put", "get", "put", "put", "get", "put", "put", "put", "put", "put", "get", "put",
         "put", "get", "put", "get", "get", "get", "put", "get", "get", "put", "put", "put", "put", "get", "put", "put",
         "put", "put", "get", "get", "get", "put", "put", "put", "get", "put", "put", "put", "get", "put", "put", "put",
         "get", "get", "get", "put", "put", "put", "put", "get", "put", "put", "put", "put", "put", "put", "put"]
values = [[10], [10, 13], [3, 17], [6, 11], [10, 5], [9, 10], [13], [2, 19], [2], [3], [5, 25], [8], [9, 22], [5, 5],
          [1, 30], [11], [9, 12], [7], [5], [8], [9], [4, 30], [9, 3], [9], [10], [10], [6, 14], [3, 1], [3], [10, 11],
          [8], [2, 14], [1], [5], [4], [11, 4], [12, 24], [5, 18], [13], [7, 23], [8], [12], [3, 27], [2, 12], [5],
          [2, 9], [13, 4], [8, 18], [1, 7], [6], [9, 29], [8, 21], [5], [6, 30], [1, 12], [10], [4, 15], [7, 22],
          [11, 26], [8, 17], [9, 29], [5], [3, 4], [11, 30], [12], [4, 29], [3], [9], [6], [3, 4], [1], [10], [3, 29],
          [10, 28], [1, 20], [11, 13], [3], [3, 12], [3, 8], [10, 9], [3, 26], [8], [7], [5], [13, 17], [2, 27],
          [11, 15], [12], [9, 19], [2, 15], [3, 16], [1], [12, 17], [9, 1], [6, 19], [4], [5], [5], [8, 1], [11, 7],
          [5, 2], [9, 28], [1], [2, 2], [7, 4], [4, 22], [7, 24], [9, 26], [13, 28], [11, 26]]

sol = LRUCache(values[0][0])

for i, value in zip(instr[1:], values[1:]):
    print(i, value)
    if i == 'put':
        sol.put(value[0], value[1])
    else:
        print(sol.get(value[0]))
    sol.linked_list.pretty_print()
    print()
