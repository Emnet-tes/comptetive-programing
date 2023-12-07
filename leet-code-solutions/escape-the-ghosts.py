class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ghost=abs(target[0])+abs(target[-1])
        x=0
        for i in range(len(ghosts)):
                x=abs(target[0]-ghosts[i][0])+abs(target[1]-ghosts[i][1])
                if x<=ghost:
                    return False
        return True
            
                
        
            
        