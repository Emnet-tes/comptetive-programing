class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prx=defaultdict(int)
        cnt=0
        total=0
        for n in nums:
            total+=n
            if total-goal in prx: 
                cnt+=prx[total-goal]
            if total==goal:
                cnt+=1
            prx[total]+=1
        
        return cnt
