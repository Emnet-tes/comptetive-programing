class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num=1
        def reoccur(n,num,i):
            if num==n:
                return True
            if num>n:
                return False
            num=pow(3,i)
            print(num)
            return reoccur(n,num,i+1)
        return reoccur(n,num,0)
        