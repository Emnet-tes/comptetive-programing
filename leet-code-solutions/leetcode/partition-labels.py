class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = defaultdict(int)

        for i,n in enumerate(s):
            last_index[n] = i

        maxi=last_index[s[0]]
        partion=0
        ans=[]
        i=0
        
        while i < len(s):
            maxi = max(maxi,last_index[s[i]])
            if i == maxi:
                if ans:
                    ans.append(i-partion)
                    partion=i
                else:
                    ans.append(i+1)
                    partion=i
                if i<len(s)-1:
                    maxi = last_index[s[i+1]]
            i += 1
        return ans



            
        