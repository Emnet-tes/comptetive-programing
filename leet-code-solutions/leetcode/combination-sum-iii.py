class Solution:
    def combinationSum3(self, k: int, target: int) -> List[List[int]]:
        ans=[]
        bucket=[]
        s=set()
        def backtrack(idx):
            n=len(bucket)
            if sum(bucket)==target:
                y=sorted(bucket[::])
                x=tuple(y)
                if x not in s and n==k :
                    ans.append(y)
                    s.add(tuple(x))
                return
            if sum(bucket)>target:
                return
            val=None
            for i in range(idx,10):
                if i!=val:
                    bucket.append(i)
                    backtrack(i+1)
                    val=bucket.pop()
            return ans
        return backtrack(1)
        