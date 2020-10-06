class Solution:
    def minSwapsCouples(self, row):
        total_swaps = 0
        where_is_person = {}
        current_couples = {}

        for i in range(0, len(row), 2):
            person1, person2 = row[i], row[i + 1]

            if self.areCouple(person1, person2):
                continue

            where_is_person[person1] = i
            where_is_person[person2] = i
            current_couples[i] = (person1, person2)

        for couple in current_couples:
            if current_couples[couple] is None:
                continue

            person1, person2 = current_couples[couple]

            cost1, couples1 = self.getMinimumChanges(person1, couple, current_couples, where_is_person)
            cost2, couples2 = self.getMinimumChanges(person2, couple, current_couples, where_is_person)

            if cost1 < cost2:
                self.fixCouples(couples1, current_couples)
                total_swaps += cost1
            else:
                self.fixCouples(couples2, current_couples)
                total_swaps += cost2

        return total_swaps

    def areCouple(self, person1, person2):
        return self.getCouple(person1) == self.getCouple(person2)

    def getCouple(self, person):
        return person // 2

    def fixCouples(self, couples, current_couples):
        for couple in couples:
            current_couples[couple] = None

    def getPartner(self, person):
        return person + 1 if person % 2 == 0 else person - 1

    def getMinimumChanges(self, person, couple, current_couples, where_is_person):
        visited = set()
        visited.add(couple)
        changes = 0
        couples = [couple]
        while True:
            next_couple = where_is_person[self.getPartner(person)]
            if next_couple in visited:
                break
            visited.add(next_couple)
            couples.append(next_couple)
            if self.areCouple(person, current_couples[next_couple][0]):
                person = current_couples[next_couple][1]
            else:
                person = current_couples[next_couple][0]
            changes += 1

        return changes, couples


sol = Solution()

assert sol.minSwapsCouples([3, 2, 0, 1]) == 0
assert sol.minSwapsCouples([0, 2, 1, 3]) == 1
assert sol.minSwapsCouples([0, 2, 1, 3, 8, 9, 7, 5, 6, 4, 19, 17, 10, 12, 11, 14, 13, 15, 18, 16]) == 5
assert sol.minSwapsCouples([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]) == 0
assert sol.minSwapsCouples(
    [0, 2, 1, 3, 8, 9, 7, 5, 6, 4, 19, 17, 10, 12, 11, 14, 13, 15, 18, 16, 20, 22, 21, 23, 29, 28, 26, 27, 24, 25]
) == 6
