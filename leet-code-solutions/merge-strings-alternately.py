class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result=[]
        j=0
        i=0
        m=max(len(word1),len(word2))
        for _ in range(m):
            while i<len(word1)and j<len(word2):
                result.append(word1[i])
                result.append(word2[j])
                i+=1
                j+=1
            if i<len(word1):
                    result.append(word1[i])
                    i+=1
            elif j<len(word2):
                    result.append(word2[j])
                    j+=1
        return "".join(result)
        
