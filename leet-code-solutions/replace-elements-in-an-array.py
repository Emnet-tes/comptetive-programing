class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        container={}
        for i in range(len(nums)):
            container[nums[i]]=i
        
        for x,y in operations:
            m=container[x]
            nums[m]=y
            del container[x]
            container[y]=m
        print(container)
        return nums
                

        