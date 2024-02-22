class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num=[]
        
        for i,n in enumerate(tokens):
            if (n=='+' or n=='-' or n=='/' or n=='*'):
                if n=='+':
                    first = num.pop()
                    second = num.pop()
                    num.append(int(first)+int(second))
                elif n=='-':
                    second = num.pop()
                    first = num.pop()
                    num.append(int(first)-int(second))
                elif n=='*':
                    second = num.pop()
                    first = num.pop()
                    num.append(int(first)*int(second))
                elif n=='/':
                    second = num.pop()
                    first = num.pop()
                    num.append(math.trunc(int(first)/int(second)))
            else:
                num.append(int(n))
        print(num)
        return num[0]
                    
                
