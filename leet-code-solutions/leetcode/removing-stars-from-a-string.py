class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        ans=[]
        for n in s:
            stack.append(n)
        print(stack)
        for i,n in enumerate(stack):
            if n =='*' and len(ans)!=0:
                ans.pop()
            elif n!='*':
                ans.append(n)
        return (''.join(ans))

        