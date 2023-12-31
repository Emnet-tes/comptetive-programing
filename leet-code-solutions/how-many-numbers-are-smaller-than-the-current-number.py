class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smallcounter=defaultdict(int)
        sortnumber=sorted(nums)
        for i in range(len(nums)):
            if sortnumber[i] not in smallcounter.keys():
                smallcounter[sortnumber[i]]=i
        ans=[]
        for i in range(len(nums)):
            ans.append(smallcounter[nums[i]])
        return ans
        