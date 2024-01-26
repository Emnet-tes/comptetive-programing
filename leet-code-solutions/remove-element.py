class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right=len(nums)-1

        for left in range(len(nums)):

            if nums[left]==val:

                while nums[right]==val and left<right:
                    right-=1
                nums[left],nums[right]=nums[right],nums[left]

            if left==right and nums[left]==val:
                return right

            if left==right and nums[left]!=val:
                return 
                
        return right
