class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        li=set(nums)
        ans=0
        for i in range(len(nums)):
            count=0
            if nums[i]-1 not in li:
                while nums[i]+count in li:
                    count+=1
                ans=max(ans,count)
        return ans
            
        
        