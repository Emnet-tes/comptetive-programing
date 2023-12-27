class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
   
        count=0
        li=[]
        sums=0
        for i in range(len(flips)):
            li.append(flips[i])
            sums+=flips[i]
            if sums==((i+1)*(i+2))/2:
                count+=1
            
            
        return count