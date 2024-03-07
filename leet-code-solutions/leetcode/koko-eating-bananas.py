class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #in one hour how many bananas should to finish in h

        def helper(n):
            res=0

            for x in piles:
                res += math.ceil(x/n)
            
            return res
        low = 1
        high = max(piles)

        while low <= high:

            mid = (low+high)//2
            k = helper(mid)

            if k <= h:
                high = mid-1
            else:
                low = mid+1
        
        return low

        
        
        