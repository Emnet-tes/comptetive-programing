class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=-1
        right=len(nums)
        start=-1
        found=False
        while left+1 < right:
            mid = (left+right)//2
            if nums[mid]==target:
                found=True
            if nums[mid]>=target:
                right=mid
            elif nums[mid]<target:
                left=mid

        print(right,'st')
        if found:
            start=right
        
        
        left=-1
        right=len(nums)
        end=-1
        found=False
        while left+1 < right:
            mid = (left+right)//2
            if nums[mid]==target:
                found=True
            if nums[mid]<=target:
                left=mid
            else:
                right=mid
        print(left,'end',right)
        if found:
            end=left
        return [start,end]