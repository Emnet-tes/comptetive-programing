class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good=0
        mydic={}
        for i in range(len(nums)):
            mydic[nums[i]]=nums.count(nums[i])
        for x in mydic:
            good += (mydic[x]*(mydic[x]-1))//2
        return good
           