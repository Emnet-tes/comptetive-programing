class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j=len(numbers)-1
        i=0
        while i<j:
            x=numbers[i]+numbers[j]
            if  x==target:
                return (i+1,j+1)
            elif x>target:
                j-=1
            else:
                i+=1