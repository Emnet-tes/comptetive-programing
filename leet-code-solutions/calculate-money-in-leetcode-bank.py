class Solution:
    def totalMoney(self, n: int) -> int:
        if n<8: 
            return sum(range(1,n+1)) 
        else: 
            ans=0 
            i=0 
            x=7 
            while n>0: 
                ans+=sum(range(i+1,x+1)) 
                if n-7 <7 : 
                    n-=7 
                    ans+=sum(range(i+2,n+i+2)) 
                    break 
                n-=7 
                i+=1 
                x+=1 
        return ans
        