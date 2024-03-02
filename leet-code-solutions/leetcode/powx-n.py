class Solution:
    def myPow(self, x: float, n: int) -> float:
        def calculator(x,n):
           if x == 0: return 0
           if n == 0: return 1

           res=calculator(x,n//2)
           res*=res
           return x*res if n%2 else res
        ans=calculator(x,abs(n))
        return 1/ans if n<0 else ans
