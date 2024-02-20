class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach=0

        for i in range(len(nums)):
            if i>reach or reach>=len(nums)-1:
                break
            reach=max(reach,i+nums[i])
        print(reach)
        return reach>=len(nums)-1
            

        