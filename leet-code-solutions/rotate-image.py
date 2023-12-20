class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        col=[]
        for c in range( len(matrix[0])):
            row=[]
            for r in range(len(matrix)-1,-1,-1):
                row.append(matrix[r][c])
            col.append(row)
        print(col)
        for i in range(len(col)):
           for j in range(len(col[0])):
               matrix[i][j]=col[i][j]
        
        