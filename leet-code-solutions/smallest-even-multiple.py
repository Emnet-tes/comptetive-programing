class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        x=n*2
        if n%2==0:
           return min(x,n)
        else:
           return x
        
        