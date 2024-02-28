class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stk=[]
        ans=0
        mod=10**9+7
        for i,n in enumerate(arr):
            #make the stack strictly increasing
            while stk and arr[stk[-1]]>n:
                temp=stk.pop()
                if stk:
                    left=temp-stk[-1]
                else:
                    left=temp+1
                right=i-temp
                ans+=(left*right*arr[temp])
                ans%=mod
            stk.append(i)
        for i in range(len(stk)):
            if i>0:
                left=stk[i]-stk[i-1]
            else:
                left=stk[i]+1
            right=len(arr)-stk[i]
            ans+=(left*right*arr[stk[i]])
            ans%=mod
        return ans