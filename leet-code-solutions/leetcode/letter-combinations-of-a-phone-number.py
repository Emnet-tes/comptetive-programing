class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d={ 2: "abc",3: "def",4: "ghi",5: "jkl",6: "mno",7: "pqrs",8: "tuv",
            9: "wxyz"}
        ans=[]
        bucket=[]
        def backtrc(idx):
            if idx==len(digits):
                ans.append(''.join(bucket))
                return
            for i in range(len(d[int(digits[idx])])):
                bucket.append(d[int(digits[idx])][i])
                backtrc(idx+1)
                bucket.pop()
            return ans
        return backtrc(0)

        