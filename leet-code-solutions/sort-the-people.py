class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #using bubble sort algorithm
        box=defaultdict(int)

        for i in range(len(heights)):
            box[heights[i]]=names[i]

        for i in range(len(heights)-1,0,-1):
            for j in range(0,i):
                if heights[j+1]>heights[j]:
                    heights[j+1],heights[j] = heights[j],heights[j+1]

        li=[]
        for i in range(len(heights)):
            li.append(box[heights[i]])
            
        return li
