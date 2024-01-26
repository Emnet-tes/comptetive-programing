class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left=0
        maximumScore=0
        occurenceKeeper=defaultdict(int)
        score=0
        for right in range(len(nums)):
            occurenceKeeper[nums[right]]+=1
            score+=nums[right]
            while occurenceKeeper[nums[right]]>1:
                occurenceKeeper[nums[left]]-=1
                score-=nums[left]
                left+=1
            maximumScore=max(maximumScore,score)
        return maximumScore