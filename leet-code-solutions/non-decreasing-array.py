class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        check=0
        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                continue
            elif check==1:
                return False
            else:
                if  nums[i+1]>=nums[abs(i-1)]  and check==0 :
                    nums[i]=nums[i+1]
                else:
                    nums[i+1]=nums[i]
            check+=1
        return True

        