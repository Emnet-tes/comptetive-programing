class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid=[[0 for _ in range(n)]for _ in range(m)]

        north=(-1,0)
        south=(1,0)
        west=(0,-1)
        east=(0,1)
        for x,y in guards:
            grid[x][y]='G'
        for x,y in walls:
            grid[x][y]='W' 
        print(grid)  
        def canSee(r,c,direction)  :
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]=='W' or grid[r][c]=='G':
                return
            grid[r][c]='M'
            canSee(r+direction[0],c+direction[1],direction)
        for r in range(m):
            for c in range(n):
                if grid[r][c]=='G':
                    #for north
                    canSee(r-1,c,north)
                    #for south
                    canSee(r+1,c,south) 
                    #for east
                    canSee(r,c+1,east)
                    #for west
                    canSee(r,c-1,west)  
        unguarded=0
        for r in range(m):
            for c in range(n):
                if grid[r][c]==0:
                    unguarded+=1

        return unguarded

        