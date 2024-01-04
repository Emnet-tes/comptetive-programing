class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        cnt=0
        while i<j:
            x=nums[i]+nums[j]
            if x<k:
                i+=1
            elif x>k:
                j-=1
            else:
                cnt+=1
                i+=1
                j-=1
        return cnt

        