class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        val=0
        left=0
        right=2**(n-1)
        for _ in range(n-1):
            mid=(left+right)//2
            if k<=mid:
                right=mid
            elif k>mid:
                left=mid+1
                if val:
                    val=0
                else:
                    val=1
        return val