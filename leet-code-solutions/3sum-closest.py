class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        x=nums[0]+nums[1]+nums[-1]
        for i in range(len(nums)-2):
            j=i+1
            k=len(nums)-1
            while j<k:
                y=nums[i]+nums[j]+nums[k]
                if y==target:
                    return y
                if (abs(y-target)<abs(x-target)):
                    x=y
                if y>target:
                    k-=1
                else:
                    j+=1
        return x
