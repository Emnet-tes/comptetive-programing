class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total=[]
        t=0
        for i in range(len(nums)):
            t+=nums[i]
            total.append(t)
        return total