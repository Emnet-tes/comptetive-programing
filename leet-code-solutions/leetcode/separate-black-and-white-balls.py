class Solution:
    def minimumSteps(self, s: str) -> int:
        cnt=0
        ans=0
        for c in s:
            if c=='1':
                cnt+=1
            else:
                ans+=cnt
        return ans