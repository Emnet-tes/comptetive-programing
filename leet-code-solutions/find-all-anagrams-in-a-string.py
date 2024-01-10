class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        k=len(p)
        boxp=defaultdict(int)
        cnt=[]
        for i in range(k):
            boxp[p[i]]+=1
        for i in range(len(s)-k+1):
            sub=s[i:i+k]
            subcount=Counter(sub)
            if boxp==subcount:
                cnt.append(i)
        return cnt
