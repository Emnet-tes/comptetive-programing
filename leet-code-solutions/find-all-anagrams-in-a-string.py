class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        cnt=[]
        boxp=Counter(p)
        left=0
        sub=s[:k]
        subcount=Counter(sub)
        if boxp==subcount:
            cnt.append(0)
        
        for right in range(k,len(s)):
            subcount[s[left]]-=1
            subcount[s[right]]+=1
            if boxp==subcount:
                cnt.append(left+1)
            left+=1
            
        return cnt