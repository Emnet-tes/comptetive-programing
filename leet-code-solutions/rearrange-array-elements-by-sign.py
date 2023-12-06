class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive=[]
        negative=[]
        ordered=[]
        for i in range(len(nums)):
            if nums[i]>=0:
                postive.append(nums[i])
            else:
                negative.append(nums[i])
        for i in range(len(nums)//2):
            ordered.append(postive[i])
            ordered.append(negative[i])
        return ordered

        