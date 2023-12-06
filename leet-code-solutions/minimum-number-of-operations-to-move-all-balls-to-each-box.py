class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        li=[]
        for i in range(len(boxes)):
            ball=0
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    ball+=abs(j-i)
            li.append(ball)
        return li
        