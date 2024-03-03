class Solution:
    def decodeString(self, s: str) -> str:
        stk=[]
        for n in s:
            if n==']':
                word=''
                while stk and stk[-1]!='[':
                    word = stk.pop() + word
                stk.pop() #remove [
                
                num=''
                while stk and stk[-1].isdigit():
                    num = stk.pop() + num
                stk.append(int(num)*word)
            else:
                stk.append(n)
        return ''.join(stk)