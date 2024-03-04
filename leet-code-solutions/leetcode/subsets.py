class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        bucket=[]
        ans=[]
        def backtrc(idx):
            ans.append(bucket[::])
            for i in range(idx,len(nums)):
                bucket.append(nums[i])
                backtrc(i+1)
                bucket.pop()
        backtrc(0)
        return ans