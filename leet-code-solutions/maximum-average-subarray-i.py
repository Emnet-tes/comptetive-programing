class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cnt=sum(nums[:k])
        val=cnt
        for i in range(1,len(nums)-k+1):
            val=val-nums[i-1]+nums[i+k-1]
            cnt=max(val,cnt)
        return cnt/k