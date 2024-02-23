class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        mono=[]
        ans=[]
        i=0
        while i<len(nums):
            while mono and nums[mono[-1]] < nums[i]:
                mono.pop()
            mono.append(i)
            if i-mono[0]==k:
                mono.pop(0)
            if i>=k-1:
                ans.append(nums[mono[0]])
            i+=1
        return ans