class Solution:
    def isHappy(self, n: int) -> bool:
        li= set()
        r=0
        while n!=1 and n not in li :
            sum=0
            li.add(n)
            while n:
                r=n%10
                sum+=r*r
                n//=10
            n=sum
        return n==1
        