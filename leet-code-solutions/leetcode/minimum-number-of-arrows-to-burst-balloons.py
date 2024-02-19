class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        start=0
        end=float('inf')
        cnt=0
        i=0
        points.sort()
        intersection=[]
        intersection.append(points[0][0])
        intersection.append(points[0][1])
        
        while i<len(points):
            start=max(intersection[0],points[i][0])
            end=min(intersection[1],points[i][1])
            if start<=end:
                intersection=[start,end]
                i+=1
                continue
            else:
                intersection=[points[i][0],points[i][1]]
                print(intersection)
                cnt+=1
                i+=1
                    
        return cnt+1


        