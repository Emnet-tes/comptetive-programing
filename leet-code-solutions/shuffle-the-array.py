class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first=[]
        second=[]
        shuffled=[]
        for i in range(len(nums)):
            if i<n:
                first.append(nums[i])
            else:
                second.append(nums[i])
        for i in range(len(nums)//2):
            shuffled.append(first[i])
            shuffled.append(second[i])
        return shuffled
        