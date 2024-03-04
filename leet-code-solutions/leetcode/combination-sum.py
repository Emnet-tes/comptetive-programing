class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        bucket=[]
        def backtrack(idx):
            if sum(bucket)==target:
                ans.append(bucket[::])
                return
            if sum(bucket)>target:
                return
            for i in range(idx,len(candidates)):
                bucket.append(candidates[i])
                backtrack(i)
                bucket.pop()
            return ans
        return backtrack(0)
        