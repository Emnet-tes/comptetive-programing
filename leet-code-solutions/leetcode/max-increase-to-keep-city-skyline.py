class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max=[]
        col_max=[]
        ans=0
        n=len(grid)
        #for row maximum
        for r in range(n):
            row=0
            for c in range(n):
                row=max(row,grid[r][c])
            row_max.append(row)
        #for col maximum traversing vertically
        for c in range(n):
            col=0
            for r in range(n):
                col=max(col,grid[r][c])
            col_max.append(col)

        # finding the difference
        val=0
        for r in range(n):
            for c in range(n):
                
                val=min(row_max[r],col_max[c])
                ans+=val-grid[r][c]
        return ans
            

        
            
                

        