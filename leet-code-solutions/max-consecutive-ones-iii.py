class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        ans=0
        left=0
        number=defaultdict(int)

        for right in range(len(nums)):

            number[nums[right]]+=1

            while number[0]>k :
                number[nums[left]]-=1
                left+=1
            ans=max(ans,right-left+1)
            
        return ans