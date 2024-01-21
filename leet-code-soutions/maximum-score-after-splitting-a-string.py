class Solution:
    def maxScore(self, s: str) -> int:
        pre=s.count('1',1)
        if s[0]=='0':
            pre+=1
        res=pre
        for j in range(1,len(s)-1):
            if s[j]=='0':
                pre+=1
            else:
                pre-=1
            res=max(res,pre)
        return  res