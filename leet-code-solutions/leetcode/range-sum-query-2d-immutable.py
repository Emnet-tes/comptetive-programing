class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix=matrix
        self.grid=[[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for r in range(len(self.matrix)):
            for c in range(len(self.matrix[0])):
                self.grid[r][c] = self.matrix[r][c]
                if r > 0:
                    self.grid[r][c] += self.grid[r - 1][c]
                if c > 0:
                    self.grid[r][c] += self.grid[r][c - 1]
                if c > 0 and r > 0:
                    self.grid[r][c] -= self.grid[r - 1][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.grid[row2][col2]
        if row1 > 0:
            total -= self.grid[row1 - 1][col2]
        if col1 > 0:
            total -= self.grid[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            total += self.grid[row1 - 1][col1 - 1]
        return total
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)