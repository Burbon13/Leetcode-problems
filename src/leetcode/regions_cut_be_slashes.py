# https://leetcode.com/problems/regions-cut-by-slashes/
from queue import SimpleQueue


class Solution:
    def regionsBySlashes(self, grid) -> int:
        slashes_dict = {}
        n = len(grid)

        for i, row in enumerate(grid):
            for j, char in enumerate(row):
                if char == ' ':
                    continue
                if char == '/':
                    slashes_dict[(i, j)] = '/'
                else:
                    slashes_dict[(i, j)] = '\\'

        number_of_ares = 0
        visited = set()
        cell_queue = SimpleQueue()

        # sub_cell -> next pos: (i_diff, j_diff, sub_cell)
        # sub_cell[k] = [no_Restriction, \ restriction, / restriction]
        next_to_go = {0: [(-1, 0, 2), (0, 0, 3), (0, 0, 1)],
                      1: [(0, 1, 3), (0, 0, 2), (0, 0, 0)],
                      2: [(1, 0, 0), (0, 0, 1), (0, 0, 3)],
                      3: [(0, -1, 1), (0, 0, 0), (0, 0, 2)]}

        for i in range(n):
            for j in range(n):
                for sub_cell in range(4):
                    if (i, j, sub_cell) not in visited:
                        number_of_ares += 1
                        cell_queue.put((i, j, sub_cell))
                        visited.add((i, j, sub_cell))

                        while not cell_queue.empty():
                            current_cell = cell_queue.get()
                            current_i = current_cell[0]
                            current_j = current_cell[1]
                            current_sub_cell = current_cell[2]

                            # No restriction possible
                            next_i = current_cell[0] + next_to_go[current_cell[2]][0][0]
                            next_j = current_cell[1] + next_to_go[current_cell[2]][0][1]
                            next_sub_cell = next_to_go[current_cell[2]][0][2]
                            nex_pos_tuple = (next_i, next_j, next_sub_cell)
                            if 0 <= next_i < n and 0 <= next_j < n and nex_pos_tuple not in visited:
                                visited.add(nex_pos_tuple)
                                cell_queue.put(nex_pos_tuple)
                                continue

                            # \ Restriction possible
                            if (current_i, current_j) not in slashes_dict or slashes_dict[
                                (current_i, current_j)] != '\\':
                                next_i = current_cell[0] + next_to_go[current_cell[2]][1][0]
                                next_j = current_cell[1] + next_to_go[current_cell[2]][1][1]
                                next_sub_cell = next_to_go[current_cell[2]][1][2]
                                nex_pos_tuple = (next_i, next_j, next_sub_cell)
                                if 0 <= next_i < n and 0 <= next_j < n and nex_pos_tuple not in visited:
                                    visited.add(nex_pos_tuple)
                                    cell_queue.put(nex_pos_tuple)
                                    continue

                            # / Restriction possible
                            if (current_i, current_j) not in slashes_dict or slashes_dict[
                                (current_i, current_j)] != '/':
                                next_i = current_cell[0] + next_to_go[current_cell[2]][2][0]
                                next_j = current_cell[1] + next_to_go[current_cell[2]][2][1]
                                next_sub_cell = next_to_go[current_cell[2]][2][2]
                                if next_i == 0 and next_j == 1 and next_sub_cell == 2:
                                    a = 3
                                nex_pos_tuple = (next_i, next_j, next_sub_cell)
                                if 0 <= next_i < n and 0 <= next_j < n and nex_pos_tuple not in visited:
                                    visited.add(nex_pos_tuple)
                                    cell_queue.put(nex_pos_tuple)
                                    continue
                        # print(visited)

        return number_of_ares


print(Solution().regionsBySlashes([
    " /",
    "  "
]))
print(Solution().regionsBySlashes([
    "\\/",
    "/\\"
]))
print(Solution().regionsBySlashes([
    "/\\",
    "\\/"
]))
print(Solution().regionsBySlashes([
    "//",
    "/ "
]))
