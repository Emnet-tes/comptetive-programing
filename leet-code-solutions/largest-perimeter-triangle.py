class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        check=0
        result=0
        if len(nums)==3 and sum(nums)!=0:
            return sum(nums)
        else:
            for i in range(len(nums)-2):
                check=nums[i]+nums[i+1]+nums[i+2]
                if nums[i]+nums[i+1]>nums[i+2]:
                    result=max(result,check)
                    check=0
        return result