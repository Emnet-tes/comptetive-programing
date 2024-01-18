class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i=0
        j=0
        x=0
        ans=[]
        while i<len(firstList) and j<len(secondList):
            maximum=max(firstList[i][0],secondList[j][0])
            minimum=min(firstList[i][1],secondList[j][1])
            if maximum<=minimum:
                ans.append([maximum,minimum])
            if firstList[i][1]<secondList[j][1]:
                i+=1
            else:
                j+=1
        return ans
            