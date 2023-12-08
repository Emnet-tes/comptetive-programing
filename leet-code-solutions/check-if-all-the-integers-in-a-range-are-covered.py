class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        li=[]
        for j in range(left,right+1):
            li.append(j)
        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                if j in li:
                    li.remove(j)
        print(len(li))
        return True if len(li)==0 else False
        
