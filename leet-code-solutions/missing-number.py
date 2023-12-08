class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total=sum(nums)
        x=0
        for i in range(len(nums)+1):
            x+=i
        return x-total
        