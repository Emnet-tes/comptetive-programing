class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]
        current=0
        maxi_sum=nums[0]
        pre=0
        for i in range(1,len(nums)):
            current=nums[i]
            pre=maxi_sum+current
            maxi_sum=max(pre,current)
            ans=max(maxi_sum,ans)
        return ans
        
