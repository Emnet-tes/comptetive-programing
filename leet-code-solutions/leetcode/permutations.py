class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(nums):
            ans=[]
            if len(nums)==1:
                return [copy.deepcopy(nums)]
            for i in range(len(nums)):
                temp=nums.pop(0)
                choice=helper(nums)
                
                for c in choice:
                    c.append(temp)
                nums.append(temp)
                ans.extend(choice)
            print(ans)
            return ans
        return helper(nums)
        