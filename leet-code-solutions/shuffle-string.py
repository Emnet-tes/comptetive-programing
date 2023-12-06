class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t=["x" ]*len(s)
        slist=[]
        
        for j in range(len(s)):
            slist.append(s[j])

        for i in range(len(slist)):
            t[indices[i]]=slist[i]
        return "".join(t)