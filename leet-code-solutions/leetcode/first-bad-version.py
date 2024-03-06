# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left=1
        right=n
        mid=0
        while left<=right:
            mid=(left+right)//2
            ans=isBadVersion(mid)
            if not ans:
                left=mid+1
            else:
                if not isBadVersion(mid-1):
                    return mid
                right=mid-1

        return right
