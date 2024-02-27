class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        ans=[-1]*len(nums)
        two_nums=[]
        stk=[]

        for i in range(2*len(nums)):
            two_nums.append(nums[i%len(nums)])

        for i,n in enumerate(two_nums):
            # make it strictly decreasing
            while stk and nums[stk[-1]]<n:
               ans[stk[-1]]=n
               stk.pop()
            stk.append(i%len(nums))
        return ans