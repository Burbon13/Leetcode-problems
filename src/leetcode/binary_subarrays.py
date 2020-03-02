class Solution:
    def numSubarraysWithSum(self, A, S: int) -> int:
        left_zeros = self.__left_zeros_list(A)
        right_zeros = self.__right_zeros_list(A)

        index1 = self.__first_1_index(A)
        if index1 == len(A):
            return 0

        index2 = self.__last_1_index(A, index1, S)

        if index2 == len(A):
            return 0

        total = 0

        while True:
            total += (left_zeros[index1] + 1) * (right_zeros[index2] + 1)

            index1 = self.__next_1_index(A, index1)
            if index1 == len(A):
                break
            index2 = self.__next_1_index(A, index2)

        return total

    def __first_1_index(self, A):
        index = 0
        while index < len(A) and A[index] == 0:
            index += 1
        return index

    def __last_1_index(self, A, index1, S):
        S -= 1
        index2 = index1 + 1
        while index2 < len(A) and S > 0:
            if A[index2] == 1:
                S -= 1
                if S == 0:
                    break
            index2 += 1
        return index2

    def __next_1_index(self, A, index):
        index += 1
        while index < len(A) and A[index] == 0:
            index += 1
        return index

    def __left_zeros_list(self, A):
        left_zeros = [0 for _ in range(len(A))]

        zeros = 1 if A[0] == 0 else 0
        for index, value in enumerate(A[1:]):
            if value == 1:
                left_zeros[index + 1] = zeros
                zeros = 0
            else:
                zeros += 1

        return left_zeros

    def __right_zeros_list(self, A):
        right_zeros = [0 for _ in range(len(A))]

        zeros = 1 if A[-1] == 0 else 0
        index = len(A) - 2
        while index >= 0:
            value = A[index]
            if value == 1:
                right_zeros[index] = zeros
                zeros = 0
            else:
                zeros += 1
            index -= 1

        return right_zeros


solution = Solution()

print(solution.numSubarraysWithSum([1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0], 2))
