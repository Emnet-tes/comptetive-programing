class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans=0
        for i in range(len(points)-1):
            x,y=points[i]
            targetx,targety=points[i+1]
            ans+=max(abs(targetx-x),abs(targety-y))
        return ans

        