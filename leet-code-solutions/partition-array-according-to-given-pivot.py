class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        li=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                li.append(nums[i])
        for i in range(len(nums)):
            if nums[i]==pivot:
                li.append(nums[i])
        for i in range(len(nums)):
            if nums[i]>pivot:
                li.append(nums[i])
        return li
        