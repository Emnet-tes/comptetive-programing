class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        r1=0
        r2=0
        for i in range(len(num1)):
            r1=r1*10+ord(num1[i])-48
        for i in range(len(num2)):
            r2=r2*10+ord(num2[i])-48
        return str(r1*r2)