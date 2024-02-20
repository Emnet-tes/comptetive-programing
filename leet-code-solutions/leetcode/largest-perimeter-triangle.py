class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        result=0
        nums.sort()
        if len(nums)<3:
            return 0
        if len(nums)==3:
            return sum(nums)
        check=0
        for i in range(len(nums)-2):
            check=nums[i]+nums[i+1]+nums[i+2]
            if nums[i]+nums[i+1]>nums[i+2]:
                result=max(result,check)
                check=0
        return result
