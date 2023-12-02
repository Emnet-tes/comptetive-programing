class Solution:
    def romanToInt(self, s: str) -> int:
        mydict={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        result=0
        for i in range(len(s)-1):
            if mydict[s[i]]<mydict[s[i+1]]:
                result-=mydict[s[i]]
            else:
                result+=mydict[s[i]]
        return result+mydict[s[-1]]
        
        