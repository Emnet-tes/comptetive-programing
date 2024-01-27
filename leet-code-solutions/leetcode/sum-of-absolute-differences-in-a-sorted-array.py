class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        pre=[]
        suff=[]
        front=0
        for n in nums:
            front+=n
            pre.append(front)
        back=0
        rever = list(reversed(nums))  
        for m in rever:
            back+=m
            suff.append(back)
        suff.reverse()
        ans=[]
        print(pre,suff)
        for i in range(len(nums)):
            left=(nums[i]*i)-pre[i]
            right=suff[i]-(nums[i]*(len(nums)-i-1))
            ans.append(left+right)
        return ans 
