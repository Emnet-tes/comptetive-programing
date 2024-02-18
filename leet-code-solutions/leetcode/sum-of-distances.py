class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        left_cnt=defaultdict(int)
        left_index_sum=defaultdict(int)
        
        for i, c in enumerate(nums):
            ans[i]+=left_cnt[c]*i-left_index_sum[c]

            left_cnt[c]+=1
            left_index_sum[c]+=i

        right_cnt=defaultdict(int)
        right_index_sum=defaultdict(int)

        for i in range(len(nums)-1,-1,-1):
            c=nums[i]
            ans[i]+=right_index_sum[c]-right_cnt[c]*i

            right_cnt[c]+=1
            right_index_sum[c]+=i
        
        return ans
        
        