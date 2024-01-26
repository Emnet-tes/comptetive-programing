class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre_product=1
        zero_count=0
        ans=[]
        for n in nums:
            if n!=0:
                pre_product*=n
            else:
                zero_count+=1

        for n in nums:
            if zero_count==0   :
                ans.append(pre_product//n)

            elif zero_count>1 :
                ans.append(0)

            elif (zero_count==1 and n==0) :
                ans.append(pre_product)

            else:
                ans.append(0)
                
        return ans