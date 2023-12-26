class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mydect=defaultdict(int)
        for i in range(len(heights)):
            mydect[heights[i]]=names[i]
        for i in range(len(heights)):
            for j in range(len(heights)-1 ):
                if heights[j]< heights[j+1]:
                    temp=heights[j]
                    heights[j]=heights[j+1]
                    heights[j+1]=temp
        li=[]
        for i in range(len(heights)):
            li.append(mydect[heights[i]])

        return li
            
                
        