class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=-1
        n=len(nums)
        for j in range(n):
            if nums[j]:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
        