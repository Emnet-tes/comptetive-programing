class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=defaultdict(int)
        ans=0

        for n in s:
            d[n]+=1
        odd=0
        odd_count=0

        for m in d.keys():
            if  d[m]%2!=0 :
                odd+=d[m]
                odd_count+=1
            else:
                ans+=d[m]
        
        if odd:
            ans+=odd-odd_count+1
        return ans
            