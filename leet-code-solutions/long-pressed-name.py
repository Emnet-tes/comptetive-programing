class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i=0
        j=0
        while j<len(typed) :
            if   i<len(name) and name[i]==typed[j]:
                j+=1
                i+=1
            elif j > 0 and typed[j-1] == typed[j]:
                j += 1
            else:
                return False

        return i == len(name)