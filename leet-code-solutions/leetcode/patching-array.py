class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        cursum=0
        ans=0
        for x in nums:
            if x>n:
                break
            while x-1>cursum:
                cursum+=cursum+1
                ans+=1
            cursum+=x
        while n>cursum:
            cursum+=cursum+1
            ans+=1
        return ans