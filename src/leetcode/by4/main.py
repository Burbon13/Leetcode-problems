class Solution:
    def matrixBlockSum(self, mat, K):

        self._generateDp(mat)

        print(mat)

        mat_to_ret = []
        for i in range(len(mat)):
            row = []
            for j in range(len(mat[0])):
                row.append(self._getVal(i, j, K, mat))
            mat_to_ret.append(row)

        return mat_to_ret

    def _generateDp(self, mat):
        for i in range(len(mat)):
            for j in range(1, len(mat[0])):
                mat[i][j] += mat[i][j - 1]

        for i in range(1, len(mat)):
            for j in range(len(mat[0])):
                mat[i][j] += mat[i - 1][j]

    def _getVal(self, i, j, K, dp):
        i1 = max(0, i - K) - 1
        j1 = max(0, j - K) - 1
        i2 = min(i + K, len(dp) - 1)
        j2 = min(j + K, len(dp[0]) - 1)

        print('i, j', i, j)
        print('i1 j1', i1, j1)
        print('i2, j2', i2, j2)

        lefts = (dp[i2][j1] if j1 >= 0 else 0)
        rights = (dp[i1][j2] if i1 >= 0 else 0)
        upside = (dp[i1][j1] if (j1 >= 0 and i1 >= 0) else 0)

        print(dp[i2][j2], lefts, rights, upside)
        print('-------')

        return dp[i2][j2] - lefts - rights + upside


print(Solution().matrixBlockSum([[1,1,1],[1,1,1],[1,1,1],[1,1,1]], 1))
# expected [[109,238,141],[169,359,258],[191,346,251],[287,453,348],[227,332,231]]