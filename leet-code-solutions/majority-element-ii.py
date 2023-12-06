class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        li=[]
        for i in range(len(nums)):
            if nums.count(nums[i])>len(nums)//3 and nums[i] not in li:
                li.append(nums[i])
        return li

        