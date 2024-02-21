class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        total=0
        ans=0
        for i,n in enumerate(nums):
            total+=n
            x=((total+i)//(i+1))
            ans=max(ans,x)
        return ans

        