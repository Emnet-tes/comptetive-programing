class Solution:
    def sortSentence(self, s: str) -> str:
        s=list(map(str,s.split()) )    
        separet=defaultdict(int)
        for i in range(len(s)):
            separet[int(s[i][-1])]=s[i][:len(s[i])-1]
        ans=sorted(separet.keys())
        output=[]
        for answer in ans:
            output.append(separet[answer])
        return " ".join(output)
