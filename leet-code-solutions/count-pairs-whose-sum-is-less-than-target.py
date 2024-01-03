class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        j=1
        count=0
        nums.sort()
        for i in range(len(nums)):
            j=i+1
            while j<(len(nums)):
                x=nums[i]+nums[j]
                if x<target:
                    count+=1
                j+=1
        return count