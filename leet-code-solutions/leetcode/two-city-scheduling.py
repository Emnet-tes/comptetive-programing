class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        half=len(costs)//2
        costs.sort(key=lambda x:x[0]-x[1])
        ans=0
        for i in range(len(costs)):
            if i<half:
                ans+=costs[i][0]
            else:
                ans+=costs[i][1]
        return ans