class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        size=0
        if len(nums)==1 and nums[0]==1:
            return 1
        elif 1 not in nums:
            return 0
        else:
            for i in range(len(nums)-1):
                if nums[i]==0:
                    size=0
                if nums[i]==1 and nums[i+1]==1:
                    size+=1
                ans=max(ans,size+1)
        return ans  
        