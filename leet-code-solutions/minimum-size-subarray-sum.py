class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        start=0
        current=0
        minval=float('inf')
        for i in range(n):
            current+=nums[i]
            while current>=target:
                minval=min(minval,i+1-start)
                current-=nums[start]
                start+=1
        if minval!=float('inf'):
            return minval
        return 0