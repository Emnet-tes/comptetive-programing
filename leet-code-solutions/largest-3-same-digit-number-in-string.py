class Solution:
    def largestGoodInteger(self, num: str) -> str:
        size=0
        ans=0
        n=9
        while n>=0:
            j=f'{n}'
            take=j+j+j
            print(take)
            if take in num:
                return take
            else:
                n-=1
        return ""

        