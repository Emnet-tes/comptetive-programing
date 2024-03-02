class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:

        def recur(i,j,turn):
            if i==j:
                if turn:
                    return [nums[i],0]
                else:
                    return [0,nums[i]]

            left=recur(i+1,j,not turn)
            right=recur(i,j-1,not turn)
            

            if turn:
                if nums[i]+left[0]-left[1]>nums[j]+right[0]-right[1]:
                    left[0]+=nums[i]
                    return left
                else:
                    right[0]+=nums[j]
                    return right

            else:
                if nums[i]+left[1]-left[0]>right[1]+nums[j]-right[0]:
                    left[1]+=nums[i]
                    return left
                else:
                    right[1]+=nums[j]
                    return right
        ans=recur(0,len(nums)-1,True)
        
        return ans[0]>=ans[1]


        