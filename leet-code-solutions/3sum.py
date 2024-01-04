class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans=set()
        for i in range(len(nums)):
            if nums[i]==nums[i-1] and nums[-1]!=0:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                x=nums[i]+nums[j]+nums[k]
                if x<0:
                    j+=1
                elif x>0:
                    k-=1
                else:
                    ans.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                    
        return ans
        