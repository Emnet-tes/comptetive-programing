class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        #using selection sort algorithm
        for i in range(len(heights)):
            index=i
            for j in range(i+1,len(heights)):
                if heights[j]>heights[index]:
                    index=j
            if index!=i:
                heights[index],heights[i]=heights[i],heights[index]
                names[index], names[i] = names[i], names[index]

        return names

        