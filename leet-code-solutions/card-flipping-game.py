class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        fli=[]
        bli=[]
        n=len(fronts)
        y=float('inf')
        x=set()
        for i in range(n):
            if fronts[i]==backs[i] :
               x.add(fronts[i])
        for i in range(n):
            if fronts[i] not in x:
                y=min(y,fronts[i])
        for i in range(n):
            if backs[i] not in x:
                y=min(y,backs[i])
        return y if y!=float('inf') else 0