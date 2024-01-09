class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1)
        s1=''.join(sorted(s1))
        for i in range(len(s2)-n1+1):
            if s1 in ''.join(sorted(s2[i:i+n1])):
                return True
        return False