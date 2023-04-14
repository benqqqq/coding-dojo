import sys
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        ans = [[sys.maxsize if mat[i][j] == 1 else 0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                min_candidate = [ans[i][j]]
                if i - 1 >= 0:
                    min_candidate.append(ans[i - 1][j] + 1)
                if j - 1 >= 0:
                    min_candidate.append(ans[i][j - 1] + 1)

                ans[i][j] = min(min_candidate)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                min_candidate = [ans[i][j]]
                if i + 1 < m:
                    min_candidate.append(ans[i + 1][j] + 1)
                if j + 1 < n:
                    min_candidate.append(ans[i][j + 1] + 1)

                ans[i][j] = min(min_candidate)

        return ans

