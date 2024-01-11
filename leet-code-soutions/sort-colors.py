class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            index=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[index]:
                    index=j
            if index!=i:
                nums[index],nums[i]=nums[i],nums[index]