class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d=Counter(s)
        b=set()
        ans=[]
        for n in s:
            d[n]-=1
            if n not in b:
                while ans and ord(n)<ord(ans[-1]) and d[ans[-1]]!=0:
                    b.discard(ans[-1])
                    ans.pop()
                ans.append(n)
                b.add(n)
            
        return "".join(ans)
