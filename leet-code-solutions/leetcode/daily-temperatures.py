class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        mono_stk=[0]
        ans=[0]* len(temperatures)
        for i in range(1,len(temperatures)):

            while mono_stk and temperatures[i]>temperatures[mono_stk[-1]] :
                ans[mono_stk[-1]]+=i-mono_stk[-1]
                mono_stk.pop()
            mono_stk.append(i)
        
        return ans





        