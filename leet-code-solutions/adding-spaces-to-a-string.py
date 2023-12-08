class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        li=''
        j=0
        for i in spaces:
            li+=s[j:i]+' '
            j=i
        li+=s[j:]
        return li