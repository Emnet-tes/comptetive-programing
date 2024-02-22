class Solution:
    def simplifyPath(self, path: str) -> str:
        stack=[]
        stack=path.split('/')
        print(stack)
        ans=[]
        for i,n in enumerate(stack):
            if n=='' or n=='.':
                continue
            elif n=='..':
                if len(ans)<2:
                    ans.clear()
                else:
                    ans.pop()
            else:
                ans.append(n)
        print(ans)
        if len(ans)==0:
            return '/'
        s=""      
        for i,n in enumerate(ans):
            if len(stack)>1 and i==len(stack)-1:
                break
            s+='/'+n
        return s