class Solution:
    def findMin(self, nums: List[int]) -> int:
        # minimum if the preveious elment is greater than it or there no elment
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)//2
            if nums[mid+1]<nums[mid]:
                return nums[mid+1]
            if nums[mid]<nums[mid-1]:
                return nums[mid]
            if nums[-1]>nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return nums[left]