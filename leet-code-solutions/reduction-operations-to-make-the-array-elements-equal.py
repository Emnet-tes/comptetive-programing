class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        operation=0
        nums.sort(reverse=True)
        if len(nums)*nums[0]==sum(nums):
            return operation
        else:
            for i in range(len(nums)-1):
                if nums[i]>nums[i+1]:
                    operation+=i+1
        return operation
        
            
        
        