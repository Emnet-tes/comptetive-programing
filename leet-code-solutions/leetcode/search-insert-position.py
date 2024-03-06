class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        
        while left<=right:
            mid=(left+right)//2
            if nums[mid]<=target:
                left=mid+1
            else:
                right=mid-1

        if right<0:
            return 0

        if nums[right]<target:
            return right+1
        else:
            return right