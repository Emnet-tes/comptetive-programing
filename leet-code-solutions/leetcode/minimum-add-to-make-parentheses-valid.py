class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open=0
        moves=0
        for n in s:
            if n=='(':
                open+=1
            else:
                if open:
                    open-=1
                else:
                    moves+=1
        while open:
            moves+=1
            open-=1
        return moves
            
        