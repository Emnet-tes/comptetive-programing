class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        bucket=[]
        s=set()
        def backtrack(idx):
            if sum(bucket)==target:
                y=sorted(bucket[::])
                x=tuple(y)
                if x not in s:
                    ans.append(y)
                    s.add(tuple(x))
                return
            if sum(bucket)>target:
                return
            val=None
            for i in range(idx,len(candidates)):
                if candidates[i]!=val:
                    bucket.append(candidates[i])
                    backtrack(i+1)
                    val=bucket.pop()
            return ans
        return backtrack(0)
        