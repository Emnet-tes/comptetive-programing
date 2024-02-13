class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        pre=[0]*(len(nums)+1)
        nums.sort(reverse=True)
        
        for x,y in requests:
            pre[x]+=1
            pre[y+1]-=1

        for i in range(1,len(pre)):
            pre[i]+=pre[i-1]
        pre.sort(reverse=True)
        ans=0
        for x,y in zip(pre,nums):
            ans+=x*y
        return ans%(10**9+7)
