class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        size=0
        left=0
        box=defaultdict(int)
        for right in range(len(nums)):
            box[nums[right]]+=1
            while box[0]>1:
                box[nums[left]]-=1
                left+=1
            size=max(size,right-left)
        return size