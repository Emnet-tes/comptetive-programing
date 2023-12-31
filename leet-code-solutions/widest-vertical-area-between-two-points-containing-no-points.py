class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        answer=0
        print(points[1][0])
        xbox=[]
        for area in range(len(points)):
            xbox.append(points[area][0])
        xbox.sort()
        for i in range(len(xbox)-1):
            answer=max(answer,abs(xbox[i+1]-xbox[i]))
        return answer