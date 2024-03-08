class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #the smallest divisor
        def helper(n):
            res=0

            for x in nums:
                res += math.ceil(x/n)
            
            return res
        low = 1
        high = max(nums)

        while low <= high:

            mid = (low+high)//2
            k = helper(mid)

            if k <= threshold:
                high = mid-1
            else:
                low = mid+1
        
        return low

        
        
        