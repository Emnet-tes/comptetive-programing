class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        bucket=[]
        s=set()
        def backtrack(idx):
            x=sorted(bucket[::])
            y=tuple(x)
            if y not in s:
                s.add(y)
                ans.append(x)
            if idx==len(nums):
                return
            for i in range(idx,len(nums)):
                bucket.append(nums[i])
                backtrack(i+1)
                bucket.pop()
            return ans
        
        return backtrack(0)
        