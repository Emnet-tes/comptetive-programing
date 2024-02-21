class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves=0
        remian=0
        while target>1:
            if maxDoubles>0:
                remain=target%2
                target//=2
                maxDoubles-=1
                moves+=1
                if remain:
                    moves+=1
            else:
                moves+=target-1
                target=1
        return moves


        