from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonalDict=defaultdict(list)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                diagonalDict[r+c].append(mat[r][c])
        ans = []
        for i, value in enumerate(diagonalDict.values()):
            if i % 2 == 0:
                ans += value[::-1]
            else:
                ans += value
        return ans