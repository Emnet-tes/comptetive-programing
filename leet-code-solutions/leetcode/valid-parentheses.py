class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        flag=True
        for n in s:
            if n=='(' or n=='[' or n=='{':
                stack.append(n)
                flag=False
            else:
                if len(stack)!=0:
                    if n==')' and stack[-1]=='(':
                        flag=True
                        stack.pop()
                    elif n==']' and stack[-1]=='[':
                        flag=True
                        stack.pop()
                    elif n=='}' and stack[-1]=='{':
                        flag=True
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return flag if len(stack)==0 else False
