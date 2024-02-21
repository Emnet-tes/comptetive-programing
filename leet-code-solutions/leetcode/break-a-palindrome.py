class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        size=len(palindrome)
        pali_list=[]
        flag=True
        if size==1:#case 1
            return ""
        half=size//2
        sub=palindrome[:half+1]
        for i,m in enumerate(palindrome):
            pali_list.append(m)
            
        if pali_list[0]!='a': #case 2
            pali_list[0]='a'
            return "".join(pali_list)
        else:                   #case 3
            if pali_list.count('a')==size:
                pali_list[-1]='b'
                return "".join(pali_list)
            else:
                if sub.count('a')==half:
                    pali_list[-1]='b'
                    return "".join(pali_list)
                for i,n in enumerate(palindrome):
                    if n!='a':
                        pali_list[i]='a'
                        return "".join(pali_list)
       