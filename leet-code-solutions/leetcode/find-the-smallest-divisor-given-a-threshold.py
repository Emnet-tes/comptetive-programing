class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        #the smallest divisor
        def helper(n):
            res=0

            for x in nums:
                res += math.ceil(x/n)
            
            return res
        left = 1
        right = max(nums)

        while left <= right:

            mid = (left + right)//2
            k = helper(mid)

            if k <= threshold:
                right = mid-1
            else:
                left = mid+1
        
        return left

        
        
        