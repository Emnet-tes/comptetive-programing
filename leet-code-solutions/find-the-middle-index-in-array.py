class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        forward=[]
        backward=[]
        ans=0
        for i in nums:
            ans+=i
            forward.append(ans)
        ans=0
        for i in range(len(nums)-1,-1,-1):
            ans+=nums[i]
            backward.append(ans)
        backward.reverse()
        print(backward)
        for i in range(len(forward)):
            if forward[i]==backward[i]:
                return i
        return -1
