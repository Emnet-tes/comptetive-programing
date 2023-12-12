class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        li={}
        for i in range(len(nums)):
            y=target-nums[i]
            if y in li:
                return [li[y],i]
            else:
                li[nums[i]]=i
