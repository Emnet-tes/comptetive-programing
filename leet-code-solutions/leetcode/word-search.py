class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        visited=set() #track dead end
        board_row=len(board)
        board_col=len(board[0])

        def search(row,col,idx):
            #found all the lettert
            if idx == len(word):
                return True

            if (row>=board_row or col>=board_col or row<0 or col<0 or word[idx]!=board[row][col]
                or (row,col) in visited):
                return False

            #check all direction
            visited.add((row,col))
            ans=(search(row,col+1,idx+1) or search(row,col-1,idx+1) or search(row+1,col,idx+1) 
                or search(row-1,col,idx+1))
            visited.remove((row,col))
            return ans

        for r in range(board_row):
            for c in range(board_col):
                if search(r,c,0):
                    return True
        return False