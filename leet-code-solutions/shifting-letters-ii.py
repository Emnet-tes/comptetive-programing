class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        op=[0]*(len(s)+1)
         
        for i,j,k in shifts:
            if k==0:
                op[i]-=1
                op[j+1]+=1
            else :
                op[i]+=1
                op[j+1]-=1
        pre = 0
        for i in range(len(s)):
            pre += op[i]
            
            new_code = (((ord(s[i]) + pre) - 97) % 26) + 97
            s = s[:i] + chr(new_code) + s[i+1:]
        
        return s
        