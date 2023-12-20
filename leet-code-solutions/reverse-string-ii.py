class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        string_Box=list(s)
        for i in range(0,len(s),2*k):
            string_Box[i:i+k]=reversed(s[i:i+k])
        return "".join(string_Box)
        